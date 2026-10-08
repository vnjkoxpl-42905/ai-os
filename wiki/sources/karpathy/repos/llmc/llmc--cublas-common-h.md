---
type: source
subject: "llm.c / llmc/cublas_common.h"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: llmc/cublas_common.h

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:50.180220Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/cublas_common.h) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `8b23a2da5768506fb02c110dc071cdf947b502397d6af71caf033e6ce25841cc`

## What the complete source contains

Evidence: `default to bfloat16` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/cublas_common.h)). Compile flags choose FP32, FP16 or the default bfloat16 cuBLAS element type.

Evidence: `32 * 1024 * 1024` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/cublas_common.h)). It defines a 32-MiB cuBLASLt workspace and FP32 compute settings, maintains shared handles, and exits on cuBLAS status failures.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
