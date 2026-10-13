# Four situations page (2026-10-13)

Joshua asked for his Conditional Relationships chart (`C:/Users/Joshu/Desktop/Conditional_Relationships_Source_Chart.html`) to follow the Contrapositive lesson as its own page. The same chart is already preserved in `raw/sources/conditional-reasoning-voice-standard/conditional_reasoning_transcription.html` (line 279).

Implemented, provisional until Joshua reviews (worktree `ai-os-projects/lsatu-conditional-bootcamp`, uncommitted):
- New course step `four-situations`, "What the rule tells you", directly after `contrapositive`.
- `components/FourSituations.tsx` + `four-situations.css`: definition panel, the necessary-condition trap, the four-row chart (same rows and order as the source; original pool/lifeguard example), habit paragraph, Pop Quiz (library reminder-text rule, one item per situation).
- `SufficientQuiz.tsx` now exports a shared `QuickQuiz`; the Sufficient quiz is unchanged in behaviour.
- Tests: course count 21 to 22, lessons 9 to 10, position pinned after contrapositive; two content tests for the page.

Verified: tests pass (the full-suite run has one load timeout in LessonPages.test.tsx, which passes alone); app typecheck passes; chart rendered at the 640px pane width (cards) and measured at 1280px (three columns, no overflow); quiz wrong-answer feedback clicked live.

Not done: no narrated video (the gold standard calls for one). Source wording "ignore the conditional" was paraphrased to "Set it aside".

## Necessary page: source passage woven in (2026-10-13)

Joshua asked to weave in the source's opening of the Necessary section (transcription HTML line 206-208). Added "Where the certainty is" after the approved takeaway: the name says it, the necessary condition is the place of certainty, it is what you can prove (law-school example). Group 2 intro now says the necessary condition is the part after "then" in an if-then rule and these words mark that same part. Deliberately not carried over: "slams the door that the sufficient condition opens" (door is banned student wording) and "then" as a standalone indicator (rejected 2026-10-11). "At some point" dropped (necessary is not about timing). Provisional, uncommitted. Tests 45/45 on the affected files; checked in the preview.

## Early contrapositive step removed (2026-10-13)

Joshua approved ("yes do what u want") removing step 5, `missing-requirement` ("The contrapositive", Maya question plus reference step 7 four-situations explorer on the raffle rule). It duplicated the approved Contrapositive page and the new Four situations page. Its two films (enough-to-know, what-stays-open) still play on the Sufficient page, so no media left the course. Removed: path entry, `MissingRequirementNote`, its content test. `missing-requirement-note.css` deleted with Joshua's OK (2026-10-13). Course is 21 steps (9 lessons, 12 drills). Conditional suite and app typecheck pass; lessons list checked in the preview.
