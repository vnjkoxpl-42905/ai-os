---
type: source
subject: Claude Jargon Fixer guide
created: 2026-10-29
updated: 2026-10-29
aliases: [Jargon Fixer, Claude plain language guide]
tags: [llm-wiki, ai-workspace]
evidence: ../../raw/sources/ai-guides-2026-10-29/jargon-fixer/claude-jargon-fixer-guide.pdf
sha256: 360297cc8c35152a1c8d15b855532fd3dfd414c0eceff236dbd07fb86fcf7c3b
sources:
  - ../../raw/sources/ai-guides-2026-10-29/jargon-fixer/PROVENANCE.md
contradictions: []
---

# Claude Jargon Fixer guide

RoboNuggets supplied guide, publication date unknown; captured 2026-10-29 from the supplied Desktop PDF. [Original PDF](../../raw/sources/ai-guides-2026-10-29/jargon-fixer/claude-jargon-fixer-guide.pdf) and [provenance](../../raw/sources/ai-guides-2026-10-29/jargon-fixer/PROVENANCE.md).

## What it proposes

The guide presents three ways to control dense responses: an always-on Claude output style, an on-demand rewriting skill, and a standing instruction. It links [bro](https://github.com/dmmulroy/skills/blob/main/bro/SKILL.md), [wait-what](https://github.com/mattpocock/skills), and an [ASD-STE100 skill](https://github.com/danyuchn/asd-ste100-skill). Its `/quick` resource is said to be in the RoboNuggets community; it is not packaged in the guide.

## Application here

Plain, direct language and preserving technical facts apply to both runtimes and already align with Joshua's instructions. Claude output-style settings are runtime-specific and are not Codex settings. An on-demand rewrite is useful when requested; no need to impose an infantilizing tone or claim strict compliance with a specialized aviation standard. The guide's benchmark and product-version claims are unverified and time-sensitive. External skill links require inspection before installation; a link in a guide is not proof that a skill is installed or trustworthy.

## Mentions in source

Source heading: The three fixes at a glance (page 2)
Source heading: Any voice you want (page 6)

PDF extraction may insert spacing into visual text; the archived PDF is the authoritative evidence.

## Local implementation (2026-10-29)

`bro` and `wait-what` are available in the Claude and Codex project catalogs and active folders. Their skill files match across the four copies. Existing `humanizer` supplies an additional editing route. Fresh-session discovery and invocation remain untested; no global output style was changed.

## Integration review (2026-10-29)

Done AQ-044: [review](../../research/2026-10-29-ai-guides/integrations-review.md) checked the linked resources. `asd-ste100` is installed project-scoped for Claude and Codex, with pinned provenance; its linter passed a small stdin check, but does not establish full compliance with the official standard. Fresh-session invocation remains untested.
