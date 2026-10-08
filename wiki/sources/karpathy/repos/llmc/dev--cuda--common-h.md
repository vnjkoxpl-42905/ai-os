---
type: source
subject: "llm.c / dev/cuda/common.h"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: dev/cuda/common.h

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:49.863717Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/common.h) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `cf73117df76f26ce18ba03a5c67c4de96478fb627c0467675c316ad9b05bcfed`

## What the complete source contains

Evidence: `Packed128 data structure` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/common.h)). The benchmark header supplies aligned vector loads/stores and cache hints, warp/block reductions, precision aliases, random tensors, CUDA/cuBLAS checks, and GPU-zero setup with architecture-dependent TF32 selection.

Evidence: `Skip masked elements` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/common.h)). Numerical comparison skips nonfinite CPU references and applies absolute-plus-relative rounding tolerance, with BF16 epsilon 0.079; mismatches terminate. The timer clears L2 before each measured CUDA-event call. These harness choices are implementation evidence, not proof of tested kernels or exhaustive nonfinite-result handling.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
