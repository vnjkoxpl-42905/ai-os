---
type: teaching-notes
subject: Flaw and Famous Flaws Claude Code Handoff Folder
updated: 2026-07-17
aliases: []
---

# Flaw and Famous Flaws — Claude Code Handoff Folder

This folder is the complete handoff package for the Flaw and Famous Flaws LSAT U module build. Everything Claude Code needs to build v1 is here. Nothing else is required.

## File order (read in this sequence)

1. **01_BUILD_BRIEF.md** — START HERE. Self-contained build instructions: tech stack, file/folder structure, design tokens, 22-feature priority list, interaction specs, edge cases, LSAT U integration notes, 20-day build sequence, two gap-fill invention tasks. Read this first to orient.

2. **05_compiled_content_voiced.md** — THE CANONICAL CONTENT SOURCE. Voice-locked compiled content for Note 1 (8-section procedural lesson), Note 2 (15-entry Famous Flaws catalog), the Disguise Library, and the Disambiguation Matrix. Render its passages near-verbatim into the web app. Do NOT edit for tone. Do NOT flatten the voice. This file is what the build agent ports.

3. **02_spec_artifact.html** — Open in a browser. Visual reference for the Stage 1 audit (rubric, source rankings, repetition map, gap analysis). Use this when you need to fact-check what made it into the compiled content vs. what was dropped.

4. **03_design_artifact.html** — Open in a browser. Visual reference for the Stage 3 design system. All 14 component patterns rendered live including the interactive Cake-on-Blocks SVG and the Three Languages classifier. Use this when implementing components — visual ground truth.

5. **04_raw_extracted_sources.txt** — Plain-text extraction of the original 30 source files. Use this ONLY when you need to verify a specific Joshua phrasing against the original source material. Not for general reading.

## How to use this folder with Claude Code

1. Open Claude Code in this folder (or a parent folder).
2. Paste the prompt from PROMPT.txt to kick off the build.
3. Claude Code will read 01_BUILD_BRIEF.md, treat 05_compiled_content_voiced.md as the canonical content source, and reference the other three files as needed.

## Hard rules for the build agent

- Voice preservation: the two-register voice in 05_compiled_content_voiced.md is locked. Render passages near-verbatim. Do not flatten. Do not consumer-SaaS-ify.
- Canonical content: when the brief summary and 05_compiled_content_voiced.md disagree, the voiced file always wins.
- Pedagogical flow: end-of-module drill seeds spaced repetition. Never cold-test before teaching.
- Design tokens: locked from Stage 3. Do not change without flagging.
- Two known content gaps: answer keys for two drills + PT cites for Abstract Flaw Sets. Build agent invents these (see §10 of the brief).
