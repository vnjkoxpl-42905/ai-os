---
type: brainstorm
subject: Plan Make the second brain actually know Joshua feed it his real history
updated: 2026-07-19
aliases: []
---

# Plan: Make the second brain actually know Joshua — feed it his real history
_Locked via grill — by Claude + Joshua, 2026-07-18_

> **STATUS (filed from root 2026-07-18): ~70% executed.**
> - Step 1 SECURE — ✅ done. `raw/sources/private/` + the takeout zip are git-ignored (`.gitignore:54`); mbox confirmed ignored.
> - Step 2 FREEZE — ⚠️ partial. Takeout mbox frozen at `raw/sources/private/takeout/`, but **no `PROVENANCE.md` / `SHA256SUMS` yet**, and no per-student transcript freeze under that tree. **OPEN.**
> - Step 3 STRUCTURE — ✅ done 2026-07-17 (as noted inline below).
> - Step 4 INGEST — ⚠️ partial. Corpus/voice ingests done (see `wiki/log.md` 2026-07-18 entries); the **student-identity mine from the mailbox → thin `students/<name>/index.md` is NOT done.** OPEN.
> Two open threads remain: (2) provenance/hash the frozen takeout, (4) the student-identity ingest.

## Goal

Joshua's stated mission: "I want my second brain to really know me, in and out —
that's why I have it." The brain is well-built but under-fed — the last real
*ingest* (not system/reform work) was the onboarding intake on 2026-07-16.
Meanwhile the raw material that actually constitutes "Joshua, in and out" is
sitting frozen and unprocessed: a **753MB Google Takeout of his entire inbox**
at `raw/takeout-20260717T014418Z-1-001.zip` and **~a year of session
transcripts**. This plan (a) secures that material properly, (b) resolves the
folder/structure confusion the grill surfaced, and (c) runs the first real
ingest since the reform — mining the high-value seams so the brain gains
founding knowledge of his students, promises, and voice, WITHOUT manufacturing
living pages for workflows he doesn't run (he confirmed he does not actively use
transcripts — they are "in case I need it" archive).

## Approach

1. **SECURE FIRST (before anything touches git).**
   - Add ignore rules so `raw/takeout*`, `*.zip`, and a new `raw/sources/private/`
     tree are git-ignored. Verify each with `git check-ignore -v`.
   - Confirm the 753MB zip is NOT already tracked in history (`git log --all --
     -- <path>`); if it is, that's a scrub job, flag it, do not proceed to ingest.
   - Nothing else runs until `git check-ignore` confirms the zip is ignored.

2. **FREEZE the sources as proper raw evidence (copy, never move the originals
   until verified).**
   - Unzip the takeout to a git-ignored working area; record counts (emails,
     date range, attachment count) WITHOUT loading bodies into context.
   - File transcripts under `raw/sources/private/transcripts/<student>/` (frozen)
     with a `PROVENANCE.md` + SHA256SUMS per the existing pattern (mirrors the
     youtube/ source treatment).
   - The email .mbox stays git-ignored, frozen, with its own PROVENANCE.md.

3. **RESOLVE the structure (the grill's conceptual output).** ✅ DONE 2026-07-17
   — deletions and link fix all executed; wiki is clean (hubs + entities/ +
   reference files only).
   - Three sibling knowledge stores stay as-is and are CORRECT: `wiki/` (Joshua +
     business), `corpus/` (LSAT teaching), `students/` (per-student). Corpus is
     NOT ingested into wiki — it is a peer wiki, connected by wikilinks, not
     nesting (grill Q1: connected by links, not sameness).
   - Delete the empty category-error folders: `wiki/knowledge/` (everything is
     knowledge — meaningless divider) and `wiki/concepts/` (concepts currently
     live in corpus; recreate only when a non-LSAT concept appears).
   - Delete `wiki/INDEX.generated.md` (stale duplicate index — still lists the
     deleted components/Shadcn tree and the deleted ea-build-plan.md; the
     hand-maintained `wiki/index.md` is the single index).
   - Fix the dead `[[ea-build-plan]]` link in `wiki/index.md` (file no longer
     exists) — remove it or restore the file.

4. **INGEST the high-value seam (first real ingest since reform).**
   - Mine the email zip for WHO the active students are and WHAT is live/promised
     (consultation history, commitments) — the founding knowledge a brain that
     "knows Joshua" needs today.
   - For each identified student: create a THIN `students/<name>/index.md` — who
     they are, current focus, and a POINTER to their frozen transcript pile.
     Student page is the hub; its focus line wikilinks to the corpus concept
     (grill Q2/Q3: student pages link out to corpus + business).
   - Do NOT distill a year of transcripts into rich pages — distill-on-demand
     when a specific need appears (grill Q6: transcripts are dormant archive).
   - Log the ingest in `wiki/log.md` (`## [2026-07-18] ingest | ...`); update
     `wiki/index.md`.

## Key decisions & tradeoffs

- **Distill-on-demand, not distill-everything.** Rejected building living
  per-student pages from a year of transcripts because Joshua confirmed he does
  not use transcripts actively. Tradeoff: the brain won't "know" transcript
  detail until a specific ingest — accepted, because manufacturing unread pages
  creates rot, and the machinery to distill-on-demand is already there.
- **Three sibling stores, connected by links, not merged.** Rejected merging
  business/teaching/students into one wiki. The connection is wikilinks; merging
  would duplicate concept explanations across student folders.
- **Secure-before-ingest is a hard gate.** The 753MB inbox zip is Tier A and
  currently NOT git-ignored. No processing happens until it is provably ignored.
- **Student folders are permanent-but-archivable**, one structure for everyone
  regardless of timeline; inactive → `students/_archive/`, never deleted.
- **Copy, never move/delete originals** until hash-verified (vault hard rule).

## Risks / open questions

- Is the 753MB zip already in git history? If yes, this becomes a scrub job
  first (per `wiki/HANDLING.md`), not an ingest.
- Student identity resolution from email is fuzzy — how to distinguish a real
  ongoing student from a one-off inquiry or a newsletter? Needs a heuristic
  (reply threads + consultation link + multiple exchanges) and human confirm
  before any folder is created.
- Transcript → student mapping: are transcripts labeled by student name, or will
  matching them to email-identified students require judgment?
- Context cost of scanning a 753MB mailbox — must be done via counts/greps and
  subagent summaries, never by loading bodies into the main context.

## Out of scope

- Distilling the full transcript archive into rich pages (deferred to on-demand).
- Any send/reply to real email — this is a dead export, read-only.
- Rebuilding corpus or students structure — they are correct; only wiki cleanup
  and thin student-page creation are in scope.
- Giving the repo a git remote (unchanged standing rule).
- The 6-hour video breakdown (separate, earlier thread).
