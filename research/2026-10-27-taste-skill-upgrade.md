# Taste Skill v2 replaced the older preset

2026-10-27. Source: https://github.com/Leonxlnx/taste-skill, commit `12af471f627f866411b4bd785b19646d3672784c`, `skills/taste-skill`. All 39 tracked upstream files copied. The upstream SKILL.md has only a short AI OS project-authority contract added; the old body is gone.

Updated seven copies: `skills/claude`, `skills/codex`, `.claude/skills`, `.agents/skills` under ai-os, and existing home `.claude/skills`, `.agents/skills`, `.codex/skills`, each under `design-taste-frontend`. Supporting files hash-match upstream; all installed entrypoints match each other. Previous seven copies preserved at `C:/Users/Joshu/dev/ai-os-projects/_skill-backups/20261027-taste-v2`; source checkout lives at sibling `taste-skill`.

Validation: 10 Node module syntax checks passed; deterministic page options and full page draw passed; app kind listing and full workspace draw passed; HTML lint fixture passed. Independent skill reviewer found no material local defects. Whole-catalog check-skills failed on seven unrelated current findings: cli-anything-aios parity and six CLAUDE.md peers under a preserved Supabase node_modules link in handoffs. No Taste finding.

Known upstream limitation: documented individual scroll scenes, demos and library/scenes.json are absent in this upstream commit. Page draw handles the absence, but scroll-scene support is not verified. Browser inspection and network image workflow were not run. No commit or push.

The related TasteCode download was separately checked by the parent task against the official latest v0.1.1 release and exact release hash; no app installation was authorized or performed as part of this skill replacement.
