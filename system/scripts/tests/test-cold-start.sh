#!/bin/zsh
set -euo pipefail

ROOT="${0:A:h:h:h:h}"
"$ROOT/system/scripts/cold-start-check.sh" --self-test
print 'test-cold-start: PASS'
