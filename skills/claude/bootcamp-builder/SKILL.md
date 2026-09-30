---
name: bootcamp-builder
description: Build a complete repo-native LSAT U bootcamp for a new topic, cloning the Intro to LR (Main Conclusion) build process end to end. Interviews Joshua, ingests the content files he feeds it plus a scan of /Curriculum/{Topic}/, then drives a gated multi-session build inside the LSATU repo (src/bootcamps/{slug}/) until bootcamp-parity-audit passes against Intro to LR. Replaces lsat-u-topic-builder. Use when Joshua says "build a [topic] bootcamp", "new bootcamp", "spin up [topic]", "/bootcamp-builder [topic]", or wants to replicate the Intro to LR process for another topic.
---

# Bootcamp Builder

Turn a topic + content into a shipped, repo-native LSAT U bootcamp that matches Intro to LR quality. This is the productized version of the Intro to LR (Main Conclusion) build process. It replaces `lsat-u-topic-builder`.

**The template is the code, not a doc:** `C:/Users/Joshu/dev/ai-os-projects/lsatu/src/bootcamps/main-conclusion/` (the Intro to LR build). Read it before scaffolding anything. Its structure:

```
src/bootcamps/{slug}/
  App.tsx, routes.tsx        # nested <BootcampRoutes/> mounted under /bootcamp/{slug}/*
  components/                # workspace-shell (chrome), drills, pickers, coach's note, command palette, trap-master, smart-hints...
  content/*.source.ts        # authored content as typed TS sources + schemas.ts
  data/*.generated.json      # generated from sources via scripts/{slug}/import-content.ts
  modules/                   # lessons, reference, drills, practice-drills, simulator, hard-sentences, diagnostics, journal, settings, ModuleIndex
  persistence/               # Persistence interface, LocalStorage/IndexedDB/SupabaseSynced, slug-prefixed keys
  hooks/ lib/ styles/ types/
  __tests__/impeccable-bans.test.ts
```

## Hard rules (never violate)

- **Design: reuse Intro to LR exactly.** Same components, tokens, chrome, look. No per-topic themes, no bronze accents by default. A student moving between bootcamps sees one product.
- **Pedagogy locked:** teach-first calibrate-after, never cold-test; warm-coach voice; preserve Joshua's exact phrasings verbatim; no em dashes anywhere.
- **Quality bar:** `archive/wiki-pre-rebuild-2026-07-16/domains/lsat-u/synthesis/bootcamp-quality-bar.md` in the vault. ModuleIntro is a real lesson; mastery tracking not attempt counting; reveal panels teach; no dead clicks, no fake analytics, no raw localStorage as UI text.
- **Structure:** clone the Intro to LR module set by default. Deviations (drop/add/merge modules for topic fit) are PROPOSED at Gate 2 and require Joshua's approval.
- **No invented LSAT content silently.** Content comes from Joshua's files. Gaps are flagged; Joshua decides (he authors, Claude drafts for his review, or defer to v1.5).
- **Git:** Lovable pushes to the same origin/main. Always `git fetch` first, commit path-scoped (`git commit -- <paths>`, check `git status` for pre-staged files), never force-push. After clean diff + green build, commit and push without asking.
- **Missing reviewed content counts as build failure**, not something to paper over.

## Multi-session continuity (vault checkpointing)

The build spans many sessions. State lives in the Obsidian vault (`~/ai-os`):

1. On Gate 0, create `archive/wiki-pre-rebuild-2026-07-16/domains/lsat-u/synthesis/{slug}-bootcamp-build.md` with a **Gate ledger** (Gate 0..5, each `pending / in progress / APPROVED YYYY-MM-DD`), module checklist, decisions, and open questions.
2. Add a `## Now` item to `wiki/tasks.md`: `{Topic} bootcamp build (gate N)`.
3. After EVERY gate approval and at every session end, update the build page + append one line to `wiki/log.md`.
4. A fresh session resumes by reading the build page first, then jumping to the current gate. Never redo an APPROVED gate.

## The gated process

### Gate 0: Interview (no files touched yet)

Grill Joshua (AskUserQuestion, batched, opinionated options). Cover:
- Topic name, slug, route target (`/bootcamp/{slug}`)
- What content files he will feed it, and where they are
- Topic's named tools, must-preserve worked examples, signature traps (his versions of FABS / Trojan Horse)
- Which Intro to LR modules he suspects won't fit this topic
- Priority order and anything explicitly out of scope

Create the vault build page, record answers. → **Joshua approves scope.**

### Gate 1: Content intake + audit

Sources = BOTH: (a) every file Joshua fed it, and (b) a scan of `C:/Users/Joshu/dev/ai-os/Claude/02_PROJECTS/lsat-u/Curriculum/{Topic}/` (Notes/, Homework/, megadocs, scans) — flag anything relevant he didn't mention, plus a light `mdfind` sweep for topic files elsewhere on the Mac.

For every file: read it fully; summarize unique teaching content; note overlap; extract named tools, worked examples, voicy passages (mark verbatim-preserve). Tier-grade S/A/B/C/D:
- **S** foundation, preserve verbatim where possible; **A** use heavily; **B** integrate selectively; **C** mine one block, drop rest; **D** unique-content-free, recommend drop.

Map the corpus against every Intro to LR module (lessons, reference vault, indicator vault, flashcards, drills, practice drills, simulator + trap master, hard sentences, diagnostics, journal): `sufficient / marginal / insufficient` each. For each gap, ask Joshua: he authors, Claude drafts for review, or defer.

Write `AUDIT.md` into the vault build page folder or as a section of the build page. → **Joshua reviews the audit + gap decisions.**

### Gate 2: Inspection report (before ANY code)

A written plan, no code yet:
- Proposed module set = Intro to LR clone, with any topic-fit deviations explicitly argued
- Component reuse map: which main-conclusion components port as-is, which need topic variants, which are N/A
- Content schema plan: the `content/*.source.ts` files to author and the import script (`scripts/{slug}/import-content.ts`) to generate `data/*.generated.json`
- Persistence plan: slug prefix, records
- Route wiring into the LSAT U app (mirror how main-conclusion mounts)
- Build order (module sequence), risks, and what stays placeholder-free vs deferred
→ **Joshua approves before a single file is written.**

### Gate 3: Build, module by module

Scaffold the sub-app by cloning main-conclusion patterns (copy-and-adapt, do not fork the design). Then build in the approved order. Per module:
1. Author `content/*.source.ts` from S/A-tier material (verbatim passages kept verbatim); run the import pipeline to generate data.
2. Build the module UI from the ported components.
3. Verify: typecheck, tests (including a `{slug}` impeccable-bans test cloned from main-conclusion), click through the surface.
4. **Per-module sign-off from Joshua** before the next module. Commit path-scoped, push after green.
5. Update the vault gate ledger + module checklist.

### Gate 4: Impeccable sweep

Full polish pass across the bootcamp (dead clicks, empty states, reveal-panel teaching quality, mastery tracking wiring, copy voice). Fix everything found.

### Gate 5: Parity audit — the definition of done

Run `/bootcamp-parity-audit {slug}` against Intro to LR. **The build is not done until it passes.** Close every gap it finds, re-run until clean. Then: mark the vault build page complete, strike the tasks.md item, log it, and give Joshua the shipped summary (route, module list, anything deferred to v1.5).

## What this skill does NOT do

- Never modifies main-conclusion or other bootcamps' files.
- Never claims sufficiency the audit didn't show.
- Never skips a gate or proceeds past one without Joshua's explicit approval.
- Never invents structure or theme beyond the Intro to LR template without an approved deviation.
