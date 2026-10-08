---
type: source
subject: "llm.c / llmc/sampler.h"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: llmc/sampler.h

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:50.272070Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/sampler.h) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `06401eb36656617fb604b144a7ea89df0915c68226bf4d436f94a5daf2b68ac1`

## What the complete source contains

Evidence: `Simple xorshift RNG` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/sampler.h)). This header supplies a xorshift random generator and a float draw in the unit interval.

Evidence: `coin *= norm;` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/sampler.h)). Token sampling sums exponentiated logits and scales the draw by that sum before traversing the cumulative mass, with a final-token rounding fallback. It is a minimal sampler without a max-logit stabilization step in this function.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
