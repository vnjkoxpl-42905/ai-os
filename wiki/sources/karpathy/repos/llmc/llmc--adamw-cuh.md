---
type: source
subject: "llm.c / llmc/adamw.cuh"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: llmc/adamw.cuh

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:50.165610Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/adamw.cuh) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `08a7ddbc007c092006a0ba096dc644fe12939eb793f323c3f02eb611fad24fbb`

## What the complete source contains

Evidence: `update our low precision version of the parameters using stochastic rounding` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/adamw.cuh)). The optimizer updates first/second moments in float, applies bias corrections and weight decay, and writes low-precision parameters with stochastic rounding; an optional float master copy retains the update value.

Evidence: `must match block size of adamw_update so that RNG also matches` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/adamw.cuh)). Both update and master-copy initialization use matching 512-thread launch blocks and shared seed conventions, with strided slices and caller-provided gradient scaling. The interpolation helper credits an NVIDIA technique; repository ownership does not imply sole authorship.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
