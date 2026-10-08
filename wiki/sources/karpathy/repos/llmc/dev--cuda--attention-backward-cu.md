---
type: source
subject: "llm.c / dev/cuda/attention_backward.cu"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: dev/cuda/attention_backward.cu

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:49.834922Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/attention_backward.cu) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `f97d80a1dd74533817c9c5c0d89998f663863d257e324fb4218bb6d73292e623`

## What the complete source contains

Evidence: `scale instead moved and fused into the softmax` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/attention_backward.cu)). The demonstration moves attention scaling into causal softmax and decomposes attention gradients into layout transformations, batched matrix products, and a selectable softmax derivative.

Evidence: `Actually disentangling the loops and simplifying the resulting math` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/attention_backward.cu)). Eight backward-softmax variants progress from explicit Jacobian loops through register/shared-memory reuse to a weighted-row-sum algebraic simplification.

Evidence: `go through blocks in reverse order, so the slowest block starts first` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/attention_backward.cu)). The final variant schedules long causal rows first and processes four rows per block to reduce the scheduling tail.

Evidence: `the gradients at qkvr and vaccum will remain unchecked` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/attention_backward.cu)). The harness compares attention matrices and input gradients with a CPU reference, but leaves two intermediate gradient buffers unchecked. Its forward matrix comparisons use B*T*C rather than the full B*NH*T*T extent.

Evidence: `Number of non-matching gradients:` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/attention_backward.cu)). A separate input-gradient mismatch count is printed without changing the final success return; timing sweeps six block sizes on a fixed B=4, T=1024, C=768, NH=12 case.

## Interpretation and limits

Read through EOF. Source-level comparisons are not executed results. Fixed divisible dimensions and partial forward comparisons do not establish general-shape correctness. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
