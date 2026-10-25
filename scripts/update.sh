#!/usr/bin/env bash
# Apply new code on a server: install packages, migrate, collect static files
# and restart the site. Run from the project folder after `git pull`.
set -euo pipefail
cd "$(dirname "$0")/.."

if [[ -x .venv/bin/python ]]; then PY=".venv/bin/python"; else PY=".venv/Scripts/python"; fi

"$PY" -m pip install --quiet -r requirements.txt
"$PY" manage.py migrate --noinput
"$PY" manage.py collectstatic --noinput -v0

if command -v systemctl >/dev/null 2>&1 && systemctl cat m3m.service >/dev/null 2>&1; then
  sudo systemctl restart m3m
  echo "Site restarted."
else
  echo "Updated. Restart your server process to load the new code."
fi
