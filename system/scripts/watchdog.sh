#!/bin/zsh
set -u

[[ $# -ge 2 ]] || { print -u2 'usage: watchdog.sh MAX_SECONDS COMMAND...'; exit 2; }
max_seconds="$1"
shift
"$@" &
child=$!
(
  /bin/sleep "$max_seconds"
  /bin/kill -TERM "$child" 2>/dev/null || exit 0
  /bin/sleep 5
  /bin/kill -KILL "$child" 2>/dev/null || true
) &
timer=$!
wait "$child"
result=$?
# The timer's sleep must die first: killing only the subshell orphans the sleep
# to PID 1, where it holds the job's stdout open for the rest of max_seconds.
/usr/bin/pkill -P "$timer" 2>/dev/null || true
/bin/kill "$timer" 2>/dev/null || true
wait "$timer" 2>/dev/null || true
exit "$result"

