# My Work tabs, completion and progress tracking: Brainstorm / Discovery Notes
Date: 2026-10-29 · Goal: Make Notes / Assigned work / Completed visually distinct, and make work auto-move to Completed when truly done, tracked from first open.
Status: shipped 2026-10-30 (PR 255, live); teacher override, completion dates and some open receipts still open. See 2026-10-30-my-work-build-plan.md
Context sources: LSAT U repo (ai-os-projects/lsatu, checked out on codex/rc-quality): src/pages/MyWorkPage.tsx, src/hooks/useAssignedTodoFeed.ts, src/lib/studentWorkEvidence.ts. Screenshots of the live page (2026-10-29).

## What Joshua asked (verbatim intent)
- Tabs Notes / Assigned work / Completed should be clearly distinguished, not just side by side; keep hierarchy and improve UX.
- Finished work leaves "Assigned work" and lands in "Completed" automatically, verified.
- Opening and closing work is tracked, per what was assigned (a section, a drill, a course...).
- Opened-but-unfinished work shows a visible (red) marker.

## Facts found in code (verified 2026-10-29)
- Status already has three values: assigned / in_progress / completed (useAssignedTodoFeed.ts).
- Completion is computed per type from saved work evidence (homework, guided drill, activity, teacher assignment, weekly plan, Reading Center). Rows with unreadable evidence show "Progress unverified".
- Completed tab is the same list filtered to status completed.
- Branch checked out here (codex/rc-quality) has a simpler My Work page than the live screenshot (search, subject and type filters, "To start 10"). The redesign must be built on whatever main holds. Flag.

## Summary / key decisions
- Tabs: segmented control with a count on each tab, Assigned work visually strongest, larger tap targets (Q1, confirmed).
- Completion: automatic per assignment type from saved work, plus teacher-side override; no student self-marking (Q3, confirmed via "go with recommended").
- Completed rows show date, result where one exists, and a Review button (Q4, confirmed via recommendation).
- Scope: must work for every assignment type and be plain enough for anyone to understand (Q5/Q6).
- "Red" marker: Joshua says "read typo". My reading, UNCONFIRMED: he meant an opened/read marker, not the colour red. Re-asked in Round 2.

## Q&A log
### Round 1 (answers received 2026-10-29)
#### Q1 - Tab design
- Recommended: segmented control with counts, Assigned strongest.
- Captured: "recommended option and larger taps" = accept (a), make tap targets larger.
#### Q2 - Meaning of "red"
- Captured: "read typo" (his words). Tentative: he wrote "red" but meant "read" (opened) marker. Not confirmed.
- Flags: confirm in Round 2.
#### Q3 - Who decides complete
- Captured: go with recommended: automatic per type + teacher override, no student self-marking.
#### Q4 - Completed visibility
- Captured: recommendation (a): date, result where one exists, Review button.
#### Q5/Q6 - Types and audience
- Captured: "make sure it's broadly useful and understandable for anyone" = cover all assignment types, plain wording. No specific broken type named.
- Flags: no known-misbehaving types; I will test types myself.

### Round 2 (answers received 2026-10-30)
#### Q1 - Marker meaning
- Captured: "typo i meant to say read". The marker is an opened/read marker, NOT the colour red. Resolves the Round 1 flag.
- Flags: I recommended an accent-colour "In progress" badge with red kept for overdue; he answered the question as "read", so the badge wording is mine to propose and confirm in Round 3.
#### Q2 - When "In progress" starts
- Captured: ON FIRST OPEN (opened, even with nothing saved). Overrides my recommendation (after first save).
- Flags: needs a new "opened" event written per assignment; unverified whether the live app writes one today. Opened-but-nothing-saved is distinct from saved-progress; decide whether the row shows both.
#### Q3 - Continue group
- Captured: Yes (recommended). In-progress work gets a "Continue" group above "To start".
#### Q4 - Row buttons
- Captured: Yes (recommended). Start / Continue / Review, with a progress line on each row.

#### Q5 - Moves to Completed
- Captured: Yes (recommended). Finished work moves immediately, with a "Moved to Completed" message.
#### Q6 - Completion can't be checked
- First asked unclearly; Joshua asked who checks and what "check" means ("/waitwhat"). Re-asked in plain words: the app (not a person) reads saved work to decide done/not done; sometimes the read fails.
- Captured (2026-10-30): Keep in Assigned and add a Retry: "We couldn't check this. Tap to retry". Nothing moves by mistake.
#### Q7 - Notes unread
- Captured: Yes (recommended). Notes tab gets an Unread marker and count.

### Round 3 (answers received 2026-10-30)
- Opened with nothing saved: same "In progress" badge, row sits in Continue, progress line reads "Opened, not started".
- Teacher override: mark any row Completed, or send a Completed row back to Assigned; the student sees it move.

## Open flags (pending input)
- Still unverified in code: whether the live app writes an "opened" event per assignment type; whether main's feed logic matches the checked-out branch. Check on a fresh branch off main before building.
- Which branch holds the live My Work UI shown in the screenshot -> me (check main).
