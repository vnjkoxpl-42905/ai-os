---
type: source
subject: "llm.c / dev/cuda/fused_residual_forward.cu"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: dev/cuda/fused_residual_forward.cu

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:49.892940Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/fused_residual_forward.cu) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `f1c1c112eaadf0d9a137b4214c02660615729239641bd2aaf7946c522536b033`

## What the complete source contains

Evidence: `numerically more stable variance estimation` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/fused_residual_forward.cu)). The BF16 experiment advances from separate residual-plus-normalization launches through naive and warp fusion, vectorized one-pass statistics, shared-memory caching with centered variance, and persistent multiple-warps-per-token processing.

Evidence: `this may fail, in which case we fall back` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/fused_residual_forward.cu)). Shared-memory variants provide lower-memory fallbacks when resource configuration fails. The harness compares residual, normalized output and statistics over six block sizes before timing. Several captured token guards use idx greater than N rather than greater-or-equal; fixed divisible-shape comparisons do not establish general boundary safety. No kernel ran here.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
