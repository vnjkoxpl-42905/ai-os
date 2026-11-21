# Necessary-condition typography and motion

User authorized local implementation of the previous motion plan, a brief bold subtitle, better presentation and Claude Code review after implementation. No commit, push, deployment or paid media generation.

Codex is builder; fresh Claude Code is inspector using configured CLI defaults. Maximum two inspection rounds, two fix rounds. This is standalone implementation followed by requested inspection, not a claim of independent plan approval.

Baseline commit: 67230dfae74a1466515d570fcb7b8a96ab5cb9c5. Checkout already contains extensive unrelated and earlier untracked work. Limit this inspection to the following current-turn changes; do not require remediation of unrelated files:
- src/bootcamps/conditionals/openingCoursePath.ts: necessary subtitle changed to What the sufficient condition requires.
- src/bootcamps/conditionals/components/OpeningCourse.tsx: bold necessary subtitle only.
- src/bootcamps/conditionals/components/NecessaryConditionStatement.tsx: new complete-sentence figure, condition labels, indicator explanation, once-visible CSS emphasis and replay.
- src/bootcamps/conditionals/components/ConditionalReferenceSequence.tsx: mounts figure instead of old blockquote; replaces studenthood jargon with ordinary language.
- src/bootcamps/conditionals/components/NecessaryConditionExperience.tsx: keyed visual verdict, existing live region remains mounted.
- src/bootcamps/conditionals/components/sufficient-condition-experience.css: figure, labels, mobile stacking, highlight and verdict motion, reduced-motion treatment.

Acceptance: full sentence immediately readable; complete then clause visually emphasized; then distinguished from the condition; labels explain enough versus required without reversal/causality/time; replay usable by keyboard; no repeating automatic motion; reduced-motion has all information and no animations; no overflow at narrow and wide viewports; existing two-state interaction and films preserved. Inspect pedagogy and implementation and suggest meaningful improvements. Do not edit project files.

Proof: npm run test -- --run src/bootcamps/conditionals/components/ConditionalReferenceSequence.test.tsx src/bootcamps/conditionals/components/OpeningCourseContent.test.tsx src/bootcamps/conditionals/components/NecessaryConditionExperience.test.tsx (30 passed). Host also runs npm run typecheck and npm run build; browser checks performed separately. Reviewer cannot claim browser execution.

Source rationale: vault wiki/sources/claude-now-does-video-free-javascript.md and references/website-design-planning.md. Reuse the existing ivory, ink and brass visual system. Native HTML/CSS rather than a new video dependency.
