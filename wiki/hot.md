---
type: operating-layer
subject: Hot last-session cache
updated: 2026-09-30
aliases: []
---

# Hot — last-session cache

Freshest working state; the first page `/pickup` reads. Rebuilt fresh in the 2026-07-16 vault rebuild (the old cache is archived).

## Current schema change (2026-09-30)

The current LLM Wiki operating rules are [[system/schema/llm-wiki]]. The first authorized ingest example is [[wiki/sources/llm-wiki-pattern]], linked to [[wiki/concepts/compiled-knowledge]]. The wiki index now contains a complete fenced catalog maintained by `system/scripts/wiki-maintenance.py`; structural lint is separate from source-grounded semantic review.

## Most recent (2026-09-30): Yahunatan's conditional Must Be True schedule assigned

- Live account is Yahunathan. [Assignment log](../students/yahunatan-zetvy/assignment-log.md) records all four assignments and IDs.
- Four-question untimed guided drills unlock and are due 2026-09-30 (difficulty 1-2), 2026-10-01 (2-3), and 2026-10-03 (3 only). Friday 2026-10-02 is off.
- PT101.S3 LR is assigned for Sunday 2026-10-04: 26 questions, standard 35-minute timer. Nothing assigned Monday 2026-10-05.
- All 12 questions are conditional Must Be True in the deployed bank; no cross-drill or Sunday overlap. Saved content, student access, Classroom visibility, exact dates and one unread bell per drill verified headlessly. All four assignment calls returned inbox/bell/email OK; email receipt not independently verified.
- Added authored guided-spec support to the existing headless assignment wrapper and a read-only verifier. Browser launch QA skipped at Joshua's request. Two primary-checkout question labels disagree with operational/live data; discrepancy recorded in the student's log. Tasks ledger unchanged.

## Previous (2026-09-30): Applications separated from Obsidian

- Joshua authorized moving application folders after Obsidian stalled at Loading vault.
- All 33 project folders now live in `C:/Users/Joshu/dev/ai-os-projects`; the vault stays at `C:/Users/Joshu/dev/ai-os`.
- Git worktree links, operational tools, skill paths, and backup conventions were updated. Existing application edits were preserved.
- The old `projects/` tree contains only empty directories. No files were deleted and no junction reconnects it to the applications.
- Obsidian remained stuck at Loading cache after relocation. Preserved its old IndexedDB directory at `C:/Users/Joshu/AppData/Roaming/obsidian/IndexedDB.pre-relocation-2026-09-30` and restarted it to rebuild the cache.
- Verified the vault opened and displayed `wiki/index.md` through the Obsidian URI handoff. A real browser Web Clipper save remains unverified; do not report that separate extension test as passed.

## Current LSAT U audit implementation (2026-09-30)

Use the [build sequence](../brainstorms/2026-09-28-lsatu-build-sequence.md) as the audit authority.

- `122eadf` passed 132 tests, typecheck/build, lint, independent review and guarded push. Exact GitHub main, Lovable import/publication and fresh live routes were verified on 2026-09-30.
- RRC closeout now retains exact-take recording/response evidence and requires account completion acknowledgment; failures retry before the report. Fresh live history failure blocked recording. The genuine section remains unfinished.
- Teacher Activity Unassign is wired behind a backend capability. The source-preserving SQL draft passes 35 isolated checks but is not deployed; current live controls remain disabled. Required Lovable Cloud route confirmation is pending.
- Six owned source ID sets matched in ordinary student/teacher reads. Six exact cross-owner identity UPDATE attempts returned zero rows against teacher-confirmed foreign fixtures. INSERT and teacher mutation attribution remain open.
- Inactive timed control/receipt/LR-binding SQL passes 34 isolated checks; full parent/child writer, content manifest, lease/closeout contract, adapter adoption and two-client race acceptance are still needed. Drafts and acceptance notes reached GitHub main as `de5e1d3` and were imported by Lovable. This follow-up changes no frontend source; the published functional slice is `122eadf`.
- #166/#167 and the later functional tickets remain open; #178 design review remains deferred. No backend deployment or credit-spending action occurred. Browser interceptions/blocks and synthetic state were cleared.
- Active isolated app checkout remains `C:/Users/Joshu/dev/lsatu-connected-experience`, branch `codex/connected-experience`; dev server exec session `14309` serves port 8080. This separate worktree was not moved with the primary applications. Unrelated outer repo edits remain preserved.

The sections below preserve earlier session snapshots. They are historical context, not verified current operational state; use current instructions and live backends when they disagree.

## Most recent (2026-09-11): RRC demo films Round 8 live, audited, board published

- Round 8 of the RRC demo films ("text written in the air") is live on lsatprep.study under Lovable deployment `d0ecbeb4`: the dark slabs are gone, every card is light-written type on the room, phrases write in under a second, natural blinks on holds. App PR #122 merged as `6836bdb` (six files, no code); film source in private repo `vnjkoxpl-42905/lsatu-films` (`main` = R8 `6357e00`, R7 tagged `r7-shipped-pub`).
- Verified on the live domain, not the diff: the three mp4s match the encodes byte for byte (36,382,871 / 37,121,022 / 25,787,844), the signed-in theatre references them, all three decode and play in Chrome at 1920x1080 (139.93 / 141.59 / 109.59 s). Frames at the changed beats checked from the shipped bytes.
- Found while verifying: **Lovable static hosting ignores HTTP Range** for every asset. Chrome reports `video.seekable [0,0]`, so the theatre's scrubber and arrow keys do nothing on production, nothing is cached, and iPhone playback is at risk (Apple requires byte-range support; not tested on a device). Predates Round 8; the bootcamp mp4 has it too. Fix is a public Supabase Storage bucket plus a repoint in the demos file. Needs his go.
- `impeccable audit` of /activities/sections: 14/20. Beyond the host: em dashes in live student copy (`SectionProgress.tsx:69`), no `<main>` landmark, Full screen a no-op on iPhone, film type ~8 px inline on a phone. All in [[tasks]] Next.
- Progress board (pipeline, evidence table, audit, open decisions, rounds, rollback): https://claude.ai/code/artifact/88636536-9e3c-40ac-bb02-1d99ec221dc4
- Not done: the theatre watched in motion in a signed-in browser (his Chrome tab sat behind Pinterest and Chrome held the media back; the component is unchanged since verified 02:12). Waiting on him: verdict on Round 8, the hosting move, the two audio questions from Round 7, permission to clear the em dashes.
- Rollback if rejected: `git checkout 9b6b51c -- public/rrc-demos` on a fresh branch, PR, merge, `deploy_project`.

## Previous (2026-09-11, earlier): RRC Steps 8 to 12 on PR #111, re-merged with main, waiting on Joshua

- Five sessions from 2026-09-09 built Steps 8 to 12 of the RRC fix plan: the beat waits to hear her before counting (six-second check, then Start anyway / Ask again / Leave this section); the door stops lifting on hover; the phone door flows copy then stage; the record says what the code decided; and a polish pass (no em dashes, one name per thing, Recall verdict in words, `.rc__cta`).
- PR #111 (`rrc-step-12`) carries all of it and supersedes #105, #106, #107, #109. On 2026-09-11 main had moved (three merges, including #114 demo videos on the briefing page), so #111 was merged with main in a throwaway worktree: one import conflict, both kept. Head `c635b7b`, 107 files / 2,795 tests, mergeable.
- Scores after Step 12 missed both targets (audit 15/20 vs 17, critique 26/40 vs 32). What is left is shape: the door teaches the method six times before stimulus one, the console needs distilling, "details carried" and "Coverage" are unclear. Listed in [[RRC-DRILL-AUDIT-CRITIQUE-2026-09-09]].
- Waiting on Joshua: merge #111 as one or the four small PRs, then publish, then pick among the five next actions.
- Housekeeping owed: `scripts/rrc-ungraded.ts` has not been run since 2026-09-09; `sweep-rrc-grading` is still unscheduled; merged `rrc-step-6`/`-7` branches undeleted; a leftover empty directory `projects/lsatu-wt-rrc12` could not be removed (permission denied) and needs a manual delete.

## Now

- **D1 Step 4 (vault rebuild) executed 2026-07-16.** New `wiki/` + `corpus/` + `students/` stand; prior wiki archived at `archive/wiki-pre-rebuild-2026-07-16/`. Product work continues in [[tasks]] unchanged.
- **D1 #5 (post-session pipeline): DEPLOYED and live, 2026-07-16.** Lovable pass reported green (3 functions, migration present, all secrets — `EDGE_INTERNAL_KEY` is project-scoped so the same-value trap can't happen; gateway `ai.gateway.lovable.dev` confirmed unchanged). Frontend Publish verified live in the browser. **Then Joshua pivoted the workflow: the app's ingest UI is not how he'll work — Claude is the workplace; ingestion and post-session actions go through Claude directly.** The formal runbook E2E was aborted at his direction and is no longer the plan of record. **The `lsat-u-platform-actions` skill now exists (activated both runtimes)** — one entry point to assign drills/homework/activities, post to classrooms, message students, and ingest sessions from this workspace via his Chrome admin session. The original "D1 #6 gated on live E2E" adjudication predates this pivot and needs re-adjudication.

## Open threads

- RRC films: seeking is dead on production because the host ignores Range; hosting move is a P0 decision in [[tasks]] Next.
- Testing Centre: copy decisions, P3 design notes, practice-test freshness filter, scoped-world question, pre-`776f69b` run repair. All in [[tasks]] Next.
- Booking is not production-safe on cancellation or recent Google Calendar changes until the P1 batch is fixed and live-verified.
- Archived knowledge (product specs, entities, concepts) re-enters organically via `raw/` ingests when actually needed — do not bulk re-import.
- Corpus is empty by design; it fills from teaching materials and transcripts as they are ingested.
- **Failing lsatu tests, updated 2026-07-16:** `ConclusionTypeLab` is already handled per Joshua — do not investigate. `page-six-switchboard` and `Practice` remain genuinely failing (pre-existing, reproduce on a clean baseline, fail standalone — NOT the documented suite-load flake) and are deferred, not resolved.

<!-- brain-automation-alerts:start -->
<!-- brain-automation-alerts:end -->
