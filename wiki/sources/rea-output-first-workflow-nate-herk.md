---
type: source
subject: "Nate Herk: investigate a narrow feature and test the rebuilt behavior"
created: 2026-10-24
updated: 2026-10-24
aliases: ["I Tested the Viral Reverse Engineer Anything Skill. What You Need to Know"]
tags: [design, ai-workspace, source]
evidence: ../../raw/sources/clips/rea-output-first-workflow-nate-herk/source.md
sha256: 8111be36b9ef717216deffcf0ea217e19570ea0f7454bad483ffcb35601564fc
sources:
  - ../../raw/sources/clips/rea-output-first-workflow-nate-herk/PROVENANCE.md
contradictions: []
---

# Nate Herk: investigate a narrow feature and test the rebuilt behavior

**Source:** I Tested the Viral Reverse Engineer Anything Skill. What You Need to Know. Author: Nate Herk. [Original video](https://www.youtube.com/watch?v=rL5tw6h78zo). Publication and capture dates unknown. Ingested 2026-10-24.

**Evidence:** [preserved complete clip](../../raw/sources/clips/rea-output-first-workflow-nate-herk/source.md), [provenance and hash](../../raw/sources/clips/rea-output-first-workflow-nate-herk/PROVENANCE.md). Status: captured and text-compiled, not independently tested.

## What the source says

- At 1:06–2:55 he derives a desired style or workflow from concrete examples, including frame-by-frame motion analysis. References act as a more specific target than a generic request.

- At 3:22–4:54 he distinguishes recreating useful behavior from copying exact UI or an entire hosted service. His Loom-inspired recorder saves locally rather than reproducing Loom cloud infrastructure.

- At 7:36–10:58 his five-step approach is: pick one feature; route investigation by build type; read a saved summary before traces; mark findings seen/inferred/unknown; rebuild and test. Reusing the summary avoids rerunning very large analyses.

- At 9:48 he warns against building on inferred claims as though they were facts. At 10:58–12:27 he limits inspection to accessible/local evidence, warns against copying exact code/assets and says results depend on the model and setup.

- At 4:54 he promotes ScrollCraft for scroll-driven animations, layering, typography, spacing, depth and taste. This is a separate resource mention, not proof it outperforms existing GSAP/design skills.

- At 12:56–14:29 he reports better but slower results in his own REA comparison and extends the reference-first method to day-to-day processes and skills. This is an informal observation, not a benchmark.

## Application here, separated from source claims

This strengthens a practical design-reference workflow: inspect a particular picker, calendar or transition, save concise observations, and compare the rebuilt interaction with that target. It supports studying motion visually, not merely accumulating still screenshots.

## Actionable proposals

- Use existing ScrollCraft plus GSAP skills where relevant rather than install a duplicate from the promoted link.
- Select a specific reference behavior; save its evidence summary with seen/inferred/unknown labels and test criteria.
- Reuse saved investigation summaries rather than rerun large analysis files.
- Compare source and rebuilt behavior visually and interactively; keep screen appearance separate from functionality.
- If REA itself is useful, attach this evidence to the existing evaluation item and verify present setup before installation.

Queue disposition is coordinated in the [batch report](../../research/2026-10-24-design-hub/ingest-b.md). These proposals are not installations, approvals or production changes.

## Mentions in source

> "It's easier to pick out features." (7:36)

> "seen, inferred, or unknown." (9:23)

> "you should never be copying exact code or assets." (10:58)

## Limits and conflicts

Full captured transcript through 14:29 was read. No actual reference video, frame sequence, app internals, REA repository or ScrollCraft implementation was inspected in this text-ingest pass. Model names, changing star counts and quality/speed comparisons are attributed source claims only. No unresolved factual contradiction was established; differences in opinion or demonstration outcomes are not contradictions.

Related: [design hub](../../design/README.md), [website planning](../../references/website-design-planning.md), [AI workspace hub](../../references/ai-workspace/index.md). [Earlier Nick Saraev REA source](reverse-engineer-anything-rea.md).


## Design action routing (2026-10-24)

- Proposed, not built: [AQ-029 · Evaluate a bounded reference-driven design critique recipe](../../references/ai-workspace/action-queue.md).


## Related design sources (2026-10-24)

Complementary captured accounts, not independent verification of product claims: [rea-feature-investigation-chase-ai](rea-feature-investigation-chase-ai.md), [astra-website-design-loop-jack](astra-website-design-loop-jack.md). Compare their concrete methods through the [design hub](../../design/README.md).


## Queue record

Partial 2026-10-26: AQ-029. Bounded critique recipe implemented with observable findings and finite revisions. Remaining: use it on a selected rendered feature and preserve before/after evidence. [Implementation record](../../research/2026-10-26-source-implementation/REPORT.md).
