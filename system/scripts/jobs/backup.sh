#!/bin/zsh
# Nightly backup of the brain. This repo has NO git remote, so this is the only
# recovery path. Two artifacts, both outside the repo (never nest a backup inside):
#   1. git bundle  — full history, restorable with `git clone <bundle>`
#   2. .env copy   — the one critical file git never tracks
# Keeps the last 14 of each. Simple by design (reform decision 2026-07-17).
set -euo pipefail
ROOT="${BRAIN_ROOT:-${0:A:h:h:h:h}}"
DEST="$HOME/ai-os-backups"
mkdir -p "$DEST"
stamp="$(/bin/date '+%Y-%m-%d')"

git -C "$ROOT" bundle create "$DEST/ai-os-$stamp.bundle" --all
/bin/cp "$ROOT/.env" "$DEST/env-$stamp"
/bin/chmod 600 "$DEST/env-$stamp"

# verify the bundle is restorable metadata-wise
git -C "$ROOT" bundle verify "$DEST/ai-os-$stamp.bundle" >/dev/null

# retention: newest 14 of each
ls -t "$DEST"/ai-os-*.bundle 2>/dev/null | tail -n +15 | while read -r old; do /bin/rm -f "$old"; done
ls -t "$DEST"/env-* 2>/dev/null | tail -n +15 | while read -r old; do /bin/rm -f "$old"; done

print "backup: PASS $DEST/ai-os-$stamp.bundle ($(du -h "$DEST/ai-os-$stamp.bundle" | cut -f1 | tr -d ' '))"
