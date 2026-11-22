"""
Fluvio — 30-Day Rolling SQLite Time-Series Persistence Layer (Standard Library Python 3)

Stores hourly hydrological & meteorological snapshots across all registered countries
(400 stations x 8 lead days + 37 catchments x 8 forecast days per snapshot) in a
compact, WAL-enabled, indexed SQLite database for downstream hydrological modeling,
forecast skill verification, and ML retraining.
"""

import datetime
import os
import sqlite3
import threading
import time

DEFAULT_DB_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data",
    "fluvio_history.sqlite",
)
DB_PATH = os.environ.get("FLUVIO_DB_PATH") or os.environ.get("WVIS_DB_PATH", DEFAULT_DB_PATH)
RETENTION_DAYS = int(os.environ.get("FLUVIO_RETENTION_DAYS") or os.environ.get("WVIS_RETENTION_DAYS", 30))

_DB_LOCK = threading.Lock()


def _connect(db_path: str = DB_PATH) -> sqlite3.Connection:
    parent = os.path.dirname(os.path.abspath(db_path))
    if parent:
        os.makedirs(parent, exist_ok=True)
    conn = sqlite3.connect(db_path, timeout=15.0)
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA synchronous=NORMAL;")
    conn.execute("PRAGMA foreign_keys=ON;")
    return conn


def init_db(db_path: str = DB_PATH) -> None:
    """Initializes the SQLite schema and indexes if not already present."""
    with _DB_LOCK:
        conn = _connect(db_path)
        try:
            conn.executescript(
                """
                CREATE TABLE IF NOT EXISTS snapshots (
                    snapshot_ts INTEGER PRIMARY KEY,
                    generated_at TEXT NOT NULL,
                    observation_date TEXT NOT NULL,
                    total_stations INTEGER NOT NULL,
                    live_matched INTEGER NOT NULL,
                    official_forecasts INTEGER NOT NULL
                );

                CREATE TABLE IF NOT EXISTS sources (
                    source_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    source_name TEXT UNIQUE NOT NULL
                );

                CREATE TABLE IF NOT EXISTS station_observations (
                    snapshot_ts INTEGER NOT NULL,
                    station_code TEXT NOT NULL,
                    country TEXT NOT NULL,
                    lead_day INTEGER NOT NULL,
                    target_date TEXT NOT NULL,
                    level_cm INTEGER NOT NULL,
                    uncertainty_cm INTEGER NOT NULL,
                    delta_from_today_cm INTEGER NOT NULL,
                    daily_change_cm INTEGER NOT NULL,
                    discharge_m3s REAL,
                    water_temp_c REAL,
                    precip_mm REAL,
                    cum_precip_mm REAL,
                    temp_max_c REAL,
                    temp_min_c REAL,
                    wind_kmh REAL,
                    alert_level TEXT NOT NULL,
                    source_id INTEGER,
                    PRIMARY KEY (snapshot_ts, station_code, lead_day)
                ) WITHOUT ROWID;

                CREATE INDEX IF NOT EXISTS idx_station_obs_code_ts
                    ON station_observations (station_code, snapshot_ts, lead_day);

                CREATE TABLE IF NOT EXISTS catchment_weather (
                    snapshot_ts INTEGER NOT NULL,
                    catchment_id TEXT NOT NULL,
                    forecast_date TEXT NOT NULL,
                    precip_mm REAL,
                    temp_max_c REAL,
                    temp_min_c REAL,
                    et0_mm REAL,
                    wind_kmh REAL,
                    PRIMARY KEY (snapshot_ts, catchment_id, forecast_date)
                ) WITHOUT ROWID;
                """
            )
            conn.commit()
        finally:
            conn.close()


def save_snapshot(payload: dict, db_path: str = DB_PATH, retention_days: int = RETENTION_DAYS) -> dict:
    """Persists one hydrological+weather snapshot and prunes records older than retention_days."""
    snapshot_ts = int(time.time())
    meta = payload.get("meta", {})
    stations = payload.get("stations", [])
    catchments = payload.get("catchments", {})

    with _DB_LOCK:
        conn = _connect(db_path)
        try:
            cur = conn.cursor()

            # Resolve / intern source strings to compact integer IDs
            source_names = {
                tl.get("source", "")
                for st in stations
                for tl in st.get("timeline", [])
                if tl.get("source")
            }
            if source_names:
                cur.executemany(
                    "INSERT OR IGNORE INTO sources (source_name) VALUES (?)",
                    [(name,) for name in source_names],
                )
            source_map = dict(cur.execute("SELECT source_name, source_id FROM sources").fetchall())

            cur.execute(
                """
                INSERT OR REPLACE INTO snapshots
                    (snapshot_ts, generated_at, observation_date, total_stations, live_matched, official_forecasts)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    snapshot_ts,
                    meta.get("generated_at", ""),
                    meta.get("observation_date", ""),
                    int(meta.get("total_stations", len(stations))),
                    int(meta.get("live_hydroinfo_matched", 0)),
                    int(meta.get("official_ovf_forecast_stations", 0)),
                ),
            )

            st_rows = []
            for st in stations:
                code = st["code"]
                country = st.get("country", "HU")
                water_temp = st.get("water_temp_c")
                for tl in st.get("timeline", []):
                    st_rows.append(
                        (
                            snapshot_ts,
                            code,
                            country,
                            int(tl["day"]),
                            tl["date"],
                            int(tl["level_cm"]),
                            int(tl["uncertainty_cm"]),
                            int(tl["delta_from_today_cm"]),
                            int(tl["daily_change_cm"]),
                            tl.get("discharge_m3s"),
                            water_temp,
                            tl.get("precip_mm"),
                            tl.get("cum_precip_mm"),
                            tl.get("temp_max_c"),
                            tl.get("temp_min_c"),
                            tl.get("wind_kmh"),
                            tl.get("alert_level", "normal"),
                            source_map.get(tl.get("source", "")),
                        )
                    )

            cur.executemany(
                """
                INSERT OR REPLACE INTO station_observations VALUES
                    (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                st_rows,
            )

            cw_rows = []
            for cid, cobj in catchments.items():
                for w in cobj.get("weather", []):
                    cw_rows.append(
                        (
                            snapshot_ts,
                            cid,
                            w["date"],
                            w.get("precip_mm"),
                            w.get("temp_max_c"),
                            w.get("temp_min_c"),
                            w.get("et0_mm"),
                            w.get("wind_kmh"),
                        )
                    )

            cur.executemany(
                """
                INSERT OR REPLACE INTO catchment_weather VALUES
                    (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                cw_rows,
            )

            # Enforce rolling retention window (default 30 days)
            cutoff_ts = snapshot_ts - int(retention_days) * 86400
            cur.execute("DELETE FROM station_observations WHERE snapshot_ts < ?", (cutoff_ts,))
            cur.execute("DELETE FROM catchment_weather WHERE snapshot_ts < ?", (cutoff_ts,))
            cur.execute("DELETE FROM snapshots WHERE snapshot_ts < ?", (cutoff_ts,))

            conn.commit()
        finally:
            conn.close()

    return get_db_stats(db_path=db_path, retention_days=retention_days)


def get_db_stats(db_path: str = DB_PATH, retention_days: int = RETENTION_DAYS) -> dict:
    """Returns current SQLite database statistics and disk usage."""
    if not os.path.exists(db_path):
        return {
            "db_path": db_path,
            "retention_days": retention_days,
            "snapshots_count": 0,
            "station_rows": 0,
            "catchment_rows": 0,
            "oldest_snapshot_at": None,
            "newest_snapshot_at": None,
            "db_size_bytes": 0,
        }

    with _DB_LOCK:
        conn = _connect(db_path)
        try:
            snaps, min_ts, max_ts = conn.execute(
                "SELECT COUNT(*), MIN(snapshot_ts), MAX(snapshot_ts) FROM snapshots"
            ).fetchone()
            st_rows = conn.execute("SELECT COUNT(*) FROM station_observations").fetchone()[0]
            cw_rows = conn.execute("SELECT COUNT(*) FROM catchment_weather").fetchone()[0]
        finally:
            conn.close()

    def _fmt_ts(ts):
        if not ts:
            return None
        return datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")

    total_bytes = 0
    for suffix in ("", "-wal", "-shm"):
        p = db_path + suffix
        if os.path.exists(p):
            total_bytes += os.path.getsize(p)

    return {
        "db_path": db_path,
        "retention_days": retention_days,
        "snapshots_count": snaps or 0,
        "station_rows": st_rows or 0,
        "catchment_rows": cw_rows or 0,
        "oldest_snapshot_at": _fmt_ts(min_ts),
        "newest_snapshot_at": _fmt_ts(max_ts),
        "db_size_bytes": total_bytes,
    }


def query_station_history(
    station_code: str,
    hours: int = 720,
    lead_day: int = 0,
    db_path: str = DB_PATH,
) -> dict:
    """Fetches historical time-series observations/forecasts for one station for model calculations."""
    hours = max(1, min(int(hours), 24 * 90))
    cutoff_ts = int(time.time()) - hours * 3600

    with _DB_LOCK:
        conn = _connect(db_path)
        try:
            if lead_day is None:
                rows = conn.execute(
                    """
                    SELECT o.snapshot_ts, s.generated_at, o.lead_day, o.target_date,
                           o.level_cm, o.uncertainty_cm, o.delta_from_today_cm, o.daily_change_cm,
                           o.discharge_m3s, o.water_temp_c, o.precip_mm, o.cum_precip_mm,
                           o.temp_max_c, o.temp_min_c, o.wind_kmh, o.alert_level, src.source_name
                    FROM station_observations o
                    JOIN snapshots s ON s.snapshot_ts = o.snapshot_ts
                    LEFT JOIN sources src ON src.source_id = o.source_id
                    WHERE o.station_code = ? AND o.snapshot_ts >= ?
                    ORDER BY o.snapshot_ts ASC, o.lead_day ASC
                    """,
                    (station_code, cutoff_ts),
                ).fetchall()
            else:
                rows = conn.execute(
                    """
                    SELECT o.snapshot_ts, s.generated_at, o.lead_day, o.target_date,
                           o.level_cm, o.uncertainty_cm, o.delta_from_today_cm, o.daily_change_cm,
                           o.discharge_m3s, o.water_temp_c, o.precip_mm, o.cum_precip_mm,
                           o.temp_max_c, o.temp_min_c, o.wind_kmh, o.alert_level, src.source_name
                    FROM station_observations o
                    JOIN snapshots s ON s.snapshot_ts = o.snapshot_ts
                    LEFT JOIN sources src ON src.source_id = o.source_id
                    WHERE o.station_code = ? AND o.snapshot_ts >= ? AND o.lead_day = ?
                    ORDER BY o.snapshot_ts ASC
                    """,
                    (station_code, cutoff_ts, int(lead_day)),
                ).fetchall()
        finally:
            conn.close()

    return {
        "station_code": station_code,
        "hours": hours,
        "lead_day": lead_day,
        "count": len(rows),
        "records": [
            {
                "snapshot_ts": r[0],
                "captured_at": r[1],
                "lead_day": r[2],
                "target_date": r[3],
                "level_cm": r[4],
                "uncertainty_cm": r[5],
                "delta_from_today_cm": r[6],
                "daily_change_cm": r[7],
                "discharge_m3s": r[8],
                "water_temp_c": r[9],
                "precip_mm": r[10],
                "cum_precip_mm": r[11],
                "temp_max_c": r[12],
                "temp_min_c": r[13],
                "wind_kmh": r[14],
                "alert_level": r[15],
                "source": r[16],
            }
            for r in rows
        ],
    }


def list_recent_snapshots(limit: int = 48, db_path: str = DB_PATH) -> list:
    """Lists recent captured snapshots from the SQLite archive."""
    limit = max(1, min(int(limit), 720))
    with _DB_LOCK:
        conn = _connect(db_path)
        try:
            rows = conn.execute(
                """
                SELECT snapshot_ts, generated_at, observation_date,
                       total_stations, live_matched, official_forecasts
                FROM snapshots
                ORDER BY snapshot_ts DESC
                LIMIT ?
                """,
                (limit,),
            ).fetchall()
        finally:
            conn.close()

    return [
        {
            "snapshot_ts": r[0],
            "generated_at": r[1],
            "observation_date": r[2],
            "total_stations": r[3],
            "live_matched": r[4],
            "official_forecasts": r[5],
        }
        for r in rows
    ]
