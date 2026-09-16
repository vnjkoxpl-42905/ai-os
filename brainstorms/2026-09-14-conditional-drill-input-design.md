# Conditional Drill Input Design: Brainstorm / Discovery Notes
Date: 2026-09-14 · Goal: Decide how the conditional drill should assess diagramming and verbal if/then/because reasoning without making exact speech recognition the gate.
Status: in progress
Context sources: `projects/lsatu/src/pages/ActivityLab.tsx`; `projects/lsatu/ACTIVITIES-DESIGN.md`; `projects/lsatu/data/guided-drills/02_week_5_blue_lr_guided_drills.md`; `projects/lsatu/brainstorms/2026-06-15-guided-drills-upgrade.md`

## Summary / key decisions
- Current authority: the 2026-09-16 handoff supersedes the early on-platform construction direction below. Paper-first, five diagram choices, deterministic grading, and no AI grading are settled. Earlier Q&A remains as history.
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

## 2026-09-16: Drill audit and proposed expansion

Status: proposals for Joshua's review. No application changes or deployment performed. Static audit of checkout `C:/Users/Joshu/AppData/Local/Temp/lsatu-conditional-intro-20260915`, revision `f8971f11`. Live inspection blocked because browser-harness was unavailable and Computer Use returned a native-pipe connection error. Do not describe these findings as live reproduction.

### Fix answer exposure and recording first

- The current answer generator deliberately includes the direct conditional and its contrapositive as credited choices. Both preserve meaning, so two valid answers are not themselves a logic error. They are a task-design problem if the student is told there is one answer. For ordinary five-choice questions, use one credited equivalence class and four genuinely distinct incorrect answers. Teach equivalence in separately signposted questions.
- Audit clarification: the current content explicitly credits both forms, and both choices receive full correctness. This is a deliberate design choice, not proof of faulty grading. A question asking specifically for the contrapositive can distinguish the requested form without falsely teaching that the original rule is invalid.
- Item 48 is a biconditional, but generic distractor verdicts still classify its converse as partial despite the explanation crediting it. Author choices against the whole logical relationship, including both directions where needed; do not reuse one-way distractor rules blindly.
- Item 62 also needs content review. Its explanation claims that no trustworthy match yields no confirmed spring dating, although failure of a sufficient condition does not rule out the outcome. Do not use it as the model for the new linking progression.
- The stage renders the credited answer and contrapositive before submission with reduced opacity. Dimming is not hiding. Reveal feedback only after the student's answer is committed. Reveal choices only after the paper attempt, preserving the settled workflow.
- Preview skips persisted progress and writes. Practice-again and missed-question retries also bypass writes. Keep preview clearly identified as unsaved; record every student practice session, including repeats and incomplete sessions.
- Assigned first runs already write per-answer records to `activity_item_responses`, hydrate progress, and have an outbox fallback. Extend this system rather than replacing it. Its uniqueness key is assignment + student + item order + within-item attempt number. Simply enabling writes for repeat practice would collide with the original run; introduce a distinct run identity.
- Save each submitted answer with a session ID, item/version ID, displayed choice order, selected choice, outcome, attempt number, hint/reveal status and timestamp. Keep initial correctness separate from correctness after feedback. A retry must not erase the first attempt.
- Resume the same item and reveal state after refresh. Show saved, saving, or retry-needed honestly. Use idempotent submission IDs so network retries do not double-count. Keep an unsynced local fallback and retry when online; never present that as cross-device saved history.
- Provide separate actions for Continue unfinished session, Start new practice, Review past sessions, and Retry missed questions. History should retain the exact question and answer presented, even after content revisions.

### Expand what the student must reason through

Preserve four introductory groups and the separate 'Required means right' takeaway. Keep sophistication inside the drill. The audited bank contains 62 items but effectively no actual multi-rule chaining exercises; a sentence containing multiple conditionals is not the same as a linking task.

| Proposed task | What the student does on paper | What the choices assess |
|---|---|---|
| Translate a rule | Identify each condition, direction, and negation | One equivalent diagram among reversal, inverse, polarity and scope errors |
| Contrapose | Reverse direction and negate the complete conditions | Correct negation, including AND/OR changes |
| Compare small wording changes | Diagram 'if', 'only if', 'unless', or 'only' variants | Whether the relationship changes, not just keyword recognition |
| Link two rules | Combine A → B and B → C | A → C, with invalid reverse chains as distractors |
| Turn a rule before linking | Combine A → B and ¬C → ¬B | A → C after contraposing the second rule |
| Decide whether rules connect | Inspect A → B and C → B | Recognize that a shared necessary condition gives no A/C link |
| Apply a stated fact | Use a chain plus A, or plus ¬C | Distinguish deriving a rule from establishing a fact |
| Find the missing bridge | Supply the rule needed to reach a target conclusion | A sufficient connecting premise among direction and relevance traps |
| Repair a student's reasoning | Locate the first invalid inference | Name the actual error and choose the repair |
| Find a counterexample | Make the premises true and proposed conclusion false | Why a reversal or inverse is invalid |
| Handle compound conditions | Preserve parentheses and AND/OR scope | Whether both triggers are needed and what follows from each branch |
| Extract rules from a paragraph | Ignore irrelevant detail and build a linked diagram | Conditional reasoning in longer natural language |

All are proposals. Each can use authored five-choice answers and deterministic local grading. Arbitrary free text, speech or handwriting does not become the graded artifact.

### A long linking item should earn its length

Proposed original stimulus:

> Anyone who mentors a clinic student must have completed ethics training. Only approved volunteers may complete that training. No approved volunteer has an unresolved conflict of interest. The clinic runs evening and weekend sessions. Lena mentors a clinic student.

Let M = mentors a clinic student, E = completed ethics training, A = approved volunteer, C = unresolved conflict. Diagram M → E → A → ¬C, with M(Lena). Therefore ¬C(Lena).

Use separate rounds to ask: which rules connect; what must be true of Lena; what follows if a person has an unresolved conflict; what remains possible if someone does not mentor; which added rule would justify a new conclusion. Do not count repeated questions about an already-explained passage as independent mastery. Follow them with fresh transfer items.

The evening/weekend sentence is irrelevant. Its purpose is to test extraction, not to create a hidden exception. Longer items should vary chain length, rule order, contrapositive steps and compound scope independently before mixing them.

### Feedback should identify the missing move

- After submission, show the student's choice beside the credited diagram, then explain the exact error. For A → B, choosing B → A warrants: 'B is required when A occurs. B can still occur without A.'
- Offer one small repair step before revealing a complete walkthrough. Hints can progress from identifying the required condition to orienting one rule to showing the chain.
- Then give a fresh item using the same reasoning error in a new setting. Improvement on a new problem is more informative than clicking the displayed answer on a retry.
- Fade scaffolds: labelled conditions and highlighted linking terms first; plain prose and unlabelled terms later. Keep help available without making it part of every question.
- Teach with a short worked example before introducing a new operation. Do not surprise-test an untaught move.
- Track translation, direction, negation, compounds, contraposition, linking and inference separately. Use these records to propose the next short practice set. A single overall percentage hides the reason for a mistake.
- Distinguish unseen questions from review. Shuffle answer positions and vary contexts, while grading authored logic rather than generating unchecked prose.

### Recommended implementation order

1. Stop answer leakage, make answer expectations unambiguous, and record repeat practice reliably.
2. Add a dedicated linking progression: two rules, contraposition to connect, three or more rules, then longer paragraphs and compound chains.
3. Add error-specific feedback, targeted repair items, resumable sessions and review history.
4. Add adaptive mixed practice after the underlying answer and history records are trustworthy.

Acceptance checks for implementation: no answer text exposed before commitment; one semantic correct answer where the instructions promise one; original and contrapositive never treated as logically different; each student submission survives refresh; repeated and incomplete sessions remain visible; failed network saves are recoverable without duplicates; preview remains explicitly unsaved; deterministic grading makes no AI call.

## 2026-09-16: Joshua narrows the expansion to conditional practice

This clarification supersedes conflicting proposals above. Preserve multiple choice, paper-first work, and the existing overall design with modest improvements. Do not introduce argument-repair mode or require an on-screen diagram builder. Longer reading passages are not the target; short premise-only paragraphs are acceptable as an optional later conditional exercise, as Joshua explicitly suggested in the same clarification.

Add two modes: supply a missing conditional that makes a target conclusion follow, and identify what Must Be True from multiple conditionals. Begin with variables, then use words and phrases. Progress through direct chains, contraposition, negative links, AND requirements and OR alternatives. Preserve all four current introductory groups and the separate “Required means right” takeaway; also vary the rules, universals, guarantees and requirements language shown in Joshua's screenshots.

Original companion draft: [20 conditional linking questions](2026-09-16-conditional-linking-question-bank.md), comprising 10 missing-link items and 10 Must Be True items, each with five choices and explanations. The bank is authored content for review, not official LSAT material or a deployed app update. Its final symbolic formulations were checked with exhaustive Boolean valuations for single-answer correctness and consistent premises. Save-every-student-run remains part of the requested improvement.

Corpus grounding: Conditional Logic notes distinguish chaining rules from triggering them with facts. Sufficient Assumption notes identify missing beginning, middle and end bridges and connect supplying a premise to deriving a Must Be True conclusion. The 2026-09-15 COPY-CORRECTIONS entry preserves the current four-group map and paper-first wording; older source taxonomies remain historical rather than replacing it.

## 2026-09-16: Approved notation and one entry with four worlds

Joshua's latest clarification governs the next implementation:

- Use a diagonal slash through a negated letter, matching the supplied LSAT screenshots. Keep the directional arrow. Write “and” and “or” as words, without formal operator glyphs or logical grouping parentheses/brackets in student-facing diagrams. Use line breaks, spacing and branches to preserve compound scope. In Markdown, A̸ represents the slash-through treatment; the app should draw the diagonal stroke and expose “not A” to assistive technology.
- Navigation: Activity Center → Conditional Reasoning → choose a world. Use four choices: **General Conditionals**, **Linking**, **Missing Link**, and **Must Be True**. The user allowed three or four worlds; four keeps connecting rules distinct from deriving facts and compound consequences.
- General Conditionals preserves the current Conditional Rephrase work. This is an additive expansion. Do not replace its questions, remove existing functionality, overwrite saved work, or invalidate assignments and links. Retain its stable activity identity even if its display label changes.
- Linking practices joining rules, including contraposition needed to make a connection. Missing Link supplies a sufficient connecting premise. Must Be True derives what follows from rules and facts. All keep the paper-first and five-choice interaction.
- Each world has separate resumable runs and history. Opening the selector does not start a new run or erase the active one. Existing assignments retain a direct route to the assigned General Conditionals work, with an explicit Continue action where needed.
- Preserve all four indicator groups across language-based practice. New worlds build on the current framework rather than substituting another taxonomy.

The companion [question bank](2026-09-16-conditional-linking-question-bank.md) has been reformatted throughout, with all 20 question identities and answer keys preserved. It now specifies the four-world entry. A separate Linking set and app implementation are still pending; these edits do not claim that the new selector is live.

## 2026-09-16: All twelve photographed Missing Link exercises are required

Joshua supplied six photos of “Missing Links in Conditional Chains as Sufficient Assumptions” and asked to include every question. This concretely establishes the Missing Link format: one or two premises, an explicit conditional conclusion, and a missing sufficient assumption. Preserve five-choice selection and the slash notation already settled.

The photos contain four single-premise and eight two-premise exercises, plus worked explanations. All twelve prompts have been added to the companion bank as PHOTO-ML01 through PHOTO-ML12, with five-choice adaptations, newly written explanations, direct/contrapositive answer forms, and checked distractor counterexamples. The prior twenty authored items remain. The inventory is now 22 Missing Link entries and 10 Must Be True entries. Some entries intentionally share equivalent structures; entry count is not independent skill coverage.

Do not cap required content at ten items. Ten questions per sitting was an assistant recommendation, not a user decision, and may not exclude any of the twelve supplied exercises. Difficulty navigation and session length remain unanswered interview choices. The photos settle Missing Link content; they do not implicitly answer those separate questions.

Both a bridge and its contrapositive may be shown in post-answer explanation, but only one may appear among five choices when the task promises one correct answer. The pairs PHOTO-ML05/07, PHOTO-ML06/08 and PHOTO-ML09/10 intentionally practice contraposed conclusions and equivalent bridges. Keep them, without counting an immediate paired repeat as independent mastery.

Source images remain unmodified under `C:/Users/Joshu/.codex/codex-remote-attachments/01a0a8d7-9b78-7b61-8735-7d6fd1f13ab4/EDF24AF0-6494-4A6B-9C0E-AE726382FF49/`. This update is to authored content and design notes; app implementation remains pending.
