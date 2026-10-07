# Golden-set shortlist: LR Standard explanations

Survey date: 2026-09-26. Corpus: the LSAT U database dump in `db/` (PT101 to PT159, 3,419 explained LR questions), joined to `public/data/PT*-LR.json` for type, features, reasoning and difficulty. "Standard" means the `standard` style where a question has one (236 questions, almost all PT156-158 plus a few elsewhere) and otherwise the `single` style (3,183), which is the same shape: Argument breakdown plus five choice notes. Every candidate below was read, not scored on length. Rubric and the strong-vs-loose comparison it came from are in `observations.md`.

Scores are 0 to 2 on six criteria: **P** prediction before choices, **X** precise gap/flaw named, **E** question-grounded eliminations, **T** transferable move, **C** clear and unpadded, **L** learner value (teaches what a student needs to understand and repeat the move, beyond justifying the key). Max 12. Completeness (full breakdown and all five notes) is a gate, not a score: every candidate passed it. Because only strong explanations were shortlisted, scores cluster at 11-12; the weakness line is what separates them. **Fid** flags a fidelity problem: `slip` (factual or typo error in the text), `tone` (author disparages the question or answer), `register` (explicit-Standard PT157/158 prose: em-dash heavy, formulaic), `transcription` (diagram or text damaged).

Difficulty bands: E = 1-2, M = 3, H = 4-5. The gap questions skew easy (480 of 772 are difficulty 1-2), so the golden set does too.

## Recommended golden set (50)

| # | ID | Family | Type (DB) | Diff | Features | Score | Fid |
|---|---|---|---|---|---|---|---|
| 1 | PT107-S3-Q5 | MBT/Most Supported | Most Supported | 1 | Conditional Diagramming; Causal Chains; Science | 12 |  |
| 2 | PT145-S2-Q23 | MBT/Most Supported | Must be True | 2 | Sufficient vs. Necessary Flaw; Contrapositive Logic; Quantifiers | 12 | slip |
| 3 | PT104-S1-Q3 | MBT/Most Supported | Most Supported | 3 | Explain Curious Fact; Important Pivot; Alternatives; Causal Difference-Maker; Rebuttals | 12 |  |
| 4 | PT142-S4-Q7 | MBT/Most Supported | Most Supported | 3 | Logical Completion | 12 |  |
| 5 | PT143-S1-Q13 | MBT/Most Supported | Most Supported | 5 | Important Pivot | 12 |  |
| 6 | PT151-S2-Q3 | Flaw | Flaw | 1 | Abstract Answers; Argue the Anti-Conclusion; Causal Chains; Focused on Evidence; Plans / Recommendations; Predictions | 10 |  |
| 7 | PT102-S2-Q9 | Flaw | Flaw | 2 | Explain Curious Fact; Alternatives; Anti-Causal; Argue the Anti-Conclusion | 12 |  |
| 8 | PT139-S4-Q18 | Flaw | Flaw | 3 | Relative vs. Absolute; Math-y Stuff; Net Effect; Plans / Recommendations | 11 |  |
| 9 | PT143-S3-Q18 | Flaw | Flaw | 3 | Sufficient vs. Necessary Flaw; Contrapositive Logic; Plans / Recommendations; Untriggered Conditional | 12 |  |
| 10 | PT118-S3-Q13 | Flaw | Flaw | 4 | Famous Flaws; Belief / Knowledge / Intent; Abstract Answers; Sampling | 12 |  |
| 11 | PT142-S4-Q22 | Flaw | Flaw | 4 | Sufficient vs. Necessary Flaw; Famous Flaws | 12 |  |
| 12 | PT111-S4-Q4 | Paradox | Paradox | 1 | Math-y Stuff | 12 |  |
| 13 | PT151-S2-Q13 | Paradox | Paradox | 2 | Causal Difference-Maker | 12 |  |
| 14 | PT143-S1-Q6 | Paradox | Paradox | 3 | (none) | 12 |  |
| 15 | PT142-S4-Q6 | Necessary Assumption | Necessary Assumption | 1 | Defender; Rebuttals; Timeframes | 12 |  |
| 16 | PT137-S3-Q11 | Necessary Assumption | Necessary Assumption | 2 | Explain Curious Fact; Alternatives; Anti-Causal; Defender; Timeframes | 12 |  |
| 17 | PT107-S1-Q15 | Necessary Assumption | Necessary Assumption | 3 | Missing Link / Idea; Argue the Anti-Conclusion; Assumes Difference; Defender; Dense Stimulus; Medical; New Concept in Conclusion; Science | 12 |  |
| 18 | PT154-S1-Q18 | Necessary Assumption | Necessary Assumption | 4 | Missing Link / Idea; Anti-Causal; Assumes Similarity | 12 |  |
| 19 | PT138-S3-Q1 | Principle-Strengthen | Principle-Strengthen | 2 | Principles in Answers; Weighing Tradeoffs | 12 |  |
| 20 | PT138-S2-Q5 | Principle-Strengthen | Principle-Strengthen | 2 | Missing Link / Idea; Principles in Stimulus | 12 |  |
| 21 | PT155-S4-Q9 | Principle-Strengthen | Principle-Strengthen | 2 | Abstract Answers; First Sentence Conclusion; Missing Link / Idea; Anti-Causal; Intermediate Conclusions; Plans / Recommendations; Principles in Answers | 12 |  |
| 22 | PT151-S2-Q4 | Principle-Conform | Principle-Conform | 1 | Missing Link / Idea; Principles in Answers | 12 |  |
| 23 | PT135-S1-Q6 | Principle-Conform | Principle-Conform | 3 | Implicit Principles | 12 |  |
| 24 | PT121-S4-Q9 | Weaken | Weaken | 2 | Explain Curious Fact; Alternatives; Medical | 12 |  |
| 25 | PT153-S2-Q13 | Weaken | Weaken | 2 | Analogies; Assumes Similarity | 12 |  |
| 26 | PT155-S1-Q19 | Weaken | Weaken | 4 | Explain Curious Fact; Plausibility | 12 |  |
| 27 | PT155-S1-Q23 | Weaken | Weaken (EXCEPT) | 5 | Explain Curious Fact; EXCEPT; Science | 12 |  |
| 28 | PT133-S1-Q17 | Method | Method | 2 | Analogies | 12 |  |
| 29 | PT144-S2-Q8 | Method | Method of Response | 2 | Explain Curious Fact; Ruling Out Options | 12 |  |
| 30 | PT147-S4-Q12 | Method | Method of Argument (type inferred) | 5 | 2-Speaker; Math-y Stuff; Rebuttals | 12 |  |
| 31 | PT154-S1-Q10 | Parallel | Parallel | 1 | (none) | 12 |  |
| 32 | PT108-S2-Q16 | Parallel | Parallel | 2 | Explain Curious Fact; Alternatives; Anti-Causal | 12 |  |
| 33 | PT155-S2-Q19 | Parallel | Parallel Reasoning | 3 | First Sentence Conclusion; Intermediate Conclusions; Timeframes | 12 |  |
| 34 | PT154-S2-Q10 | Parallel Flaw | Parallel Flaw | 1 | Famous Flaws; Sampling; Quantifiers; Rebuttals | 12 |  |
| 35 | PT138-S2-Q25 | Parallel Flaw | Parallel Flaw | 3 | Conditional Diagramming; Conditional Conclusion; Repetitive Answers | 12 |  |
| 36 | PT146-S1-Q21 | Parallel Flaw | Parallel Flaw | 5 | Conditional Diagramming; Quantifiers; Repetitive Answers | 11 | transcription |
| 37 | PT128-S3-Q1 | Strengthen | Strengthen | 1 | Plausibility | 12 |  |
| 38 | PT146-S2-Q13 | Strengthen | Strengthen | 3 | Explain Curious Fact; Medical; Plausibility; Timeframes | 12 |  |
| 39 | PT101-S2-Q4 | Strengthen | Strengthen | 3 | Explain Curious Fact; Breadcrumbs; EXCEPT; Focused on Evidence; Plausibility | 12 |  |
| 40 | PT145-S4-Q2 | Agree/Disagree | Agree/Disagree | 1 | 2-Speaker; Analogies | 12 |  |
| 41 | PT153-S2-Q9 | Agree/Disagree | Agree/Disagree | 2 | 2-Speaker | 12 |  |
| 42 | PT150-S3-Q15 | Agree/Disagree | Agree/Disagree | 4 | 2-Speaker | 12 |  |
| 43 | PT139-S4-Q1 | Main Conclusion | Main Conclusion | 1 | First Sentence Conclusion; Important Pivot; Rebuttals | 12 |  |
| 44 | PT103-S2-Q8 | Main Conclusion | Main Conclusion | 3 | Sufficient vs. Necessary Flaw; First Sentence Conclusion; Contrapositive Logic; Rebuttals | 12 |  |
| 45 | PT154-S2-Q20 | Main Conclusion | Main Conclusion | 4 | First Sentence Conclusion | 12 |  |
| 46 | PT149-S3-Q6 | Role | Role | 2 | Plans / Recommendations; Rebuttals | 12 | slip |
| 47 | PT119-S4-Q25 | Role | Role | 3 | Abstract Answers; Intermediate Conclusions | 12 |  |
| 48 | PT146-S2-Q3 | Sufficient Assumption | Sufficient Assumption | 1 | Missing Link / Idea; New Concept in Conclusion | 12 |  |
| 49 | PT116-S3-Q16 | Sufficient Assumption | Sufficient Assumption | 2 | Missing Link / Idea; Quantifiers | 12 |  |
| 50 | PT141-S4-Q6 | Evaluate | Evaluate the Argument | 1 | Argue the Anti-Conclusion; Plans / Recommendations | 12 |  |

Difficulty mix: 27 easy, 13 medium, 10 hard. Source: 19 from PT101-138, 31 from PT139-159. All 50 are single-style; no explicit-Standard (PT157/158) item made the golden set because their choice notes use a register that conflicts with the house voice (see observations.md). If an explicit-Standard model is wanted, PT158-S4-Q20 (shortlisted) is the best one; PT157-S2-Q7 is the runner-up (read, strong breakdown, not shortlisted).

## Candidates by family (80)

Golden-set members are marked **G**.

### MBT/Most Supported

Gap questions in this family: 115 (by difficulty: d1 23, d2 41, d3 24, d4 13, d5 14).

**PT107-S3-Q5** **G** · Most Supported (bank: Most Strongly Supported) · d1 · Conditional Diagramming; Causal Chains; Science · single · 609w · score 12/12 (P2 X2 E2 T2 C2 L2)
Easy inference built on a causal/conditional chain. States the general move ("if X leads to Y and Y leads to Z, infer X leads to Z"), predicts the chained answer, and rejects B as a sufficient condition misread as necessary and E as reversed causation.
*Weakness:* The chain diagram is inline text and loses its layout.

**PT145-S2-Q23** **G** · Must be True (bank: Must be true) · d2 · Sufficient vs. Necessary Flaw; Contrapositive Logic; Quantifiers · single · 806w · score 12/12 (P2 X2 E2 T2 C2 L2) · fid: slip
Explains which statement commands attention (a lone Most claim is inert, the conditional is not), contraposes, and diagrams the inference before the choices. Wrong answers are refuted with concrete counterexample numbers (100 Velyena mines vs 11 gold mines), the clearest quantifier teaching in the corpus.
*Weakness:* Correct-answer note says "have violated" where it means "have never violated".

**PT104-S1-Q3** **G** · Most Supported · d3 · Explain Curious Fact; Important Pivot; Alternatives; Causal Difference-Maker; Rebuttals · single · 608w · score 12/12 (P2 X2 E2 T2 C2 L2)
Inference that ends on a rebuttal: frames the two competing causal explanations (size vs age) and predicts a safely worded answer that holds age constant. B and C are shown to misplace which variable is held constant.
*Weakness:* Goal step spends a paragraph on facts vs opinions before the prediction.

**PT142-S4-Q7** **G** · Most Supported (bank: Most Strongly Supported) · d3 · Logical Completion · single · 817w · score 12/12 (P2 X2 E2 T2 C2 L2)
Logical completion: treats "assuming X" as one more premise, chains stress to less pain, and predicts a weakly worded causal answer. Each wrong answer is shown to over-reach (usually, surgery, reversed causation).
*Weakness:* Folk-remedy aside is longer than needed.

**PT143-S1-Q13** **G** · Most Supported (bank: Most Strongly Supported) · d5 · Important Pivot · single · 675w · score 12/12 (P2 X2 E2 T2 C2 L2)
Names the pattern ("Reconcile the Pivot") and predicts a moderately worded answer, including what the wrong answers will overdo. Eliminations are grounded: counterfactual speculation (A, D) and right direction but too far ("sketchy, not worthless").
*Weakness:* A and D notes are near-identical text.


### Flaw

Gap questions in this family: 116 (by difficulty: d1 32, d2 36, d3 21, d4 13, d5 14).

**PT151-S2-Q3** **G** · Flaw · d1 · Abstract Answers; Argue the Anti-Conclusion; Causal Chains; Focused on Evidence; Plans / Recommendations; Predictions · single · 1026w · score 10/12 (P1 X2 E2 T2 C1 L2)
Easy abstract-answer Flaw on a causal chain (slippery slope). Each abstract answer is translated back into the argument ("was there a premise saying X was widely accepted?"), which is the move students need for abstract answer choices.
*Weakness:* Goal admits it cannot narrow the objection; long for a d1.

**PT102-S2-Q9** **G** · Flaw · d2 · Explain Curious Fact; Alternatives; Anti-Causal; Argue the Anti-Conclusion · single · 708w · score 12/12 (P2 X2 E2 T2 C2 L2)
Uses the "Given that ... how could we argue that ..." frame to generate the right objection (the protection worked) before reading choices. Each famous-flaw distractor is defined in one line and checked against the argument.
*Weakness:* None significant.

**PT155-S4-Q15** · Flaw · d2 · Famous Flaws; Explain Curious Fact; Assumes Similarity; Plans / Recommendations; Timeframes · single · 655w · score 12/12 (P2 X2 E2 T2 C2 L2) · fid: slip
Names two candidate flaws up front (correlation-to-causation and "the past ten years will continue") and checks each answer against both. C and E are rejected for describing the evidence wrongly.
*Weakness:* Contains a stray "Welcome to Test 89" source reference.

**PT155-S2-Q11** · Flaw · d2 · Famous Flaws; Rebuttals; Science · single · 644w · score 12/12 (P2 X2 E2 T2 C2 L2)
Ad hominem made concrete: lists the five most common famous flaws, picks the likely one, and runs each distractor through "does X match the conclusion and Y the evidence?"
*Weakness:* Wrong-answer notes lean on defining each famous flaw.

**PT139-S4-Q18** **G** · Flaw · d3 · Relative vs. Absolute; Math-y Stuff; Net Effect; Plans / Recommendations · single · 945w · score 11/12 (P2 X2 E2 T2 C1 L2)
Does the arithmetic (25% of $400 vs 13% of $1,000) to expose the relative vs absolute flaw, then states two acceptable targets. Every choice gets the stem-driven test: "fails to consider X" means ask whether X weakens; "presumes X" means ask whether X is necessary.
*Weakness:* Long; B, C and E open with the same boilerplate sentence.

**PT143-S3-Q18** **G** · Flaw · d3 · Sufficient vs. Necessary Flaw; Contrapositive Logic; Plans / Recommendations; Untriggered Conditional · single · 737w · score 12/12 (P2 X2 E2 T2 C2 L2)
Untriggered conditional: shows the conclusion matches the rule outcome but the trigger was never established, then names the Intent vs Consequence flaw. Explains why the tempting Necessary-vs-Sufficient answer is wrong even though conditional logic is present.
*Weakness:* Final diagram lost line breaks in transcription.

**PT118-S3-Q13** **G** · Flaw · d4 · Famous Flaws; Belief / Knowledge / Intent; Abstract Answers; Sampling · single · 594w · score 12/12 (P2 X2 E2 T2 C2 L2)
Splits a two-part conclusion and objects to each part, then names the opinion-vs-fact flaw. Abstract answers are each translated into the famous flaw they describe and tested against this argument.
*Weakness:* None significant.

**PT142-S4-Q22** **G** · Flaw · d4 · Sufficient vs. Necessary Flaw; Famous Flaws · single · 805w · score 12/12 (P2 X2 E2 T2 C2 L2)
Diagrams the conditional, shows both illegal moves, identifies the one the author made, and predicts both the formal and the conversational phrasing of the right answer. Eliminations map "infers X merely from Y" onto conclusion and evidence and check the match.
*Weakness:* Some wrong-answer notes define the famous flaw at length before rejecting it.


### Paradox

Gap questions in this family: 74 (by difficulty: d1 31, d2 26, d3 13, d4 4).

**PT111-S4-Q4** **G** · Paradox · d1 · Math-y Stuff · single · 591w · score 12/12 (P2 X2 E2 T2 C2 L2)
Math paradox: explains why math paradoxes are the exception where you should predict, then runs a 100-person example until only one fix is possible. B is shown to explain the opposite direction.
*Weakness:* None significant.

**PT151-S2-Q13** **G** · Paradox (bank: Most Strongly Supported) · d2 · Causal Difference-Maker · single · 593w · score 12/12 (P2 X2 E2 T2 C2 L2)
States the expectation the fact violates, then says the fix must be tied to the online change or something that changed at the same time. Uses "No Distinction" crisply and explains why D provides a contemporaneous change that still does not explain the outcome.
*Weakness:* None significant.

**PT143-S1-Q6** **G** · Paradox (bank: Strengthen) · d3 · no features · single · 750w · score 12/12 (P2 X2 E2 T2 C2 L2)
Medium paradox with a clean prediction: the danger must fall on people who are not in the SUV. B is flagged for using outside knowledge; E is rewritten into the version that would have worked.
*Weakness:* No bank features.

**PT146-S2-Q12** · Paradox · d2 · Timeframes · single · 585w · score 11/12 (P2 X2 E1 T2 C2 L2)
Lays out several resolution routes (one analysis wrong, cobalt added later, cobalt from another source) and commits to the likeliest while staying flexible.
*Weakness:* B through E notes are short and structurally similar.

**PT106-S2-Q26** · Paradox (bank: Resolve/Reconcile/Explain EXCEPT) · d5 · EXCEPT · single · 614w · score 12/12 (P2 X2 E2 T2 C2 L2)
Paradox EXCEPT: explains that three of the four working answers usually resolve the paradox one way and one works another, lists both routes (fewer bed fires but more deaths per fire; more fires of other kinds), then shows B only restates why bed fires are dangerous.
*Weakness:* Goal step is one long paragraph.


### Necessary Assumption

Gap questions in this family: 72 (by difficulty: d1 11, d2 29, d3 17, d4 11, d5 4).

**PT142-S4-Q6** **G** · Necessary Assumption · d1 · Defender; Rebuttals; Timeframes · single · 730w · score 12/12 (P2 X2 E2 T2 C2 L2)
Easy model that says why a linking answer is less likely than a defender on a real-world argument, lists objections first, and negates the correct answer. Irrelevant-comparison traps are each named for what they compare.
*Weakness:* None significant.

**PT137-S3-Q11** **G** · Necessary Assumption · d2 · Explain Curious Fact; Alternatives; Anti-Causal; Defender; Timeframes · single · 632w · score 12/12 (P2 X2 E2 T2 C2 L2)
Frames the gap as a riddle ("how could a stronger earlier wave have spared the old coral?") and predicts both a link and a defender. Every choice gets the negation test.
*Weakness:* None significant.

**PT147-S1-Q24** · Necessary Assumption (type inferred) (bank: Necessary Assumption) · d3 · Assumes Difference; Defender; Rebuttals; Refute a Conditional; Science · single · 875w · score 11/12 (P1 X2 E2 T2 C2 L2)
New concept in the conclusion (artificial intelligence) flagged as the gap. The author admits confusion and still builds a usable prediction, which models what to do when an argument is unclear. A and C are rejected as broader than the claim about one route to AI.
*Weakness:* Leans on a guessing heuristic (answers that rule something out are "lovable").

**PT108-S3-Q1** · Necessary Assumption · d2 · Missing Link / Idea; Defender; EXCEPT; Links Between Premises; Plans / Recommendations · single · 771w · score 12/12 (P2 X2 E2 T2 C2 L2)
Necessary Assumption EXCEPT on a plan: lists what any problem/solution argument assumes (the problem matters, the fix works, nothing better) with a leaky-faucet plumber analogy, then negates each choice.
*Weakness:* Long Goal step.

**PT107-S1-Q15** **G** · Necessary Assumption · d3 · Missing Link / Idea; Argue the Anti-Conclusion; Assumes Difference; Defender; Dense Stimulus; Medical; New Concept in Conclusion; Science · single · 704w · score 12/12 (P2 X2 E2 T2 C2 L2)
Dense medical stimulus: first asks why the author thinks the condition is worse at altitude (misdiagnosis), then predicts the storyline the answer must support. D is flagged as an outside-knowledge trap and E as a misread of "can recover".
*Weakness:* Correct-answer note is casual ("Yeah, I guess he was!").

**PT154-S1-Q18** **G** · Necessary Assumption · d4 · Missing Link / Idea; Anti-Causal; Assumes Similarity · single · 904w · score 12/12 (P2 X2 E2 T2 C2 L2)
Names two precise gaps ("not necessary" read as "not helpful"; "mastered grammar" read as "learned the language"), with a Harvard/175 analogy for the first. Negation test applied to every choice.
*Weakness:* A couple of typos.


### Principle-Strengthen

Gap questions in this family: 36 (by difficulty: d1 12, d2 19, d3 2, d4 3).

**PT138-S3-Q1** **G** · Principle-Strengthen (bank: Principle-Conform) · d2 · Principles in Answers; Weighing Tradeoffs · single · 742w · score 12/12 (P2 X2 E2 T2 C2 L2)
Starts from "if premise, then conclusion", then recognizes that the right answer is a weighing-tradeoffs principle with no "should" in it, and explains why it still justifies the conclusion.
*Weakness:* Correct-answer note is short.

**PT138-S2-Q5** **G** · Principle-Strengthen (bank: Principle Strengthen) · d2 · Missing Link / Idea; Principles in Stimulus · single · 560w · score 12/12 (P2 X2 E2 T2 C2 L2)
Principle given in the stimulus: puts the judgment on the right side, identifies the one fact needed to trigger it, and predicts it word for word. B through E each fail the same trigger test.
*Weakness:* B through E share one pasted opening.

**PT155-S4-Q9** **G** · Principle-Strengthen (bank: Principle Strengthen) · d2 · Abstract Answers; First Sentence Conclusion; Missing Link / Idea; Anti-Causal; Intermediate Conclusions; Plans / Recommendations; Principles in Answers · single · 701w · score 12/12 (P2 X2 E2 T2 C2 L2)
Shows the answer may target the premise-to-intermediate-conclusion move rather than the main conclusion, with both predictions diagrammed. Abstract principles are matched by what they have the power to prove.
*Weakness:* None significant.

**PT147-S1-Q14** · Principle (Justify) (type inferred) (bank: Principle Justify) · d2 · 2-Speaker; Principles in Answers; Weighing Tradeoffs · single · 730w · score 12/12 (P2 X2 E2 T2 C2 L2)
Two-speaker principle: frames the task as answering Zagel's objection from the activist's side. Explains why the one comparison answer beats four conditionals whose triggers cannot be met.
*Weakness:* Typo in a tag ("Conlusion").


### Principle-Conform

Gap questions in this family: 34 (by difficulty: d1 9, d2 17, d3 4, d4 3, d5 1).

**PT151-S2-Q4** **G** · Principle-Conform · d1 · Missing Link / Idea; Principles in Answers · single · 654w · score 12/12 (P2 X2 E2 T2 C2 L2)
Names the two ideas behind the engineer's reasoning (golden rule; put my money where my mouth is) and diagrams every answer as trigger → outcome, asking whether the stimulus establishes the trigger.
*Weakness:* None significant.

**PT139-S1-Q8** · Principle-Conform (bank: Principle: Underlying) · d2 · Implicit Principles; Repetitive Answers; Weighing Tradeoffs · single · 491w · score 12/12 (P2 X2 E2 T2 C2 L2)
Underlying-principle model: names diminishing returns, predicts with an A vs A+ paraphrase, and separates C from D on the last ingredient only.
*Weakness:* Short (490w) for five long answer choices.

**PT135-S1-Q6** **G** · Principle-Conform · d3 · Implicit Principles · single · 664w · score 12/12 (P2 X2 E2 T2 C2 L2)
Illustrated-principle question treated like a slogan-style parallel: states the principle as "you can’t be sure, so play it safe", then walks A and B element by element (potential wrong, uncertainty, cautious action).
*Weakness:* C through E notes are brief.

**PT153-S3-Q25** · Principle-Conform (bank: Principle Conform) · d4 · Implicit Principles; Plans / Recommendations · single · 641w · score 12/12 (P2 X2 E2 T2 C2 L2)
Extracts the implicit principle with a general template ("avoid X because X leads to Y" assumes "avoid what leads to Y"), then abstracts it. Each wrong answer is matched on its evidence.
*Weakness:* None significant.

**PT152-S2-Q21** · Principle-Conform · d5 · Principles in Stimulus · single · 622w · score 12/12 (P2 X2 E2 T2 C2 L2)
Two portable rules: a rule can only prove its right-hand side, and the OR-trigger rule is the likely one used. Three choices are eliminated on the conclusion alone.
*Weakness:* The diagram block is pasted into every note.


### Weaken

Gap questions in this family: 53 (by difficulty: d1 8, d2 15, d3 15, d4 10, d5 4).

**PT121-S4-Q9** **G** · Weaken · d2 · Explain Curious Fact; Alternatives; Medical · single · 900w · score 12/12 (P2 X2 E2 T2 C2 L2)
Study-to-causal-conclusion weaken: names the correlation, the two weakening routes, and ranks D (a real methodological flaw) below A because of what the study measured.
*Weakness:* None significant.

**PT153-S2-Q13** **G** · Weaken · d2 · Analogies; Assumes Similarity · single · 784w · score 12/12 (P2 X2 E2 T2 C2 L2)
Standard analogy attack ("how are these two situations meaningfully different?"). The final note lines up all five answers as completions of "you shouldn't use a dictionary, because..." so the student sees why only B is a relevant difference.
*Weakness:* None significant.

**PT107-S1-Q16** · Weaken · d3 · Missing Link / Idea; Explain Curious Fact; Argue the Anti-Conclusion; Implicit Principles · single · 625w · score 12/12 (P2 X2 E2 T2 C2 L2)
States the implicit principle the argument runs on ("having a word for X means X was in your life") and shows why a weakly worded answer that hits it beats stronger-sounding ones.
*Weakness:* None significant.

**PT155-S1-Q19** **G** · Weaken · d4 · Explain Curious Fact; Plausibility · single · 880w · score 12/12 (P2 X2 E2 T2 C2 L2)
Curious Fact / Alternate Explanation / Plausibility frame, plus the relative vs absolute shift between evidence and conclusion. C is killed with a precise distinction (producing technology is not relying on it).
*Weakness:* E's analogy is heavier than it needs to be.

**PT106-S2-Q25** · Weaken · d4 · Intermediate Conclusions; Plans / Recommendations; Rebuttals · single · 800w · score 12/12 (P2 X2 E2 T2 C2 L2)
Three-part argument: tests both moves (unaware means involuntary; involuntary means not responsible) and predicts the "you can learn to control it" objection. The "not all A are B" rewrite is taught in C and E.
*Weakness:* None significant.

**PT155-S1-Q23** **G** · Weaken (EXCEPT) (bank: Weaken) · d5 · Explain Curious Fact; EXCEPT; Science · single · 777w · score 12/12 (P2 X2 E2 T2 C2 L2)
Best EXCEPT model found. Two fill-in sentence frames ("Life did occur on Mars. The meteorite shows the pre-life ratio because...") that every weakener must complete, so the odd one out is obvious.
*Weakness:* None significant.


### Method

Gap questions in this family: 55 (by difficulty: d1 20, d2 19, d3 12, d4 3, d5 1).

**PT133-S1-Q17** **G** · Method (bank: Method of Reasoning) · d2 · Analogies · single · 755w · score 12/12 (P2 X2 E2 T2 C2 L2)
Analogy method: names the shared principle behind the analogy and teaches "argues X by Y: X must match the conclusion, Y the evidence" to test every answer.
*Weakness:* None significant.

**PT144-S2-Q8** **G** · Method of Response (bank: Miscellaneous) · d2 · Explain Curious Fact; Ruling Out Options · single · 674w · score 12/12 (P2 X2 E2 T2 C2 L2)
Easy two-speaker method: frames the study as a curious fact, predicts "alternate explanation", and flags the recurring trap that a respondent never denies the evidence.
*Weakness:* None significant.

**PT118-S1-Q4** · Method · d2 · Abstract Answers · single · 776w · score 12/12 (P2 X2 E2 T2 C2 L2)
Lists the stock method moves (analogy, counterexample, alternate explanation, and so on) and predicts "same premises, different conclusion". A is the standard "denies the premises" trap.
*Weakness:* None significant.

**PT143-S1-Q4** · Method (bank: Method of Reasoning) · d3 · Ruling Out Options · single · 395w · score 11/12 (P2 X2 E2 T2 C2 L1)
Single-speaker method: describes the argument abstractly, then gives the two-part matching recipe ("[doing] the conclusion [by] presenting evidence") used to strike answers on one wrong word.
*Weakness:* Short (395w); correct note just restates the match.

**PT147-S4-Q12** **G** · Method of Argument (type inferred) (bank: Method of Reasoning) · d5 · 2-Speaker; Math-y Stuff; Rebuttals · single · 732w · score 12/12 (P2 X2 E2 T2 C2 L2)
Works the proportionality with numbers (Haynes inspects 65% of items but causes 50% of returns). Flags that respondents almost never deny a stated premise.
*Weakness:* B note is thin.


### Parallel

Gap questions in this family: 24 (by difficulty: d1 7, d2 10, d3 4, d4 1, d5 2).

**PT154-S1-Q10** **G** · Parallel · d1 · no features · single · 559w · score 12/12 (P2 X2 E2 T2 C2 L2)
Diagrams the dilemma (A → X, not A → X, so X) and diagrams every answer the same way, so structure mismatches are visible at a glance.
*Weakness:* No bank features; formal house voice.

**PT108-S2-Q16** **G** · Parallel · d2 · Explain Curious Fact; Alternatives; Anti-Causal · single · 788w · score 12/12 (P2 X2 E2 T2 C2 L2)
Parallel on reverse causation: offers both an algebraic and a conversational model and shows how each wrong answer breaks one ingredient (weak correlation, wrong direction, one data point).
*Weakness:* None significant.

**PT155-S2-Q19** **G** · Parallel Reasoning (bank: Parallel) · d3 · First Sentence Conclusion; Intermediate Conclusions; Timeframes · single · 442w · score 12/12 (P2 X2 E2 T2 C2 L2)
Non-formal parallel: says why not to diagram, strips the topic to a story ("even if it starts perfect, it drifts"), and uses conclusion strength for quick eliminations.
*Weakness:* Short correct-answer note.

**PT144-S4-Q22** · Parallel Reasoning (bank: Parallel method of reasoning) · d5 · Conditional Diagramming; Quantifiers; Repetitive Answers · single · 820w · score 12/12 (P2 X2 E2 T2 C2 L2)
Abstracts the form (Most A are B; only C gives B; so some A are C) and spots that the conclusion is deliberately weaker than it could be, which separates A from B. C, D, E rejected as untriggered conditionals with the backwards reading named.
*Weakness:* None significant.


### Parallel Flaw

Gap questions in this family: 31 (by difficulty: d1 3, d2 11, d3 9, d4 7, d5 1).

**PT154-S2-Q10** **G** · Parallel Flaw · d1 · Famous Flaws; Sampling; Quantifiers; Rebuttals · single · 793w · score 12/12 (P2 X2 E2 T2 C2 L2)
Sampling flaw explained with a covid and NBA-height analogy; says the personal-experience detail is not the flaw, the tiny sample is. C and D are shown to have the right feel plus an extra flaw.
*Weakness:* None significant.

**PT153-S3-Q11** · Parallel Flaw · d1 · Relative vs. Absolute; Conditional Conclusion; Math-y Stuff · single · 909w · score 11/12 (P2 X2 E2 T2 C1 L2)
Base-rate flaw with a citizenship analogy, then says you can skip full understanding and take the algebraic recipe to the answers, screening conclusions first.
*Weakness:* Analogy is long for d1.

**PT150-S3-Q8** · Parallel Flaw (bank: Flaw) · d2 · Sufficient vs. Necessary Flaw; Famous Flaws; Repetitive Answers; Ruling Out Options · single · 708w · score 12/12 (P2 X2 E2 T2 C2 L2)
Two flaws at once (illegal reversal plus arbitrary choice between A and B), reduced to a recipe (A or B → C; X is C; so X is B) that every answer is checked against.
*Weakness:* Notes are repetitive by design.

**PT138-S2-Q25** **G** · Parallel Flaw · d3 · Conditional Diagramming; Conditional Conclusion; Repetitive Answers · single · 727w · score 12/12 (P2 X2 E2 T2 C2 L2)
Conditional parallel flaw: builds the algebraic recipe (two premises with the same trigger, one reversed) and eliminates A, D and E on the trigger check alone.
*Weakness:* Diagram text is inline.

**PT146-S1-Q21** **G** · Parallel Flaw (bank: Flawed Parallel Reasoning) · d5 · Conditional Diagramming; Quantifiers; Repetitive Answers · single · 727w · score 11/12 (P2 X2 E2 T2 C1 L2) · fid: transcription
Most + most inference, with 11 soil types showing why splitting the conclusion in two is illegal. Makes the point that on formal parallel flaw you can match structure without fully diagnosing the flaw.
*Weakness:* Final sentence of the E note is garbled.


### Strengthen

Gap questions in this family: 41 (by difficulty: d1 13, d2 10, d3 11, d4 3, d5 4).

**PT128-S3-Q1** **G** · Strengthen · d1 · Plausibility · single · 953w · score 12/12 (P2 X2 E2 T2 C2 L2)
Easy strengthen on a curious fact: says the most common plausibility booster is a cause-present/effect-present data point, predicts it, and the correct answer is exactly that.
*Weakness:* Long for d1.

**PT104-S4-Q2** · Strengthen · d1 · Missing Link / Idea; Assumes Similarity; Defender; Net Effect; Predictions · single · 689w · score 12/12 (P2 X2 E2 T2 C2 L2)
Easy strengthen: states the link ("more channels is a selling point") and the net-effect objection, then shows the correct answer rules out "the channels are worse". D is dismissed with the at-least-one rule.
*Weakness:* None significant.

**PT115-S2-Q10** · Strengthen · d2 · 2-Speaker; Plans / Recommendations · single · 798w · score 12/12 (P2 X2 E2 T2 C2 L2)
Two-speaker strengthen: states Lorraine’s linking assumption, lists objections, and predicts answers that shut them down. A and D are identified as the objections themselves.
*Weakness:* None significant.

**PT146-S2-Q13** **G** · Strengthen · d3 · Explain Curious Fact; Medical; Plausibility; Timeframes · single · 722w · score 12/12 (P2 X2 E2 T2 C2 L2)
Names the "policy went into effect, then X happened" structure. The correct-answer note offers a second hypothetical correct answer (moisturizer sales), teaching the function, not just the key.
*Weakness:* None significant.

**PT101-S2-Q4** **G** · Strengthen (bank: Strengthen (EXCEPT)) · d3 · Explain Curious Fact; Breadcrumbs; EXCEPT; Focused on Evidence; Plausibility · single · 740w · score 12/12 (P2 X2 E2 T2 C2 L2)
Strengthen EXCEPT: finds a coy conclusion, then shows two answers only work if you catch the breadcrumb in the first sentence (stress and weight gain). C fails on scope (nonsmokers).
*Weakness:* None significant.

**PT154-S2-Q16** · Strengthen · d4 · Anti-Causal; Focused on Evidence; Rebuttals · single · 743w · score 12/12 (P2 X2 E2 T2 C2 L2)
"Strengthen the grounds" variant: uses a weaken mindset to generate objections, then flips them into predicted strengtheners. Flags weak-quantifier answers (C) as rarely right on Strengthen/Weaken.
*Weakness:* D note spends a line on a joke.


### Agree/Disagree

Gap questions in this family: 38 (by difficulty: d1 16, d2 10, d3 9, d4 2, d5 1).

**PT145-S4-Q2** **G** · Agree/Disagree (bank: Point at issue) · d1 · 2-Speaker; Analogies · single · 567w · score 12/12 (P2 X2 E2 T2 C2 L2)
Claim-by-claim table: for each of Albert's claims, "does Yvonne disagree?" with a yes/no reason. Every answer is tested for an Agree position and a Disagree position.
*Weakness:* None significant.

**PT153-S2-Q9** **G** · Agree/Disagree · d2 · 2-Speaker · single · 772w · score 12/12 (P2 X2 E2 T2 C2 L2)
Teaches that a speaker can agree with the conclusion but reject the reasoning (Lebron vs Jordan), which is exactly what the correct answer tests. Each wrong answer is checked for both positions.
*Weakness:* None significant.

**PT115-S2-Q23** · Agree/Disagree · d3 · 2-Speaker; Weighing Tradeoffs · single · 542w · score 12/12 (P2 X2 E2 T2 C2 L2) · fid: slip
Claim-by-claim table where the disagreement is about a conditional recommendation, not the underlying goal.
*Weakness:* One line says "Y seems to agree" where it means disagree.

**PT150-S3-Q15** **G** · Agree/Disagree · d4 · 2-Speaker · single · 643w · score 12/12 (P2 X2 E2 T2 C2 L2)
Lays out claims and reactions, including implicit ones, and names the exact friction ("strongly supports" vs "sheer speculation"). Each wrong answer is tested for both speakers, with a polling analogy.
*Weakness:* None significant.

**PT158-S4-Q20** · Agree/Disagree · d5 · 2-Speaker; Dense Stimulus; Science · standard · 759w · score 11/12 (P2 X2 E2 T2 C1 L2) · fid: register
Best explicit-Standard exemplar. Goes claim by claim through Paula and checks for Ashley's pushback, down to assumptions. Choice notes are accurate and speaker-by-speaker.
*Weakness:* PT158-register choice notes.


### Main Conclusion

Gap questions in this family: 31 (by difficulty: d1 8, d2 12, d3 8, d4 2, d5 1).

**PT139-S4-Q1** **G** · Main Conclusion · d1 · First Sentence Conclusion; Important Pivot; Rebuttals · single · 525w · score 12/12 (P2 X2 E2 T2 C2 L2)
The three Main Conclusion reminders, plus "replace referential language with specifics" before matching. Each wrong answer is labeled by role (intermediate conclusion, premise, opposing position).
*Weakness:* None significant.

**PT118-S1-Q1** · Main Conclusion · d1 · First Sentence Conclusion; Implied Conclusion; Rebuttals · single · 728w · score 12/12 (P2 X2 E2 T2 C2 L2)
Main-point variant: explains how an "the author is arguing that" stem changes what the answer looks like (a paraphrase or implication, not a restatement).
*Weakness:* None significant.

**PT103-S2-Q8** **G** · Main Conclusion · d3 · Sufficient vs. Necessary Flaw; First Sentence Conclusion; Contrapositive Logic; Rebuttals · single · 653w · score 12/12 (P2 X2 E2 T2 C2 L2)
Separates main from intermediate conclusion when both sit in the first sentence ("because" marks the support). D is named as the last-claim trap.
*Weakness:* None significant.

**PT154-S2-Q20** **G** · Main Conclusion · d4 · First Sentence Conclusion · single · 877w · score 12/12 (P2 X2 E2 T2 C2 L2)
Reading posture for Main Conclusion, a word-by-word synonym map from the first sentence to A, and a one-test elimination for B through E.
*Weakness:* Italic-label layout (PT154); one odd word ("aloofly").

**PT106-S3-Q14** · Main Conclusion · d4 · Dense Stimulus; Implied Conclusion; Intermediate Conclusions · single · 644w · score 12/12 (P2 X2 E2 T2 C2 L2)
Implied conclusion: neither the first sentence nor a pivot is the conclusion, so it tests candidates with "is this the author’s opinion, and is it supported?"
*Weakness:* None significant.


### Role

Gap questions in this family: 22 (by difficulty: d1 5, d2 7, d3 8, d4 2).

**PT149-S3-Q6** **G** · Role (bank: Role in Argument) · d2 · Plans / Recommendations; Rebuttals · single · 585w · score 12/12 (P2 X2 E2 T2 C2 L2) · fid: slip
Implicit rebuttal conclusion and the "90% first sentence or pivot" heuristic, including when it fails. E is eliminated from the "Therefore" direction alone.
*Weakness:* Typo ("rub out faces").

**PT155-S2-Q16** · Role of a Claim (Method) (bank: Role) · d3 · Conditional Conclusion; Intermediate Conclusions · single · 696w · score 12/12 (P2 X2 E2 T2 C2 L2)
Two conclusions: uses the Support Test ("which one would support the other?") to rank them, then the "Why should I believe this?" test for intermediate conclusions.
*Weakness:* None significant.

**PT119-S4-Q25** **G** · Role · d3 · Abstract Answers; Intermediate Conclusions · single · 718w · score 12/12 (P2 X2 E2 T2 C2 L2)
Role of a concession: sorts claims into conclusion, support, opposing, neutral, and uses "although" to predict a qualifying role.
*Weakness:* None significant.

**PT144-S3-Q17** · Role (bank: Argument part) · d5 · Causal Chains · single · 810w · score 12/12 (P2 X2 E2 T2 C2 L2)
Premise vs intermediate conclusion done right: is there explicit support for this claim? Walks C through that test and rejects E on two layers.
*Weakness:* "Umbrella Claim (pun intended)" aside.


### Sufficient Assumption

Gap questions in this family: 16 (by difficulty: d1 3, d2 6, d3 2, d4 2, d5 3).

**PT146-S2-Q3** **G** · Sufficient Assumption (bank: Necessary Assumption) · d1 · Missing Link / Idea; New Concept in Conclusion · single · 578w · score 12/12 (P2 X2 E2 T2 C2 L2)
Missing-link subtraction for a new concept in the conclusion, with the contrapositive shown as an equally correct form and "unless = if not" taught in the correct note.
*Weakness:* Formal house voice; no analogies.

**PT116-S3-Q16** **G** · Sufficient Assumption · d2 · Missing Link / Idea; Quantifiers · single · 895w · score 12/12 (P2 X2 E2 T2 C2 L2)
Quantified sufficient assumption: states what must be proven (at least one thing in both groups) and why a "some" statement combined with the "all" premise proves it.
*Weakness:* C through E share a pasted opening.

**PT155-S4-Q7** · Sufficient Assumption (bank: Necessary Assumption) · d2 · Missing Link / Idea; Links Between Premises; New Concept in Conclusion; Predictions; Untriggered Conditional · single · 413w · score 11/12 (P2 X2 E1 T2 C2 L2)
Untriggered conditional in the evidence: contraposes, shows the conclusion follows once the trigger is supplied, and the correct answer links both premises.
*Weakness:* Wrong-answer notes are brief ("Out of Scope").

**PT139-S4-Q21** · Sufficient Assumption · d5 · Conditional Diagramming · single · 819w · score 12/12 (P2 X2 E2 T2 C2 L2) · fid: transcription
Chains the conditionals, sees the job is triggering "published", predicts the link, then explains why A → C still works when the prediction was A and B → C (karaoke/Jenga analogy).
*Weakness:* Diagram lines lost spacing in transcription.


### Evaluate

Gap questions in this family: 3 (by difficulty: d1 2, d2 1).

**PT141-S4-Q6** **G** · Evaluate the Argument (bank: Evaluate) · d1 · Argue the Anti-Conclusion; Plans / Recommendations · single · 571w · score 12/12 (P2 X2 E2 T2 C2 L2)
Easy model: generate objections to the plan, then test each question by imagining answers to it ("whether we say two or two hundred, no effect").
*Weakness:* None significant.

**PT104-S4-Q6** · Evaluate · d3 · Argue the Anti-Conclusion; Untriggered Conditional · single · 628w · score 12/12 (P2 X2 E2 T2 C2 L2)
Evaluate on an untriggered conditional: shows the argument never established that butterflies fall, and the correct question asks exactly that.
*Weakness:* None significant.

**PT147-S1-Q17** · Evaluate (type inferred) (bank: Argument Evaluation) · d4 · Net Effect; Plans / Recommendations · single · 825w · score 12/12 (P2 X2 E2 T2 C2 L2)
Every choice gets the yes/no test: can either answer to this question produce an objection? C is worked with numbers (10% replaced a year means all of them over a decade).
*Weakness:* None significant.

## Coverage grid

Rows are families; columns are difficulty bands, then every feature that tags 10 or more gap questions (feature list and counts from `wiki/lr-missing-explanations-by-category.md`). A cell shows shortlisted candidates / golden picks, e.g. `2/1`. **`!!`** = no candidate but the gap set has 3 or more questions of that family with that feature (a real hole). `.` = no candidate and fewer than 3 gap questions need it. Blank = no candidate and no gap demand.

Feature key: Plan = Plans / Recommendations; Reb = Rebuttals; MLnk = Missing Link / Idea; ECF = Explain Curious Fact; Sci = Science; 2Spk = 2-Speaker; Anti = Argue the Anti-Conclusion; FamF = Famous Flaws; Time = Timeframes; Alt = Alternatives; PrA = Principles in Answers; SvN = Sufficient vs. Necessary Flaw; Piv = Important Pivot; NewC = New Concept in Conclusion; Plaus = Plausibility; Med = Medical; Anlg = Analogies; Net = Net Effect; AntiC = Anti-Causal; CDM = Causal Difference-Maker; Abst = Abstract Answers; EXC = EXCEPT; Def = Defender; Math = Math-y Stuff; Ctrp = Contrapositive Logic; 1stC = First Sentence Conclusion; CDiag = Conditional Diagramming; Dense = Dense Stimulus; ASim = Assumes Similarity; ROut = Ruling Out Options; Quant = Quantifiers; Pred = Predictions; LComp = Logical Completion; Trade = Weighing Tradeoffs; CConc = Conditional Conclusion; BKI = Belief / Knowledge / Intent; Brd = Breadcrumbs; IC = Intermediate Conclusions; Samp = Sampling; RefC = Refute a Conditional; ADif = Assumes Difference; FocE = Focused on Evidence; CChn = Causal Chains; PrS = Principles in Stimulus; Untr = Untriggered Conditional; ImpP = Implicit Principles.

| Family | E | M | H | Plan | Reb | MLnk | ECF | Sci | 2Spk | Anti | FamF | Time | Alt | PrA | SvN | Piv | NewC | Plaus | Med | Anlg | Net | AntiC | CDM | Abst | EXC | Def | Math | Ctrp | 1stC | CDiag | Dense | ASim | ROut | Quant | Pred | LComp | Trade | CConc | BKI | Brd | IC | Samp | RefC | ADif | FocE | CChn | PrS | Untr | ImpP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MBT/Most Supported | 2/2 | 2/2 | 1/1 | !! | 1/1 | !! | 1/1 | 1/1 | !! | . | . | !! | 1/1 |  | 1/1 | 2/2 | !! | . | !! | !! |  |  | 1/1 |  | !! | . | !! | 1/1 | . | 1/1 | !! | . | . | 1/1 |  | 1/1 | . | !! | !! | . | . |  | . |  |  | 1/1 | . | . |  |
| Flaw | 4/2 | 2/2 | 2/2 | 4/3 | 1/0 | !! | 2/1 | 1/0 | !! | 2/2 | 4/2 | 1/0 | 1/1 |  | 2/2 | . | . | !! | !! | . | 1/1 | 1/1 |  | 2/2 | . |  | 1/1 | 1/1 | . | !! |  | 1/0 | !! | . | 1/1 |  |  | !! | 1/1 |  | . | 1/1 | . | . | 1/1 | 1/1 | . | 1/1 |  |
| Paradox | 3/2 | 1/1 | 1/0 | !! | . |  | . | !! | . | . |  | 1/0 | . |  |  | . |  |  | !! |  | !! | . | 1/1 |  | 1/0 |  | 1/1 |  | . |  |  |  |  |  |  |  |  |  |  | !! |  | . |  | . |  |  |  |  |  |
| Necessary Assumption | 3/2 | 2/1 | 1/1 | 1/0 | 2/1 | 3/2 | 1/1 | 2/1 |  | 1/1 |  | 2/2 | 1/1 |  | !! | . | 1/1 | !! | 1/1 | !! | !! | 2/2 | . | . | 1/0 | 5/3 | !! | !! | . | . | 1/1 | 1/1 | !! |  | !! | . | !! | !! | . |  | . |  | 1/0 | 2/1 |  | . |  | !! |  |
| Principle-Strengthen | 4/3 | . | !! | 1/1 | . | 2/2 | . | . | 1/0 |  |  | . |  | 3/2 | . |  | . |  |  | . |  | 1/1 | !! | 1/1 |  |  |  | . | 1/1 | . | . | . |  |  |  |  | 2/1 | . | . |  | 1/1 |  |  |  |  |  | 1/1 |  | . |
| Principle-Conform | 2/1 | 1/1 | 2/0 | 1/0 | . | 1/1 |  |  |  |  |  | . |  | 1/1 |  | . | . | . |  |  | . |  | . | . |  |  |  |  | . |  |  |  |  |  |  |  | 1/0 |  | . |  |  |  |  |  |  |  | 1/0 |  | 3/1 |
| Weaken | 2/2 | 1/0 | 3/2 | 1/0 | 1/0 | 1/0 | 4/3 | 1/1 | !! | 1/0 | . | !! | 1/1 |  | . | . |  | 1/1 | 1/1 | 1/1 | !! | !! | . |  | 1/1 |  | . | . |  | . | . | 1/1 |  |  | !! |  | . |  | . | !! | 1/0 |  |  | . | !! |  |  | . | 1/0 |
| Method | 3/2 | 1/0 | 1/1 | !! | 1/1 |  | 1/1 | !! | 1/1 |  |  | . | !! |  | !! | . |  |  | !! | 1/1 |  |  |  | 1/0 | . |  | 1/1 | !! |  | . | . |  | 2/1 |  | . |  |  | . | !! |  | . |  | . |  |  |  | . |  |  |
| Parallel | 2/2 | 1/1 | 1/0 | !! | . |  | 1/1 | . |  |  |  | 1/1 | 1/1 |  | !! |  |  |  |  | . |  | 1/1 |  |  |  |  | . | !! | 1/1 | 1/0 |  | . | !! | 1/0 | . | . | . | . | . |  | 1/1 |  | . |  |  | . |  | . | . |
| Parallel Flaw | 3/1 | 1/1 | 1/1 | !! | 1/1 |  | . | . | . | !! | 2/1 | . |  |  | 1/0 |  |  |  |  | . | . | . |  |  |  |  | 1/0 |  | . | 2/2 |  |  | 1/0 | 2/2 |  |  | . | 2/1 | . |  |  | 1/1 | . | . | . |  |  |  |  |
| Strengthen | 3/1 | 2/2 | 1/0 | 1/0 | 1/0 | 1/0 | 2/2 | !! | 1/0 | . |  | 1/1 | . |  |  | . | . | 3/3 | 1/1 |  | 1/0 | 1/0 |  |  | 1/1 | 1/0 | . |  |  |  | . | 1/0 |  |  | 1/0 | . | !! |  |  | 1/1 | . | !! |  | . | 2/1 |  |  | . |  |
| Agree/Disagree | 2/2 | 1/0 | 2/1 | . | . |  | !! | 1/0 | 5/3 | . |  | !! |  |  | . |  | . | . | . | 1/1 |  |  |  |  |  |  |  |  |  |  | 1/0 |  |  |  | . |  | 1/0 |  |  |  |  |  | . |  | . |  |  |  |  |
| Main Conclusion | 2/1 | 1/1 | 2/1 | !! | 3/2 |  | . | !! |  |  |  | !! | . |  | 1/1 | 1/1 |  |  | . | !! |  | . |  |  |  |  |  | 1/1 | 4/3 |  | 1/0 |  |  |  | . |  | . | . |  |  | 1/0 |  | . |  |  |  |  |  |  |
| Role | 1/1 | 2/1 | 1/0 | 1/1 | 1/1 |  | . | . |  |  |  |  | . |  |  | !! |  | . | . |  |  |  |  | 1/1 |  |  |  |  | !! |  | . |  | . |  |  |  | . | 1/0 |  |  | 2/1 |  | . |  |  | 1/0 |  |  |  |
| Sufficient Assumption | 3/2 | . | 1/0 | . | . | 3/2 |  | . |  | . |  | . |  |  |  |  | 2/1 |  | . |  |  | . |  |  |  | . | . |  | !! | 1/0 | . |  | . | 1/1 | 1/0 |  |  |  |  |  |  |  | . |  |  |  |  | 1/0 |  |
| Evaluate | 1/1 | 1/0 | 1/0 | 2/1 |  |  | . | . |  | 2/1 |  |  | . |  |  |  |  | . | . |  | 1/0 |  |  |  | . |  | . |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 1/0 |  |

### Feature totals across the shortlist

| Feature | Gap questions | Shortlisted | Golden |
|---|---|---|---|
| Plans / Recommendations | 121 | 12 | 6 |
| Rebuttals | 115 | 12 | 7 |
| Missing Link / Idea | 82 | 11 | 7 |
| Explain Curious Fact | 81 | 12 | 10 |
| Science | 75 | 6 | 3 |
| 2-Speaker | 73 | 8 | 4 |
| Argue the Anti-Conclusion | 56 | 6 | 4 |
| Famous Flaws | 54 | 6 | 3 |
| Timeframes | 52 | 6 | 4 |
| Alternatives | 47 | 5 | 5 |
| Principles in Answers | 45 | 4 | 3 |
| Sufficient vs. Necessary Flaw | 43 | 5 | 4 |
| Important Pivot | 40 | 3 | 3 |
| New Concept in Conclusion | 37 | 3 | 2 |
| Plausibility | 34 | 4 | 4 |
| Medical | 34 | 3 | 3 |
| Analogies | 33 | 3 | 3 |
| Net Effect | 32 | 3 | 1 |
| Anti-Causal | 32 | 6 | 5 |
| Causal Difference-Maker | 32 | 2 | 2 |
| Abstract Answers | 31 | 5 | 4 |
| EXCEPT | 30 | 4 | 2 |
| Defender | 29 | 6 | 3 |
| Math-y Stuff | 28 | 4 | 3 |
| Contrapositive Logic | 28 | 3 | 3 |
| First Sentence Conclusion | 27 | 6 | 5 |
| Conditional Diagramming | 25 | 5 | 3 |
| Dense Stimulus | 23 | 3 | 1 |
| Assumes Similarity | 23 | 4 | 2 |
| Ruling Out Options | 22 | 3 | 1 |
| Quantifiers | 21 | 5 | 4 |
| Predictions | 21 | 3 | 1 |
| Logical Completion | 19 | 1 | 1 |
| Weighing Tradeoffs | 19 | 4 | 1 |
| Conditional Conclusion | 19 | 3 | 1 |
| Belief / Knowledge / Intent | 19 | 1 | 1 |
| Breadcrumbs | 15 | 1 | 1 |
| Intermediate Conclusions | 15 | 6 | 3 |
| Sampling | 15 | 2 | 2 |
| Refute a Conditional | 14 | 1 | 0 **(none)** |
| Assumes Difference | 13 | 2 | 1 |
| Focused on Evidence | 12 | 3 | 2 |
| Causal Chains | 12 | 3 | 2 |
| Principles in Stimulus | 12 | 2 | 1 |
| Untriggered Conditional | 11 | 3 | 1 |
| Implicit Principles | 10 | 4 | 1 |

### Empty cells worth acting on

Family-level cells marked `!!` above:

- MBT/Most Supported · Plans / Recommendations (5 gap questions)
- MBT/Most Supported · Missing Link / Idea (5 gap questions)
- MBT/Most Supported · 2-Speaker (4 gap questions)
- MBT/Most Supported · Timeframes (4 gap questions)
- MBT/Most Supported · New Concept in Conclusion (3 gap questions)
- MBT/Most Supported · Medical (9 gap questions)
- MBT/Most Supported · Analogies (7 gap questions)
- MBT/Most Supported · EXCEPT (5 gap questions)
- MBT/Most Supported · Math-y Stuff (6 gap questions)
- MBT/Most Supported · Dense Stimulus (5 gap questions)
- MBT/Most Supported · Conditional Conclusion (4 gap questions)
- MBT/Most Supported · Belief / Knowledge / Intent (5 gap questions)
- Flaw · Missing Link / Idea (9 gap questions)
- Flaw · 2-Speaker (3 gap questions)
- Flaw · Plausibility (3 gap questions)
- Flaw · Medical (4 gap questions)
- Flaw · Conditional Diagramming (4 gap questions)
- Flaw · Ruling Out Options (5 gap questions)
- Flaw · Conditional Conclusion (4 gap questions)
- Paradox · Plans / Recommendations (6 gap questions)
- Paradox · Science (12 gap questions)
- Paradox · Medical (3 gap questions)
- Paradox · Net Effect (3 gap questions)
- Paradox · Breadcrumbs (8 gap questions)
- Necessary Assumption · Sufficient vs. Necessary Flaw (6 gap questions)
- Necessary Assumption · Plausibility (11 gap questions)
- Necessary Assumption · Analogies (3 gap questions)
- Necessary Assumption · Net Effect (5 gap questions)
- Necessary Assumption · Math-y Stuff (3 gap questions)
- Necessary Assumption · Contrapositive Logic (5 gap questions)
- Necessary Assumption · Ruling Out Options (5 gap questions)
- Necessary Assumption · Predictions (6 gap questions)
- Necessary Assumption · Weighing Tradeoffs (4 gap questions)
- Necessary Assumption · Conditional Conclusion (4 gap questions)
- Necessary Assumption · Untriggered Conditional (3 gap questions)
- Principle-Strengthen · H (3 gap questions)
- Principle-Strengthen · Causal Difference-Maker (5 gap questions)
- Weaken · 2-Speaker (5 gap questions)
- Weaken · Timeframes (5 gap questions)
- Weaken · Net Effect (6 gap questions)
- Weaken · Anti-Causal (6 gap questions)
- Weaken · Predictions (3 gap questions)
- Weaken · Breadcrumbs (4 gap questions)
- Weaken · Focused on Evidence (4 gap questions)
- Method · Plans / Recommendations (15 gap questions)
- Method · Science (5 gap questions)
- Method · Alternatives (8 gap questions)
- Method · Sufficient vs. Necessary Flaw (3 gap questions)
- Method · Medical (3 gap questions)
- Method · Contrapositive Logic (3 gap questions)
- Method · Belief / Knowledge / Intent (4 gap questions)
- Parallel · Plans / Recommendations (4 gap questions)
- Parallel · Sufficient vs. Necessary Flaw (4 gap questions)
- Parallel · Contrapositive Logic (4 gap questions)
- Parallel · Ruling Out Options (3 gap questions)
- Parallel Flaw · Plans / Recommendations (7 gap questions)
- Parallel Flaw · Argue the Anti-Conclusion (3 gap questions)
- Strengthen · Science (6 gap questions)
- Strengthen · Weighing Tradeoffs (3 gap questions)
- Strengthen · Sampling (3 gap questions)
- Agree/Disagree · Explain Curious Fact (3 gap questions)
- Agree/Disagree · Timeframes (3 gap questions)
- Main Conclusion · Plans / Recommendations (3 gap questions)
- Main Conclusion · Science (4 gap questions)
- Main Conclusion · Timeframes (3 gap questions)
- Main Conclusion · Analogies (3 gap questions)
- Role · Important Pivot (4 gap questions)
- Role · First Sentence Conclusion (5 gap questions)
- Sufficient Assumption · First Sentence Conclusion (3 gap questions)

Features with no golden pick at all:

- Refute a Conditional (14 gap questions; 1 shortlisted)

