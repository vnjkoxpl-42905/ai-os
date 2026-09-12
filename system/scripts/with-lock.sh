#!/bin/zsh
set -u

[[ $# -ge 4 ]] || { print -u2 'usage: with-lock.sh JOB ACQUIRE_SECONDS MAX_SECONDS COMMAND...'; exit 2; }
ROOT="${BRAIN_ROOT:-${0:A:h:h:h}}"
SCRIPT_ROOT="${BRAIN_SCRIPT_ROOT:-$ROOT}"
job="$1"
acquire="$2"
maximum="$3"
shift 3
source "$SCRIPT_ROOT/system/scripts/automation-lib.sh"

/usr/bin/lockf -t "$acquire" "$ROOT/system/.lock" "$SCRIPT_ROOT/system/scripts/watchdog.sh" "$maximum" "$@"
result=$?
if (( result == 0 )); then
  brain_log "$job" success 'completed'
  brain_alert_clear "$job" || true
  brain_rotate_logs_dir || true
elif (( result == 75 )); then
  brain_log "$job" skipped 'lock contention or compare-and-swap conflict; retry on next schedule'
else
  brain_log "$job" failure "exit=$result"
  brain_alert "$job" "exit $result" || true
fi
exit "$result"
