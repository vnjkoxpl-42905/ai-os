#!/bin/zsh
# Atomically replace TARGET only if its current SHA-256 equals EXPECTED.
set -euo pipefail

[[ $# == 3 ]] || { print -u2 'usage: cas-replace.sh TARGET EXPECTED_SHA TEMP_FILE'; exit 2; }
target="$1"
expected="$2"
candidate="$3"
[[ -f "$candidate" ]] || { print -u2 'candidate missing'; exit 1; }
current="$([[ -f "$target" ]] && /usr/bin/shasum -a 256 "$target" | /usr/bin/awk '{print $1}' || print MISSING)"
[[ "$current" == "$expected" ]] || { print -u2 'compare-and-swap conflict'; exit 75; }
[[ "${candidate:h}" == "${target:h}" ]] || {
  same_dir="${target:h}/.${target:t}.cas.$$"
  /bin/cp "$candidate" "$same_dir"
  candidate="$same_dir"
}
/bin/chmod 644 "$candidate" 2>/dev/null || true
/bin/mv -f "$candidate" "$target"

