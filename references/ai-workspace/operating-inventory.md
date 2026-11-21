---
type: reference
subject: Applications, routines, memory and skills operating inventory
created: 2026-10-26
updated: 2026-10-26
aliases: [ARMS inventory, operating inventory, application routine memory skill map]
tags: [ai-workspace, inventory]
sources: [../../wiki/sources/ultimate-second-brain-arms-robonuggets.md]
---

# Inspect the operating system through its existing owners

This is the practical adoption of RoboNuggets' ARMS idea: connect the existing registries before adding another graph or integration. [Source account and limits](../../wiki/sources/ultimate-second-brain-arms-robonuggets.md). The snapshot measures local presence and selected routine metadata on 2026-10-26. It does not establish live access, granted provider scopes, successful scheduled runs or recent use.

Run `python system/scripts/brain-inventory.py --write` from the vault root to refresh the [generated inventory](../../system/generated/brain-inventory.generated.json). Without `--write`, the helper prints the proposed snapshot. It reads path presence, direct skill entrypoint names, three whitelisted automation metadata fields and one named Windows task; it does not publish credential values, automation prompts, note bodies or task actions. Existing generated output is compared before replacement.

| Layer and owner | Purpose and access mechanism | Evidence route | Limit / next useful check |
|---|---|---|---|
| Applications: gws | Gmail correspondence, Calendar and Drive/Docs session evidence; Google CLI only | [Connections](../../connections.md), generated executable paths | Current OAuth scopes/authentication and actual usage UNKNOWN; registry's successful reads are dated 2026-10-08 |
| Applications: LSAT U and Stripe | Homework, dossiers, booking and payment authority; local admin/API scripts | [Connections](../../connections.md), [dashboard](../../wiki/dashboard.md) | No fresh provider call, permission expansion or write; use bounded identity-specific reads before action |
| Applications: gh and Firecrawl | Code hosting and source research through existing CLIs | [Connections](../../connections.md), [Firecrawl guide](../firecrawl.md) | Executables found; official GitHub reads and a real Firecrawl search/scrape succeeded during this implementation pass. Current provider credits and broader access remain unmeasured |
| Routines: Codex | Payment/calendar/session-note monitor and Claudex maintenance | Two named automation.toml paths in generated inventory | Monitor PAUSED; updater ACTIVE. Stored schedule is configuration, not evidence of successful execution or time-zone behavior |
| Routines: Windows Task Scheduler | Matt Pocock skill maintenance | Named AI OS - Matt Pocock Skills Sync task | State 3 (Ready) observed; last run/result and full scheduler coverage UNKNOWN |
| Memory: wiki/corpus/students | Compiled knowledge, teaching and student records; local files with domain ownership | [Wiki schema](../../system/schema/llm-wiki.md), [wiki index](../../wiki/index.md), [student router](../../students/README.md) | Path presence observed, no content-wide freshness audit; live operational systems retain authority |
| Memory: native runtimes | Claude project memory and Codex memory | Generated path-presence rows | No content scan or automatic promotion; Codex memory may span projects |
| Skills: runtime catalogs and activations | Reusable workflow definitions, utility entrypoints and provider adaptations | [Catalog](../../skills/INDEX.md), [parity](../../skills/PARITY.md), generated entrypoint names/counts | Filesystem presence only; counts are overlapping installs, not distinct capabilities, successful invocation or usage |

## Keep existing connections until use is established

No missing integration is justified from this snapshot. No connection or routine is nominated for retirement based only on its presence or paused state. The paused monitor is a useful review candidate: check why it was paused and recent receipts before any resumption decision. The active Claudex updater and Ready Matt Pocock task should next be checked for last-run receipts and maintenance conflicts, without changing schedules. Those are explicit remaining audit questions rather than invented unused-tool findings.

The generated inventory currently sees 131 Claude project, 156 Codex project, 320 Gemini project, 289 Claude home, 300 Agents home and 150 Codex home direct skill entrypoints. Catalog checks remain the authority for parity; this inventory deliberately does not reconcile or activate copies. A future connection addition requires an actual repeated task that existing access cannot handle.
