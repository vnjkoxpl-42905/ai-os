---
type: reference
subject: Design document discovery coverage and canonical routes
created: 2026-10-24
updated: 2026-10-24
aliases: [Design document completeness audit]
tags: [design, llm-wiki]
sources: []
---

# Documents beyond the original filename catalogue

The 2026-10-24 discovery pass examined Markdown bodies for visual hierarchy, typography, palettes, interface design, motion, GSAP, components and critique. It also inspected design-specific filenames. This finds useful documents whose titles do not contain design and avoids assuming that every architecture document is visual design.

The [machine-readable inventory](../research/2026-10-24-design-completeness/documents.json) records absolute path, classification, current role, SHA-256, prior catalogue presence and actual read coverage for each candidate. It contains **169 candidates: 136 design records, 13 supporting records and 20 exclusions**. **103 design paths were absent from the old catalogue.** These counts describe this bounded discovery pass, not every file on the machine or proof that every source is fully ingested.

## High-value routes

| Topic | Canonical or historical documents |
|---|---|
| Planning, hierarchy, useful depth and reference-led iteration | [Website design planning](../references/website-design-planning.md), [principles routing synthesis](principles.md) |
| Voice and instructional UI | [LSAT teaching voice standard](../references/lsat-teaching-voice-standard.md), [copy corrections](../wiki/COPY-CORRECTIONS.md) |
| Current source tokens versus legacy defaults | [Intro to LR styling comparison](../references/intro-to-lr-design.md) |
| Historical Home choices and superseding answers | [2026-09-23 visual discovery](../brainstorms/2026-09-23-classroom-home-visual-upgrade.md), [review log](../brainstorms/2026-09-23-classroom-home-PLAN-REVIEW-LOG.md) |
| Navigation and student decisions | [Student experience prototype brief](../brainstorms/2026-09-28-lsatu-student-experience-design.md), [platform adoption plan](../brainstorms/2026-09-27-lsatu-platform-adoption-game-plan.md) |
| Teacher/student separation | [2026-10-22 role-home specification](../brainstorms/2026-10-22-role-home.build-spec.md) |
| Question retrieval and set composition | [LR setup design](../brainstorms/2026-09-26-lr-drill-setup-design.md) |
| Measured critique and honest limits | [Impeccable audit](../wiki/DRILL-HUB-IMPECCABLE-AUDIT-2026-09-08.md), [second run](../wiki/DRILL-HUB-IMPECCABLE-AUDIT-2026-09-08-RUN2.md), [third run](../wiki/DRILL-HUB-IMPECCABLE-AUDIT-2026-09-08-RUN3.md) |
| Instructional briefing and drill surfaces | [RRC briefing critique](../wiki/RRC-BRIEFING-CRITIQUE-2026-09-08.md), [full drill critique](../wiki/RRC-DRILL-AUDIT-CRITIQUE-2026-09-09.md), [Spot introduction](../brainstorms/2026-10-16-spot-intro-redesign.md) |
| Motion and reference evidence | [LexPrep teardown](../research/2026-10-21-lexprep-motion-teardown.md), [conditional motion proposal](../brainstorms/2026-09-30-conditional-curriculum/2026-10-10-necessary-definition-motion-proposal.md) |
| Independent visual comparisons | [Claude review](../research/2026-10-23-dashboard-final-audit/CLAUDE-VISUAL-REVIEW.md), [Codex scores](../research/2026-10-23-dashboard-final-audit/CODEX-VISUAL-SCORES.md), [student comparison](../research/2026-10-23-dashboard-final-audit/STUDENT-VISUAL-COMPARISON.md) |
| Current charcoal palette and widget research | [Palette record](../research/2026-10-24-charcoal-palette/PALETTE.md), [25-tip application](../research/2026-10-24-student-widgets/clip-findings.md) |

## Project authorities stay beside their code

The inventory also includes top-level `DESIGN.md` files in existing sibling LSAT U checkouts. Many are copies from the same repository generation. They remain indexed by actual path and hash rather than being merged into one new design file. Read the nearest instructions, active checkout and imported styles before treating any copy as current. This scan did not inspect every nested app design brief or certify live rendering.

The bounded external pass found design Markdown inside the dashboard handoff and prototype folders under Downloads, plus the RC builder handoff and LexPrep capture under Desktop. Those originals remain in place and are classified as project/reference material. They are not newly asserted to be ingested source summaries. Private student handoffs and generic session-handoff files were excluded.

## Coverage and exclusions

- Scanned knowledge areas: `references/`, `wiki/` excluding bulk Karpathy exports, `research/`, `brainstorms/`, `context/`, `decisions/` and `projects/`. Body scans are discovery, not a line-by-line review; the inventory identifies documents whose relevant passages were manually read.
- Skills, skill supporting references, activation copies and component repositories belong to the separate skills/repository audit. This document does not claim to have audited their runtime bodies.
- No student-folder or raw personal-export sweep. A student recap mentioning a visual example is not automatically general design knowledge.
- The generic `mbox-ingest-design` file concerns email-ingestion architecture and is a filename false positive. It should not become a visual-design source merely because it says design.
- No raw inbox source was ingested by this document pass. Ingestion status requires preserved evidence, hash and completed wiki output through the existing pipeline. No confirmed missing clip ingestion was established here.
- No original source, application file, repository or skill was moved, deleted or rewritten by this audit.

Start at [the shared design hub](README.md) in either Claude Code or Codex. Follow these links and the refreshed catalogue to their owning paths; do not create parallel copies of the principles.
