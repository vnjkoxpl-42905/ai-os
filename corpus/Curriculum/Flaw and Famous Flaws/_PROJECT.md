---
type: teaching-notes
subject: _PROJECT.md Flaw and Famous Flaws
updated: 2026-07-17
aliases: []
---

# _PROJECT.md — Flaw and Famous Flaws

## Status: PROJECT COMPLETE 2026-05-04

All four stages closed. Build brief shipped to workspace folder. Ready for Claude Code handoff.

## Stages
1. Audit and Grade — COMPLETE 2026-05-04
2. Content Compilation and Strategy — COMPLETE 2026-05-04
3. Design Polish — COMPLETE 2026-05-04
4. Claude Code Handoff — COMPLETE 2026-05-04

## Final deliverables
- **CLAUDE_CODE_BUILD_BRIEF.md** (in this folder) — self-contained build brief, all content embedded as markdown, design tokens, component patterns, file/folder structure, 22-feature priority list, interaction specs, edge cases, LSAT U integration notes, two known content gaps to invent during build (drill answer keys + Abstract Flaw PT cites). Sufficient for Claude Code to build v1 with zero re-spec.
- **outputs/flaw_spec_artifact.html** — Stage 1 audit + Stage 2 compiled content (rubric, full source inventory with tier rankings, repetition map, garbage list, gap analysis, golden version brainstorm, full Note 1 + Note 2 + invented Disguise Library + Disambiguation Matrix).
- **outputs/flaw_design_artifact.html** — Stage 3 visual design (Editorial/Legal aesthetic, color system, type stack, 14 sections of live mockups including interactive Cake-on-Blocks SVG and Three Languages classifier).
- **outputs/flaw_extracted.txt** — Stage 1 raw extraction reference (179KB, full text of 30 source files).

## Key locked decisions
- 2 notes: "Flaw Question Approach" (procedural) + "Famous Flaws Catalog" (reference) with cross-linking
- 15 catalog entries across 3 groups (G1 Real Flaw, G2 Distractor, G3 Joshua-named with Sleight of Hand promoted to top-tier billing)
- Two-register voice preserved as-is, no flattening
- Editorial/Legal aesthetic locked: cream paper · ink type · verdigris green for verdict moments · Joshua-cake pink for whimsy
- Type stack: Newsreader display + Spectral body + JetBrains Mono protocols
- 22 features speced across 3 categories (Standard Learning, High-End Tech, Visual+Interactive) with P1/P2/P3 priorities
- Tech stack: Next.js 14 App Router + React + TypeScript + Tailwind + Framer Motion + Zustand
- Pedagogical-flow rule: end-of-module calibration drill seeds spaced repetition; never cold-test before teaching

## Source counts
- Notes: 32 files audited, 13 marked for deletion, S-tier foundations: Flaw Recap.pdf, Flaws.pdf.pdf, Logical host(lecture revision).pdf, Most Common LSAT Tricks.pdf, What if..?.docx, _scan_Flaw_Master_Guide_Premium.pdf
- Homework: 14 files audited, S-tier foundations: Fallacy Homework.md, Homework_Abstract Flaw Sets1 & 2.docx, Pop Quiz - Assumption vs Objection.md
- Net after compilation: 33 files

## Open at handoff
- Two content gaps for Claude Code to invent during build:
  (a) answer keys for Flaw Drilling 30Q + Flaw Progressive Mastery 20Q (sources ship without keys)
  (b) PT-cite question sets for Abstract Flaw Sets 1 & 2 (source ships with placeholder slots)
- Spaced-repetition data persistence: localStorage in v1, account-backed in v2 when LSAT U auth lands
- Cross-module references (to Causation, Conditional Logic, Necessary Assumption modules) stubbed for v1, resolved at LSAT U integration time
