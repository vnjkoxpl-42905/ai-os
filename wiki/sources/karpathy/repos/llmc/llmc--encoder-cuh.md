---
type: source
subject: "llm.c / llmc/encoder.cuh"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: llmc/encoder.cuh

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:50.215116Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/encoder.cuh) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `a80b0164ce53a62851401a47dcf7b411c756d7f4631b96faa5c8afe4f76ca938`

## What the complete source contains

Evidence: `combines two encodings: token and position` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/encoder.cuh)). The forward encoder adds packed token and position embedding vectors; separate backward kernels accumulate into both tables.

Evidence: `we preprocess the inputs on the cpu into "buckets"` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/encoder.cuh)). Token-gradient reduction groups repeated token/channel workloads on CPU, orders larger buckets first and reduces in a fixed structure instead of relying on nondeterministic atomic aggregation. Position gradients sum across the batch, while seeded stochastic rounding converts low-precision writes. Determinism and performance are implementation intent, not locally tested outcomes.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
