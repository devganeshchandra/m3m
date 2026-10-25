#!/usr/bin/env bash
# Save all website content (database + uploaded images/files) into one file,
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

archive="backups/m3m-backup-$stamp.tar.gz"
tar -czf "$archive" -C "$work" data.json media
echo "Backup saved: $archive"
