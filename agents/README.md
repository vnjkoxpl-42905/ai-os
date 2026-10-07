# Agents — master database

Master database for agent definitions, mirroring the `skills/` model: inert storage, split into `claude/` and `codex/`, with frozen Claude vendor snapshots and generated Codex TOML equivalents. `INDEX.md` indexes it.

**Reality of this set:** standalone agents are mostly plugin-provided. `claude/` holds the stable installed-plugin agents, each named `<plugin>-<agent>.md` for provenance and collision safety (for example, `feature-dev-code-reviewer.md` vs `pr-review-toolkit-code-reviewer.md`), plus a frozen `_snapshots/` copy. `codex/` holds the authored Codex agents and generated TOML equivalents. Generated TOML files use the collision-safe filename as the agent name and are activated in `.codex/agents/`. Skill-internal sub-agents are not cataloged here because they travel with their skill.

Refresh and validate the Codex equivalents with `python system/scripts/consolidate-agents-commands.py` from the repository root.
