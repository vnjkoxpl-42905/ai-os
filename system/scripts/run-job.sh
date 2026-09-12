#!/bin/zsh
set -euo pipefail

ROOT="${BRAIN_ROOT:-${0:A:h:h:h}}"
SCRIPT_ROOT="${BRAIN_SCRIPT_ROOT:-$ROOT}"
export BRAIN_ROOT="$ROOT"
export BRAIN_SCRIPT_ROOT="$SCRIPT_ROOT"
export PATH='/usr/local/bin:/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin'
source "$SCRIPT_ROOT/system/scripts/automation-lib.sh"
job="${1:?job name required}"
shift || true

if [[ ! -e "$ROOT/system/.phase8-done" && "${BRAIN_AUTOMATION_TEST:-}" != 1 ]]; then
  brain_log "$job" inactive 'Phase 8 marker absent; safe no-op'
  exit 0
fi
script="$SCRIPT_ROOT/system/scripts/jobs/$job.sh"
[[ -x "$script" ]] || { brain_log "$job" failure 'job script missing'; exit 127; }
exec "$SCRIPT_ROOT/system/scripts/with-lock.sh" "$job" 5 "${BRAIN_JOB_MAX_SECONDS:-900}" "$script" "$@"
