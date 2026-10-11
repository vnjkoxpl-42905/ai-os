---
name: bootcamp-builder
description: Build or revise a repo-native LSAT U bootcamp using corpus sources, approved teaching preferences, and the Intro to LR benchmark. Use when Joshua asks to build a topic bootcamp, revise a bootcamp, or save bootcamp teaching preferences. Preserves scope approvals and carries corrections across sessions.
---


## Local execution contract (2026-10-10)

Preserve current curriculum sources and brainstorms checkpoints. Resolve sibling app root/current quality benchmark and installed parity helper. Absent authoritative quality reference blocks parity claim. Commit/push only when actual task authorizes it, not merely because build is green.

## Start with Joshua's accumulated preferences

Read `references/teaching-preferences.md` beside this skill before every build or revision. It records confirmed corrections, exact approved wording, conditional-logic acceptance checks, and proposals that are not approved. Apply general standards across topics; use topic-specific examples only where they fit.

When Joshua requests an ongoing preference capture, maintain this same reference as corrections arrive. Do not create a competing master skill. Record date, scope, status (explicit correction / approved wording / provisional implementation), evidence, and the regression check. Update the owning catalog and project activation copies deliberately; preserve runtime-specific differences. Read this record at session pickup. A source-backed logical fact and a user-approved design are different kinds of evidence.

For a previously authorized revision, work within its scope without asking for every gate again. A request to review together remains a review until implementation is authorized.

## Workflow

# Bootcamp Builder

Turn a topic + content into a shipped, repo-native LSAT U bootcamp that matches Intro to LR quality. This is the productized version of the Intro to LR (Main Conclusion) build process. It replaces `lsat-u-topic-builder`.

**The template is the code, not a doc:** resolve the vault root from its `AGENTS.md`, then follow its application routing to `../ai-os-projects/lsatu/src/bootcamps/main-conclusion/` (the Intro to LR build). Read the app's own instructions and the template before scaffolding anything. If inspection needs a preserved feature checkout, record its path and commit and reconcile it against the current checkout before treating it as the implementation template. Its structure:

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
- **Teaching voice:** From the canonical ai-os vault root, read `wiki/teaching-voice.md`, `references/lsat-teaching-voice-standard.md`, and `wiki/COPY-CORRECTIONS.md` before authoring or revising LSAT material. Apply the shared teaching standard to lessons, references, drills, instructions, and feedback. It governs how to teach, not the topics another bootcamp must include. Preserve Joshua's approved wording where he requires it; the attached voice reference calls for original examples and independently written explanations.
- **Quality bar:** the historical `archive/wiki-pre-rebuild-2026-07-16/domains/lsat-u/synthesis/bootcamp-quality-bar.md`, `intro-to-lr-product.md`, and `intro-to-lr-design.md` references are unavailable as of 2026-10-01. Report that absence explicitly; do not invent or recreate their contents. Continue code-based inspection using the template and these explicit rules: ModuleIntro is a real lesson; mastery tracking not attempt counting; reveal panels teach; no dead clicks, no fake analytics, no raw localStorage as UI text. Final parity cannot be certified until an approved, available quality reference is established.
- **Structure:** clone the Intro to LR module set by default. Deviations (drop/add/merge modules for topic fit) are PROPOSED at Gate 2 and require Joshua's approval.
- **No invented LSAT content silently.** Content comes from Joshua's files. Gaps are flagged; Joshua decides (he authors, the active assistant drafts for his review, or defer to v1.5).
- **Git:** Lovable pushes to the same origin/main. Always `git fetch` first, commit path-scoped (`git commit -- <paths>`, check `git status` for pre-staged files), never force-push. Commit, push, or deploy only when the actual task authorizes that action. A green build is not authorization. Preserve local-only review scope.
- **Missing reviewed content counts as build failure**, not something to paper over.

## Multi-session continuity (vault checkpointing)

The build spans many sessions. State lives in the Obsidian vault resolved from its `AGENTS.md`:

1. On Gate 0, search `brainstorms/` for the existing topic record and reuse it for the current build checkpoint. If none exists, create a dated topic record there, never in the retired archive tree. Include a **Gate ledger** (Gate 0..5, each `pending / in progress / APPROVED YYYY-MM-DD`), module checklist, decisions, and open questions.
2. Add a `## Now` item to `wiki/tasks.md`: `{Topic} bootcamp build (gate N)`.
3. After EVERY gate approval and at every session end, update the build page + append one line to `wiki/log.md`.
4. A fresh session resumes by reading the build page first, then jumping to the current gate. Never redo an APPROVED gate.

## The gated process

### Gate 0: Interview (no files touched yet)

Use the host available question tool or ordinary conversation for unresolved scope. Reuse prior answers and approvals; do not restart approved gates. Cover:
- Topic name, slug, route target (`/bootcamp/{slug}`)
- What content files he will feed it, and where they are
- Topic's named tools, must-preserve worked examples, signature traps (his versions of FABS / Trojan Horse)
- Which Intro to LR modules he suspects won't fit this topic
- Priority order and anything explicitly out of scope

Create the vault build page, record answers. → **Joshua approves scope.**

### Gate 1: Content intake + audit

Sources = BOTH: (a) every file Joshua fed it and any existing authorized topic material-inventory, and (b) a scan of `corpus/Curriculum/{Topic}/` relative to the vault root (Notes/, Homework/, megadocs, scans). Follow the inventory's source routes and flag relevant material he did not mention. Use bounded `rg --files` and `rg` searches on this machine for gaps; report missing directories rather than assuming historical paths or Mac-only `mdfind` exist. Do not read source archives wholesale.

For every file: read it fully; summarize unique teaching content; note overlap; extract named tools, worked examples, voicy passages (mark verbatim-preserve). Tier-grade S/A/B/C/D:
- **S** foundation, preserve verbatim where possible; **A** use heavily; **B** integrate selectively; **C** mine one block, drop rest; **D** unique-content-free, recommend drop.

Map the corpus against every Intro to LR module (lessons, reference vault, indicator vault, flashcards, drills, practice drills, simulator + trap master, hard sentences, diagnostics, journal): `sufficient / marginal / insufficient` each. For each gap, ask Joshua: he authors, the active assistant drafts for review, or defer.

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
4. **Per-module sign-off from Joshua** before the next module. Commit path-scoped or push only within actual task authorization.
5. Update the vault gate ledger + module checklist.

### Gate 4: Impeccable sweep

Full polish pass across the bootcamp (dead clicks, empty states, reveal-panel teaching quality, mastery tracking wiring, copy voice). Fix everything found.

### Gate 5: Parity audit — the definition of done

Run `/bootcamp-parity-audit {slug}` against Intro to LR using an approved, available quality reference. If that reference remains unavailable, report the limitation and do not certify final parity or mark the build complete. **The build is not done until it passes.** Close every gap it finds, re-run until clean. Then: mark the vault build page complete, strike the tasks.md item, log it, and give Joshua the shipped summary (route, module list, anything deferred to v1.5).

## What this skill does NOT do

- Never modifies main-conclusion or other bootcamps' files.
- Never claims sufficiency the audit didn't show.
- Never skips a gate or proceeds past one without Joshua's explicit approval.
- Never invents structure or theme beyond the Intro to LR template without an approved deviation.
