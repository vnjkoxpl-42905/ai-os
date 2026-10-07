# Jev fit rubric

Apply this rubric to the user's workflow, not to an isolated model call. The result is a reasoned recommendation; do not convert incomplete evidence into a numerical fit score.

## 1. Establish the unit of work

Record the user's objective, input source, current process, work product, and available outcome evidence. Count distinct task occurrences or items processed, with the observed date range.

- Several retries or model calls for one task are one occurrence, not repeated demand.
- Resumed sessions, duplicate exports, and branches may describe the same task. Deduplicate using identifiers and context; disclose ambiguity.
- A single large batch can be useful even without recurrence, but its benefit must justify setup effort.
- An accepted change, a test result, a reviewed shortlist, and an assistant's completion claim provide different evidence. State which is available.
- Missing records and unknown outcomes stay unknown. Do not extrapolate the observed sample to a month without an explicit assumption.

## 2. Isolate a supported judgment

Write the candidate in this form:

> Given **these available fields**, choose/score **these defined outputs**, so **this application or person** can take **this specific next step**.

Strong candidates have repeatable criteria, bounded outputs, available relevant state, and a clear use for the answer. Examples include relevance filtering, routing among known handlers, prioritizing a review queue, and classifying items before a more expensive step. These are patterns to investigate, not claims about the user's work.

Weak candidates require new facts, free-form writing, code generation, extensive reasoning across missing context, or reliable interpretation of data the application cannot supply. Unsupported inputs need a separate extraction component, whose cost and errors count.

For exact conditions, parsing, arithmetic, allowlists, or fixed thresholds, prefer ordinary code unless there is a demonstrated semantic judgment that rules cannot reasonably handle. Use current official documentation to verify the proposed output type and limits.

## 3. Identify the benefit and alternatives

Compare at least:

| Alternative | Question |
| --- | --- |
| Current workflow | What time, model work, or human effort would change? |
| Ordinary code or rules | Can the decision be solved reliably without a model? |
| Suitable small generative model | Is it already fast and inexpensive enough, with adequate quality? |
| Jev plus surrounding workflow | Does preparing state, making the decision, handling errors, and finishing the task improve the outcome? |

A fast extra call can make the whole workflow slower. Filtering is useful only if it removes enough downstream work without losing valuable items. False positives can increase later costs; false negatives can remove the very items the workflow needs.

Consider frequency or batch size, latency sensitivity, setup and maintenance effort, consequences of mistakes, and the availability of an appropriate fallback. Do not call an integration valuable merely because it could be built.

## 4. Evaluate the evidence

Use three explicit labels:

- **Observed:** supported by an identified task record, artifact, measured run, or reviewed sample. State its scope.
- **Estimated:** computed from stated assumptions. Give the assumptions and avoid false precision.
- **Unknown:** unavailable, incomplete, unmeasured, or dependent on a future test.

A repository proves that code is published. It does not prove deployment, reliability, or the author's speed/cost claims. A mocked demo is not a live model evaluation. An API response or valid output shape is not evidence that a decision was correct. Confidence values require task-specific validation before operational thresholds are justified.

Choose one disposition:

- **Pilot:** a concrete supported judgment, useful action, and testable benefit are supported by enough evidence.
- **Gather evidence:** a plausible fit exists, but missing frequency, outcomes, labels, data access, or baseline measurements prevent a recommendation.
- **Skip:** simpler code suffices, outputs do not fit, errors are too consequential for the proposed controls, or likely benefit does not justify overhead.

Rank pilot candidates by expected practical value and evidence strength, explaining uncertainty. It is valid for all candidates to be “gather evidence” or “skip.”

## 5. Make honest cost and speed comparisons

Use the same input set, quality target, and completed work product for every comparison. Separate API latency from end-to-end duration. Include extraction, queuing, concurrency, retries, fallback, human review, and later model calls where relevant.

For an API workflow, a useful estimate is:

`net API savings = baseline total API cost - (Jev cost + remaining model cost + added fallback/retry cost)`

Use current rates for the selected provider, dated in the report. Input size includes serialized state, questions, and any other billed material under that provider's rules. Do not assume free output, token accounting, model IDs, or access conditions remain unchanged. Label forecasts as estimates until actual usage is measured.

When the baseline is an assistant subscription, report potential time, usage, or capacity effects separately. There may be no reduction in the subscription bill, and the pilot may add API spending. Do not convert subscription tokens to dollars using unrelated API prices.

## 6. Design one small pilot

Define the following before a live test:

1. **Data:** a bounded, representative sample and the minimum necessary fields. Use authorized data; do not forward complete session logs to Jev.
2. **Decision:** supported typed outputs, criteria, and the action each output would enable.
3. **Reference:** user-reviewed labels or another defensible outcome measure. Include ambiguous and negative cases; reserve unseen examples when feasible.
4. **Baseline:** current workflow and the strongest simple alternative, evaluated on the same work.
5. **Success:** task-level quality, meaningful error rates, end-to-end time, and actual or explicitly estimated total cost. Set thresholds from the user's needs, not a generic confidence cutoff.
6. **Bounds:** maximum items/calls/spend and a stop condition for repeated failures. Disclose any library retries that affect those limits.
7. **Action boundary:** start with a report or human-reviewed recommendation. Keep existing permissions and safeguards; a decision must not authorize its own execution.
8. **Next step:** adopt, revise, or abandon based on results. No automatic hooks, routing changes, or rollout are implied by a successful sample.

The audit itself proposes this test. It does not make paid calls or claim to have measured the result.
