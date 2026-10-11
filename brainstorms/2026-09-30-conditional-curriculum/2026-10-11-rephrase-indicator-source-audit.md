# These sets supply a progression from spotting words to preserving complete conditions

Date: 2026-10-11. Read-only review of all four files assigned from `C:/Users/Joshu/Desktop/Conditionals - Final Set/Group 1 and 2 - EVERYTHING/`. Sources were not changed. This is an analysis and integration recommendation, not ingestion or app implementation.

## What was examined

Every numbered worksheet prompt and every answer-key entry was read. PDF text was extracted with pypdf; Word paragraphs were read from document.xml, including all three sections. All nine PDF key pages were rendered with pypdfium2; visual inspection covered indicator-key pages 1 and 3 and rephrase-key pages 1 and 3, confirming arrow direction, slash notation, and the actual unmarked group-label answers. The remaining pages were read as text, not visually inspected. Text extracts and rendered key pages are in sibling `2026-10-11-rephrase-indicator-extracts/`.

| ID | File relative to source root | Pages | SHA256 |
|---|---|---:|---|
| RW | If-Then rephrase set (Sep 5)/Homework/2025-09-05_IF_THEN worksheet.pdf | 7 | 6e889126da7457708b435ef73d3ccaeec4824ebddfafea6e72881e3f77090ff8 |
| RK | If-Then rephrase set (Sep 5)/Answer Key/2025-09-05_Answer Key.pdf | 5 | d7b334632a0b5a4259095d88f42844816a9a73848e7c6afcb87d3f6a676c8650 |
| IW | Indicator ID set (Part 1)/Homework/2025-09-03_G1 &G2 worksheet (1) (1).docx | Reflowable DOCX | 43dbf02fd4f7ec1002dac4aa69b383eafc110dd2259044a53b1383c2a0935f6d |
| IK | Indicator ID set (Part 1)/Answer Key/2025-09-03_G1 & G2 Answer key (1) (1).pdf | 4 | 6f7761e1a1c66ce691e3c805220b15107883bf764a9b4e687e5c95af6ab6c155 |

IW metadata says Pages=1 but Words=0/Characters=0 and is stale, so it is not a rendered page count. Cite IW by Part/item, and its paired IK page instead of inventing Word pagination.

Counts: RW has 25 prompts, each requesting if/then, contrapositive, indicator and one group label. IW Part 1 has 13 indicator-label prompts; Part 2 has 10 diagram/role prompts; Part 3 has 20 prompts asking original diagram, contrapositive diagram, ordinary if/then, ordinary contrapositive. Total 68 task instances, 58 distinct stems: all 10 Part 2 stems repeat Part 1. Keys are paired answers, not extra questions. The full four-file comparison found no missing numbered prompts.

## Decisions needed before importing

1. **A group belongs to an indicator, not to the whole sentence.** RW Q1,6,7,11,20,25 combine Group 1 and Group 2 expressions, yet the sheet says check one and the key says Sufficient for both. Students who identify `must`, `requires`, or `always` correctly could be marked wrong. Ask students to select each indicator and label its role separately, or name the specific indicator to classify.
2. **Resolve `the only` consistently.** IK Part 1 Q4 assigns Group 2 to “The only foods that spoil quickly are those without preservatives.” RW quick guide and Q4,10,22 classify `the only` Group 1. Under the existing convention, spoil quickly is sufficient and without preservatives is necessary. IK supplies no circle/underline showing whether it classified `only` inside the phrase or the complete `the only` expression. Do not import this binary label unchanged.
3. **Preserve permission and requirement language.** RW Q8 changes “can apply” into “applies.” IK Part 3 Q8 and Q18 change “can occur/can be processed” into actual occurrence/processing. Those are not faithful equivalent paraphrases. Keep eligible/can apply and can be processed throughout original and contrapositive. Do not equate a requirement with proof that a person actually complied unless the exercise explicitly treats the statement as an exceptionless factual rule.
4. **Keep scope and time restrictions.** IK Part 2 Q10 and Part 3 Q12 drop `before` in the answer. RW Q18 loses `currently`; Q17,19,25 compress matching/ownership restrictions; these are repairable but counterproductive in a lesson about complete conditions. Keep the full target in feedback even if a diagram uses an explicitly defined abbreviation.
5. **Repair the borrowing answer.** IK Part 2 Q6 changes “requires collateral” to “collateral secures a loan.” A requirement for collateral does not establish that collateral successfully secures the loan. Use a clearer statement such as “A loan is granted only if collateral is provided,” then diagram that exact rule.
6. **Gate contrapositive work.** Both sets require contraposition extensively. Their vocabulary is Group 1/2, but their reasoning requirements exceed the opening sufficient/necessary/arrow sequence. Separate forward translation items from later contrapositive tasks rather than putting the entire PDFs into Drill 1.

## Rephrase ledger: all 25 prompts

`Sound` means the intended one-way relation and reversed-negated relation are valid under the worksheet's stipulated-rule reading. It does not endorse the real-world truth of an invented rule. `Repair` means exact wording or scoring needs change. Indicator labels use the source convention, with mixed-indicator problems explicitly noted. Every row includes the worksheet and key page; all four requested answers were examined.

| Item; RW/RK page | Focus and intended relation | Key audit / integration |
|---|---|---|
| Q1; 1/1 | all + must; marathon runner → hydrate beforehand | Repair. Mixed groups forced to one label. Hydration duty vs actual hydration in contra is also blurred; clarify exceptionless rule. |
| Q2; 1/1 | whenever; sunlight hits panels → generate electricity | Sound basic translation/contra; use consistent time/event context. Good first forward item. |
| Q3; 1/1 | only those; rebate received → conserved water | Sound. Good only-at-front contrast. |
| Q4; 1/1 | the only; unlocking with a key → blue key used | Repair ambiguity: “only key” excludes other keys, not every other way of opening a door. Key asserts every unlocked door used blue key. Rewrite “door can be unlocked only with the blue key” or limit explicitly to key-based unlocking. |
| Q5; 2/1 | requires; chess success → strategic thinking | Sound intended requirement. Preserve time consistency. |
| Q6; 2/2 | any + must; artist uses oil paints → thorough brush cleaning required | Repair mixed indicator grading and duty/actual compliance in contra. Keep `artist` and `thoroughly`. |
| Q7; 2/2 | all + require; successful project → effective teamwork required | Forward/contra consistently retain `required`; mixed indicator classification needs repair. Good contrasting requirement-status with actual action. |
| Q8; 2/2 | only those; can apply → architecture degree | Repair modal loss in if/then (`applies`). Key contra retains cannot apply, exposing inconsistency. Use eligibility on both sides. |
| Q9; 3/2 | whenever; sun sets → lights turn on | Sound event rule; use as easy transfer, not additional conceptual coverage over Q2. |
| Q10; 3/2 | the only; wisdom → experience | Sound intended metaphorical requirement, but less concrete beginner example. Keep for later language transfer. |
| Q11; 3/2–3 | every + must + to be; legally binding agreement → in writing | Intended direction sound. Repair mixed label: `every` scopes agreements while must/to expresses binding requirement. Do not imply every agreement is written. |
| Q12; 3/3 | only if; goals achieved → committed | Sound. Good direct Group 2 translation. |
| Q13; 4/3 | anyone; studies physics → encounters complex math | Sound. Good expanded any/people variant. |
| Q14; 4/3 | when; artists inspired → celebrated pieces | Sound stipulated rule, empirically implausible if read as factual advice. Suitable fictional-rule framing or replace topic. |
| Q15; 4/3 | only when; plant thrives → adequate sunlight reaching its leaves | Sound full modifier preserved. Strong complete-condition example. |
| Q16; 4/3–4 | only those; submission reviewed → applicant identity confirmed by registrar | Sound, preserves reviewer/registrar qualifier. Strong complex noun-phrase extraction. |
| Q17; 5/4 | only where; license renewed → exists payment record matching license identifier | Direction sound. Key abbreviates to “matching payment record”; explicitly define matching to this license identifier. |
| Q18; 5/4 | only when; certification → form signed by evaluator whose authorization currently active | Repair. Keep `currently`; contra should say “No evaluator whose authorization is currently active signs the form,” not ambiguous “an evaluator ... does not sign.” One non-signing evaluator does not rule out another qualifying signer. |
| Q19; 5/4 | only if; request processed → portal-assigned file for requester present | Direction sound; key omits assigned-to-requester restriction. Restore it for complete-condition practice. |
| Q20; 5/4 | every + requires; failed-seal device → recalibration required | Forward/contra preserve requirement-status, but mixed label needs repair. Strong relative-clause example. |
| Q21; 6/4–5 | if; registrar verifies registration → admission granted | Sound. Keep person identity and registrar in same event. |
| Q22; 6/5 | the only; entry accepted → clerk records it in registry | Sound; registry restriction preserved. Best clear `the only` example; compare with only-front form after convention explained. |
| Q23; 6/5 | where; verification that training requirement met appears in file → access granted | Sound, carefully retains verification rather than merely training completed. Strong full-condition extraction. |
| Q24; 6/5 | whenever; threshold-meeting complaint filed with office → investigation begins | Sound. Key retains threshold and filing office via defined phrase. Strong scope item. |
| Q25; 7/5 | all + always; agency-issued permit → audit trail matching transaction record | Direction sound; mixed indicator label and undefined shortened `matching` need repair. |

## Indicator ledger Part 1: all 13 identification items

All keys on IK p1; IW references are Part 1/item. The rendered key has group numbers but does not circle or highlight the selected word despite the task asking students to do so. Add exact spans in the digital answer data.

| Item | Indicator and teaching target | Key audit |
|---|---|---|
| 1 | only if; promotion qualification requires completed training | Group 2 sound; only if at beginning requires reading whole sentence. |
| 2 | any; student missing lesson → receives notes | Group 1 sound; keep who-clause. |
| 3 | only when; can enter backyard → gate unlocked | Group 2 sound; retain permission/capability wording. |
| 4 | the only; quickly spoiling food → no preservatives | Group 2 conflicts with this package's `the only` Group 1 convention. Repair classification/selected span before import. |
| 5 | where; maintenance complete → servers restart | Group 1 sound; contrast with only where. |
| 6 | must ... to; avoiding fines requires seatbelts | Group 2 sound; don't isolate must from purpose phrase or turn general duties into guarantees of compliance. |
| 7 | if after result; alarm sounds → workers evacuate | Group 1 sound; good reversal-of-sentence-order rep. |
| 8 | requires; borrowing and collateral | Group 2 sound lexical recognition, but source phrase `to secure a loan` is awkward/ambiguous; rewrite before diagramming. |
| 9 | all; on-time application → reviewed | Group 1 sound; `submitted on time` essential. |
| 10 | when; show ID → can enter | Group 1 sound; keep `can`. |
| 11 | always; document errors before troubleshooting | Group 2 intended; imperative is an instruction, not evidence everyone follows it. Frame as a rule that must be obeyed or use declarative rule. |
| 12 | only where; accessible park → pathways lead there | Group 2 sound; explicit location reference needed in feedback. |
| 13 | every; author publishes → gains recognition | Group 1 sound; keep publishes qualifier. |

## Indicator ledger Part 2: all 10 diagram/role items

All IK p1. These repeat Part 1 stems and add S/N role work. Treat them as scaffolded stages on the same examples, not ten new transfer questions.

| Item (Part 1 source) | Expected arrow / task | Key audit |
|---|---|---|
| 1 (1) | qualify for promotion → complete training | Sound; inverted only-if phrasing. |
| 2 (2) | student misses lesson → student receives notes | Sound. |
| 3 (3) | houseguest can enter backyard → gate unlocked | Sound; correctly retains can. |
| 4 (6) | avoid fines → wear seatbelts | Sound intended necessary means; preserve driver context. |
| 5 (9) | application submitted on time → application reviewed | Sound and useful scope practice. |
| 6 (8) | borrowing → collateral required | Repair: key instead says collateral secures a loan, an unsupported result. Rewrite source for clarity and regenerate key. |
| 7 (7) | alarm sounds → workers evacuate | Sound; sufficient condition comes last. |
| 8 (10) | visitors show ID → visitors can enter | Sound; correct modal preservation. |
| 9 (13) | author publishes → author gains recognition | Sound. |
| 10 (11) | troubleshooting begins → errors documented beforehand | Repair: key omits before. Also imperative/factual-rule issue noted above. |

## Indicator ledger Part 3: all 20 original/contra/rephrase items

Each row audits original diagram, its slash-negated contrapositive, prose if/then, and prose contra. Leading slash means negation of the complete bracketed expression, not deleting a word. Teach this before these items.

| Item; IK page | Intended relation / skill | Key audit |
|---|---|---|
| 1; 1 | intern completes program → offered full-time position | Sound with domain restriction: abbreviated diagram drops interns; define domain as interns or preserve it. |
| 2; 2 | submit report by Friday → grade finalized | Sound; contra retains by Friday rather than denying all submission. Strong deadline example. |
| 3; 2 | final bell rings → students exit building | Sound. |
| 4; 2 | participant finishes marathon → receives medal | Sound. |
| 5; 2 | device left unattended → powers down automatically | Sound; keep automatically in negation. |
| 6; 2 | committee meets → minutes recorded | Sound; sufficient condition last. |
| 7; 2 | employees qualify for bonuses → exceed sales targets | Sound necessary condition with fronted goal. |
| 8; 2 | expenditures can occur → managers approved budgets first | Repair modal loss: original says can occur; all key versions say occur. Keep authorization/can across both forms. |
| 9; 2 | temporarily halting operations → system maintenance required | Conditional direction intended; key upgrades requires to performed. Clarify factual prerequisite assumption or preserve requirement-state. |
| 10; 2 | access granted → credentials verified | Sound. |
| 11; 2–3 | servers reboot → security protocols permit it | Sound; only where used non-locatively. |
| 12; 3 | entry → security checks conducted before entry | Repair lost before; also imperative requires compliance-rule framing. |
| 13; 3 | protocol fails to initiate within 1 minute → alarms do not deactivate on their own | Sound negative/negative rule; contra correctly positive/positive. Later-phase challenge; keep time and on their own. |
| 14; 3 | backups performed → detects low storage for 2 cycles | Sound. Negative must encompass full two-cycle condition. |
| 15; 3 | three reviewers call for revision → reports published | Diagram sound; prose contra “three reviewers did not call” risks scope ambiguity (three non-callers vs not three callers). Use “It is not the case that three reviewers called for revision.” Source outcome is intentionally counterintuitive; frame stipulated rule. |
| 16; 3 | allowed to board → documents verified by both authorities | Sound. Not both does not mean neither; useful later compound-scope bridge. |
| 17; 3 | any extreme-temperature exposure → sample integrity compromised | Sound. Contra correctly no exposure rather than some unaffected exposure. |
| 18; 3 | request can be processed → employee submits detailed online report | Repair modal loss: keys say processed, not can be processed. Preserve detailed and online. |
| 19; 4 | safety standards unmet → inspections immediately | Sound; contra retains not immediately, not no inspection. Useful negative-trigger example. |
| 20; 4 | server restart → critical software patches applied first | Sound; preserves ordering in contra. Contrast with Q12 to teach why before/first matters. |

## Integrate by skill instead of publishing whole packets

The strongest progression is already latent in IW: locate the indicator, identify the complete sufficient/necessary conditions, draw the forward arrow, then later express the contrapositive. Reuse its repeated examples deliberately for coached practice, but use different stems to assess transfer.

- **Sufficient/necessary lesson notes:** one plain example per indicator; use RW Q2 and Q12 as contrasting when/only-if directions. Retain definitions already approved. No need for a separate page repeating lists.
- **Group 1/2 flashcards:** expression on front, complete sentence and annotated condition on back. Draw from IK Part 1 once labels/spans fixed; do not simply upload group numbers as explanatory answers. `where` vs `only where`, `when` vs `only when`, and `only` vs `the only` deserve paired contrasts.
- **Must-arrow practice:** IK Part 2 Q1,3,7,8 test placing conditions from different sentence orders; show complete left/right clauses and ask which is sufficient/necessary. Keep permission words visible. Do not demand contraposition yet.
- **Find the complete condition:** RW Q15–19,23–25 and IK Part 3 Q2,13,14,16 are strong evidence this skill deserves instruction. Start with on-time applications (IK Part 2 Q5), then contrast a full condition with one missing only its qualifier. Do not begin with the densest administrative sentences.
- **Forward translation drill:** use a selected clean mixed set from RW Q2,3,5,9,12,13,15,16,21–24 plus IK Part 2. Ask for the complete condition, then arrow placement. Avoid treating many same-form examples as new skills.
- **Later contraposition drill:** unlock after negating complete conditions is taught. IK Part 3 Q13,14,16,19 and RW Q18 are genuinely harder than basic indicator recognition. Repair Q18 first. Assess negation scope separately before requiring all four written outputs at once.
- **Teacher answer notes:** retain exact source IDs, repaired-key rationale, and accepted alternate paraphrases. Record original and adapted text separately. Never silently overwrite the source key.

These are source-backed content options, not a recommendation to add all 68 tasks to the learner path. The set is strongest for sentence translation and qualified conditions. It provides little standalone evidence about rule-vs-fact, invalid reversal, or applying a fresh factual trigger; those should remain distinct objectives in the bootcamp rather than be inferred from successful rewriting.
