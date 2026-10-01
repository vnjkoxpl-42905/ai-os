# Conditional applications need a separate evidence pass

Date: 2026-09-30.

## Browser inspection was blocked

The requested Codex in-app browser could not be inspected in this delegated pass. `cua.createBrowserTab('iab', ...)` timed out after roughly 32 seconds and reset the runtime. A subsequent `cua.getState()` also timed out and reset it. A later retry with a 60-second timeout completed in roughly 13 seconds but returned `apps: []` and `browsers: []`. No other browser was substituted. No lesson, answer, completion state, or study-plan setting was changed. Because tab creation had an unknown outcome and the recovered inventory contained no browsers, a temporary tab's existence and closure could not be verified.

This delegated browser session obtained no direct LR observations. **The parent session subsequently inspected the live LR schedule and written lesson pages.** That evidence supersedes the overall browser blocker for the resources below. No videos were watched or official questions solved. Drill interactions and feedback remain unverified.

## Live LR evidence obtained by the parent session

The schedule at `https://7sage.com/u/usr_031j8RfMOF3zm8TC7Hg2iW/study-plan/logical-reasoning` places the relevant sections in this order: MBT, PSA/rule application, Principle, SA, NA, and later Parallel and LR Logic Tags. These broad section labels do not establish that every resource is conditional-specific. Principle and Parallel were located in the schedule; their substantive teaching was not inspected in the evidence supplied here.

| Written resource inspected | What it teaches and how it develops earlier skills | Evidence limit |
|---|---|---|
| [MBT theory and approach](https://7sage.com/lessons/logical-reasoning/inference-and-must-be-true-questions/mbt-theory-and-approach?sidebar=study_plan) | Distinguishes guaranteed inference from weaker support, situating MBT and MSS on a support spectrum. Students interpret grammar carefully, use foundational notation where suitable, and either anticipate an inference or eliminate answers lacking adequate support. This transfers translation and linking into answer evaluation. | Written teaching observed; specific practice mechanics not inspected. |
| [PSAR theory and approach](https://7sage.com/lessons/logical-reasoning/pseudo-sufficient-assumption-or-rule-application-questions/psar-theory-and-approach?sidebar=study_plan) | Students select a rule connecting the supplied facts to the desired conclusion. They must verify every trigger element and the correct consequence rather than match a familiar phrase. General wording variants increase the abstraction required. | Written teaching observed. |
| [PSAA theory and approach](https://7sage.com/lessons/logical-reasoning/pseudo-sufficient-assumption-or-rule-application-questions/psaa-theory-and-approach?sidebar=study_plan) | Reverses the task: the rule is supplied and students identify its proper application or facts needed to activate it. Checking all trigger conditions trains rule application beyond recognizing an indicator. | Written teaching observed. |
| [SA theory and approach](https://7sage.com/lessons/logical-reasoning/sufficient-assumption-questions/theory-and-approach-sa?sidebar=study_plan) | An answer must guarantee the conclusion, rather than merely strengthen it. Students identify premises and conclusion, locate a gap between premises or at the final inference, and test a bridging rule. A broader rule can still be sufficient. | Written teaching observed. |
| [SA versus MBT](https://7sage.com/lessons/logical-reasoning/sufficient-assumption-questions/sufficient-assumption-questions-vs-must-be-true-questions?sidebar=study_plan) | Contrasts deriving A→C from A→B and B→C with supplying a missing A→B or B→C. The comparison makes inference direction and the missing-link task explicit. It points back to only-if, unless, no, and contraposition when foundations require repair. | Written comparison observed; foundation remediation referenced, not tested. |
| [NA theory, part 1](https://7sage.com/lessons/logical-reasoning/necessary-assumption-questions/theory-part-1-na?sidebar=study_plan) | The inspected written brief contrasts a necessary requirement with a powerful sufficient condition. It provides an important distinction after SA: what an argument needs can differ from what would guarantee its conclusion. | Brief text only; attached video not watched. |
| [Link assumption tag](https://7sage.com/lessons/logical-reasoning/lr-logic-tags/the-link-assumption-tag?sidebar=study_plan) | Tracks shifts between premises or from premises to conclusion and identifies the link needed to connect them. It applies across multiple reasoning frameworks, so link-assumption tagging should not be treated as exclusively conditional. | Written tag explanation observed. |

### Relative emphasis visible in the catalogue

The MBT section contains eight numbered lessons, eleven You Try entries, one drill, plus review/live-class resources. SA contains four numbered lessons and sixteen You Try entries, plus review, drill, live-class and stem-worksheet resources. These are **section catalogue counts**, not counts of conditional-only lessons or independent mastered skills. They suggest substantial question application alongside theory, but do not prove exercise difficulty, feedback quality or adaptive behavior.

The observed application flow develops three related tasks: derive a conclusion from rules and facts; choose/apply a rule that connects facts to a judgment; supply a rule that repairs an argument. NA then distinguishes requirements from guarantees. That is a useful sequencing insight for LSAT U, not evidence that every student should study all application types before the quantifier phase.

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

The parent observations resolve the written-theory portions listed above. The comparison remains incomplete for video-only nuance, actual drill interactions, question-level coverage, and the uninspected Principle/Parallel teaching. No paid transcript or proprietary drill-prompt archive was created.
