---
type: source
subject: "llm.c / llmc/gelu.cuh"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: llmc/gelu.cuh

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:50.230245Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/gelu.cuh) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `203ed0770e40c52e2eda837eb455cf8f851dc29b0638cdda33194e869a3db87b`

## What the complete source contains

Evidence: `Approximate) GeLU` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/gelu.cuh)). The implementation uses the tanh approximation to GELU and a hand-derived backward expression on packed 128-bit loads.

Evidence: `assert(N % (block_size * x128::size) == 0)` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/gelu.cuh)). Forward and in-place backward launchers require divisibility by their block/packing sizes, use different block sizes and check CUDA launch errors. Cache-streaming choices are explicit but performance was not measured.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
