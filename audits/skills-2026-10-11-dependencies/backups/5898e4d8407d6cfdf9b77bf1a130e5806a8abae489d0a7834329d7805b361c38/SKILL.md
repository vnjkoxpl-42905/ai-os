---
name: bootcamp-parity-audit
description: Audit a given LSAT U bootcamp's feature and visual parity against the flagship Intro to LR (Main Conclusion) bootcamp, anchored to the quality bar doc. Use when Joshua asks to "compare against Intro to LR", "check parity", "audit [bootcamp name]", or wants to know how far a bootcamp is from shipped quality. Trigger with /bootcamp-parity-audit <bootcamp-name>.
---


## Local execution contract (2026-10-10)

Resolve existing authoritative current benchmarks from the target app/manual/curriculum. Legacy archive anchors are unavailable until verified; report parity blocked for absent benchmarks and never invent a replacement. Current application lives in sibling ai-os-projects.

## Workflow

Audit a named LSAT U bootcamp against the flagship Intro to LR (Main Conclusion) bootcamp and the shared quality bar, and report the delta.

## Inputs

The bootcamp name/slug (e.g. "Abstract", "Flaw & Famous Flaws", "Causation Station"). If not given, ask which one, once, don't guess.

## Anchor documents (read these first, in order)

1. `~/ai-os/archive/wiki-pre-rebuild-2026-07-16/domains/lsat-u/synthesis/bootcamp-quality-bar.md` — the shared bar every bootcamp finishes to.
2. `~/ai-os/archive/wiki-pre-rebuild-2026-07-16/domains/lsat-u/synthesis/intro-to-lr-product.md` — the flagship's product spec (what "done" looks like).
3. `~/ai-os/archive/wiki-pre-rebuild-2026-07-16/domains/lsat-u/synthesis/intro-to-lr-design.md` — the flagship's design system (colors, type, role tokens).
4. `~/ai-os/wiki/entities/intro-to-lr-bootcamp.md` if it exists, for entity-level facts.
5. Whatever entity page exists for the target bootcamp under `wiki/entities/` — read it if present; if it doesn't exist yet, say so, that itself is a gap.

## Codebase pass

In the LSATU repo (`C:/Users/Joshu/dev/ai-os/../ai-os-projects/lsatu/`):
1. Find the target bootcamp's source directory under `src/bootcamps/`.
2. Compare its file/component structure against the Intro to LR structure (`src/bootcamps/main-conclusion/`) at a glance, don't read every file, sample the key surfaces (overview, drill/practice flow, data layer).
3. Note any surface Intro to LR has that the target bootcamp lacks entirely.

## Output: 5-point delta report

Joshua's preferred format (per past sessions):

```
1. Feature parity: <what Intro to LR has that this bootcamp is missing>
2. Visual parity: <design-system deviations from intro-to-lr-design.md — colors, type, spacing, tokens>
3. Content/pedagogy parity: <coaching tone, teach-first-calibrate-after gaps vs teaching-voice.md>
4. Data/quality-bar gaps: <fake data, dead buttons, error handling — anything bootcamp-quality-bar.md flags>
5. Verdict: <shipped-quality / in-progress / needs-work, one line, plus the single highest-leverage next fix>
```

## Rules

- No em dashes. Terse per finding, don't pad with rationale unless asked.
- Diagnosis only unless Joshua asks you to fix something. Report the delta, don't start building.
- Don't re-read the full 216-file Intro to LR tree each time; use the entity/synthesis docs as the source of truth for what "done" means, and spot-check the codebase only where the docs are ambiguous.
- If the target bootcamp has no entity page in `wiki/entities/`, flag that as a documentation gap in point 5 rather than silently skipping it.
