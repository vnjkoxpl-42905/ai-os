# Conditional Drill Input Design: Brainstorm / Discovery Notes
Date: 2026-09-14 · Goal: Decide how the conditional drill should assess diagramming and verbal if/then/because reasoning without making exact speech recognition the gate.
Status: in progress
Context sources: `projects/lsatu/src/pages/ActivityLab.tsx`; `projects/lsatu/ACTIVITIES-DESIGN.md`; `projects/lsatu/data/guided-drills/02_week_5_blue_lr_guided_drills.md`; `projects/lsatu/brainstorms/2026-06-15-guided-drills-upgrade.md`

## Summary / key decisions
- The activity's desired target is semantic equivalence, but Joshua does not want AI to judge it.
- The activity should remain entirely on-platform rather than requiring paper as the graded interface.
- Current implementation is not truly meaning-based: `ActivityItemView` gives the conditional world a single free-text response, and `judgeConditionalResponse` tries to infer equivalence through a strict `If X, then Y` parser plus content-word overlap, polarity checks, and a few hard-coded fault rules.
- The current content explicitly says wording is free, but the current parser rejects ordinary equivalent forms unless they fit its narrow grammar. That is the central mismatch.
- Strong design direction (recommendation, not yet confirmed): stop asking the browser to understand arbitrary language. Ask the student to construct the logical form from authored selectable components, then optionally let them type/say the natural-language version as ungraded rehearsal.

## Q&A log
### Round 1
#### Q1 - What counts as correct?
- Asked: Should the drill grade exact wording or preserved logical relationship?
- Recommended: Grade meaning, not wording; exact phrasing should never be the pass/fail gate.
- Captured: Joshua agreed that meaning is the right target, while raising the unresolved implementation question of how a non-AI system can detect meaning reliably.
- Tentative: Semantic equivalence should be represented by structured fields rather than inferred from arbitrary text.
- Flags: Define the structured answer model -> Joshua and implementation design.

#### Q2 - What should the student submit?
- Asked: What should be the primary graded artifact: paper plus on-screen choice, direct on-screen construction, or free-form text/speech?
- Recommended: Keep the work on-platform and use deterministic structured interaction; do not make free-form speech the authoritative answer.
- Captured: Joshua wants this solved inside the existing Conditional Rephrase activity on the platform. He does not want to depend on AI capabilities.
- Tentative: Replace or supplement the current textarea with authored controls that encode the conditional's parts and direction.
- Flags: Choose the exact interaction pattern -> next round.

### Review evidence before Round 2
- `conditional-rephrase.json` defines 62 authored items with credited if-then and contrapositive strings. It already identifies the instructional dimensions: trigger/required side, direction, negation, compound `and/or`, biconditionals, and the two classic errors.
- `routing.ts` parses only authored `If X, then Y` strings. Its local judge uses light normalization and content-token overlap. This can catch some paraphrases but cannot establish arbitrary synonymy or scope reliably; it will also reject equivalent forms that do not match the grammar.
- `ItemPrompt.tsx` currently routes `free-text` to a textarea and treats `mcq`/`variation` as not implemented. The activity is therefore structurally capable of a local judge but not yet of a structured answer UI.

### User clarification after Round 2 prompt
- The attached screenshot confirms the target is the existing Conditional Rephrase activity, not a new paper workflow: one free-text answer area, 62 questions, two tries per question, and the credited answer shown after the tries.
- The redesign should preserve this activity's role and overall flow while replacing the untrustworthy free-form grading step with a deterministic interaction.

### User pivot after Round 3 prompt
- Joshua's preferred immediate solution is paper-first self-production: the student solves the conditional on paper, then uses the platform to check it.
- The platform should not attempt to detect or interpret the student's handwriting, typing, or speech.
- Proposed flow: show a question; instruct the student to write the answer first; reveal a finite set of candidate answer lines; have the student click the line that corresponds to what they wrote; grade that selection deterministically.
- This intentionally accepts an honor-system component in exchange for a simple, fair, no-AI implementation.
- Tentative: the candidate lines should include the credited direct conditional and/or contrapositive plus authored distractors representing reversal, inverse/illegal negation, and other relevant traps.

## Q&A log

## Open flags
- Decide whether the platform checks the direct conditional, the contrapositive, or both -> next round.
- Decide whether answer choices are full natural-language lines, diagrams, or both -> next round.
- Decide whether the student must attest that they wrote their answer before revealing choices -> next round.
