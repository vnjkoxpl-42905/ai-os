---
title: Contrapositive, how Joshua teaches it
type: concept
tags: [lsat-u, conditional-logic, contrapositive, pedagogy]
created: 2026-10-11
updated: 2026-10-11
status: active
subject: Contrapositive
aliases: [contrapositive, logical equivalent]
---

# Contrapositive: how Joshua teaches it

Gathered 2026-10-11 from his own session transcripts (Gemini auto-notes, raw ASR, so quotes are near-verbatim and unchecked against audio). Use this before writing any contrapositive lesson, drill, flashcard or explanation. Voice rules live in [[teaching-voice]] and [[COPY-CORRECTIONS]]; this page holds the substance.

## The core idea, in his words

- **It is the logical equivalent.** "Definitionally, contrapositive all it means is logically equivalent." The two statements are interchangeable and equally valid. Source: `students/asia/sessions/2026-08-25-conditional-logic/transcript.md:240-265`.
- **Same statement, said another way.** When a student said it is "a different way of writing the original," he said yes. `students/charles-moore/transcript-downloads/2026-09-09-charles-moore-notes-by-gemini.md:395-413`. Also `students/zeina-borji/sessions/2026-09-25-conditional-foundations/transcript.md:936`: "they're identical statements."
- **Every conditional has exactly one partner.** His handles: "evil twin," "dance partners," "interchangeable." `students/sandra/sessions/2026-09-28-conditional-logic-foundations/transcript.md:100,246`; `students/_other-sessions/2025-10-30-fiorella-notes-by-gemini.md:262`.
- **Why it is true, in his reasoning.** Sufficient means enough. If the necessary condition didn't happen, the sufficient one couldn't have, because if it had, the outcome would have happened. `students/_other-sessions/2025-10-30-fiorella-notes-by-gemini.md:204`.

## How he says to use it

- **Two moves.** Flip and negate, also "swap and slash." Put the slash through both ideas. `students/dakota/...:507-516`.
- **Read it back in plain English.** Say what the contrapositive means in normal English. Turning it too far into symbols can get in the way. `raw/sources/lsat-curriculum/students/New Folder With Items/Sonja - 2025 10 31 18_43 EDT - Notes by Gemini.md:978-980`.
- **Negation is not opposite.** Rich becomes "not rich," not "poor." Hot becomes "not hot," not "cold." A double negative turns positive.
- **Diagram to train, not to perform.** "We're diagramming so that we don't have to diagram." Drill with the diagram, then say it in your head. `students/ivory-johnson/sessions/2026-09-19-session/transcript.md:207`.
- **Do it up front.** It becomes subconscious with practice.
- **Chains.** Negate from the point you're asked about and negate everything before it, not after.

## What students get wrong

- **Reading right to left.** "We only read left to right." Meeting someone at the train station doesn't mean they took the same transport.
- **Denying the sufficient or affirming the necessary.** Neither gives a conclusion.
- **Half the move.** Swapping without negating (reverse) or negating without swapping (inverse).
- **Bait.** Wrong answers use the reverse or inverse on purpose. The true contrapositive often sits in the choices looking odd.
- **Compound conditions.** For a requirement list, one missing piece is enough. "And" becomes "or" when negated. The megadoc states the rule (`corpus/Curriculum/Conditional Logic/Notes/_megadoc_notes_conditionals.md:62`); authorship of that line is unverified.
- **Negating "more."** "Not more" means "at least as."

## Where it shows up on the LSAT

- **Must be true and inference:** he says the contrapositive is "almost always" what they test, and facts can trigger the rule or its contrapositive.
- **Chains:** head to tail, with the contrapositive as the plot twist.
- **Sufficient assumption:** the correct answer often states the connection in contrapositive form (`corpus/Curriculum/Sufficient Assumption/Notes/_megadoc_notes_sufficient_assumption.md:63`, authorship unverified).
- **Flaw:** called a false reversal or false contrapositive.

## Cautions when writing

- **Do not call it 'the one other thing you know'.** Joshua said so on 2026-10-11, even though some transcripts use that phrase. Stress equivalence and interchangeability instead.
- **Avoid the raffle example** in new material. Current lesson example: elevator moving, doors closed.

- He says "everything else is wrong" or "false" in places. Teach it as **unknown**. The rule plus a fact on the other side settles nothing.
- "Only one logically equivalent statement" is a teaching simplification. Other equivalent rewrites exist.
- He once calls the contrapositive "the inverse" in a session (`students/sandra/...`). In the bootcamp the inverse is the half move (negate only). Use the bootcamp meaning.
- The source HTML's "ignore the conditional" and "all you know" lines overclaim. Do not copy them.

## Wording that failed

Joshua rejected an explanation built on a rule "making a promise," the right side being something the left "depends on," and a left side with "nothing to stand on." It read as sophistry. The version he wants leads with: the contrapositive is the same rule said a different way, logically equivalent, interchangeable, then says plainly what it states. See [[COPY-CORRECTIONS]], 2026-10-11 contrapositive entry.

## The source HTML's method (reviewed 2026-10-11)

`raw/sources/conditional-reasoning-voice-standard/conditional_reasoning_transcription.html`, lines 234-285 and its diagramming section. Order: recap the Must relationship, thought experiment (coffee and walking) with a STOP and a guess box, reveal by reasoning about the unmet necessary burden, name the contrapositive, 'produced organically... waiting to be recognized', a first-person revisit (breathing and air), a four-situations chart, notation with the squiggle, four original and contrapositive pairs, 'flip and negate', and read-it-two-ways with 'don't diagram the contrapositive out of habit'. Joshua asked that our lesson mirror this with fresh examples and a flip card for the solution. Do not copy its overclaims or its examples.

## Where it lives in the product

`ai-os-projects/lsatu-conditional-bootcamp/src/bootcamps/conditionals/components/OpeningCourseContent.tsx`, function `ContrapositiveNote`, lesson id `contrapositive`, titled "Contrapositive".
