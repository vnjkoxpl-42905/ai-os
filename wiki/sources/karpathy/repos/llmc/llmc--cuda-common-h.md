---
type: source
subject: "llm.c / llmc/cuda_common.h"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: llmc/cuda_common.h

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:50.187380Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/cuda_common.h) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `a8e62a7a6c76c5c410872d4b999e4afa167f966c7d5620d266b1fd51f719ab2e`

## What the complete source contains

Evidence: `currently not implemented` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/cuda_common.h)). CUDA precision selection includes a source warning that FP16 may require a gradient scaler not currently implemented; the default type is bfloat16.

Evidence: `using double buffering` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/cuda_common.h)). Device/file transfer helpers allocate two pinned host buffers and overlap transfers with disk reads or writes, with checked operations and stream synchronization. The header also supplies CUDA error handling, freeing with pointer reset, NVTX scopes and architecture-based launch constants. The declaration named False actually has true bool_constant type in the captured text; semantic inspection does not establish runtime impact.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
