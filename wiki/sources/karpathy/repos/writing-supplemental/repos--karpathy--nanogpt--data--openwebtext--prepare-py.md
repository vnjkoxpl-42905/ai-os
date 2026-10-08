---
type: source
subject: Karpathy repository source context
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [llm-wiki, karpathy, source-context]
sources:
  - ../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanoGPT/data/openwebtext/prepare.py
---

# repos/karpathy/nanoGPT/data/openwebtext/prepare.py

Original: [captured source](https://github.com/karpathy/nanoGPT). Capture: 2026-10-08T09:35:04.217222Z. Attribution: karpathy; classification: `authored_code`.

Archived: [physical raw file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanoGPT/data/openwebtext/prepare.py). SHA-256: `77f3ef0cc8132d77f90c2bd5f9c3be86d1b3da7428e100559c58aee2bcb6eb12`.

## Source account

```text
train_test_split(test_size=0.0005, seed=2357, shuffle=True)
```

Downloads OpenWebText, creates a seeded validation split, applies ordinary GPT-2 BPE plus end-of-text per document, and writes contiguous uint16 memmaps through 1024 shards. Dataset/token counts and sizes are historical source comments. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanoGPT/data/openwebtext/prepare.py).

## Limits

Code not executed; configured checks are not passing test evidence. This source does not independently establish Karpathy personal beliefs. Raw unchanged.
