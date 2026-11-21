---
type: source
subject: "llm.c / dev/cuda/matmul_backward_bias.cu"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: dev/cuda/matmul_backward_bias.cu

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:49.935076Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/matmul_backward_bias.cu) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `38294acb8f1d15d4a2661d8149bc1647e6c4a3cb4099d53dc7facef62f730723`

## What the complete source contains

Evidence: `dbias = dout.sum((0,1))` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/matmul_backward_bias.cu)). The bias-only experiment compares channel-wise block/warp reductions, coalesced column reductions, FP32 atomics with low-precision conversion, smaller packed warp tiles, and separately reduced auxiliary partials.

Evidence: `kernel 9 overwrites temp buffer` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/matmul_backward_bias.cu)). Kernel nine avoids clearing temporary storage by writing separate partial sums, while launchers bypass the auxiliary buffer when one reduction partition suffices. The harness resets output before seven fixed-shape comparisons, with looser BF16 tolerance, then times repeated calls. No measured performance or general shape safety is claimed.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
