---
type: source
subject: "llm.c / dev/cuda/nccl_all_reduce.cu"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: dev/cuda/nccl_all_reduce.cu

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:49.949877Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/nccl_all_reduce.cu) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `2845c929f87d55e4791e5414c72f49d7e8d16e7111d49e4144cea368006ee546`

## What the complete source contains

Evidence: `Copied from NCCL examples` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/nccl_all_reduce.cu)). The credited NCCL example uses hostname hashes to assign local GPU indices, MPI to broadcast a communicator ID, and one rank-valued vector per process.

Evidence: `ncclSum` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/nccl_all_reduce.cu)). It sums 32-million-element vectors collectively and compares their host mean with the sum of rank values. The error branch prints without changing the program exit status; the Linux MPI launch example was not executed.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
