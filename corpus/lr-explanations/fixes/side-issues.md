---
type: survey
subject: LR explanation data problems found during the revamp survey
updated: 2026-09-27
status: read-only survey; nothing was changed
---

# Side issues: data, labels and transcription

Found while surveying the DB dump (the read-only DB dump of 2026-09-26) against the question bank (`lsatu-wt-parser/public/data`). Companion to [[revamp-list]] and [[choice-note-issues]]. Ordered by how much a student could be misled.

## 1. Content that belongs to a different question

These show a student reasoning that does not match the question in front of them.

| Question | What is wrong | Evidence |
|---|---|---|
| PT108-S3-Q6 | The DB stimulus and all five notes are for a different question from the official one. | DB stimulus: the bass catch downstream of the power plant fell. Bank stimulus for PT108-S3-Q6: the algae population downstream *rose*, with choices about detergents, water temperature and dissolved oxygen. The notes talk about predators, anglers and cooler water, which match neither set of choices. DB key C and bank key C agree only by coincidence. Needs a source check before anything else. |
| PT137-S3-Q25 | Evaluate step is from another question. | "Denise and Reshmi agree that people decide whether to commit a crime." The speakers are Graham and Adelaide (chess computer). |
| PT143-S4-Q18 | Speaker table and Evaluate are from PT137-S3-Q25's template. | Table headed "Graham / Adelaide" (speakers are Wong and Tate); Evaluate says they disagree about countries being "better off as democracies" (the issue is autocracies). |
| PT135-S4-Q25 | A note is from another question. | "Neither Samuel nor Tova address a general trend of modern life." Speakers are Lutsina and Priscilla. |
| PT133-S3-Q4 | E note carries speakers from PT142-S2-Q7. | "Neither Talbert nor Sklar would agree with this statement." Speakers are Sam and Meli. |

## 2. Suspected mis-keys

No explanation argues for a letter other than `correct_choice`. The scan's 16 "key conflict" hits in notes were all "Yes, the author assumes this, but..." openings. Two related items:

- **PT158-S4-Q22** (Weaken, d5): the breakdown's Goal predicts the "different epistemologists contradict each other" objection, which is choice D. The key (E, "much debate as to which thinkers were epistemologists") is right, and the E note explains it well, but the breakdown steers students to D and the D note then calls contradiction "a feature, not a bug". Rewrite the breakdown.
- **Bank answer keys disagree with the DB on 18 questions**, all of them bank entries filed under a different PT, section or question number ("moved" in `revamp-inventory.csv` (in this folder)). I read five of these (PT116-S2-Q6, Q7, Q8; PT131-S3-Q16, Q17) and the DB key is correct in every case. So the bank's `correctAnswer` is wrong for these, not the DB. Anything that reads the bank's key (drills, analytics, the golden-survey inventory) would mis-grade them:

  PT101-S2-Q19 (DB E, bank D), PT101-S3-Q19 (D/E), PT113-S3-Q21 (C/A), PT113-S3-Q22 (D/A), PT113-S3-Q23 (B/A), PT113-S3-Q24 (E/A), PT116-S2-Q4 (B/C), PT116-S2-Q6 (E/B), PT116-S2-Q7 (C/D), PT116-S2-Q8 (C/E), PT119-S2-Q19 (B/E), PT119-S2-Q21 (A/C), PT119-S4-Q8 (A/C), PT129-S3-Q18 (B/D), PT129-S3-Q19 (D/A), PT131-S3-Q16 (E/C), PT131-S3-Q17 (A/E), PT148-S4-Q24 (E/A).

  Note PT113-S3-Q21 to Q24 all have bank key A, which looks like a placeholder.

## 3. Bank alignment

- **PT119-S2-Q19** is matched to bank entry PT103-S2-Q24, which is a different question on the same topic (musical intervals; the bank one is about an isolated tribe's preferences). Its difficulty and features in `revamp-inventory.csv` (in this folder) are borrowed from the wrong question.
- **PT101-S3-Q1**: the bank stimulus differs from the DB's in both speakers' text (bank: election boards hiring extra help; Sharon concludes "apathy"). The DB text reads like the real question. The bank's choices for this question may not match either.
- 110 explained questions have no bank entry at all, so there is no difficulty and no answer-choice text on disk to check notes against (for example PT119-S2-Q12, PT119-S3-Q3, PT131-S2-Q5).

## 4. Empty or partial explanations

| Problem | Count | Questions |
|---|---|---|
| Explanation row exists with no steps and no notes | 2 | PT122-S1-Q9, PT147-S4-Q6 |
| Breakdown only, no choice notes | 16 | PT102-S3-Q14, PT117-S3-Q2, PT117-S3-Q8, PT117-S4-Q3, PT117-S4-Q5, PT118-S1-Q9, PT118-S3-Q8, PT119-S2-Q7, PT119-S2-Q12, PT119-S2-Q24, PT119-S3-Q3, PT119-S3-Q20, PT119-S4-Q2, PT120-S1-Q23, PT120-S1-Q26, PT120-S4-Q17 |
| Some notes missing | 8 | PT105-S4-Q14 (3 of 5), PT133-S2-Q25 (3, including the correct answer), PT107-S3-Q7, PT108-S3-Q16, PT111-S1-Q22, PT119-S2-Q15, PT146-S3-Q11, PT156-S2-Q19 (4 each) |
| Placeholder text as a note | 2 | PT147-S4-Q4 A (correct), PT147-S4-Q3 D (correct): "(No authored tag or explanation for this choice.)" |
| Notes but no Argument Breakdown | 224 | Heaviest in PT148 (33), PT111 (14), PT122 (11), PT116 (10), PT102 (9). |
| Question has no explanation at all | 352 | Known (`is_explained = false`); the 772-gap plan covers these. |

Several breakdown-only rows (PT117-S3-Q8, PT118-S1-Q9, PT119-S2-Q12, PT119-S3-Q3, PT119-S2-Q24, PT119-S4-Q2, PT120-S1-Q23, PT120-S4-Q17) are written in a different register from the LSAT Lab text: bracketed labels like "Rossi's argument structure", em-dashes, "i.e." glosses. They look like later fill-ins written without the answer choices. Two of them (PT119-S2-Q12, PT119-S3-Q3) have no bank entry, so the choices may never have been available to whoever wrote them.

## 5. Transcription damage

| Damage | Count | Examples |
|---|---|---|
| Margin diagrams spliced into sentences | about 192 rows, almost all PT123-140 voice-B | PT132-S2-Q6 "Listing exact caffeine LCC -> ELC content would make it easier"; PT137-S4-Q15; PT135-S2-Q14 |
| Notes broken into one-to-four-word lines (a diagram column that lost its table) | about 98 rows | PT137-S3-Q12 B, PT130-S1-Q13, PT135-S1-Q25 D, PT138-S2-Q1 B |
| Two-speaker table flattened into interleaved prose | 12 | PT123-S3-Q3, PT123-S3-Q7, PT131-S1-Q23, PT131-S2-Q2, PT133-S3-Q4, PT134-S3-Q5, PT134-S3-Q7, PT135-S4-Q25, PT136-S4-Q19, PT137-S3-Q25, PT139-S1-Q2, PT140-S2-Q5 |
| Literal "- paragraph" lines | 30 rows | PT123-S3-Q12 (between every step), PT124-S3-Q19, PT123-S3-Q23 |
| Spaces lost around bold or italic words | at least 30 rows | PT106-S3-Q24 "aCurious", "islesslikely"; PT104-S4-Q14 "publishedbeforethe"; PT126-S1-Q12 "HQ -> EEquality"; PT126-S3-Q15 "askTheordore" |
| Truncated mid-sentence | spot-found | PT125-S2-Q11 C note ("supports the argument's"); PT134-S3-Q3 Given step; PT138-S2-Q11 C note; PT158-S4-Q3 Evidence step |
| Unbalanced `**` | 8 rows | PT101-S2-Q1, PT101-S2-Q21, PT102-S3-Q17 |

## 6. LSAT Lab leftovers

Text that refers to things students on LSAT U cannot see:

- "try this one" with no link: PT102-S2-Q20, PT139-S1-Q5, PT140-S3-Q18, PT158-S4-Q25.
- "click on the bold if you'd like to see other examples": PT140-S3-Q7.
- "watch the class recording, via the play button on the highlighter toolbar": PT132-S4-Q18.
- "Welcome to Test 89, everyone": PT155-S4-Q15 (LSAT Lab's numbering).
- "the sentence ends here with no continuation on the LSAT Lab page": PT143-S4-Q9 (a transcription note left in student text).
- "As we analyzed" with no analysis present (the breakdown is missing): PT148-S3-Q19 A, B, E.

## 7. Question-type labels

`lr_questions.question_type` has **82 distinct values** for about 18 real types: the same type appears as "Must be True", "Must Be True", "Must Be True (Inference)", "Must be True (EXCEPT)"; "Paradox EXCEPT" and "Paradox (EXCEPT)"; 30-odd "(type inferred)" suffixes. Anything that groups by this column (drill filters, analytics) will split types.

Labels that are plainly wrong for the stem:

| Question | Label | Stem says |
|---|---|---|
| PT108-S2-Q13 | Strengthen | "most strongly supports the claim that Ramona and Martin agree" (Agree/Disagree) |
| PT108-S3-Q20 | Strengthen | "provide the most support for holding that they disagree" (Agree/Disagree) |
| PT109-S4-Q14 | Strengthen | "The statements above, if true, most strongly support which one of the following" (Most Supported) |
| PT125-S4-Q12 | Parallel Flaw | "which one of the following is most supported by them" (Most Supported) |
| PT125-S4-Q16 | Most Supported | "most vulnerable to criticism" (Flaw) |
| PT113-S4-Q12, PT128-S2-Q3 | Necessary Assumption | "is flawed because..." (Flaw) |
| PT125-S4-Q14, PT128-S3-Q12, PT151-S2-Q1, PT151-S3-Q18 | Weaken | "vulnerable to criticism / flawed because" (Flaw) |
| PT107-S3-Q6 | Flaw | "a questionable assumption on which the argument relies" (Necessary Assumption) |
| PT132-S2-Q1 | Most Supported | "principle best illustrated" (Principle-Conform) |

## 8. Smaller slips spotted while reading

- PT126-S1-Q2 "This fail to connect"; PT127-S2-Q8 "bolder"; PT127-S3-Q19 "Eric" for Erich; PT148-S3-Q19 "Panjak"; PT131-S2-Q5 "synthensized alphahyrdoxy"; PT124-S1-Q12 "lessons" for lessens; PT135-S4-Q6 copies the stimulus as "over- nitrified" (it says overnutrified); PT112-S1-Q9 "raising" for raisins and "per capita" for per calorie; PT107-S3-Q6 "is every badly weakened".
- The question bank carries a "Games-y LR" feature tag (already noted 2026-09-26); worth renaming given the no-Logic-Games rule for student copy.
