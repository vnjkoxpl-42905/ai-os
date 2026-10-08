---
type: source
subject: "llm.c / dev/cuda/gelu_forward.cu"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: dev/cuda/gelu_forward.cu

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:49.903622Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/gelu_forward.cu) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `8bb3661d3a24f1c7f4f071bd581be604e249947094d2ba18c590c2fcbb64397c`

## What the complete source contains

Evidence: `version 2 is bfloat16 with the Packed128 data structure` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/gelu_forward.cu)). The experiment compares scalar and packed BF16 tanh-GELU forward kernels with a CPU reference.

Evidence: `validate_result(d_out, out` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/gelu_forward.cu)). It evaluates six block sizes with precision-dependent tolerance before timing repeats and estimating bandwidth. Streaming-load versus cached-store choices are explicit; advertised bandwidth comments are historical context rather than achieved local measurements.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
