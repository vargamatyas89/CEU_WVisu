#!/usr/bin/env bash
# RiverRadar napi auto-deploy (systemd timer hívja, 03:30 Europe/Budapest).
# Ha az origin/main újabb, mint a szerveren futó commit: SQLite mentés -> pull -> build -> újraindítás
# -> health check; hiba esetén visszaállás az előző commitra és e-mail értesítés.
# A Tariff Radar auto-deploy mintájára; a címzett a /etc/default/riverradar-autodeploy fájlból jön.
set -uo pipefail
APP_DIR=/opt/riverradar
STATE_DIR=/var/lib/riverradar
STATE=$STATE_DIR/last_deployed_sha
LOG=/var/log/riverradar-autodeploy.log
BACKUPS=/root/predeploy-riverradar          # külön a Tariff Radar /root/predeploy mappájától
CONTAINER=riverradar
DB_IN_CONTAINER=/data/riverradar_history.sqlite
SMTP_ENV=/opt/tariffwatcher/.env.production # az SMTP-adatok innen jönnek, titkot nem írunk ki
COMPOSE=(docker compose -f "$APP_DIR/deploy/docker-compose.yml")
NOTIFY_TO="${NOTIFY_TO:-}"
mkdir -p "$STATE_DIR" "$BACKUPS"
exec 9>/var/lock/riverradar-autodeploy.lock
flock -n 9 || { echo "$(date -Is) másik futás megy, kilépek" >> "$LOG"; exit 0; }
exec >> "$LOG" 2>&1
log() { echo "$(date -Is) $*"; }

notify() { # $1 tárgy, $2 szöveg
  [ -n "$NOTIFY_TO" ] || { log "(NOTIFY_TO nincs beállítva, nem küldök e-mailt)"; return 0; }
  python3 - "$1" "$2" "$NOTIFY_TO" "$SMTP_ENV" <<'PY' || log "(értesítő e-mail nem ment el)"
import smtplib, sys
from email.message import EmailMessage
env = {}
for l in open(sys.argv[4]):
    if "=" in l and not l.startswith("#"):
        k, v = l.rstrip("\n").split("=", 1); env[k] = v
m = EmailMessage(); m["Subject"] = sys.argv[1]; m["From"] = env["ALERT_FROM_EMAIL"]; m["To"] = sys.argv[3]
m.set_content(sys.argv[2])
s = smtplib.SMTP(env["SMTP_HOST"], int(env["SMTP_PORT"]), timeout=30); s.starttls()
s.login(env["SMTP_USER"], env["SMTP_PASSWORD"]); s.send_message(m); s.quit()
PY
}

health_ok() { # max ~4 perc várakozás a konténer saját healthcheckjére (DNS-től/Caddytől független)
  for i in $(seq 1 24); do
    [ "$(docker inspect -f '{{.State.Health.Status}}' "$CONTAINER" 2>/dev/null)" = "healthy" ] && return 0
    sleep 10
  done
  return 1
}

rebuild() {
  docker network inspect edge >/dev/null 2>&1 || docker network create edge >/dev/null || return 1
  "${COMPOSE[@]}" up -d --build --force-recreate --remove-orphans
}

backup_db() { # SQLite online backup a konténerből; az előzmény 30 napos gördülő, ezért hiba esetén csak figyelmeztetünk
  docker exec "$CONTAINER" test -f "$DB_IN_CONTAINER" 2>/dev/null || { log "nincs még adatbázis, mentés kihagyva"; return 0; }
  docker exec "$CONTAINER" python -c "import sqlite3; s=sqlite3.connect('$DB_IN_CONTAINER'); d=sqlite3.connect('/tmp/pre-deploy.sqlite'); s.backup(d); d.close()" \
    && docker cp "$CONTAINER:/tmp/pre-deploy.sqlite" "$BK.raw" \
    && gzip -c "$BK.raw" > "$BK" && [ -s "$BK" ]
  local rc=$?; rm -f "$BK.raw"; return $rc
}

cd "$APP_DIR" || { log "HIBA: $APP_DIR hiányzik"; exit 1; }
log "== auto-deploy ellenőrzés indul"

if [ -n "$(git status --porcelain --untracked-files=no)" ]; then
  log "HIBA: módosított, nem commitolt fájlok vannak a szerveren, nem frissítek"
  notify "[RiverRadar] auto-deploy kihagyva" "Nem commitolt módosítás van a szerveren ($APP_DIR), ezért nem frissítettem. Részletek: $LOG"
  exit 1
fi

git fetch -q origin main || { log "HIBA: git fetch nem sikerült"; notify "[RiverRadar] auto-deploy: git fetch hiba" "A git fetch nem sikerült. Részletek: $LOG"; exit 1; }
REMOTE=$(git rev-parse origin/main)
CURRENT=$(git rev-parse HEAD)
LAST=$(cat "$STATE" 2>/dev/null || echo "$CURRENT")
echo "$LAST" > "$STATE"
log "szerveren futó: ${CURRENT:0:7} | utoljára telepített: ${LAST:0:7} | origin/main: ${REMOTE:0:7}"

if [ "$REMOTE" = "$CURRENT" ]; then log "nincs újabb commit, nincs teendő"; exit 0; fi
if ! git merge-base --is-ancestor "$CURRENT" "$REMOTE"; then
  log "HIBA: az origin/main nem előre-tekerés (force push?), nem frissítek"
  notify "[RiverRadar] auto-deploy kihagyva" "Az origin/main (${REMOTE:0:7}) nem a futó commit (${CURRENT:0:7}) leszármazottja. Kézi ellenőrzés kell."
  exit 1
fi

CHANGES=$(git log --oneline "$CURRENT..$REMOTE" | head -20)
log "új commitok:"; echo "$CHANGES"

BK="$BACKUPS/rr-$(date +%Y%m%d-%H%M)-pre-${REMOTE:0:7}.sqlite.gz"
if backup_db; then
  log "SQLite mentés: $BK"
else
  log "FIGYELEM: SQLite mentés nem sikerült, a frissítés folytatódik (az előzmény újragyűlik)"; rm -f "$BK"; BK="(nincs)"
fi
ls -1t "$BACKUPS"/rr-*.sqlite.gz 2>/dev/null | tail -n +4 | xargs -r rm -f   # csak a 3 legutóbbi mentés marad

git merge --ff-only origin/main || { log "HIBA: ff-only merge nem sikerült"; exit 1; }
log "kód frissítve: ${REMOTE:0:7}, build + újraindítás"

if rebuild && health_ok; then
  echo "$REMOTE" > "$STATE"
  log "SIKER: ${REMOTE:0:7} fut, konténer healthy"
  notify "[RiverRadar] auto-deploy sikeres: ${REMOTE:0:7}" "Telepítve: ${REMOTE:0:7} (előző: ${CURRENT:0:7}).\n\nÚj commitok:\n$CHANGES\n\nMentés: $BK"
  exit 0
fi

log "HIBA: a frissítés után nincs egészséges állapot, visszaállás: ${CURRENT:0:7}"
git reset --hard "$CURRENT"
if rebuild && health_ok; then
  log "VISSZAÁLLÍTVA: ${CURRENT:0:7} fut"
  notify "[RiverRadar] auto-deploy SIKERTELEN, visszaállítva" "A ${REMOTE:0:7} telepítése nem lett egészséges, visszaálltam: ${CURRENT:0:7}.\nMentés a frissítés előttről: $BK\nRészletek: $LOG"
else
  log "KRITIKUS: a visszaállás után sem egészséges az alkalmazás"
  notify "[RiverRadar] KRITIKUS: az alkalmazás nem egészséges" "Sem a ${REMOTE:0:7}, sem a visszaállított ${CURRENT:0:7} nem indult egészségesen. Kézi beavatkozás kell. Mentés: $BK\nRészletek: $LOG"
fi
exit 1
