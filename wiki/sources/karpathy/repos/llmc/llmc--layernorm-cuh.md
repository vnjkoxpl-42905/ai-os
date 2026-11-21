---
type: source
subject: "llm.c / llmc/layernorm.cuh"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: llmc/layernorm.cuh

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:50.238785Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/layernorm.cuh) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `fa66e3ef08b1b03a48ed85a5b22fb5f2447eb6a15ac09ff8e676958decb1ce6d`

## What the complete source contains

Evidence: `All parameters use a += in the backward pass` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/layernorm.cuh)). The header distinguishes accumulated parameter/residual gradients from overwriteable activation gradients and implements packed normalization, residual sum, and fused residual-plus-normalization operations.

Evidence: `fall back to the version without shared memory` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/layernorm.cuh)). Forward launchers attempt larger shared-memory kernels and provide non-shared or separate-operation fallbacks. Backward calculates local gradients, reduces parameter partials through shared/global scratch, and uses an atomic completion flag so the last block combines them. Captured shape guards, synchronization and resource assumptions need numerical and GPU validation; no run was performed.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
