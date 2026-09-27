# Practice Exams: Brainstorm / Discovery Notes

Date: 2026-09-26 · Goal: Define LSAT U's Practice Exams navigation and unfinished exam experience using the supplied LexPrep example and the current Testing Centre.
Status: in progress
Context sources: User screenshots and browser comment (2026-09-26); `wiki/hot.md`; `wiki/tasks.md`; LSAT U code; live LSAT U `/testing` and LexPrep Practice Exams, Attempts, All Exams, and PrepTest detail pages inspected on 2026-09-26.

## Summary / key decisions

- User-confirmed: Rename the classroom navigation item from "Testing Centre" to "Practice Exams".
- User-confirmed: Use the LexPrep example for the initial Practice Exams structure: landing page, All Exams, and Attempts. Do not copy the paywall, payments, or unrelated features.
- User-confirmed: Keep an "Unfinished exams and sections" area on the Practice Exams landing page, with a resume action for full exams and standalone timed LR and RC sections. Custom drills remain in Drill per the accepted recommendation.
- User-confirmed: Make unfinished work persist across devices under the student's account, even though this requires a larger persistence change.
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

## Open flags (pending input)

- Legacy browser-only full exams have no stored account identity. Decide how a signed-in student claims existing runs without attaching another user's work on a shared browser. -> Joshua (product decision); implementation to enforce.
- Decide what happens to a previously started full exam after the student's PrepTest access changes. -> Joshua (access policy).
- Decide whether active timed sections keep counting while the browser is closed, or resume with the saved remaining time. -> Joshua (testing experience).
