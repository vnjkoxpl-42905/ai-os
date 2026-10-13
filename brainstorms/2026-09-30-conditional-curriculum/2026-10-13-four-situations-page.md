# Four situations page (2026-10-13)

Joshua asked for his Conditional Relationships chart (`C:/Users/Joshu/Desktop/Conditional_Relationships_Source_Chart.html`) to follow the Contrapositive lesson as its own page. The same chart is already preserved in `raw/sources/conditional-reasoning-voice-standard/conditional_reasoning_transcription.html` (line 279).

Implemented, provisional until Joshua reviews (worktree `ai-os-projects/lsatu-conditional-bootcamp`, uncommitted):
- New course step `four-situations`, "What the rule tells you", directly after `contrapositive`.
- `components/FourSituations.tsx` + `four-situations.css`: definition panel, the necessary-condition trap, the four-row chart (same rows and order as the source; original pool/lifeguard example), habit paragraph, Pop Quiz (library reminder-text rule, one item per situation).
- `SufficientQuiz.tsx` now exports a shared `QuickQuiz`; the Sufficient quiz is unchanged in behaviour.
- Tests: course count 21 to 22, lessons 9 to 10, position pinned after contrapositive; two content tests for the page.

Verified: tests pass (the full-suite run has one load timeout in LessonPages.test.tsx, which passes alone); app typecheck passes; chart rendered at the 640px pane width (cards) and measured at 1280px (three columns, no overflow); quiz wrong-answer feedback clicked live.

Not done: no narrated video (the gold standard calls for one). Source wording "ignore the conditional" was paraphrased to "Set it aside".
