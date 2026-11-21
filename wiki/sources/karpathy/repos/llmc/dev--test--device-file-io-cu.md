---
type: source
subject: "llm.c / dev/test/device_file_io.cu"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: dev/test/device_file_io.cu

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:50.068972Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/test/device_file_io.cu) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `fa06dcf4fc8b2f5484f0cda1a4c42c640acbcfea18bc9685ae3883c3e6cdd096`

## What the complete source contains

Evidence: `if(random_data[i] != cmp[i])` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/test/device_file_io.cu)). The GPU/file round-trip test copies seeded floats to device memory, writes and reloads through differently sized host buffers, then requires exact element equality.

Evidence: `test(125'000, 10000, 10000)` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/test/device_file_io.cu)). Its cases cover buffers larger than the data, unequal smaller buffers, exact size and a larger array. It removes its temporary file after a mismatch or completed comparison; no execution occurred here.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
