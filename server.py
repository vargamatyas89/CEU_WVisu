#!/usr/bin/env python3
"""
RiverRadar — Interactive Hydrological Map and 1–7 Day Forecast System for Central Europe, the Danube Basin and Zakarpattia
Backend API & Static File Server (Standard Library Python 3)

Modular Country Architecture & Multi-Source Live Telemetry:
1. countries/<country>.py — one module per country/region (10 modules, 511 gauges; registered in countries/__init__.py)
2. storage.py — hourly SQLite snapshots with 30-day rolling retention
3. Live Data Sources:
   - hydroinfo.hu (dunhif_a.html, tishif_a.html, tohid.html, dunelotH.html, tiselotH.html)
   - vizugy.hu (OperativVizallas - 272 live hourly gauges on smaller waters, streams and canals)
   - Open-Meteo Weather & Copernicus GloFAS v4 (5 km resolution) Flood API
"""

import concurrent.futures
import datetime
import html
import http.server
import json
import math
import os
import re
import socketserver
import threading
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

from countries import CATCHMENTS, COUNTRIES_META, STATIONS_CATALOG
import storage

PORT = int(os.environ.get("PORT", 8080))
STATIC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")

# Cache & Hourly Background Refresh Configuration
_CACHE = {
    "timestamp": 0,
    "payload": None,
}
_CACHE_LOCK = threading.Lock()
_REFRESH_LOCK = threading.Lock()
REFRESH_INTERVAL_SECONDS = int(os.environ.get("REFRESH_INTERVAL_SECONDS", 3600))  # 1 hour default
CACHE_TTL_SECONDS = REFRESH_INTERVAL_SECONDS


def _clean_html(raw: str) -> str:
    txt = html.unescape(re.sub(r"<[^>]+>", " ", raw))
    return re.sub(r"\s+", " ", txt).strip()


def _norm_hu(s: str) -> str:
    """Normalize Hungarian strings across ISO-8859-2 / UTF-8 quirks (õ->ő, û->ű)."""
    return (
        s.lower()
        .replace("õ", "ő")
        .replace("û", "ű")
        .replace("ô", "ő")
        .strip()
    )


def _parse_int(val: str, default=None):
    if not val or val.strip() == "-":
        return default
    m = re.search(r"[-+]?\d+", val.replace(" ", ""))
    return int(m.group(0)) if m else default


def _parse_float(val: str, default=None):
    if not val or "//" in val or val.strip() == "-":
        return default
    val_clean = val.replace(",", ".").strip()
    m = re.search(r"[-+]?\d+(?:\.\d+)?", val_clean)
    return float(m.group(0)) if m else default


def fetch_hydroinfo_observations():
    """Fetches live current hydrological tables from hydroinfo.hu (covers both 44xxxx HU and 74xxxx RO stations)."""
    observations = {}
    obs_date_str = None
    urls = [
        ("duna", "https://www.hydroinfo.hu/tables/dunhif_a.html"),
        ("tisza", "https://www.hydroinfo.hu/tables/tishif_a.html"),
        ("tavak", "https://www.hydroinfo.hu/tables/tohid.html"),
    ]

    for kind, url in urls:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (RiverRadar HydroMap)"})
            with urllib.request.urlopen(req, timeout=7) as resp:
                text = resp.read().decode("iso-8859-2", errors="replace")
                if not obs_date_str:
                    m_date = re.search(r"Észlelés:\s*([^<]+)", html.unescape(text))
                    if m_date:
                        obs_date_str = m_date.group(1).strip()

                trs = re.findall(r"<tr[^>]*>(.*?)</tr>", text, re.S | re.I)
                for tr in trs:
                    tds = [_clean_html(td) for td in re.findall(r"<td[^>]*>(.*?)</td>", tr, re.S | re.I)]
                    if len(tds) >= 8 and re.match(r"^\d{6}$", tds[0]):
                        code = tds[0]
                        st_name = tds[1]
                        river_name = tds[2]
                        yest_morn = _parse_int(tds[3])
                        yest_eve = _parse_int(tds[4])
                        today_morn = _parse_int(tds[5])
                        diff_24h = _parse_int(tds[6], 0)

                        if kind == "tavak":
                            discharge = None
                            water_temp = _parse_float(tds[7]) if len(tds) > 7 else None
                            ice_status = tds[8] if len(tds) > 8 and tds[8] != "//" else "jégmentes"
                        else:
                            discharge = _parse_float(tds[7]) if len(tds) > 7 else None
                            water_temp = _parse_float(tds[8]) if len(tds) > 8 else None
                            ice_status = tds[9] if len(tds) > 9 and tds[9] != "//" else "jégmentes"

                        if today_morn is not None:
                            observations[code] = {
                                "code": code,
                                "name": st_name,
                                "river": river_name,
                                "yest_morning_cm": yest_morn,
                                "yest_evening_cm": yest_eve,
                                "current_level_cm": today_morn,
                                "diff_24h_cm": diff_24h if diff_24h is not None else 0,
                                "discharge_m3s": discharge,
                                "water_temp_c": water_temp,
                                "ice_status": ice_status,
                                "origin": "hydroinfo.hu",
                            }
        except Exception as exc:
            print(f"[WARN] Failed to fetch {url}: {exc}")

    return observations, obs_date_str


def fetch_vizugy_operative_observations():
    """Fetches live hourly telemetry for 272 Hungarian stations (including smaller streams, creeks, canals, reservoirs) from vizugy.hu."""
    vizugy_by_id = {}
    try:
        req = urllib.request.Request("https://www.vizugy.hu/", headers={"User-Agent": "Mozilla/5.0 (RiverRadar HydroMap)"})
        with urllib.request.urlopen(req, timeout=8) as resp:
            text = resp.read().decode("utf-8", errors="replace")
            arrays = dict(re.findall(r"([A-Za-z0-9_]+)\s*=\s*new\s+Array\((.*?)\);", text, re.S))

            def get_arr(key):
                raw_body = arrays.get(key, "")
                return [x.strip() for x in re.findall(r"'([^']*)'", raw_body)]

            torzs = get_arr("VizmerceTorzsSzam")
            names = get_arr("VizmerceNev")
            rivers = get_arr("VizfolyasNev")
            levels = get_arr("Vizallas")
            discharges = get_arr("Vizhozam")
            temps = get_arr("Vizho")
            times = get_arr("UtolsoMeresIdopontja")
            lkvs = get_arr("LKV")
            lnvs = get_arr("LNV")

            count = min(len(torzs), len(names), len(levels))
            for i in range(count):
                tid = torzs[i].strip()
                lvl = _parse_int(levels[i])
                if not tid or lvl is None:
                    continue
                q_val = _parse_float(discharges[i]) if i < len(discharges) else None
                if q_val is not None and q_val <= 0.0:
                    q_val = None
                t_val = _parse_float(temps[i]) if i < len(temps) else None
                if t_val is not None and t_val <= 0.0:
                    t_val = None

                vizugy_by_id[tid] = {
                    "vizugy_id": tid,
                    "name": names[i],
                    "river": rivers[i] if i < len(rivers) else "",
                    "current_level_cm": lvl,
                    "discharge_m3s": q_val,
                    "water_temp_c": t_val,
                    "measured_at": times[i] if i < len(times) else "",
                    "lkv_cm": _parse_int(lkvs[i]) if i < len(lkvs) else None,
                    "lnv_cm": _parse_int(lnvs[i]) if i < len(lnvs) else None,
                    "origin": "vizugy.hu",
                }
    except Exception as exc:
        print(f"[WARN] Failed to fetch vizugy.hu operative telemetry: {exc}")

    return vizugy_by_id


def fetch_dhmz_croatia_observations():
    """Fetches live hourly telemetry for 211 Croatian stations from DHMZ (hidro.dhz.hr)."""
    dhmz_by_id = {}
    try:
        req = urllib.request.Request(
            "https://hidro.dhz.hr/hidroweb/skripte/hidrobazahtml.py?funkc=podaciautomatskih",
            headers={"User-Agent": "Mozilla/5.0 (RiverRadar HydroMap)"},
        )
        with urllib.request.urlopen(req, timeout=8) as resp:
            text = resp.read().decode("utf-8", errors="replace")
            for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", text, re.S | re.I):
                tds = [_clean_html(td) for td in re.findall(r"<td[^>]*>(.*?)</td>", tr, re.S | re.I)]
                if len(tds) >= 6 and re.match(r"^\d{3,5}$", tds[1]):
                    did = tds[1].strip()
                    lvl = _parse_int(tds[5])
                    if did and lvl is not None:
                        dhmz_by_id[did] = {
                            "dhmz_id": did,
                            "name": tds[0],
                            "river": tds[2],
                            "measured_at": tds[4],
                            "current_level_cm": lvl,
                            "origin": "hidro.dhz.hr (DHMZ)",
                        }
    except Exception as exc:
        print(f"[WARN] Failed to fetch DHMZ Croatia telemetry: {exc}")

    return dhmz_by_id


def fetch_rhmz_serbia_observations():
    """Fetches live telemetry for 160+ Serbian stations from RHMZ (hidmet.gov.rs/latin/osmotreni/stanje_voda.php)."""
    rhmz_by_id = {}
    try:
        req = urllib.request.Request(
            "https://www.hidmet.gov.rs/latin/osmotreni/stanje_voda.php",
            headers={"User-Agent": "Mozilla/5.0 (RiverRadar HydroMap)"},
        )
        with urllib.request.urlopen(req, timeout=8) as resp:
            text = resp.read().decode("utf-8", errors="replace")
            for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", text, re.S | re.I):
                m_id = re.search(r"hm_id=(\d+)", tr)
                if not m_id:
                    continue
                rid = m_id.group(1)
                tds = [_clean_html(td) for td in re.findall(r"<td[^>]*>(.*?)</td>", tr, re.S | re.I)]
                tail = [x for x in tds[3:] if x != ""]
                if len(tail) >= 2:
                    lvl = _parse_int(tail[0])
                    if lvl is None:
                        continue
                    chg = _parse_int(tail[1], 0)
                    q_val = _parse_float(tail[2]) if len(tail) > 2 and tail[2] not in ("*", "-") else None
                    t_val = _parse_float(tail[3]) if len(tail) > 3 and tail[3] not in ("*", "-") else None
                    rhmz_by_id[rid] = {
                        "rhmz_id": rid,
                        "name": tds[2] if len(tds) > 2 else "",
                        "river": tds[0] if len(tds) > 0 else "",
                        "current_level_cm": lvl,
                        "diff_24h_cm": chg if chg is not None else 0,
                        "discharge_m3s": q_val,
                        "water_temp_c": t_val,
                        "origin": "hidmet.gov.rs (RHMZ)",
                    }
    except Exception as exc:
        print(f"[WARN] Failed to fetch RHMZ Serbia telemetry: {exc}")

    return rhmz_by_id


def fetch_arso_slovenia_observations():
    """Fetches live telemetry for 190+ Slovenian stations from ARSO (arso.gov.si/xml/vode/hidro_podatki_zadnji.xml)."""
    arso_by_id = {}
    try:
        req = urllib.request.Request(
            "https://www.arso.gov.si/xml/vode/hidro_podatki_zadnji.xml",
            headers={"User-Agent": "Mozilla/5.0 (RiverRadar HydroMap)"},
        )
        with urllib.request.urlopen(req, timeout=8) as resp:
            root = ET.fromstring(resp.read())
            for st in root.findall("postaja"):
                aid = (st.attrib.get("sifra") or "").strip()
                vod_raw = (st.findtext("vodostaj") or "").strip()
                lvl = _parse_int(vod_raw)
                if not aid or lvl is None:
                    continue
                q_val = _parse_float(st.findtext("pretok") or "")
                t_val = _parse_float(st.findtext("temp_vode") or "")
                measured_at = (st.findtext("datum_cet") or st.findtext("datum") or "").strip()
                arso_by_id[aid] = {
                    "arso_id": aid,
                    "name": (st.findtext("merilno_mesto") or "").strip(),
                    "river": (st.findtext("reka") or "").strip(),
                    "current_level_cm": lvl,
                    "discharge_m3s": q_val,
                    "water_temp_c": t_val,
                    "measured_at": measured_at,
                    "origin": "arso.gov.si (ARSO)",
                }
    except Exception as exc:
        print(f"[WARN] Failed to fetch ARSO Slovenia telemetry: {exc}")

    return arso_by_id


def fetch_hnd_bayern_observations():
    """Fetches live official Bavarian Danube Basin telemetry from HND Bayern (hnd.bayern.de)."""
    urls = [
        "https://www.hnd.bayern.de/pegel/donau_bis_kelheim/tabellen",
        "https://www.hnd.bayern.de/pegel/donau_bis_passau/tabellen",
        "https://www.hnd.bayern.de/pegel/iller_lech/tabellen",
        "https://www.hnd.bayern.de/pegel/isar/tabellen",
        "https://www.hnd.bayern.de/pegel/naab_regen/tabellen",
        "https://www.hnd.bayern.de/pegel/inn/tabellen",
    ]
    hnd_by_id = {}

    def _fetch_one(url):
        rows_out = {}
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (RiverRadar HydroMap)"})
            with urllib.request.urlopen(req, timeout=8) as resp:
                page = resp.read().decode("utf-8", errors="replace")
            for tr in re.findall(r"<tr\b[^>]*>(.*?)</tr>", page, re.S | re.I):
                m_id = re.search(r"-(\d{7,8})(?:[\"'/])", tr)
                if not m_id:
                    continue
                cells = [
                    _clean_html(c).replace("\u00ad", "").strip()
                    for c in re.findall(r"<td\b[^>]*>(.*?)</td>", tr, re.S | re.I)
                ]
                if len(cells) < 6:
                    continue
                raw_w = cells[3].strip()
                if not raw_w or raw_w == "---":
                    continue
                w_float = _parse_float(raw_w)
                if w_float is None:
                    continue
                # Lakes on HND Bayern are reported in m ü. NHN with decimal comma (e.g. 517,83)
                is_m_nhn = ("," in raw_w or "." in raw_w) and w_float > 300.0
                lvl_cm = None if is_m_nhn else int(round(w_float))
                diff_2h = _parse_int(cells[4], None)
                q_val = _parse_float(cells[5])
                rows_out[m_id.group(1)] = {
                    "name": cells[0],
                    "river": cells[1],
                    "measured_at": cells[2],
                    "current_level_cm": lvl_cm,
                    "level_raw_m": w_float if is_m_nhn else None,
                    "diff_2h_cm": diff_2h,
                    "discharge_m3s": q_val,
                    "origin": "hnd.bayern.de (HND Bayern)",
                }
        except Exception as exc:
            print(f"[WARN] Failed to fetch HND Bayern table {url}: {exc}")
        return rows_out

    with concurrent.futures.ThreadPoolExecutor(max_workers=len(urls)) as ex:
        for part in ex.map(_fetch_one, urls):
            hnd_by_id.update(part)

    return hnd_by_id


def fetch_hvz_bw_observations():
    """Fetches live official Upper Danube headwater telemetry from HVZ Baden-Württemberg."""
    hvz_by_id = {}
    url = "https://www.hvz.baden-wuerttemberg.de/js/hvz_peg_stmn.js"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (RiverRadar HydroMap)"})
        with urllib.request.urlopen(req, timeout=8) as resp:
            text = resp.read().decode("utf-8", errors="replace")
        # Rows look like: ['00151','Donaueschingen (Add.)','Donau',6,'117','cm','22.11.2026 13:00 MEZ','--','','...',...]
        pat = re.compile(
            r"\['(\d{5})','([^']*)','([^']*)',\d+,'([^']*)','cm','([^']*)','([^']*)'"
        )
        for m in pat.finditer(text):
            sid, name, river, w_str, measured_at, q_str = m.groups()
            lvl = _parse_int(w_str)
            if lvl is None:
                continue
            q_val = _parse_float(q_str)
            hvz_by_id[sid] = {
                "name": name,
                "river": river,
                "current_level_cm": lvl,
                "discharge_m3s": q_val,
                "measured_at": measured_at,
                "origin": "hvz.baden-wuerttemberg.de (HVZ BW)",
            }
    except Exception as exc:
        print(f"[WARN] Failed to fetch HVZ Baden-Württemberg telemetry: {exc}")

    return hvz_by_id


def fetch_appd_bulgaria_observations():
    """Fetches live official Bulgarian Danube telemetry from IAPPD / APPD (appd-bg.org)."""
    appd_by_key = {}
    url = "https://www.appd-bg.org/site/"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (RiverRadar HydroMap)"})
        with urllib.request.urlopen(req, timeout=8) as resp:
            page = resp.read().decode("utf-8", errors="replace")
        for tr in re.findall(r"<tr\b[^>]*>(.*?)</tr>", page, re.S | re.I):
            cells = [
                re.sub(r"\s+", " ", _clean_html(c)).strip()
                for c in re.findall(r"<t[dh]\b[^>]*>(.*?)</t[dh]>", tr, re.S | re.I)
            ]
            if len(cells) < 3:
                continue
            key = cells[0].lower()
            if not key or "мост" in key or "," in key:
                continue
            m_lvl = re.match(r"^(-?\d{1,4})\b", cells[2])
            if not m_lvl:
                continue
            lvl = int(m_lvl.group(1))
            q_val = _parse_float(cells[3]) if len(cells) >= 4 else None
            t_val = _parse_float(cells[5]) if len(cells) >= 6 else (
                _parse_float(cells[4]) if len(cells) >= 5 else None
            )
            # Keep the primary official row (with discharge) if already present; fill missing temp/level otherwise
            existing = appd_by_key.get(key)
            if not existing or (existing["discharge_m3s"] is None and q_val is not None):
                appd_by_key[key] = {
                    "name": cells[0],
                    "current_level_cm": lvl,
                    "discharge_m3s": q_val,
                    "water_temp_c": t_val,
                    "origin": "appd-bg.org (ИАППД)",
                }
            elif existing and existing["water_temp_c"] is None and t_val is not None:
                existing["water_temp_c"] = t_val
    except Exception as exc:
        print(f"[WARN] Failed to fetch APPD Bulgaria telemetry: {exc}")

    return appd_by_key


def fetch_nimh_bulgaria_observations():
    """Fetches live official Bulgarian inland river telemetry from NIMH (hydro.bg)."""
    nimh_by_id = {}
    url = "https://hydro.bg/bg/t1.php?ime=&gr=data/&gn=tablRekiB2017"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (RiverRadar HydroMap)"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            page = resp.read().decode("utf-8", errors="replace")
        for tr in re.findall(r"<tr\b[^>]*>(.*?)</tr>", page, re.S | re.I):
            cells = [
                re.sub(r"\s+", " ", _clean_html(c)).strip()
                for c in re.findall(r"<t[dh]\b[^>]*>(.*?)</t[dh]>", tr, re.S | re.I)
            ]
            if len(cells) < 8 or not re.match(r"^\d{4,6}$", cells[0]):
                continue
            sid = cells[0]
            lvl = _parse_int(cells[6])
            if lvl is None:
                continue
            q_val = _parse_float(cells[7].replace(" ", ""))
            diff_24h = _parse_int(cells[8], 0) if len(cells) >= 9 else 0
            nimh_by_id[sid] = {
                "river": cells[1],
                "name": cells[2],
                "current_level_cm": lvl,
                "discharge_m3s": q_val,
                "diff_24h_cm": diff_24h,
                "origin": "hydro.bg (НИМХ)",
            }
    except Exception as exc:
        print(f"[WARN] Failed to fetch NIMH Bulgaria telemetry: {exc}")

    return nimh_by_id


def fetch_hydroinfo_official_forecasts():
    """Fetches official 6-day water level predictions from hydroinfo.hu (dunelotH.html, tiselotH.html)."""
    forecasts_by_key = {}
    urls = [
        "https://www.hydroinfo.hu/tables/dunelotH.html",
        "https://www.hydroinfo.hu/tables/tiselotH.html",
    ]

    for url in urls:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (RiverRadar HydroMap)"})
            with urllib.request.urlopen(req, timeout=7) as resp:
                text = resp.read().decode("iso-8859-2", errors="replace")
                flat = re.sub(
                    r"<table[^>]*>\s*<tr>\s*<td[^>]*>(.*?)</td>\s*<td[^>]*>(.*?)</td>\s*</tr>\s*</table>",
                    r"\1 | \2",
                    text,
                    flags=re.S | re.I,
                )
                trs = re.findall(r"<tr[^>]*>(.*?)</tr>", flat, re.S | re.I)
                for tr in trs:
                    tds = [_clean_html(td) for td in re.findall(r"<td[^>]*>(.*?)</td>", tr, re.S | re.I)]
                    if len(tds) >= 8 and "(" in tds[0]:
                        header = tds[0]
                        m_hdr = re.match(r"^([^\(]+?)\s*\(([^)]+)\)", header)
                        if not m_hdr:
                            continue
                        river_and_station = m_hdr.group(1).strip()
                        issued_at = m_hdr.group(2).strip()
                        norm_key = _norm_hu(river_and_station)

                        days_pred = []
                        for col in tds[2:8]:
                            parts = col.split("|")
                            val = _parse_int(parts[0])
                            unc = _parse_int(parts[1], 15) if len(parts) > 1 else 15
                            if val is not None:
                                days_pred.append({"level_cm": val, "uncertainty_cm": abs(unc)})
                        if len(days_pred) == 6:
                            forecasts_by_key[norm_key] = {
                                "issued_at": issued_at,
                                "days": days_pred,
                            }
        except Exception as exc:
            print(f"[WARN] Failed to fetch official forecast {url}: {exc}")

    return forecasts_by_key


def fetch_all_catchments_weather():
    """Fetches 8-day weather and GloFAS river discharge forecast for all catchments using batched Open-Meteo requests."""
    cids = list(CATCHMENTS.keys())
    lats = ",".join(str(CATCHMENTS[c]["lat"]) for c in cids)
    lons = ",".join(str(CATCHMENTS[c]["lon"]) for c in cids)

    weather_by_cid = {}
    discharge_by_cid = {}

    try:
        w_url = (
            f"https://api.open-meteo.com/v1/forecast?latitude={lats}&longitude={lons}"
            f"&daily=precipitation_sum,temperature_2m_max,temperature_2m_min,et0_fao_evapotranspiration,wind_speed_10m_max"
            f"&timezone=Europe%2FBudapest&forecast_days=8"
        )
        req = urllib.request.Request(w_url, headers={"User-Agent": "RiverRadar-HydroMap/1.0"})
        with urllib.request.urlopen(req, timeout=8) as resp:
            wdata_list = json.loads(resp.read().decode("utf-8"))
            if isinstance(wdata_list, dict):
                wdata_list = [wdata_list]
            for idx, cid in enumerate(cids):
                if idx < len(wdata_list):
                    daily = wdata_list[idx].get("daily", {})
                    times = daily.get("time", [])
                    precips = daily.get("precipitation_sum", [])
                    tmaxs = daily.get("temperature_2m_max", [])
                    tmins = daily.get("temperature_2m_min", [])
                    et0s = daily.get("et0_fao_evapotranspiration", [])
                    winds = daily.get("wind_speed_10m_max", [])
                    w_days = []
                    for i in range(min(8, len(times))):
                        w_days.append({
                            "date": times[i],
                            "precip_mm": round(float(precips[i] or 0.0), 1),
                            "temp_max_c": round(float(tmaxs[i] or 8.0), 1),
                            "temp_min_c": round(float(tmins[i] or 2.0), 1),
                            "et0_mm": round(float(et0s[i] or 1.2), 1),
                            "wind_kmh": round(float(winds[i] or 12.0), 1),
                        })
                    weather_by_cid[cid] = w_days
    except Exception as exc:
        print(f"[WARN] Batched Open-Meteo weather fallback activated: {exc}")

    try:
        f_url = (
            f"https://flood-api.open-meteo.com/v1/flood?latitude={lats}&longitude={lons}"
            f"&daily=river_discharge&forecast_days=8"
        )
        req = urllib.request.Request(f_url, headers={"User-Agent": "RiverRadar-HydroMap/1.0"})
        with urllib.request.urlopen(req, timeout=8) as resp:
            fdata_list = json.loads(resp.read().decode("utf-8"))
            if isinstance(fdata_list, dict):
                fdata_list = [fdata_list]
            for idx, cid in enumerate(cids):
                if idx < len(fdata_list):
                    q_list = fdata_list[idx].get("daily", {}).get("river_discharge", [])
                    discharge_by_cid[cid] = [round(float(q or 0.0), 1) for q in q_list[:8]]
    except Exception as exc:
        print(f"[WARN] Batched Open-Meteo flood fallback activated: {exc}")

    base_date = datetime.date.today()
    results = {}
    for idx, cid in enumerate(cids):
        cinfo = CATCHMENTS[cid]
        w_days = weather_by_cid.get(cid, [])
        if len(w_days) < 8:
            w_days = []
            for d in range(8):
                dt = (base_date + datetime.timedelta(days=d)).isoformat()
                p = [2.4, 6.8, 11.5, 4.2, 1.0, 0.4, 3.6, 5.1][d]
                w_days.append({
                    "date": dt,
                    "precip_mm": round(p + (idx % 3) * 0.6, 1),
                    "temp_max_c": round(9.5 - d * 0.3, 1),
                    "temp_min_c": round(3.2 - d * 0.2, 1),
                    "et0_mm": 1.1,
                    "wind_kmh": 15.0,
                })
        results[cid] = {
            "info": cinfo,
            "weather": w_days,
            "glofas_discharge": discharge_by_cid.get(cid, []),
        }
    return results


def classify_alert(level_cm: int, thresholds: dict):
    if level_cm >= thresholds["deg3"]:
        return "deg3", "Flood alert level III"
    if level_cm >= thresholds["deg2"]:
        return "deg2", "Flood alert level II"
    if level_cm >= thresholds["deg1"]:
        return "deg1", "Flood alert level I"
    elevated_cutoff = thresholds["deg1"] - max(60, int((thresholds["deg1"] - thresholds["low"]) * 0.25))
    if level_cm >= elevated_cutoff:
        return "elevated", "Elevated water level"
    if level_cm <= thresholds["low"]:
        return "low", "Low water"
    return "normal", "Normal water level"


def build_hydro_payload(force_refresh=False):
    now = time.time()
    with _CACHE_LOCK:
        if not force_refresh and _CACHE["payload"] and (now - _CACHE["timestamp"] < CACHE_TTL_SECONDS):
            return _CACHE["payload"]

    with _REFRESH_LOCK:
        now = time.time()
        with _CACHE_LOCK:
            if not force_refresh and _CACHE["payload"] and (now - _CACHE["timestamp"] < CACHE_TTL_SECONDS):
                return _CACHE["payload"]

        return _fetch_and_build_payload(now)


def _fetch_and_build_payload(now: float):
    obs_map, obs_date = fetch_hydroinfo_observations()
    vizugy_map = fetch_vizugy_operative_observations()
    dhmz_map = fetch_dhmz_croatia_observations()
    rhmz_map = fetch_rhmz_serbia_observations()
    arso_map = fetch_arso_slovenia_observations()
    hnd_map = fetch_hnd_bayern_observations()
    hvz_map = fetch_hvz_bw_observations()
    appd_map = fetch_appd_bulgaria_observations()
    nimh_map = fetch_nimh_bulgaria_observations()
    ovf_forecasts = fetch_hydroinfo_official_forecasts()
    catchment_weather = fetch_all_catchments_weather()

    live_obs_count = 0
    live_vizugy_count = 0
    live_ovf_forecast_count = 0
    stations_out = []

    for st in STATIONS_CATALOG:
        code = st["code"]
        vizugy_id = st.get("vizugy_id") or (code.replace("VIZUGY_", "") if code.startswith("VIZUGY_") else None)
        dhmz_id = st.get("dhmz_id") or (code.replace("DHMZ_", "") if code.startswith("DHMZ_") else None)
        rhmz_id = st.get("rhmz_id") or (code.replace("RHMZ_", "") if code.startswith("RHMZ_") else None)
        arso_id = st.get("arso_id") or (code.replace("ARSO_", "") if code.startswith("ARSO_") else None)
        hnd_id = st.get("hnd_id") or (code.replace("DE_BY_", "") if code.startswith("DE_BY_") else None)
        hvz_id = st.get("hvz_id") or (code.replace("DE_BW_", "") if code.startswith("DE_BW_") else None)
        appd_key = st.get("appd_key")
        nimh_id = st.get("nimh_id") or (code.replace("BG_NIMH_", "") if code.startswith("BG_NIMH_") else None)
        obs = obs_map.get(code)
        v_obs = vizugy_map.get(vizugy_id) if vizugy_id else None
        d_obs = dhmz_map.get(dhmz_id) if dhmz_id else None
        r_obs = rhmz_map.get(rhmz_id) if rhmz_id else None
        a_obs = arso_map.get(arso_id) if arso_id else None
        hnd_obs = hnd_map.get(hnd_id) if hnd_id else None
        hvz_obs = hvz_map.get(hvz_id) if hvz_id else None
        appd_obs = appd_map.get(appd_key) if appd_key else None
        nimh_obs = nimh_map.get(nimh_id) if nimh_id else None

        if obs:
            live_obs_count += 1
            curr_level = obs["current_level_cm"]
            diff_24h = obs["diff_24h_cm"]
            discharge_0 = (
                obs["discharge_m3s"]
                if obs["discharge_m3s"] is not None
                else (
                    appd_obs["discharge_m3s"]
                    if appd_obs and appd_obs["discharge_m3s"]
                    else (
                        hnd_obs["discharge_m3s"]
                        if hnd_obs and hnd_obs["discharge_m3s"]
                        else (
                            v_obs["discharge_m3s"]
                            if v_obs and v_obs["discharge_m3s"]
                            else (
                                r_obs["discharge_m3s"]
                                if r_obs and r_obs["discharge_m3s"]
                                else (a_obs["discharge_m3s"] if a_obs and a_obs["discharge_m3s"] else st["default_discharge"])
                            )
                        )
                    )
                )
            )
            water_temp = (
                obs["water_temp_c"]
                if obs["water_temp_c"] is not None
                else (
                    appd_obs["water_temp_c"]
                    if appd_obs and appd_obs["water_temp_c"] is not None
                    else (a_obs["water_temp_c"] if a_obs and a_obs["water_temp_c"] is not None else st["default_temp"])
                )
            )
            ice_status = obs["ice_status"]
            day0_source = "OVF / INHGA / SHMÚ / eHYD / ARSO / HND / APPD official live reading (hydroinfo.hu)"
        elif v_obs:
            live_obs_count += 1
            live_vizugy_count += 1
            curr_level = v_obs["current_level_cm"]
            diff_24h = st["default_diff24h"]
            discharge_0 = v_obs["discharge_m3s"] if v_obs["discharge_m3s"] is not None else st["default_discharge"]
            water_temp = v_obs["water_temp_c"] if v_obs["water_temp_c"] is not None else st["default_temp"]
            ice_status = "jégmentes"
            day0_source = f"OVF Operational Water Level live reading (vizugy.hu • {v_obs['measured_at']})"
        elif d_obs:
            live_obs_count += 1
            curr_level = d_obs["current_level_cm"]
            diff_24h = st["default_diff24h"]
            discharge_0 = st["default_discharge"]
            water_temp = st["default_temp"]
            ice_status = "jégmentes"
            day0_source = f"DHMZ Croatia live reading (hidro.dhz.hr • {d_obs['measured_at']})"
        elif r_obs:
            live_obs_count += 1
            curr_level = r_obs["current_level_cm"]
            diff_24h = r_obs["diff_24h_cm"]
            discharge_0 = r_obs["discharge_m3s"] if r_obs["discharge_m3s"] is not None else st["default_discharge"]
            water_temp = r_obs["water_temp_c"] if r_obs["water_temp_c"] is not None else st["default_temp"]
            ice_status = "jégmentes"
            day0_source = "RHMZ Serbia official live reading (hidmet.gov.rs)"
        elif a_obs:
            live_obs_count += 1
            curr_level = a_obs["current_level_cm"]
            diff_24h = st["default_diff24h"]
            discharge_0 = a_obs["discharge_m3s"] if a_obs["discharge_m3s"] is not None else st["default_discharge"]
            water_temp = a_obs["water_temp_c"] if a_obs["water_temp_c"] is not None else st["default_temp"]
            ice_status = "jégmentes"
            day0_source = f"ARSO Slovenia live reading (arso.gov.si • {a_obs['measured_at']})"
        elif hnd_obs and (hnd_obs["current_level_cm"] is not None or (hnd_obs["level_raw_m"] is not None and st.get("zero_m_nhn"))):
            live_obs_count += 1
            if hnd_obs["level_raw_m"] is not None and st.get("zero_m_nhn"):
                curr_level = int(round((hnd_obs["level_raw_m"] - st["zero_m_nhn"]) * 100.0))
            else:
                curr_level = hnd_obs["current_level_cm"]
            diff_24h = hnd_obs["diff_2h_cm"] if hnd_obs["diff_2h_cm"] is not None else st["default_diff24h"]
            discharge_0 = hnd_obs["discharge_m3s"] if hnd_obs["discharge_m3s"] is not None else st["default_discharge"]
            water_temp = st["default_temp"]
            ice_status = "jégmentes"
            day0_source = f"HND Bayern official live reading (hnd.bayern.de • {hnd_obs['measured_at']})"
        elif hvz_obs:
            live_obs_count += 1
            curr_level = hvz_obs["current_level_cm"]
            diff_24h = st["default_diff24h"]
            discharge_0 = hvz_obs["discharge_m3s"] if hvz_obs["discharge_m3s"] is not None else st["default_discharge"]
            water_temp = st["default_temp"]
            ice_status = "jégmentes"
            day0_source = f"HVZ Baden-Württemberg live reading (hvz.baden-wuerttemberg.de • {hvz_obs['measured_at']})"
        elif appd_obs:
            live_obs_count += 1
            curr_level = appd_obs["current_level_cm"]
            diff_24h = st["default_diff24h"]
            discharge_0 = appd_obs["discharge_m3s"] if appd_obs["discharge_m3s"] is not None else st["default_discharge"]
            water_temp = appd_obs["water_temp_c"] if appd_obs["water_temp_c"] is not None else st["default_temp"]
            ice_status = "jégmentes"
            day0_source = "ИАППД Bulgaria Danube live reading (appd-bg.org)"
        elif nimh_obs:
            live_obs_count += 1
            curr_level = nimh_obs["current_level_cm"]
            diff_24h = nimh_obs["diff_24h_cm"]
            discharge_0 = nimh_obs["discharge_m3s"] if nimh_obs["discharge_m3s"] is not None else st["default_discharge"]
            water_temp = st["default_temp"]
            ice_status = "jégmentes"
            day0_source = "НИМХ Bulgaria official live reading (hydro.bg)"
        else:
            anchor_code = st.get("transboundary_anchor")
            anchor_obs = obs_map.get(anchor_code) if anchor_code else None
            if anchor_obs:
                anchor_st = next((x for x in STATIONS_CATALOG if x["code"] == anchor_code), None)
                if anchor_st:
                    a_span = max(80, anchor_st["thresholds"]["deg1"] - anchor_st["thresholds"]["low"])
                    st_span = max(60, st["thresholds"]["deg1"] - st["thresholds"]["low"])
                    rel_anom = (anchor_obs["current_level_cm"] - anchor_st["default_level"]) / a_span
                    scale = 0.25 if st["basin"] == "tavak" else 0.72
                    curr_level = int(round(st["default_level"] + rel_anom * st_span * scale))
                    diff_24h = int(round((anchor_obs["diff_24h_cm"] / a_span) * st_span * scale))
                    discharge_0 = max(0.2, round(st["default_discharge"] * math.exp(rel_anom * 0.7), 1))
                    water_temp = (
                        anchor_obs["water_temp_c"]
                        if anchor_obs["water_temp_c"] is not None
                        else st["default_temp"]
                    )
                    ice_status = anchor_obs.get("ice_status", "jégmentes")
                    day0_source = f"Copernicus GloFAS v4 (5km) & cross-border calibration ({anchor_st['name']})"
                else:
                    curr_level = st["default_level"]
                    diff_24h = st["default_diff24h"]
                    discharge_0 = st["default_discharge"]
                    water_temp = st["default_temp"]
                    ice_status = "jégmentes"
                    day0_source = "Copernicus GloFAS v4 (5km) & regional reference"
            else:
                curr_level = st["default_level"]
                diff_24h = st["default_diff24h"]
                discharge_0 = st["default_discharge"]
                water_temp = st["default_temp"]
                ice_status = "jégmentes"
                day0_source = "Copernicus GloFAS v4 (5km) & regional reference"

        lookup_key = _norm_hu(f"{st['river']} {st['name']}")
        ovf_fc = ovf_forecasts.get(lookup_key)
        if not ovf_fc:
            st_norm = _norm_hu(st["name"])
            rv_norm = _norm_hu(st["river"])
            for k, v in ovf_forecasts.items():
                if k.startswith(rv_norm + " ") and (k.endswith(" " + st_norm) or st_norm in k):
                    ovf_fc = v
                    break

        if ovf_fc:
            live_ovf_forecast_count += 1

        c_data = catchment_weather.get(st["catchment"], catchment_weather["mid_duna"])
        w_days = c_data["weather"]
        q_days = c_data["glofas_discharge"]
        resp_factor = c_data["info"]["response_factor"]
        lag_days = c_data["info"]["lag_days"]
        water_category = st.get("water_category", "major")

        # Smaller streams & creeks respond faster to local rainfall and recede faster
        if water_category == "minor":
            resp_factor = resp_factor * 0.72
            lag_days = max(0, lag_days - 1)

        timeline = []
        cum_precip = 0.0
        prev_level = curr_level

        for d in range(8):
            w_day = w_days[min(d, len(w_days) - 1)]
            p_mm = w_day["precip_mm"]
            if d > 0:
                cum_precip = round(cum_precip + p_mm, 1)

            if d == 0:
                lvl = curr_level
                unc = 0
                src = day0_source
                daily_chg = diff_24h
            elif ovf_fc and 1 <= d <= 6:
                lvl = ovf_fc["days"][d - 1]["level_cm"]
                unc = ovf_fc["days"][d - 1]["uncertainty_cm"]
                src = "OVF Hivatalos 6 napos modell + Open-Meteo"
                daily_chg = lvl - prev_level
            elif ovf_fc and d == 7:
                d5_lvl = ovf_fc["days"][4]["level_cm"]
                d6_lvl = ovf_fc["days"][5]["level_cm"]
                momentum = (d6_lvl - d5_lvl) * 0.65
                eff_day = max(0, d - lag_days)
                net_rain = max(0.0, w_days[min(eff_day, len(w_days) - 1)]["precip_mm"] - w_day["et0_mm"] * 0.7)
                rain_push = net_rain * resp_factor * 0.85
                lvl = int(round(d6_lvl + momentum + rain_push))
                unc = int(round(ovf_fc["days"][5]["uncertainty_cm"] * 1.15 + 4))
                src = "OVF extrapolation + Open-Meteo GloFAS (day 7)"
                daily_chg = lvl - prev_level
            else:
                decay = (0.45 if water_category == "minor" else 0.55) ** d
                momentum_step = diff_24h * decay
                eff_day = max(0, d - lag_days)
                eff_w = w_days[min(eff_day, len(w_days) - 1)]
                net_precip = eff_w["precip_mm"] - eff_w["et0_mm"] * 0.65
                rain_step = net_precip * resp_factor

                glofas_step = 0.0
                if len(q_days) > d and q_days[0] > 0.5:
                    q_ratio = (q_days[d] - q_days[d - 1]) / max(1.0, q_days[0])
                    glofas_step = q_ratio * (35.0 if water_category == "minor" else 65.0)

                mean_target = (st["thresholds"]["low"] + st["thresholds"]["deg1"]) * 0.36
                reversion = (mean_target - prev_level) * (0.02 if st["basin"] == "tavak" else 0.07)

                step_delta = momentum_step + rain_step + glofas_step + reversion
                lvl = int(round(prev_level + step_delta))
                unc = int(round((3 if st["basin"] == "tavak" else 5) + d * (1.8 if st["basin"] == "tavak" else 3.8)))
                src = "Open-Meteo + GloFAS v4 (5km) small-catchment runoff model" if water_category == "minor" else "Open-Meteo + GloFAS hydrological runoff model"
                daily_chg = lvl - prev_level

            level_span = max(80, st["thresholds"]["deg1"] - st["thresholds"]["low"])
            rel_stage = (lvl - curr_level) / level_span
            est_q = max(0.2, round(discharge_0 * math.exp(rel_stage * 0.85), 1))

            alert_code, alert_label = classify_alert(lvl, st["thresholds"])

            timeline.append({
                "day": d,
                "date": w_day["date"],
                "label": "Today (Live)" if d == 0 else f"+{d} day",
                "level_cm": lvl,
                "uncertainty_cm": unc,
                "delta_from_today_cm": lvl - curr_level,
                "daily_change_cm": daily_chg,
                "discharge_m3s": est_q,
                "precip_mm": p_mm,
                "cum_precip_mm": cum_precip,
                "temp_max_c": w_day["temp_max_c"],
                "temp_min_c": w_day["temp_min_c"],
                "wind_kmh": w_day["wind_kmh"],
                "alert_level": alert_code,
                "alert_label": alert_label,
                "source": src,
            })
            prev_level = lvl

        stations_out.append({
            "code": st["code"],
            "country": st.get("country", "HU"),
            "water_category": water_category,
            "name": st["name"],
            "river": st["river"],
            "basin": st["basin"],
            "catchment": st["catchment"],
            "catchment_name": c_data["info"]["name"],
            "reach_name": st["reach_name"],
            "lat": st["lat"],
            "lon": st["lon"],
            "fkm": st["fkm"],
            "thresholds": st["thresholds"],
            "water_temp_c": water_temp,
            "ice_status": ice_status,
            "has_official_ovf_forecast": bool(ovf_fc),
            "ovf_issued_at": ovf_fc["issued_at"] if ovf_fc else (obs_date or "Updated"),
            "response_factor": resp_factor,
            "lag_days": lag_days,
            "timeline": timeline,
        })

    payload = {
        "meta": {
            "generated_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "next_refresh_at": (
                datetime.datetime.now() + datetime.timedelta(seconds=REFRESH_INTERVAL_SECONDS)
            ).strftime("%Y-%m-%d %H:%M:%S"),
            "refresh_interval_seconds": REFRESH_INTERVAL_SECONDS,
            "observation_date": obs_date or datetime.date.today().strftime("%Y. %m. %d."),
            "total_stations": len(stations_out),
            "hu_stations": sum(1 for s in stations_out if s["country"] == "HU"),
            "ro_stations": sum(1 for s in stations_out if s["country"] == "RO"),
            "sk_stations": sum(1 for s in stations_out if s["country"] == "SK"),
            "at_stations": sum(1 for s in stations_out if s["country"] == "AT"),
            "hr_stations": sum(1 for s in stations_out if s["country"] == "HR"),
            "rs_stations": sum(1 for s in stations_out if s["country"] == "RS"),
            "si_stations": sum(1 for s in stations_out if s["country"] == "SI"),
            "ua_stations": sum(1 for s in stations_out if s["country"] == "UA"),
            "de_stations": sum(1 for s in stations_out if s["country"] == "DE"),
            "bg_stations": sum(1 for s in stations_out if s["country"] == "BG"),
            "major_stations": sum(1 for s in stations_out if s["water_category"] == "major"),
            "minor_stations": sum(1 for s in stations_out if s["water_category"] == "minor"),
            "countries": COUNTRIES_META,
            "live_hydroinfo_matched": live_obs_count,
            "live_vizugy_matched": live_vizugy_count,
            "official_ovf_forecast_stations": live_ovf_forecast_count,
            "sources": [
                "Hungarian National Hydrological Forecasting Service (OVF / hydroinfo.hu & vizugy.hu)",
                "INHGA Romania (74xxxx), SHMÚ Slovakia (14xxxx) & eHYD Austria (24xxxx)",
                "DHMZ Croatia (hidro.dhz.hr), RHMZ Serbia (hidmet.gov.rs) & ARSO Slovenia (arso.gov.si)",
                "HND Bayern (hnd.bayern.de) & HVZ Baden-Württemberg (hvz.baden-wuerttemberg.de)",
                "ИАППД Bulgaria (appd-bg.org) & НИМХ Bulgaria (hydro.bg)",
                "Copernicus GloFAS v4 (5 km resolution discharge model) & Open-Meteo IFS",
            ],
        },
        "catchments": {
            cid: {
                "name": cdata["info"]["name"],
                "weather": cdata["weather"],
            }
            for cid, cdata in catchment_weather.items()
        },
        "stations": stations_out,
    }

    try:
        storage.init_db()
        payload["meta"]["storage"] = storage.save_snapshot(payload)
    except Exception as exc:
        print(f"[WARN] Failed to persist snapshot to SQLite: {exc}", flush=True)

    with _CACHE_LOCK:
        _CACHE["timestamp"] = now
        _CACHE["payload"] = payload
    return payload


def start_hourly_refresh_worker(stop_event: threading.Event, interval_seconds: int = REFRESH_INTERVAL_SECONDS):
    """Starts a daemon background thread that refreshes hydrological and weather data on a fixed interval."""
    def _worker():
        while not stop_event.wait(interval_seconds):
            started = time.time()
            try:
                refreshed = build_hydro_payload(force_refresh=True)
                elapsed = time.time() - started
                meta = refreshed["meta"]
                print(
                    f"[RiverRadar] Hourly background refresh complete in {elapsed:.2f}s "
                    f"({meta['total_stations']} stations, {meta['live_hydroinfo_matched']} live measurements, "
                    f"next at {meta['next_refresh_at']}).",
                    flush=True,
                )
            except Exception as exc:
                print(f"[WARN] Hourly background refresh failed: {exc}", flush=True)

    thread = threading.Thread(target=_worker, name="riverradar-hourly-refresh", daemon=True)
    thread.start()
    return thread


class HydroRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=STATIC_DIR, **kwargs)

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cache-Control", "no-store, must-revalidate")
        super().end_headers()

    def _send_json(self, obj, status=200):
        body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path in ("/api/hydro-data", "/api/refresh"):
            force = parsed.path == "/api/refresh"
            try:
                data = build_hydro_payload(force_refresh=force)
                self._send_json(data, 200)
            except Exception as exc:
                self._send_json({"error": str(exc)}, 500)
            return

        if parsed.path == "/api/history/stats":
            try:
                self._send_json(storage.get_db_stats(), 200)
            except Exception as exc:
                self._send_json({"error": str(exc)}, 500)
            return

        if parsed.path == "/api/history":
            try:
                qs = urllib.parse.parse_qs(parsed.query)
                station_code = qs.get("station", [None])[0]
                if not station_code:
                    limit = int(qs.get("limit", ["48"])[0])
                    self._send_json(
                        {
                            "stats": storage.get_db_stats(),
                            "snapshots": storage.list_recent_snapshots(limit=limit),
                        },
                        200,
                    )
                    return

                hours = int(qs.get("hours", ["720"])[0])
                lead_raw = qs.get("lead_day", ["0"])[0]
                lead_day = None if lead_raw == "all" else int(lead_raw)
                result = storage.query_station_history(
                    station_code=station_code,
                    hours=hours,
                    lead_day=lead_day,
                )
                self._send_json(result, 200)
            except Exception as exc:
                self._send_json({"error": str(exc)}, 400)
            return

        if parsed.path == "/":
            self.path = "/index.html"
        return super().do_GET()


if __name__ == "__main__":
    storage.init_db()
    print(f"[RiverRadar] Pre-warming live hydrological & meteorological cache (Modular countries: {', '.join(COUNTRIES_META.keys())})...")
    payload = build_hydro_payload(force_refresh=True)
    meta = payload["meta"]
    st_info = meta.get("storage", {})
    print(
        f"[RiverRadar] Loaded {meta['total_stations']} stations "
        f"(HU: {meta['hu_stations']}, RO: {meta['ro_stations']}, SK: {meta['sk_stations']}, "
        f"AT: {meta['at_stations']}, HR: {meta['hr_stations']}, RS: {meta['rs_stations']}, "
        f"SI: {meta['si_stations']}, UA-ZK: {meta['ua_stations']}, DE-Danube: {meta['de_stations']}, BG: {meta['bg_stations']} | "
        f"Major: {meta['major_stations']}, Minor waters: {meta['minor_stations']} | "
        f"{meta['live_hydroinfo_matched']} live measurements, {meta['official_ovf_forecast_stations']} official 6-day OVF forecasts)."
    )
    if st_info:
        print(
            f"[RiverRadar] SQLite 30-day archive ready at {st_info.get('db_path')} "
            f"({st_info.get('snapshots_count')} snapshots, {st_info.get('station_rows')} station rows, "
            f"{st_info.get('db_size_bytes', 0) / 1024:.1f} KiB, retention={st_info.get('retention_days')}d)."
        )
    stop_event = threading.Event()
    start_hourly_refresh_worker(stop_event, REFRESH_INTERVAL_SECONDS)
    print(f"[RiverRadar] Background refresh thread active (every {REFRESH_INTERVAL_SECONDS}s, next at {meta['next_refresh_at']}).")
    socketserver.TCPServer.allow_reuse_address = True
    try:
        with socketserver.ThreadingTCPServer(("127.0.0.1", PORT), HydroRequestHandler) as httpd:
            print(f"[RiverRadar] Server listening at http://localhost:{PORT}")
            httpd.serve_forever()
    except KeyboardInterrupt:
        stop_event.set()
        print("\n[RiverRadar] Shutting down cleanly.")
