#!/bin/zsh
set -euo pipefail

ROOT="${0:A:h:h:h:h}"
"$ROOT/system/scripts/automation-failure-test.sh" --self-test
print 'test-failure-injection: PASS'
