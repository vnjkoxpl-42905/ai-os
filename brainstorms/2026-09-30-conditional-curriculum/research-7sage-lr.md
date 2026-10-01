# Conditional applications need a separate evidence pass

Date: 2026-09-30.

## Browser inspection was blocked

The requested Codex in-app browser could not be inspected in this delegated pass. `cua.createBrowserTab('iab', ...)` timed out after roughly 32 seconds and reset the runtime. A subsequent `cua.getState()` also timed out and reset it. A later retry with a 60-second timeout completed in roughly 13 seconds but returned `apps: []` and `browsers: []`. No other browser was substituted. No lesson, answer, completion state, or study-plan setting was changed. Because tab creation had an unknown outcome and the recovered inventory contained no browsers, a temporary tab's existence and closure could not be verified.

**No 7Sage Logical Reasoning lesson or drill was directly observed in this pass.** The screenshots supplied by Joshua show Foundations, not the Logical Reasoning application sequence. This file must not be used as evidence of 7Sage's LR teaching order, emphasis, exercise formats, feedback, or difficulty progression. No videos were watched.

## Existing LSAT U materials support this original application map

Source: `material-inventory.md` in this directory. This is a proposed LSAT U structure based on the earlier local inventory, not a reconstruction of 7Sage.

| Application | What students must learn | Proposed training | Prerequisites | Existing local support |
|---|---|---|---|---|
| Must Be True | Establish exactly what follows from the supplied rules and facts; separate proof from possibility | Translate, trigger rules, chain, prove one answer, explain why tempting alternatives lack support | Translation, contraposition, linking, compound conditions | Complete filed MBT/MSS lecture package; ten authored MBT questions; targeted guided drills |
| Most Strongly Supported | Distinguish certainty from strongest support; recognize when formal rules prove a conclusion and when other evidence supplies only support | Contrast guaranteed conclusions with plausible extensions; identify strength of evidence | MBT foundations and conclusion strength | MBT/MSS lecture package; question-level coverage still needs review |
| Sufficient Assumption | Supply a rule that makes the conclusion follow; identify the exact missing connection | Isolate premises and conclusion, mark recurring terms, find the gap, insert candidate rule and rerun proof | Linking, contraposition, direction, irrelevance | Ten-chapter SA bootcamp, twelve written exercises, twenty-two Missing Link questions |
| Necessary Assumption | Identify what the argument requires without confusing it with a rule that guarantees the conclusion | Negate candidates, test whether reasoning survives, contrast required bridge with overstrong sufficient bridge | Negation, conditional direction, argument analysis | Legacy method notes; a complete current conditional-NA teaching/practice sequence is unverified |
| Flaw | Diagnose reversal, inverse reasoning, and unjustified links; connect the mistake to the argument's conclusion | Identify attempted inference, supply a counterexample, then match an abstract description | Valid/invalid moves, triggering and no-link contrasts | Legacy fallacy material and conditional-question pools; dedicated coverage unverified |
| Parallel reasoning / parallel flaw | Match logical relationships rather than subject matter or vocabulary | Abstract structure, preserve negation and condition direction, compare validity and conclusion form | All preceding foundational operations | Indexed pools and legacy notes; individual explanation quality unverified |
| Principle applications | Apply or select a general rule that connects case facts to a judgment | Match every requirement of the rule to facts; check exceptions, scope and rule strength | Triggering, sufficient/necessary distinction, compounds | Inventory identifies real-question application pool; full teaching sequence unverified |

## Original examples illustrate distinct tasks

Use these newly written examples for planning, not as evidence of either provider's lessons.

- **MBT:** Every certified guide completed safety training. Mina is a certified guide. Therefore Mina completed safety training. Training does not prove Mina is certified.
- **SA:** Every approved proposal has a budget. This proposal has a budget, so it receives funding. A sufficient bridge is: every proposal with a budget receives funding. Having the required budget does not establish approval.
- **NA:** The argument says a team's certificate proves it can enter a tournament. A necessary assumption is that this certificate does not fail to satisfy an entry requirement. The actual answer must be tested against the complete argument, not a memorized word pattern.
- **Flaw:** Every funded team submitted a form. This team submitted a form, so it is funded. The rule permits unfunded teams to submit forms too.
- **Principle:** A request with both supervisor approval and a complete receipt must be reimbursed. A receipt alone does not trigger that rule.

## Design implications already established by Joshua

Keep three levels: Beginner, Medium, Advanced. Difficulty and scope are independent: general mixed application practice or a specific skill can be assigned at any level. Optional timing applies to Medium and Advanced. The complete self-study pathway also contains individually assignable pieces. Quantifier reasoning follows conditionals as the next phase and remains directly assignable.

An application label is not enough to establish difficulty. Beginner work can make premises, conclusion and indicator explicit. Medium work can vary language and require one hidden contraposition or link. Advanced work can combine compound conditions, multiple chains, distracting premises and close answer choices. These are authoring proposals requiring Joshua's review, not existing verified level definitions.

## Evidence still needed from 7Sage LR

1. Exact order and location of conditional applications in MBT/MSS, SA, NA, flaw, parallel and principle sections.
2. Which resources explicitly teach conditional reasoning versus merely contain a conditional question.
3. For each inspected lesson: learning objective, prerequisite, one concise summary, URL and whether text or video was actually reviewed.
4. For each inspected drill: student action, response format, hint/reveal behavior, explanation, practice volume, variation and transfer. Do not infer these from a title or scheduled minutes.
5. Separate substantive training time from estimates and repetition counts; do not infer automatic adaptation from the label "adaptive drill".
6. Identify where foundational skills are retaught, assumed, or contrasted with other reasoning. This is necessary before comparing overlap and proposing an original LSAT U course.

The comparison remains incomplete until those observations are possible. No paid transcript or proprietary drill-prompt archive was created.
