# Jev workflow audit report

Use this structure as a guide, not a form to fill with invented content. Keep the report proportional to the available evidence. Replace bracketed placeholders; omit sections that do not apply.

## Recommendation

[State the strongest useful conclusion: one pilot to try, a specific evidence gap to resolve, or no good Jev fit found. Explain why in two or three sentences.]

The discovery audit used the existing assistant. [State whether any Jev calls occurred; for the discovery phase, none should have occurred. Do not imply that normal assistant usage was free.]

## Evidence and coverage

Requested window: [start–end, timezone if relevant].

| Source and selected scope | Observed dates | Records examined | Distinct workflows or occurrences | Gaps |
| --- | --- | --- | --- | --- |
| [Accessible source/project] | [Actual coverage] | [Count and unit] | [Count or unknown] | [Missing dates, unsupported formats, unavailable outcomes] |

[Briefly explain summary/excerpt sampling, deduplication, and any uncertain grouping. Distinguish candidate history records from verified task completion. State unavailable cloud/device history instead of treating it as zero work.]

[If relevant: analysis used minimized excerpts with the current assistant provider; local history discovery does not mean all analysis stayed on-device. Do not reproduce secrets or sensitive content.]

## Opportunities

Include zero to three candidates. Do not manufacture a full list.

| Rank / disposition | Workflow and evidence | Specific Jev judgment | Enabled action and likely benefit | Simpler alternative / main uncertainty |
| --- | --- | --- | --- | --- |
| [1 / Pilot] | [Observed recurrence or batch size; local task/artifact reference] | [Inputs → defined output] | [Who does what next; work potentially reduced] | [Code or small-model alternative; unknowns] |

Use stable task identifiers or clickable local source references where available. Prefer short neutral descriptions over sensitive titles. If the report will be shared publicly, remove private local references and identifiable content from the shared copy.

For each recommendation, label its important claims **Observed**, **Estimated**, or **Unknown**. Public examples may support the design pattern; identify author-reported or mocked results explicitly. Do not use another project's benchmark as this user's forecast.

## One proposed pilot

**Workflow:** [Current input → work performed → useful outcome.]

**Evidence:** [One or two local references and what each actually establishes.]

**Judgment contract:**

- Input: [Minimum fields already available; note any extraction required.]
- Output: [Supported choice set, score, or yes/no fields with clear meanings.]
- Next action: [Specific application step or human decision.]
- Remaining work: [What code, a generative model, or a person still handles.]

**Why test Jev:** [The bottleneck or repeated work it might reduce, with the strongest ordinary-code/small-model counterargument.]

**Test design:** [Bounded sample size, representative/difficult/negative cases, labels or review method, identical baseline workload, and authorization/data boundaries. If necessary details are unknown, state what must be established first.]

| Measure | Existing baseline | Pilot target / method | Evidence status |
| --- | --- | --- | --- |
| Decision quality and consequential errors | [Measured or unknown] | [How judged; required outcome] | [Observed/estimated/unknown] |
| Completed-workflow duration | [Measured or unknown] | [Include preparation, fallback, and downstream work] | [Status] |
| Total API cost / subscription effect | [Comparable cost or unknown] | [Dated rates and assumptions, or measure during test] | [Status] |
| Setup and maintenance effort | [Known current process] | [Main integration work and ongoing dependency] | [Status] |

**Limits and fallback:** [Maximum items/calls/spend proposed for setup, stop conditions, review/fallback behavior, and what a wrong decision would cost. These proposed bounds are not authorization to run the test.]

**Decision after testing:** [Adopt, revise, or abandon criteria. No automatic rollout.]

## If no good fit was found

[Use this instead of a forced pilot. Explain the mismatch or missing evidence and one small useful next step. Examples: measure the frequency of a candidate workflow, label a small sample, or implement an exact rule in ordinary code.]

## Next step

[For an audit-only request, offer guided setup of the selected pilot using the setup guide. If setup is already requested and authorized, state the concrete next step and proceed within that authorization. Ask only for information or authorization that is actually missing.]
