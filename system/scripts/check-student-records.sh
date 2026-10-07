#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
STUDENTS="$ROOT/students"
errors=0

for dir in "$STUDENTS"/*/; do
  [ -d "$dir" ] || continue
  slug="$(basename "$dir")"
  case "$slug" in
    _templates|"previous transcripts ") continue ;;
    former-students)
      # Container of former-student folders: lighter schema (generated records
      # only, no active-only primaries). profile.generated.md is the one
      # required file; generated files must carry the generated marker.
      for fdir in "$dir"*/; do
        [ -d "$fdir" ] || continue
        fslug="$(basename "$fdir")"
        if [ ! -f "$fdir/profile.generated.md" ]; then
          printf 'MISSING former-students/%s/profile.generated.md\n' "$fslug"
          errors=$((errors + 1))
        fi
        for gen in "$fdir"*.generated.md; do
          [ -f "$gen" ] || continue
          if ! rg -q '^generated: true$' "$gen"; then
            printf 'INVALID generated marker former-students/%s/%s\n' "$fslug" "$(basename "$gen")"
            errors=$((errors + 1))
          fi
        done
      done
      continue ;;
  esac

  for file in "$slug.md" transcripts.md assignment-log.md teaching-notes.md open-loops.md live-status.generated.md; do
    if [ ! -f "$dir/$file" ]; then
      printf 'MISSING %s/%s\n' "$slug" "$file"
      errors=$((errors + 1))
    fi
  done

  if [ -f "$dir/live-status.generated.md" ] && ! rg -q '^generated: true$' "$dir/live-status.generated.md"; then
    printf 'INVALID generated marker %s/live-status.generated.md\n' "$slug"
    errors=$((errors + 1))
  fi

  if [ -d "$dir/sessions" ]; then
    while IFS= read -r session; do
      [ -d "$session" ] || continue
      for file in transcript.md summary.md topic-map.md; do
        if [ ! -f "$session/$file" ]; then
          printf 'INCOMPLETE %s/%s/%s\n' "$slug" "${session#"$dir"}" "$file"
          errors=$((errors + 1))
        fi
      done
    done < <(find "$dir/sessions" -mindepth 1 -maxdepth 1 -type d -print)
  fi
done

if [ "$errors" -gt 0 ]; then
  printf '%s student-record issue(s) found.\n' "$errors"
  exit 1
fi

printf 'Student-record structure is complete for all active student folders.\n'
