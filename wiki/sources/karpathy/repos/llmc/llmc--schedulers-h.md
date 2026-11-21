---
type: source
subject: "llm.c / llmc/schedulers.h"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: llmc/schedulers.h

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:50.277587Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/schedulers.h) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `1f5dfc93b57009c0f154665f75b0764226e7f933c7856d3e8a6650f30cfd434c`

## What the complete source contains

Evidence: `last 20% decay using 1 - sqrt` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/schedulers.h)). The scheduler implements cosine, linear, constant and warmup-stable-decay variants; WSD holds the peak until the final fifth of training.

Evidence: `Unknown learning rate scheduler type:` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/schedulers.h)). Dispatch is explicit by string, and an unsupported type terminates with an error. Decaying schedules assert an in-range ratio rather than accepting arbitrary steps.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
