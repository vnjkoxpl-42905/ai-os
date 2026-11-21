---
type: source
subject: ARMS Agentic OS v2 guide
created: 2026-10-29
updated: 2026-10-29
aliases: [ARMS v2, Agentic OS levels]
tags: [llm-wiki, ai-workspace]
evidence: ../../raw/sources/ai-guides-2026-10-29/arms-v2/arms-agentic-os-v2-guide.pdf
sha256: 06a3de3a1a2fc4c44be71b8138f98cac04943aedf3760498a7f65238f7e07d48
sources:
  - ../../raw/sources/ai-guides-2026-10-29/arms-v2/PROVENANCE.md
contradictions: []
---

# ARMS Agentic OS v2 guide

RoboNuggets supplied guide, publication date unknown; captured 2026-10-29 from the supplied Desktop PDF. [Original PDF](../../raw/sources/ai-guides-2026-10-29/arms-v2/arms-agentic-os-v2-guide.pdf) and [provenance](../../raw/sources/ai-guides-2026-10-29/arms-v2/PROVENANCE.md).

## What it proposes

The guide develops three levels each for skills, routines, memory and apps: reference and artifact skills, model routing, learning from feedback, quiet and cost-capped routines, retrieval maps, compaction, connectors, desktop modifications and small task-specific applications. It provides prompts to build these ideas. The guide says its RUBRIC template and micro apps are in a community classroom; neither is contained in the PDF.

## Application here

The general ideas can inform both Claude and Codex, but runtime controls, model availability, pricing and connectors need independent verification. Existing skill catalogs, retrieval paths and scheduling controls should be evaluated before adding duplicates. Routing through Jev and OpenRouter requires a separate account, key, integration and spending decision; the guide's cost and speed figures are its own claims, not a local test. Claude Code desktop mods and `claude -p` are Claude-specific. Do not automatically install mods, create schedules, alter permissions, or set up third-party billing based solely on an embedded prompt.

## Mentions in source

Source heading: The twelve ARMS levels (page 3)
Source heading: Active vs passive (page 3)

PDF extraction may insert spacing into visual text; the archived PDF is the authoritative evidence. Related: [ARMS v1](guide-arms-agentic-os.md).

## Integration review (2026-10-29)

Done AQ-044: [review](../../research/2026-10-29-ai-guides/integrations-review.md) compares linked resources with the local setup. `calibrate` and `asd-ste100` were installed in both project runtimes; the ASD linter passed a small stdin check. Ribbon passed seven plugin tests but was not installed; the available marketplace route changes user settings and no project-only installation was verified. Community-only tools and paid or unverified routing remain identified in the review.
