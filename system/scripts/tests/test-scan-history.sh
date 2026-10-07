#!/bin/zsh
set -euo pipefail
root="${0:A:h:h:h:h}"
output="$($root/system/scripts/scan-secrets.sh history 2>&1)"
print -r -- "$output"
print -r -- "$output" | /usr/bin/grep -q 'secret-scan: PASS (history)'
