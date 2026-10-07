#!/bin/zsh
set -euo pipefail

ROOT="${0:A:h:h:h}"
cd "$ROOT"
git config core.hooksPath system/scripts/hooks
actual="$(git config --get core.hooksPath)"
[[ "$actual" == "system/scripts/hooks" ]] || {
  print -u2 "bootstrap: core.hooksPath mismatch: $actual"
  exit 1
}
chmod +x system/scripts/hooks/pre-commit system/scripts/scan-secrets.sh
print "bootstrap: core.hooksPath=$actual"
