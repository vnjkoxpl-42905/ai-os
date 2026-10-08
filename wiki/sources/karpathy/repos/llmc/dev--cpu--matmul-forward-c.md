---
type: source
subject: "llm.c / dev/cpu/matmul_forward.c"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: dev/cpu/matmul_forward.c

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:49.822485Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cpu/matmul_forward.c) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `681d81f1e603bb7efd8727b625f8bed802be5ac821237bbf8520a3a3c732acee`

## What the complete source contains

Evidence: `reuse the loaded weight LOOP_UNROLL many times` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cpu/matmul_forward.c)). The CPU experiment compares a direct matrix multiplication with an eight-position unrolled variant credited by its ngc92 name, aiming to reuse weights across batch/time positions.

Evidence: `float t_eff = tolerance + fabs(cpu_reference[i]);` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cpu/matmul_forward.c)). It verifies seeded outputs then times repeated kernels. The effective error threshold includes the full reference magnitude, a much looser criterion than a conventional tiny relative tolerance; the nonmultiple-of-eight case prints and returns rather than taking the comment-described fallback.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
