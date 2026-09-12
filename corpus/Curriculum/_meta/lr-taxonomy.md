---
type: teaching-notes
subject: LR taxonomy the two axes
updated: 2026-07-16
aliases: []
---

# LR taxonomy — the two axes

Recovered from the pre-consolidation `LSAT DUMP/LR/` structure (2026-07-16). This is the reference model for how LR content is organized. `corpus/Curriculum/` is currently **flat** — one folder per topic, each with `Homework/` and `Notes/`. This document records the ontology behind it so the flat names stay principled.

## The core distinction

Two independent dimensions get confused constantly:

- **Question type** — what the question asks you to *do*. Find the conclusion, weaken the argument, match the structure.
- **Reasoning pattern** — what the argument is *made of*. Causal, conditional, quantified, comparative.

They are orthogonal. A causal argument can appear inside a Weaken question, a Flaw question, or a Must Be True question. Filing "Causation" and "Role" as siblings implies they are the same kind of thing. They are not.

## Axis 1 — question families

Grouped by the cognitive move the question demands.

| Family | Types |
|---|---|
| **Assumption & Objection** — supply or attack the missing link | Flaw · Necessary Assumption · Sufficient Assumption · Strengthen · Weaken · Principle |
| **Inference** — derive what follows | Must Be True · Must Be False · Most Supported |
| **Match** — identify or mirror structure | Main Conclusion · Method · Role · Parallel · Parallel Flaw · Agree/Disagree |
| **Unfamilied** | Paradox |

## Axis 2 — reasoning patterns

What the stimulus is built from, cutting across every family above.

Abstract · Causation · Comparison · Conditional Logic (→ Conditional Diagramming) · Quantifiers · Rebuttals · Explain Curious Fact · Famous Flaws · Math-y Stuff

`_question-feature-index/_reasoning-types/` is where this axis is indexed.

## Current state

All 23 topic folders carry `Homework/` + `Notes/`. Added 2026-07-16 to close gaps against this model: **Weaken, Paradox, Most Supported, Must Be False, Agree Disagree** (previously absent), and `Flaw/` gained the `Homework`+`Notes` pair its siblings already had.

Still unmodeled as folders, tracked here only: Explain Curious Fact, Famous Flaws, Math-y Stuff, Rebuttals, Conditional Diagramming.

## Relation to the app

LSAT U bootcamps draw from this. Bootcamp names seen in the pre-consolidation build output: `lrfoundational`, `structuredrill`, `introconclusiondrill`, `first-sentence-vs-rebuttal`, `arguments`, `causation-station`.
