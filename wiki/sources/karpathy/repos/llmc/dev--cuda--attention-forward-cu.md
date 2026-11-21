---
type: source
subject: "llm.c / dev/cuda/attention_forward.cu"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: dev/cuda/attention_forward.cu

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:49.841613Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/attention_forward.cu) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `ed6c8170cc350ac358ab473ee354b3f227e714ca4ac10fd0857e3940c450486e`

## What the complete source contains

Evidence: `taken, adapted from` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/attention_forward.cu)). The naive FlashAttention variant credits two external minimal implementations. Other variants compare a CPU-style GPU port, cuBLAS matrix products, fused causal online softmax, lower precision, and optional cuDNN attention.

Evidence: `recalculation is faster than doing the round-trip through memory.` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/attention_forward.cu)). The online causal softmax recomputes exponentials on its output pass rather than storing an intermediate exponential tensor; this is an implementation rationale, not a measured result here.

Evidence: `skipping (un)permute (unrealistic but useful comparison point)` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/attention_forward.cu)). One performance-only variant skips layout conversions after validation. These timings would not represent an otherwise unchanged FP32 end-to-end network.

Evidence: `Need a cache because graph->build_operation_graph() is slow` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/attention_forward.cu)). The optional cuDNN path caches graph plans, uses strided packed QKV directly, stores backward statistics when requested, and grows workspace on demand.

Evidence: `float accuracy_threshold = (kernel_num <= 4) ? 1e-3f : 1e-2f;` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/attention_forward.cu)). The fixed B=8, T=1024, C=768, NH=12 harness compares five block sizes and relaxes accuracy for lower precision. Intermediate attention matrices are checked only when the selected algorithm materializes comparable representations.

## Interpretation and limits

Read through EOF; no kernels executed. Header mentions version 11 but dispatch has no case 11. Claimed historical speedups are comments, not independently reproduced benchmarks. cuDNN conversion runs only once in its local first-run flag; later output validation does not reconvert each run. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
