# Skills — master database

This is the **master database** for skills across Joshua's whole setup — every authored, project, and vendor/plugin skill from every root (Claude, Codex, plugins, per-project `.claude/` and `.agents/`), unioned in one place.

## Storage model

- **Inert.** Nothing here auto-loads. A skill only runs when it's *activated* — **copied** (not symlinked, since 2026-07-17) into a project's `.claude/skills/` or `.agents/skills/` (or into the conservative global roots). This directory is search-and-storage, not a load path. A copy doesn't auto-follow edits to the DB source — re-copy after editing a skill here; `system/scripts/check-skills.sh` flags any activation whose `SKILL.md` has drifted.
- **Split by tool origin, always.** Skills are filed under `claude/` or `codex/` depending on which tool's root they came from — **never merged into one shared folder, even when the content is byte-identical.** If a skill exists for both tools, it gets one entry under each: `claude/<name>/` and `codex/<name>/`. This keeps each tool's set independently editable without silently forking a shared file.
- **A+B for vendor/plugin skills.** A vendor or plugin skill gets (A) a live symlink under `claude/<name>/` or `codex/<name>/` pointing at its real location in the plugin, so it always reflects the installed version, **and** (B) a frozen copy under `claude/_snapshots/<name>/` or `codex/_snapshots/<name>/` for point-in-time reference. Snapshots are refreshed manually, not on a schedule — re-run the refresh only when asked.
- **Authored and project skills** are real files, source of truth, filed the same way under `claude/<name>/` or `codex/<name>/`.

## Which copy actually runs

- **Claude Code loads `~/.claude/skills` before the vault's `.claude/skills`.** When both hold a skill, the home copy wins (observed 2026-10-12: the session listing showed the home `bootcamp-builder`, not the newer vault copy). Editing only the catalog or the vault activation changes nothing for Claude while a home copy exists. Codex loads `~/.agents/skills`, `~/.codex/skills` and the vault's `.agents/skills`.
- After editing a catalog skill, make every installed copy match it: `python audits/skills-2026-10-12-karpathy/sync_loaded_copies.py <skill> ...` (backs up what it overwrites, never creates new activations). Home copies that are deliberate dispatchers or pointers (`ingest`, `second-brain-*`, `assign-lsatu-work`) stay as they are.
- `check-skills.sh` fails on a shadowed vault copy and warns with a count of home copies that differ from the catalog.

## Listing budget

Claude Code gives skill descriptions 1% of the context window by default and hands them out by recent use, then listing order. With ~400 skills that left most of Joshua's own operational skills listed by name only. The vault's `.claude/settings.json` therefore raises `skillListingBudgetFraction` to 0.015, hides never-used vendor packs from the model (`user-invocable-only`, still runnable as `/name`), and lists never-used generic skills by name only. Regenerate after the working set changes: edit `audits/skills-2026-10-12-karpathy/name-only.json`, then run `python audits/skills-2026-10-12-karpathy/listing_overrides.py`. A skill listed by name only that starts getting used should come off that list.

## Save-to-both

Creating a new skill (via skill-creator or by hand) always writes to **both**: the current project's `.claude/skills/` (or `.agents/skills/`) **and** this DB, every time, unconditionally. New skills are project-scoped by default — never auto-promoted to global.

## Finding things

- `claude/README.md` and `codex/README.md` index that tool's skills.
- `INDEX.md` (once generated) is the full one-line-per-skill index across both, grouped by source-type.

See [PARITY.md](PARITY.md) for runtime decisions and [the decision log](../decisions/log.md) for the consolidation rationale.
