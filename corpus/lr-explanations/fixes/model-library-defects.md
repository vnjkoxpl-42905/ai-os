---
type: fix-detail
subject: Defects in existing LR explanations found while building the model library
created: 2026-09-27
---

# Defects found while building the model library (2026-09-27)

Each helper read the candidates for its types in full and checked every choice note against the printed answer text. These are the problems they reported, copied from the fidelity sections of each file in [[../models/index|models/]]. Existing explanations are not being edited now; this is the queue for the revamp track.

## Flaw

### Flaw: 4. Fidelity problems found
- **PT146-S3-Q1 (A note):** reads the answer back as "quite unlikely to be unrepresentative". The choice says "quite likely to be unrepresentative". This inverts the key's own wording. (slip)
- **PT120-S4-Q23 (C note):** diagrams the answer as "if more than 10 absent → normal rate". C says the normal rate is reached *only when* no more than the average are absent, so the diagram should end "→ not normal rate". (slip; picked anyway, and the note should be corrected before anyone copies it)
- **PT113-S2-Q25 (B note):** "Since this answer starts with fails to consider / ignores the possibility". B actually starts "denies the possibility". The prefix-driven test is applied to a prefix the choice does not have. (misdescribes the choice)
- **PT111-S1-Q17 (Evidence step):** "under the ice sheet covering central America". The stimulus says central Antarctica. (slip)
- **PT103-S2-Q21:** the A note says "The prosecution isn't arguing ...", but the speaker is Ziegler's attorney (the defense). The Evaluate step has a garbled sentence ("what is the evidence he was that we was insane"). (slip)
- **PT122-S2-Q23 (Evaluate):** a truncated parenthetical, "(I even wrote )". (transcription)
- **PT138-S3-Q16 (Evidence step):** the conditional is scrambled across columns ("If people believe that important problems can then people be addressed only by → become large numbers of ppl unenthusiastic ..."). It cannot be read. (transcription)
- **PT124-S2-Q11 (Evaluate):** the chain line "major invest → high S.O.L → maintain in impr Inf. funct. Inf" is garbled. (transcription, minor)
- **PT107-S4-Q18 (D note):** the diagram "Action appears → could be describe in altruistic terms of self-interest" puts "altruistic" on the wrong side, and "it must be true that ." ends in a blank. (transcription)
- **PT147-S1-Q15 (Evaluate):** "Unproven vs. Proven True" should be "Proven False". (slip)
- **PT154-S1-Q9 (Evaluate):** "Only / only if are necessary indicators (the only is sufficient)" is a confusing parenthetical. (minor slip)
- **PT138-S2-Q24 (A note):** "Any time on LSAT that we see 'If [conclusion] ...', it will be wrong" is an overbroad rule stated as fact. The C note puts a sample answer labeled "A)" inside the C note. (register / slip)
- **PT154-S2-Q12 (D note):** "this formulation of the Causal flaw answer is always wrong" is an overclaim. (register)

No candidate had a correct-answer note arguing for the wrong key. There was no mocking of the question at the "hot garbage" level. The worst tone is PT113-S3-Q9's aside in the correct note.

## MBT-MBF

### MBT-MBF: 3. Fidelity problems found (all candidates read, picked or not)
### Must Be True / Most Supported
- **PT145-S2-Q23** (picked, golden): D note says "Most of Moradco's Velyena mines have violated" where it means "have never violated".
- **PT145-S4-Q13**: E note refers the student to "the explanation for (C)"; it means (D).
- **PT111-S3-Q18**: every conditional chain is flattened onto one line and unreadable; the A contrapositive ("not → not → not → not 4th 3rd 2nd 1st") is garbled. (transcription)
- **PT108-S3-Q23**: chains flattened in Statements and in the B and E notes; the A note never actually says why A is wrong. (transcription)
- **PT140-S3-Q17** (picked): Statements and Evaluate diagrams flattened; the choice-note diagrams survive. (transcription)
- **PT106-S2-Q19**: worked-number tables collapsed with run-together words ("150pieces of mail 100 correctly addressed50incorrect"). (transcription)
- **PT116-S3-Q21**: C diagram garbled ("participated → not attended → not received in arts fair spring cleanup certificate"). (transcription)
- **PT149-S3-Q21** and **PT107-S1-Q21**: A notes claim the tempting wrong answer is deliberately placed in slot (A). Unsupported; PT107-S1-Q21 also has "they usually but" for "put", and its D note claims D and C are equivalent, which is questionable.
- **PT154-S2-Q22**: C note reuses B's closing sentence about late-career originality, which does not address C's oil-painting claim.
- **PT127-S1-Q17**: D (22%) and E notes are identical.
- **PT107-S4-Q23**: B and C notes paste the same one-claim paragraph. Uses outside astronomy numbers (age of universe) only as illustration, not to justify the key.
- **PT143-S3-Q24**: "woke consumerism instinct" aside in Evaluate (tone, not accuracy).
- **PT118-S1-Q22**: C note repeats itself mid-paragraph ("But more than one thing can be responsible...").
- **PT101-S3-Q7** (picked): typo "make them now too bad" (not too bad).
- **PT155-S1-Q15** (picked): not an error, but note that the correct-answer note openly says E adds an assumption (allowed outside vs outside). Keep that honesty if modelling it.

### Must Be False
- **PT145-S2-Q25**: B and E notes assign contradictory ranks ("northern fur seals (4th) > (elephant seal) (2nd)"; "Weddell seal (4th) > (dolphins) (1st)"). The key is right but those notes are nonsense. Not picked for this reason.
- **PT124-S2-Q2**: B note says Samantha's friends "all like green tea"; the stimulus says black tea.
- **PT152-S2-Q24**: D and E notes say "we can contradict this fact"; they mean "can't". The notes are also identical.
- **PT122-S4-Q5**: Evaluate says "we already know that all veterinarians ARE devoted to biological science and DO love animals"; the stimulus gives Most, not All. Contrapositive diagram also garbled.
- **PT116-S3-Q17**: Goal's second contradiction pattern reads "favored / does offer a net gain"; it should be "not favored / does offer a net gain". The choice notes get it right.
- **PT151-S2-Q22**: D note says people who dislike each other have "at least once treated each other with respect"; the stimulus says only that they may.
- **PT114-S4-Q25**: D note typo "Religious music can stand independent of religious music" (should be "of religious worship").
- **PT111-S4-Q22**: Experiment step is truncated mid-word ("gamma interferon is an ant"). (transcription)
- **PT106-S1-Q20**: run-together words ("arenottrue", "investmentweak") and flattened chains throughout. (transcription)
- **PT129-S3-Q14**: A and B notes are transcription-damaged and self-contradictory (B: "OCF + ~LN ... the food has no fat"). Also a principle-violation question rather than MBF.
- **PT112-S4-Q7**: em-dash-heavy register in a different voice; accurate, not a style model. (register)
- **PT129-S2-Q23**: em-dash in Evaluate; thin notes. (register)
- **PT153-S3-Q16** (picked): A note calls an answer "automatically garbage". Mild; a jab at an answer, not at the question.
- **PT146-S3-Q22** (picked): Maples is "his" in one note and "her" in two others.
- **PT127-S3-Q22**: Evaluate's second inference ("members of a given species tend to face similar daily challenges") reverses the stimulus's support relation. Minor.
- **PT108-S3-Q18**: bank tags it "Games-y LR". Worth knowing given the no-Logic-Games rule for student copy; the explanation itself does not mention games.

## MC-Role-Agree

### MC-Role-Agree: Fidelity problems
- **PT112-S3-Q23**: the breakdown's Conclusion line reads "The union's strength was declining". That is the article's claim. The author's implied conclusion is the opposite (Evaluate and Goal state it correctly).
- **PT102-S4-Q1**: the breakdown's Conclusion line says "a prime example of fiscal responsibility". The stimulus says "irresponsibility". The Goal step has it right.
- **PT146-S2-Q14**: the C note says "For a meeting to be Z, it needs to have Y and Z", with the variables garbled. It should be X and Y.
- **PT140-S1-Q7**: the A note restates the author's view but never says why A is wrong. The E note calls a conclusion-plus-premise answer an LSAC "mistake"; that answer shape is not rare.
- **PT115-S2-Q1**: the side-by-side synonym match in the C note is flattened into one line (transcription).
- **PT106-S1-Q18**: formatting loss merged words ("author'sOpinionshining", "massive interventions(like", "=We need to take into account").
- **PT153-S3-Q9**: "99.8%" and "100% guaranteed" are overclaims, not errors of fact about the question.
- Off-type items (listed above) were not audited for fidelity. One noticed in passing: in the PT159-S3-Q17 B note, the diagram is labelled "(A)".

---

### MC-Role-Agree: Fidelity problems
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

### MC-Role-Agree: Fidelity problems
- **PT115-S2-Q23**: under X's 3rd idea the breakdown says "Yes, Y seems to agree" and then describes disagreement. It should say disagree.
- **PT103-S2-Q3**: the E note ends "We can find support for either person arguing that 'the institution of the family is still traditional'". It should say can't.
- **PT152-S1-Q17**: the A note says Xavier is "specifically saying that no one wants to sit outside + breathe exhaust". The stimulus says "few people".
- **PT148-S1-Q18**: calls the correct answer "garbage" (tone). The C note says neither speaker discussed violence causing violence; that is fair, but it is the only distinction offered for a 16% trap.
- **PT146-S2-Q26**: the correct note argues the key reads "backwards" before accepting it (tone / disowning).
- **PT109-S4-Q10**: outside history in a "p.s." with a political characterization. The B note gives no reason.
- **PT138-S2-Q21**: the conditional diagram in the E note is flattened (transcription). "legal feels".
- **PT108-S2-Q11**: the conditional diagram in the D note is flattened ("~unique meth not genuinely auto disc → and~unique domain").
- **PT111-S3-Q10**: an aside second-guesses the question's premise ($29k as not underpaid). Keep it out of new copy.

## NA

### NA: 4. Fidelity problems found
- **PT127-S1-Q13 (pick 3):** Goal says "staying" for "stating". It also says "ruling out the idea that other aspects ... do not make top-loaders the better overall choice", which is the reverse of what it means.
- **PT118-S3-Q19 (pick 12):** B note says "they spend 10% as much time on curative, even though curative cuts down medical costs greatly"; both should be "preventive". The Evaluate linking diagram is flattened.
- **PT122-S1-Q10 (pick 7):** Goal diagram garbled ("any fly with no UV has means no UV damage to this gene").
- **PT140-S2-Q6 (pick 11):** A note says "causal chain is motion" (should be "in motion").
- **PT148-S1-Q5 (pick 5):** "in danger of surviving" (should be "not surviving"); "no let's negate" (should be "so").
- **PT148-S4-Q18 (pick 18):** Evidence reads "Some the proposed tax reform bill" (the verb "criticize" is missing).
- **PT150-S2-Q12 (pick 2):** in the D note, a hypothetical is labeled "(A)" and could be misread as the real choice A.
- **PT154-S1-Q18 (already golden):** A note has a garbled sentence ("This is talking about paying more attention not being helped extra").
- **PT140-S3-Q19, PT121-S1-Q20:** timeline and diagrams flattened into one line (transcription).
- **PT104-S1-Q21:** missing spaces throughout ("shouldnotexport", "Swould beavailable", "mosteffective").
- **PT105-S2-Q20:** missing spaces ("doeshave", "not because").
- **PT109-S3-Q25:** D note says "needs of business schools" where the stimulus means "needs of business".
- **PT143-S4-Q20:** the Evidence step adds a premise that is not in the stimulus ("If the rain forests are not preserved, then thousands of plant species ... will be lost").
- **PT108-S3-Q1 (EXCEPT, not picked):** the Goal says the author assumes "there's some other way to address bias that would be at least as effective as trained editors". That is backwards; the author assumes there is no other way that works as well.
- No choice note misquotes or describes the wrong choice among the 20 picks. I checked each against the printed choice text.

## Paradox-Method

### Paradox-Method: Fidelity problems found (Paradox shortlist)
- PT128-S2-Q19: B note misreads the choice ("If most crimes are reported"); the choice says most crimes are **not** reported. Correct note also uses a sexual-harassment example, which is a poor fit for student copy.
- PT149-S1-Q10: author disowns the question ("hot garbage", "ignore this question ever existed"). Disqualify.
- PT137-S4-Q3: Evaluate analogy is built on Logic Games practice. Conflicts with the no-LG rule for student copy; otherwise a decent explanation.
- PT143-S1-Q19: worked example moves from OKC to "Austin" mid-sentence.
- PT143-S3-Q5: A note says "The town is not an economic wasteland"; the sense needs "now".
- PT126-S4-Q5: conditional diagram lost its line break ("needed drugsdidn't receive drugs").
- PT104-S4-Q8: B note has lost spaces ("formostconsumers").
- PT106-S1-Q17: Evaluate's number layout is flattened ("mallyet,Local economy").
- PT140-S2-Q7: missing word ("grain might be a very part"); A and D notes are identical.
- PT112-S4-Q5: Evaluate numbers two routes "2."; B note uses a real-politics example (Trump, Biden, Yang).
- PT148-S4-Q3: E note stops before the verdict (never says the choice points the opposite way).
- PT122-S1-Q4: D note describes the reconciliation a random fluctuation would give, but never finishes the thought that D rules that out.
- PT144-S3-Q5: typo "The work 'some'".
- PT143-S1-Q6 (golden): the Evaluate brainstorm says carbon monoxide causes lung cancer. Outside the choice notes, but a factual slip to avoid copying.
- PT143-S1-Q21: Strengthen stem, not Paradox. Skipped (the explanation itself is good, especially the E note on the background constraint).
- PT106-S3-Q13: "resolve the dispute in favor of one party" is closer to Strengthen; skipped.

---

### Paradox-Method: Fidelity problems found (Method shortlist)
- PT148-S1-Q20: calls the correct answer "so, so dumb" (already noted in the golden-set survey). Disqualify.
- PT138-S3-Q20: "real crappy argument", "This correct answer is miserable", and an Elon Musk aside. Tone disqualifies.
- PT152-S1-Q24: "random-ass pile of scouring pads" in the C note.
- PT135-S4-Q16: Goal says "the critic responded by saying that the trigger ... didn't apply"; it is the economist.
- PT151-S4-Q21: D note says the claim "has been attributed to anyone"; the sense needs "has not been".
- PT106-S1-Q7: E note says "mental disorders"; the stimulus is about neurological disorders. Lost spaces ("arenotviolating").
- PT105-S2-Q21: lost spaces and a flattened diagram in the A and C notes ("thatif ... would bealmost everybody", "arenotbeing met"). Otherwise a good contrapositive-of-a-counterfactual model; usable only after cleanup.
- PT119-S2-Q17: typo "The does conclude".
- PT133-S3-Q19: typo "The is answer".
- PT137-S2-Q12: Evaluate sentence "to rule out the possibility that dosage wasn't the problem, herbal interference was" is a muddled double negative.
- PT111-S3-Q23: royalty arithmetic in the Evaluate is garbled (labels "$20 royalty" once but totals two). Also a different type (below).
- PT112-S3-Q8 and PT102-S4-Q19: bank tag fields are garbled or blank. The explanations themselves are fine.
- Different type, skipped: PT103-S2-Q25 (Necessary Assumption stem), PT151-S2-Q5 (Necessary Assumption), PT115-S2-Q7 (necessary for a method to work; NA in practice), PT122-S4-Q8 (weaken a method's reliability), PT101-S2-Q10 and PT131-S1-Q14 (Role), PT111-S3-Q23 (what conclusion the reply leads to), PT148-S1-Q12 (Paradox; moved to the Paradox table).

## Parallel

### Parallel: 4. Fidelity problems found
- **PT148-S3-Q26:** printed choice D reads "if a movie is quite unpopular, it will probably not be made into a movie". This looks like corrupted bank text (the matching version is "if a novel is..."). The note does not notice. The Evaluate step also flips a sign ("it wouldn't be true that 'if a country is new, it's probably ruled by a monarch'" should be "probably not ruled"). Its algebra table is flattened.
- **PT142-S4-Q19 (picked):** the Goal recipe is written as the reversal (A → B; X was B; so X probably A). The C note uses the correct form. Fix the Goal before using it as a model.
- **PT140-S3-Q24:** C note says neither premise has an "or" in the outcome. C's first sentence ("blurred or dark if the camera is not working properly") is exactly that.
- **PT106-S2-Q15:** E note says the conclusion is "Mark will not go to the museum". Printed E concludes "he will go to the museum". There are also lost spaces throughout.
- **PT151-S4-Q25:** B note has a pasted fragment mid-sentence ("...functionally equivalent to what the taxes are increased", so the conclusion should be...").
- **PT136-S2-Q16:** Opposing Support misstates the owners' belief with a double negative ("do not believe that ... would not cover").
- **PT151-S2-Q19 (picked):** "Monroe" for Munroe in the breakdown (cosmetic).
- **PT111-S4-Q23 (picked):** duplicated words in C note ("can' apply the can't apply").
- **PT106-S3-Q26 (picked):** lost spaces in A and C notes.
- **Stray em dashes** (single, not the heavy register): PT120-S1-Q15 A note, PT149-S4-Q23 Evaluate code block. Strip them in any adapted copy.

---

### Parallel: 4. Fidelity problems found
- **PT126-S4-Q24:** tone ("train that wrecked into a dumpster fire"); the author says they do not understand what the test writers meant. Disqualify.
- **PT120-S1-Q21:** B note says "Intro to English" where printed B says the introductory course in engineering.
- **PT140-S3-Q15:** E note ends "there's a premise that's a specific type of hiker". Printed E has no such premise (it is about trails in two regions); the sentence contradicts its own point. Evaluate also brings in outside facts (microscopic organisms lack nervous systems) to explain the flaw.
- **PT152-S1-Q25:** A note's objection reads "Couldn't Morgan be the one who's wrong?" The conflict in printed A is the TV news vs. the newspaper report, so the objection should be "couldn't the TV news be wrong?"
- **PT138-S2-Q25 (golden):** Evaluate says the "only if" term goes on the right side "(sufficient condition)". It should say necessary.
- **PT146-S1-Q21 (golden):** E note's last sentence is garbled ("Some cosmetics sell shampoo, and some cosmetics and toothpaste"); already noted in golden-set.md.
- **PT155-S1-Q8 (picked):** Evidence restates "does not have both" as "doesn't have X and doesn't have Y". The Evaluate diagram (~A or ~B) is correct.
- **PT105-S2-Q17:** Goal recipe ends "X was true for Thing B" (should be Thing A). Lost spaces throughout.
- **PT106-S1-Q3, PT106-S2-Q20, PT108-S2-Q21 (C note):** lost spaces between words.
- **PT140-S2-Q23:** breakdown and D table flattened beyond reading.
- **PT117-S2-Q22 (picked):** "Jenn" for Jane (cosmetic).
- **Stray single em dashes:** PT153-S3-Q11 E, PT152-S1-Q25 B, PT140-S3-Q15 A. Strip them in any adapted copy.

## Principle

### Principle: Fidelity problems found
- **PT101-S2-Q25 (disqualify):** The C note diagrams a trigger about "a hardship greater than the gain they were anticipating", but printed C says "expect that most people will accept the claim as true". The D note diagrams "no possibility that someone will act as if the claim might be true", but printed D says "ethical only if those making it have good intentions". Two notes describe choices that are not on the page.
- **PT106-S2-Q12:** The C note reverses "justified only when all alternative strategies ... have failed" into "failed → justified". It also says we don't know whether George tried alternatives, but the stimulus says "After several attempts to distract".
- **PT149-S4-Q21:** Mocking tone at the open ("Reddit badge for 'Least readable'"). The D note diagrams "understand justice" where the choice says "injustice".
- **PT104-S1-Q24:** Transcription damage: dropped spaces ("requireexclusivedependence", "ispreferable", "theopinion indicator").
- **PT107-S1-Q22:** The Goal and D diagrams are flattened into unreadable single lines.
- **PT134-S1-Q12:** Diagrams are flattened. The C note says the principle tells "the government whether or not to advocate", but C governs the advocate ("one").
- **PT144-S2-Q14:** A through D notes are pasted. The E note says "It's pretty shocking that LSAC would ask us", which is mild disowning.
- **PT113-S2-Q22:** The C note rejects the choice using outside claims about judges' sentencing discretion.
- **PT137-S4-Q8:** The B note leans on speculation ("salt is probably the cheaper option"). This is used against a wrong answer, not for the key, but it is still outside reasoning.
- **Type mismatch:** PT152-S2-Q21 ("The principles cited ... justify the reasoning in which one of the following") is Principle-Conform, with the principle in the stimulus and applications in the answers. I scored it under Conform.

---

### Principle: Fidelity problems found
- **PT119-S3-Q8:** The correct-answer (D) note ends "(E) still feels the most supportable", which is the wrong letter. It also has "- paragraph" artifacts.
- **PT117-S2-Q12:** The A note has five stray "- paragraph" lines (transcription damage).
- **PT105-S4-Q24:** Transcription damage (dropped spaces such as "cannotremainfree" and "don't earn X → won't havebest chance"), flattened diagrams, and a bare "Goal" line with no header. The Evaluate also uses a sensitive outside example.
- **PT109-S1-Q18:** The D note says "It shouldn't surprise us that they have asked about whether it's damaging the ozone layer", but the conclusion is that they have *not* considered it.
- **PT139-S4-Q6:** The C note says "on the board" three times where the rule is about the finance committee.
- **PT140-S1-Q25:** The Goal checklist is numbered 1, 2, 4, 3.
- **PT120-S1-Q7:** The D note argues that Terry ignores mitigating circumstances but never states the verdict (that means Terry follows D).
- **PT159-S3-Q14:** Typos ("stimlus", "surrouding"). It is also a Most Supported subtype by its own admission.
- **PT148-S4-Q6:** Evaluate disowns the stem ("a stretch to call this an argument ... a Necessary Assumption question as our tagging does"). This is mild, but it should not be copied.
- **Type mismatches in this shortlist:** PT134-S2-Q23 (flaw in the application), PT149-S4-Q17 (the principle most undermines), PT142-S4-Q12 (reconcile an apparent conflict), PT159-S3-Q14 and PT136-S2-Q9 (a proposition illustrated, closer to Most Supported). Stems of the "must be assumed" / "depends on assuming" kind (PT146-S1-Q24, PT155-S1-Q12, PT127-S2-Q20, PT102-S2-Q24) are principle Necessary Assumption. I kept one (PT102-S2-Q24) because the family bucket includes them.

## Strengthen-SA

### Strengthen-SA: Strengthen fidelity problems
- **PT142-S1-Q2:** the C note calls the Parthenon "a government building, I believe". That is wrong (it is a temple) and it is outside knowledge. It is not used to justify the key.
- **PT108-S2-Q14:** the B-note diagram is flattened ("IF British govt THEN the UFOs withholds info → ...") and reads wrong as printed. The prose around it is fine.
- **PT141-S2-Q22:** uses "genetic drift" for natural selection. The A note leans on an outside definition of species (they cannot interbreed).
- **PT148-S1-Q11:** B note has "of 'Effect w/o Cause'" (should read "or"). C and E are duplicates.
- **PT146-S3-Q21:** the A note is one flattened paragraph (transcription).
- **PT113-S2-Q6:** typo "world $500" for "worth $500".
- **PT143-S3-Q21:** typo "he heard" for "we heard".
- **Choice-text fidelity:** I checked every picked note against the printed choices and found no misquotes.
- **Type check:** all 40 Strengthen candidates are Strengthen. PT154-S2-Q16 is a "strengthen the grounds" variant and PT150-S2-Q7 is "justify the contention"; both still behave as Strengthen.

---

### Strengthen-SA: Sufficient Assumption fidelity problems
- **PT144-S2-Q22 (excluded).** The Evaluate diagrams lost their negations. The text reads "serves purpose → provides legal protection / provides legal protection → serves purpose" and "email suggests something illegal → provides legal protection", which state the opposite of the argument. The either-way A note is strong, but the diagrams now teach the wrong logic.
- **PT152-S4-Q3:** the D note says "We were never told that 'these regular smokers rarely look at the packaging'" when it means "We were told". That slip reverses the trigger check on the correct answer.
- **PT115-S2-Q21:** the A note ends mid-sentence ("Most skilled artists are") and is truncated.
- **PT146-S2-Q9:** "journey will reveal" for "journalist" (twice).
- **PT118-S1-Q23:** "never no" for "never know".
- **Inline diagrams:** many d4-d5 picks (PT118-S1-Q21, PT118-S4-Q22, PT113-S4-Q20, PT139-S4-Q21, PT112-S1-Q26) have flattened diagrams. The prose still carries the logic, but new explanations should use code-block diagrams like PT153-S3-Q3 and PT154-S4-Q20.
- **Not SA by type** (skip for this library):
  - PT102-S4-Q7 and PT104-S1-Q16 ("do most to justify"). The explanations themselves call these Strengthen, and the PT102 key is argued as a necessary assumption.
  - PT143-S3-Q12 ("justifies the application of the policy") is Principle, applying a stated policy.
- **Choice-text fidelity:** no misquoted choices found in the picked notes.

## Weaken-Evaluate

### Weaken-Evaluate: Fidelity problems found (Weaken)
- PT139-S4-Q7 (D note): "The author is promising that we can find an audio version" should read "is not promising".
- PT142-S2-Q20: the Goal says the computer may have generated "tons of false negatives", and the C note says "the doctor won when it came to false negatives". Both should be false positives (the cardiologist was better on cases with no heart attack). Not picked.
- PT106-S2-Q25 (Evaluate step): "Given that ... her blinking was voluntary" should be her humming, and involuntary. Missing spaces too ("it'snotinvoluntary", "Marianneshouldbe"). Not picked.
- PT119-S4-Q17: the causal-chain diagram is garbled. The C note relies on outside chemistry. The B note admits it uses outside knowledge.
- PT109-S4-Q19: "FOOTNOTE:" pasted mid-sentence in the B note.
- PT106-S3-Q11 (C note): the worked-number table is flattened and unreadable. PT140-S1-Q13 (E note): the rule-of-thumb chart is flattened.
- PT121-S4-Q9 (golden): stray "- paragraph" line in C.
- PT141-S2-Q9 (E note): "Probably now" should be "not". PT154-S4-Q22 (C note): "spots" should be "sports". PT103-S3-Q24 (D note): "cars told" should be "cars sold".
- PT105-S4-Q5 (D note): "as this correct answer shows" refers to B, not D.
- Tone flags: PT146-S2-Q22, PT120-S1-Q22, PT144-S4-Q23 (disqualifying). PT154-S4-Q22 D ("legendarily horrid correct answer") and PT140-S2-Q12 C ("His name is Greg and he sucks") are milder.

---

### Weaken-Evaluate: Fidelity problems found (Evaluate)
- PT139-S1-Q5 (E note): describes a different choice. It repeats B's reasoning ("The study controlled for how much coffee was consumed"), but printed E asks whether people with arthritis are less likely to drink coffee of any kind. The C note also points to a missing link ("try this one"). Excluded for this. The rest is model-quality, so fixing E would make it pickable.
- PT146-S3-Q8 (C note): "the exact same evidence X the courtroom" is missing "outside".
- PT142-S1-Q21 (Goal): the sentence is cut off after "undermining the plausibility".
- PT150-S3-Q21: printed choice E is truncated in the source ("Was the finance minister in office when the last").
- PT104-S4-Q6: missing spaces ("wouldstrengthen", "wouldnotbe", "destroyingmost").
- PT108-S2-Q9 (E note): "proceeding" should be "following".
- PT146-S2-Q16 (A note): outside-knowledge p.s. about roast caffeine. Not used for the key, but it should not be copied.
- PT148-S4-Q22 (A note): applies a Necessary Assumption rule on an Evaluate question. The reasoning still holds, but the label is wrong.
- Tone: PT146-S3-Q23 C, PT138-S2-Q14 opening.

