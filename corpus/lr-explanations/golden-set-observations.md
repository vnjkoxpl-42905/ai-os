# Observations: LR Standard explanations

Survey date: 2026-09-26. Read-only. Primary corpus: the DB dump in `db/` (PT101 to PT159). The local markdown in `lsatu-wt-parser/Explanations/` (PT139 to PT159) was used to check layout and choice tags, which the dump does not include.

## 1. What the corpus actually is

**Styles.** `lr_explanations.style` has four values: `single` 3,183, `standard` 236, `brief` 236, `another_way` 236. Every question with a `standard` row also has `brief` and `another_way`, and no question has both `standard` and `single`. So "the Standard explanation" is `standard` where it exists and `single` everywhere else. Both have the same shape (Argument breakdown steps, then five choice notes). 352 of 3,771 questions have no explanation at all (`is_explained = false`).

**Where the explicit Standard lives.** 126 of the 236 `standard` rows are PT157 and PT158. The rest are scattered one to nine per test (PT101-110, PT117-133, PT137-144, PT148, PT156).

**Totals per family** (3,419 explained questions; "complete" = full breakdown plus five choice notes; "with prediction" = also has a Goal / Anticipate / Predict step; E/M/H = difficulty 1-2 / 3 / 4-5 among complete):

| Family | Explained | explicit standard | single | Complete | with prediction | E | M | H |
|---|---|---|---|---|---|---|---|---|
| Flaw | 524 | 33 | 491 | 488 | 426 | 162 | 134 | 178 |
| Must Be True / Most Supported | 462 | 33 | 429 | 348 | 326 | 98 | 91 | 145 |
| Necessary Assumption | 352 | 20 | 332 | 325 | 266 | 98 | 90 | 128 |
| Weaken | 335 | 24 | 311 | 295 | 253 | 88 | 70 | 126 |
| Strengthen | 277 | 16 | 261 | 245 | 208 | 104 | 55 | 74 |
| Paradox | 213 | 15 | 198 | 195 | 142 | 77 | 45 | 69 |
| Sufficient Assumption | 193 | 10 | 183 | 180 | 130 | 39 | 44 | 91 |
| Principle-Strengthen (justify) | 181 | 12 | 169 | 168 | 151 | 69 | 37 | 59 |
| Main Conclusion | 144 | 11 | 133 | 99 | 90 | 51 | 22 | 25 |
| Role | 126 | 15 | 111 | 107 | 104 | 25 | 36 | 44 |
| Parallel Flaw | 123 | 7 | 116 | 119 | 116 | 35 | 23 | 55 |
| Agree/Disagree | 119 | 7 | 112 | 112 | 97 | 47 | 26 | 35 |
| Parallel | 100 | 6 | 94 | 97 | 78 | 26 | 31 | 36 |
| Principle-Conform (apply / illustrate) | 99 | 8 | 91 | 85 | 71 | 41 | 14 | 26 |
| Method | 91 | 13 | 78 | 85 | 84 | 37 | 21 | 25 |
| Must Be False | 43 | 2 | 41 | 40 | 39 | 9 | 4 | 25 |
| Evaluate | 28 | 4 | 24 | 27 | 27 | 11 | 6 | 8 |
| Fill-in / Complete | 9 | 0 | 9 | 7 | 7 | 4 | 0 | 3 |

Family comes from the question stem checked against the DB `question_type` label: they agree on 2,961 of 3,419 rows (87%); the rest are resolved by the label (379) or by the bank type where it agrees with the stem (79). I did not trust the bank's `questionType`: in the PT139-159 overlap it disagrees with the file label on 224 of 1,234 questions, and many of those are a default "Most Strongly Supported" on questions that are plainly Flaw, Paradox or Role.

**Data problems found (not fixed, reported only).**
- The local `Explanations/PT140-explanations.md` is a thin, different version: about 100 words per question against about 630 in the DB. All 69 PT140 overlaps differ; every other PT139-159 question matches the DB within 20 words. Anyone reading PT140 from the markdown sees the wrong text.
- Bank alignment: 110 explained DB questions have no matching bank entry at the same PT/section/question, and 27 match a bank entry filed under another number (for example, the local PT148-S4-Q24 to Q26 stimuli sit in the bank under PT149-S4-Q24 to Q26). Features and difficulty for those are missing or borrowed; the inventory column `bank_match` says which.
- Transcription damage recurs in diagrams: arrow diagrams flattened onto one line (PT139-S4-Q8, PT139-S4-Q21), and in PT144-S2-Q22 the negation marks were lost so two diagrams now read backwards.
- Leftover source references: "try this one" pointing at a missing link (PT139-S1-Q5), "Welcome to Test 89" (PT155-S4-Q15).
- The bank carries a "Games-y LR" feature tag (for example PT119-S4-Q24). Worth knowing given the no-Logic-Games rule for student copy.

## 2. Quality by test range

| PTs | Explained | Avg words | Complete | Em-dashes per 1k words | Notes |
|---|---|---|---|---|---|
| 101-122 | 1,158 | 553 | 85% | 0.5 | Full LSAT Lab voice. Many golden picks come from here. |
| 123-138 | 1,025 | 362 | 51% | 0.7 | Noticeably thinner. Most "incomplete" rows have a breakdown but no Goal step (346), and choice notes are often one or two lines. Some notes read like generic summaries (PT126-S4-Q20: "This introduces arbitrators, which are outside the scope"). |
| 139-156 | 1,097 | 588 | 91% | 0.6 | Same voice as 101-122. Consistently strong. |
| 157-159 | 139 | 672 | 89% | 7.1 | PT157/158 are explicit Standard. Breakdowns are in the house voice; choice notes are a different register (below). |

**The PT157/158 explicit-Standard register.** Choice notes run about 100+ words each, open with formulas ("This answer captures...", "This answer identifies the argument's central flaw"), use em-dashes at roughly ten times the rate of everything else, and repeat the same point several ways. More importantly, they contain accuracy slips I did not find in the single-style text at the same rate:
- PT158-S3-Q2: the D note describes a different answer ("can effectively combine knowledge") from the actual choice ("can effectively solve many problems"); A is tagged "No Impact" while its note argues it undermines the argument.
- PT158-S2-Q16: the correct-answer note imports outside history (Plato's family wealth, Philip of Macedon) to justify the answer.
- PT158-S2-Q18: the A note argues against a claim the choice does not make.

That is why no explicit-Standard item made the golden set, and why the house voice rules (no em-dashes) matter for the writing guide.

**Two voices inside the single style.** Most text is one conversational author (voice A: "Hey, author", "Let's look for", FABS, Curious Fact, Given that / How can it be that). A second, more formal author appears in about 15% of questions (voice B: "Beware of answers that...", "If you chose this answer...", "This answer choice..."). Voice B is accurate and structured but lighter on prediction and analogy. Examples: PT146-S2-Q8, PT151-S2-Q1, PT152-S4-Q5, PT154-S1-Q10, PT155-S4-Q1. Both voices can produce a strong explanation; voice A produces most of the best ones.

## 3. What separates strong from loose (the empirical comparison)

I picked ten explanations that were clearly strong and ten that were complete but loose, read all twenty side by side, then measured a few things.

- **Strong (10):** PT139-S4-Q18 Flaw, PT142-S4-Q22 Flaw, PT145-S2-Q19 Paradox, PT154-S1-Q18 NA, PT153-S2-Q13 Weaken, PT146-S2-Q13 Strengthen, PT147-S1-Q17 Evaluate, PT152-S2-Q21 Principle-Conform, PT150-S3-Q15 Agree/Disagree, PT144-S3-Q17 Role.
- **Loose but complete (10), with the failure each shows:** PT127-S2-Q3 Weaken (two wrong answers get one line each: "This supports the argument's explanation"); PT126-S4-Q20 Weaken (generic summary notes, a Goal that restates the task); PT124-S3-Q10 Role (short, and "Haha. This answer is unthinkably weird"); PT151-S2-Q18 Strengthen (117 words total; the 29% trap gets one sentence); PT146-S2-Q8 Flaw (every wrong answer is "The argument never discusses X", correct note is one line); PT142-S4-Q5 Principle (mechanical, no reason why the trap tempts); PT155-S2-Q10 Paradox (fine idea, thin notes); PT158-S3-Q2 Strengthen (long, but misquotes a choice); PT158-S2-Q16 Paradox (long, but brings in outside facts); PT148-S1-Q20 Method (sound analysis, but calls the correct answer "so, so dumb").

Measured averages (strong vs loose):

| Measure | Strong | Loose |
|---|---|---|
| Total words | 773 | 394 |
| Words in the Evaluate step | 169 | 77 |
| Words in the Goal step | 66 | 43 |
| Goal names 3+ content words from the stimulus | 0.9 | 0.5 |
| Avg words per wrong-answer note | 87 | 45 |
| Wrong-answer notes under 20 words (verdict only) | 0.0 per question | 1.1 per question |
| Wrong-answer notes that run an explicit test (negate it, does it weaken, does it trigger the rule, why should we believe it) | 1.4 of 4 | 0.2 of 4 |
| Words in the correct-answer note | 143 | 60 |
| Examples, analogies or worked numbers | 2.0 | 0.5 |
| Stated generalizations ("whenever", "on X questions", "usually") | 1.6 | 0.3 |

What actually separates them, in order of how reliably it predicted my judgment:

1. **The Evaluate step argues with the argument.** Strong ones do real work before the choices: they build the objection ("Given that X, how could we argue not-Y?"), do the arithmetic (25% of $400 vs 13% of $1,000), or set the two populations side by side. Loose ones restate the stimulus and move on.
2. **The Goal names the answer, not the task.** Strong: "look for an answer saying the fish in the leafless trees are exposed to predators that hunt by sight." Loose: "Find the flaw that mistakes a response to danger for a cause", "Identify an answer choice that supports fairness." Strong Goals often give two acceptable shapes (a linking answer or a defender).
3. **Every wrong answer gets a reason tied to this question, and usually a test.** The loose group's signature is the verdict-only note: "This is irrelevant.", "That is unnecessary.", "The argument never discusses profits." Strong notes say what the answer claims, what was needed, and where they diverge, often by running the family's test on it (negate it; would it weaken; is the trigger established; does the conclusion match the rule's right side).
4. **The popular trap gets the most attention.** Strong explanations spend their longest wrong-answer note on the choice that drew 15-30% of students and say why it tempts. Loose ones treat it like every other wrong answer.
5. **The correct-answer note explains the fit, and often generalizes it.** Strong: "Another correct answer performing the same function could have said..." (PT146-S2-Q13); the karaoke/Jenga reason why A → C still works when you predicted A and B → C (PT139-S4-Q21). Loose: "This is the flaw."
6. **Fidelity.** Two loose items are long. Length did not save them: a misquoted answer choice, imported outside facts, or the author disowning the question destroys model value regardless of word count.

What did not separate them: word count by itself (PT152-S4-Q19 is 479 words and strong; PT158-S2-Q16 is 716 and loose), the choice-tag vocabulary, and the presence of jokes (several strong ones joke; it only hurts when the joke is at the question's or the answer's expense).

## 4. Rubric used for the shortlist

Gate (hard requirement): full Argument breakdown and all five choice notes. Every shortlisted candidate passed.

Scored 0 / 1 / 2:

| Criterion | 2 | 1 | 0 |
|---|---|---|---|
| **P** Prediction | Goal names the content or shape of the right answer before the choices (may give two acceptable shapes) | Goal names the task or admits it cannot predict | No prediction |
| **X** Precision | Names the exact gap, flaw or relationship in this argument's words | Uses the right label but stays generic | Label only, or wrong |
| **E** Eliminations | Every wrong answer gets a question-grounded reason; the popular trap gets the most attention | Most do; one or two verdict-only notes | Verdict-only notes |
| **T** Transfer | States the move in a form that works on the next question of this type (the test, the rule, the recurring trap) | Transfer is implicit | None |
| **C** Clarity | Plain, no padding, no pasted repetition | Some padding or pasted notes | Hard to follow |
| **L** Learner value | Teaches what a student needs to understand and repeat the move: why the trap tempts, what to do when stuck, a worked example or analogy, a second correct answer that would also work | Justifies the key well but does not teach the move | Only justifies the key |

Plus a **fidelity flag** (not scored; disqualifying if serious): `slip` factual or typo error, `tone` the author mocks the question or answer, `register` explicit-Standard PT157/158 prose, `transcription` damaged text.

Learner value is the criterion that most often separated a 10 from a 12. Many explanations justify the key correctly (1) but only the best ones also show the student the move they will reuse (2).

## 5. Step structure per family (DB, most common sequences)

Labels normalized (parenthetical indicator words dropped: "Conclusion (therefore)" counts as Conclusion).

- **Flaw (524):** Conclusion > Evidence > Evaluate > Goal (67%); Evidence > Conclusion > Evaluate (9%); with an Intermediate Conclusion step (5%). Evaluate usually names the famous flaw or builds the objection; Goal often gives both the formal and the "fails to consider" phrasing.
- **Must Be True / Most Supported (462):** Statements > Evaluate > Goal (45%); Statements only (16%). Statements is often a diagram. Evaluate scans for conditional, causal, math and pivot wording and names the inference to make.
- **Necessary Assumption (352):** Conclusion > Evidence > Evaluate > Goal (66%). Goal typically offers a linking answer and a defender answer, and says "negate it".
- **Weaken (335) / Strengthen (277):** Conclusion > Evidence > Evaluate > Goal (59% / 55%). Evaluate uses "Given that ... how could we argue that ..." or Curious Fact / Alternate Explanation / Plausibility.
- **Paradox (213):** "Apparent Paradox > Evaluate" (22%, older tests) or "Given that ... > How can it be that / Why is it that ... > Evaluate > Goal" (about 30% combined, often with Evaluate / Goal merged).
- **Sufficient Assumption (193):** Conclusion > Evidence > Evaluate > Goal (53%); Evidence > Conclusion > Evaluate (21%). Goal usually diagrams the missing link as the logic path.
- **Principle-Strengthen (181):** Conclusion > Evidence > Evaluate > Goal (48%). Goal is "If evidence, then conclusion" in general terms.
- **Principle-Conform (99):** mixed. Conclusion > Evidence > Evaluate > Goal (24%) when the principle is in the answers; Principle > Evaluate > Goal (9%) or Principle > Goal (7%) when it is in the stimulus.
- **Main Conclusion (144) / Role (126):** Conclusion > Evidence > Evaluate > Goal (42% / 53%), with an Intermediate Conclusion step in about 8%. Evaluate almost always opens with the reminder that the conclusion usually comes early (first sentence or after a pivot).
- **Parallel (100) / Parallel Flaw (123):** Conclusion > Evidence > Evaluate > Goal (49% / 67%), Evidence first in about 19-35%. Goal is an algebraic recipe (P1, P2, C) or a plain-language template.
- **Agree/Disagree (119):** speaker-named steps. "Speaker's Claims > Speaker's Responses > Goal", often a numbered claim list with "Does [speaker 2] disagree?" per claim.
- **Method (91):** Conclusion > Evidence > Evaluate > Goal (37%) for one speaker; "X's Conclusion > X's Evidence > Y's Response > Evaluate > Goal" for two speakers.
- **Evaluate (28):** Conclusion > Evidence > Evaluate > Goal (75%).

## 6. Recurring phrasing conventions

- **Frames:** "Given that ... how could we (still) argue that ..." (Weaken, Strengthen, NA, Flaw); "Curious Fact ... Author's Explanation ... Alternate Explanation / Plausibility" (any causal argument); "Given that ... How can it be that ..." (Paradox); "If Evidence, then Conclusion" (Principle, SA).
- **Tests in choice notes:** negate it and ask if it weakens (NA); "fails to consider X" means ask whether X weakens, "presumes X" means ask whether X is necessary (Flaw); "argues X by Y: X must match the conclusion and Y the evidence" (Method, Flaw); a rule can only prove its right-hand side (Principle, SA); "can we support the Agree position and the Disagree position?" (Agree/Disagree); "Why should we believe this?" (Role, Main Conclusion).
- **Recurring trap names:** Too Strong (the most common NA and MBT tag), Out of Scope, No Impact, Unclear Impact, No Distinction (Paradox), Deepens Paradox, Wrong Flaw / Not an Objection (Flaw), Bad Conclusion / Evidence / Trigger Match (Principle, Parallel), Premise / Last-Claim Trap / Opposing Position (Main Conclusion), Unsupported Agree/Disagree Position (Agree/Disagree), Fake Opposite / Illegal Negation (NA), Reversal (SA). Tags come from the local markdown; the dump does not include them.
- **Rules stated as rules:** "Most X can only be concluded from a Most X premise"; "some / sometimes / can is almost always wrong on Strengthen, Weaken, Paradox, SA"; "the second speaker almost never denies the first speaker's evidence"; "about 85-90% of Main Conclusion questions put the conclusion in the first sentence or after a pivot"; "on EXCEPT, three of the working answers usually work one way and one works another".
- **Voice habits that should not be copied:** mocking the question or answer ("hot garbage", "so, so dumb", "unthinkably weird", "dumpster fire"), and the PT157/158 em-dash register.

## 7. `Explanations/targeted-questions/`

Three files: a README and two explanations, PT134-S1-Q16 (Flaw, belief vs implication, answer A) and PT158-S4-Q24 (Weaken, food-supply chain, answer D). The README says they were "added for LSAT U use when Joshua needs specific questions available outside a full PrepTest-section explanation file."

They are not LSAT Lab transcriptions. The layout is different and the parser will not read it: an H1 title, a metadata block (type, answer, LSAT U order, bank file), H2 sections for Stimulus, Prompt, Argument breakdown, **Written explanation** (a free prose section the LSAT Lab files do not have), Answer choice explanations with an italic tag, and a closing **Student takeaway**. The prose is written in LSAT U's own voice: no em-dashes, short sentences, jokes built on the stimulus ("the drug sneaks into the food supply wearing a tiny trench coat", "Still a raccoon in the kitchen"), and a one-line takeaway ("Break the link that matters. That's the move.").

Authorship: git attributes them to `vnjkoxpl-42905` (Joshua's account) inside a bulk commit dated 2026-09-05 titled "Update RRC launch page copy", with no co-author line and no other reference in the repo or wiki. The style, the house-voice compliance and the README wording point to an AI assistant (Claude or Codex) drafting them for Joshua. That is an inference; the git history cannot confirm who typed them.

They are useful as a picture of the target voice (especially "Written explanation" and "Student takeaway", which have no LSAT Lab equivalent). They are not in the golden set because they are outside the corpus and use a different structure.

## 8. Caveats

- All scores are one reader's judgment, formed by reading each candidate once. Treat 11 vs 12 as a tie.
- Features and difficulty come from the question bank. 110 explained questions have no bank match, and some shortlisted items have no features in the bank at all (PT143-S1-Q6, PT154-S1-Q10), so the coverage grid undercounts them.
- I read about 125 explanations in full or near-full, weighted toward the highest-scoring candidates in each family and difficulty band. I did not read all 3,000, so a better exemplar for a thin cell may exist.
