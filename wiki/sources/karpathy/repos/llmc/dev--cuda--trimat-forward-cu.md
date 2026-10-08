---
type: source
subject: "llm.c / dev/cuda/trimat_forward.cu"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: dev/cuda/trimat_forward.cu

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:49.980418Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/trimat_forward.cu) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `de489128de76194a5710fc4466c7d050f33edc661c08e9a6e83cf856352cdf0b`

## What the complete source contains

Evidence: `by @ngc92` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/trimat_forward.cu)). This contributor-attributed story teaches lower-triangular autoregressive query-key multiplication through a cuBLAS baseline, naive loops, register reuse, packed coalesced loads and shared-memory tiles. Its cookie-cutter analogy explicitly identifies register capacity, strided access and bank conflicts.

Evidence: `assert(T % 128 == 0);` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/trimat_forward.cu)). Handwritten launchers require sequence length divisible by 128. The CPU reference masks upper-triangle values with NaNs so comparisons ignore that region; timing comments are historical narrative claims, not local measurements. The executable compares one GPT-2-like shape before cuBLAS timing and was not run. This is not exclusively Karpathy-authored evidence.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
