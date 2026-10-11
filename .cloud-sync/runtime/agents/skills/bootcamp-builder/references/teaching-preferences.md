# Bootcamp teaching preferences

Captured 2026-10-11 from Joshua's conditional-bootcamp conversation. These are requirements for future builds where applicable, not proof that any implementation has passed acceptance.

## General standards confirmed by repeated corrections

- Compare the topic against internal corpus sources before drafting. Preserve source provenance and distinguish a source claim from Joshua's decision. Ingest new clips through the ingest skill before relying on them. Never infer a video transcript from its title.
- Explain the concept in plain language, then develop it through a concrete familiar example. Introduce notation after meaning. A short definition alone is not a lesson. Avoid recursive definitions and tongue twisters.
- Break explanations into readable sections with clear visual hierarchy, larger text, generous spacing, and short paragraphs. Inspect the actual rendered page, including the docked browser width and mobile, rather than treating JSX inspection as visual approval.
- Bring meaningful interaction early, after enough teaching to attempt it. Feedback explains the reasoning and distinguishes given facts from conclusions of a rule. Do not merely cycle reveal buttons and call that practice.
- Use color, emphasis, and motion to direct attention to the entire relevant idea. Preserve complete conditions, restrictions, timing, modality, and the difference between a rule and a fact.
- Preserve existing teaching media while revising. Check that videos still exist and play in their intended lesson. New media must earn its place in the teaching flow.
- Review content against the corpus, review the rendered UI, and use independent Claude Code review when requested. Record the actual model from the run, review artifact, findings, disposition, and limitations. Code/screenshot review is not live browser testing. Tests, local build, deployment, and signed-in acceptance are separate claims.

## Necessary-condition lesson: explicitly approved wording

Joshua supplied and approved this copy on 2026-10-11:

> **A necessary condition is a requirement. It has to be met, but meeting it might not be enough.**
> For example, you have to be a student to be enrolled in law school. That makes being a student **necessary for law-school enrollment**.
> But being a student doesn’t mean you’re enrolled in law school. You could be studying history instead.
> **Being a student is required. It doesn’t establish enrollment on its own.**

Keep “might not”: a condition may be both necessary and sufficient. Do not replace this with “something another condition can’t be true without.”

Explicit page corrections:
- Emphasize the complete consequent, “then you are a student,” and identify “you are a student” as the condition. Do not teach isolated “then” as a standalone necessary-condition indicator.
- Law student / history student / not a student should be vertical case tabs. Keep keyboard navigation, visible selected state, and mobile stacking. This is a decision for this case comparison, not a mandate for every interaction.
- Remove “Replay emphasis”; use a gentle continuous pulse for this page, with a static reduced-motion equivalent. This does not authorize constant pulsing on every page.
- Make clear which facts are given and which follow. If a history case says not enrolled, make it explicitly given rather than inferring it from studying history.

Content preservation checks for the conditional sequence:
- Necessary examples retain only, only if, only when, only where, always, requires, must; explain their meaning in the complete sentence and preserve modality/scope. This is the existing lesson coverage, not a context-free replacement dictionary.
- Sufficient Group 1 stays on-page: if; when/whenever; any/anytime; all; every/every time; in order to; people who; each.
- Keep the reference-letter qualifiers, including current and accepted for review. A distractor should reveal a reasoning error, not reward guessing.

## Must arrow: correction and open work

- Confirmed title: **Must arrow**, not “Read the must arrow.”
- Teach the direction explicitly with a familiar relationship: in this convention sufficient on the left, necessary on the right, arrow pointing right. The left condition guarantees the right **if the left condition is true**. The arrow alone asserts neither condition as a fact, neither causation nor chronological order, and no reverse inference.
- The lead “A must arrow shows what has to be true if another condition is true” was rejected as too abstract on 2026-10-11. Do not preserve it as approved wording. Joshua wants the direction shown and explained directly.
- Current provisional implementation: “The must arrow points from left to right. If the left side is true, the right side must be true.” The new LSAT Lab clip (jeDnykOrswY) supports certainty at 0:31 and left requiring right at 8:19, per the source review in this session. This wording is not yet user-approved.
- Source comparison completed; final wording remains provisional pending Joshua’s review. Earlier assistant summaries saying tests passed or an opening was updated are implementation reports, not user approval.
- Source pointers, relative to the vault resolved through its AGENTS.md: `wiki/sources/lsat-lab-conditional-logic-clip.md` and `corpus/Curriculum/Conditional Logic/Notes/_megadoc_reference_conditionals.md#the-must-arrow-shows-a-direction-of-guarantee`.

## Continue the same record

For each new correction, add a dated entry here with topic/page scope, exact wording when approved, status, evidence, and a concrete acceptance check. Keep rejected wording visible only as a regression warning. Do not turn ambiguous dictation into a named person or a universal rule. Reconcile conflicts with Joshua's newest explicit direction. At completion, report what was verified and what remains provisional. Reuse the existing bootcamp-builder skill as the master workflow.
