#!/bin/zsh
# Runs the test suite under system/scripts/tests/.
#
# Why this exists: every test here was written to protect an invariant, and until
# 2026-07-16 exactly one of eighteen was wired into any runner. The other
# seventeen silently rotted — test-schema-sync.sh had been asserting a Tier A
# policy that was amended out from under it, and nothing noticed, because nothing
# ran it. A test nothing runs is a comment.
#
# Usage: run-tests.sh [--list]
set -uo pipefail

ROOT="${${BRAIN_ROOT:-${0:A:h:h:h}}:A}"
TESTS="$ROOT/system/scripts/tests"

# Skipped tests are named here with a reason and reported on every run. A silent
# skip reads as a pass; that is how a suite lies.
typeset -A SKIP

if [[ "${1:-}" == --list ]]; then
  for test in "$TESTS"/*.sh(N); do print -r -- "${test:t}"; done
  exit 0
fi

integer passed=0 failed=0 skipped=0
typeset -a failures
for test in "$TESTS"/*.sh(N); do
  name="${test:t}"
  if [[ -n "${SKIP[$name]:-}" ]]; then
    print -r -- "SKIP  $name — ${SKIP[$name]}"
    (( skipped += 1 ))
    continue
  fi
  if output="$(zsh "$test" 2>&1)"; then
    print -r -- "PASS  $name"
    (( passed += 1 ))
  else
    print -r -- "FAIL  $name — ${$(print -r -- "$output" | /usr/bin/tail -1)}"
    failures+=("$name")
    (( failed += 1 ))
  fi
done

# a suite that verifies nothing is worse than no suite
(( passed + failed > 0 )) || { print -u2 'run-tests: no tests found; nothing verified'; exit 1; }
print -- "run-tests: $passed passed, $failed failed, $skipped skipped"
(( failed == 0 )) || { print -u2 "run-tests: FAIL ${failures[*]}"; exit 1; }
print 'run-tests: PASS'
