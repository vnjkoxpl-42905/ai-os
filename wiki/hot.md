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

## LSAT U AI audit checkpoint (2026-10-01)

Claude study-tools build finished using observed claude-opus-5-5 at requested low effort. Two delegated fix rounds were followed by bounded Codex correctness fixes and independent Codex inspection. Fresh Claude inspection claudex-25sqwxlh approved the mixed production snapshot; its missing-LR-find inference was corrected by source and actual browser verification. Isolated study branch codex/study-tools-179 has local commit 2792e14; 39 files/311 tests, typecheck/build passed. LR and RC bookmarks/cross-outs survived browser reload; LR highlights and find, keyboard controls, five CSS widths, doubled text and RC touch visibility were checked. Final actual narrow RC side-pane acceptance remains pending; open_in_codex was queued while this task was hidden. No new publication or push. Whole #179 remains open for explanation/mode/first-blind semantics and full acceptance. [Study evidence](../../lsatu-study-tools-179/docs/implementation-plans/2026-10-01-study-tools-179-verification.md).

Activity AI branch codex/ai-grading-integrity has local commits e1fb1fa and 4bc4777, separate from study changes. Source-bound service-only admission, durable receipts, bounded quotas, exactly-once dispatch, trusted snapshot grading and explicit unverified retry UI passed 77 focused tests, 123 isolated SQL assertions, 33 real PostgreSQL race/role checks, 19 mocked Edge/SQL checks, typecheck, Deno and build. Browser blocked grading before transport, retained answer/retry and exposed a contrast defect now fixed and visually verified. SQL migration 20261001120000_activity_ai_admission_v1.sql installed through direct free Lovable SQL on 2026-10-01. All 21 authored Activities, 102 assignments and 1657 responses retained identical ordered-row digests. Configuration disabled; private tables empty, RLS/role permissions verified. Owned source returns disabled/503; foreign source denied/403. No provider calls or Lovable credits in this pass. Edge deployment through Lovable agent still requires immediate credit confirmation; matching frontend is not published. Ordinary-JWT, lost-reply, revoked-access live acceptance and broader AI routes remain open. [AI readiness](../../lsatu-ai-grading-integrity/docs/implementation-plans/2026-10-01-activity-ai-admission-readiness.md).

Both isolated app checkouts are clean. Original connected checkout retains unrelated supabase/functions/mcp/index.ts edit. Owned dev servers stopped; static previews running on 8181 (exec 86146) and 8182 (38637). Browser test overrides and network blocks restored. No files or records deleted; task statuses and native memory unchanged.

Deployment follow-up: Joshua explicitly approved the single Lovable-agent deployment. Lovable's deployment tool reported `activity-coach` success, including `response.ts`, at a reported cost of 0.5 credits; no version number returned and no paid post-deploy grading call made. Agent edit `edt-573e399d-4d56-4018-a584-b6b9e2f850ea`, commit `4474d9f9bdc68036983873f119e044137ab359c1`. GitHub comparison found only regenerated `src/integrations/supabase/types.ts`, reflecting installed revocation/timed schema, despite the deploy-only instruction. Local checkout fast-forwarded without touching unrelated MCP edits. Exact original Activity completion/score/time rechecked unchanged. Wider AI diligence remains open; deployed malformed-output behavior has deterministic tests, not a paid live failure test.

Joshua approved one prepared Activity grading Submit. Owned assignment `333838aa-cc3b-4789-a707-b8f50f918c25` genuinely graded correct, saved completion 100% with 1/1/1 score fields, and retained it on reload; Library displays 100%, one item. Live Lovable AI dashboard confirms `google/gemini-3.1-flash-lite`, 514 input/51 output tokens, 910ms, 0.0008 credits. No other grading call was made. Exact teacher Work mirror still needs a walk.

All 13 proxy chat callers are forced to Lite; Inspect, TA agent and RRC direct fallback need separate controls. Source audit found missing per-account budgets/entitlement binding, client-controlled grading authority, ineffective model selectors/provenance and repeatable force regrading. Narrow malformed-grade rejection and privacy-safe logging fix `e8419dce551036921123852b3263f888132dd8cd` passed 17 tests, independent review, typecheck/build and guarded push. Exact GitHub main and Lovable import verified. Backend deployment remains pending; immediate credit confirmation was requested for one deploy-only Lovable agent action. No model policy changed. [Full AI audit](../../lsatu-connected-experience/docs/specs/2026-10-01-ai-diligence-audit.md). All fourteen functional audit tickets plus deferred #178 remain open; thirty functional frontend slices remain published.

## Most recent (2026-10-01): Conditional curriculum research and assignment model

- [Main synthesis](../brainstorms/2026-09-30-conditional-curriculum/curriculum-analysis.md) connects the observed teaching sequence, practice emphasis, original examples, and existing LSAT U assets. [Interview capture](../brainstorms/2026-09-30-conditional-curriculum.md) remains the decision record.
- Confirmed scope: independent full pathway plus area/specific-skill/general assignments at Beginner, Medium, Advanced; all four language groups; optional Medium/Advanced timing; quantifiers follow conditionals and remain separately assignable.
- 7Sage signed-in research mapped 54 conditional, 34 intersecting-set, 12 formal-flaw resources; written teaching and worksheets inspected, selected Answer reveals verified. LR written resources connect MBT, rule application, and sufficient bridges.
- Four translation sets after Group 2 are cumulative Groups 1+2, not Group 2-only. Seven translation worksheets contain 35 visible tasks; two chaining sets contain ten. Scheduled minutes are study estimates.
- LSAT Lab introductory lesson 16784, scheduled core class 32874, advanced class 32838, and quantifier class 33015 were read through their full available captions. The personalized study plan supplies the five-level topic structure, easier/medium/harder sets, timing and review instructions, and independent flashcard scope/difficulty filters. Audio and boards remain unverified; locked topic levels and answer-submission feedback remain uninspected.
- 7Sage's public overview captions were read fully. Principle and Parallel written teaching now inspected. Compound worksheet corrected to six prompts, all six written Answer reveals read; the nested-box workshop and opening You Try tester were opened without answering. Viewing may affect history or in-progress state, but no answers or completion were submitted.
- No curriculum published, work assigned, answers submitted, or task statuses changed. Next: resolve remaining source coverage and curriculum packaging/mastery/placement decisions before implementation.

## Previous (2026-09-30): Yahunatan recap V7 ready for review

- Current draft is [Facts, Rules, and What Follows V7](../brainstorms/2026-09-30-yahunatan-post-session-recap/conditional-reasoning-v7.html), open in Codex at the opening. The [canonical 2026-09-16 recap](../students/yahunatan-zetvy/recaps/2026-09-16-recap.md) contains its exact current V7 export block. Prior versions are preserved history.
- Re-read the recap skill and teaching voice after Joshua's four browser comments. Replaced vague read/find/keep instructions with two numbered worked examples: Mira's trained fact plus the badge rule gives Mira a badge; training-to-badge plus badge-to-access gives a new conditional rule. Inputs, conclusions and reasons are separately visible, including the rules-only existence limit.
- Reviewed the whole note and cut redundant coaching. Definitions, four fact scenarios, contraposition, compound negation, linking, hidden chains, scope and complete should/may predicates remain. Seven typed checks, two objective quizzes and four cumulative problems remain; typed writing is self-comparison. Assignment sequence unchanged.
- Independent conceptual/editorial review passed. Actual browser verified opening copy, keyboard navigation, typed comparison and desktop/phone layout without horizontal overflow. Corrected an inherited paragraph background that reduced explanation contrast. Saved final numbered-opening and phone proof; normal viewport restored.
- Generated JavaScript syntax, student routers, skill validation and all four identical quality-bar mirrors pass. Confirmed-account publishing dry run accepted the 92,531-byte standalone package without writes. Copy corrections and source map record the concrete-opening standard.
- Shared teacher lecture remains separate at its previously verified 189 moments; original sources are unchanged. Nothing posted, sent or newly assigned. Await approval of this exact V7 package. Task statuses are unchanged.

## Previous (2026-09-30): Yahunatan's conditional Must Be True schedule assigned

- Live account is Yahunathan. [Assignment log](../students/yahunatan-zetvy/assignment-log.md) records all seven assignments and IDs.
- Four-question untimed guided drills unlock and are due 2026-09-30 (difficulty 1-2), 2026-10-01 (2-3), and 2026-10-03 (3 only). Friday 2026-10-02 is off.
- PT101.S3 LR is assigned for Sunday 2026-10-04: 26 questions, standard 35-minute timer. Nothing assigned Monday 2026-10-05.
- Added existing conditional guided drills beside MBT on the same dates: Easier Set 4 on 2026-09-30 (9 questions, 1-2), Easier Set 2 on 2026-10-01 (7 questions, 2-3), Medium Set 4 on 2026-10-03 (9 questions, 3 only via beginner assignment). Verified source rows, access, Classroom visibility and dates; inbox/bell/email OK. Repeat batch returned the same three IDs and no notifications.
- All 12 questions are conditional Must Be True in the deployed bank; no cross-drill or Sunday overlap. Saved content, student access, Classroom visibility, exact dates and one unread bell per drill verified headlessly. All four assignment calls returned inbox/bell/email OK; email receipt not independently verified.
- Added authored guided-spec support to the existing headless assignment wrapper and a read-only verifier. Browser launch QA skipped at Joshua's request. Two primary-checkout question labels disagree with operational/live data; discrepancy recorded in the student's log. Tasks ledger unchanged.
- Mapped all 119 guided drills in the [generated catalog](../references/lsatu-guided-drill-catalog.md). Extended local lsat-u-lessons MCP with search, preview and batch assignment; all three additional assignments used one sign-in and lookup, runner 15.3 seconds. The short project assignment skill routes directly to this path, with existing content first and a current-chat MCP fallback. No app deployment or Lovable credits.

## Previous (2026-09-30): Applications separated from Obsidian

- Joshua authorized moving application folders after Obsidian stalled at Loading vault.
- All 33 project folders now live in `C:/Users/Joshu/dev/ai-os-projects`; the vault stays at `C:/Users/Joshu/dev/ai-os`.
- Git worktree links, operational tools, skill paths, and backup conventions were updated. Existing application edits were preserved.
- The old `projects/` tree contains only empty directories. No files were deleted and no junction reconnects it to the applications.
- Obsidian remained stuck at Loading cache after relocation. Preserved its old IndexedDB directory at `C:/Users/Joshu/AppData/Roaming/obsidian/IndexedDB.pre-relocation-2026-09-30` and restarted it to rebuild the cache.
- Verified the vault opened and displayed `wiki/index.md` through the Obsidian URI handoff. A real browser Web Clipper save remains unverified; do not report that separate extension test as passed.

## Current LSAT U audit implementation (2026-09-30): thirty slices published, full PT browser closeout verified

- [Build sequence](../brainstorms/2026-09-28-lsatu-build-sequence.md) is authoritative. Latest functional `b315ac5` follows integrated `a7d416a` and expanded catalog `6b69bc7`; exact main/import, free publication and fresh live behavior were checked separately. Deployment `b0c1359a-ac3b-47c7-97e2-11ddc780de32`; Published/no changes waiting. Fourteen functional tickets and deferred #178 remain open.
- Integrated native saves/completion, exact native/Hard Sentences Review, teacher-selected reasons, canonical selected-student identity, navigation/access/preferences and History gates passed 339 distinct focused tests, typecheck/build and independent review. Actual Codex browser checked five CSS widths and real side pane. New creation confirmation passed 72 focused checks and fresh production same-UUID account creation, without false missing-parent error.
- Standalone 236 catalog selected 714b, 156 LR/80 RC; 21 original tables preserved in schema transaction, all old definitions/sittings/receipts/bindings retained. Both isolated engines 618 checks, ordinary JWT 24 checks passed. Full PT config enabled/c27b/30000ms unchanged. New local LR/RC recovery/closeout and fresh production expanded LR launch/finish plus exact reports passed.
- Fresh owned production PT 102 `4474e82e-6530-4792-a08b-9de7c30ef94c` completed all three legs in browser. Report/reload 3/75 with disclosed estimated 120. Break save failure blocked advancement; long interruption caused definite expired-lease rejection, explicit command preservation/reload/claim recovered paused 9:00, reload retained it. Full final browser closeout now verified; no physical second-device/lost TCP reply/revoked in-flight UI claim.
- Prepared paid-grading fixture 333838aa-cc3b-4789-a707-b8f50f918c25 remains in_progress with one exact authored item and typed answer; no grader/credit/notification. Immediate one-Submit approval is pending. Original assignments retained. User-opened Codex tab 6 keeps the form; new live confirmation tab is a deliverable.
- App `C:/Users/Joshu/dev/lsatu-connected-experience`, branch codex/connected-experience. Documentation-only checkpoint d8b5d7c1008df12311568cb92b291dfa32f23ca7 is verified on GitHub main; the app checkout is clean. Dev server 19097 / port 8080 retained and rechecked. Isolated PostgreSQL port 55437 was stopped gracefully; diagnostic data retained. Preserve unrelated vault work. Wider sources/Review families and later functional acceptance remain open.

## Previous LSAT U audit implementation snapshot (2026-09-30)

Use the [build sequence](../brainstorms/2026-09-28-lsatu-build-sequence.md) as the audit authority.

- `122eadf` passed 132 tests, typecheck/build, lint, independent review and guarded push. Exact GitHub main, Lovable import/publication and fresh live routes were verified on 2026-09-30.
- RRC closeout now retains exact-take recording/response evidence and requires account completion acknowledgment; failures retry before the report. Fresh live history failure blocked recording. The genuine section remains unfinished.
- Teacher Activity source revocation is now deployed through the connected Lovable Cloud database tool under Joshua's explicit authorization. Original assignment, response, grade and classroom values were transactionally checked and preserved. Ordinary student denial and teacher UI Unassign acknowledgment passed on designated QA fixtures; saved responses remain retained. No deletion or paid grading occurred.
- Six owned source ID sets matched in ordinary student/teacher reads. Six exact cross-owner identity UPDATE attempts returned zero rows against teacher-confirmed foreign fixtures. INSERT and teacher mutation attribution remain open.
- Prepared inactive atomic PrepTest batch `bcd7eec1a05b5ef0619d3b07290f57a6ecc5234b` is verified on GitHub main through guarded push. It includes protected parent/LR/RC writes, actual grant locks, server lease/device/epoch rules, stable receipts, atomic LR journal/history and RC closeout, frozen content for 59 PTs/177 legs/222 source hashes, and unused client/parent/LR/RC adapters. Existing runners are not switched; no backend installation or activation occurred. The published functional slice remains `122eadf`.
- Final integrated verification passed 309 tests across 11 files, 154 isolated writer assertions, 36 foundation assertions, 46 real PostgreSQL multi-connection assertions and 10 managed-role assertions. Typecheck, build, scoped lint, manifest freshness, diff checks and independent backend/client review passed. Native two-tab Web Locks retained one exact pending command and rejected the contender; synthetic browser state/tabs were cleared. Fresh read-only live ACL evidence led to corrected deployment SET membership and auth identity delegation. The isolated PostgreSQL cluster was stopped gracefully; diagnostic data was preserved.
- Current integrated batch `1644ce7406acb443c25c4496435026fc6f8ea736` reached exact GitHub main through guarded push. Protected parent and dedicated LR/RC children are integrated; unfinished legacy sittings are read-only. Backend foundation/writer and incremental metadata upgrade are deployed with ten-table original-value preservation. Catalog `c27b478f2d50f8353a98d4a1a905d2f94f87929ba2ea2179230d4f7a3d51c25c` has 59 PTs; 30-second lease is enabled. Existing legacy parents were not adopted or rewritten.
- Ordinary two-client QA acceptance passed receipt replay, epoch/lease/revision rejection, revoked access, atomic LR/RC closeout and retained original tester work. Local live-connected browser checks passed saved answers, paused reload clocks, blocked-commit recovery and widths 390/820/1060/1280/1600. Final integrated tests passed 176 across 15 files, typecheck and production build. These checks do not establish physical second-device UI or fresh production frontend acceptance.
- Lovable imported exact `1644ce7`. Initial publication failed; free retry `dc6b6cde-1dda-429d-a385-099b0dd826fb` reported Your website was updated. Fresh production protected RC hydrated paused at 31:22, blocked Next hid questions, exact retry after restoring network acknowledged question 2, and paused reload retained 30:11. Fresh production LR hydrated paused at 30:03. This is the twenty-sixth published slice; physical second-device, lost TCP reply and revoked in-flight UI acceptance remain open.
- Next: resolve publication, verify fresh protected-runner production routes, then complete missing-source diagnostics and remaining source/INSERT/teacher attribution evidence. Genuine graded Activity completion still requires immediate possible-credit confirmation. No ticket status was changed.
- Lovable imported exact `bcd7eec` and reported preview ready. This inactive checkpoint was not published; live functional acceptance remains `122eadf`. See the app writer/client/child readiness documents and foundation verification record before continuing.
- #166/#167 and the later functional tickets remain open; #178 design review remains deferred. Backend deployment occurred under explicit authorization; no Lovable credits, agent prompts or grading requests were used. Root browser interceptions and device overrides were cleared.
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

- Yahunatan: await approval of the V7 recap before posting the exact reviewed package. Current preview and primary record are linked above.
- RRC films: seeking is dead on production because the host ignores Range; hosting move is a P0 decision in [[tasks]] Next.
- Testing Centre: copy decisions, P3 design notes, practice-test freshness filter, scoped-world question, pre-`776f69b` run repair. All in [[tasks]] Next.
- Booking is not production-safe on cancellation or recent Google Calendar changes until the P1 batch is fixed and live-verified.
- Archived knowledge (product specs, entities, concepts) re-enters organically via `raw/` ingests when actually needed — do not bulk re-import.
- Corpus is empty by design; it fills from teaching materials and transcripts as they are ingested.
- **Failing lsatu tests, updated 2026-07-16:** `ConclusionTypeLab` is already handled per Joshua — do not investigate. `page-six-switchboard` and `Practice` remain genuinely failing (pre-existing, reproduce on a clean baseline, fail standalone — NOT the documented suite-load flake) and are deferred, not resolved.

<!-- brain-automation-alerts:start -->
<!-- brain-automation-alerts:end -->
