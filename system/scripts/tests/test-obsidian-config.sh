#!/bin/zsh
set -euo pipefail
root="${0:A:h:h:h:h}"
for name in app.json appearance.json core-plugins.json hotkeys.json community-plugins.json; do
  /usr/bin/ruby -rjson -e 'JSON.parse(File.read(ARGV[0]))' "$root/.obsidian/$name"
done
# community plugins are user-managed (12 enabled as of 2026-07-17); assert the file is a valid JSON array
/usr/bin/ruby -rjson -e 'exit(JSON.parse(File.read(ARGV[0])).is_a?(Array) ? 0 : 1)' "$root/.obsidian/community-plugins.json"
[[ -s "$root/system/reviews/karpathywiki-review.md" ]]
# workspace.json is created whenever the vault is open in Obsidian and is git-ignored — no assertion.
