#!/bin/zsh
set -euo pipefail
ROOT="${0:A:h:h:h}"

[[ -x /usr/bin/lockf ]] || { print -u2 'native lockf missing'; exit 1; }
for script in "$ROOT"/system/scripts/*.sh "$ROOT"/system/scripts/jobs/*.sh; do
  zsh -n "$script"
done
# the plists are the source of truth for which jobs exist. A hardcoded count and
# a hardcoded label list both go stale the moment a job is added — that is exactly
# how memory-index shipped in a264514..4dad395 while this gate still asserted 7.
# Two prefixes are live: the legacy com.joshua.brain.* (backup) and the current
# com.joshua.ai-os.* (everything since the rename). Stripping one hardcoded
# prefix silently mislabels the other, so take the job name as the final
# dot-component and keep the full label for the launchctl lookup.
typeset -a labels jobs
integer plists=0
for plist in "$ROOT"/system/launchd/*.plist(N); do
  /usr/bin/plutil -lint "$plist" >/dev/null
  labels+=("${plist:t:r}")
  jobs+=("${${plist:t:r}##*.}")
  (( plists += 1 ))
done
# a self-test that asserts nothing is worse than no self-test
(( plists > 0 )) || { print -u2 'no launchd plists found; nothing verified'; exit 1; }
for job in $jobs; do
  [[ -x "$ROOT/system/scripts/jobs/$job.sh" ]] || { print -u2 "plist has no job script: $job"; exit 1; }
done
"$ROOT/system/scripts/tests/test-automation.sh" >/dev/null
if [[ -e "$ROOT/system/.phase8-done" ]]; then
  integer loaded=0
  for label in $labels; do
    /bin/launchctl print "gui/$UID/$label" >/dev/null 2>&1 || { print -u2 "launchd job missing: $label"; exit 1; }
    (( loaded += 1 ))
  done
  print "automation-self-test: PASS ($loaded valid loaded plists; lock/CAS/watchdog/failure alert verified)"
else
  if /bin/launchctl list 2>/dev/null | /usr/bin/grep -q 'com.joshua.brain'; then
    print -u2 'brain launchd jobs loaded before Phase 8 marker'
    exit 1
  fi
  print "automation-self-test: PASS ($plists valid unloaded plists; lock/CAS/watchdog/failure alert verified)"
fi
