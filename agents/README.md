# Agents — master database

Master database for agent definitions, mirroring the `skills/` model: inert storage, split into `claude/` and `codex/`, vendor items as live symlink + `_snapshots/` frozen copy, save-to-both on creation. `INDEX.md` indexes it.

**Reality of this set:** standalone agents are almost entirely plugin-provided. `claude/` holds the stable installed-plugin agents (from `~/.claude/plugins/marketplaces/…`), each named `<plugin>-<agent>.md` for provenance and collision-safety (e.g. `feature-dev-code-reviewer.md` vs `pr-review-toolkit-code-reviewer.md`), as a symlink into the plugin plus a `_snapshots/` copy. `codex/` holds the authored Codex agents (`web-researcher.toml`, `web-search-modules/`). Skill-internal sub-agents (e.g. `skill-creator/agents/*`) are NOT cataloged here — they travel with their skill in the skills DB.

Populated/refreshed by `system/scripts/consolidate-agents-commands.py`. See `/Users/joshuaf/ai-os/PLAN.md`.
