---
type: source
subject: "llm.c / dev/cuda/Makefile"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: dev/cuda/Makefile

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:49.926822Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/Makefile) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `1056179fba1f0483913238ca5d028f0996cae7e84885ec631146abc5086a742c`

## What the complete source contains

Evidence: `nvcc not found.` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/Makefile)). The standalone-kernel Makefile requires nvcc and optionally emits code for an explicit or locally queried GPU compute capability.

Evidence: `all_ptx:` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/Makefile)). It groups forward/backward, optimizer, norm, permutation and NCCL executables, provides run-all targets and exports PTX/SASS through cuobjdump. Matmul adds OpenMP while NCCL adds MPI/NCCL libraries; its paths are Linux examples.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
