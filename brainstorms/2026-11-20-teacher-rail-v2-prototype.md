# Teacher rail v2 prototype
Date 2026-11-20 · Synthetic-data prototype emulating LexPrep's docked chat rail in LSAT U's look. Continues [the rail brainstorm](2026-11-19-classroom-navigation-and-teacher-rail.md).

Files: `design/prototypes/teacher-rail-v2/index.html` (app), `compare.html` (390 / 924 / 1440 side by side). Serve with launch config `teacher-rail-v2-static` (http://localhost:8135).

## Built
- Docked rail pushes the page (padding-right, 200 ms), no overlay. 384 px, 420 px from 1280. Bell and rail toggle top-right of the page header; Ctrl + . toggles.
- One rail header row: view menu (or three icons, prototype toggle), chat tabs, "+N" overflow, +, Inbox. Active tab charcoal; unread dot; pencil for unsent message.
- Name line with Open student record; thread with New messages divider and Jump to latest; pinned composer; failed send keeps the text with Retry.
- Student access with Needs access / All students; signup alert opens and highlights the row.
- Student work follows the active student, Change / Follow active student, one assignment in progress with Resume, Discard confirm, failure keeps edits.
- Phone below 768: full-screen rail with Back; height bound to the visual viewport.

## Walkthrough results (in-app browser, scripted clicks)
Passed: overflow chat opens and stays visible; per-student unsent messages survive switching and refresh; new student shows "nothing is created until you send"; assignment for Celia keeps recipient and note while Work follows Dakota; refresh restores it; failed send then Retry; closing a tab with text asks Keep open / Discard and close; bell clears badge on open; signup alert lands in Needs access with the row highlighted.

## Findings to decide
- Tabs visible: 924 px shows 2 chat tabs + overflow; 1440 shows 3. Three view icons in the row cost ~64 px, i.e. about one tab.
- At 924 the Classroom nav is already a drawer (1024 rule), so the page card keeps ~520 px.
- Phone keyboard: simulated by shrinking the visual-viewport height; composer stayed above it. Not checked on a real phone.
