---
type: source
subject: "llm.c / llmc/mfu.h"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: llmc/mfu.h

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:50.256574Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/mfu.h) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `ae11125a837b1c9ef6e3677d47cf20774466e0c8e0fe620aa57d3f72c54d4888`

## What the complete source contains

Evidence: `may well go wrong` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/mfu.h)). The header explicitly qualifies its theoretical GPU FLOPS estimates, scaling architecture baseline figures by specific tensor-core counts and clock rates to estimate model utilization.

Evidence: `Compiled without nvml support` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/mfu.h)). Optional NVML code retrieves GPU zero clock/power/thermal/fan and averaged utilization samples, with simplified throttle reasons. Missing NVML tracking terminates; unsupported devices or precisions return unavailable FLOPS. Stored GPU specifications are historical source data, not current verified hardware facts.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
