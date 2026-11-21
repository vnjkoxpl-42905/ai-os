---
type: source
subject: Karpathy repository source context
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [llm-wiki, karpathy, source-context]
sources:
  - ../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanochat/tests/test_tokenizer.py
---

# repos/karpathy/nanochat/tests/test_tokenizer.py

Original: [captured source](https://github.com/karpathy/nanochat). Capture: 2026-10-08T09:35:02.575458Z. Attribution: karpathy; classification: `authored_code`.

Archived: [physical raw file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanochat/tests/test_tokenizer.py). SHA-256: `761c29ec91b8dc1ff11b62681388233587e15566dcc2cfc67b8718135bdce571`.

## Source account

```text
Trains a tiny throwaway tokenizer in-process
```

A hermetic tiny BPE fixture checks vocabulary size, Unicode roundtrips, unique explicit special tokens, ordinary special-token-looking text, batched encoding, completion rendering and truncation. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanochat/tests/test_tokenizer.py).

```text
python tool calls are supervised, python outputs (come from the interpreter) are not
```

Conversation tests check assistant-only training masks, merged system instructions, supervised tool calls, and unsupervised interpreter output delimiters/content. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanochat/tests/test_tokenizer.py).

## Limits

Code not executed; configured checks are not passing test evidence. This source does not independently establish Karpathy personal beliefs. Raw unchanged.
