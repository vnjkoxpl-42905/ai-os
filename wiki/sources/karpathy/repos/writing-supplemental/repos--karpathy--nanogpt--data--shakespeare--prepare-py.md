---
type: source
subject: Karpathy repository source context
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [llm-wiki, karpathy, source-context]
sources:
  - ../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanoGPT/data/shakespeare/prepare.py
---

# repos/karpathy/nanoGPT/data/shakespeare/prepare.py

Original: [captured source](https://github.com/karpathy/nanoGPT). Capture: 2026-10-08T09:35:04.226129Z. Attribution: karpathy; classification: `authored_code`.

Archived: [physical raw file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanoGPT/data/shakespeare/prepare.py). SHA-256: `f8d47267f00963138314bb969e75071211bf1140c248bf31b9e60e7750027f06`.

## Source account

```text
enc.encode_ordinary(train_data)
```

Downloads Tiny Shakespeare if absent, splits raw text 90/10 before ordinary GPT-2 BPE, and writes separate uint16 token streams. Requests lack explicit HTTP status/timeout checking. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanoGPT/data/shakespeare/prepare.py).

## Limits

Code not executed; configured checks are not passing test evidence. This source does not independently establish Karpathy personal beliefs. Raw unchanged.
