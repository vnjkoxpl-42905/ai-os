---
type: source
subject: "llm.c / llmc/cudnn_att.cpp"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: llmc/cudnn_att.cpp

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:50.198446Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/cudnn_att.cpp) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `58fd7e545427a4ba3953551c604de4835ef9acf63d04463acdfe12ba6169ad5f`

## What the complete source contains

Evidence: `Need a cache because graph->build_operation_graph() is slow` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/cudnn_att.cpp)). cuDNN frontend graphs are cached by dimensions and inference/training mode so repeated attention calls reuse built plans and a workspace grown only as needed.

Evidence: `Loosely based on cuDNN frontend samples` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/cudnn_att.cpp)). The credited sample-derived implementation feeds packed QKV through causal scaled dot-product forward/backward attention with float computation and BF16/FP16 IO; training retains statistics. FP32 is rejected at compile time and newer frontend versions select deterministic backward algorithms. Compatibility and determinism were not executed or measured here.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
