---
type: source
subject: "llm.c / Makefile"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: Makefile

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:49.693097Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/Makefile) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `c51520f9a03256163ec170a5ff862976c6a6345332ecaf11f70682139e34a575`

## What the complete source contains

Evidence: `PRECISION ?= BF16` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/Makefile)). The root build defaults to BF16 with validated FP32/FP16 alternatives and generates CPU, CUDA, reference-test and profiling targets according to compiler availability.

Evidence: `cuDNN is manually disabled by default` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/Makefile)). It detects platform-dependent OpenMP, optional cuDNN, NCCL and MPI, with Linux/macOS and Windows MSVC handling, customizable compute capability and build paths. Configuration detection and compilation were not run; captured paths/version assumptions need local validation.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
