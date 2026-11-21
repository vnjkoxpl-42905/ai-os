---
type: source
subject: "llm.c / test_gpt2.c"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: test_gpt2.c

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:49.720212Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/test_gpt2.c) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `f08f9849455948677055e89ed5ac5992cf641593547ff772b8be8ea69e952780`

## What the complete source contains

Evidence: `ignoring padding` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/test_gpt2.c)). The CPU integration test reads exported Python inputs, logits, loss and gradients, compares real vocabulary entries while respecting padded tensor stride, and checks sixteen parameter-gradient tensors.

Evidence: `overall okay: %d` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/test_gpt2.c)). It runs ten training updates against fixed expected losses and combines comparison flags into allok, but ends with return zero regardless of that flag. Printed agreement and successful process exit are distinct; no reference checkpoint or test was executed here.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
