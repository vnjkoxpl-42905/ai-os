---
type: source
subject: "llm.c / dev/cuda/gelu_backward.cu"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: dev/cuda/gelu_backward.cu

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:49.900069Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/gelu_backward.cu) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `657cc0fcf305ee20fd1eae082dfd8061c67e57822469d3819d96c572ccdf0dcf`

## What the complete source contains

Evidence: `version 2 uses the Packed128 data structure` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/gelu_backward.cu)). The backward benchmark compares scalar and packed CUDA forms of the analytic tanh-GELU derivative with a CPU calculation.

Evidence: `float tol = 1e-2f` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/gelu_backward.cu)). BF16/FP16 validation permits a larger tolerance than FP32; the harness performs comparisons before repeated timing. Its bandwidth calculation is a rough formula in code, not a measured efficiency result for Joshua hardware.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
