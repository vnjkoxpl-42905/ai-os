---
type: survey
subject: LR choice-note problems
updated: 2026-09-27
status: read-only survey
---

# Choice Note problems confirmed by reading

Each row was checked against the stimulus and the answer choices in the question bank (`lsatu-wt-parser/public/data`), since the DB rows do not store the choices. Companion to [[revamp-list]].

**Key conflicts:** none found. The scan flagged 16 notes that seemed to call a wrong letter correct; every one was a "Yes, the author assumes this, but..." opening. No explanation argues for a letter other than `correct_choice`. Two items point students the wrong way without contradicting the key: PT158-S4-Q22 (the breakdown predicts wrong choice D) and PT108-S3-Q6 (the notes belong to a different question; see side-issues).

**Popular traps:** the DB has no answer-choice percentages, and the local markdown that does was out of scope, so "verdict-only note on the popular trap" could not be tested directly. What can be said: 577 explanations have at least one wrong-answer note under 15 words or a bare "not relevant" / "out of scope" verdict (`verdict_only` column in `revamp-inventory.csv` (in this folder)), and in the 100 Weak items that is the typical note.

## Misquotes, and notes written for a different question (9)

| Question | Type | Diff | Choice | Problem | Quote or detail |
|---|---|---|---|---|---|
| PT105-S4-Q14 | Necessary Assumption | 4 | D (correct) | misquote | "Choice (D) states that upper-income citizens could use the money"; D says "would use". |
| PT108-S3-Q6 | Paradox | 4 | all | wrong question | All five notes (predators, anglers, cooler water) answer a different question from the official one (algae increase; choices about detergents, temperature, oxygen). |
| PT137-S3-Q25 | Agree/Disagree | 2 | breakdown | wrong question | Evaluate: "Denise and Reshmi agree that people decide whether to commit a crime." |
| PT137-S4-Q15 | MBT/Most Supported | 4 | B | misquote | Note: "will worsen soil damage"; choice says "worsen soil drainage". |
| PT158-S2-Q22 | Parallel Flaw | 4 | D | misquote | Describes D as "not in the town's best interest to use the land for recreation"; D is about developing the other borders. |
| PT158-S3-Q2 | Strengthen | 1 | D | misquote | Note is about students who "can effectively combine knowledge"; D says they "can effectively solve many problems". (Also found in the 2026-09-26 survey.) |
| PT158-S3-Q9 | Weaken | 4 | C | misquote | Treats "negligible price increases for consumers" as "negligible additional costs to drug companies". |
| PT158-S3-Q13 | Necessary Assumption | 5 | E | misquote | Argues against "will not help patients address any difficulties they have in their relationships", not in E. |
| PT158-S3-Q17 | Principle-Conform | 5 | A, B, C, D | misquote | Notes describe choices that do not exist: "(2) enjoy learning math", "(2) have customers recommend the product", "(2) borrowers to return books in good condition", "(2) its employees to start working on Saturdays". |

## Wrong logic, wrong speakers, contradictions and outside facts (47)

| Question | Type | Diff | Choice | Problem | Quote or detail |
|---|---|---|---|---|---|
| PT112-S1-Q9 | Paradox | 4 | B (correct) | slip | "close to being 3 mg iron per capita" (per calorie); "raising" for raisins. |
| PT116-S2-Q8 | Strengthen | 3 | C | hedged logic | "And it almost might suggest to us that prison terms are currently too lax to be a deterrent, but raising them might work." |
| PT116-S3-Q6 | Agree/Disagree | 3 | C | wrong logic | "Speaker two definitely agrees"; Maria never says the stock market provides reliable income. |
| PT123-S3-Q7 | Agree/Disagree | 2 | A | wrong logic | "What is desirable is not discussed by neither Antonio nor Marla." Antonio says moderation costs "the joy of spontaneity". |
| PT124-S3-Q3 | Main Conclusion | 2 | D | mislabel | "This applies the opposing point..."; the point is the author's own concession. |
| PT127-S2-Q8 | Weaken | 4 | A | wrong logic | "Other boulders are not relevant to the argument." A is about how far glaciers carry boulders, which bears on "hundreds of miles". |
| PT127-S2-Q8 | Weaken | 4 | C | thin / pasted | Same note as B; never says a northern source is consistent with a southward glacier. |
| PT127-S3-Q5 | Main Conclusion | 2 | A | wrong logic | "This is evidence that supports the argument's main point." A overstates "avoid unnecessary use" as eliminate all use. |
| PT130-S1-Q13 | Main Conclusion | 5 | E | misses the reason | Note restates B instead of naming E's shift to "one will always have curiosity". |
| PT130-S1-Q24 | Weaken | 5 | A | self-contradiction | Says A's bears "didn't come from other parts of the valley", then that A "doesn't clarify" where they came from. |
| PT131-S3-Q11 | Strengthen | 2 | C | wrong logic | "This supports the opposing point that scholars and scientists find research libraries more convenient than public libraries." |
| PT131-S3-Q17 | Paradox | 4 | E | pasted | Identical to the C note. |
| PT132-S2-Q3 | Strengthen | 2 | A | wrong logic | "Although medication M can be produced in liquid form, the company developing M does not have soft-gel manufacturing technology." |
| PT132-S2-Q3 | Strengthen | 2 | B (correct) | diagram slip | Diagram reads "~PT" while the note says M has an unpleasant taste. |
| PT132-S2-Q6 | MBT/Most Supported | 2 | D | wrong logic / misstatement | Note: "People who wish to limit their caffeine intake are out of scope"; choice D is about people who wish to eliminate it. |
| PT132-S2-Q15 | Sufficient Assumption | 5 | B (correct) | loose logic | Says B "triggers the rule"; B denies the necessary condition. |
| PT133-S1-Q9 | MBT/Most Supported | 2 | A | wrong logic | "The statements do not suggest that increasing the number of transistors... led to doubling the computing speed" (they do, via "hence"); A fails on "only". |
| PT133-S1-Q20 | MBT/Most Supported | 4 | D | garbled diagram / wrong logic | Diagram concludes "down CL -> up TC"; the chain gives down CL -> down TC, and D reverses it. |
| PT133-S2-Q19 | MBT/Most Supported | 3 | A | wrong logic | Cites the third statement (typos in modern works) to judge a spelling correction in an older work. |
| PT133-S2-Q19 | MBT/Most Supported | 3 | C | wrong logic | "This negates the first statement"; C fails because the stimulus says "may" modernize when frequent, not "should" when it interferes. |
| PT133-S3-Q4 | Agree/Disagree | 1 | E | wrong speakers | "Neither Talbert nor Sklar would agree with this statement." The speakers are Sam and Meli. |
| PT133-S3-Q10 | Main Conclusion | 2 | B | unsupported claim | "it does not attempt to blur people's ability to distinguish between wants and needs" |
| PT134-S1-Q1 | Main Conclusion | 1 | B | pasted / wrong | "Advisable is not the same as, nor the equivalent of, necessary." belongs to A only. |
| PT134-S2-Q17 | Sufficient Assumption | 4 | A | wrong logic | Calls A a negation of the premise; A is about spontaneous people being liked, not a negation. |
| PT134-S3-Q3 | MBT/Most Supported | 1 | A | wrong logic | "it's more likely that older whales would be more able to tolerate engine noise"; speculation, not the reason A is unsupported. |
| PT134-S3-Q7 | Agree/Disagree | 2 | A | questionable | "Neither Tanner nor Saldana would agree with this statement"; Saldana's view arguably supports A. |
| PT134-S3-Q26 | Sufficient Assumption | 5 | B | misses the reason | "This negates the argument's conclusion." |
| PT135-S2-Q1 | Principle-Conform | 1 | D (correct) | slip in diagram | "(Display -> Damage) -> Display" should end in ~Display. |
| PT135-S2-Q17 | Role | 5 | C | wrong logic | "The author concedes this point and does not attempt to refute it." |
| PT135-S4-Q6 | MBT/Most Supported | 2 | C | misses the reason | Never names the "in any way other than" overreach. |
| PT135-S4-Q25 | Agree/Disagree | 2 | A | pasted from another question | "Neither Samuel nor Tova address a general trend of modern life." The speakers are Lutsina and Priscilla. |
| PT136-S4-Q26 | Main Conclusion | 3 | E | contradictory | Note says a similar point is a premise, then "This however suggests that human language did begin after..." |
| PT140-S2-Q14 | MBT/Most Supported | 5 | E | misses the reason | "This reverses the relationship MD -> EP"; E fails on "Only epic poetry". |
| PT142-S2-Q9 | Main Conclusion | 3 | B | questionable logic | "This follows from the musicologist's evidence but is not stated." |
| PT143-S4-Q18 | Agree/Disagree | 2 | breakdown | wrong speakers | Table headed "Graham / Adelaide"; Evaluate says "better off as democracies" (should be autocracies). |
| PT148-S3-Q8 | Sufficient Assumption | 2 | A | wrong logic | "This supports the premise that players often control... detailed human figures." |
| PT148-S3-Q19 | Agree/Disagree | 3 | A, B, E | dangling reference / pasted | "As we analyzed, Pankaj makes no statements about the government at all." There is no analysis in the breakdown (none exists). |
| PT151-S2-Q18 | Strengthen | 5 | B | wrong logic | "Drought-resistant surrounding grasses cut against, not for, the termite hypothesis." B rules out drought as a rival cause. |
| PT157-S3-Q25 | Weaken | 5 | D | self-contradiction | Says D "muddies the distinction", then "this actually supports the argument's conclusion". |
| PT158-S2-Q16 | Paradox | 4 | C (correct) | outside facts | Justifies C with Plato's family wealth and Philip of Macedon, not in the stimulus. (From the 2026-09-26 survey.) |
| PT158-S2-Q18 | Flaw | 5 | A | wrong logic | Argues against a claim A does not make. (From the 2026-09-26 survey; not re-read.) |
| PT158-S2-Q22 | Parallel Flaw | 4 | A | wrong logic | Calls A valid; A ignores the third route to office ("special qualifications"). |
| PT158-S2-Q22 | Parallel Flaw | 4 | B | wrong logic | Calls B valid and quotes a conclusion B does not have ("the plant will not thrive"). |
| PT158-S3-Q2 | Strengthen | 1 | A | tag vs note | A is tagged No Impact while its note argues A undermines the argument. (From the 2026-09-26 survey.) |
| PT158-S3-Q20 | MBT/Most Supported | 5 | D | wrong logic | "only primates have opposable thumbs, meaning ALL primates have them" (reversal of "only"). |
| PT158-S3-Q20 | MBT/Most Supported | 5 | C, E | outside facts | Cites owl monkeys and "many lemur species in the real world are nocturnal". |
| PT158-S4-Q22 | Weaken | 5 | D | conflicts with breakdown | Breakdown Goal predicts the contradiction objection; D note calls contradiction "a feature, not a bug". |

## Missing, placeholder, truncated or garbled notes (15)

| Question | Type | Diff | Choice | Problem | Quote or detail |
|---|---|---|---|---|---|
| PT105-S4-Q14 | Necessary Assumption | 4 | C, E | missing note | No notes. |
| PT123-S3-Q23 | Flaw | 3 | C | stray markup | Two literal "- paragraph" lines before the note text. |
| PT124-S3-Q19 | MBT/Most Supported | 2 | C | stray markup | Note carries a literal "- paragraph" line. |
| PT125-S2-Q11 | Main Conclusion | 2 | C | truncated | Note ends "This is evidence that supports the argument's". |
| PT133-S1-Q20 | MBT/Most Supported | 4 | C | garbled | Note restates a different conditional ("If traffic congestion increases...") and never says why C fails. |
| PT133-S2-Q25 | Strengthen | 2 | A, C | missing note | No note for A or for the correct answer C. |
| PT135-S2-Q14 | MBT/Most Supported | 2 | D | garbled | "Urban societies require SOC -> RC large-scale farming..." no reason given. |
| PT137-S3-Q12 | MBT/Most Supported | 3 | B | garbled | Note is broken into a one-word-per-line column beside a diagram. |
| PT138-S2-Q1 | MBT/Most Supported | 1 | B | garbled layout | One-word-per-line column. |
| PT138-S2-Q11 | Role | 3 | C | truncated | "This correctly describes the role of premise" |
| PT138-S3-Q4 | MBT/Most Supported | 2 | D | garbled | "While it's not that the most polluted cities improved their air quality, it could be true that all cities improved..." |
| PT138-S3-Q4 | MBT/Most Supported | 2 | C | grammar | "is not necessarily follow from the statements" |
| PT147-S4-Q3 | Paradox | 1 | D (correct) | placeholder | "(No authored tag or explanation for this choice.)" |
| PT147-S4-Q4 | Sufficient Assumption | 2 | A (correct) | placeholder | "(No authored tag or explanation for this choice.)" |
| PT156-S2-Q19 | Weaken | 2 | A | missing note | No note. |

## Verdict-only or pasted notes, confirmed by reading (55 questions)

Letters are the wrong-answer notes under about 15 words or bare verdicts ("This is a premise", "X is not relevant"). Where the column is "-", the notes are longer but pasted or label-only.

| Question | Type | Diff | Verdict-only notes |
|---|---|---|---|
| PT112-S4-Q24 | Weaken | 2 | EABC |
| PT122-S2-Q16 | Must Be False | 4 | - |
| PT123-S3-Q1 | Principle-Conform | 2 | EABD |
| PT123-S3-Q2 | Paradox | 1 | EBCD |
| PT123-S3-Q8 | Flaw | 1 | BCD |
| PT123-S3-Q12 | Main Conclusion | 3 | BCE |
| PT123-S3-Q14 | Principle-Conform | 2 | AB |
| PT123-S3-Q23 | Flaw | 3 | E |
| PT124-S1-Q4 | Main Conclusion | 2 | EBC |
| PT125-S2-Q11 | Main Conclusion | 2 | EAC |
| PT125-S4-Q11 | Main Conclusion | 4 | EABD |
| PT126-S1-Q2 | Necessary Assumption | 1 | EBCD |
| PT126-S1-Q18 | Main Conclusion | 4 | ABCD |
| PT126-S3-Q13 | Main Conclusion | 3 | EBC |
| PT126-S3-Q16 | MBT/Most Supported | 2 | EABD |
| PT127-S2-Q8 | Weaken | 4 | EABC |
| PT129-S1-Q4 | Main Conclusion | 1 | ABCD |
| PT130-S4-Q3 | Main Conclusion | 2 | EBD |
| PT131-S1-Q1 | Main Conclusion | 1 | EAB |
| PT131-S1-Q10 | Flaw | 3 | ABCD |
| PT131-S1-Q13 | Main Conclusion | 4 | ECD |
| PT131-S2-Q10 | Main Conclusion | 1 | BC |
| PT131-S3-Q9 | Main Conclusion | 1 | EABC |
| PT131-S3-Q17 | Paradox | 4 | D |
| PT132-S2-Q1 | MBT/Most Supported | 1 | EAB |
| PT132-S2-Q6 | MBT/Most Supported | 2 | DEBC |
| PT132-S2-Q10 | Main Conclusion | 2 | EACD |
| PT132-S4-Q1 | Main Conclusion | 1 | EAB |
| PT132-S4-Q12 | Main Conclusion | 2 | E |
| PT133-S1-Q9 | MBT/Most Supported | 2 | EBC |
| PT133-S1-Q13 | Main Conclusion | 2 | BCE |
| PT133-S3-Q10 | Main Conclusion | 2 | CD |
| PT134-S1-Q1 | Main Conclusion | 1 | ABDE |
| PT134-S2-Q1 | Main Conclusion | 1 | EAB |
| PT134-S2-Q4 | Strengthen | 1 | EDAB |
| PT134-S2-Q6 | Flaw | 2 | ABD |
| PT134-S2-Q11 | Paradox | 2 | EABD |
| PT135-S1-Q2 | Main Conclusion | 3 | BCD |
| PT135-S1-Q22 | Role | 3 | BD |
| PT135-S4-Q12 | Role | 3 | ABD |
| PT135-S4-Q14 | Main Conclusion | 3 | ABCD |
| PT136-S4-Q9 | Main Conclusion | 2 | ECD |
| PT137-S4-Q1 | Main Conclusion | 2 | ECD |
| PT138-S2-Q11 | Role | 3 | A |
| PT138-S2-Q17 | Main Conclusion | 2 | EDB |
| PT138-S2-Q22 | Role | 3 | ACD |
| PT138-S4-Q8 | Main Conclusion | 2 | BCD |
| PT139-S1-Q9 | Main Conclusion | 2 | BCDE |
| PT142-S2-Q9 | Main Conclusion | 3 | ABD |
| PT142-S2-Q13 | Sufficient Assumption | 3 | ECD |
| PT143-S4-Q16 | Main Conclusion | 2 | ABD |
| PT144-S3-Q18 | Main Conclusion | 2 | EBC |
| PT147-S4-Q4 | Sufficient Assumption | 2 | - |
| PT148-S3-Q19 | Agree/Disagree | 3 | ABE |
| PT148-S4-Q2 | Agree/Disagree | 1 | EAD |