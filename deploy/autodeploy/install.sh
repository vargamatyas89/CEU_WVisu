#!/usr/bin/env bash
# Telepíti a napi auto-deployt a szerverre (root-ként futtasd).
set -euo pipefail
SRC="$(cd "$(dirname "$0")" && pwd)"
install -m 700 "$SRC/riverradar-autodeploy.sh" /usr/local/sbin/riverradar-autodeploy.sh
install -m 644 "$SRC/riverradar-autodeploy.service" /etc/systemd/system/
install -m 644 "$SRC/riverradar-autodeploy.timer" /etc/systemd/system/
printf "/var/log/riverradar-autodeploy.log { monthly rotate 6 compress missingok notifempty }\n" > /etc/logrotate.d/riverradar-autodeploy
if [ ! -f /etc/default/riverradar-autodeploy ]; then
  printf "# Hiba/siker értesítések címzettje (üresen: nincs e-mail)\nNOTIFY_TO=\n" > /etc/default/riverradar-autodeploy
  chmod 600 /etc/default/riverradar-autodeploy
  echo "FIGYELEM: állítsd be a NOTIFY_TO-t: /etc/default/riverradar-autodeploy"
fi
systemctl daemon-reload
systemctl enable --now riverradar-autodeploy.timer
systemctl list-timers riverradar-autodeploy.timer --no-pager
