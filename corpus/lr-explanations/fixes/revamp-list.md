---
type: survey
subject: LR explanations to revamp
updated: 2026-09-27
status: read-only survey; nothing in the database was changed
---

# LR explanations worth revamping

Source: the DB dump in the read-only DB dump of 2026-09-26: 3,419 explanations, `standard` where it exists, else `single`. Difficulty (1-5) comes from the question bank in `lsatu-wt-parser/public/data`; `?` means the bank has no entry for that question. The standard is [[../golden-set]] and [[../golden-set-observations]]. Every row with its score and flags: `revamp-inventory.csv` (in this folder) (columns `verdict`, `verdict_source`, `verdict_note` carry this list).

## Counts

| Severity | Items | Read in full | Listed by rule, not read |
|---|---|---|---|
| Revamp | 192 | 88 | 104 |
| Weak | 100 | 95 | 5 |
| Watch | 231 | 8 | 223 |
| **Total** | **523** | **191** | **332** |

- **Revamp**: fails as teaching or contains an error. Includes all 126 PT157/158 explicit-Standard rows. I read 25 of those; all 25 show the em-dash, padded register, and 9 also have a misquote, wrong logic, outside facts or a self-contradiction (8 of the 9 are PT158).
- **Weak**: complete or nearly so, but loose: role labels as notes ("This is a premise"), "not relevant" notes, no prediction. A student gets little from it.
- **Watch**: the teaching is sound but something mechanical is wrong: no breakdown, stray markup, LSAT Lab leftovers, a flattened table, a small slip.
- "Listed by rule" means the item was caught by an exact rule (PT157/158 explicit Standard, literal "- paragraph", zero breakdown steps, missing notes, a named LSAT Lab leftover) and not read. Everything else was read against the stimulus, the stem and the bank answer choices.

## How far to trust the scan

I read a random 30 from outside the top 150 (scores under 9.5). None needed a revamp. 6 were Weak, and all 6 scored 5 or more. 8 were Watch. 16 were fine. Every row scoring 6 or more was Weak or Watch. Of the 20 scoring under 3, 16 were fine and 4 had a small defect the scan missed (spaces lost around emphasis, "per capita" for "per calorie", a class-recording reference, stray markup). So the score ranks weakness well, over-rates "no breakdown" when the notes are good, and misses small transcription damage. The automatic misquote check was too noisy to use, because the house style quotes paraphrases; every misquote below was found by reading.

**Not yet read:** 136 more rows score between 7 and 9.5 and are not on this list. Going by the random check, most are Weak: voice-B notes that only name the role ("This is a premise"), concentrated in PT123-138. Sort `revamp-inventory.csv` (in this folder) by `score` to work through them.

## Revamp (192)

### Flaw (25)

| Question | Diff | Tags | Problem |
|---|---|---|---|
| PT102-S3-Q14 | 1 | no-notes | Breakdown only; all five choice notes missing. *(rule, not read)* |
| PT119-S2-Q24 | 3 | no-notes; emdash-heavy | Breakdown exists (em-dash heavy, different register) but all five choice notes are missing. |
| PT120-S1-Q23 | 3 | no-notes; emdash | Breakdown only; all five choice notes missing. |
| PT123-S3-Q23 | 3 | damage; verdict-only | Conclusion and Evaluate labels are fused into the Evidence step body; C note carries two "- paragraph" markup lines. |
| PT134-S2-Q6 | 2 | damage; verdict-only | C note is a broken diagram; A, B, D are "not relevant"; C (the near-miss reversal of E) gets no real explanation. |
| PT157-S2-Q9 | 3 | pt157-158-register | Explicit-Standard register (8.4 em-dashes per 1k words; wrong-answer notes average 83.5 words). *(rule, not read)* |
| PT157-S2-Q12 | 2 | pt157-158-register | Accurate, but every note is a 90-word em-dash paragraph restating "reverses the conditional". |
| PT157-S2-Q20 | 5 | pt157-158-register | Explicit-Standard register (6.3 em-dashes per 1k words; wrong-answer notes average 99.0 words). *(rule, not read)* |
| PT157-S2-Q25 | 4 | pt157-158-register | Explicit-Standard register (6.9 em-dashes per 1k words; wrong-answer notes average 91.2 words). *(rule, not read)* |
| PT157-S3-Q9 | 2 | pt157-158-register | Explicit-Standard register (7.8 em-dashes per 1k words; wrong-answer notes average 33.0 words). *(rule, not read)* |
| PT157-S3-Q12 | 5 | pt157-158-register | Explicit-Standard register (11.8 em-dashes per 1k words; wrong-answer notes average 39.0 words). *(rule, not read)* |
| PT157-S3-Q14 | 4 | pt157-158-register | Explicit-Standard register (8.5 em-dashes per 1k words; wrong-answer notes average 41.5 words). *(rule, not read)* |
| PT157-S3-Q17 | 3 | pt157-158-register | Explicit-Standard register (14.7 em-dashes per 1k words; wrong-answer notes average 31.5 words). *(rule, not read)* |
| PT158-S2-Q2 | 3 | pt157-158-register | Explicit-Standard register (7.7 em-dashes per 1k words; wrong-answer notes average 124.0 words). *(rule, not read)* |
| PT158-S2-Q10 | 5 | pt157-158-register | Explicit-Standard register (7.9 em-dashes per 1k words; wrong-answer notes average 101.0 words). *(rule, not read)* |
| PT158-S2-Q14 | 5 | pt157-158-register | Explicit-Standard register (6.1 em-dashes per 1k words; wrong-answer notes average 105.2 words). *(rule, not read)* |
| PT158-S2-Q18 | 5 | pt157-158-register; wrong-logic | A note argues against a claim A does not make. (Found in the 2026-09-26 survey; not re-read.) |
| PT158-S3-Q1 | 1 | pt157-158-register | Explicit-Standard register (10.2 em-dashes per 1k words; wrong-answer notes average 119.5 words). *(rule, not read)* |
| PT158-S3-Q4 | 3 | pt157-158-register | Explicit-Standard register (3.2 em-dashes per 1k words; wrong-answer notes average 113.5 words). *(rule, not read)* |
| PT158-S3-Q8 | 1 | pt157-158-register | Explicit-Standard register (6.8 em-dashes per 1k words; wrong-answer notes average 105.0 words). *(rule, not read)* |
| PT158-S4-Q2 | 2 | pt157-158-register | Explicit-Standard register (8.5 em-dashes per 1k words; wrong-answer notes average 114.5 words). *(rule, not read)* |
| PT158-S4-Q4 | 3 | pt157-158-register | Explicit-Standard register (8.5 em-dashes per 1k words; wrong-answer notes average 125.2 words). *(rule, not read)* |
| PT158-S4-Q6 | 4 | pt157-158-register | Explicit-Standard register (7.2 em-dashes per 1k words; wrong-answer notes average 124.0 words). *(rule, not read)* |
| PT158-S4-Q18 | 5 | pt157-158-register | Correct; padded. |
| PT158-S4-Q23 | 4 | pt157-158-register; prediction-miss | Notes right, but the breakdown never mentions the new garage, which is the whole answer. |

### MBT/Most Supported (37)

| Question | Diff | Tags | Problem |
|---|---|---|---|
| PT117-S4-Q3 | 3 | no-notes | Strong breakdown (worked numbers) but all five choice notes missing. |
| PT119-S2-Q7 | 2 | no-notes | Chain diagram in the breakdown; all five choice notes missing. |
| PT119-S2-Q12 | ? | no-notes; no-bank-match; emdash | Breakdown only, no choice notes, and no bank entry, so the choices are not on file anywhere we checked. |
| PT122-S1-Q9 | 3 | empty | Explanation row exists but has no steps and no choice notes. |
| PT124-S3-Q19 | 2 | damage; thin-notes | Stray "- paragraph" markup in C note; B and C notes identical; no statement of the "not all three" rule as a diagram. |
| PT125-S4-Q12 | 2 | label; thin-notes | DB type says Parallel Flaw; it is Most Supported. Correct note is "supported by the second statement". |
| PT126-S3-Q16 | 2 | no-breakdown; verdict-only | No breakdown; four wrong notes are all "X is not discussed in the statements". |
| PT130-S3-Q10 | 2 | no-breakdown; thin-correct-note | No breakdown or diagram on a conditional Must Be True; E note is "This follows from the first and third statements." |
| PT132-S2-Q1 | 1 | short-breakdown; verdict-only; label | Principle-illustration question filed as Most Supported; notes are one line; no statement of the principle to match. |
| PT132-S2-Q6 | 2 | damage; misstatement; verdict-only | Diagram margin text is spliced into the stimulus copy; D note says people who wish to "limit" are out of scope, but D is about people who wish to eliminate. |
| PT133-S1-Q9 | 2 | wrong-logic; verdict-only | A note says the statements do not link transistor count to speed, but the stimulus says speed doubled "hence" from transistors; A is wrong for "only effective way". |
| PT133-S1-Q20 | 4 | damage; wrong-logic | d4 conditional chain; C and D notes are garbled diagrams, and D's diagram concludes ~CL -> up TC, which is not what the chain yields. |
| PT133-S2-Q12 | 5 | thin-notes; no-prediction | d5 Most Supported answered with "supported by the second and third statements"; never explains the Winslow split. |
| PT133-S2-Q14 | 5 | thin-notes; no-prediction | d5 conditional inference; C note is one line ("rephrases the third statement") and never shows why "some can cease" does not make it nonaddictive. |
| PT133-S2-Q19 | 3 | wrong-logic; thin-notes | A note cites the modern-works typo rule for an older-works case; C note calls C a negation instead of naming may vs should. |
| PT134-S1-Q18 | 2 | no-breakdown; thin-correct-note | No breakdown on a conditional chain; correct note is a bare diagram; C note wanders into when the bridge was built. |
| PT134-S3-Q3 | 1 | damage; wrong-logic | Given step truncated mid-sentence; A note argues older whales probably tolerate noise better, which is speculation, not the reason A fails. |
| PT135-S2-Q14 | 2 | damage; wrong-logic | D note is a garbled diagram ("SOC -> RC") that never says why D fails; flattened diagrams in Given. |
| PT135-S4-Q6 | 2 | thin-notes; typo | Given step copies "over- nitrified"; C note never says the problem is C's "in any way other than". |
| PT137-S3-Q12 | 3 | no-breakdown; damage | No breakdown on a d3 conditional inference; B note is a one-word-per-line column; correct note diagram is garbled. |
| PT137-S4-Q15 | 4 | damage; misquote; thin-notes | Flattened diagram in Given; B note misquotes the choice ("worsen soil damage"); d4 with one-line notes. |
| PT157-S2-Q1 | 2 | pt157-158-register | Explicit-Standard register (6.4 em-dashes per 1k words; wrong-answer notes average 98.0 words). *(rule, not read)* |
| PT157-S2-Q3 | 2 | pt157-158-register | Explicit-Standard register (8.4 em-dashes per 1k words; wrong-answer notes average 77.5 words). *(rule, not read)* |
| PT157-S2-Q6 | 1 | pt157-158-register | Explicit-Standard register (5.5 em-dashes per 1k words; wrong-answer notes average 76.8 words). *(rule, not read)* |
| PT157-S2-Q7 | 3 | pt157-158-register | Explicit-Standard register (12.4 em-dashes per 1k words; wrong-answer notes average 79.2 words). *(rule, not read)* |
| PT157-S2-Q15 | 3 | pt157-158-register | Accurate; padded em-dash notes. |
| PT157-S2-Q19 | 5 | pt157-158-register | Correct; tight for this register. |
| PT157-S3-Q7 | 3 | pt157-158-register | Explicit-Standard register (0.0 em-dashes per 1k words; wrong-answer notes average 33.8 words). *(rule, not read)* |
| PT157-S3-Q21 | 5 | pt157-158-register | Explicit-Standard register (9.7 em-dashes per 1k words; wrong-answer notes average 77.2 words). *(rule, not read)* |
| PT157-S3-Q23 | 5 | pt157-158-register | Correct. |
| PT158-S2-Q4 | 3 | pt157-158-register | Explicit-Standard register (5.1 em-dashes per 1k words; wrong-answer notes average 80.0 words). *(rule, not read)* |
| PT158-S2-Q6 | 3 | pt157-158-register | Explicit-Standard register (3.0 em-dashes per 1k words; wrong-answer notes average 99.8 words). *(rule, not read)* |
| PT158-S2-Q8 | 3 | pt157-158-register | Explicit-Standard register (9.8 em-dashes per 1k words; wrong-answer notes average 87.0 words). *(rule, not read)* |
| PT158-S3-Q16 | 4 | pt157-158-register | Explicit-Standard register (4.2 em-dashes per 1k words; wrong-answer notes average 96.5 words). *(rule, not read)* |
| PT158-S3-Q20 | 5 | pt157-158-register; wrong-logic; outside-facts | D note reads "only primates have opposable thumbs" as "ALL primates have them" (a reversal); C and E notes cite real-world owl monkeys and nocturnal lemurs. |
| PT158-S3-Q23 | 5 | pt157-158-register | Explicit-Standard register (14.0 em-dashes per 1k words; wrong-answer notes average 89.2 words). *(rule, not read)* |
| PT158-S4-Q11 | 3 | pt157-158-register | Explicit-Standard register (10.9 em-dashes per 1k words; wrong-answer notes average 83.8 words). *(rule, not read)* |

### Necessary Assumption (16)

| Question | Diff | Tags | Problem |
|---|---|---|---|
| PT105-S4-Q14 | 4 | no-breakdown; missing-notes; misquote | No breakdown; no notes for C or E; D note misquotes D ("could use" for "would use") and reads as generic filler ("Option (A) is irrelevant"). |
| PT119-S3-Q20 | 3 | no-notes | Breakdown only; all five choice notes missing. *(rule, not read)* |
| PT126-S1-Q2 | 1 | verdict-only; thin-correct-note; no-prediction | One-line notes, no negation test on a Necessary Assumption; typo "This fail to connect". |
| PT147-S4-Q6 | 2 | empty | Explanation row exists but has no steps and no choice notes. |
| PT157-S2-Q24 | 4 | pt157-158-register | Correct; negation tests present; long. |
| PT157-S3-Q13 | 2 | pt157-158-register | Explicit-Standard register (5.6 em-dashes per 1k words; wrong-answer notes average 44.2 words). *(rule, not read)* |
| PT157-S3-Q20 | 4 | pt157-158-register | Explicit-Standard register (9.3 em-dashes per 1k words; wrong-answer notes average 76.5 words). *(rule, not read)* |
| PT158-S2-Q3 | 4 | pt157-158-register | Explicit-Standard register (6.4 em-dashes per 1k words; wrong-answer notes average 106.2 words). *(rule, not read)* |
| PT158-S2-Q11 | 3 | pt157-158-register | Explicit-Standard register (4.3 em-dashes per 1k words; wrong-answer notes average 95.0 words). *(rule, not read)* |
| PT158-S2-Q17 | 5 | pt157-158-register | Explicit-Standard register (6.4 em-dashes per 1k words; wrong-answer notes average 109.0 words). *(rule, not read)* |
| PT158-S2-Q19 | 5 | pt157-158-register | Explicit-Standard register (7.7 em-dashes per 1k words; wrong-answer notes average 108.5 words). *(rule, not read)* |
| PT158-S3-Q13 | 5 | pt157-158-register; misquote | E note argues against "will not help patients address any difficulties they have in their relationships", which is not in E; B note restates B loosely. |
| PT158-S3-Q15 | 3 | pt157-158-register | Explicit-Standard register (8.4 em-dashes per 1k words; wrong-answer notes average 103.0 words). *(rule, not read)* |
| PT158-S3-Q21 | 5 | pt157-158-register | Explicit-Standard register (6.0 em-dashes per 1k words; wrong-answer notes average 105.8 words). *(rule, not read)* |
| PT158-S4-Q7 | 3 | pt157-158-register | Explicit-Standard register (4.9 em-dashes per 1k words; wrong-answer notes average 120.8 words). *(rule, not read)* |
| PT158-S4-Q13 | 4 | pt157-158-register | Explicit-Standard register (11.7 em-dashes per 1k words; wrong-answer notes average 87.8 words). *(rule, not read)* |

### Weaken (20)

| Question | Diff | Tags | Problem |
|---|---|---|---|
| PT112-S4-Q24 | 2 | no-breakdown; verdict-only; thin-correct-note | No breakdown; every note is 5-10 words ("Says something good about voicemail") and E is never shown to strengthen rather than weaken. |
| PT117-S4-Q5 | 1 | no-notes | Good breakdown and Goal; all five choice notes missing. |
| PT127-S2-Q8 | 4 | wrong-logic; verdict-only | d4 Weaken; A is dismissed as "other boulders are not relevant" though it bears on distance; C (a source to the north) is treated like B with no word on why it would strengthen; "bolder" typo. |
| PT156-S2-Q19 | 2 | no-breakdown; missing-notes | No breakdown; no note for A; typos ("possiblitiy"). |
| PT157-S2-Q2 | 3 | pt157-158-register | Explicit-Standard register (4.8 em-dashes per 1k words; wrong-answer notes average 87.2 words). *(rule, not read)* |
| PT157-S2-Q4 | 2 | pt157-158-register | Explicit-Standard register (4.2 em-dashes per 1k words; wrong-answer notes average 82.5 words). *(rule, not read)* |
| PT157-S2-Q10 | 3 | pt157-158-register | Explicit-Standard register (5.1 em-dashes per 1k words; wrong-answer notes average 79.5 words). *(rule, not read)* |
| PT157-S3-Q6 | 2 | pt157-158-register | Explicit-Standard register (0.0 em-dashes per 1k words; wrong-answer notes average 57.8 words). *(rule, not read)* |
| PT157-S3-Q15 | 2 | pt157-158-register | Explicit-Standard register (8.5 em-dashes per 1k words; wrong-answer notes average 36.5 words). *(rule, not read)* |
| PT157-S3-Q25 | 5 | pt157-158-register; self-contradiction | D note argues it muddies the study, then says it supports the conclusion. |
| PT158-S2-Q7 | 4 | pt157-158-register | Explicit-Standard register (6.0 em-dashes per 1k words; wrong-answer notes average 94.0 words). *(rule, not read)* |
| PT158-S2-Q21 | 5 | pt157-158-register | Explicit-Standard register (0.0 em-dashes per 1k words; wrong-answer notes average 81.2 words). *(rule, not read)* |
| PT158-S3-Q5 | 2 | pt157-158-register | Correct; padded. |
| PT158-S3-Q7 | 1 | pt157-158-register | Explicit-Standard register (8.3 em-dashes per 1k words; wrong-answer notes average 114.0 words). *(rule, not read)* |
| PT158-S3-Q9 | 4 | pt157-158-register; misstatement | C note turns "negligible price increases for consumers" into "negligible additional costs to drug companies". |
| PT158-S3-Q24 | 2 | pt157-158-register | Explicit-Standard register (6.2 em-dashes per 1k words; wrong-answer notes average 101.5 words). *(rule, not read)* |
| PT158-S4-Q1 | 3 | pt157-158-register | Explicit-Standard register (3.8 em-dashes per 1k words; wrong-answer notes average 105.8 words). *(rule, not read)* |
| PT158-S4-Q16 | 5 | pt157-158-register | Correct; Mt. Whitney analogy is good. |
| PT158-S4-Q22 | 5 | pt157-158-register; breakdown-vs-notes conflict | Breakdown Goal predicts the contradiction objection (choice D); the D note then calls contradictions "a feature". Key E is right; the breakdown points students at the wrong answer. |
| PT158-S4-Q24 | 4 | pt157-158-register | Explicit-Standard register (6.6 em-dashes per 1k words; wrong-answer notes average 99.8 words). *(rule, not read)* |

### Strengthen (14)

| Question | Diff | Tags | Problem |
|---|---|---|---|
| PT116-S2-Q8 | 3 | no-breakdown; key-check | No breakdown on a Strengthen EXCEPT; C note hedges ("it almost might suggest"). Key C is right; bank says E (see side issues). |
| PT120-S1-Q26 | 5 | no-notes | Breakdown only; all five choice notes missing. *(rule, not read)* |
| PT132-S2-Q3 | 2 | label; wrong-logic | Assumption question filed as Strengthen; A note is a non sequitur (liquid form answered with soft-gel); B note's diagram reads "~PT" for "PT". |
| PT133-S2-Q25 | 2 | missing-notes | No notes for A or for the correct answer C. |
| PT151-S2-Q18 | 5 | thin-notes; wrong-logic; emdash | d5 Strengthen in 115 words; B note says drought-resistant grass cuts against termites, when it rules out drought as a rival cause. |
| PT157-S2-Q13 | 4 | pt157-158-register | Explicit-Standard register (4.8 em-dashes per 1k words; wrong-answer notes average 91.8 words). *(rule, not read)* |
| PT157-S3-Q1 | 1 | pt157-158-register | Explicit-Standard register (6.9 em-dashes per 1k words; wrong-answer notes average 93.0 words). *(rule, not read)* |
| PT157-S3-Q10 | 1 | pt157-158-register | Explicit-Standard register (9.0 em-dashes per 1k words; wrong-answer notes average 29.2 words). *(rule, not read)* |
| PT158-S2-Q15 | 4 | pt157-158-register | Explicit-Standard register (4.0 em-dashes per 1k words; wrong-answer notes average 111.5 words). *(rule, not read)* |
| PT158-S3-Q2 | 1 | pt157-158-register; misquote; tag-conflict | D note describes a different choice ("can effectively combine knowledge"); A is tagged No Impact while its note argues A undermines the argument. (Found in the 2026-09-26 survey; re-read here.) |
| PT158-S3-Q11 | 3 | pt157-158-register | Explicit-Standard register (2.6 em-dashes per 1k words; wrong-answer notes average 108.0 words). *(rule, not read)* |
| PT158-S4-Q14 | 4 | pt157-158-register | Explicit-Standard register (10.7 em-dashes per 1k words; wrong-answer notes average 84.8 words). *(rule, not read)* |
| PT158-S4-Q15 | 5 | pt157-158-register | Correct; padded. |
| PT158-S4-Q21 | 5 | pt157-158-register | Explicit-Standard register (6.6 em-dashes per 1k words; wrong-answer notes average 103.8 words). *(rule, not read)* |

### Paradox (12)

| Question | Diff | Tags | Problem |
|---|---|---|---|
| PT108-S3-Q6 | 4 | stimulus-mismatch | DB stimulus (bass catch fell) and every note (predators, anglers) do not match the official question in the bank (algae rose; choices about detergents, temperature, oxygen). The whole item is for a different question. |
| PT117-S3-Q2 | 2 | no-notes | Good breakdown and Goal, but all five choice notes are missing. |
| PT123-S3-Q2 | 1 | verdict-only; pasted-notes | EXCEPT Paradox: B-E share one pasted sentence; no prediction of the two routes (more usage, higher rates). |
| PT147-S4-Q3 | 1 | no-breakdown; placeholder | No breakdown; correct note is the placeholder "(No authored tag or explanation for this choice.)". |
| PT157-S2-Q11 | 3 | pt157-158-register | Explicit-Standard register (10.8 em-dashes per 1k words; wrong-answer notes average 84.5 words). *(rule, not read)* |
| PT157-S3-Q18 | 5 | pt157-158-register | Correct; shorter than most. |
| PT158-S2-Q5 | 3 | pt157-158-register | Explicit-Standard register (3.8 em-dashes per 1k words; wrong-answer notes average 94.8 words). *(rule, not read)* |
| PT158-S2-Q16 | 4 | pt157-158-register; outside-facts | Correct note brings in Plato's family wealth and Philip of Macedon; breakdown says the paradox "isn't really paradoxical". (Found 2026-09-26; re-read here.) |
| PT158-S2-Q20 | 5 | pt157-158-register | Explicit-Standard register (7.6 em-dashes per 1k words; wrong-answer notes average 104.2 words). *(rule, not read)* |
| PT158-S3-Q6 | 2 | pt157-158-register | Explicit-Standard register (9.1 em-dashes per 1k words; wrong-answer notes average 101.8 words). *(rule, not read)* |
| PT158-S4-Q12 | 5 | pt157-158-register | Explicit-Standard register (16.1 em-dashes per 1k words; wrong-answer notes average 80.8 words). *(rule, not read)* |
| PT158-S4-Q19 | 4 | pt157-158-register | Explicit-Standard register (9.4 em-dashes per 1k words; wrong-answer notes average 91.2 words). *(rule, not read)* |

### Sufficient Assumption (9)

| Question | Diff | Tags | Problem |
|---|---|---|---|
| PT134-S2-Q17 | 4 | thin-notes; no-prediction | d4 SA explained by margin diagrams; A note calls A a negation of the premise, which it is not. |
| PT143-S4-Q25 | 5 | short-breakdown; thin-notes; no-prediction | Hard (d5) SA explained only by arrow diagrams; no prose on why B links SI to RL or why the reversal traps tempt. |
| PT147-S4-Q4 | 2 | no-breakdown; placeholder; pasted-notes | No breakdown; correct note is the placeholder "(No authored tag or explanation for this choice.)"; B-E are one pasted sentence (C with a typo, "gone up"). |
| PT157-S2-Q16 | 4 | pt157-158-register | Explicit-Standard register (1.6 em-dashes per 1k words; wrong-answer notes average 81.0 words). *(rule, not read)* |
| PT157-S2-Q18 | 5 | pt157-158-register | Explicit-Standard register (5.3 em-dashes per 1k words; wrong-answer notes average 86.2 words). *(rule, not read)* |
| PT157-S2-Q22 | 5 | pt157-158-register | Explicit-Standard register (1.7 em-dashes per 1k words; wrong-answer notes average 104.0 words). *(rule, not read)* |
| PT158-S2-Q24 | 3 | pt157-158-register | Explicit-Standard register (6.0 em-dashes per 1k words; wrong-answer notes average 117.0 words). *(rule, not read)* |
| PT158-S3-Q19 | 5 | pt157-158-register | Explicit-Standard register (7.3 em-dashes per 1k words; wrong-answer notes average 101.5 words). *(rule, not read)* |
| PT158-S4-Q25 | 5 | pt157-158-register; source-leftover | Explicit-Standard register (7.9 em-dashes per 1k words; wrong-answer notes average 83.5 words). Also: "p.s. if you want to try another problem just like this, try this one." with no link. *(rule, not read)* |

### Principle-Strengthen (7)

| Question | Diff | Tags | Problem |
|---|---|---|---|
| PT118-S3-Q8 | 3 | no-notes | Breakdown only; all five choice notes missing. *(rule, not read)* |
| PT157-S2-Q14 | 4 | pt157-158-register | Explicit-Standard register (4.7 em-dashes per 1k words; wrong-answer notes average 85.5 words). *(rule, not read)* |
| PT157-S2-Q21 | 5 | pt157-158-register | Explicit-Standard register (8.2 em-dashes per 1k words; wrong-answer notes average 92.8 words). *(rule, not read)* |
| PT157-S2-Q23 | 1 | pt157-158-register | Explicit-Standard register (10.5 em-dashes per 1k words; wrong-answer notes average 85.5 words). *(rule, not read)* |
| PT157-S3-Q4 | 2 | pt157-158-register | Explicit-Standard register (8.4 em-dashes per 1k words; wrong-answer notes average 100.5 words). *(rule, not read)* |
| PT158-S2-Q12 | 5 | pt157-158-register | Explicit-Standard register (8.1 em-dashes per 1k words; wrong-answer notes average 109.0 words). *(rule, not read)* |
| PT158-S4-Q17 | 2 | pt157-158-register; padding | Correct; 150-word notes. |

### Principle-Conform (7)

| Question | Diff | Tags | Problem |
|---|---|---|---|
| PT118-S1-Q9 | 2 | no-notes; emdash | Breakdown only; all five choice notes missing. |
| PT123-S3-Q1 | 2 | short-breakdown; verdict-only; thin-correct-note | Breakdown restates the analysis; correct note never names the sacrifice (better-tasting, cheaper wine). |
| PT157-S3-Q5 | 2 | pt157-158-register; garbled-breakdown | Breakdown treats a set of facts as an argument and reads "Taylor's methods have robbing their work"; notes correct but padded. |
| PT157-S3-Q16 | 3 | pt157-158-register | Explicit-Standard register (9.2 em-dashes per 1k words; wrong-answer notes average 35.0 words). *(rule, not read)* |
| PT158-S2-Q23 | 2 | pt157-158-register | Explicit-Standard register (8.8 em-dashes per 1k words; wrong-answer notes average 115.5 words). *(rule, not read)* |
| PT158-S3-Q17 | 5 | pt157-158-register; misquote x4; wrong-logic | A, B, C and D notes describe choices that do not exist ("enjoy learning math", "recommend the product", "return books in good condition", "start working on Saturdays"). D's real problem (build new vs expand old) is never named. |
| PT158-S3-Q25 | 4 | pt157-158-register | Explicit-Standard register (9.0 em-dashes per 1k words; wrong-answer notes average 107.8 words). *(rule, not read)* |

### Main Conclusion (13)

| Question | Diff | Tags | Problem |
|---|---|---|---|
| PT125-S2-Q11 | 2 | short-breakdown; verdict-only; damage | Role labels only; C note is cut off mid-sentence ("supports the argument's"). |
| PT130-S1-Q13 | 5 | damage; wrong-logic | d5 conditional Main Conclusion; notes are one-word-per-line columns; E note restates B's logic and never says E swaps "inspire curiosity" for "have curiosity". |
| PT131-S3-Q9 | 1 | verdict-only; thin-correct-note; no-prediction | Role labels only ("This is a premise"); no reading of the rebuttal structure. |
| PT136-S4-Q26 | 3 | mislabel; wrong-logic | Breakdown labels the author's own premises as "Opposing Evidence/Point"; E note contradicts itself. |
| PT148-S4-Q9 | 2 | no-breakdown; heuristic-only | No breakdown; four wrong notes rest on "This ain't the first sentence" and a claim that the conclusion is explicit "99% of the time". |
| PT157-S2-Q5 | 2 | pt157-158-register | Explicit-Standard register (7.1 em-dashes per 1k words; wrong-answer notes average 78.5 words). *(rule, not read)* |
| PT157-S3-Q2 | 1 | pt157-158-register | Explicit-Standard register (8.2 em-dashes per 1k words; wrong-answer notes average 73.0 words). *(rule, not read)* |
| PT158-S2-Q1 | 3 | pt157-158-register | Explicit-Standard register (9.8 em-dashes per 1k words; wrong-answer notes average 119.5 words). *(rule, not read)* |
| PT158-S2-Q13 | 4 | pt157-158-register | Explicit-Standard register (7.0 em-dashes per 1k words; wrong-answer notes average 105.0 words). *(rule, not read)* |
| PT158-S3-Q3 | 3 | pt157-158-register | Explicit-Standard register (7.7 em-dashes per 1k words; wrong-answer notes average 118.0 words). *(rule, not read)* |
| PT158-S3-Q10 | 3 | pt157-158-register | Explicit-Standard register (5.3 em-dashes per 1k words; wrong-answer notes average 120.0 words). *(rule, not read)* |
| PT158-S4-Q8 | 4 | pt157-158-register; padding | Correct, but notes run 100-150 words with repeated points ("building blocks", "edifice"). |
| PT158-S4-Q10 | 3 | pt157-158-register | Explicit-Standard register (13.7 em-dashes per 1k words; wrong-answer notes average 78.8 words). *(rule, not read)* |

### Role (8)

| Question | Diff | Tags | Problem |
|---|---|---|---|
| PT135-S2-Q17 | 5 | wrong-logic; thin-notes | d5 Role; C note says "The author concedes this point", but C fails because the claim is the philosopher's example, not Graham's analogy. |
| PT157-S3-Q8 | 3 | pt157-158-register | Explicit-Standard register (16.9 em-dashes per 1k words; wrong-answer notes average 31.2 words). *(rule, not read)* |
| PT157-S3-Q11 | 4 | pt157-158-register | Explicit-Standard register (13.9 em-dashes per 1k words; wrong-answer notes average 43.8 words). *(rule, not read)* |
| PT157-S3-Q22 | 5 | pt157-158-register | Explicit-Standard register (10.0 em-dashes per 1k words; wrong-answer notes average 85.0 words). *(rule, not read)* |
| PT158-S2-Q9 | 5 | pt157-158-register | Explicit-Standard register (8.2 em-dashes per 1k words; wrong-answer notes average 91.0 words). *(rule, not read)* |
| PT158-S3-Q12 | 3 | pt157-158-register | Correct; 150-word em-dash notes. |
| PT158-S3-Q18 | 5 | pt157-158-register | Explicit-Standard register (7.0 em-dashes per 1k words; wrong-answer notes average 102.2 words). *(rule, not read)* |
| PT158-S4-Q3 | 4 | pt157-158-register | Correct; padded; the Evidence step is cut off ("tentative."). |

### Parallel Flaw (7)

| Question | Diff | Tags | Problem |
|---|---|---|---|
| PT120-S4-Q17 | 5 | no-notes; emdash | d5 Parallel Flaw with a sound breakdown; all five choice notes missing, which is where this question is won. |
| PT157-S2-Q17 | 2 | pt157-158-register | Explicit-Standard register (6.8 em-dashes per 1k words; wrong-answer notes average 89.2 words). *(rule, not read)* |
| PT157-S3-Q19 | 4 | pt157-158-register | Explicit-Standard register (7.8 em-dashes per 1k words; wrong-answer notes average 92.0 words). *(rule, not read)* |
| PT158-S2-Q22 | 4 | pt157-158-register; misquote; wrong-logic | D note describes a different D ("not in the town's best interest to use the land for recreation"); A note calls A valid, but A ignores the third route ("special qualifications"); B note calls B valid. |
| PT158-S3-Q14 | 4 | pt157-158-register | Explicit-Standard register (8.4 em-dashes per 1k words; wrong-answer notes average 119.0 words). *(rule, not read)* |
| PT158-S4-Q5 | 2 | pt157-158-register | Explicit-Standard register (6.2 em-dashes per 1k words; wrong-answer notes average 126.2 words). *(rule, not read)* |
| PT158-S4-Q26 | 5 | pt157-158-register | Explicit-Standard register (9.4 em-dashes per 1k words; wrong-answer notes average 98.0 words). *(rule, not read)* |

### Parallel (3)

| Question | Diff | Tags | Problem |
|---|---|---|---|
| PT157-S2-Q8 | 3 | pt157-158-register | Explicit-Standard register (5.7 em-dashes per 1k words; wrong-answer notes average 94.0 words). *(rule, not read)* |
| PT157-S3-Q24 | 5 | pt157-158-register | Explicit-Standard register (3.2 em-dashes per 1k words; wrong-answer notes average 72.5 words). *(rule, not read)* |
| PT158-S2-Q25 | 3 | pt157-158-register | Explicit-Standard register (5.2 em-dashes per 1k words; wrong-answer notes average 124.5 words). *(rule, not read)* |

### Agree/Disagree (10)

| Question | Diff | Tags | Problem |
|---|---|---|---|
| PT116-S3-Q6 | 3 | no-breakdown; wrong-logic | No breakdown; C note says Maria "definitely agrees" that the stock market gives reliable income, which she never says; E note apologises ("the best that we've got"). |
| PT123-S3-Q7 | 2 | damage; wrong-logic | Two-speaker table flattened; A note ("not discussed by neither") is wrong, since Antonio does value taking chances; C note ungrammatical. |
| PT135-S4-Q25 | 2 | wrong-speakers; damage | A note names "Samuel nor Tova" and "a general trend of modern life", pasted from another question; speaker table flattened. |
| PT137-S3-Q25 | 2 | wrong-question-text; damage | Evaluate step is from a different question ("Denise and Reshmi agree that people decide whether to commit a crime"); speaker table flattened; notes are labels. |
| PT143-S4-Q18 | 2 | wrong-speakers; wrong-logic | Breakdown table is headed "Graham / Adelaide" (the speakers are Wong and Tate); Evaluate says they disagree whether countries are better off as democracies, when the issue is autocracies. |
| PT148-S3-Q19 | 3 | no-breakdown; dangling-reference; pasted-notes | No breakdown, yet A, B and E say "As we analyzed"; three notes pasted; "Panjak" typo. |
| PT148-S4-Q2 | 1 | no-breakdown; verdict-only | No breakdown; A and D notes list who said what but never say whether both speakers hold the view. |
| PT157-S3-Q3 | 1 | pt157-158-register | Explicit-Standard register (6.6 em-dashes per 1k words; wrong-answer notes average 101.5 words). *(rule, not read)* |
| PT158-S4-Q9 | 5 | pt157-158-register | Explicit-Standard register (7.2 em-dashes per 1k words; wrong-answer notes average 120.5 words). *(rule, not read)* |
| PT158-S4-Q20 | 5 | pt157-158-register | Explicit-Standard register (8.1 em-dashes per 1k words; wrong-answer notes average 90.0 words). *(rule, not read)* |

### Method (3)

| Question | Diff | Tags | Problem |
|---|---|---|---|
| PT117-S3-Q8 | 3 | no-notes; emdash | Breakdown only, in a different register ("Rossi's argument structure"); all five choice notes missing. |
| PT119-S4-Q2 | 1 | no-notes | Breakdown only; all five choice notes missing. |
| PT158-S3-Q22 | 5 | pt157-158-register | Explicit-Standard register (7.8 em-dashes per 1k words; wrong-answer notes average 97.0 words). *(rule, not read)* |

### Evaluate (1)

| Question | Diff | Tags | Problem |
|---|---|---|---|
| PT119-S3-Q3 | ? | no-notes; no-bank-match; emdash | Breakdown only, no choice notes, no bank entry. |

## Weak (100)

### Flaw (7)

| Question | Diff | Tags | Problem |
|---|---|---|---|
| PT107-S3-Q7 | 3 | missing-notes | Only 4 of 5 choice notes present. *(rule, not read)* |
| PT123-S3-Q8 | 1 | verdict-only | Evaluate is right; four notes are "not relevant". |
| PT124-S1-Q18 | 4 | thin-notes | d4 conditional flaw with diagram; notes are one line. |
| PT125-S4-Q19 | 2 | thin-notes | Assumption named and diagrammed; notes brief. |
| PT130-S4-Q14 | 2 | thin-notes | Evaluate names belief vs fact; notes one line each. |
| PT131-S1-Q10 | 3 | verdict-only | Evaluate is good; B note answers a claim B does not make. |
| PT133-S2-Q6 | 3 | thin-notes; thin-correct-note | Evaluate names the overgeneralisation; notes are one line. |

### MBT/Most Supported (12)

| Question | Diff | Tags | Problem |
|---|---|---|---|
| PT104-S4-Q14 | 4 | no-breakdown; damage | Notes do the math well, but no breakdown and spacing lost ("publishedbeforethe"). |
| PT116-S2-Q7 | 2 | no-breakdown; key-check | No breakdown; notes are good. Key C is right; bank says D (see side issues). |
| PT126-S1-Q5 | 2 | thin-notes; no-prediction | Accurate one-line notes; no prediction; typo "It's origin". |
| PT131-S3-Q7 | 2 | thin-notes | Accurate; no prediction; notes brief. |
| PT132-S2-Q19 | 4 | no-prediction; damage | d4 quantifier chain; flattened diagram in Given, C note diagram in a margin column; logic is right. |
| PT135-S1-Q25 | 5 | damage; thin-notes | d5 formal inference; correct-note proof is right but broken into a narrow column; wrong notes are reversal labels. |
| PT138-S2-Q1 | 1 | damage | B and C notes are one-word-per-line columns beside diagrams. |
| PT138-S3-Q4 | 2 | no-breakdown; garbled-note | No breakdown; D note is garbled ("While it's not that the most polluted cities improved..."). |
| PT139-S1-Q21 | 5 | damage; thin-notes | d5 quantifier inference; flattened diagram in Given; notes accurate but one line. |
| PT140-S2-Q14 | 5 | thin-notes; wrong-logic | d5; E note's "reverses MD -> EP" does not describe E's "only epic poetry" error. |
| PT142-S2-Q10 | 2 | thin-notes | Causal chain diagrammed; notes fine but brief. |
| PT147-S1-Q8 | 2 | no-breakdown | No breakdown; notes reason well. |

### Necessary Assumption (1)

| Question | Diff | Tags | Problem |
|---|---|---|---|
| PT126-S1-Q12 | 2 | damage | Diagrams fused into words ("HQ -> EEquality", "SN -> FAwithin"). |

### Weaken (6)

| Question | Diff | Tags | Problem |
|---|---|---|---|
| PT116-S2-Q6 | 1 | no-breakdown; key-check | No breakdown; notes sound. Key E is right; bank says B (see side issues). |
| PT117-S4-Q1 | 1 | no-breakdown | No breakdown; notes and the correct-answer note are sound. |
| PT118-S4-Q4 | 3 | no-breakdown; generic | No breakdown; generic filler register, logic fine. |
| PT124-S3-Q9 | 3 | thin-notes | Correlation-causation named; notes brief. |
| PT124-S3-Q16 | 1 | thin-notes | Evaluate states the weaken route; notes brief. |
| PT133-S2-Q1 | 3 | thin-notes | Evaluate raises the disadvantages route; notes brief. |

### Strengthen (7)

| Question | Diff | Tags | Problem |
|---|---|---|---|
| PT111-S1-Q15 | 3 | no-breakdown | No breakdown; EXCEPT notes are sound. |
| PT118-S4-Q7 | 1 | no-breakdown | No breakdown; notes are sound. |
| PT120-S4-Q8 | 1 | no-breakdown; generic | No breakdown; generic register; notes list each answer's downside without saying why "downside" means not a strengthener. |
| PT131-S2-Q5 | ? | no-bank-match; typos; thin-notes | No bank entry, so the choices cannot be checked; typos "synthensized alphahyrdoxy". |
| PT131-S3-Q11 | 2 | mislabel; wrong-logic | Concession labelled Opposing Point; C note says C "supports the opposing point that scholars... find research libraries more convenient", which C does not say. |
| PT134-S2-Q4 | 1 | verdict-only; damage | Gap named with diagram; A and D are "not relevant". |
| PT144-S3-Q25 | 3 | thin-notes | One-line notes on a d3 provision question. |

### Paradox (3)

| Question | Diff | Tags | Problem |
|---|---|---|---|
| PT131-S3-Q17 | 4 | pasted-notes; key-check | EXCEPT Paradox; C and E share one pasted note. Key A matches the DB; bank says E (see side issues). |
| PT134-S2-Q11 | 2 | pasted-notes | EXCEPT Paradox with a usable Evaluate; notes are pasted ("This provides a disadvantage to larger hospitals"). |
| PT135-S2-Q20 | 3 | thin-notes; loose-logic | A note says A explains why reconstruction is costly (A is about coordination); B note is muddled; Evaluate repeats "prioritizes that prioritizes". |

### Sufficient Assumption (7)

| Question | Diff | Tags | Problem |
|---|---|---|---|
| PT111-S1-Q22 | 4 | missing-notes | Only 4 of 5 choice notes present. *(rule, not read)* |
| PT127-S3-Q16 | 4 | thin-notes; damage | d4 SA with margin diagrams; accurate but terse. |
| PT132-S2-Q15 | 5 | thin-notes; loose-logic | d5 SA; correct note says B "triggers" the rule when it denies the necessary condition. |
| PT134-S3-Q26 | 5 | thin-notes; loose-logic | d5 SA; B note ("negates the conclusion") does not describe B. |
| PT136-S2-Q19 | 3 | thin-notes | SA gap named and diagrammed; notes brief. |
| PT142-S2-Q13 | 3 | verdict-only; thin-correct-note | Gap (EW -> IR) is named correctly, but C is "This supports the argument's premise" and D gets only a reversal diagram. |
| PT148-S3-Q8 | 2 | no-breakdown; wrong-logic | No breakdown; A note says A "supports the premise", but A is irrelevant to identification. |

### Principle-Strengthen (4)

| Question | Diff | Tags | Problem |
|---|---|---|---|
| PT126-S3-Q17 | 4 | no-breakdown; damage | No breakdown; correct note's spaces are stripped; wrong notes are good. |
| PT127-S3-Q3 | 2 | thin-notes | Gap named; notes brief but right. |
| PT142-S2-Q5 | 2 | thin-notes; thin-correct-note | Right idea (curators' judgment makes it appropriate) but every note is one or two lines. |
| PT150-S3-Q25 | 3 | thin-notes; thin-correct-note | Accurate and tidy, but every wrong note is one clause; no analogy or test. |

### Principle-Conform (4)

| Question | Diff | Tags | Problem |
|---|---|---|---|
| PT108-S3-Q16 | 4 | missing-notes | Only 4 of 5 choice notes present. *(rule, not read)* |
| PT119-S2-Q15 | ? | missing-notes | Only 4 of 5 choice notes present. *(rule, not read)* |
| PT123-S3-Q14 | 2 | damage; verdict-only | Stray "- paragraph" markup; wrong notes are "does not address". |
| PT135-S2-Q1 | 1 | damage; slip | Correct-note diagram drops the negation ("(Display -> Damage) -> Display"). |

### Main Conclusion (33)

| Question | Diff | Tags | Problem |
|---|---|---|---|
| PT102-S3-Q17 | 4 | no-breakdown; damage | No breakdown; stray "**" in correct note; notes are good. |
| PT113-S3-Q4 | 2 | no-breakdown; generic | No breakdown; notes in a generic filler register ("This answer makes a claim about..."). |
| PT123-S3-Q12 | 3 | damage; verdict-only | Stray "- paragraph" steps between every step; notes are role labels. |
| PT124-S1-Q4 | 2 | verdict-only; pasted-notes | Breakdown is fine (IC marked) but notes are pasted role labels. |
| PT124-S3-Q3 | 2 | mislabel; thin-notes | The author's own concession is labelled "Opposing Point"; D note follows the mislabel. |
| PT125-S4-Q11 | 4 | verdict-only; thin-correct-note | d4 Main Conclusion; structure mapped correctly, notes are role labels. |
| PT126-S1-Q18 | 4 | verdict-only | Good rephrase of the IC and MC; notes are labels. |
| PT126-S3-Q13 | 3 | verdict-only; thin-correct-note | Breakdown maps the opposing view well; notes are role labels only. |
| PT126-S3-Q20 | 3 | thin-notes | C called "an unstated assumption"; otherwise labels. |
| PT127-S3-Q5 | 2 | mislabel; wrong-logic | A note calls A evidence, but A ("eliminate the use of insecticides") overstates the concession. |
| PT127-S3-Q19 | 3 | thin-notes; typo | Labels only; "Eric" for Erich. |
| PT129-S1-Q4 | 1 | verdict-only | Evaluate explains the last-claim conclusion well; notes are labels. |
| PT130-S4-Q3 | 2 | pasted-notes | D and E share one pasted "assumption underlies" note. |
| PT131-S1-Q1 | 1 | verdict-only | Structure right; notes are labels. |
| PT131-S1-Q13 | 4 | verdict-only | Structure right; notes are labels. |
| PT131-S2-Q10 | 1 | verdict-only; pasted-notes | IC chain is mapped correctly; notes are pasted role labels. |
| PT132-S2-Q10 | 2 | verdict-only; pasted-notes | Role labels only. |
| PT132-S4-Q1 | 1 | verdict-only | Structure right; notes are labels. |
| PT132-S4-Q12 | 2 | verdict-only | E is called "an assumption of the intermediate argument", which is loose. |
| PT133-S1-Q13 | 2 | verdict-only | Structure right; notes are labels. |
| PT133-S3-Q10 | 2 | verdict-only | B note states as fact that advertising "does not attempt to blur", which the stimulus never says; C and D are "not made in the argument". |
| PT134-S1-Q1 | 1 | pasted-notes; wrong-logic | B carries A's pasted note ("Advisable is not the same as necessary"), which has nothing to do with B. |
| PT134-S2-Q1 | 1 | verdict-only | Labels only. |
| PT135-S1-Q2 | 3 | verdict-only; pasted-notes | Breakdown correct with IC; notes are pasted role labels. |
| PT135-S4-Q14 | 3 | verdict-only | Role map right; notes labels. |
| PT136-S4-Q9 | 2 | verdict-only | Labels; "interesting stories" labelled Opposing Evidence. |
| PT137-S4-Q1 | 2 | verdict-only | Labels only. |
| PT138-S2-Q17 | 2 | verdict-only | Labels only. |
| PT138-S4-Q8 | 2 | verdict-only | Labels only. |
| PT139-S1-Q9 | 2 | verdict-only | Role labels only; D and E both called "an assumption of the argument's conclusion" with no reason. |
| PT142-S2-Q9 | 3 | mislabel; verdict-only | Concession labelled "Opposing Point"; B note says B follows from the evidence, which is doubtful. |
| PT143-S4-Q16 | 2 | verdict-only | Labels only. |
| PT144-S3-Q18 | 2 | verdict-only | Labels only. |

### Role (6)

| Question | Diff | Tags | Problem |
|---|---|---|---|
| PT126-S1-Q19 | 3 | mislabel; thin-notes | Toledo example labelled "Opposing Point"; notes are one line but the qualify-vs-refute idea is right. |
| PT135-S1-Q22 | 3 | verdict-only | Role labels only. |
| PT135-S4-Q12 | 3 | verdict-only | Role map right; notes labels. |
| PT138-S2-Q11 | 3 | damage; verdict-only | Correct note truncated ("the role of premise"); rest are one-line labels. |
| PT138-S2-Q22 | 3 | verdict-only; thin-correct-note | Role map is right; notes just restate each choice's label. |
| PT143-S4-Q22 | 2 | thin-notes | Role map is correct; notes are brief. |

### Parallel Flaw (1)

| Question | Diff | Tags | Problem |
|---|---|---|---|
| PT122-S1-Q23 | 4 | no-breakdown | No breakdown; notes build a good parallel template for each answer. |

### Agree/Disagree (6)

| Question | Diff | Tags | Problem |
|---|---|---|---|
| PT133-S3-Q4 | 1 | wrong-speakers; damage | E note says "Neither Talbert nor Sklar" (speakers from PT142-S2-Q7); speaker table flattened. |
| PT134-S3-Q5 | 1 | damage | Two-speaker table flattened into interleaved prose. |
| PT134-S3-Q7 | 2 | damage; thin-notes | Two-speaker table flattened into interleaved prose ("Voters are better Thus, they don't able to choose"). |
| PT136-S4-Q19 | 3 | damage; thin-notes | Two-speaker table flattened into interleaved prose. |
| PT139-S1-Q2 | 2 | damage; thin-notes | Two-speaker table flattened into interleaved prose. |
| PT140-S2-Q5 | 1 | damage; thin-notes | Two-speaker table flattened into interleaved prose. |

### Method (1)

| Question | Diff | Tags | Problem |
|---|---|---|---|
| PT124-S1-Q12 | 3 | thin-notes | Equivocation on "risk" explained; typo "lessons". |

### Must Be False (2)

| Question | Diff | Tags | Problem |
|---|---|---|---|
| PT122-S2-Q16 | 4 | no-breakdown; pasted-notes; damage | No breakdown; the same flattened chain is pasted into four notes; logic is right. |
| PT146-S3-Q11 | 3 | missing-notes | Only 4 of 5 choice notes present. *(rule, not read)* |

## Watch (231)

### Flaw (36)

| Question | Diff | Tags | Problem |
|---|---|---|---|
| PT102-S2-Q20 | 4 | source-leftover | "If you want to see a similar example, try this one." with no link. *(rule, not read)* |
| PT103-S1-Q3 | 2 | no-breakdown | Five choice notes (481 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT106-S3-Q20 | 4 | no-breakdown | Five choice notes (479 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT107-S4-Q14 | 3 | no-breakdown | Five choice notes (344 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT110-S2-Q9 | 4 | no-breakdown | Five choice notes (430 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT111-S1-Q17 | 5 | no-breakdown | Five choice notes (686 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT111-S3-Q26 | 4 | no-breakdown | Five choice notes (327 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT113-S3-Q3 | 1 | no-breakdown | Five choice notes (358 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT113-S4-Q12 | 5 | no-breakdown | Five choice notes (565 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT113-S4-Q17 | 5 | no-breakdown | Five choice notes (645 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT114-S2-Q5 | 2 | no-breakdown | Five choice notes (383 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT116-S2-Q20 | 4 | no-breakdown | Five choice notes (243 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT117-S2-Q1 | ? | stray-markup | Literal "- paragraph" line(s) left in the text. *(rule, not read)* |
| PT117-S2-Q21 | 3 | stray-markup | Literal "- paragraph" line(s) left in the text. *(rule, not read)* |
| PT119-S4-Q10 | 4 | no-breakdown | Five choice notes (202 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT120-S4-Q10 | 2 | no-breakdown | Five choice notes (212 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT121-S4-Q15 | 3 | no-breakdown | Five choice notes (393 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT121-S4-Q25 | 5 | no-breakdown | Five choice notes (705 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT122-S1-Q22 | 5 | no-breakdown | Five choice notes (560 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT122-S1-Q25 | 2 | stray-markup | Literal "- paragraph" line(s) left in the text. *(rule, not read)* |
| PT123-S3-Q4 | 2 | stray-markup | Literal "- paragraph" line(s) left in the text. *(rule, not read)* |
| PT124-S2-Q20 | 5 | no-breakdown | Five choice notes (619 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT126-S4-Q12 | 2 | no-breakdown | Five choice notes (248 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT138-S3-Q3 | 2 | no-breakdown | Five choice notes (369 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT139-S4-Q11 | 4 | no-breakdown | Five choice notes (472 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT140-S3-Q7 | 2 | source-leftover | "click on the bold if you'd like to see other examples" (LSAT Lab interface). *(rule, not read)* |
| PT140-S3-Q18 | 4 | source-leftover | "If you want to try a somewhat similar problem, try this one." with no link. *(rule, not read)* |
| PT148-S3-Q5 | 3 | no-breakdown | Five choice notes (642 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT148-S3-Q14 | 3 | no-breakdown | Five choice notes (533 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT148-S3-Q16 | 5 | no-breakdown | Five choice notes (420 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT148-S3-Q18 | 3 | no-breakdown | Five choice notes (588 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT148-S3-Q20 | 4 | no-breakdown | Five choice notes (522 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT148-S4-Q1 | 1 | no-breakdown | Five choice notes (396 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT148-S4-Q11 | 2 | no-breakdown | Five choice notes (627 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT152-S2-Q11 | 1 | no-breakdown | Five choice notes (548 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT155-S4-Q15 | 2 | source-leftover | "Welcome to Test 89, everyone." (LSAT Lab test numbering). *(rule, not read)* |

### MBT/Most Supported (25)

| Question | Diff | Tags | Problem |
|---|---|---|---|
| PT102-S2-Q3 | 1 | no-breakdown | Five choice notes (264 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT102-S2-Q19 | 3 | no-breakdown | Five choice notes (262 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT104-S1-Q9 | 3 | no-breakdown | Five choice notes (173 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT105-S4-Q15 | 5 | no-breakdown | Five choice notes (360 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT106-S2-Q10 | 5 | no-breakdown | Five choice notes (318 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT107-S3-Q22 | 5 | no-breakdown | Five choice notes (319 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT109-S1-Q9 | 3 | no-breakdown | Five choice notes (210 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT109-S4-Q14 | 4 | no-breakdown | Five choice notes (358 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT111-S1-Q12 | 2 | no-breakdown | Five choice notes (239 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT111-S3-Q16 | 2 | no-breakdown | Five choice notes (514 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT111-S4-Q3 | 1 | minor | Stray "- paragraph" markup in D and E; typo "communicated". |
| PT112-S1-Q14 | 3 | no-breakdown | Five choice notes (438 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT114-S2-Q22 | 5 | no-breakdown | Five choice notes (366 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT117-S2-Q14 | ? | stray-markup | Literal "- paragraph" line(s) left in the text. *(rule, not read)* |
| PT118-S4-Q16 | 3 | no-breakdown | Five choice notes (371 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT119-S2-Q2 | 2 | no-breakdown | Five choice notes (281 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT120-S1-Q16 | 2 | no-breakdown | Five choice notes (237 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT120-S3-Q1 | 2 | no-breakdown | Five choice notes (204 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT122-S1-Q21 | 3 | no-breakdown | Five choice notes (346 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT123-S2-Q24 | 2 | stray-markup | Literal "- paragraph" line(s) left in the text. *(rule, not read)* |
| PT123-S3-Q22 | 4 | stray-markup | Literal "- paragraph" line(s) left in the text. *(rule, not read)* |
| PT127-S1-Q26 | 3 | no-breakdown | Five choice notes (584 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT138-S3-Q13 | 2 | no-breakdown | Five choice notes (301 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT148-S3-Q17 | 3 | no-breakdown | Five choice notes (378 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT148-S3-Q24 | 4 | no-breakdown | Five choice notes (456 words in all) but no Argument Breakdown. *(rule, not read)* |

### Necessary Assumption (26)

| Question | Diff | Tags | Problem |
|---|---|---|---|
| PT101-S3-Q13 | 1 | no-breakdown | Five choice notes (364 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT104-S4-Q4 | 2 | no-breakdown | Five choice notes (436 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT104-S4-Q20 | 4 | no-breakdown | Five choice notes (433 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT105-S1-Q23 | 5 | no-breakdown | Five choice notes (531 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT105-S4-Q4 | 2 | no-breakdown | Five choice notes (285 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT106-S2-Q8 | 2 | no-breakdown | Five choice notes (387 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT106-S2-Q11 | 3 | no-breakdown | Five choice notes (471 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT107-S3-Q1 | 1 | no-breakdown | Five choice notes (294 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT111-S1-Q14 | 2 | no-breakdown | Five choice notes (300 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT114-S1-Q24 | 4 | no-breakdown | Five choice notes (255 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT115-S4-Q4 | 2 | no-breakdown | Five choice notes (537 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT117-S3-Q25 | 3 | no-breakdown | Five choice notes (495 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT118-S4-Q6 | 3 | no-breakdown | Five choice notes (475 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT120-S1-Q14 | 2 | stray-markup | Literal "- paragraph" line(s) left in the text. *(rule, not read)* |
| PT122-S1-Q24 | 3 | no-breakdown | Five choice notes (358 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT122-S2-Q17 | 4 | no-breakdown | Five choice notes (444 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT123-S3-Q11 | 3 | stray-markup | Literal "- paragraph" line(s) left in the text. *(rule, not read)* |
| PT127-S1-Q13 | 2 | no-breakdown | Five choice notes (695 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT127-S1-Q19 | 4 | no-breakdown | Five choice notes (479 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT128-S3-Q17 | 3 | no-breakdown | Five choice notes (201 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT137-S2-Q6 | 1 | no-breakdown | Five choice notes (397 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT148-S3-Q12 | 5 | no-breakdown | Five choice notes (301 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT148-S3-Q15 | 2 | no-breakdown | Five choice notes (591 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT148-S3-Q21 | 4 | no-breakdown | Five choice notes (487 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT149-S4-Q4 | 1 | no-breakdown | Five choice notes (418 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT152-S2-Q12 | 5 | no-breakdown | Five choice notes (255 words in all) but no Argument Breakdown. *(rule, not read)* |

### Weaken (38)

| Question | Diff | Tags | Problem |
|---|---|---|---|
| PT102-S2-Q5 | 2 | no-breakdown | Five choice notes (144 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT103-S2-Q5 | 3 | no-breakdown | Five choice notes (338 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT103-S3-Q6 | 2 | no-breakdown | Five choice notes (202 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT103-S3-Q14 | 4 | no-breakdown | Five choice notes (303 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT104-S1-Q8 | 2 | no-breakdown | Five choice notes (202 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT104-S4-Q15 | 4 | no-breakdown | Five choice notes (369 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT104-S4-Q18 | 5 | no-breakdown | Five choice notes (603 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT106-S3-Q11 | 4 | no-breakdown | Five choice notes (665 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT109-S1-Q4 | 3 | no-breakdown | Five choice notes (394 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT109-S3-Q7 | 3 | no-breakdown | Five choice notes (378 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT111-S1-Q4 | 5 | no-breakdown | Five choice notes (689 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT111-S1-Q13 | 3 | no-breakdown | Five choice notes (481 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT111-S3-Q8 | 2 | no-breakdown | Five choice notes (335 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT112-S1-Q2 | 2 | no-breakdown | Five choice notes (161 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT112-S1-Q8 | 3 | no-breakdown | Five choice notes (249 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT112-S4-Q11 | 3 | no-breakdown | Five choice notes (299 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT113-S2-Q14 | 2 | no-breakdown | Five choice notes (145 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT113-S4-Q11 | 3 | no-breakdown | Five choice notes (137 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT114-S4-Q13 | 4 | no-breakdown | Five choice notes (204 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT115-S4-Q22 | 3 | no-breakdown | Five choice notes (139 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT116-S3-Q8 | 3 | no-breakdown | Five choice notes (160 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT117-S2-Q4 | ? | no-breakdown | Five choice notes (224 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT118-S3-Q2 | 2 | no-breakdown | Five choice notes (277 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT119-S3-Q6 | 2 | stray-markup | Literal "- paragraph" line(s) left in the text. *(rule, not read)* |
| PT121-S1-Q19 | 3 | no-breakdown | Five choice notes (507 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT121-S4-Q9 | 2 | stray-markup | Literal "- paragraph" line(s) left in the text. *(rule, not read)* |
| PT122-S1-Q16 | 4 | no-breakdown | Five choice notes (477 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT122-S2-Q6 | 2 | no-breakdown | Five choice notes (147 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT123-S3-Q15 | 4 | stray-markup | Literal "- paragraph" line(s) left in the text. *(rule, not read)* |
| PT124-S2-Q26 | 4 | no-breakdown | Five choice notes (471 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT127-S1-Q6 | 2 | no-breakdown | Five choice notes (184 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT128-S2-Q17 | 4 | no-breakdown | Five choice notes (449 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT130-S1-Q24 | 5 | minor | Strong d5, but the A note first says A's bears came from outside the valley, then admits A does not say so. |
| PT138-S4-Q6 | 3 | no-breakdown | Five choice notes (327 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT147-S4-Q19 | 4 | no-breakdown | Five choice notes (480 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT148-S3-Q10 | 5 | no-breakdown | Five choice notes (410 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT149-S4-Q2 | 1 | no-breakdown | Five choice notes (235 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT154-S2-Q5 | 1 | no-breakdown | Five choice notes (342 words in all) but no Argument Breakdown. *(rule, not read)* |

### Strengthen (29)

| Question | Diff | Tags | Problem |
|---|---|---|---|
| PT102-S2-Q4 | 4 | no-breakdown | Five choice notes (271 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT102-S4-Q6 | 2 | no-breakdown | Five choice notes (312 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT106-S1-Q15 | 3 | no-breakdown | Five choice notes (236 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT106-S3-Q6 | 1 | no-breakdown | Five choice notes (331 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT106-S3-Q24 | 2 | minor | Strong, but spaces lost around emphasised words ("aCurious", "islesslikely"); heuristic missed it. |
| PT108-S2-Q14 | 4 | no-breakdown | Five choice notes (597 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT109-S3-Q4 | 2 | no-breakdown | Five choice notes (263 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT110-S3-Q24 | 3 | no-breakdown | Five choice notes (372 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT112-S3-Q11 | 1 | no-breakdown | Five choice notes (195 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT112-S4-Q12 | 3 | no-breakdown | Five choice notes (233 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT113-S4-Q13 | 5 | no-breakdown | Five choice notes (216 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT114-S4-Q5 | 2 | no-breakdown | Five choice notes (166 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT117-S4-Q14 | 3 | stray-markup | Literal "- paragraph" line(s) left in the text. *(rule, not read)* |
| PT120-S1-Q11 | 3 | no-breakdown | Five choice notes (139 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT120-S4-Q2 | 2 | no-breakdown | Five choice notes (205 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT120-S4-Q24 | 2 | no-breakdown | Five choice notes (140 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT122-S2-Q4 | 2 | no-breakdown | Five choice notes (201 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT124-S1-Q6 | 3 | stray-markup | Literal "- paragraph" line(s) left in the text. *(rule, not read)* |
| PT124-S2-Q19 | 4 | no-breakdown | Five choice notes (383 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT127-S1-Q9 | 3 | no-breakdown | Five choice notes (692 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT138-S3-Q7 | 2 | no-breakdown | Five choice notes (162 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT142-S1-Q4 | 1 | no-breakdown | Five choice notes (166 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT148-S3-Q7 | 2 | no-breakdown | Five choice notes (215 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT148-S3-Q23 | 5 | no-breakdown | Five choice notes (430 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT148-S3-Q25 | 5 | no-breakdown | Five choice notes (706 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT148-S4-Q4 | 1 | minor | Excellent notes; only problem is no breakdown. |
| PT148-S4-Q7 | 2 | no-breakdown | Five choice notes (234 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT148-S4-Q10 | 5 | no-breakdown | Five choice notes (367 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT152-S2-Q9 | 3 | no-breakdown | Five choice notes (181 words in all) but no Argument Breakdown. *(rule, not read)* |

### Paradox (17)

| Question | Diff | Tags | Problem |
|---|---|---|---|
| PT101-S3-Q14 | 2 | no-breakdown | Five choice notes (289 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT107-S1-Q4 | 3 | no-breakdown | Five choice notes (190 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT111-S1-Q10 | 2 | no-breakdown | Five choice notes (211 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT112-S1-Q9 | 4 | minor | Strong worked example, but says "3 mg iron per capita" for per calorie; "raising" for raisins. |
| PT113-S4-Q5 | 2 | no-breakdown | Five choice notes (299 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT115-S2-Q5 | 1 | no-breakdown | Five choice notes (263 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT116-S3-Q13 | 4 | no-breakdown | Five choice notes (490 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT116-S3-Q15 | 4 | no-breakdown | Five choice notes (219 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT118-S3-Q17 | 3 | no-breakdown | Five choice notes (369 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT123-S2-Q25 | 4 | stray-markup | Literal "- paragraph" line(s) left in the text. *(rule, not read)* |
| PT124-S2-Q21 | 2 | no-breakdown | Five choice notes (328 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT148-S3-Q9 | 2 | no-breakdown | Five choice notes (388 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT148-S3-Q11 | 2 | no-breakdown | Five choice notes (596 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT148-S4-Q3 | 2 | no-breakdown | Five choice notes (444 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT151-S3-Q23 | 2 | no-breakdown | Five choice notes (153 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT152-S2-Q8 | 1 | no-breakdown | Five choice notes (194 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT154-S2-Q3 | 1 | no-breakdown | Five choice notes (349 words in all) but no Argument Breakdown. *(rule, not read)* |

### Sufficient Assumption (13)

| Question | Diff | Tags | Problem |
|---|---|---|---|
| PT102-S3-Q18 | 5 | no-breakdown | Five choice notes (292 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT109-S4-Q13 | 5 | no-breakdown | Five choice notes (317 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT111-S4-Q19 | 4 | stray-markup | Literal "- paragraph" line(s) left in the text. *(rule, not read)* |
| PT117-S2-Q13 | ? | stray-markup | Literal "- paragraph" line(s) left in the text. *(rule, not read)* |
| PT120-S1-Q9 | 1 | no-breakdown | Five choice notes (326 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT122-S2-Q7 | 5 | no-breakdown | Five choice notes (508 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT123-S2-Q6 | 3 | stray-markup | Literal "- paragraph" line(s) left in the text. *(rule, not read)* |
| PT126-S4-Q23 | 4 | no-breakdown | Five choice notes (360 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT128-S3-Q11 | 3 | no-breakdown | Five choice notes (227 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT132-S4-Q18 | 5 | minor; source-leftover | Strong, but tells students to "watch the class recording, via the play button on the highlighter toolbar", an LSAT Lab leftover the heuristic missed. Also: Tells students to "watch the class recording, via the play button on the highlighter toolbar". |
| PT145-S2-Q9 | 2 | no-breakdown | Five choice notes (295 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT146-S3-Q20 | 4 | no-breakdown | Five choice notes (302 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT148-S4-Q5 | 2 | no-breakdown | Five choice notes (375 words in all) but no Argument Breakdown. *(rule, not read)* |

### Principle-Strengthen (10)

| Question | Diff | Tags | Problem |
|---|---|---|---|
| PT107-S4-Q17 | 2 | no-breakdown | Five choice notes (500 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT114-S4-Q4 | 1 | no-breakdown | Five choice notes (211 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT116-S3-Q7 | 2 | no-breakdown | Five choice notes (529 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT122-S1-Q17 | 2 | no-breakdown | Five choice notes (288 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT138-S3-Q12 | 5 | no-breakdown | Five choice notes (504 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT143-S1-Q2 | 2 | no-breakdown | Five choice notes (241 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT148-S3-Q6 | 1 | no-breakdown | Five choice notes (494 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT148-S4-Q6 | 2 | no-breakdown | Five choice notes (652 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT148-S4-Q8 | 2 | no-breakdown | Five choice notes (609 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT154-S2-Q4 | 1 | no-breakdown | Five choice notes (340 words in all) but no Argument Breakdown. *(rule, not read)* |

### Principle-Conform (3)

| Question | Diff | Tags | Problem |
|---|---|---|---|
| PT117-S2-Q12 | ? | stray-markup | Literal "- paragraph" line(s) left in the text. *(rule, not read)* |
| PT118-S3-Q18 | 3 | no-breakdown | Five choice notes (359 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT119-S3-Q8 | ? | stray-markup | Literal "- paragraph" line(s) left in the text. *(rule, not read)* |

### Main Conclusion (6)

| Question | Diff | Tags | Problem |
|---|---|---|---|
| PT109-S1-Q5 | 3 | no-breakdown | Five choice notes (259 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT111-S1-Q3 | 1 | no-breakdown | Five choice notes (390 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT111-S1-Q16 | 3 | no-breakdown | Five choice notes (231 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT121-S4-Q1 | 2 | no-breakdown | Five choice notes (283 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT141-S4-Q5 | 3 | no-breakdown | Five choice notes (247 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT152-S2-Q10 | 4 | no-breakdown | Five choice notes (381 words in all) but no Argument Breakdown. *(rule, not read)* |

### Role (4)

| Question | Diff | Tags | Problem |
|---|---|---|---|
| PT107-S4-Q2 | 3 | no-breakdown | Five choice notes (455 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT111-S1-Q1 | 3 | no-breakdown | Five choice notes (333 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT124-S1-Q11 | 2 | stray-markup | Literal "- paragraph" line(s) left in the text. *(rule, not read)* |
| PT148-S3-Q13 | 4 | minor | Good notes; no breakdown. |

### Parallel Flaw (4)

| Question | Diff | Tags | Problem |
|---|---|---|---|
| PT103-S3-Q13 | 3 | no-breakdown | Five choice notes (313 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT124-S1-Q21 | 4 | stray-markup | Literal "- paragraph" line(s) left in the text. *(rule, not read)* |
| PT125-S4-Q8 | 1 | stray-markup | Literal "- paragraph" line(s) left in the text. *(rule, not read)* |
| PT148-S3-Q22 | 4 | no-breakdown | Five choice notes (587 words in all) but no Argument Breakdown. *(rule, not read)* |

### Parallel (6)

| Question | Diff | Tags | Problem |
|---|---|---|---|
| PT111-S3-Q14 | 1 | no-breakdown | Five choice notes (322 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT116-S3-Q25 | 5 | no-breakdown | Five choice notes (340 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT125-S4-Q25 | 3 | stray-markup | Literal "- paragraph" line(s) left in the text. *(rule, not read)* |
| PT134-S2-Q3 | 2 | minor | Sound, but notes are narrow diagram columns. |
| PT143-S4-Q9 | 1 | source-leftover | Text says "the sentence ends here with no continuation on the LSAT Lab page" (truncated at source). *(rule, not read)* |
| PT148-S3-Q26 | 4 | no-breakdown | Five choice notes (515 words in all) but no Argument Breakdown. *(rule, not read)* |

### Agree/Disagree (7)

| Question | Diff | Tags | Problem |
|---|---|---|---|
| PT107-S4-Q13 | 5 | no-breakdown | Five choice notes (262 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT108-S2-Q13 | 4 | no-breakdown | Five choice notes (458 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT123-S3-Q3 | 3 | stray-markup | Literal "- paragraph" line(s) left in the text. Also: two-speaker table flattened. *(rule, not read)* |
| PT131-S1-Q23 | 2 | damage | Two-speaker table (Constance / Brigita) flattened into interleaved prose. *(rule, not read)* |
| PT131-S2-Q2 | ? | damage | Two-speaker table (Price / Albrecht) flattened into interleaved prose. *(rule, not read)* |
| PT142-S2-Q7 | 2 | no-breakdown | Five choice notes (151 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT147-S4-Q5 | 3 | no-breakdown | Five choice notes (171 words in all) but no Argument Breakdown. *(rule, not read)* |

### Method (3)

| Question | Diff | Tags | Problem |
|---|---|---|---|
| PT104-S4-Q21 | 5 | no-breakdown | Five choice notes (312 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT107-S1-Q12 | 3 | no-breakdown | Five choice notes (436 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT112-S1-Q7 | 4 | no-breakdown | Five choice notes (216 words in all) but no Argument Breakdown. *(rule, not read)* |

### Must Be False (1)

| Question | Diff | Tags | Problem |
|---|---|---|---|
| PT127-S1-Q25 | 5 | no-breakdown | Five choice notes (564 words in all) but no Argument Breakdown. *(rule, not read)* |

### Evaluate (1)

| Question | Diff | Tags | Problem |
|---|---|---|---|
| PT139-S1-Q5 | 3 | source-leftover | "try this one" with no link. *(rule, not read)* |

### Fill-in/Complete (2)

| Question | Diff | Tags | Problem |
|---|---|---|---|
| PT102-S3-Q19 | 2 | no-breakdown | Five choice notes (298 words in all) but no Argument Breakdown. *(rule, not read)* |
| PT146-S1-Q8 | 3 | no-breakdown | Five choice notes (378 words in all) but no Argument Breakdown. *(rule, not read)* |
