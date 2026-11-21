# My Work tabs, opened tracking and completion: Build plan
Date: 2026-10-30 · Source: brainstorms/2026-10-29-my-work-tabs-and-completion.md (Rounds 1-3)
Status: plan only, nothing built. Build on a new branch off origin/main (never main, never codex/rc-quality).

## What origin/main already has (verified 2026-10-30 by grep, not yet run)
- Migration `20261028140000_student_work_delivery.sql` and `src/lib/studentWorkState.ts`: per-student receipts with `first_opened_at`, `last_opened_at`, `read_at`, keyed by source table, source id and issuance.
- `useAssignedTodoFeed.ts` already sets `openedAt` and `isUnread` on each row from those receipts (line ~299).
- `markNoteRead` exists for Notes.
- Existing test "does not confuse opening with progress or completion" asserts that an opened row stays `assigned`.

## Conflict to settle first
Joshua chose: opened = "In progress". Main's tests deliberately say opened is NOT progress. Resolution proposed: keep the stored status (assigned / in_progress / completed) untouched and add a derived display state, `isOpened`, used only by the My Work page. Change the one test to say opening does not change stored status or completion, and add tests for the display state. Confirm with Joshua before changing that test.

**Decided 2026-10-30 (Joshua): display only.** Stored status unchanged; "In progress" is derived from the opened receipt. The one test changes as described.

**Step 2 audit (2026-10-30, grep of origin/main 61c61b4a, not run):** the open receipt is written by `acknowledgeStudentWork` via `useLoadedStudentWorkAcknowledgment`. Wired in: Classroom notes and destinations (ClassroomRouteViews, useClassroomDestinationAcknowledgment), bootcamps (BootcampGate), activities (ActivityRunner), guided drills (GuidedDrillStart), practice tests (PracticeTestRun, TimedPracticeTestRun), section directions (SectionDirections), assignment updates (AssignmentUpdate). No call found for: teacher assignments, weekly plan items. Reading Center keeps its own `last_opened_at`. Homework is probably covered through SectionDirections; confirm. Those are the types to wire or map.

Worktree: `C:\Users\Joshu\dev\ai-os-projects\lsatu-mywork` on `claude/my-work-tabs-progress` (from origin/main). `npm ci` was started there; baseline tests not yet run.

## Build steps
1. Branch `claude/my-work-tabs-progress` off origin/main. Run existing My Work tests first for a baseline.
2. Verify opening is written for every type: list which assignment types call the receipt write on open (homework, guided drill, activity, teacher assignment, weekly plan, practice test, Reading Center, lessons). Add the call where one is missing. Receipts must be idempotent and keyed by issuance so a reissue starts unopened.
3. Feed: add derived `displayState` = to_start | continue | completed | unverified, plus `progressLine` text per type ("6 of 10 done", "Opened, not started"). Completion logic untouched.
4. Page layout: segmented control (Notes / Assigned work / Completed) with counts, Assigned strongest, 44px tap targets. Assigned splits into "Continue" above "To start". Keep search and filters.
5. Row buttons: Start / Continue / Review. Completed rows show date, result where one exists, Review.
6. Move on finish: when saved work proves done, row leaves Assigned, tab counts update, short "Moved to Completed" message.
7. Unverifiable: row stays in Assigned, shows "We couldn't check this. Tap to retry" (replaces "Progress unverified"); retry refetches that row's evidence.
8. Notes: Unread marker per note and Unread count on the tab, from `read_at`.
9. Teacher override: mark Completed or reopen, written as a teacher override record, never touching student answers. Needs a table or column and RLS; design in step 2 of review. Existing student work is never modified or removed (optional fields, fallbacks).
10. Copy: plain wording, no em dashes, no internal labels; log new strings in wiki/COPY-CORRECTIONS.md if corrected.

## Verification (run before saying done)
- Unit tests: feed state per type (unopened, opened, saved, done, unreadable evidence); reissue resets opened; override mark and reopen.
- Browser, signed in as a test student on a localhost port: open each type once, confirm it moves to Continue, finish one, confirm it lands in Completed with the message; force a failed evidence read, confirm Retry. Never clear browser storage.
- Mobile width and dark mode screenshots of the tabs.
- Typecheck, lint, full test run. Then PR; merge only on Joshua's word, then publish with free deploy_project and prove the bundle changed (standing rule). Teacher override table needs a migration; edge functions or credit-spending Lovable actions need Joshua's confirmation first.

## Risks
- Opening on first view marks work "In progress" even if the student only glanced. Accepted by Joshua.
- Teacher override schema is the largest unknown.
- Types with no receipt write today will look unopened until fixed in step 2.
