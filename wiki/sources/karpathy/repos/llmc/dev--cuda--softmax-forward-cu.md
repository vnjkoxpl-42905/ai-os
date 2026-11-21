---
type: source
subject: "llm.c / dev/cuda/softmax_forward.cu"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: dev/cuda/softmax_forward.cu

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:49.973254Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/softmax_forward.cu) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `5bc29aae3b655fbccdb40a9dc3a071e64f9b9f53e2c98d0fb0c82e346990013e`

## What the complete source contains

Evidence: `Online normalizer calculation for softmax` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/softmax_forward.cu)). The benchmark compares eight direct, shared-memory, warp-reduction, online-normalizer and large-vocabulary unrolled softmax variants, with a double-accumulating CPU reference.

Evidence: `the tests are not actually meaningful` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/softmax_forward.cu)). Inputs deliberately include amplified outliers so near-zero probabilities cannot make comparisons vacuous. A largest-probability assertion and six launch-size comparisons precede timing at GPT-2 vocabulary size; the quoted motivation is specific test design, not proof every boundary case passes.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
