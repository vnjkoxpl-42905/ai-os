#!/bin/zsh
set -euo pipefail

ROOT="${BRAIN_ROOT:-${0:A:h:h:h}}"
SCRIPT_ROOT="${BRAIN_SCRIPT_ROOT:-$ROOT}"
mode="${1:---check}"
evidence="$ROOT/system/generated/failure-injection.generated.tsv"

if [[ "$mode" == --self-test ]]; then
  "$ROOT/system/scripts/tests/test-automation.sh" >/dev/null
  print 'automation-failure self-test: PASS'
  exit 0
fi

if [[ "$mode" == --run ]]; then
  [[ -e "$ROOT/system/.phase8-done" ]] || { print -u2 'Phase 8 marker absent'; exit 1; }
  set +e
  BRAIN_NO_NOTIFY=1 BRAIN_JOB_MAX_SECONDS=30 "$SCRIPT_ROOT/system/scripts/run-job.sh" failure-probe >/dev/null 2>&1
  rc=$?
  set -e
  [[ "$rc" == 42 ]] || { print -u2 "unexpected failure-probe status: $rc"; exit 1; }
  rg -q $'failure-probe\tfailure\texit=42' "$ROOT/system/logs/automation.tsv"
  rg -q 'failure-probe: exit 42' "$ROOT/wiki/hot.md"
  mkdir -p "${evidence:h}"
  tmp="$evidence.tmp.$$"
  /usr/bin/printf 'timestamp\tprobe_exit\tlog_alert\thot_alert\n%s\t42\tpass\tpass\n' "$(date -u '+%Y-%m-%dT%H:%M:%SZ')" > "$tmp"
  mv "$tmp" "$evidence"
  print 'automation-failure-test: PASS injected exit=42 and observed log+hot alert'
  exit 0
fi

[[ -s "$evidence" ]] || { print -u2 'failure-injection evidence missing'; exit 1; }
rg -q $'failure-probe\tfailure\texit=42' "$ROOT/system/logs/automation.tsv"
# Deliberately NOT asserting the hot.md alert here. That block is single-slot and
# replace-only by design (automation-lib.sh:brain_alert), and it is now cleared
# when a job recovers — so any later alert or recovery legitimately erases the
# probe's line. --run asserts the alert at the moment it fires, which is the only
# point it is guaranteed observable; this durable evidence is what survives.
print 'automation-failure-test: PASS evidence+log alert present'
