---
type: source
subject: "llm.c / dev/cuda/matmul_backward.cu"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: dev/cuda/matmul_backward.cu

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:49.930897Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/matmul_backward.cu) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `e171f336f3f2fb2aae87b04607ff48a6a768de8a36b0d75d337a472ba96bc79d`

## What the complete source contains

Evidence: `because gradients add` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/matmul_backward.cu)). The experiment uses cuBLAS GEMMs with beta one for accumulated input and weight gradients, plus a separate shared-memory reduction for bias gradients.

Evidence: `ugh the above isn't working` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/matmul_backward.cu)). Commented cuBLAS bias paths are explicitly left unresolved while the active bias kernel writes its sum. An OpenMP CPU reference and fixed-shape FP32 comparisons precede timing; this file was not compiled or benchmarked.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
