#!/bin/zsh
set -euo pipefail

ROOT="${0:A:h:h:h:h}"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
mkdir -p "$tmp/system/logs" "$tmp/system/scripts/jobs" "$tmp/wiki" "$tmp/raw/inbox"
print -n 'old' > "$tmp/target"
print -n 'new' > "$tmp/candidate"
old_hash="$(shasum -a 256 "$tmp/target" | awk '{print $1}')"

BRAIN_ROOT="$tmp" "$ROOT/system/scripts/cas-replace.sh" "$tmp/target" "$old_hash" "$tmp/candidate"
[[ "$(<"$tmp/target")" == new ]]
print -n 'candidate' > "$tmp/candidate"
if BRAIN_ROOT="$tmp" "$ROOT/system/scripts/cas-replace.sh" "$tmp/target" "$old_hash" "$tmp/candidate" 2>/dev/null; then
  print -u2 'CAS accepted a stale target hash'
  exit 1
fi

print -n '# hot' > "$tmp/wiki/hot.md"
BRAIN_ROOT="$tmp" BRAIN_SCRIPT_ROOT="$ROOT" "$ROOT/system/scripts/run-job.sh" session-guard
[[ ! -e "$tmp/system/.phase8-done" ]]
grep -q $'session-guard\tinactive' "$tmp/system/logs/automation.tsv"

if BRAIN_ROOT="$tmp" BRAIN_SCRIPT_ROOT="$ROOT" BRAIN_AUTOMATION_TEST=1 BRAIN_NO_NOTIFY=1 \
  "$ROOT/system/scripts/run-job.sh" failure-probe 2>/dev/null; then
  print -u2 'failure probe unexpectedly passed'
  exit 1
fi
grep -q $'failure-probe\tfailure' "$tmp/system/logs/automation.tsv"
grep -q '<!-- brain-automation-alerts:start -->' "$tmp/wiki/hot.md"

print 'automation: PASS'
