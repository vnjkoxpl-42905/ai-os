# Post-session note redesign: Brainstorm / Discovery Notes
Date: 2026-10-25 · Goal: define what the post-session note extracts, how it is structured, its voice, and the process, then rewrite the post-session-recap skill.
Status: design decisions recorded; skill rewritten on the Session Manual after Joshua confirmed "These match." Workflow reconciled against the full saved chat on 2026-10-25. Sample-note preparation is complete; whole-set visual verification and approved student delivery remain separate unfinished steps.
Context sources: .claude/skills/post-session-recap/SKILL.md, references/lesson-quality-bar.md, references/recap-calibration.md, brainstorms/2026-09-30-yahunatan-post-session-recap/

## Summary / key decisions
- ~~Two layers: a short session note, plus an optional linked deeper lesson.~~ Superseded R4: every session gets three notes: session recap, drill primer, method reference.
- Recap: teach the relevant concepts and traps without blaming the student; include Joshua's explanation, specific credit, two or three practice checks, homework and next steps. Primer: the actual drill's rule, trap and one habit. Method reference: reusable complete method, lightly revised if it exists.
- Include Joshua's explanation. Round 1 explicitly confirmed it; the earlier inference from an unselected option does not override that answer.
- Format scaling was superseded by three note types after every session. Do not re-ask the old tiers question.
- Include Joshua's explanation: conceptual, with session particulars where needed. (confirmed R1)
- Opening: generic concept first, then the session specifics. (confirmed R1)
- Length: ~5-minute read, engaging, 2-3 practice checks, a note they can return to. (confirmed R2)
- Calibration method: interview first (this file).

## Q&A log
### Round 0 (AskUserQuestion, 2026-10-25)
#### Purpose
- Captured: "Both, two layers."
#### Required contents
- Captured: Their exact mistake; Practice checks; Homework + next steps.
#### Format scaling
- Captured: "help explain these options, I'm not clear with the difference." -> re-asked in Round 1.
#### Calibration
- Captured: Interview me first.

### Round 1 (2026-10-25)
#### Q2 - Include Joshua's explanation?
- Recommended: include, tied to the mistake, his transcript wording where good.
- Captured: Yes. "Should be conceptual and using particulars as well if necessary." Explanation is conceptual; session specifics are used where they help.
#### Q3 - Open on session or concept?
- Recommended: open on the session mistake.
- Captured: "Yes, but have it start with generic concept." Opening = the generic concept first, then the student's session particulars. (Overrides recommendation; consistent with current skill's concept-first opening.)
- Tentative (Claude reading, confirm): concept should reach the student's actual mistake quickly, not by section 5 as in Yahunatan V3.
#### Q1, Q4, Q5, Q6
- Unanswered; re-asked in Round 2.

### Round 2 (2026-10-25)
#### Q5 - Length
- Recommended: ~3 min, 300-500 words.
- Captured: "maybe 5 minutes but should be engaging, and 2 to 3 practice checks, and it should be a note they can return to." So: ~5-minute read, engaging, 2-3 practice checks, built as a reference the student revisits later (not a one-time recap).
#### Q1, Q4, Q6, Q7
- Unanswered; re-asked.

### Round 3 (2026-10-25)
#### Q4 - Address
- Captured: (a) Directly to the student ("you"), in Joshua's voice.
#### Q6 - Extra extraction
- Captured: "my database on there." Interpreted (tentative, confirm): pull context from the LSAT U database / student's page, not only the transcript.
#### Q7 - Reaching the mistake
- Captured: "It shouldn't say 'here's your mistake.' It should be just explaining what not to do, in a way." -> Supersedes the "In our session, this is where it slipped" framing. The note teaches the trap as what not to do, without calling out the student's error directly.
- Captured instruction: review the notes Joshua already posted on students' pages (LSAT U) as reference for what good looks like.
#### Q1, Q8
- Unanswered.

### Research: notes already posted on LSAT U (pulled 2026-10-25, read-only, classroom_items type=note)
- 13 markdown notes + several HTML lessons. Session-specific ones: Fernande "What we did on Thursday" (2026-08-27 session); Lexi "How to work: ..." drill primers (2026-08-05); Parallel Reasoning method notes (Steven, Sofia, Celia); Steven week schedule.
- Fernande note shape: "In order" (one bold-led paragraph per idea taught, concept first then the session question as a worked case) -> "What changed" (growth from start to end of session, framed positively: "You named the real difficulty yourself") -> "Carry forward" (5 action bullets). Second person, plain, short. No quizzes. ~650 words.
- Observation (Claude): this note never says "your mistake was"; it names the trap as a general move and credits what the student did right. Matches Q7.
- Lexi primers: ~120 words, the rule from the session + two-step routine + one reminder. Tight.
- Parallel Reasoning: long reference doc, numbered sections, feature/indicator tables, "keep this open while drilling."
- Tentative: Fernande note is the closest existing model; needs confirmation.

### Round 4 (2026-10-25)
- Showed brainstorms/2026-10-25-posted-note-types.html (recap / drill primer / method reference).
- Captured: "yes I want the three part for every note." Ambiguous: (a) every session produces all three note types, or (b) every note uses the Fernande three-section shape. -> clarifying.

- Clarified: **All three note types after every session**: session recap + drill primer + method reference. (confirmed; supersedes "optional deeper lesson" in Round 0 and makes Q1 tiers moot)

### Round 5 (2026-10-25)
- Joshua: "check how we can [do it] comprehensively for each" (interpreted as: compare the three types row by row). Q10-Q15 unanswered.
- Claude added a "Side by side" tab to brainstorms/2026-10-25-posted-note-types.html: job, when read, length, structure, opening, how the trap is taught, session particulars, sources, one-per, gaps. Proposed additions marked; nothing decided.

### Round 6 (2026-10-25)
- Q11: "Just revise if it already exists, you don't have to make a new one, only slight adjustments." Method reference: one per question type; revise lightly if it exists.
- Q12: Yes. No drill assigned -> Claude picks a matching set, Joshua approves before assignment.
- Q13: "It should be highly visually interactive and easy to read." Applies to the notes (all three, tentative: confirm scope).
- Q14: Not needed. Transcript is the source; no LSAT U drill data pull. (Supersedes the tentative Q6 "database" reading.)
- Q15: "Look at my other notes I've posted on the students' pages and reference and follow in line with those." -> Ending follows the posted notes: Carry forward bullets, with the "worth carrying" line inside What changed. No separate invented closer.
- Q10: unanswered.

### Round 7 (2026-10-25)
- Joshua: "let's generate for Amanda, then Yahunathan's most recent session." First real test of the design.
- New requirement (Joshua, mid-turn): "pay attention in the note if I discussed assigning something or a certain task that needs to be considered: what we're going to assign, her homework, notes or drills." -> Every recap's Carry forward lists every assignment and promise from the transcript; the private section tables each item with who/status, flagging ones Joshua still has to pick.
- Q10 and Q13 still unanswered; drafts used the recommendations (checks in the recap; recap interactive, primer and reference clean visual pages) and say so.
- Drafts: brainstorms/2026-10-25-amanda-post-session/ (recap, Unless primer, Parallel Reasoning lightly revised) and brainstorms/2026-10-25-yahunatan-post-session/ (recap, Negation Station primer, new Necessary Assumption reference). Primary records: students/amanda/recaps/2026-10-21-recap.md, students/yahunatan-zetvy/recaps/2026-10-20-recap.md. Nothing posted.

### Round 8 (2026-10-25): drafts rejected
- Joshua on the Yahunathan recap: "what the heck is this, terrible. I want you to look at my other notes I have made, you can find it, check all of my students the past 6 months, you can see what I've used ... the stuff you just made was terrible, it's the wrong look. Look at my inventory, we want to build an inventory and reuse it for future students and notes." Pointed at http://127.0.0.1:5200 (LSAT U redesign preview: cream background, editorial serif, mono small-caps eyebrows).
- Claude's miss: invented a new visual system (navy panels, Inter, generic cards) instead of reusing his posted notes. Only the 13 markdown notes had been read; the HTML notes (Reading Flaw Answer Choices "Session Manual", Conditional Cheat Sheet / Breakdown, Famous Flaws, Causation) were never opened.
- Decision: build a reusable inventory of his real notes (brainstorms/2026-10-25-note-inventory/INVENTORY.md) and rebuild drafts from its components. Both Amanda and Yahunathan drafts are void.

### Round 9 (2026-10-25)
- Joshua: "Use Reading Flaw Answer Choices (the Session Manual) as the model look and structure. Rebuild Amanda and Yahunathan from it." (confirmed)
- Rebuilt all six notes with the model's own CSS (`brainstorms/2026-10-25-note-inventory/session-manual.css`) and builder (`build_session_manual.py`). Correction logged in post-session-recap `references/recap-calibration.md`.

## Current decisions and remaining work, reconciled 2026-10-25

This section supersedes the earlier open-flags list. The dated Q&A above remains historical evidence.

- Three note types, concept-first teaching, direct voice, about five minutes for the recap, no direct blame, and every assignment/promise captured are settled. No repeat design interview is needed.
- Joshua explicitly requested visually interactive, readable notes. The later "These match" accepted the Session Manual examples and his next instruction requested the skill rewrite. The accepted examples place practice checks in the recap and use static primers/references; that is the working sample, not an explicit universal ban on interaction in those other note types.
- The model is Reading Flaw Answer Choices (Session Manual). Use its look and suitable structure/components from the inventory, not an invented theme or an artificial taxonomy for every session.
- Transcript supplies session teaching; posted notes/inventory supply the model and reusable references; corpus grounds the full reference. A broad student-performance data pull is unnecessary. Narrow operational reads still verify assignment and delivery status.
- Endings follow the posted-note examples and the week's work. The old separate invented closer question is superseded.
- Record every commitment privately with owner, timestamp and certainty. Keep tentative offers tentative. Put student work and relevant promises in the visible recap; account fixes and teacher-only delivery work remain private unless relevant to the student.
- Choose a concrete matching drill/set proposal for Joshua to approve rather than repeatedly asking him to supply names. Complete note writing, sync and checks while those choices are pending.
- Both recap Markdown records now match rebuilt HTML, with earlier text retained privately. Six publisher dry-runs passed. This is preparation evidence, not posting or student visibility evidence. See the dated preparation readbacks in the student recap records.
- Remaining sample delivery work: whole-set rendered desktop/phone verification; final homework choices/live validation; explicit posting approval; then post or update the six documents without duplicates and read back/log the result. Primers/references are not claimed visually verified. No notes or homework have been posted by this continuation.

## Grill-me continuation, 2026-10-25

Status: in progress. Joshua explicitly invoked grill-me to stress-test the post-session note process. Resume the existing capture; do not treat the prior assistant's workflow reconciliation as new user-confirmed answers. No further skill changes, note edits, assignments or posting during the interview until shared understanding is confirmed.

### Design tree

- Settled: three distinct note purposes; conceptual opening; direct voice; no blame; approximately five-minute recap; two or three practice checks; Session Manual model and inventory; slight revision of existing method references; full commitment capture; draft before approved delivery.
- Round 10 confirmed: focus the recap on the main lesson and briefly cover other ideas; ask students to explain practice answers before checking; use existing notes for the full method reference; include something to try in all three notes. Current frontier: whether explanations require typing, and whether notes are graded or have required completion.
- Dependent decisions: exact teaching outline, practice format and interactions for the sample notes follow the answers. Operational homework choices and delivery approval remain separate; they do not block this interview.

### Round 10

#### Q16 - Breadth versus depth in a multi-topic recap
- Asked: When a session covers several ideas, should the recap teach one central reasoning skill deeply and treat the others as brief connected reminders?
- Recommended: One central skill, with at most two supporting ideas. Preserve all assignments separately even when the related teaching is brief. Keep broader method detail in the method reference.
- Captured: Awaiting Joshua's answer.
- Flags: Depth/coverage choice -> Joshua.

#### Q17 - What a practice check requires
- Asked: Should the two or three checks require the student to answer and explain why before revealing the answer, rather than only recognizing a label?
- Recommended: Require an answer plus a brief reason. Include a fresh application, a tempting invalid inference and a transfer example; reveal the reasoning without automated grading by default.
- Captured: Awaiting Joshua's answer.
- Flags: Practice-check expectation -> Joshua.

#### Q18 - Scope of a new method reference
- Asked: If the session teaches only part of a question type and no reference exists, should the new reference cover the full method using Joshua's existing curriculum, with session-specific teaching grounded in the transcript?
- Recommended: Yes. Use Joshua's corpus for the full reference; flag missing or conflicting instruction instead of silently filling it with a new method. Keep the recap focused on the actual session.
- Captured: Awaiting Joshua's answer.
- Flags: Full-reference source scope -> Joshua.

#### Q19 - Interaction by note purpose
- Asked: Should the recap use the two or three reasoning checks, the primer stay short with one quick try-it example, and the method reference use worked examples and optional reveals where useful?
- Recommended: Yes, all in the approved Session Manual style. Each interaction has a teaching purpose; no extra controls solely for visual activity.
- Captured: Awaiting Joshua's answer.
- Flags: Interaction expectation across the three note types -> Joshua.

## Open flags for the resumed interview

- Q16 through Q19 answered yes to the simplified questions; see Round 10 answer checkpoint below. Extra details in earlier recommendations remain unconfirmed unless repeated in the accepted wording.
- After answers: checkpoint each answer, update any superseded recommendation, read back the saved entries, then recompute the next frontier.


### Round 10 answer checkpoint

Joshua answered: "yes to all save those answers and keep going with the next questions." This accepts the simplified questions immediately preceding his answer. The earlier fuller recommendations above remain historical; do not silently treat their extra detail as approved.

#### Q16 - Recap focus: confirmed
- Asked: "Should the recap focus on the main lesson and briefly cover the other ideas?"
- Recommended: Yes. Still include every homework task.
- Captured: Yes. Teach the main lesson in depth; cover other ideas briefly; preserve every homework task.
- Supersedes: awaiting-answer status above. The earlier proposed maximum of two supporting ideas was not part of the simplified question and is not a confirmed limit.
- Flags: None for this decision.

#### Q17 - Explain before checking: confirmed
- Asked: "Should students explain why their practice answer is right before checking it?"
- Recommended: Yes.
- Captured: Yes. Students explain why before checking the answer.
- Supersedes: awaiting-answer status above. Exact exercise mix, mandatory typing and automatic grading were not confirmed by this answer.
- Flags: Response mode and grading are the next frontier -> Joshua.

#### Q18 - Full method reference: confirmed
- Asked: "Should the method reference teach the full method from your existing notes, even if you covered only part in the session?"
- Recommended: Yes.
- Captured: Yes. Use Joshua's existing teaching notes for the full reference even when the session covers only part.
- Supersedes: awaiting-answer status above. Do not invent missing source teaching.
- Flags: None for this decision.

#### Q19 - Something to try in all three notes: confirmed
- Asked: "Should all three notes include something to try?"
- Recommended: Practice checks in the recap; one quick example in the drill primer; examples with answers to reveal in the reference.
- Captured: Yes to that structure for all three notes.
- Supersedes: the earlier static primer/reference sample as a default for future implementations. Earlier sample files are not yet updated to this new decision.
- Flags: Implementation follows shared-understanding confirmation, not this answer alone.

### Round 11 - Questions prepared, answers pending

#### Q20 - How the student explains an answer
- Asked: Can students think or say their explanation before revealing the answer, without having to type it?
- Recommended: Yes. Let them explain aloud or think it through; typing is optional.
- Captured: Awaiting answer.
- Flags: Required response mode -> Joshua.

#### Q21 - Scores and required completion
- Asked: Should these notes stay ungraded, with no score and no requirement to finish every activity?
- Recommended: Yes. Notes support review; assigned drills carry the formal practice requirements.
- Captured: Awaiting answer.
- Flags: Grading and required completion -> Joshua.


### Round 11 correction checkpoint

- User correction: "this a post session recap note"; "its not about score"; asks for a plain explanation of what the assistant means.
- Q20 response mode: not answered. Do not infer a choice about typing, speaking or silent explanation.
- Q21 scores/required completion: rejected as the wrong focus. The user is developing a post-session recap note, not a scored assessment. Do not record agreement to the assistant's separate proposal about optional completion.
- Assistant error: introduced assessment and completion-policy questions when the user needed a concrete explanation of the small practice examples already approved. Remove those questions from the current interview frontier.
- Plain explanation supplied: a short example inside the note asks what follows from a taught rule; the student thinks through an answer and reveals the teacher's explanation. This illustrates the existing approved practice-check purpose, not a new approved response-mode policy.
- Resume point: explain the three-note workflow with a concrete recap example. Do not add another round of abstract interaction or scoring questions before the user understands and wants to continue.


### Concrete-review checkpoint

- Joshua confirmed the plain explanation of the post-session recap: "Yes thats what I mean."
- Requested next action: show Amanda's actual Session Manual recap, review the note and finish the process.
- Resume point: review `brainstorms/2026-10-25-amanda-post-session/recap.html`; do not continue the abstract interview or infer posting approval.
- Actual file exists (17,384 bytes). Requested opening in Codex; tool returned queued, not proof the preview is already visible.
