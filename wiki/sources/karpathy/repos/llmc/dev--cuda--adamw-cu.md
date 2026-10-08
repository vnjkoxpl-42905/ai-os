---
type: source
subject: "llm.c / dev/cuda/adamw.cu"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: dev/cuda/adamw.cu

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:49.828522Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/adamw.cu) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `93efbc8828167136721311388a9cf612954bfe8ec9827b75a67ef0152a3834eb`

## What the complete source contains

Evidence: `using optimized linear interpolation` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/adamw.cu)). The standalone experiment compares a fused scalar AdamW kernel with a register-cached interpolation variant against a CPU reference. Moment bias corrections are computed once by the host launcher.

Evidence: `amsgrad=True` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/adamw.cu)). AMSGrad, precision variants and further instruction-level optimizations remain explicit TODOs. The harness checks parameters and both moments for one seeded configuration before 1000 timing repeats; no execution or performance result is established here.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
