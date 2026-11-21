---
type: source
subject: Karpathy repository source context
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [llm-wiki, karpathy, source-context]
sources:
  - ../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanoGPT/config/train_gpt2.py
---

# repos/karpathy/nanoGPT/config/train_gpt2.py

Original: [captured source](https://github.com/karpathy/nanoGPT). Capture: 2026-10-08T09:35:04.204542Z. Attribution: karpathy; classification: `authored_config`.

Archived: [physical raw file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanoGPT/config/train_gpt2.py). SHA-256: `0add8a916edf704e001e87aaf63647eea9d6df964c10129ff60ad479bdbd55c4`.

## Source account

```text
12 batch size * 1024 block size * 5 gradaccum * 8 GPUs = 491,520
```

Eight-GPU GPT-2 training recipe targets roughly half a million tokens per update, 600000 iterations, external experiment logging, and 0.1 weight decay. Historical five-day/loss comments are not local runtime evidence. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanoGPT/config/train_gpt2.py).

## Limits

Code not executed; configured checks are not passing test evidence. This source does not independently establish Karpathy personal beliefs. Raw unchanged.
