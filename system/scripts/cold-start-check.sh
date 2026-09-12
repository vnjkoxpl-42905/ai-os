#!/bin/zsh
set -euo pipefail

ROOT="${BRAIN_ROOT:-${0:A:h:h:h}}"
RUNTIME_HOME="${BRAIN_RUNTIME_HOME:-$HOME}"

check_cold_start() {
  local runtime cwd pickup adapter
  # This list tracks the CURRENT architecture, not the original one. Four former
  # requirements were retired by deliberate reform commits and must not come
  # back: README.md and HOW-THIS-OS-WORKS.md (11ae157), root MEMORY.md and
  # system/schema/core.md (c3bd811 — memory moved to native automemory, the
  # schema generator was retired in favour of hand-edited routers). The check
  # kept asserting all four long after they were gone, which is why a cold start
  # failed against the real vault while the fixture-based test passed.
  for required in CONTEXT.md connections.md decisions/log.md wiki/tasks.md wiki/hot.md wiki/dashboard.md wiki/index.md wiki/log.md; do
    [[ -s "$ROOT/$required" ]] || { print -u2 "cold-start required file missing: $required"; return 1; }
  done
  # core.md: global roots hold only a tiny always-on set; everything else is
  # activated per-project. pickup is a brain-scoped skill, so the project
  # activation is the correct one — accept either, global first.
  for runtime in claude codex; do
    if [[ "$runtime" == claude ]]; then
      pickup="$RUNTIME_HOME/.claude/skills/pickup/SKILL.md"
      [[ -s "$pickup" ]] || pickup="$ROOT/.claude/skills/pickup/SKILL.md"
      adapter="$ROOT/CLAUDE.md"
    else
      pickup="$RUNTIME_HOME/.agents/skills/pickup/SKILL.md"
      [[ -s "$pickup" ]] || pickup="$ROOT/.agents/skills/pickup/SKILL.md"
      adapter="$ROOT/AGENTS.md"
    fi
    [[ -s "$adapter" && -s "$pickup" ]] || { print -u2 "$runtime cold-start discovery missing"; return 1; }
    rg -q '(~/ai-os|/Users/joshuaf/ai-os)' "$pickup" || { print -u2 "$runtime pickup does not target brain"; return 1; }
    if rg -q '(Obsidian Vault|Documents/AI GATHER|Documents/Claude)' "$pickup"; then
      print -u2 "$runtime pickup retains old path"
      return 1
    fi
    for cwd in "$ROOT" "$ROOT/students"; do
      if [[ "${BRAIN_COLD_START_TEST:-0}" != 1 ]]; then
        [[ "$(git -C "$cwd" rev-parse --show-toplevel 2>/dev/null)" == "$ROOT" ]] || { print -u2 "$runtime nested Git orientation failed: $cwd"; return 1; }
      fi
      print "PASS cold-start runtime=$runtime cwd=$cwd pickup=oriented mode=static-resolution"
    done
  done
}

if [[ "${1:-}" == --self-test ]]; then
  tmp="$(mktemp -d "${TMPDIR:-/tmp}/brain-cold-start.XXXXXX")"
  trap "rm -rf -- ${(q)tmp}" EXIT
  brain="$tmp/brain"
  home="$tmp/home"
  mkdir -p "$brain/wiki" "$brain/students" "$brain/decisions" "$home/.claude/skills/pickup" "$home/.agents/skills/pickup"
  for required in CONTEXT.md connections.md CLAUDE.md AGENTS.md; do print fixture > "$brain/$required"; done
  for required in tasks.md hot.md dashboard.md index.md log.md; do print fixture > "$brain/wiki/$required"; done
  print fixture > "$brain/decisions/log.md"
  print 'Vault root: `~/ai-os`.' > "$home/.claude/skills/pickup/SKILL.md"
  print 'Vault root: `~/ai-os`.' > "$home/.agents/skills/pickup/SKILL.md"
  BRAIN_ROOT="$brain" BRAIN_RUNTIME_HOME="$home" BRAIN_COLD_START_TEST=1 "$0" >/dev/null
  print 'cold-start self-test: PASS'
  exit 0
fi

check_cold_start
