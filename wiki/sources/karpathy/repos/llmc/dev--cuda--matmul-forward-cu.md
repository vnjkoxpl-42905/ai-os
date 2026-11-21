---
type: source
subject: "llm.c / dev/cuda/matmul_forward.cu"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: dev/cuda/matmul_forward.cu

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:49.942898Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/matmul_forward.cu) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `264b6feb706ce36ce30871e2096ea02c20a2ad1c47f4582206d78b2eb41b98fb`

## What the complete source contains

Evidence: `semi-efficient handwritten kernel` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/matmul_forward.cu)). Four forward variants span direct per-output loops, cuBLAS plus separate bias addition, cuBLASLt bias epilogue, and a handwritten shared-memory/vectorized 128-by-128 tile.

Evidence: `int has_gelu = 0;` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/matmul_forward.cu)). The Lt path contains optional GELU epilogue branches but disables GELU in this harness. The fixed GPT-2-like shape is CPU-compared before timings over four launch sizes; TF32 is architecture-selected, and claimed efficiency or shape-general correctness was not reproduced.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
