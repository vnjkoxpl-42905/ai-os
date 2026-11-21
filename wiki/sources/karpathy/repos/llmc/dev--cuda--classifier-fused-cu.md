---
type: source
subject: "llm.c / dev/cuda/classifier_fused.cu"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: dev/cuda/classifier_fused.cu

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:49.854401Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/classifier_fused.cu) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `ba90f81dc8fb6e231cf2d17dbe79bda9ccf73bc368cb0f00eb14fcc733ef5cfc`

## What the complete source contains

Evidence: `dloss\` can be known beforehand` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/classifier_fused.cu)). The experiment fuses stable softmax, target cross-entropy and logit derivatives to avoid materializing full probability tensors. Five variants compare warp/block reductions, float4 or Packed128 access, padded vocabulary handling and optional probability/gradient writes.

Evidence: `the outputs will be wrong` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/classifier_fused.cu)). The source explicitly warns that the captured low-precision harness lacks proper format conversion; kernel four/five BF16 or FP16 runs skip correctness checks and are timing-only. FP32 fixed-shape loss/gradient comparisons undo padding and use amplified outliers. No performance measurements or passing validation were produced here.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
