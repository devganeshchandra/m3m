#!/usr/bin/env bash
# Save all website content (database + uploaded images/files) into one file,
# plus a native PostgreSQL dump (database.dump) when the site runs on PostgreSQL,
# e.g. to move the site to another machine or keep a nightly copy.
#
#   ./scripts/backup.sh                  -> backups/m3m-backup-YYYY-MM-DD_HHMM.tar.gz
#
# Restore it with ./scripts/restore.sh <file>.
set -euo pipefail
cd "$(dirname "$0")/.."

if [[ -x .venv/bin/python ]]; then PY=".venv/bin/python"; else PY=".venv/Scripts/python"; fi

stamp="$(date +%Y-%m-%d_%H%M)"
work="$(mktemp -d)"
trap 'rm -rf "$work"' EXIT
mkdir -p backups

"$PY" manage.py dumpdata \
  --natural-foreign --natural-primary --indent 1 \
  --exclude contenttypes --exclude auth.permission \
  --exclude sessions --exclude admin.logentry \
  --output "$work/data.json"

mkdir -p media
cp -r media "$work/media"
files=(data.json media)

# On PostgreSQL, also keep a native dump (pg_restore can load it into any PostgreSQL server).
set -a; [[ -f .env ]] && source .env; set +a
if [[ "${DB_ENGINE:-sqlite}" =~ ^postgres ]] && command -v pg_dump >/dev/null; then
  PGPASSWORD="${DB_PASSWORD:-}" pg_dump --format=custom --no-owner     --host="${DB_HOST:-localhost}" --port="${DB_PORT:-5432}" --username="${DB_USER:-m3m}"     --file="$work/database.dump" "${DB_NAME:-m3m}"
  files+=(database.dump)
fi

archive="backups/m3m-backup-$stamp.tar.gz"
tar -czf "$archive" -C "$work" "${files[@]}"
echo "Backup saved: $archive"
