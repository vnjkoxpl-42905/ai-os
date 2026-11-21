---
type: source
subject: "llm.c / dev/cuda/permute.cu"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: dev/cuda/permute.cu

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:49.953891Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/permute.cu) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `151f35e936527450ddc300580be5cfebbd49ace12f8f96bf3f38a658ad409228`

## What the complete source contains

Evidence: `dim4, dim3, dim1, dim2` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/permute.cu)). The teaching example explains flattening and reindexing a four-dimensional tensor into a different axis order, then implements matching CPU and CUDA permutations.

Evidence: `validate_result(d_permuted_matrix` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/permute.cu)). Its main program computes a CPU reference, checks GPU output and benchmarks repeated launches. The printed CPU timing label says milliseconds although its clock-derived variable is seconds; no timing or correctness was independently measured.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
