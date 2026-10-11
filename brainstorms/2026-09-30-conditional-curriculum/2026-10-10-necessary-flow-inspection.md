# Necessary page reading-flow revision

User explicitly authorized fixing page hierarchy, larger text, better spacing and flow, earlier interaction, and Claude Code review of actual UI and text. Codex builds, Claude inspects with configured CLI model. Maximum two inspection rounds/two fix rounds. Local only; no commit/push/deploy. Preexisting checkout is extensively dirty; baseline 67230dfae74a1466515d570fcb7b8a96ab5cb9c5 does not isolate this turn. Review this bounded scope, not unrelated work.

## Changed files and acceptance

- ConditionalReferenceSequence.tsx (under src/bootcamps/conditionals/components): necessary ReferenceStep 4 now short definition, original sentence figure, one takeaway, interaction, then explanation of required versus enough. Removed abstract Required for what paragraph and duplicated comparison. Both-roles caveat moved to details. Group2 seven expressions, worked examples, practice and video preserved.
- NecessaryConditionExperience.tsx: three concrete cases, law student, history student explicitly not enrolled, nonstudent. Distinguish facts given from deductions; never infer nonenrollment from history alone. Stable live region, keyboard native buttons, selected aria-pressed, brief visual animation. Inspect all text for intuitive teaching and logical precision.
- sufficient-condition-experience.css: scoped nc-lesson rules increase teaching paragraphs to20px (18px at<=640), labels16px, supporting text18px, consistent measure/spacing, responsive stacking. No impact to sufficient lesson.
- NecessaryConditionStatement.tsx: observer does not override prior user replay; reduced-motion hides no-op replay via CSS. Existing readable whole clause preserved.
- NecessaryConditionExperience.test.tsx and OpeningCourseContent.test.tsx: three cases and early interaction order regressions updated. Read tests.

## Actual UI evidence to inspect

Use Read on these PNGs as well as source. They are screenshots from the running browser, not mockups. If image Read is unsupported, disclose that; do not claim visual review from source alone.
C:/Users/Joshu/.codex/visualizations/2026/10/10/01a1282c-ac7e-7380-90fe-9ca58e32512f/necessary-flow-opening.png
C:/Users/Joshu/.codex/visualizations/2026/10/10/01a1282c-ac7e-7380-90fe-9ca58e32512f/necessary-flow-interaction.png
C:/Users/Joshu/.codex/visualizations/2026/10/10/01a1282c-ac7e-7380-90fe-9ca58e32512f/necessary-flow-mobile.png

Inspect text size, reading sequence, repetition, logical meaning, spacing and hierarchy. The host independently clicked all three cases, used keyboard Enter on History student and measured 20px teaching text/16px labels on desktop,18px on actual CSS320 with no overflow. Screenshots only cover specified regions; do not pretend to have operated browser. Full relevant source gives remaining text. User asked meaningful teaching quality review, not merely absence of runtime defects.

Verification: 30 tests pass using npm run test -- --run src/bootcamps/conditionals/components/ConditionalReferenceSequence.test.tsx src/bootcamps/conditionals/components/OpeningCourseContent.test.tsx src/bootcamps/conditionals/components/NecessaryConditionExperience.test.tsx. Host runs npm run typecheck and npm run build; final browser matrix includes320/960/1600, reduced motion and default side panel. Reviewer reads only; no edits.
