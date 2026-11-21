---
type: source
subject: "llm.c / dev/data/tinyshakespeare.py"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: dev/data/tinyshakespeare.py

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:50.027870Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/data/tinyshakespeare.py) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `3d85d9eb6ff52d0c7498b9c25aadb428c9887af972448d1b3b73a5781a333cae`

## What the complete source contains

Evidence: `keeping that behavior for backwards compatibility` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/data/tinyshakespeare.py)). The preprocessor preserves its historic newline behavior around end-of-text-delimited sections rather than silently changing dataset bytes.

Evidence: `val_tokens = tokens[:32768]` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/data/tinyshakespeare.py)). It downloads the char-rnn text if absent, supports GPT-2 or Llama tokenization and takes the first 32768 tokens for validation, writing the rest as training data through the common binary writer. Commented sample counts are historical output, not regenerated results.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
