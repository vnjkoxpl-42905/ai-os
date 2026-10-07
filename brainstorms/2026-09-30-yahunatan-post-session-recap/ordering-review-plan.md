# Review: conditional recap V7 teaching order

Started 2026-09-30. Requested by Joshua. Codex-review workflow reversed: Codex orchestrates and Claude is the read-only critic. Adapted to review an existing teaching artifact rather than application code. MAX_ROUNDS=5; first round diagnoses the current note. No implementation authorized by this review request.

## Goal

Review the current student-facing note's learning sequence. Joshua says the ordering does not make sense. Determine precisely where the note asks the student to use something before it is taught, where detail interrupts the main conceptual progression, and what ordering would better support the two central operations: applying a rule to a fact and linking rules to make a new rule. Do not presume the previous reviews or current organization are correct.

## Evidence

- Current review source: `brainstorms/2026-09-30-yahunatan-post-session-recap/concept-lesson-v7.md`.
- Actual rendered artifact: `brainstorms/2026-09-30-yahunatan-post-session-recap/conditional-reasoning-v7.html`. Static source review only; report that limitation rather than claiming live visual inspection.
- Canonical export authority: current V7 marker block in `students/yahunatan-zetvy/recaps/2026-09-16-recap.md`. Earlier blocks are history, not current content.
- Writing and teaching requirements: `.agents/skills/post-session-recap/SKILL.md`, its `references/lesson-quality-bar.md`, and `wiki/teaching-voice.md`.
- Requested quality comparison: `brainstorms/2026-09-28-recap-format/07-quantity-statements-lesson.md`. Introduce meaning, teach components, compare and combine.
- General reasoning source if clarification is needed: `corpus/lectures/logical-reasoning/must-be-true/core/2026-08-27-33013/transcript.md` and `teleprompter.md`. Shared teacher lecture is separate; do not change it or import question dialogue.

## Approach

1. Read the whole current note and voice/quality requirements. Map each concept's prerequisites and first use.
2. Evaluate the opening: are the two worked scenarios an effective preview, or do they rely on undefined ideas? Preserve Joshua's requested visible numbered distinction, but recommend how it should fit into the progression.
3. Review the sequence of definitions, advice/permission qualifiers, forward application, contraposition, four fact cases, compound negation, linking, hidden chains, invalid linking and cumulative practice.
4. Give specific findings with section names and source line references, the reading problem, and a concrete fix. Distinguish material ordering defects from optional stylistic preferences. Do not invent learner facts or prescribe new homework.
5. Recommend one complete section order, including where demonstrations and checks belong. Say what to move, what to shorten, what to merge and why. Preserve coverage, exact qualifiers, scope/existence limits, and assigned diagramming-before-LSAT order.

## Decisions and tradeoffs

The user has settled concept-first teaching, definitions, useful concrete explanations, two numbered reasoning scenarios, and readable visual hierarchy. Review how to deliver those goals. Do not ask whether to remove the lesson's core content. The teaching order is open to critique; a sequence alternative is advisory until Joshua chooses it.

## Risks and boundaries

No files may be modified by the reviewer. No platform action, student communication, assignment change, new source capture, or website change. Do not execute publisher/build scripts. The current renderer contains interactive insertions; examine them when evaluating sequence and do not confuse Markdown marker placeholders with missing student content. Prior approval claims are not proof that the teaching order works.

## Requested output

Lead with the strongest finding. List prioritized specific problems, then the recommended order and a concise rationale. Include any unresolved decision that genuinely needs Joshua's judgment. End with exactly `VERDICT: APPROVED` if the current V7 ordering is sound enough to keep, or `VERDICT: REVISE` if material sequencing problems remain. This verdict evaluates V7, not an imagined future revision.
