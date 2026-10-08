---
type: source
subject: "llm.c / llmc/zero.cuh"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: llmc/zero.cuh

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:50.291817Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/zero.cuh) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `db46ddf5c15053d66cfa3679f79b895538a6b7a9ce7fe7f757f0400680607613`

## What the complete source contains

Evidence: `Zero Stage2 and Stage3 are not yet supported` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/zero.cuh)). The distributed utilities support disabled or stage-one optimizer sharding and explicitly fall back for unsupported later stages or nondivisible parameter counts.

Evidence: `we avoid having to synchronize the host` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/zero.cuh)). Gradient aggregation uses CUDA events to order compute and NCCL streams, grouping all-reduce or reduce-scatter calls. Initialization can share NCCL IDs via MPI, TCP or a shared-file protocol; the latter is explicitly described as naive synchronization. NCCL example code is credited. Network/file robustness and multi-GPU correctness were not tested here.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
