---
type: source
subject: "llm.c / scripts/run_gpt2_124M.sh"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: scripts/run_gpt2_124M.sh

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:50.308223Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/scripts/run_gpt2_124M.sh) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `c0fbaba7108b6971c12aca2a65854048528f87fdb90d79b3055ba246a605c983`

## What the complete source contains

Evidence: `DONE_00018865` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/scripts/run_gpt2_124M.sh)). The CUDA recipe loops until the expected completion marker appears, with resume enabled and eight MPI ranks.

Evidence: `-e "d12"` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/scripts/run_gpt2_124M.sh)). The d12 FineWeb10B recipe configures sequence length 1024, global batch 524288 and learning rate 0.0006. The comments estimate time and cost on A100 hardware; those are historical source estimates, not current prices.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
