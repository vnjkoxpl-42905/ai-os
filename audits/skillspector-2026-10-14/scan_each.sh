#!/usr/bin/env bash
# Scan every skill folder on its own with SkillSpector static mode (--no-llm).
# A recursive scan stops after a 32-skill budget, so each skill gets its own run.
# usage: bash scan_each.sh <skills-root> <label>
root="$1"; label="$2"; out="$(dirname "$0")/$label"; mkdir -p "$out"
for d in "$root"/*/; do
  [ -f "$d/SKILL.md" ] || continue
  name=$(basename "$d"); real=$(cd "$d" && pwd -P)
  printf '%s\t%s\t%s\n' "$name" "$real" "$out"
done | xargs -P 8 -d '\n' -I{} bash -c '
  IFS=$'"'"'\t'"'"' read -r name real out <<< "{}"
  skillspector scan "$real" --no-llm --format json -o "$out/$name.json" > "$out/$name.log" 2>&1
  echo "$name rc=$?" >> "$out/_exit-codes.txt"'
echo "$label done: $(wc -l < "$out/_exit-codes.txt") scans"
