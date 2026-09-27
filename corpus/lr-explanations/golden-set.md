---
type: teaching-notes
subject: Golden set of LR Standard explanations
updated: 2026-09-26
status: in use; PT106-S2-Q26 added at Joshua's request 2026-09-26, no swaps requested
---

# LR golden set: the 51 explanations new ones are modelled on

The model set for writing the 772 missing LR explanations (plan: [[../../brainstorms/2026-09-26-lr-explanation-coverage]]). Every pick is an existing LSAT Lab explanation in the LSAT U database (the database, not the local markdown, is the source of truth), read in full and scored against a rubric built by comparing strong and loose explanations. They are references, not edits: nothing here changes an existing explanation.

- Full rubric, strong-vs-loose comparison, step structure per type, voice notes: [[golden-set-observations]]
- All 80 candidates, scores and the family x feature coverage grid: [[golden-set-candidates]]
- Joshua's reference sheets (added 2026-09-27): `C:\Users\Joshu\OneDrive\Desktop\2024-Updated-LR-cram-sheet.pdf` and `C:\Users\Joshu\Downloads\LR GUIDELINE QUESTION TYPE AND REASONING TYPE.pdf` (famous flaw names, per-type reading and prephrase goals, trap names).
- Nearest-neighbor scan: `system/scripts/lr-explanations/neighbors.py` ranks every complete DB explanation by type, shared features, stimulus shape and quality for a given question; `show.py SLOT ...` prints one in full. Each draft names the neighbors it was modelled on.

## What separates a top-tier explanation from a loose one

Length does not. These do:

1. **The Evaluate step argues with the argument** ("How could we argue the opposite?") instead of restating it.
2. **The Goal names the answer** it expects, not just the task.
3. **Every wrong answer gets a reason and usually a test.** Loose ones average one verdict-only note per question ("This is irrelevant").
4. **The most popular trap gets the most attention.**
5. **The correct-answer note teaches the move**, so a student can repeat it on the next question, not just confirm the key.

Complete (full breakdown plus all five Choice Notes) is a gate, not a score.

## Do not copy from the corpus

Joshua, 2026-09-26: a personal jab at the test is fine; it makes the voice personal.


- The PT157/158 explicit-Standard register: heavy em-dashes and formulaic phrasing. None of those made the set.
- Typos and slips carried in the source (flagged in the table).

## The set

Difficulty 1-5. Mix: 27 easy, 13 medium, 11 hard, which tracks the gap list (480 of the 772 are difficulty 1-2).

| # | Question | Family | Diff | Features | Why it is here | Weakness |
|---|---|---|---|---|---|---|
| 1 | PT107-S3-Q5 | MBT/Most Supported | 1 | Conditional Diagramming; Causal Chains; Science | Easy inference built on a causal/conditional chain. States the general move ("if X leads to Y and Y leads to Z, infer X leads to Z"), predicts the chained answer, and rejects B as a sufficient condition misread as necessary and E as reversed causation. | The chain diagram is inline text and loses its layout. |
| 2 | PT145-S2-Q23 | MBT/Most Supported | 2 | Sufficient vs. Necessary Flaw; Contrapositive Logic; Quantifiers | Explains which statement commands attention (a lone Most claim is inert, the conditional is not), contraposes, and diagrams the inference before the choices. Wrong answers are refuted with concrete counterexample numbers (100 Velyena mines vs 11 gold mines), the clearest quantifier teaching in the corpus. | Correct-answer note says "have violated" where it means "have never violated". (fidelity: slip) |
| 3 | PT104-S1-Q3 | MBT/Most Supported | 3 | Explain Curious Fact; Important Pivot; Alternatives; Causal Difference-Maker; Rebuttals | Inference that ends on a rebuttal: frames the two competing causal explanations (size vs age) and predicts a safely worded answer that holds age constant. B and C are shown to misplace which variable is held constant. | Goal step spends a paragraph on facts vs opinions before the prediction. |
| 4 | PT142-S4-Q7 | MBT/Most Supported | 3 | Logical Completion | Logical completion: treats "assuming X" as one more premise, chains stress to less pain, and predicts a weakly worded causal answer. Each wrong answer is shown to over-reach (usually, surgery, reversed causation). | Folk-remedy aside is longer than needed. |
| 5 | PT143-S1-Q13 | MBT/Most Supported | 5 | Important Pivot | Names the pattern ("Reconcile the Pivot") and predicts a moderately worded answer, including what the wrong answers will overdo. Eliminations are grounded: counterfactual speculation (A, D) and right direction but too far ("sketchy, not worthless"). | A and D notes are near-identical text. |
| 6 | PT151-S2-Q3 | Flaw | 1 | Abstract Answers; Argue the Anti-Conclusion; Causal Chains; Focused on Evidence; Plans / Recommendations; Predictions | Easy abstract-answer Flaw on a causal chain (slippery slope). Each abstract answer is translated back into the argument ("was there a premise saying X was widely accepted?"), which is the move students need for abstract answer choices. | Goal admits it cannot narrow the objection; long for a d1. |
| 7 | PT102-S2-Q9 | Flaw | 2 | Explain Curious Fact; Alternatives; Anti-Causal; Argue the Anti-Conclusion | Uses the "Given that ... how could we argue that ..." frame to generate the right objection (the protection worked) before reading choices. Each famous-flaw distractor is defined in one line and checked against the argument. | None significant. |
| 8 | PT139-S4-Q18 | Flaw | 3 | Relative vs. Absolute; Math-y Stuff; Net Effect; Plans / Recommendations | Does the arithmetic (25% of $400 vs 13% of $1,000) to expose the relative vs absolute flaw, then states two acceptable targets. Every choice gets the stem-driven test: "fails to consider X" means ask whether X weakens; "presumes X" means ask whether X is necessary. | Long; B, C and E open with the same boilerplate sentence. |
| 9 | PT143-S3-Q18 | Flaw | 3 | Sufficient vs. Necessary Flaw; Contrapositive Logic; Plans / Recommendations; Untriggered Conditional | Untriggered conditional: shows the conclusion matches the rule outcome but the trigger was never established, then names the Intent vs Consequence flaw. Explains why the tempting Necessary-vs-Sufficient answer is wrong even though conditional logic is present. | Final diagram lost line breaks in transcription. |
| 10 | PT118-S3-Q13 | Flaw | 4 | Famous Flaws; Belief / Knowledge / Intent; Abstract Answers; Sampling | Splits a two-part conclusion and objects to each part, then names the opinion-vs-fact flaw. Abstract answers are each translated into the famous flaw they describe and tested against this argument. | None significant. |
| 11 | PT142-S4-Q22 | Flaw | 4 | Sufficient vs. Necessary Flaw; Famous Flaws | Diagrams the conditional, shows both illegal moves, identifies the one the author made, and predicts both the formal and the conversational phrasing of the right answer. Eliminations map "infers X merely from Y" onto conclusion and evidence and check the match. | Some wrong-answer notes define the famous flaw at length before rejecting it. |
| 12 | PT111-S4-Q4 | Paradox | 1 | Math-y Stuff | Math paradox: explains why math paradoxes are the exception where you should predict, then runs a 100-person example until only one fix is possible. B is shown to explain the opposite direction. | None significant. |
| 13 | PT151-S2-Q13 | Paradox | 2 | Causal Difference-Maker | States the expectation the fact violates, then says the fix must be tied to the online change or something that changed at the same time. Uses "No Distinction" crisply and explains why D provides a contemporaneous change that still does not explain the outcome. | None significant. |
| 14 | PT143-S1-Q6 | Paradox | 3 | (none) | Medium paradox with a clean prediction: the danger must fall on people who are not in the SUV. B is flagged for using outside knowledge; E is rewritten into the version that would have worked. | No bank features. |
| 15 | PT142-S4-Q6 | Necessary Assumption | 1 | Defender; Rebuttals; Timeframes | Easy model that says why a linking answer is less likely than a defender on a real-world argument, lists objections first, and negates the correct answer. Irrelevant-comparison traps are each named for what they compare. | None significant. |
| 16 | PT137-S3-Q11 | Necessary Assumption | 2 | Explain Curious Fact; Alternatives; Anti-Causal; Defender; Timeframes | Frames the gap as a riddle ("how could a stronger earlier wave have spared the old coral?") and predicts both a link and a defender. Every choice gets the negation test. | None significant. |
| 17 | PT107-S1-Q15 | Necessary Assumption | 3 | Missing Link / Idea; Argue the Anti-Conclusion; Assumes Difference; Defender; Dense Stimulus; Medical; New Concept in Conclusion; Science | Dense medical stimulus: first asks why the author thinks the condition is worse at altitude (misdiagnosis), then predicts the storyline the answer must support. D is flagged as an outside-knowledge trap and E as a misread of "can recover". | Correct-answer note is casual ("Yeah, I guess he was!"). |
| 18 | PT154-S1-Q18 | Necessary Assumption | 4 | Missing Link / Idea; Anti-Causal; Assumes Similarity | Names two precise gaps ("not necessary" read as "not helpful"; "mastered grammar" read as "learned the language"), with a Harvard/175 analogy for the first. Negation test applied to every choice. | A couple of typos. |
| 19 | PT138-S3-Q1 | Principle-Strengthen | 2 | Principles in Answers; Weighing Tradeoffs | Starts from "if premise, then conclusion", then recognizes that the right answer is a weighing-tradeoffs principle with no "should" in it, and explains why it still justifies the conclusion. | Correct-answer note is short. |
| 20 | PT138-S2-Q5 | Principle-Strengthen | 2 | Missing Link / Idea; Principles in Stimulus | Principle given in the stimulus: puts the judgment on the right side, identifies the one fact needed to trigger it, and predicts it word for word. B through E each fail the same trigger test. | B through E share one pasted opening. |
| 21 | PT155-S4-Q9 | Principle-Strengthen | 2 | Abstract Answers; First Sentence Conclusion; Missing Link / Idea; Anti-Causal; Intermediate Conclusions; Plans / Recommendations; Principles in Answers | Shows the answer may target the premise-to-intermediate-conclusion move rather than the main conclusion, with both predictions diagrammed. Abstract principles are matched by what they have the power to prove. | None significant. |
| 22 | PT151-S2-Q4 | Principle-Conform | 1 | Missing Link / Idea; Principles in Answers | Names the two ideas behind the engineer's reasoning (golden rule; put my money where my mouth is) and diagrams every answer as trigger → outcome, asking whether the stimulus establishes the trigger. | None significant. |
| 23 | PT135-S1-Q6 | Principle-Conform | 3 | Implicit Principles | Illustrated-principle question treated like a slogan-style parallel: states the principle as "you can’t be sure, so play it safe", then walks A and B element by element (potential wrong, uncertainty, cautious action). | C through E notes are brief. |
| 24 | PT121-S4-Q9 | Weaken | 2 | Explain Curious Fact; Alternatives; Medical | Study-to-causal-conclusion weaken: names the correlation, the two weakening routes, and ranks D (a real methodological flaw) below A because of what the study measured. | None significant. |
| 25 | PT153-S2-Q13 | Weaken | 2 | Analogies; Assumes Similarity | Standard analogy attack ("how are these two situations meaningfully different?"). The final note lines up all five answers as completions of "you shouldn't use a dictionary, because..." so the student sees why only B is a relevant difference. | None significant. |
| 26 | PT155-S1-Q19 | Weaken | 4 | Explain Curious Fact; Plausibility | Curious Fact / Alternate Explanation / Plausibility frame, plus the relative vs absolute shift between evidence and conclusion. C is killed with a precise distinction (producing technology is not relying on it). | E's analogy is heavier than it needs to be. |
| 27 | PT155-S1-Q23 | Weaken | 5 | Explain Curious Fact; EXCEPT; Science | Best EXCEPT model found. Two fill-in sentence frames ("Life did occur on Mars. The meteorite shows the pre-life ratio because...") that every weakener must complete, so the odd one out is obvious. | None significant. |
| 28 | PT133-S1-Q17 | Method | 2 | Analogies | Analogy method: names the shared principle behind the analogy and teaches "argues X by Y: X must match the conclusion, Y the evidence" to test every answer. | None significant. |
| 29 | PT144-S2-Q8 | Method | 2 | Explain Curious Fact; Ruling Out Options | Easy two-speaker method: frames the study as a curious fact, predicts "alternate explanation", and flags the recurring trap that a respondent never denies the evidence. | None significant. |
| 30 | PT147-S4-Q12 | Method | 5 | 2-Speaker; Math-y Stuff; Rebuttals | Works the proportionality with numbers (Haynes inspects 65% of items but causes 50% of returns). Flags that respondents almost never deny a stated premise. | B note is thin. |
| 31 | PT154-S1-Q10 | Parallel | 1 | (none) | Diagrams the dilemma (A → X, not A → X, so X) and diagrams every answer the same way, so structure mismatches are visible at a glance. | No bank features; formal house voice. |
| 32 | PT108-S2-Q16 | Parallel | 2 | Explain Curious Fact; Alternatives; Anti-Causal | Parallel on reverse causation: offers both an algebraic and a conversational model and shows how each wrong answer breaks one ingredient (weak correlation, wrong direction, one data point). | None significant. |
| 33 | PT155-S2-Q19 | Parallel | 3 | First Sentence Conclusion; Intermediate Conclusions; Timeframes | Non-formal parallel: says why not to diagram, strips the topic to a story ("even if it starts perfect, it drifts"), and uses conclusion strength for quick eliminations. | Short correct-answer note. |
| 34 | PT154-S2-Q10 | Parallel Flaw | 1 | Famous Flaws; Sampling; Quantifiers; Rebuttals | Sampling flaw explained with a covid and NBA-height analogy; says the personal-experience detail is not the flaw, the tiny sample is. C and D are shown to have the right feel plus an extra flaw. | None significant. |
| 35 | PT138-S2-Q25 | Parallel Flaw | 3 | Conditional Diagramming; Conditional Conclusion; Repetitive Answers | Conditional parallel flaw: builds the algebraic recipe (two premises with the same trigger, one reversed) and eliminates A, D and E on the trigger check alone. | Diagram text is inline. |
| 36 | PT146-S1-Q21 | Parallel Flaw | 5 | Conditional Diagramming; Quantifiers; Repetitive Answers | Most + most inference, with 11 soil types showing why splitting the conclusion in two is illegal. Makes the point that on formal parallel flaw you can match structure without fully diagnosing the flaw. | Final sentence of the E note is garbled. (fidelity: transcription) |
| 37 | PT128-S3-Q1 | Strengthen | 1 | Plausibility | Easy strengthen on a curious fact: says the most common plausibility booster is a cause-present/effect-present data point, predicts it, and the correct answer is exactly that. | Long for d1. |
| 38 | PT146-S2-Q13 | Strengthen | 3 | Explain Curious Fact; Medical; Plausibility; Timeframes | Names the "policy went into effect, then X happened" structure. The correct-answer note offers a second hypothetical correct answer (moisturizer sales), teaching the function, not just the key. | None significant. |
| 39 | PT101-S2-Q4 | Strengthen | 3 | Explain Curious Fact; Breadcrumbs; EXCEPT; Focused on Evidence; Plausibility | Strengthen EXCEPT: finds a coy conclusion, then shows two answers only work if you catch the breadcrumb in the first sentence (stress and weight gain). C fails on scope (nonsmokers). | None significant. |
| 40 | PT145-S4-Q2 | Agree/Disagree | 1 | 2-Speaker; Analogies | Claim-by-claim table: for each of Albert's claims, "does Yvonne disagree?" with a yes/no reason. Every answer is tested for an Agree position and a Disagree position. | None significant. |
| 41 | PT153-S2-Q9 | Agree/Disagree | 2 | 2-Speaker | Teaches that a speaker can agree with the conclusion but reject the reasoning (Lebron vs Jordan), which is exactly what the correct answer tests. Each wrong answer is checked for both positions. | None significant. |
| 42 | PT150-S3-Q15 | Agree/Disagree | 4 | 2-Speaker | Lays out claims and reactions, including implicit ones, and names the exact friction ("strongly supports" vs "sheer speculation"). Each wrong answer is tested for both speakers, with a polling analogy. | None significant. |
| 43 | PT139-S4-Q1 | Main Conclusion | 1 | First Sentence Conclusion; Important Pivot; Rebuttals | The three Main Conclusion reminders, plus "replace referential language with specifics" before matching. Each wrong answer is labeled by role (intermediate conclusion, premise, opposing position). | None significant. |
| 44 | PT103-S2-Q8 | Main Conclusion | 3 | Sufficient vs. Necessary Flaw; First Sentence Conclusion; Contrapositive Logic; Rebuttals | Separates main from intermediate conclusion when both sit in the first sentence ("because" marks the support). D is named as the last-claim trap. | None significant. |
| 45 | PT154-S2-Q20 | Main Conclusion | 4 | First Sentence Conclusion | Reading posture for Main Conclusion, a word-by-word synonym map from the first sentence to A, and a one-test elimination for B through E. | Italic-label layout (PT154); one odd word ("aloofly"). |
| 46 | PT149-S3-Q6 | Role | 2 | Plans / Recommendations; Rebuttals | Implicit rebuttal conclusion and the "90% first sentence or pivot" heuristic, including when it fails. E is eliminated from the "Therefore" direction alone. | Typo ("rub out faces"). (fidelity: slip) |
| 47 | PT119-S4-Q25 | Role | 3 | Abstract Answers; Intermediate Conclusions | Role of a concession: sorts claims into conclusion, support, opposing, neutral, and uses "although" to predict a qualifying role. | None significant. |
| 48 | PT146-S2-Q3 | Sufficient Assumption | 1 | Missing Link / Idea; New Concept in Conclusion | Missing-link subtraction for a new concept in the conclusion, with the contrapositive shown as an equally correct form and "unless = if not" taught in the correct note. | Formal house voice; no analogies. |
| 49 | PT116-S3-Q16 | Sufficient Assumption | 2 | Missing Link / Idea; Quantifiers | Quantified sufficient assumption: states what must be proven (at least one thing in both groups) and why a "some" statement combined with the "all" premise proves it. | C through E share a pasted opening. |
| 50 | PT141-S4-Q6 | Evaluate | 1 | Argue the Anti-Conclusion; Plans / Recommendations | Easy model: generate objections to the plan, then test each question by imagining answers to it ("whether we say two or two hundred, no effect"). | None significant. |
| 51 | PT106-S2-Q26 | Paradox | 5 | EXCEPT | Paradox EXCEPT: explains that three of the four working answers usually resolve the paradox one way and one works another, lists both routes (fewer bed fires but more deaths per fire; more fires of other kinds), then shows B only restates why bed fires are dangerous. Added 2026-09-26 to fill the hard and EXCEPT Paradox gaps. | Goal step is one long paragraph. |

## Where the set is thin

- **Refute a Conditional**: 14 gap questions, no strong exemplar anywhere in the corpus. The guide for it will lean on the conditional picks (#2, #9, #35, #44) and LSAT Hacks for context.
- **Paradox**: hard and EXCEPT now covered by #51 (PT106-S2-Q26).
- **Method on Plans / Recommendations** (15 gap questions) has no pick.
- Most other empty cells are topic features (Science, Medical) that do not change how an explanation is built, so they do not need their own model.
