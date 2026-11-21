---
type: source
subject: "llm.c / dev/data/data_common.py"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: dev/data/data_common.py

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:49.985951Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/data/data_common.py) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `d58249637bab130794fbe7bc2762f2b876449528efdd39a48cc78aeedc28827a`

## What the complete source contains

Evidence: `First comes a header with 256 int32s` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/data/data_common.py)). Shared writers serialize token datasets with a fixed binary header and model-specific GPT-2 uint16 or Llama uint32 token storage.

Evidence: `expected 4 completions for now` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/data/data_common.py)). The multiple-choice writer stores four candidates, context/completion token lengths, labels, indices, byte lengths and a delimiter, with range/size assertions. The download helper streams response bytes with progress but does not explicitly raise HTTP status failures.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
