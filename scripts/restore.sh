#!/usr/bin/env bash
# Replace this machine's content with a backup made by backup.sh.
#
#   ./scripts/restore.sh backups/m3m-backup-2026-10-23_1800.tar.gz
#
# WARNING: everything currently in the database (projects, enquiries, admin
# users…) and in media/ is replaced by the backup.
set -euo pipefail
cd "$(dirname "$0")/.."

archive="${1:?Usage: ./scripts/restore.sh <backup .tar.gz file>}"
[[ -f "$archive" ]] || { echo "File not found: $archive" >&2; exit 1; }
if [[ -x .venv/bin/python ]]; then PY=".venv/bin/python"; else PY=".venv/Scripts/python"; fi

if [[ "${FORCE:-}" != "1" ]]; then
  read -r -p "This replaces ALL current content and admin users with the backup. Continue? [y/N] " answer
  [[ "$answer" =~ ^[Yy]$ ]] || { echo "Cancelled."; exit 1; }
fi

work="$(mktemp -d)"
trap 'rm -rf "$work"' EXIT
tar -xzf "$archive" -C "$work"

"$PY" manage.py migrate --noinput
"$PY" manage.py flush --noinput
"$PY" manage.py loaddata "$work/data.json"

rm -rf media
cp -r "$work/media" media
echo "Restore complete. Restart the site if it is running (sudo systemctl restart m3m)."
