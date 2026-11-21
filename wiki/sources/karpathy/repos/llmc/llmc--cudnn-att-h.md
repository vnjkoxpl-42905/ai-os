---
type: source
subject: "llm.c / llmc/cudnn_att.h"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: llmc/cudnn_att.h

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:50.203049Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/cudnn_att.h) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `50621fde56d739efffb95fab1506a391b2a78d7afdfafe54eaf25b59a083cba5`

## What the complete source contains

Evidence: `cuDNN (flash) attention` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/cudnn_att.h)). This header declares creation/destruction and forward/backward cuDNN attention interfaces.

Evidence: `input: (B, T, 3, NH, HS) QKV` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/cudnn_att.h)). The documented interface uses packed QKV inputs and separate statistics for the backward pass, with shape dimensions and a CUDA stream passed explicitly. The implementations live elsewhere.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
