---
type: source
subject: "llm.c / dev/cuda/layernorm_backward.cu"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: dev/cuda/layernorm_backward.cu

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:49.916358Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/layernorm_backward.cu) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `af6b5ced78a7e0d3230aac5e429e90370f56912456aec973ec686f2013e6b2a7`

## What the complete source contains

Evidence: `first: two reduce operations` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/layernorm_backward.cu)). The CPU reference computes the two row-wise reductions needed for input gradients and accumulates input, scale, and bias gradients. Ten CUDA variants explore how these reductions and cross-row parameter sums are organized.

Evidence: `FP32 scratchpad per threadgroup, zero atomics except atomicAdd` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/layernorm_backward.cu)). One variant stores each block contribution in FP32 scratch memory and uses a completion counter so the final block reduces partial sums; other variants use shared or global floating-point atomics or BF16 compare-and-swap.

Evidence: `we use a shared memory friendly index, and reorder before the final write` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/layernorm_backward.cu)). Packed-load variants separate the coalesced global-memory layout from the shared-memory banking layout, then reorder parameter gradients on output.

Evidence: `warning: this kernel is _extremely_ close to getting register spills` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/layernorm_backward.cu)). The final variant trades increased shared memory for vector accesses and fewer barriers, with explicit comments warning that register pressure can erase a putative optimization.

Evidence: `int C = 1600;   // this is the problematic size` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/layernorm_backward.cu)). The harness targets B=8, T=1024, C=1600 with six block sizes; lower-precision tolerances are 0.1 for input gradients and 0.5 for parameter gradients. Version 9 requires channel divisibility and therefore is incompatible with this BF16 channel count.

## Interpretation and limits

Read through EOF; no GPU run. The harness omits block size 768 due to a documented failure. Version 10 remaps 1024 threads to 512, so those requested cases are not distinct launches. Performance and correctness comments remain source evidence only. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
