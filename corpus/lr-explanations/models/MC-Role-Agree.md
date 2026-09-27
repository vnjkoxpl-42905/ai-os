# Model picks: Main Conclusion, Role, Agree/Disagree

Read 2026-09-27. Every candidate in the three shortlists (40 + 40 + 40) was read in full against the printed stimulus and choices. Scores are one reader's judgment on the P X E T C L rubric (0/1/2 each, /12); treat an 11 and a 12 as a tie. "Golden" means the slot is already in `corpus/lr-explanations/golden-set.md`.

---

## Main Conclusion

**Off-type candidates (skipped).** 16 of the 40 are not Main Conclusion. The stem says "conclusion", which pulled them in:
- Sufficient Assumption: PT117-S2-Q13, PT113-S4-Q9, PT142-S1-Q12, PT111-S4-Q19, PT117-S4-Q26, PT115-S4-Q17, PT116-S2-Q18, PT159-S3-Q17, PT126-S4-Q19, PT154-S1-Q11, PT152-S2-Q3 (stem: "overall conclusion ... strongly supported if assumed")
- Necessary Assumption: PT102-S4-Q9
- Strengthen / justify: PT110-S3-Q21
- Flaw: PT140-S1-Q18
- Method: PT146-S1-Q5, PT143-S3-Q11

That leaves 24 real MC candidates. I picked 20 of them. Five are difficulty 1-2. Easy MC is thin in this shortlist, and the gap list is weighted toward easy questions. If more easy models are needed, search scores.json for fam = Main Conclusion, diff 1-2.

### Picks

| # | Slot | Diff | Sub-pattern / features | Rubric /12 | What makes it a model | Weakness | Golden? |
|---|---|---|---|---|---|---|---|
| 1 | PT139-S4-Q1 | 1 | First sentence + rebuttal; referential ("that view") | 11 | Gives the three MC reminders (last claim ~10%, intermediate conclusions exist, first sentence or pivot), then swaps "that view" for the specific belief before matching. Labels each wrong answer by role: intermediate/last-claim (A), premise (B, C), opposing position (D). | B and C notes are two lines each. | Y |
| 2 | PT111-S1-Q3 | 1 | Attribution, then "but" pivot; pronoun ("this theory") | 10 | Treats "attributed" as the cue that a rebuttal is coming, then fills in the pronoun: "It may be wrong to think longer life span is why...". The correct note checks strength ("may explain" = "may be wrong"). D's note says why an inference you could draw is still not the conclusion. | B through E open with the same pasted sentence. | N |
| 3 | PT118-S1-Q1 | 1 | Main Point stem ("The author is arguing that"); first-sentence conclusion | 9 | Explains how a Main Point stem differs: the answer may give an implied or combined version of the conclusion, so you loosen the match on purpose. Works out how the unclear premise supports the conclusion (consumption goes up, well-being does not). | All traps are 0-4%, so none gets a long note. "super aloof". | N |
| 4 | PT155-S2-Q6 | 2 | Second-sentence conclusion; speculative "must"; "and" joins premises | 10 | The party analogy (friends left, "they must have gotten a call from the babysitter") shows why "must" here marks the author's opinion. States the rule that two claims joined by "and" are premises. The last-claim trap E (9%) is killed with the support test. | Correct note is one line. | N |
| 5 | PT153-S3-Q5 | 2 | Final-sentence conclusion ("Consequently"); causal chain | 10 | Runs the support test in both directions ("why believe A? because B" vs "why believe B? because A") to pick the conclusion when the keyword could be causal. D's note: a dependent clause cannot be a main conclusion. C (14%, intermediate conclusion) is placed in the chain. | The Evaluate step is one dense paragraph. | N |
| 6 | PT103-S2-Q8 | 3 | First-sentence conclusion with a "because" clause (MC + IC in one sentence) | 11 | Separates the main clause from the "because" clause in the same sentence. The C trap (18%) is rejected as the claim introduced by "because". D gets the support test and the last-claim warning. | B note is short. | Y |
| 7 | PT151-S4-Q8 | 3 | First sentence, "should"; last-sentence trap | 10 | Lists the two questions to ask while reading (is the first sentence an opinion? is there an attribution to rebut?). Gives the 22% last-claim trap E the support test, and when no support turns up it says so ("? ?"). | A note calls A an intermediate conclusion without showing its support. | N |
| 8 | PT152-S4-Q21 | 3 | Two intermediate conclusions; "should" first sentence; "So" last sentence | 11 | Builds the whole chain as "why? because..." under the breakdown headings, so the student sees four levels. B (25%, the "So" claim) is shown to be the reason for sentence 1, which is the move students need when the last sentence carries a conclusion word. | B note is two lines for a 25% trap. "(jerks)" aside. | N |
| 9 | PT119-S3-Q21 | 3 | First sentence that is also a rebuttal ("misleading") | 11 | Correct note weighs "misleading" vs "deceptive" and says they are close enough when nothing is closer. C (12%) is rejected on a precise distinction: the author objected that the data were incomplete, not that they were inaccurate. D note: a claim nothing supports is not a conclusion. | B, D, E open with the same "doesn't look anything like the first sentence" line. | N |
| 10 | PT153-S3-Q9 | 4 | Conditional conclusion before "since"; FABS | 10 | Teaches that "since" marks its own clause as support, which makes the other clause the conclusion. The last-claim trap B gets examples of what support would have sounded like ("donations have been low this cycle"). | "99.8% of the time" overclaims. D note is one rule line. | N |
| 11 | PT154-S2-Q20 | 4 | First-sentence conclusion that sounds like a fact; hard synonym match | 11 | A reading posture for MC, then a side-by-side synonym map from sentence 1 to A. Says the second "Because" is causal, not a reasoning indicator. Each wrong answer is dropped with one test (it names something sentence 1 never mentions), then given its role. | "aloofly". The "punch" joke is aimed at the correct answer, though it is mild. | Y |
| 12 | PT116-S3-Q23 | 4 | Second-sentence "probably" conclusion; "to see this, consider"; causal "thus" | 12 | Both 16% traps get real work. For A, it writes out what support for a science fact would look like and notes the passage gives none. For D, it separates a causal "thus" from a reasoning "thus" with paired examples. Says a science fact cannot be the conclusion. | None significant. | N |
| 13 | PT123-S2-Q10 | 4 | First sentence "should"; last claim baits with "clearly ... should" | 11 | Evaluate explains why the final "clearly ... should" claim is bait: it is unsupported, and "and" pairs it with claim 2 as support. The 25% trap E gets the longest note: "something the author would agree with" is a different task from "what the author concluded". | B note is one line. | N |
| 14 | PT146-S2-Q14 | 4 | Final-sentence conditional conclusion ("then"); Reversal trap | 11 | The 27% trap A (a reversal of the conclusion) is diagrammed against the conclusion. Rules tied to cue words: "according to a study" and "moreover" cannot introduce the conclusion. Admits LSAC now sometimes puts the conclusion last to beat test-prep advice. | C note garbles the variables ("to be Z, it needs Y and Z"). D note is one line. | N |
| 15 | PT152-S2-Q10 | 4 | Final-sentence conclusion after "Thus ... However ... Therefore" | 11 | Sorts three keywords by job: "Thus" gives an implication of the old method, "However" marks the author's turn, "Therefore" marks the conclusion. The 19% trap D gets the longest note and pins the difference ("when land uses diversified" vs "when people realized plow time was inadequate"). | A note is mostly a verdict. | N |
| 16 | PT112-S3-Q23 | 4 | Implied rebuttal conclusion ("directed toward establishing") | 10 | Uses the Ringo example to show how to state an implied rebuttal conclusion, and reads the sarcastic "as if" as the author's position showing. Correct note explains why "no reason to believe" is the responsible version (and names Unproven vs Proven False). A (24%) is placed as support. | Fidelity: the breakdown's Conclusion line states the article's view ("strength was declining"), the reverse of the author's. | N |
| 17 | PT112-S1-Q6 | 4 | Main Point stem; attribution, then "However" rebuttal; third-factor explanation | 10 | Recognizes the pattern (curious fact, alternate explanation by a third factor) and predicts a combined answer because the stem says Main Point. A (24%) is rejected precisely: the author doubts the cause, not whether the outbreaks happened. E is flagged as the last claim. | A note is short for a 24% trap. | N |
| 18 | PT106-S3-Q14 | 4 | Implied conclusion; neither first sentence nor pivot | 10 | Says plainly that the usual heuristics fail here and falls back on two tests: is it the author's opinion, and did she support it. Gives a support chain for A. E (21%) fails on scope (it never mentions voting). | C and D notes are ordinary. | N |
| 19 | PT115-S2-Q1 | 4 | Conclusion inside a quotation; argument by contrapositive | 10 | Reduces a dense quotation to "A is X, because if not-X then Z, and not-Z", then diagrams the traps D (10%) and E (17%) as reversed and negated versions of the conditional premise. | Transcription: the side-by-side match in the C note is flattened. Downton Abbey aside. | N |
| 20 | PT140-S1-Q7 | 4 | "However" pivot followed by "because"; referential ("Gillette's argument") | 9 | Explains that a pivot can go "However, conclusion. Because, support" or "However, support. Thus, conclusion", and the keyword after it decides which. Fills in what "Gillette's argument" refers to before matching. | B (27%) gets two lines. The A note never says why A is wrong. The E note calls a conclusion-plus-premise answer an "anomaly". | N |

Reserves, read and not picked: PT106-S1-Q18 (good pivot model, but formatting loss merges words throughout), PT102-S4-Q1 (Main Point; breakdown slip, see fidelity), PT111-S4-Q9 (four wrong-answer notes are the same pasted verdict), PT151-S4-Q3 (formal voice, thin notes).

### What the best ones do

- **Set the reading posture before reading.** They say "the conclusion is usually earlier than its support" before the first sentence, then test each early claim: is it the author's opinion, and does what follows support it? (PT139-S4-Q1, PT154-S2-Q20)
- **Replace referential language before matching.** "This theory may be wrong" becomes "it may be wrong to think longer life span is why women get Alzheimer's more". The student matches the full meaning, not the pronoun. (PT111-S1-Q3, PT140-S1-Q7)
- **Run the support test on the trap, and say what support would have looked like.** "Why should we believe X? A reason would sound like '...', and nothing like that is here." That shows the student the test, not just a verdict. (PT116-S3-Q23, PT153-S3-Q9)
- **Sort keywords by job.** They name the fixed rules (FABS marks support; "and" and "moreover" join premises; "according to a study" is never the conclusion). They also flag the ones that can mislead: causal "thus" and "because" versus reasoning "thus" and "because". (PT116-S3-Q23, PT146-S2-Q14, PT152-S2-Q10)
- **Map intermediate conclusions as a chain.** "Why? Because..." down every level, so the student sees that the "So" claim is a reason for the first sentence, not the top. (PT152-S4-Q21, PT103-S2-Q8)
- **Handle the exceptions honestly.** The final sentence is sometimes the conclusion. They say so, then show the keyword or support test that proves it this time. (PT153-S3-Q5, PT146-S2-Q14, PT152-S2-Q10)
- **Spend the most words on the most popular trap, and name why it tempts.** The last claim feels like a conclusion, an assumption the author would accept, or a reversal of the conclusion. (PT123-S2-Q10 E at 25%, PT146-S2-Q14 A at 27%, PT152-S2-Q10 D at 19%)
- **Show the synonym match term by term.** A side-by-side map from the conclusion to the answer, including why a near-synonym is close enough ("misleading" vs "deceptive"). (PT154-S2-Q20, PT119-S3-Q21)
- **Adjust for the stem.** Main Point and "the author is arguing that" allow an implied or combined answer, and "directed toward establishing" tells you the conclusion is implied. (PT118-S1-Q1, PT112-S1-Q6, PT112-S3-Q23)

### What the weaker candidates got wrong

- **Pasted verdicts.** Four of five notes read "There was no explicit claim that said X. We're looking to match the 2nd half of the first sentence." (PT111-S4-Q9). Nothing in that note is specific to the question.
- **Rejecting on appearance only.** "This does not look like the first sentence" and nothing more, when the choice was a premise or an intermediate conclusion worth one sentence. (Partly in PT119-S3-Q21 and PT154-S2-Q20; worse in PT106-S1-Q18 A.)
- **Short notes on the big trap.** The 27% last-claim trap gets two lines (PT140-S1-Q7 B). The 24% trap gets one short paragraph (PT112-S1-Q6 A).
- **Overclaimed statistics as a substitute for reasoning.** "99.8% of the time" (PT153-S3-Q9), "Why would LSAC make this mistake?" (PT140-S1-Q7 E).
- **Formal-voice brevity.** Correct and accurate, but no prediction beyond "keep an open mind", and one-sentence notes. (PT151-S4-Q3)

### Fidelity problems

- **PT112-S3-Q23**: the breakdown's Conclusion line reads "The union's strength was declining". That is the article's claim. The author's implied conclusion is the opposite (Evaluate and Goal state it correctly).
- **PT102-S4-Q1**: the breakdown's Conclusion line says "a prime example of fiscal responsibility". The stimulus says "irresponsibility". The Goal step has it right.
- **PT146-S2-Q14**: the C note says "For a meeting to be Z, it needs to have Y and Z", with the variables garbled. It should be X and Y.
- **PT140-S1-Q7**: the A note restates the author's view but never says why A is wrong. The E note calls a conclusion-plus-premise answer an LSAC "mistake"; that answer shape is not rare.
- **PT115-S2-Q1**: the side-by-side synonym match in the C note is flattened into one line (transcription).
- **PT106-S1-Q18**: formatting loss merged words ("author'sOpinionshining", "massive interventions(like", "=We need to take into account").
- **PT153-S3-Q9**: "99.8%" and "100% guaranteed" are overclaims, not errors of fact about the question.
- Off-type items (listed above) were not audited for fidelity. One noticed in passing: in the PT159-S3-Q17 B note, the diagram is labelled "(A)".

---

## Role

All 40 candidates are Role questions. I picked 20. Easy Role is thin: the corpus has 25 easy Role explanations out of 107, and no difficulty-1 candidate made this shortlist.

### Picks

| # | Slot | Diff | Sub-pattern / features | Rubric /12 | What makes it a model | Weakness | Golden? |
|---|---|---|---|---|---|---|---|
| 1 | PT135-S1-Q10 | 2 | Premise (final claim); prediction conclusion | 10 | Predicts with the four buckets (Premise / Support / Evidence / Partial Support). D (7%, "qualifies") gets a lesson on what "qualify" means on the LSAT, with before-and-after examples. A says what support for the claim would have to address. | B note is one line. | N |
| 2 | PT116-S2-Q2 | 2 | Concession: rebuts an anticipated objection ("Of course") | 11 | Names the concession cue words (Of course / Granted / Although / While). Writes out the objector's line ("Earth can't breathe!") and the author's reply before looking at choices. B is tested with its own internal logic ("insects don't breathe, so Earth isn't an organism?" makes no sense). | Traps are all 2-3%, so no long note is needed. | N |
| 3 | PT146-S3-Q4 | 2 | Concession: a conforming example of a rule the author then limits | 11 | Numbers the four moves (attributed rule, concession example, pivot to counterexample, rebuttal conclusion) and predicts "acknowledges some data fit the rule". The E note explains why a claim can be a concession rather than a reason. | A and B notes open with the same line. One jab in the breakdown ("rub it in the poor's face"). | N |
| 4 | PT146-S3-Q14 | 2 | Opposing hypothesis (someone else's explanation) | 10 | Recasts the argument as curious fact, their explanation, the author's explanation, with a crying-over-onions example. Teaches a fallback: if you only know the claim is Opposing, pick the only answer whose wording opposes. | D and E notes are short. | N |
| 5 | PT149-S3-Q6 | 2 | Premise under an implicit rebuttal conclusion | 11 | Explains the "90% first sentence or pivot" heuristic, including when it fails. E is eliminated from the direction of "Therefore" alone. "Many" vs "most" disposes of C and D. | Typo "rub out faces". | Y |
| 6 | PT119-S4-Q25 | 3 | Concession / qualification ("Although") | 11 | Sorts claims into conclusion, support, opposing, neutral, and uses "although" to predict a qualifying role that belongs to the author (a caveat, not someone else's view). D (11%) is rejected precisely: the concession admits overlap between roles, not an unclear distinction. | A note is one line. | Y |
| 7 | PT107-S4-Q2 | 3 | Role of a phrase (limits the conclusion's scope) | 10 | Teaches that a phrase with no subject and verb cannot be evidence or a conclusion, with a list of example phrases. "To the extent that" is shown to limit the claim, with an invented parallel. B's note shows that limiting scope is different from ranking causes. | Do not copy the A-note analogy: "Gilly's Games Guide ... Games section" refers to Logic Games, which conflicts with the no-LG rule. | N |
| 8 | PT110-S2-Q22 | 3 | Two attributions, implied rebuttal; "wrong opponent" traps | 10 | Explains a hard real-world background (capitalism predates industrialization) in plain language. A and B (11%, 8%) are shown to aim at the first sentence's position when the claim targets the second sentence's critics. "Contradiction" is taught as an extreme word. | C note stops at "conclusively prove" without more. | N |
| 9 | PT152-S4-Q6 | 3 | Intermediate conclusion in the last sentence ("Thus"); main conclusion first | 10 | Warns that Role is "super famous" for intermediate conclusions, so a final "Thus" needs a check. The correct note runs "why? because" twice to show the claim is both supported and supporting. E is placed as an inference from the hypothesis. | C (11%) gets one line. | N |
| 10 | PT155-S2-Q16 | 3 | First sentence is the intermediate conclusion; main conclusion last ("Hence") | 10 | Uses the support test to settle which of two conclusions supports the other (ask "why?" of each and see which answer fits). D's note builds a real "instance of a general conclusion" to show what D would need. | E note repeats B's text. C note is thin. | N |
| 11 | PT155-S4-Q17 | 3 | Premise supporting a chain of intermediate conclusions | 11 | Maps "Because 1, 2. As a result, 3. Thus, 4" and explains why the correct answer says "explanation for a premise": an intermediate conclusion is both a conclusion and a premise ("supported premise"). E (10%) is rejected by showing the argument has intermediate conclusions. | A and B notes are short. | N |
| 12 | PT123-S2-Q11 | 4 | Historical analogy used as evidence; rebuttal | 11 | The 21% trap D gets the longest note: it is evidence, but it names a different conclusion and ignores that the evidence is an analogy from centuries ago. The C note explains why the test avoided the word "premise" and what "example of a cultural change" is doing. | A note is one line. | N |
| 13 | PT151-S4-Q17 | 4 | Untenable consequence of the rejected view (reductio) | 11 | Separates a chain of implications from a chain of reasoning, using a Bruno Mars 1969 reductio as the parallel. That kills both A and E (18%), which treat the claim as something the author supports. | A and E notes are near-identical pasted text. Stray "T" in the D note. | N |
| 14 | PT145-S4-Q14 | 4 | Example ("For instance") supporting a supported premise | 10 | Walks every cue word (Obviously, Yet, For instance, consequently, Hence) and says which ones mislead. D (23%) is rejected on "directly": the example supports sentence 2, which supports the conclusion. B's note defines "the phenomenon the argument seeks to explain". | The E note runs everything together in one paragraph. | N |
| 15 | PT122-S2-Q12 | 4 | First-claim premise in a four-sentence build-up | 11 | Makes the stimulus concrete with the "pee before the car trip" analogy, then attacks the two popular traps. B (16%): a "phenomenon" needs a curious fact, and this has none. E (14%): the third sentence has no support, so it cannot be a conclusion. It also describes what support for it would sound like. | C note is one line (fine for a correct answer this plain). | N |
| 16 | PT147-S1-Q22 | 5 | Intermediate conclusion that denies the opposing argument's assumption | 11 | Works backward through an abstract correct answer: did the author reject reasoning? was something assumed? does the claim deny it? A (29%) gets a note that builds what a real alternative explanation would sound like. B (23%) gets a two-level support chain. | "Slow golf clap" joke at the answer. D note is slightly muddled about whose principle is questioned. | N |
| 17 | PT144-S3-Q17 | 5 | Premise vs intermediate conclusion (causal chain); prediction conclusion | 12 | C (26%) gets the most attention with the support test: common sense can make a claim believable, but only explicit support makes it a conclusion (the bucket-of-water example). E is killed on "not intended to support", then on its subtler first half. States that a prediction about the future is an opinion. | None significant. Named strong in the golden-set observations. | N |
| 18 | PT153-S3-Q8 | 5 | Two premises joined by "and"; no intermediate conclusion | 11 | Diagrams each abstract answer as an arrow chain ("Our Claim → IC → MC") and shows that B (29%) and C (21%) each invent an intermediate conclusion. Supplies what support for the claim would have to be ("life depends on water ... oxygen"). | Same example sentence repeated in three notes. | N |
| 19 | PT140-S2-Q24 | 5 | Chain of three conclusions (so, so, this suggests) | 10 | Labels each of the six claims with its keyword and job, then numbers the four-step chain in the correct note. B (23%) is eliminated at its first half, with the support test showing "so" means support was given. D's note works a number example on why complexity implies a long history. | Slip: "4.6 million years ago" in the C note (billion). | N |
| 20 | PT143-S3-Q20 | 5 | Potential objection countered by analogy | 10 | Uses the support test to classify the claim as Opposing ("Because transportation will be more expensive?" makes no sense). B is dissected: it would be tempting if "ships" read "jets". A (16%) and E (12%) are each broken at a specific phrase ("two analogies"; "in the conclusion"). | Transcription: the analogy table in the D note is flattened. | N |

Reserves, read and not picked: PT149-S4-Q15 (good support-test notes on A and C, same move as #11 and #17), PT127-S1-Q21 (noun-modifier-as-fact lesson; the correct note hedges), PT117-S4-Q24 (role of an opposing view with a partial concession; decent), PT150-S2-Q8 (the claim is the main conclusion; clean d2), PT111-S4-Q15 (good A note; one slip), PT115-S2-Q22.

### What the best ones do

- **Predict with four buckets first.** Main Conclusion, Support, Opposing, Neutral. Refine to premise vs intermediate conclusion only if the choices force it ("let's cross that bridge if we come to it"). (PT115-S2-Q22, PT145-S4-Q14, PT144-S3-Q17)
- **Use the support test to tell a premise from an intermediate conclusion, and describe the missing support.** "Why should we believe this? Support would sound like '...'. None is given, so it is a premise." (PT144-S3-Q17, PT153-S3-Q8, PT122-S2-Q12)
- **Name concessions and qualifications by their cue words.** Of course, Granted, Although, This may be true: the author's own opposing point, not an opponent's. Then write out the objection the concession answers. (PT116-S2-Q2, PT119-S4-Q25, PT146-S3-Q4)
- **Draw the hierarchy.** "Because 1, 2. As a result, 3. Thus, 4," or an arrow chain, so each abstract answer can be checked against the structure. (PT155-S4-Q17, PT153-S3-Q8, PT140-S2-Q24)
- **Work backward through a stacked abstract answer.** Take it piece by piece: did the author reject reasoning, was there an assumption, does the claim deny it? (PT147-S1-Q22, PT151-S4-Q17)
- **Give an invented parallel for an unusual structure.** Bruno Mars for a reductio, the car trip for acting early, a limiting phrase about a study guide. (PT151-S4-Q17, PT122-S2-Q12, PT107-S4-Q2, with the LG caveat)
- **Pin down the specific word that breaks a close trap.** "Directly" (PT145-S4-Q14 D), "ships" vs "jets" (PT143-S3-Q20 B), the wrong opponent (PT110-S2-Q22 A and B), "many" vs "most" (PT149-S3-Q6 C and D).
- **Teach LSAT vocabulary once, with examples.** Qualify (PT135-S1-Q10 D), phenomenon and explanation (PT122-S2-Q12 B, PT145-S4-Q14 B), contradiction (PT110-S2-Q22 B), supported vs unsupported premise (PT155-S4-Q17 C).

### What the weaker candidates got wrong

- **Answering about the wrong claim.** PT154-S2-Q18 builds its Goal and correct note around the second-sentence definition, but the stem asks about the "because" clause. That is disqualifying no matter how good the rest is.
- **Disowning or mocking the key.** "I really don't like this correct answer" (PT153-S3-Q20 A) before a reluctant defense. "This answer is gibberish" (PT104-S1-Q17 D).
- **"I have no idea what we should be looking for" with no fallback.** PT104-S4-Q24 and PT118-S3-Q23 admit it in the Goal. PT146-S3-Q14 shows the better version: say what little you know (Opposing) and use it.
- **Pasted notes.** The same paragraph repeated across two or three choices (PT151-S4-Q17 A and E; PT155-S2-Q16 B and E; PT113-S3-Q12 B through D).
- **Outside knowledge and loaded examples.** Superbug background (PT104-S4-Q24), organ-rejection biology (PT111-S4-Q15 D), a Biden/Trump example (PT118-S3-Q23 C), "believe the accuser" (PT153-S2-Q20 B).

### Fidelity problems

- **PT154-S2-Q18**: the Goal says "We're being asked about the 2nd sentence", and the C note asks whether "the definition in the 2nd sentence" supports the conclusion. The stem asks about the claim that abandoning any custom would destroy the culture, which is the "because" clause of the last sentence. The explanation is about a different claim. Disqualify.
- **PT118-S3-Q23**: the A note says "In my hypothetical, it would be clear that the vegetarian position is correct". The stimulus says it would be less clear.
- **PT104-S1-Q17**: the Evaluate paraphrase reverses the premise ("if a society's laws are helping citizens, then obviously society won't be stable"). There is also lost spacing ("Conclusionbefore").
- **PT104-S4-Q24**: lost spacing throughout ("peoplewhodotake"). Outside knowledge about antibiotic-resistant bacteria is used to frame the answer.
- **PT140-S2-Q24**: "4.6 million years ago" in the C note; the stimulus says billion.
- **PT111-S4-Q15**: the D note ends "which is how we know that the last sentence was supported by anything". It means "wasn't".
- **PT145-S4-Q22**: the breakdown labels sentence 1 "Evidence (for)", but "for" introduces "music is merely sound". The Evaluate template ("X is true. After all, Y and thus Z") does not match the stimulus.
- **PT143-S3-Q20** (D note) and **PT154-S2-Q18** (C diagram): side-by-side tables are flattened (transcription).
- **PT151-S4-Q17**: stray "T" in the D note. A and E are pasted duplicates.
- **PT107-S4-Q2**: not an error, but the A-note example is about a Logic Games guide. Do not carry it into student copy.

---

## Agree/Disagree

All 40 are Agree/Disagree. Agree-type stems in the shortlist: PT148-S1-Q18, PT146-S2-Q26, PT111-S1-Q26, PT152-S1-Q17. One EXCEPT: PT155-S4-Q19. I picked 20.

### Picks

| # | Slot | Diff | Sub-pattern / features | Rubric /12 | What makes it a model | Weakness | Golden? |
|---|---|---|---|---|---|---|---|
| 1 | PT145-S4-Q2 | 1 | Explicit clash on the conclusion; analogy reply | 11 | Goes claim by claim ("does Yvonne disagree?" yes/no with a reason). Every answer is tested for an Agree position and a Disagree position. E's note says what a legitimate version of E would have been. | Traps are 0-2%, so little trap teaching. | Y |
| 2 | PT144-S4-Q4 | 1 | Speaker 1 makes only one claim | 10 | States the rule: when speaker 1 makes one claim, speaker 2 has to be disagreeing with it. Each wrong answer is shown to have only one side supported, with Annette's position checked, not assumed (E note). | Very easy, so little trap depth. | N |
| 3 | PT149-S1-Q7 | 2 | Explicit clash found on the first claim; "both agree" traps | 10 | Stops the claim scan once an explicit disagreement turns up and says why that is enough. B and D are shown as both-agree using the matching quotes side by side. The C note: rejecting one method does not commit you to another being better (the Saturn example). | E note drifts into how science works in general. | N |
| 4 | PT153-S2-Q9 | 2 | Agree with the conclusion, reject the reasoning | 11 | Teaches that a speaker can accept the conclusion but reject the rationale (Lebron vs Jordan). Each wrong answer is checked for both positions, including the extreme wording "most important value" in B and E. | None significant. | Y |
| 5 | PT150-S3-Q20 | 2 | Clash on an unstated link between the claims (cite vs read) | 11 | Marks each of the student's claims as disagreed, agreed, or no comment. The correct note admits the answer is not the central fight and finds the unstated link the speakers treat differently. A trap (4%) is rejected on "are" vs "should". | Typo ("read whatever they with"). Goal predicted claim 1, not the answer. | N |
| 6 | PT114-S2-Q19 | 2 | Clash on the combined inference (1 → 3), not on either step | 11 | Lays out Beckstein's explicit claims and each implicit step (1 → 2, 2 → 3, 1 → 3), and shows Sedley only clearly disagrees with the combined step. That is the level the correct answer tests. The diagram makes it visible. | Wrong-answer notes are brief, but they state the reason. | N |
| 7 | PT105-S1-Q15 | 3 | Single claim each; one side's position in the other side's words | 11 | Predicts how LSAC will disguise the answer: speaker 2's position phrased in speaker 1's language (the correct note confirms it). A (14%) is rejected on relative vs absolute: "better use" does not mean "not good use". | B and D notes are short. | N |
| 8 | PT138-S3-Q25 | 3 | Explicit clash stated as a conditional | 10 | Explains the answer's conditional form: the disputed claim was itself a conditional. Gives the useful Harvard/Stanford rule (an obvious clash is often tested one layer down, on the reasons), and admits the rule did not apply this time. D (19%) is rejected as speaker-1-unsupported. | The Evaluate prediction missed the answer, and D's note is short for 19%. | N |
| 9 | PT111-S3-Q10 | 3 | Majority vs average; conditional reply ("If pay is the issue") | 11 | Shows the two numbers do not conflict (majority under $20k vs average over $29k), so A cannot be supported. B's note repairs the wording to show what B would need to be right. The E note uses a Lady Gaga example to teach that a conditional refusal is not a blanket refusal. | An aside questioning the question's premise ("weird that LSAC wants us to hear $29k as not underpaid"). | N |
| 10 | PT117-S4-Q10 | 3 | Implicit clash on disposition; no explicit denial | 10 | Models what to do when you first see no disagreement: question yourself claim by claim ("Does Q think people are predisposed not to pollute?") until the implicit clash appears. States the rebuttal position in plain words before testing support. | C note leans on common sense ("do we ever say pollution when not referring to people?"). | N |
| 11 | PT147-S4-Q20 | 4 | Assumption-level clash (why the pumps were shut) | 12 | Finds no disagreement with explicit claims, then lists Edgar's assumptions and tests each. It rejects "inconsequential" (C, 24%) because Rafaela calls the threat serious, not the fish. The correct note defends an extreme-sounding answer ("only reason") by showing Edgar really holds it. | None significant. | N |
| 12 | PT108-S3-Q20 | 4 | Definitional clash (what counts as "interpreting") | 12 | Explains how the speakers end at "always" vs "never": each uses "interpret" in a different sense. The correct note shows Ramon would contradict himself under Sarah's definition. A (18%) and B (12%) are split by "does" vs "should". | None significant. | N |
| 13 | PT101-S2-Q14 | 4 | Clash on the underlying reason; strength of the Disagree position | 11 | States the transfer rule (an explicit clash usually gets tested on the rationale underneath) and derives the social-drinker disagreement. D (18%) is rejected because disagreeing with "some" requires the extreme "not a single driver". The same move handles E in reverse. | "Migeul" typo. COVID aside. | N |
| 14 | PT118-S3-Q20 | 4 | "Always" vs "not always"; the E trap needs "never" | 11 | E (26%) gets the key strength test: to disagree with "sometimes desirable" someone must hold "never desirable", and Pat does not. B is derived by saying what Pat's "No, not always" commits him to. | C note is brief. | N |
| 15 | PT109-S3-Q19 | 4 | Clash stated as a conditional ("Any government that permits emigration...") | 11 | Uses the question "does Edward argue at least some governments have the right?" to find the explicit clash, and shows the answer rephrased in Edward's words. D (28%) gets the longest note: Edward might grant that taxation is force and still defend it. E is a reversal of Edward's conditional. | A note is a little long. | N |
| 16 | PT150-S3-Q15 | 4 | Strength words ("strongly supports" vs "sheer speculation") | 11 | Names the exact friction in the two speakers' words. A (23%) is rejected because Olson never claims primates are younger than 55 million years. The C note uses a polling analogy to show the model does not need a representative sample. | Minor typos. | Y |
| 17 | PT138-S2-Q21 | 5 | Disagreeing with a conditional (left side true, right side false) | 11 | Teaches that to deny a conditional you only need one case where the left side holds and the right side fails, then finds exactly that in Simon's reply. D is taken apart by contraposition. A and B are rejected as untouched by either speaker ("expected to lose" vs "would have lost"). | Transcription: the E diagram is flattened. "legal feels" typo. | N |
| 18 | PT155-S4-Q19 | 5 | EXCEPT: four disagreements and one without support | 10 | Resets the standard for EXCEPT ("most supportable", not explicit) and ranks how well each of A, B, D, E is supported, so the student sees why C, with no support for disagreement, is the odd one out. | Admits the weak support openly, which is honest but makes the notes long. | N |
| 19 | PT111-S1-Q26 | 4 | Agree stem; shared background assumption | 10 | States the pattern for Agree stems: the speakers usually clash, so look for background both accept. Walks both claims, then supports B from each speaker's own wording ("threaten" and "the promise of"). D (20%) is rejected because Hampton never discusses habitats. | C note is short. | N |
| 20 | PT152-S1-Q17 | 5 | Agree stem; two big traps (28%, 22%) | 10 | Uses a line-by-line A/?/table for Miranda's reactions. The C trap (22%) is named as a Necessary vs Sufficient error: no indoor seating means failure, but seating does not guarantee success. E's note builds "risky venture" from "not surprised" and "likely to fail". | The A note says Xavier claimed "no one" wants to sit outside (the stimulus says "few"), and its ketchup/mustard analogy is muddled. | N |

Reserves, read and not picked: PT120-S3-Q9 (ranking clash, "even more worthwhile" vs "what counts most", clean d4), PT137-S2-Q16 (assumption-level clash on genre, good), PT115-S4-Q7 ("at issue" stem, good B note), PT102-S4-Q22 (D disagree position too strong), PT129-S1-Q11, PT154-S2-Q25 (precise trap work, but a roughly 150-word riff on the name "Babson").

### What the best ones do

- **Go through speaker 1's claims one by one, asking "Does speaker 2 argue the opposite?"** Mark each as disagreed, agreed, or no comment before looking at the choices. (PT145-S4-Q2, PT150-S3-Q20, PT149-S1-Q7)
- **When no explicit claim is denied, list speaker 1's assumptions and test those.** That is how the implicit clash surfaces. (PT147-S4-Q20, PT117-S4-Q10, PT114-S2-Q19)
- **Test every choice for both positions.** "Can we support the Agree position? Can we support the Disagree position?" Say which side is missing, in that speaker's words. (PT153-S2-Q9, PT145-S4-Q2)
- **State the strength of the Disagree position.** To disagree with "some" or "sometimes" you must hold "none" or "never". That kills weakly worded traps, and the reverse kills strongly worded ones. (PT118-S3-Q20 E, PT101-S2-Q14 D and E, PT102-S4-Q22 D)
- **Separate "is" from "should", and "does" from "would".** A speaker who only talks about what should happen gives no position on what does happen. (PT108-S3-Q20 A and B, PT149-S1-Q3 B)
- **Watch for word-sense shifts.** Two speakers can reach "always" vs "never" by using one word two ways. (PT108-S3-Q20)
- **Predict the disguise.** One side's position phrased in the other side's words, or an explicit clash tested at the level of the reason underneath. (PT105-S1-Q15, PT101-S2-Q14, PT138-S3-Q25)
- **Handle conditionals.** Disagreeing with "if A then B" means holding that A can be true without B. A choice that reverses a speaker's conditional is unsupported. (PT138-S2-Q21, PT109-S3-Q19 E, PT140-S1-Q10 E)
- **For Agree stems and EXCEPT stems, reset the standard out loud.** Agree usually means shared background. EXCEPT means rank how supportable each disagreement is. (PT111-S1-Q26, PT155-S4-Q19)

### What the weaker candidates got wrong

- **Mocking or disowning the credited answer.** "Haha, what a garbage correct answer" (PT148-S1-Q18 D). "terribly written ... obnoxiously sloppy ... technically broken" (PT146-S2-Q26 E). Both are Agree stems, which is why the Agree slots went to PT111-S1-Q26 and PT152-S1-Q17.
- **Short notes on a big trap.** PT146-S2-Q26 gives the 26% trap B one line. PT109-S4-Q10 gives the 17% trap B one sentence with no reason.
- **Outside facts.** PT109-S4-Q10 adds a paragraph of Soviet history (glasnost, perestroika) with a political reading of the writers' motives.
- **Padding.** PT154-S2-Q25 spends about 150 words on the name "Babson" and adds an 8th-grade anecdote. The trap analysis is good, but the padding costs Clarity.
- **Slips that flip the logic.** "Yes, Y seems to agree" where the note means disagree (PT115-S2-Q23). "We can find support" where it means can't (PT103-S2-Q3).

### Fidelity problems

- **PT115-S2-Q23**: under X's 3rd idea the breakdown says "Yes, Y seems to agree" and then describes disagreement. It should say disagree.
- **PT103-S2-Q3**: the E note ends "We can find support for either person arguing that 'the institution of the family is still traditional'". It should say can't.
- **PT152-S1-Q17**: the A note says Xavier is "specifically saying that no one wants to sit outside + breathe exhaust". The stimulus says "few people".
- **PT148-S1-Q18**: calls the correct answer "garbage" (tone). The C note says neither speaker discussed violence causing violence; that is fair, but it is the only distinction offered for a 16% trap.
- **PT146-S2-Q26**: the correct note argues the key reads "backwards" before accepting it (tone / disowning).
- **PT109-S4-Q10**: outside history in a "p.s." with a political characterization. The B note gives no reason.
- **PT138-S2-Q21**: the conditional diagram in the E note is flattened (transcription). "legal feels".
- **PT108-S2-Q11**: the conditional diagram in the D note is flattened ("~unique meth not genuinely auto disc → and~unique domain").
- **PT111-S3-Q10**: an aside second-guesses the question's premise ($29k as not underpaid). Keep it out of new copy.
