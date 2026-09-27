# Practice Exams: Brainstorm / Discovery Notes

Date: 2026-09-26 · Goal: Define LSAT U's Practice Exams navigation and unfinished exam experience using the supplied LexPrep example and the current Testing Centre.
Status: in progress
Context sources: User screenshots and browser comment (2026-09-26); `wiki/hot.md`; `wiki/tasks.md`; LSAT U code; live LSAT U `/testing` and LexPrep Practice Exams, Attempts, All Exams, and PrepTest detail pages inspected on 2026-09-26.

## Summary / key decisions

- User-confirmed: Rename the classroom navigation item from "Testing Centre" to "Practice Exams".
- User-confirmed: Use the LexPrep example for the initial Practice Exams structure: landing page, All Exams, and Attempts. Do not copy the paywall, payments, or unrelated features.
- User-confirmed: Keep an "Unfinished exams and sections" area on the Practice Exams landing page, with a resume action for full exams and standalone timed LR and RC sections. Custom drills remain in Drill per the accepted recommendation.
- User-confirmed: Make unfinished work persist across devices under the student's account, even though this requires a larger persistence change.
- User-confirmed: Attempts should show both in-progress and completed full exams and timed sections, with available result links. All Exams should have PrepTest detail pages showing sections, start options, and the student's attempts.
- User-confirmed: Preserve attempts and results after PrepTest access is lost, while preventing resume into questions the student can no longer access.
- User-confirmed: An active timed section pauses when the browser is closed. Time away must not count against the student. This supersedes the prior wall-clock recommendation.
- User-confirmed on 2026-09-27: Switching to another tab keeps the section clock running; leaving the exam page or closing the browser pauses it at saved elapsed time. A second device may take over only after a clear "Continue on this device" action, and the first device must stop saving.
- Unresolved: Joshua rejected a one-time manual claim prompt for older browser-only full-exam runs, expecting work to be tied to the student's database account. The existing full-exam implementation is browser-only and legacy keys carry no user identity. A safe migration path still needs a decision.
- The user requested a grill-me interview after inspecting the example and current product.
- Verified current behavior: LSAT U already has an "Unfinished sittings" list for in-progress full PrepTests, shown when the current browser has one. It uses local browser storage. Standalone LR and RC sections resume through separate stores and do not appear in that list.
- Verified reference: LexPrep's Practice Exams landing has two start actions and an "Unfinished exams and sections" area. Its sidebar has Attempts and All Exams subpages. The Attempts page is paywalled for the inspected free account; All Exams lists PrepTests and a detail page shows sections and attempts.
- Superseded tentative recommendation (before Round 1): Keep the two start actions and place a unified unfinished area below them. Round 1 confirmed the unified scope and added All Exams, Attempts, and cross-device persistence.
- Verified technical boundary: LSAT U's existing `practice_test_runs` database table has owner policies and a revision field, but the full-test UI still reads and writes browser localStorage only. LR timed-section progress uses a local-first store that syncs to Supabase; RC progress is already in Supabase. Cross-device resume requires conflict-safe writes and timer restoration, especially for RC.
- Verified product boundary: `/history` already offers broad question/section review, so a new Attempts page can focus on exam and timed-section sittings. Existing assigned-only access restricts available PrepTests and should be preserved unless Joshua explicitly changes that rule.

## Q&A log

### Round 1

#### Q1 - Practice Exams navigation
- Asked: Should LSAT U use a Practice Exams landing page, All Exams page, and Attempts page, without copying LexPrep's paywall?
- Recommended: Yes; make Attempts useful without a paywall and keep the two start options on the landing page.
- Captured: Joshua accepted the recommendation for all three pages. The LexPrep screenshots provide the idea and initial structure, not a complete copy. No payment components or paywall belong in this work.

#### Q2 - Unfinished work
- Asked: Should the landing page list unfinished full exams and standalone timed LR and RC sections, while leaving custom drills in Drill?
- Recommended: Yes; each item should identify its PrepTest, current section, progress, and Resume action.
- Captured: Joshua accepted the recommendation.

#### Q3 - Across-device persistence
- Asked: Should an unfinished exam appear when a student signs in on another device?
- Recommended: Yes; replace the browser-only limitation with account-backed persistence.
- Captured: Joshua explicitly accepted the larger persistence change.

### Round 2

#### Q4 - Attempts page
- Asked: Should Attempts show in-progress and completed full exams and timed sections, linking to available results while leaving general question history on History?
- Recommended: Yes.
- Captured: Joshua said it "should show both" and accepted the recommendation.

#### Q5 - All Exams page
- Asked: Should each available PrepTest open a detail page showing sections, start options, and that student's attempts?
- Recommended: Yes; preserve current assignment and access rules.
- Captured: Joshua answered yes and asked for the recommendation to be restated.

#### Q6 - Existing browser runs
- Asked: Should the app present a one-time list of local unfinished exams for the student to claim individually?
- Recommended: Yes, because old browser storage keys do not identify an account.
- Captured: Joshua said no to a manual claim prompt. He expects work to be in the student's account database, and wants attempts and results preserved.
- Flag: Current full-exam runs are saved only in browser localStorage, despite an existing database table, and the old keys have no user identity. Do not infer permission to auto-attach them to whoever signs in. Resolve the safe migration behavior in a later round.

#### Q7 - Access changes
- Asked: If a student later loses access to a PrepTest, should they still be able to resume its unfinished questions?
- Recommended: Preserve the attempt and result but block resume into inaccessible questions.
- Captured: Joshua accepted the recommendation and emphasized that access should be handled carefully.

#### Q8 - Clock while closed
- Asked: Should time continue to pass while a timed section is closed?
- Recommended: Yes, using a wall-clock deadline; this recommendation was rejected.
- Captured: Joshua said the section "should pause" when the browser is closed; time should definitely not keep running.

### Round 3 (2026-09-27)

#### Q9 - Older unfinished full exams
- Asked: Should older browser-only runs remain usable on their original browser without automatic migration, while new runs sync to the account?
- Recommended: Yes, to avoid attaching a shared browser's old run to the wrong account.
- Captured: Joshua invoked wait-what for this question. No decision yet; explain the existing storage distinction in simpler terms before asking again.
- Flag: Do not infer agreement to leave older runs on one device.

#### Q10 - Pause boundary
- Asked: Should switching tabs keep the clock running while leaving the exam page or closing the browser pauses it?
- Recommended: Yes.
- Captured: Joshua accepted the recommendation.

#### Q11 - Two-device handoff
- Asked: Should a second device explicitly take over an unfinished section and stop the first device from saving?
- Recommended: Yes, with a clear "Continue on this device" action.
- Captured: Joshua accepted the recommendation.

## Open flags (pending input)

- Legacy browser-only full exams have no stored account identity. Manual claim was rejected; decide how to preserve old local runs without attaching another user's work on a shared browser. -> Joshua (product decision); implementation to enforce.
- Q10 pause boundary and Q11 handoff are confirmed; implementation must save elapsed time and enforce one active device with account-backed revision/lease logic. -> Implementation design.
