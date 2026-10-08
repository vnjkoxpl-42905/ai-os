---
type: source
subject: "llm.c / dev/cuda/layernorm_forward.cu"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: dev/cuda/layernorm_forward.cu

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:49.921223Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/layernorm_forward.cu) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `f17d02e245e9f133e9658f1d3a9e05986f95d6e0471ebd0f1ac48bdea6e544d0`

## What the complete source contains

Evidence: `var(x) == mean(x**2) - mean(x)**2` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/layernorm_forward.cu)). Six variants compare serial rows, separate mean/variance/normalization launches, cooperative warp reductions, one-pass moment estimates, block-per-row reductions and packed shared-memory caching. All retain normalization statistics for backward use.

Evidence: `fall back to the version without shared memory` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/layernorm_forward.cu)). The packed launcher falls back if dynamic shared-memory configuration fails. The harness compares output, mean and reciprocal standard deviation across six block sizes at one fixed shape before timing. Numerical stability, arbitrary shapes and GPU resource compatibility were not independently tested.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
