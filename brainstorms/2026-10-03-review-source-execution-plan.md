# Finish Review by connecting saved sources

Date: 2026-10-03
Status: execution plan, not implementation authorization. LR saved feedback/provenance work is separate and underway. Review code, backend changes and live writes have not been performed by this plan.

Recommendation: reuse the existing Review system. Connect historical Intro to LR first because its exact saved attempt and backend source resolver already exist. Then define the remaining source bindings together, deploy one reviewed additive backend batch, and reuse the saved review panel across those adapters. Do not rebuild the queue or migrate historical answers into invented attempts.

## What already exists and what each source still needs

The source audit inspected the published implementation at `abd65fc`; the subsequent `2fa3319` release changes bank labels only. Existing publication and runtime observations below come from saved verification records, not a new live source-by-source walk on 2026-10-03. Open tickets do not mean these features are unbuilt.

| Source | Existing implementation and identity | Remaining work and its purpose |
|---|---|---|
| Historical Intro to LR | Drills 3.1 through 3.5, 3.7 and 3.9 map authored content to exact owner-filtered `intro_lr_attempts.id`. Queue and detail already exist. Existing episode RPC resolves this source kind. | Add route binding, saved episode panel and teacher loader. Let students finish review of an existing saved miss without altering the attempt. Future producer logging still needs durable acknowledgement; historical unsaved answers remain absent. |
| Three native Intro to LR labs | Main Conclusion, First-Sentence vs Rebuttal and Conclusion Type have distinct response UUIDs, run UUID and per-question ordinal. Exact queue/detail, student episodes and teacher reason already exist. | Prove reload, failed save/retry, completion, later miss and teacher/student agreement. Pending source submission recovery is currently mounted-page-only. This is acceptance and a bounded durability gap, not a new lab implementation. |
| Hard Sentences cluster | Exact `intro_lr_attempts.id`; source/owner validation; queue/detail, episodes and teacher selection. | Verify the same saved review lifecycle. Harden future fire-and-forget source logging separately. Do not label an unknown historical first answer as recorded. |
| Hard Sentences capstone | Exact owner and `bootcamp_kv.record_id` envelope; M5/item payload validation; queue/detail, episodes and teacher selection. | Verify the same lifecycle. Preserve envelope identity because historical payload UUIDs can differ. |
| Custom/guided LR saved runs | `drill_runs` has distinct run UUIDs, frozen queue and answers. Saved feedback/provenance work is underway separately. The wrong-answer journal aggregates by question. | Add direct exact run/question review binding. Keep retakes separate and prevent question-wide journal completion from closing another sitting. |
| LR journal and flags | Queue, journal detail, flag notes and return filters are published. | Bind new review work to explicit saved evidence. A qid-aggregate journal cannot silently stand in for a distinct attempt. Marking reviewed must leave flags and source answers intact. |
| Standalone LR sections | Exact completed-section blank adapter exists. Answered misses currently enter through the journal. | Add exact sitting/question miss binding. Keep the original section context and distinguish opened/left blank from never opened. |
| Standalone RC drills | Exact `(sessionId, qid)` adapter; completed misses and flags; active flags continue the drill without answer review. | Add separate saved episodes and explicit eligible skipped-answer handling. Current RC reanswer can create a scored attempt, so the new review answer must use the episode ledger instead. Preserve active-run protection. |
| Full PrepTest LR | Completed parent/leg gates and exact run/leg/question detail; misses, flags and blanks already supported. | Connect episodes to the same completed source. Preserve parent and leg ownership/completion checks and repeated sittings. |
| Full PrepTest RC | Frozen-session first answer; completed misses/flags with exact context. | Add episodes and explicit skipped-answer coverage where reliable evidence exists. Do not infer a blank from a missing response alone. |
| Generic Activities | Completed assignment/timestamp and attributable judged responses required. Exact assignment/item detail, first/latest answers and read retry exist. | Add episode source binding, panel and teacher selection. Preserve assignment UUID/item order plus response UUID/attempt number. Positive real owned Activity-miss detail still needs acceptance; the existing approved correct QA fixture does not prove it. |
| Read, Recall, Colour (RRC) | Own section history, reports, recordings and grades exist. Central Activity Review intentionally excludes section/spoken-recall formats. | Build a dedicated adapter against assignment/attempt/source-section/stimulus identity. Define eligible review from actual grade/report evidence. Unjudged recall is not an incorrect answer. Preserve recording access and existing reports. |
| Other bootcamp exercises | Official bank practice can already enter journal/section routes. Other authored exercises have mixed persistence; lesson progress can be a mutable snapshot. | Inventory actual producers, add immutable submissions only where absent, then connect supported exercises. Never reconstruct historical attempts from current progress or fabricate lost answers. |
| Teacher-selected review | Durable admin reason, canonical selected-student scope, actor checks and student completion state exist for native labs/Hard Sentences misses. | Expand the loader through the common adapters. Broader correct/flagged/skipped selections and teacher feedback require explicit contract support; current UI only offers supported saved misses. |

## Execute in the order that avoids repeated work

Engineer-hour ranges below are planning estimates, not delivery promises. They include focused implementation, meaningful tests and review; live acceptance is estimated separately. Provider/backend approvals, inaccessible fixtures and unexpected schema differences can extend elapsed time. Shared work should be done once rather than summed into every source estimate.

| Order | Task and simple purpose | Estimated engineer hours |
|---|---|---|
| 1 | Connect historical Intro LR to the existing panel, projection and teacher loader. Deliver a complete review flow using a source the backend already understands. | 3 to 6 |
| 2 | Agree common source bindings and eligible reasons, then implement adapters for LR runs/sections, RC, completed PrepTests and Activities. Keep each review tied to the exact owned submission or sitting. | 8 to 14 |
| 3 | Extend the existing protected source resolver in one additive backend batch. Validate ownership, completion, provenance and immutable identity before accepting review work. | 6 to 12 |
| 4 | Reuse one panel, queue projection and teacher loader across those bindings. Save review answers, reveal, diagnoses and completion without creating new scored source attempts. | 5 to 9 |
| 5 | Add RRC's dedicated report/stimulus adapter and exact detail. Review actual saved recall evidence with its own semantics. | 6 to 12 |
| 6 | Inventory remaining bootcamp producers, then implement missing submission contracts in bounded families. Make future answers reviewable without pretending historical snapshots are attempts. | 2 to 4 inventory; 4 to 10 per materially different producer family |
| 7 | Run a reusable real-account acceptance matrix for existing and newly connected sources. Prove the student and teacher see the same saved work. | 6 to 12 for the core source batch; 2 to 4 additional per special source family |

Existing native/Hard Sentences acceptance should begin alongside order 1 when reliable owned fixtures are available. The core batch through order 4 plus core acceptance is approximately 28 to 53 engineer hours. RRC and remaining bootcamp producer families add their own ranges. This is a scope estimate, not a ticket completion percentage.

Impact ranking: exact LR/RC/test sitting review first, Activities second, expanded teacher selection third, historical Intro LR fourth, and RRC/other bootcamp adapters fifth. Source ownership and save correctness are required foundations for all of them. Historical Intro LR comes first in execution because it is a small extension with immediate benefit. The most time is shared source adapters plus backend validation (14 to 26 hours combined); the smallest useful implementation is historical Intro LR (3 to 6 hours). Core scope is roughly 4 to 7 full engineering days, excluding deployment wait time. RRC and additional bootcamp producers are separate scope choices.

## Keep the existing episode guarantees

The deployed episode system uses exact source identity and separate student-miss/teacher-selection episodes. Opening retries return the same episode; event UUID retries return the same acknowledged payload. Only the student appends review work. Blind answer precedes recorded reveal, missed completion requires error and right-answer diagnoses, and completion is terminal. A later source attempt creates a new episode. Source answers and flags are preserved.

Extend those guarantees rather than replacing them. Resolve a source on the server using the authenticated actor and intended student. Validate the completed source and return its exact question identity. Avoid broad client-written ownership/correctness assertions. Existing source tables and writers have differing permissions, so owner-scoped data must not be described as independently certified historical correctness.

The current panel explicitly says source feedback may already have been visible. Its optional review answer and recorded Reveal do not reconstruct historical Blind Review. Keep this distinction when connecting new sources. For uncertain saves, retain the original immutable request and reconcile exact identity before allowing another event; include reload recovery if the new slice claims it.

## Prove each connected source once

Use actual owned records where available. Any new QA fixture must be clearly labeled and separately authorized; do not rewrite a student's miss for a demo. For each source, verify exact detail and reload, source read failure/retry, review event failure/retry, reviewed queue suppression, later distinct miss, flag/source preservation, and student/teacher agreement. Verify denied cross-account and stale-account responses, URL filter/last-opened return identity, narrow/docked layouts and enlarged text. Use existing tests for the shared machinery and add source-specific ownership/identity assertions rather than duplicating the same panel tests per family.

Prepare and review the additive backend proposal before seeking the required deployment-route or credit-spend approval. Do not bundle unrelated #176 Schedule backend work into Review. Published code and passing mocks are distinct from completed ordinary-account task walks.

## Evidence and implementation pointers

- [Published Review integrity and actual browser evidence](../../lsatu-review-197/docs/implementation-plans/2026-10-02-review-170-integrity-verification.md): 87 related tests, authenticated filter/detail/return, responsive checks and read-failure recovery; publication `cc294c7`. It does not certify every source's completed review lifecycle.
- [Episode deployment record](../../lsatu-review-197/docs/agent/verification/2026-09-30-review-episodes.json) and [26 ordinary-JWT checks](../../lsatu-review-197/docs/agent/verification/2026-09-30-review-episodes-live.json): deployed native/Hard Sentences contract, stable replay, student/admin agreement and unchanged source digest. The SQL artifact's old unapplied header is stale; these records are historical evidence, not a fresh backend read.
- [Source binding and projection](../../lsatu-review-197/src/lib/scopedReviewEpisodes.ts): currently recognizes native-lab and Hard Sentences routes only.
- [Reusable episode panel](../../lsatu-review-197/src/components/review/SavedReviewEpisodePanel.tsx), [service](../../lsatu-review-197/src/lib/reviewEpisodes.ts) and [protected SQL contract](../../lsatu-review-197/docs/implementation-plans/artifacts/2026-09-30-review-episodes.sql).
- [Historical Intro LR adapter](../../lsatu-review-197/src/components/review/introLrReviewSource.ts), [native adapter](../../lsatu-review-197/src/components/review/nativeLabReviewSource.ts), [Hard Sentences adapter](../../lsatu-review-197/src/components/review/hardSentencesReviewSource.ts), [Activity queue gates](../../lsatu-review-197/src/components/review/reviewQueueModel.ts) and [teacher selections](../../lsatu-review-197/src/components/review/TeacherReviewSelections.tsx).

Plan creation makes no Review implementation, new test run, backend deployment, production write or ticket-close claim. The main build sequence and wiki ledgers are maintained separately by the parent task.
