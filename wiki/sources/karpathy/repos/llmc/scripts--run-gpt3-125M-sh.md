---
type: source
subject: "llm.c / scripts/run_gpt3_125M.sh"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: scripts/run_gpt3_125M.sh

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:50.329223Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/scripts/run_gpt3_125M.sh) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `9cdec0f9ceb209e7225ce7c8f3296086299948884c776637aabc8e3b2837828e`

## What the complete source contains

Evidence: `note context length: 1024 -> 2048 for GPT-3` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/scripts/run_gpt3_125M.sh)). The source explicitly distinguishes its GPT-3-style context length from GPT-2.

Evidence: `-e "gpt3:c768"` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/scripts/run_gpt3_125M.sh)). Its FineWeb recipe selects gpt3:c768, sequence length 2048, 572204 steps, resume, cosine-related decay and loss/gradient skip thresholds. The comments describe 300B-token training; no run is evidenced here.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
