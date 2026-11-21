---
type: source
subject: "llm.c / llmc/matmul.cuh"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: llmc/matmul.cuh

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:50.251034Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/matmul.cuh) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `56a506fe614ec25370a3475ea893a0c0655bc0beadf3b3ee49bb5f27e4160342`

## What the complete source contains

Evidence: `All cuBLASLt pointers must be aligned` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/matmul.cuh)). The cuBLASLt wrapper enforces 16-byte pointer alignment, configures transpose/strided batches, workspace heuristics, accumulation and bias/GELU epilogues, then destroys temporary descriptors.

Evidence: `we can skip the bias_buffer accumulation` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/matmul.cuh)). Backward bias reduction either writes directly or reduces temporary partials according to available parallelism. Input gradients overwrite, weight gradients accumulate, and GELU may run as a fused epilogue or separate kernel. Hardware-efficiency comments are tentative source observations, not local benchmarks.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
