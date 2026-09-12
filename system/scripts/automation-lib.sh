#!/bin/zsh
# Sourced library: callers choose errexit behavior; nounset remains enforced.
set -u

BRAIN_ROOT="${BRAIN_ROOT:-${0:A:h:h:h}}"
BRAIN_SCRIPT_ROOT="${BRAIN_SCRIPT_ROOT:-$BRAIN_ROOT}"
LOG_DIR="$BRAIN_ROOT/system/logs"
LOG_FILE="$LOG_DIR/automation.tsv"

brain_hash() {
  local filepath="$1"
  [[ -f "$filepath" ]] && /usr/bin/shasum -a 256 "$filepath" | /usr/bin/awk '{print $1}' || print 'MISSING'
}

brain_redact() {
  /usr/bin/sed -E \
    -e "s#${HOME//\//\\/}#~#g" \
    -e 's/((api[_-]?key|access[_-]?token|auth[_-]?token|password)[[:space:]]*[:=])[[:space:]]*[^[:space:]]+/\1<redacted>/Ig' \
    -e 's/(sk-(proj-)?[0-9A-Za-z_-]{12})[0-9A-Za-z_-]*/\1<redacted>/g'
}

# Rotate at 10 MB keeping 5 generations (approved 2026-07-16, STEP2 §6).
BRAIN_LOG_ROTATE_BYTES=10485760
BRAIN_LOG_ROTATE_KEEP=5

brain_rotate_log() {
  local logfile="$1" i
  [[ -f "$logfile" ]] || return 0
  (( $(/usr/bin/stat -f %z "$logfile") < BRAIN_LOG_ROTATE_BYTES )) && return 0
  /bin/rm -f "$logfile.$BRAIN_LOG_ROTATE_KEEP"
  for (( i = BRAIN_LOG_ROTATE_KEEP - 1; i >= 1; i-- )); do
    [[ -f "$logfile.$i" ]] && /bin/mv "$logfile.$i" "$logfile.$((i + 1))"
  done
  /bin/mv "$logfile" "$logfile.1"
}

# launchd keeps its stdout/stderr files open, so a mv would leave the daemon
# writing to the rotated inode forever; copy-then-truncate keeps the fd valid.
brain_rotate_logs_dir() {
  local logfile i
  for logfile in "$LOG_DIR"/*.log(N) "$LOG_DIR"/*.tsv(N); do
    [[ "$logfile" == "$LOG_FILE" ]] && continue  # brain_log rotates this one itself
    (( $(/usr/bin/stat -f %z "$logfile") < BRAIN_LOG_ROTATE_BYTES )) && continue
    /bin/rm -f "$logfile.$BRAIN_LOG_ROTATE_KEEP"
    for (( i = BRAIN_LOG_ROTATE_KEEP - 1; i >= 1; i-- )); do
      [[ -f "$logfile.$i" ]] && /bin/mv "$logfile.$i" "$logfile.$((i + 1))"
    done
    /bin/cp "$logfile" "$logfile.1" && : > "$logfile"
  done
  return 0
}

brain_log() {
  local job="$1" result="$2" message="${3:-}"
  /bin/mkdir -p "$LOG_DIR"
  /bin/chmod 700 "$LOG_DIR"
  brain_rotate_log "$LOG_FILE"
  local cleaned
  cleaned="$(print -r -- "$message" | brain_redact | /usr/bin/tr '\n\t' '  ')"
  print -r -- "$(/bin/date -u '+%Y-%m-%dT%H:%M:%SZ')"$'\t'"$job"$'\t'"$result"$'\t'"$cleaned" >> "$LOG_FILE"
  /bin/chmod 600 "$LOG_FILE"
}

brain_alert() {
  local job="$1" message="$2" target="$BRAIN_ROOT/wiki/hot.md" attempt expected tmp
  for attempt in 1 2 3; do
    expected="$(brain_hash "$target")"
    tmp="${target}.automation.$$"
    /usr/bin/awk -v line="- $(/bin/date -u '+%Y-%m-%dT%H:%M:%SZ') — ${job}: ${message}" '
      BEGIN { in_block=0; found=0 }
      /<!-- brain-automation-alerts:start -->/ { found=1; in_block=1; print; print line; next }
      /<!-- brain-automation-alerts:end -->/ { in_block=0; print; next }
      !in_block { print }
      END { if (!found) { print ""; print "<!-- brain-automation-alerts:start -->"; print line; print "<!-- brain-automation-alerts:end -->" } }
    ' "$target" > "$tmp"
    if "$BRAIN_SCRIPT_ROOT/system/scripts/cas-replace.sh" "$target" "$expected" "$tmp"; then
      if [[ "${BRAIN_NO_NOTIFY:-0}" != 1 ]]; then
        /usr/bin/osascript -e "display notification \"Brain automation failed: $job\" with title \"Joshua's brain\"" >/dev/null 2>&1 || true
      fi
      return 0
    fi
    /bin/rm -f "$tmp"
  done
  return 1
}

# hot.md is the first thing /pickup reads, and brain_alert only ever fires on
# failure — so a job that failed once and has since recovered kept advertising a
# resolved failure until some *other* job happened to fail and overwrite the slot.
# Clearing on success is what makes the alert block mean "broken right now".
brain_alert_clear() {
  local job="$1" target="$BRAIN_ROOT/wiki/hot.md" attempt expected tmp
  [[ -f "$target" ]] || return 0
  /usr/bin/grep -q -- "— ${job}:" "$target" || return 0
  for attempt in 1 2 3; do
    expected="$(brain_hash "$target")"
    tmp="${target}.automation.$$"
    /usr/bin/awk -v job="$job" '
      BEGIN { in_block=0 }
      /<!-- brain-automation-alerts:start -->/ { in_block=1; print; next }
      /<!-- brain-automation-alerts:end -->/ { in_block=0; print; next }
      in_block && index($0, "— " job ":") { next }
      { print }
    ' "$target" > "$tmp"
    if "$BRAIN_SCRIPT_ROOT/system/scripts/cas-replace.sh" "$target" "$expected" "$tmp"; then return 0; fi
    /bin/rm -f "$tmp"
  done
  return 1
}

brain_fenced_prepend() {
  local target="$1" fence="$2" line="$3" attempt expected tmp
  for attempt in 1 2 3; do
    expected="$(brain_hash "$target")"
    tmp="${target}.fence.$$"
    /usr/bin/awk -v start="<!-- ${fence}:start -->" -v finish="<!-- ${fence}:end -->" -v line="$line" '
      BEGIN { in_block=0; found=0 }
      $0 == start { found=1; in_block=1; print; print line; next }
      $0 == finish { in_block=0; print; next }
      !in_block { print }
      END { if (!found) { print ""; print start; print line; print finish } }
    ' "$target" > "$tmp"
    if "$BRAIN_SCRIPT_ROOT/system/scripts/cas-replace.sh" "$target" "$expected" "$tmp"; then return 0; fi
    /bin/rm -f "$tmp"
  done
  return 75
}
