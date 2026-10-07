# Conditional linking: draft question bank

Date: 2026-09-16
Status: authored draft for review. Not installed in the application or published.
Design authority: [Conditional drill input design](2026-09-14-conditional-drill-input-design.md).

## One Conditional Reasoning entry, four worlds

Activity Center → Conditional Reasoning → choose a world. Preserve the existing activity entry and the current General Conditionals work. The new worlds are additions, not replacements.

**Latest interaction clarification:** present a couple of conditional premises and a target conclusion, then ask “What's the missing link?” Each of the five choices is one candidate connecting conditional. Do not offer five completed chains. Reveal the completed chain only in the explanation after commitment. Joshua rejected the completed-chain-choice suggestion; the existing missing-link questions already use the requested answer format. Whether Linking needs a separate tile from Missing Link remains a naming/navigation decision, not a reason to invent a different answer interaction.

| World | What the student practices | Existing work retained |
|---|---|---|
| General Conditionals | Diagram a statement, identify its direction, and recognize equivalent conditionals across all four groups. | The current Conditional Rephrase activity, its question bank, paper-first flow, and prior progress. |
| Linking | Combine two or more rules into a chain, including rules that first need contraposition. | Add a dedicated chain-building set. Do not move or remove the existing questions to populate it. |
| Missing Link | Choose the additional conditional that makes the target conclusion follow. | The ten ML draft items below. |
| Must Be True | Choose what follows from the supplied rules and facts, including AND/OR cases. | The ten MBT draft items below. |

Keep paper-first work, five multiple-choice answers, deterministic grading, and the current overall visual style. Linking focuses on connecting rules; Must Be True extends that work to facts and combined conditions. No argument-repair mode, required diagram builder, handwriting recognition, or long reading-comprehension exercise.

Each world retains its own unfinished run and history. Opening the world selector must not reset an existing run. Preserve the original activity ID and existing assignment links; they should still reach the existing work or offer an explicit Continue action. A new world must never overwrite General Conditionals progress. Each language-based progression covers all four groups.

The drafted Missing Link and Must Be True sets each begin with one worked example, then six symbolic items and four language items. The separate Linking bank remains to be authored; it must build on the same notation and progression. This gives two difficulty ramps: learn the operation with letters, then apply it to wording. Short paragraphs contain only the premises needed for conditional work. They are optional presentation of the same task, not a separate reading mode.

The first ten missing-link items are original sufficient-assumption-style exercises. The later PHOTO-ML section adds all 12 exercises from Joshua's supplied photographs. They are not official LSAT questions. Each asks which ONE supplied option makes the conclusion follow. Other sufficient assumptions can exist outside the choices; the key is not claimed to be the only possible bridge or a necessary assumption.

Notation follows Joshua's supplied LSAT examples: a diagonal slash through a letter means not, as in A̸. Keep the normal directional arrow →. Write **and** and **or** as words. Do not show formal logic operator glyphs or logical grouping parentheses/brackets in student-facing diagrams. A, B, C and the other letters name conditions. Answer labels are separate.

This Markdown draft uses a combining diagonal slash for negated letters. In the app, render a real diagonal stroke over the condition, matching the existing diagram style; provide an accessible spoken label such as “not A.” Do not substitute a horizontal strikethrough, a prefix slash, or a different negation glyph.

Examples: A → B; B̸ → A̸; A and B → C; A → B or C. Use spacing, stacked conditions, and branches to make compound scope clear. Do not flatten a more complex expression into an ambiguous line merely to remove punctuation. Internal grading may retain a structured logical representation without displaying it.

## Cover the four groups without changing their labels

The 2026-09-15 copy correction requires four groups and a separate “Required means right” takeaway. The live LSAT U page inspected in this conversation labels its groups as follows; preserve that interface pending any explicit taxonomy change:

- Group 1: “Left Sufficient triggers.”
- Group 2: “Right Necessary triggers.”
- Group 3: “If not,” covering unless, without, until and except.
- Group 4: “No A's are B,” explained as “All A's are not B.”

Joshua's attached LSAT Lab screenshots use a different organizing scheme: rules, universals, guarantees, and requirements. These are not asserted to be the same four labels as the LSAT U page. Cover all four screenshot categories as wording tags while retaining the app's existing map. Older corpus taxonomies also differ; this draft does not silently adjudicate them. Symbolic items assess logic and do not count as evidence of indicator-language mastery. The mixed word items cover all four app groups, but this starter bank does not exhaust every indicator or scenario.

Never infer arrow direction merely from the location of a word. For example, “A ensures B” means A → B; the result B follows “ensures.” Unless does not by itself mean exactly one, and no does not always mean negate the same visible noun phrase regardless of sentence structure.

## Supply the missing conditional

Common instruction: **Diagram the premises and conclusion on paper. Which additional conditional, if assumed, makes the conclusion follow?** Reveal choices after the paper step. Reveal keys and explanations only after commitment.

### ML1: Connect the open ends

Premises: A → B. C → D.

Conclusion: A → D.

| Choice | Conditional |
|---|---|
| A | C → B |
| B | D → C |
| C | B → C |
| D | B → A |
| E | D → A |

**Answer: C.** Starting with A gets you to B. The second premise starts at C and gets you to D. Add B → C and the chain becomes A → B → C → D.

Why the others fail: A joins C to B in the wrong direction. B reverses the second premise. D takes you back to A. E reverses the target rather than establishing it.

### ML2: Turn a rule before finding the gap

Premises: A → B. C̸ → B̸.

Conclusion: A → D.

| Choice | Conditional |
|---|---|
| A | D → C |
| B | C → A |
| C | C̸ → D |
| D | C → D |
| E | D → A |

**Answer: D.** Contrapose C̸ → B̸ to obtain B → C. Now A leads to B and then C. C → D finishes the chain.

Why the others fail: A runs from the destination back toward C. B loops back to A. C requires C̸, but the premises give C when A occurs. E begins at D, which is what you still need to reach.

### ML3: Match the sign as well as the letter

Premises: A → B̸. C → D.

Conclusion: A → D.

| Choice | Conditional |
|---|---|
| A | B → C |
| B | C → B̸ |
| C | C̸ → B̸ |
| D | D → C |
| E | B̸ → C |

**Answer: E.** A gives B̸, not B. The bridge must let you move from B̸ to C. Then C gives D.

Why the others fail: A requires B. B and C merely make B̸ a result; neither lets you start from B̸ and reach C. D reverses the second premise.

### ML4: Work backward from a negative conclusion

Premises: D → A. B → L.

Conclusion: L̸ → D̸.

| Choice | Conditional |
|---|---|
| A | A → B |
| B | B → A |
| C | A̸ → B |
| D | L → D |
| E | A → B̸ |

**Answer: A.** Adding A → B creates D → A → B → L. Contrapose the chain: L̸ → B̸ → A̸ → D̸. That is the conclusion.

Why the others fail: B points across the gap backward. C starts from A̸, although D supplies A. D reverses D → L. E sends A to B̸, which does not establish L or exclude D when L is absent.

### ML5: Supply the second required part

Premises: A → B. B and C → D.

Conclusion: A → D.

| Choice | Conditional |
|---|---|
| A | C → A |
| B | A → C |
| C | D → C |
| D | D → B and C |
| E | A̸ → C̸ |

**Answer: B.** A already gives B. The second rule needs B and C together. Adding A → C supplies C whenever A occurs, so the full trigger is satisfied and D follows.

Why the others fail: A does not give C from A. C and D begin with the result you need to prove. E says what happens without A; it says nothing that supplies C when A occurs.

### ML6: Cover both alternatives

Premises: A → B or C. B → D.

Conclusion: A → D.

| Choice | Conditional |
|---|---|
| A | D → C |
| B | C → A |
| C | C → D |
| D | A → B̸ |
| E | D → A |

**Answer: C.** A guarantees at least one of B and C. The B branch already reaches D. C → D makes the other branch reach D too. Either way, A guarantees D.

Why the others fail: A and E begin with D. B sends C back to A without ensuring D. D rules out B when A occurs, forcing C, but still gives no path from C to D.

### ML7: Put the bridge before the existing chain

Premises: If a visitor's badge is scanned, that visitor is admitted. A visitor is admitted only if that visitor's registration is current.

Conclusion: Every invited guest has current registration.

| Choice | Additional conditional |
|---|---|
| A | Every visitor whose badge is scanned is an invited guest. |
| B | Every visitor with current registration is an invited guest. |
| C | No invited guest has their badge scanned. |
| D | Every invited guest has their badge scanned. |
| E | Every admitted visitor is an invited guest. |

**Answer: D.** Let G = invited guest, B = badge scanned, E = admitted, R = registration current. The premises give B → E → R. Add G → B to obtain G → B → E → R.

Why the others fail: A, B and E make guest status a result, not a starting point that guarantees registration. C blocks the badge condition without ruling out guest status or establishing registration.

Coverage: Groups 1 and 2; rules, universals, requirements.

### ML8: Link through an incompatibility

Premises: No expired pass is valid. Entering the facility requires a valid pass.

Conclusion: Anyone holding only a canceled pass cannot enter the facility.

For this exercise, evaluate the person's sole pass. Let C = canceled, X = expired, V = valid, E = permitted to enter using that pass.

| Choice | Additional conditional |
|---|---|
| A | Every canceled pass is expired. |
| B | Every expired pass is canceled. |
| C | Every pass that is not canceled is expired. |
| D | Every canceled pass is valid. |
| E | Every valid pass permits entry. |

**Answer: A.** No expired pass is valid means X → V̸. Entry requires validity: E → V, so V̸ → E̸. Add C → X and canceled leads to expired, invalid, and therefore no entry using that pass.

Why the others fail: B reverses the needed connection. C addresses passes that are not canceled. D establishes validity rather than excluding entry. E gives another route into the facility, not a reason canceled passes cannot be used.

Coverage: Groups 1, 2 and 4; universals and requirements. The sole-pass condition prevents an unstated second pass from changing the result.

### ML9: Read “cannot unless” before contraposing

Premises: A shipment cannot leave unless it has been inspected. Inspection guarantees that the shipment is sealed.

Conclusion: No flagged shipment can leave.

| Choice | Additional conditional |
|---|---|
| A | Every unsealed shipment is flagged. |
| B | Every flagged shipment is unsealed. |
| C | Every flagged shipment is sealed. |
| D | Every uninspected shipment is flagged. |
| E | Every sealed shipment can leave. |

**Answer: B.** Let L = can leave, I = inspected, S = sealed, F = flagged. The premises give L → I → S. Therefore S̸ → I̸ → L̸. Adding F → S̸ establishes F → L̸.

Why the others fail: A reverses the bridge. C supplies a necessary condition for departure without ruling departure out. D makes flagged status a result, not a trigger for being uninspected. E supplies permission to leave rather than preventing it.

Coverage: Groups 1, 3 and 4; guarantees and requirements. All statuses refer to the same decision time.

### ML10: Combine alternatives, “no,” and “unless”

Premises: Every finalist submits a sample or completes an interview. No applicant who completes an interview lacks approval. Applicants receive approval unless a review is pending.

Conclusion: Every finalist receives approval.

| Choice | Additional conditional |
|---|---|
| A | Every applicant without a pending review submits a sample. |
| B | Every applicant with a pending review submits a sample. |
| C | Every applicant who submits a sample has a pending review. |
| D | Every approved applicant submits a sample. |
| E | No applicant who submits a sample has a pending review. |

**Answer: E.** Let F = finalist, S = sample, J = interview, A = approval, P = pending review. The rules are F → S or J, J → A, and P̸ → A. The interview branch already reaches approval. E supplies S → P̸, so the sample branch also reaches approval. Both alternatives now support F → A.

Why the others fail: A points from no pending review to sample, not from sample to no pending review. B and C connect samples with a pending review, which does not establish approval. D reverses a possible connection from samples to approval.

Coverage: Groups 1, 3 and 4; universals, OR branches and negation. “Unless” does not say that a pending review necessarily prevents approval.

## Must Be True

Common instruction: **Diagram the premises on paper. Which statement must be true if all the premises are true?** A conditional answer states a rule; it does not assert that its trigger actually occurs.

### MBT1: Chain three conditions

Premises: A → B. B → C.

| Choice | Statement |
|---|---|
| A | C → A |
| B | A̸ → C̸ |
| C | A → C |
| D | B → A |
| E | C → B |

**Answer: C.** A gives B, and B gives C. So A → C. A, D and E reverse valid arrows. B incorrectly treats the absence of A as ruling out C.

### MBT2: Find a connection hidden by contraposition

Premises: A → B. C̸ → B̸.

| Choice | Statement |
|---|---|
| A | C → A |
| B | B → A |
| C | A → C̸ |
| D | A → C |
| E | A̸ → C̸ |

**Answer: D.** The second premise contraposes to B → C. Join it to A → B. A and B reverse what is established. C negates the result. E infers from the absence of the starting condition.

### MBT3: Use a negative fact

Premises: A → B. B → C. C is false.

| Choice | Statement |
|---|---|
| A | A is true. |
| B | B is true. |
| C | C is true. |
| D | At least one of A and B is true. |
| E | A is false. |

**Answer: E.** C̸ gives B̸, and B̸ gives A̸. Here a fact activates the contrapositive chain. Every other option conflicts with the resulting facts.

### MBT4: One part of an AND trigger is already established

Premises: A and B → C. C → D. A is true.

| Choice | Statement |
|---|---|
| A | B → D |
| B | A → D |
| C | D → B |
| D | B̸ → D̸ |
| E | D → C |

**Answer: A.** A is already established. If B also occurs, both parts of the trigger hold, producing C and then D. B incorrectly treats A alone as enough. C and E reverse arrows. D rules out D merely because this particular trigger is incomplete.

### MBT5: Eliminate one OR alternative

Premises: A → B or C. A is true. C is false.

| Choice | Statement |
|---|---|
| A | B is false. |
| B | B is true. |
| C | C is true. |
| D | Both B and C are true. |
| E | A is false. |

**Answer: B.** A guarantees at least one of B and C. C is ruled out, so B must hold. A rejects the remaining alternative. C and D conflict with C̸. E contradicts the stated fact A.

### MBT6: Different branches, same result

Premises: A → B or C. B → D. C → D.

| Choice | Statement |
|---|---|
| A | D → A |
| B | A → B |
| C | A → D |
| D | A → C |
| E | A̸ → D̸ |

**Answer: C.** Either available branch reaches D. You do not need to know which branch occurs. A reverses the resulting rule. B and D select one alternative without support. E rules out D when A is absent, even though D could occur another way.

### MBT7: Combine “every” and “only”

Premises: Every editor reviews submissions. Only certified staff review submissions.

| Choice | Statement |
|---|---|
| A | Every certified staff member is an editor. |
| B | No person who is not an editor is certified. |
| C | Everyone who reviews submissions is an editor. |
| D | Every editor is certified. |
| E | Every certified staff member reviews submissions. |

**Answer: D.** Editor → reviewer. “Only certified staff” makes certification necessary for reviewing: reviewer → certified. Therefore editor → certified. A, C and E reverse established connections. B infers not certified from not editor.

Coverage: Groups 1 and 2; universals and requirements.

### MBT8: Chain through a “no” rule

Premises: No damaged package is accepted. Every insured package is accepted.

| Choice | Statement |
|---|---|
| A | No insured package is damaged. |
| B | Every undamaged package is insured. |
| C | Every uninsured package is damaged. |
| D | Every accepted package is insured. |
| E | Every damaged package is insured. |

**Answer: A.** Damaged → not accepted. Contrapose: accepted → not damaged. Insured → accepted → not damaged. B and D reverse valid relationships. C treats not insured as enough to establish damage. E connects damage to insurance without support.

Coverage: Groups 1 and 4; universals and contraposition. Universal rules do not establish that any packages actually exist.

### MBT9: Chain “unless” with “only if”

Premises: The machine operates unless the safety switch is off. The machine operates only if cooling is active.

| Choice | Statement |
|---|---|
| A | If the safety switch is off, the machine does not operate. |
| B | If cooling is not active, the safety switch is off. |
| C | If cooling is active, the machine operates. |
| D | If the machine does not operate, the safety switch is not off. |
| E | If cooling is not active, the safety switch is not off. |

**Answer: B.** Let S = switch off, O = operates, C = cooling active. The premises give S̸ → O → C. Contrapose the chain: C̸ → O̸ → S. A adds an unwarranted converse to the unless rule. C reverses the cooling requirement. D and E negate the switch condition incorrectly.

Coverage: Groups 2 and 3; requirements. Treat these as stipulated rules about the same operating state, not a claim about real machinery.

### MBT10: A short mixed-premise paragraph

Every research grant requires approval. Approval is withheld unless the review is complete. No incomplete application receives a completed review. A completed review guarantees either a standard award or an exception. This application receives a research grant but does not receive a standard award.

Which statement must be true about this application?

| Choice | Statement |
|---|---|
| A | It receives an exception, and it is incomplete. |
| B | It receives no exception, and it is complete. |
| C | It receives a standard award, and it is complete. |
| D | Its review is not complete, and it receives an exception. |
| E | It receives an exception, and it is complete. |

**Answer: E.** Let G = grant, A = approval, R = completed review, K = complete application, S = standard award, E = exception. Diagram G → A → R. The no rule is K̸ → R̸, so R → K. The guarantee is R → S or E. The grant establishes R and K. Since S is false, E must hold. Both parts of choice E follow.

Why the others fail: A contradicts the application's completeness. B denies the required remaining award alternative. C contradicts the stated absence of a standard award. D contradicts the completed review established by the grant.

Coverage: all four map groups across universal wording, requirements, unless and no; guarantees; contraposition; OR elimination. Application completeness and review completeness are deliberately distinct conditions.

## Small changes to the drill screen

1. Keep the existing visual identity and paper-first step. Put the premises in a compact numbered stack. In missing-link mode, separate the target conclusion with a short divider. In Must Be True mode, show only the question until choices are revealed.
2. Enter through the four-world selector, then use the selected world name as the small in-drill label: General Conditionals, Linking, Missing Link, or Must Be True. Show progress within a short set, such as 3 of 10. Keep the front page largely intact.
3. Show exactly five authored choices with exactly one correct option for these new modes. Shuffle their order once per item within each saved run, and retain that order on resume and review. Do not generate choices by mechanically reversing one stored conditional. In missing-link mode, a choice equivalent to the correct bridge is also sufficient and cannot be a distractor.
4. After commitment, show one primary explanation: original premises, any needed contrapositives, then the finished chain. Highlight the inserted rule in missing-link mode. For and/or, show stacked conditions or a branch with the written connector. Do not introduce grouping brackets.
5. Put “Why my choice fails” beside the explanation, using the chosen distractor's specific error. Keep extra explanation expandable so the screen does not show several competing answer panels.
6. Keep original attempt, retry and revealed answer distinct in saved history. Save each student run, including repeated and unfinished runs. Resume the exact item and reveal state. Teacher preview stays separate from student records.
7. Add wording-coverage and operation tags internally. A student can understand letters while still misreading only, unless or no. Do not collapse those into one mastery score.

## Logical validation performed

All 20 final formalizations were checked by exhaustive Boolean valuation. For each Must Be True item, exactly one of its five options holds in every model of the premises. For each missing-link item, the existing premises do not already establish the conclusion, exactly one option makes it follow, and the augmented premises are consistent. The intended starting condition is satisfiable for the selected bridges, so the answer is not based on making the conclusion vacuously true.

The check caught equivalent and indirectly sufficient draft distractors; those were replaced before this draft was finalized. Natural-language scope was reviewed against the formalization. This is logical content validation, not browser testing or evidence that the application has been updated.

The next content expansion should vary the existing structures across every indicator family and include dedicated no/not-both and AND/OR contraposition items. These 20 questions establish the two requested modes; they are not a complete mastery curriculum.


## All exercises from Joshua's six supplied photos

Added 2026-09-16. These 12 photographed prompts are required content for **Missing Link**. The earlier ten original missing-link items and ten Must Be True items remain intact. Total draft inventory is now 32 entries: 22 Missing Link and 10 Must Be True. This count includes deliberate equivalent structures; it is not a count of 32 independent skills.

Source: user-supplied photos of the section *Missing Links in Conditional Chains as Sufficient Assumptions*. The book's title and author are not established by the images. Photos 1–3 establish the first four prompts and their solutions; photos 3–6 establish the remaining eight. Repeated worked solutions are not counted as additional exercises. Several faint negation strokes were checked against the solution pages.

The premise/conclusion pairs below transcribe the photographs. Five-choice adaptations and explanations are newly authored. The photos use an open blank for the sufficient assumption; the app retains Joshua's requested multiple-choice interaction. All 12 must be available; the earlier proposal of ten questions per sitting is not a limit on this required content, and session length remains an open design choice.

### Read the target, orient the premises, then connect the gap

Show each premise on its own line, followed by the target conclusion and “Which additional conditional makes the conclusion follow?” The student diagrams on paper before revealing five choices. A correct option may present the bridge in its contrapositive form. Never show a bridge and its equivalent contrapositive as two separate choices in a single-answer question.

After commitment, show the needed bridge, its equivalent contrapositive, and the completed chain. Those are two forms of one answer, not competing answers. Do not expose either before submission.

### PHOTO-ML01: One premise

Premise 1: A → B

Conclusion: A → C

| Choice | Additional conditional |
|---|---|
| A | C → B |
| B | B → C |
| C | B → C̸ |
| D | B̸ → C |
| E | A → B |

**Answer: B.** A reaches B. Add B → C to reach the target C. The completed chain is A → B → C.

Equivalent answer forms: **B → C** and **C̸ → B̸**. Only one form appears among the five choices.

Why the other choices fail:

- Choice A: A is true; B is true; C is false. The premises and this option are true, but the target conclusion is false.
- Choice C: A is true; B is true; C is false. The premises and this option are true, but the target conclusion is false.
- Choice D: A is true; B is true; C is false. The premises and this option are true, but the target conclusion is false.
- Choice E: A is true; B is true; C is false. The premises and this option are true, but the target conclusion is false.

### PHOTO-ML02: One premise

Premise 1: A → B

Conclusion: C → B

| Choice | Additional conditional |
|---|---|
| A | A → C |
| B | C → A̸ |
| C | C̸ → A |
| D | C → B̸ |
| E | A̸ → C̸ |

**Answer: E.** The target starts at C, but the existing rule starts at A. Add C → A. The completed chain is C → A → B.

Equivalent answer forms: **C → A** and **A̸ → C̸**. The correct choice uses the contrapositive form. Only one form appears among the five choices.

Why the other choices fail:

- Choice A: A is false; B is false; C is true. The premises and this option are true, but the target conclusion is false.
- Choice B: A is false; B is false; C is true. The premises and this option are true, but the target conclusion is false.
- Choice C: A is false; B is false; C is true. The premises and this option are true, but the target conclusion is false.
- Choice D: A is false; B is false; C is true. The premises and this option are true, but the target conclusion is false.

### PHOTO-ML03: One premise

Premise 1: A → B

Conclusion: C → A̸

| Choice | Additional conditional |
|---|---|
| A | C → B̸ |
| B | B̸ → C |
| C | C → B |
| D | C̸ → B̸ |
| E | B → A |

**Answer: A.** The target ends at A̸. Contrapose the premise to get B̸ → A̸. Add C → B̸, producing C → B̸ → A̸.

Equivalent answer forms: **C → B̸** and **B → C̸**. Only one form appears among the five choices.

Why the other choices fail:

- Choice B: A is true; B is true; C is true. The premises and this option are true, but the target conclusion is false.
- Choice C: A is true; B is true; C is true. The premises and this option are true, but the target conclusion is false.
- Choice D: A is true; B is true; C is true. The premises and this option are true, but the target conclusion is false.
- Choice E: A is true; B is true; C is true. The premises and this option are true, but the target conclusion is false.

### PHOTO-ML04: One premise

Premise 1: A → B

Conclusion: B̸ → C

| Choice | Additional conditional |
|---|---|
| A | C → A̸ |
| B | A̸ → C̸ |
| C | C̸ → A |
| D | A → C |
| E | A → B̸ |

**Answer: C.** The target starts at B̸. Contrapose the premise: B̸ → A̸. Add A̸ → C to obtain B̸ → A̸ → C.

Equivalent answer forms: **A̸ → C** and **C̸ → A**. The correct choice uses the contrapositive form. Only one form appears among the five choices.

Why the other choices fail:

- Choice A: A is false; B is false; C is false. The premises and this option are true, but the target conclusion is false.
- Choice B: A is false; B is false; C is false. The premises and this option are true, but the target conclusion is false.
- Choice D: A is false; B is false; C is false. The premises and this option are true, but the target conclusion is false.
- Choice E: A is false; B is false; C is false. The premises and this option are true, but the target conclusion is false.

### PHOTO-ML05: Two premises

Premise 1: A → B

Premise 2: C → D

Conclusion: A → D

| Choice | Additional conditional |
|---|---|
| A | C → B |
| B | B → C̸ |
| C | B̸ → C |
| D | B → C |
| E | C → A̸ |

**Answer: D.** Starting at A reaches B. Reaching C would then lead to D. Add B → C to complete A → B → C → D.

Equivalent answer forms: **B → C** and **C̸ → B̸**. Only one form appears among the five choices.

Why the other choices fail:

- Choice A: A is true; B is true; C is false; D is false. The premises and this option are true, but the target conclusion is false.
- Choice B: A is true; B is true; C is false; D is false. The premises and this option are true, but the target conclusion is false.
- Choice C: A is true; B is true; C is false; D is false. The premises and this option are true, but the target conclusion is false.
- Choice E: A is true; B is true; C is false; D is false. The premises and this option are true, but the target conclusion is false.

### PHOTO-ML06: Two premises

Premise 1: A → B

Premise 2: C → D

Conclusion: C → B

| Choice | Additional conditional |
|---|---|
| A | A̸ → D̸ |
| B | A → D |
| C | D → A̸ |
| D | D̸ → A |
| E | D → C |

**Answer: A.** Begin with the rule containing the target start: C → D. The other rule ends at the target B: A → B. Add D → A. The completed chain is C → D → A → B.

Equivalent answer forms: **D → A** and **A̸ → D̸**. The correct choice uses the contrapositive form. Only one form appears among the five choices.

Why the other choices fail:

- Choice B: A is false; B is false; C is true; D is true. The premises and this option are true, but the target conclusion is false.
- Choice C: A is false; B is false; C is true; D is true. The premises and this option are true, but the target conclusion is false.
- Choice D: A is false; B is false; C is true; D is true. The premises and this option are true, but the target conclusion is false.
- Choice E: A is false; B is false; C is true; D is true. The premises and this option are true, but the target conclusion is false.

### PHOTO-ML07: Two premises

Premise 1: A → B

Premise 2: C → D

Conclusion: D̸ → A̸

| Choice | Additional conditional |
|---|---|
| A | B̸ → C̸ |
| B | C̸ → B |
| C | C → B̸ |
| D | C̸ → B̸ |
| E | B̸ → D |

**Answer: D.** Contrapose both premises: D̸ → C̸ and B̸ → A̸. Add C̸ → B̸ to complete D̸ → C̸ → B̸ → A̸. Alternatively, contrapose the target to A → D and find B → C. These are equivalent bridges.

Equivalent answer forms: **C̸ → B̸** and **B → C**. Only one form appears among the five choices.

Why the other choices fail:

- Choice A: A is true; B is true; C is false; D is false. The premises and this option are true, but the target conclusion is false.
- Choice B: A is true; B is true; C is false; D is false. The premises and this option are true, but the target conclusion is false.
- Choice C: A is true; B is true; C is false; D is false. The premises and this option are true, but the target conclusion is false.
- Choice E: A is true; B is true; C is false; D is false. The premises and this option are true, but the target conclusion is false.

### PHOTO-ML08: Two premises

Premise 1: A → B

Premise 2: C → D

Conclusion: B̸ → C̸

| Choice | Additional conditional |
|---|---|
| A | A → D |
| B | D → A |
| C | D → A̸ |
| D | D̸ → A |
| E | A → B |

**Answer: B.** Contrapose both premises: B̸ → A̸ and D̸ → C̸. The gap is A̸ → D̸, giving B̸ → A̸ → D̸ → C̸. Its equivalent form is D → A.

Equivalent answer forms: **D → A** and **A̸ → D̸**. Only one form appears among the five choices.

Why the other choices fail:

- Choice A: A is false; B is false; C is true; D is true. The premises and this option are true, but the target conclusion is false.
- Choice C: A is false; B is false; C is true; D is true. The premises and this option are true, but the target conclusion is false.
- Choice D: A is false; B is false; C is true; D is true. The premises and this option are true, but the target conclusion is false.
- Choice E: A is false; B is false; C is true; D is true. The premises and this option are true, but the target conclusion is false.

### PHOTO-ML09: Two premises

Premise 1: A → B

Premise 2: C → D

Conclusion: C → A̸

| Choice | Additional conditional |
|---|---|
| A | B̸ → D |
| B | D → B |
| C | D̸ → B̸ |
| D | C̸ → B̸ |
| E | B → D̸ |

**Answer: E.** Use C → D, then contrapose A → B to obtain B̸ → A̸. Add D → B̸ to complete C → D → B̸ → A̸.

Equivalent answer forms: **D → B̸** and **B → D̸**. The correct choice uses the contrapositive form. Only one form appears among the five choices.

Why the other choices fail:

- Choice A: A is true; B is true; C is true; D is true. The premises and this option are true, but the target conclusion is false.
- Choice B: A is true; B is true; C is true; D is true. The premises and this option are true, but the target conclusion is false.
- Choice C: A is true; B is true; C is true; D is true. The premises and this option are true, but the target conclusion is false.
- Choice D: A is true; B is true; C is true; D is true. The premises and this option are true, but the target conclusion is false.

### PHOTO-ML10: Two premises

Premise 1: A → B

Premise 2: C → D

Conclusion: A → C̸

| Choice | Additional conditional |
|---|---|
| A | D̸ → B |
| B | B → D |
| C | B → D̸ |
| D | B̸ → D̸ |
| E | B̸ → A̸ |

**Answer: C.** Use A → B, then contrapose C → D to obtain D̸ → C̸. Add B → D̸ to complete A → B → D̸ → C̸.

Equivalent answer forms: **B → D̸** and **D → B̸**. Only one form appears among the five choices.

Why the other choices fail:

- Choice A: A is true; B is true; C is true; D is true. The premises and this option are true, but the target conclusion is false.
- Choice B: A is true; B is true; C is true; D is true. The premises and this option are true, but the target conclusion is false.
- Choice D: A is true; B is true; C is true; D is true. The premises and this option are true, but the target conclusion is false.
- Choice E: A is true; B is true; C is true; D is true. The premises and this option are true, but the target conclusion is false.

### PHOTO-ML11: Two premises

Premise 1: A → B

Premise 2: C → D

Conclusion: D̸ → B

| Choice | Additional conditional |
|---|---|
| A | A̸ → C |
| B | A → C̸ |
| C | C̸ → A̸ |
| D | C → A |
| E | B̸ → A̸ |

**Answer: A.** Contrapose C → D to obtain D̸ → C̸. Keep A → B as written. Add C̸ → A to complete D̸ → C̸ → A → B.

Equivalent answer forms: **C̸ → A** and **A̸ → C**. The correct choice uses the contrapositive form. Only one form appears among the five choices.

Why the other choices fail:

- Choice B: A is false; B is false; C is false; D is false. The premises and this option are true, but the target conclusion is false.
- Choice C: A is false; B is false; C is false; D is false. The premises and this option are true, but the target conclusion is false.
- Choice D: A is false; B is false; C is false; D is false. The premises and this option are true, but the target conclusion is false.
- Choice E: A is false; B is false; C is false; D is false. The premises and this option are true, but the target conclusion is false.

### PHOTO-ML12: Two premises

Premise 1: A → B

Premise 2: C → D

Conclusion: B̸ → D

| Choice | Additional conditional |
|---|---|
| A | C → A̸ |
| B | A̸ → C̸ |
| C | A → C |
| D | B̸ → C̸ |
| E | A̸ → C |

**Answer: E.** Contrapose A → B to obtain B̸ → A̸. Keep C → D as written. Add A̸ → C to complete B̸ → A̸ → C → D.

Equivalent answer forms: **A̸ → C** and **C̸ → A**. Only one form appears among the five choices.

Why the other choices fail:

- Choice A: A is false; B is false; C is false; D is false. The premises and this option are true, but the target conclusion is false.
- Choice B: A is false; B is false; C is false; D is false. The premises and this option are true, but the target conclusion is false.
- Choice C: A is false; B is false; C is false; D is false. The premises and this option are true, but the target conclusion is false.
- Choice D: A is false; B is false; C is false; D is false. The premises and this option are true, but the target conclusion is false.


### Preserve the intentional repetitions

PHOTO-ML05 and PHOTO-ML07 have contraposed conclusions and equivalent bridges. So do PHOTO-ML06/PHOTO-ML08 and PHOTO-ML09/PHOTO-ML10. Keep every prompt, as Joshua requested. Use these pairs to practice recognizing equivalent forms, but do not treat success immediately after the paired explanation as fresh mastery evidence.

### Validation of the photo-derived additions

All 12 premises/conclusions were independently checked against the six photographs and their answer pages. Exhaustive Boolean checks confirm that the original premises alone do not establish the target, each credited bridge is consistent and nonvacuous, its contrapositive is equivalent, and exactly one of the five supplied options establishes the target. Every incorrect option has an explicit counterexample above. Equivalent answer choices were excluded, and correct positions vary.

This extends the saved draft only. It does not change the deployed activity, replace the existing General Conditionals questions, or settle the remaining interview choices about pacing and progression.
