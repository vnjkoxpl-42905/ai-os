# LSAT U audit implementation: connect sessions to preparation, recap, and follow-up

Date: 2026-10-02
Parent audit: #165. Decision source: #155. Implementation ticket: #176.
Repository: `vnjkoxpl-42905/lsatu-684d89db`.
Delivery: one isolated implementation branch and reviewable pull request. Publication follows independent host verification.

## The result students and Joshua need

A one-to-one appointment becomes a stable context for the work around that appointment. A student opens Schedule, selects an appointment, and sees three groups: Preparation, Recap, and Follow-up. Each group opens the exact existing saved record. Joshua sees the same appointment and links in the selected-student dossier and can deliberately connect existing owned records to it.

Students must never see another student's records or teacher-only, draft, archived, or locked material through this feature. An appointment whose end time has passed does not establish that any linked work was completed. Missing links and failed reads must look different.

This is a substantial, bounded slice of the existing audit. It does not authorize rebuilding the entire platform or closing all remaining tickets. Finish the model, student interface, teacher association controls, Notes integration, regression coverage, and verification documentation together.

## Existing work to preserve

The seven-destination navigation, assignment-aware exam access, signed-in Attempts recovery, source diagnostics, protected timed runners, Review adapters, Progress/History, study tools, and weekly settings already have implementations. Do not replace them while building this slice.

GitHub main was observed at `124fee3a4f14952c5b05abcf3bedd18dd22d1f18` on 2026-10-02. Start from the latest main, record the actual baseline, and preserve later changes. This historical SHA is orientation, not a requirement to reset the repository.

Fourteen functional audit tickets and deferred design ticket #178 remain open. A shipped feature is not proof that its full acceptance list passed. This slice contributes to #176 and supports #169/#177; it does not certify those tickets.

## Locked decisions

1. Reuse the current booking/session source and timezone formatting. Preserve booking, management, cancellation, and rescheduling behavior.
2. Identify a booking by the pair `source` and `id`. Known booking sources are `redemption` and `single_session`. The display adapter uses `booking-{source}-{id}`; never treat an arbitrary display string as authoritative ownership.
3. Associations are explicit. Never match records by title, nearby dates, student name, or email similarity.
4. Existing `classroom_items.metadata_json` is the intended additive association home, subject to verification of the existing authenticated update contract. Preserve `source_table` and `source_id`, which identify assignment/content provenance.
5. Link existing records. This slice does not generate preparation, author recaps, assign new exercises, send notifications, or rewrite old work.
6. One classroom item has at most one session association in this version. Moving it requires an explicit teacher action showing the old and new appointment. Do not overwrite silently.
7. Removing an association removes only this feature's metadata. It never deletes the item, assignment, answer, recap, or booking.
8. Student and teacher views use one shared parser/projection and exact source-link resolution. Preserve the existing source-specific destination builder.
9. Authorization remains server enforced. UI filtering adds correct presentation; it cannot substitute for row permissions.
10. No schema, RLS, Edge Function, model, production database, entitlement, or canonical question-content changes in this deliverable.

## User stories

1. As a student, I can select my appointment and see its assigned preparation before attending.
2. As a student, I can open the exact saved preparation record and return to the selected appointment.
3. As a student, I can find the published recap from that same appointment after the session.
4. As a student, I can open follow-up work without confusing it with preparation.
5. As a student, I can distinguish no linked recap from a recap source that failed to load.
6. As a student, I can see the appointment in the existing displayed timezone.
7. As a student, I retain visible verified links during a failed background refresh, with a retry notice.
8. As a student switching accounts, I never see the prior account's appointment or content while the next account loads.
9. As Joshua, I can select a verified student-owned appointment and associate an existing eligible record with a phase.
10. As Joshua, I can see the record's title, type, visibility, source, and existing association before saving.
11. As Joshua, I receive acknowledgment of a successful save before the UI claims it was linked.
12. As Joshua, a failed or uncertain save retains my selection and offers safe recovery.
13. As Joshua, I can remove a link without removing the underlying work.
14. As Joshua, I can view explicitly labeled teacher-only links that are omitted from the student view.
15. As Joshua, I see the same booking identity and student-visible links as the student's Schedule and My Work Notes.
16. As either user, an elapsed or canceled appointment never creates a false completion claim about work.
17. As either user, duplicate titles and appointments on the same day do not merge unrelated records.
18. As a keyboard or phone user, I can select appointments, open links, and use teacher controls without horizontal overflow or inaccessible dialogs.

## Source facts and hazards already found

- `useClassroomItems` scopes its query by student ID, but its comment about unlocked content does not mean the query enforces visibility/status/unlock. Explicitly enforce student presentation eligibility using the existing authoritative item contract.
- `StudentSchedulePanel` quick-add calls `classroomNotify`. Do not reuse that notification path to associate an existing record.
- `StudentBookingPanel` can return possible email matches separately. Those are not verified student-owned bookings and cannot be association targets.
- The calendar adapter can mark an elapsed booked appointment `completed`. This is calendar state, not evidence of work completion.
- Existing recaps and calendars are not automatically associated. Legacy items without explicit metadata must remain unlinked.
- Do not manufacture a relationship merely to make a demonstration appear complete.

## Data contract

Use a single versioned metadata member named `session_chain`, unless repository inspection identifies an already established equivalent. If one exists, adopt it and document the exact mapping; do not create a second competing contract.

For a new contract, use these fields:

| Field | Meaning | Validation |
|---|---|---|
| version | Contract version | Exactly 1 |
| booking_source | Booking family | redemption or single_session |
| booking_id | Original source-row ID | Nonempty valid ID according to that source's contract |
| phase | Group containing the link | preparation, recap, or follow_up |

Ownership is established by the current authenticated actor, selected subject, source-row ownership, and classroom-item ownership. A metadata field containing a student ID is not an authorization grant. Reuse existing `created_by` and item attribution for authorship; do not invent historical author claims. A recap phase must reference a recap-compatible existing item, not relabel an arbitrary drill as a recap.

Malformed, unknown-version, foreign, or unresolved associations must not create actionable student links. Teacher view should disclose an invalid or unavailable association without revealing foreign record details. Preserve unrelated metadata keys and nested values on every mutation. Never send a stale full metadata object that can overwrite concurrent changes.

Before implementing the writer, inspect the existing update API for authorization, atomic merge or optimistic concurrency, and acknowledgment. Use an existing supported atomic update/CAS contract. If the current writer cannot preserve concurrent metadata edits safely, do not add an unsafe read-then-write workaround. Complete the read path and interfaces, keep association mutation unavailable with a truthful explanation, and document the exact backend prerequisite for the host. Do not deploy a backend change as a workaround.

## Exact interface behavior

### Student Schedule

Keep the current calendar/agenda and booking controls. Selecting an owned appointment opens or expands a Session work panel within the existing Schedule surface. Its heading displays the existing appointment title, date/time, timezone, and current booking state.

Below the heading, display Preparation, Recap, and Follow-up in that order. Each record displays its title, existing type, author attribution where genuinely available, and existing verified work status where supported. Use Open preparation, Open recap, or Open follow-up as accessible action labels. Include enough title context to distinguish multiple links.

Empty group copy: No preparation linked, No recap linked, or No follow-up linked. Never say completed because a group is empty. Failed source copy identifies what could not load and includes Retry. Initial loading is distinct from empty.

Keep verified cached rows visible during background refetch failure for the same actor/subject. Mark their freshness honestly. Disable mutation or actions whose authorization cannot be confirmed by the existing contract. On actor/subject change, immediately clear prior projected data; caching must not display the previous subject.

Persist selected appointment with a versioned, validated URL query representation of source and ID. Preserve unrelated query parameters. Browser back and reload restore the same owned appointment. An invalid, unavailable, or foreign selection shows a neutral unavailable state and a way back to the user's schedule, without choosing a nearby appointment automatically.

Canceled appointments retain their legitimate historical links with a canceled label. Do not treat cancellation as completed work. Disable new linking to canceled appointments. Rescheduled appointments retain links only when the underlying source identity remains the same. If a provider creates a replacement ID, do not infer a transfer.

### Teacher dossier

Place the same Session work panel in the existing selected-student Schedule surface. Clearly label the selected student. The teacher sees student-visible links plus explicitly labeled teacher-only items permitted by existing access controls.

For a verified owned, noncanceled appointment, provide Link existing work. The dialog contains phase selection and an eligible item picker scoped to the selected student. Show item type, visibility, and any current appointment association. Require a deliberate selection and save; do not auto-select the first record.

If the item is already linked to another appointment, show both appointment identities and require explicit Move link confirmation. Saving updates only the association and waits for acknowledgment. During save, prevent duplicate submission. On failure retain the selection; distinguish unacknowledged save from acknowledged save followed by refresh failure.

Provide Remove link with confirmation explaining that the record remains available in My Work. Acknowledgment precedes removal from the panel. If the server may have committed but the response was lost, re-read authoritative association state before repeating an unsafe write. Reuse idempotent or CAS semantics where available.

Changing the selected student closes the dialog, clears draft selection, invalidates the mutation epoch, and prevents late results/toasts from affecting the next student. A late callback may invalidate the original subject's cache, but cannot alter the current subject UI.

### My Work Notes and recaps

For eligible explicitly linked records, display a session context link containing the appointment's date/time and source-backed identity. Open Schedule with that exact selection. Preserve existing record/source links, author/type labels, filters, and return behavior.

Do not move unlinked notes into a guessed session. Do not surface hidden records to students through this adapter. Teacher Work needs only a minimal adapter if necessary to resolve the same association; do not redesign the ledger.

## Ownership and exclusions

Primary permitted implementation surfaces:

- `src/lib/sessionChain.ts` and tests.
- `src/hooks/useSessionChain.ts` and tests.
- `src/components/schedule/SessionChainPanel.tsx` and tests.
- `src/pages/Schedule.tsx` and tests.
- `src/components/schedule/TodayAgenda.tsx`.
- `src/components/teacher/schedule/StudentSchedulePanel.tsx` and tests.
- `src/components/teacher/schedule/StudentBookingPanel.tsx`, minimal verified selection adapter only.
- `src/pages/teacher/students/DossierSchedule.tsx`, minimal integration if necessary.
- `src/pages/MyWorkNotesPage.tsx` and existing tests.
- `src/components/classroom/ClassroomRouteViews.tsx`, minimal session-context link display only.
- Existing classroom-item hook/helper only if a minimal, safe supported association update is required. List its exact scope before editing.
- `docs/implementation-plans/2026-10-02-schedule-176-verification.md`.

Inspect other sources as needed. Reading a file does not grant permission to redesign it. Changes outside this inventory require a documented necessary dependency; if they touch a prohibited system, stop that portion and report it.

Do not edit navigation/access policy, App route architecture, timed exam engines, Review engine, Progress metrics, weekly settings, AI callers, migrations, Edge Functions, canonical LSAT content, generated bank artifacts, AGENTS.md, or CLAUDE.md. Do not revert other contributors. Do not mutate production data, send messages/notifications, redeem usage resets, purchase credits, merge main, or deploy.

## Ordered implementation procedure

### Step 1: establish the baseline and contract map

Read repository and nested instructions. Record current branch, exact main SHA, and working-tree status. Work on an isolated feature branch. If the environment contains unrelated changes, preserve them and do not stage them.

Read the audit coverage document, #176, relevant #165/#155 requirements, and the listed source surfaces. Trace student booking ownership, teacher selected-subject scope, item eligibility, recap types, source destination resolution, and the existing metadata update contract. Write a concise contract map in the verification document before editing production code.

Checkpoint: every data family has an identified owner/filter contract; writer support and limitations are explicit. No inferred booking association or production mutation.

### Step 2: implement the shared model with behavior tests

Implement parsing, validation, source/ID identity, phase grouping, visibility eligibility, canceled-state handling, exact content links, and URL selection encoding/decoding behind one small module. Keep it pure where possible. Reuse existing eligibility and destination helpers rather than copying divergent rules.

Write regressions first for malformed metadata, foreign ownership, duplicate titles, same-day bookings, locked/draft/archived items, unknown source, cancellation, and absent links. Distinguish unresolved data from an empty valid result.

Checkpoint: the projection returns the same permitted record identities for student and teacher views, with intentional visibility differences only.

### Step 3: implement scoped reads and state transitions

Build the shared hook on existing authenticated sources. Key queries by actor and subject and by verified booking identity where appropriate. Track initial loading, same-subject refresh, partial failure, retry, and unavailable selection separately. Clear projected records on context change and reject late responses from prior context.

Do not make a source failure look like zero linked work. Retain verified same-context cached rows when safe. Avoid unbounded requests for every booking; use existing batched source reads/projections.

Checkpoint: tests prove partial failure, retry, cache retention, cross-account isolation, and late-response rejection.

### Step 4: build the student Session work panel

Integrate the shared panel into Schedule without replacing booking controls. Implement ordered groups, empty/error/loading states, exact links, selected-appointment URL persistence, and a return path. Use existing design primitives and typography.

Checkpoint: component/route tests show a student selecting one appointment, opening its exact prep/recap/follow-up, reloading and returning without changing identity or filters.

### Step 5: implement teacher explicit association controls

Use only verified selected-student bookings and eligible existing records. Implement the picker, explicit phase, move confirmation, association removal, acknowledgment, duplicate-submit prevention, and context-bound save behavior.

Use supported atomic/CAS update semantics and merge only the association member. If the existing writer is insufficient, deliver the read interface and a clearly gated unavailable writer, with the prerequisite described. Do not fake a successful save or weaken authorization.

Checkpoint: tests prove owned saves, cross-owner rejection, metadata preservation, concurrent-change rejection/recovery, unknown-result reconciliation, save failure retention, acknowledged-save/refresh-failure distinction, and actor/subject-switch safety.

### Step 6: connect Notes and teacher dossier

Use the same parsed association and URL helper in My Work Notes and the selected-student dossier. Preserve existing source actions. Add author/type labeling only from actual record fields. Do not treat elapsed calendar status as a task result.

Checkpoint: one fixture's typed booking pair and content IDs are identical across Schedule, Notes, and teacher dossier. Unlinked and hidden fixtures remain absent from student session links.

### Step 7: verify accessibility and responsive behavior

Test keyboard selection, dialog focus/escape/focus restoration, labeled actions, and status announcements. Verify actual rendered layouts at 390, 820, 1024, 1280, and 1440 pixels, including long titles and multiple links. No horizontal page overflow or clipped actions. Preserve readability at doubled text size where the harness supports it.

Use deterministic nonproduction fixtures when authenticated accounts are unavailable. Label them mocked/local; do not claim they prove production RLS, real student ownership, or live completion.

### Step 8: run release proof and inspect the diff

Run all new tests and the existing regression command below. Run full typecheck and production build, scoped lint for edited source, and diff whitespace checks. Inspect every changed/added file. Remove from the deliverable only known build-generated churn created by this run; never restore unrelated edits or delete records/files without authorization.

Checkpoint: proof commands and exact results are documented. Failed checks are repaired or explicitly block readiness. No production schema/data change, notification, or deployment occurred.

### Step 9: deliver the branch and review report

Commit only the owned verified source/tests/doc. Provide baseline SHA, final SHA, changed-file inventory, proof results, screenshots if available, limitations, and remaining live acceptance. Create a PR targeting main through the repository's permitted feature-branch flow. Do not push main or bypass safe-push protections. If branch publication is blocked, retain the local commit and report the exact restriction.

The host independently reviews and reruns proof before integration/publication. Allow at most two corrective rounds per review pass; unresolved findings remain explicit. Do not close #176 until remaining real-account acceptance is complete.

## Required regression matrix

| Scenario | Required result |
|---|---|
| Owned booking with all three phases | Exact source records in correct groups across all views |
| Empty valid booking | Three honest absence states; no completion claim |
| Booking source read fails | Failure/retry, no fabricated empty appointment |
| Item source partially fails | Named uncertainty and safe retained same-context content |
| Background refresh fails | Existing verified rows remain with freshness warning |
| Actor or selected student changes | Prior data and drafts clear; late result cannot repopulate |
| Foreign item or booking metadata | No actionable student link or foreign details |
| Possible email match only | Not eligible for association |
| Draft, archived, teacher-only, locked item | Omitted from student view; appropriate teacher labeling |
| Duplicate title or nearby appointment | No inferred merge or transfer |
| Malformed/unknown-version metadata | Safely unavailable; no crash or guessed identity |
| Source/ID collisions across families | Typed pair distinguishes the bookings |
| Canceled appointment | Historical links labeled; new linking disabled |
| Reschedule same ID / replacement ID | Same-ID links retained; replacement not automatically linked |
| Elapsed appointment | No change to work completion evidence |
| Deep link, reload, back, unrelated query | Same exact selection and preserved navigation context |
| Metadata edit race | No unrelated fields overwritten; conflict shown/reconciled |
| Double save or lost reply | No duplicate mutation; authoritative reconciliation |
| Save succeeds, refresh fails | Saved acknowledgment plus separate refresh warning |
| Student switch during save | Old save cannot alter next student's panel/toast |
| Remove link | Only association removed, record preserved |
| DST and midnight boundary | Existing timezone contract respected; no date-only matching |
| Widths and keyboard | No overflow; labeled controls and correct focus behavior |

## Proof commands

Run each command separately, following repository tooling instructions.

```text
npx vitest run src/lib/scheduleEntries.test.ts src/hooks/useBookingScheduleItems.test.ts src/lib/classroomItems.test.ts src/lib/classroomItems.route.test.ts src/pages/MyWorkNotesPage.test.tsx src/pages/teacher/students/DossierWork.test.tsx
npx vitest run src/lib/sessionChain.test.ts src/hooks/useSessionChain.test.tsx src/components/schedule/SessionChainPanel.test.tsx
npm run typecheck
npm run build
git diff --check
```

Adjust new test filenames to actual repository conventions and include every new test. Confirm existing filenames on latest main; document legitimate renames rather than silently dropping regression coverage. Run the repository's scoped ESLint invocation for every edited source file.

## Evidence required before declaring this slice ready

The verification document must include actual baseline and final commit, source and ownership contracts, metadata schema, eligibility rules, mutation support or gating, every changed file, exact test/typecheck/build/lint results, responsive/browser coverage, and unresolved findings. Distinguish automated fixture evidence, local authenticated evidence, and fresh production evidence.

Real-account host acceptance still required: one verified student-owned appointment, teacher deliberately associates legitimate existing preparation/recap/follow-up records, student Schedule and Notes resolve the identical links, teacher dossier agrees, reload persists, hidden/foreign access is rejected, and timezone/date is correct. No live mutation is implied by this implementation handoff. The host arranges narrowly authorized fixtures and publication separately.

## Stop conditions

Stop the affected portion and report a concrete blocker if ownership cannot be established, existing policies permit foreign access, metadata mutation cannot preserve concurrent edits, a requirement needs a prohibited backend change, required proof cannot run, or feature-branch publication conflicts with repository protections. Continue independent safe work where possible. Never replace missing proof with a confident claim.

No specification guarantees zero errors. Readiness requires passing observable checks, independent review, and explicit remaining limitations.
