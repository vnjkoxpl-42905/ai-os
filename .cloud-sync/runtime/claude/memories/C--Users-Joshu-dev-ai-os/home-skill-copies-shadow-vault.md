---
name: home-skill-copies-shadow-vault
description: "Claude Code loads ~/.claude/skills over the vault's .claude/skills; after a catalog edit, sync every installed copy or the edit never runs."
metadata:
  node_type: memory
  type: project
  originSessionId: 38a93a63-e397-478e-9df6-b7085bedd58f
  modified: 2026-10-12T05:23:08.133Z
---

Claude Code loads `~/.claude/skills/<name>` instead of the vault's `.claude/skills/<name>` when both exist (observed 2026-10-12: this session's listing showed the home `bootcamp-builder` description, not the newer vault copy). Editing only `skills/claude/` or the vault activation changes nothing for Claude while a home copy exists.

**Why:** On 2026-10-12, 142 home copies differed from `skills/claude` while `check-skills.sh` reported PASS. The copies that actually ran carried wrong facts: Ctrl+Space instead of Left Alt for Superwhisper, wrapup writing log entries at the top, `~/ai-os` paths, automatic push after a green build.

**How to apply:** After editing a catalog skill, run `python audits/skills-2026-10-12-karpathy/sync_loaded_copies.py <skill>` from the vault root (backs up what it overwrites), then `sh system/scripts/check-skills.sh`. That check now fails on a shadowed vault copy and warns with a drift count. Home dispatchers (`ingest`, `second-brain-*`) and the `assign-lsatu-work` pointer pair are intentional. Codex precedence is untested; identical copies make it irrelevant. Related: [[skill-listing-budget]].
