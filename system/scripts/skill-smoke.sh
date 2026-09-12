#!/bin/zsh
# Runtime skill discovery smoke test.
#
# Supersedes the pre-2026-07-15 version, which asserted exactly 11 named skills
# lived at the flat skills/<name> path and were symlinked into the global roots.
# Commit a264514 retired the flat layout for the claude/ + codex/ split, and
# core.md:58 keeps the global roots to a tiny always-on set — so that check
# could never pass again. DB-model validation now lives in check-skills.py;
# this script keeps the distinct job its name implies: whatever is *activated*
# must actually resolve and be discoverable by a runtime, from root and nested
# cwd. It audits the activated set rather than a hardcoded list, so activating
# or retiring a skill does not require editing this file.
set -euo pipefail

# :A on both sides or neither — ${destination:A} canonicalizes, so a ROOT given
# as a symlinked path (/tmp vs /private/tmp) would skip every activation.
ROOT="${${BRAIN_ROOT:-${0:A:h:h:h}}:A}"
RUNTIME_HOME="${BRAIN_RUNTIME_HOME:-$HOME}"

for runtime in claude codex; do
  if [[ "$runtime" == claude ]]; then
    adapter="$ROOT/CLAUDE.md"
    roots=("$ROOT/.claude/skills" "$RUNTIME_HOME/.claude/skills")
    subtree=claude
  else
    adapter="$ROOT/AGENTS.md"
    roots=("$ROOT/.agents/skills" "$RUNTIME_HOME/.agents/skills")
    subtree=codex
  fi
  [[ -s "$adapter" ]] || { print -u2 "$runtime adapter missing: $adapter"; exit 1; }

  integer checked=0
  for base in $roots; do
    [[ -d "$base" ]] || continue
    for destination in "$base"/*(N); do
      # only audit DB-backed activations; a runtime's own local skills are its business
      [[ -L "$destination" ]] || continue
      resolved="${destination:A}"
      [[ "$resolved" == "$ROOT/skills/"* ]] || continue
      name="${destination:t}"
      [[ "$resolved" == "$ROOT/skills/$subtree/"* ]] || {
        print -u2 "$runtime activation crosses subtree: $destination -> $resolved"; exit 1; }
      [[ -s "$destination/SKILL.md" ]] || {
        print -u2 "$runtime explicit discovery missing: $name"; exit 1; }
      rg -q "^name: ['\"]?${name}['\"]?$" "$destination/SKILL.md" || {
        print -u2 "$runtime implicit name mismatch: $name"; exit 1; }
      rg -q '^description: .+' "$destination/SKILL.md" || {
        print -u2 "$runtime implicit description missing: $name"; exit 1; }
      (( checked += 1 ))
    done
  done

  # a smoke test that verifies nothing is worse than no smoke test
  (( checked > 0 )) || { print -u2 "$runtime no DB-backed activations found; nothing verified"; exit 1; }

  for cwd in "$ROOT" "$ROOT/students"; do
    [[ "$cwd" == "$ROOT" || "$cwd" == "$ROOT"/* ]] || { print -u2 "cwd escaped brain: $cwd"; exit 1; }
    [[ -d "$cwd" ]] || { print -u2 "$runtime cwd missing: $cwd"; exit 1; }
    print "PASS skill-smoke runtime=$runtime cwd=$cwd activated=$checked mode=static-resolution"
  done
done
