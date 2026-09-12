#!/bin/zsh
set -euo pipefail
root="${0:A:h:h:h:h}"
fixture="$root/system/logs/staging/test-secret-patterns"
rm -rf "$fixture"
mkdir -p "$fixture/system/scripts"
cp "$root/system/scripts/scan-secrets.sh" "$fixture/system/scripts/scan-secrets.sh"
chmod +x "$fixture/system/scripts/scan-secrets.sh"
git -C "$fixture" init -q
print -r -- 'teacher-desk-live-inbox-calendar-todo.md' > "$fixture/manifest.tsv"
git -C "$fixture" add manifest.tsv
(cd "$fixture" && ./system/scripts/scan-secrets.sh staged)

token="sk-""proj-""abcdefghijklmnopqrstuvwxyz123456"
print -r -- "credential=$token" > "$fixture/secret.txt"
git -C "$fixture" add secret.txt
if (cd "$fixture" && ./system/scripts/scan-secrets.sh staged >/dev/null 2>&1); then
  print -u2 'scanner accepted a synthetic secret token'
  exit 1
fi
rm -rf "$fixture"
