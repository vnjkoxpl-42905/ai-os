---
type: source
subject: "llm.c / dev/test/Makefile"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: dev/test/Makefile

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:50.074496Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/test/Makefile) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `ae418d64573281ed5e575c00c1189631371046db71c04041c3a38e9b0cd821db`

## What the complete source contains

Evidence: `CFLAGS += $(TEST_CFLAGS)` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/test/Makefile)). The test Makefile supports caller-supplied flags including the documented AddressSanitizer example, and tracks header dependencies for the dataloader test.

Evidence: `Invalid precision` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/test/Makefile)). It accepts FP32/FP16/BF16, detects OpenMP and optional CUDA/multi-GPU support, and requires explicit valid precision except for clean. cuDNN is opt-in; the declared target set here contains only test_dataloader.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
