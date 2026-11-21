---
type: source
subject: "llm.c / dev/download_starter_pack.sh"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: dev/download_starter_pack.sh

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:49.794652Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/download_starter_pack.sh) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `4069547f54eb1632e1724671bfaf1ddb234109cbd39da79544fad2f687ba77bc`

## What the complete source contains

Evidence: `gpt2_124M_debug_state.bin` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/download_starter_pack.sh)). The starter pack includes GPT-2 weight, debug-state and tokenizer files plus Tiny Shakespeare and HellaSwag binary data.

Evidence: `run_in_parallel 6` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/download_starter_pack.sh)). It routes data files by filename into their dataset directories and other files to the repository parent of dev, using up to six parallel commands. The comment says batches of two but code passes six; neither establishes download success.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
