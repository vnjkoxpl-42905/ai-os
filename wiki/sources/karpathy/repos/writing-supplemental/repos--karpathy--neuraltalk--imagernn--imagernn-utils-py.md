---
type: source
subject: Karpathy repository source context
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [llm-wiki, karpathy, source-context]
sources:
  - ../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk/imagernn/imagernn_utils.py
---

# repos/karpathy/neuraltalk/imagernn/imagernn_utils.py

Original: [captured source](https://github.com/karpathy/neuraltalk). Capture: 2026-10-08T09:35:06.535031Z. Attribution: karpathy; classification: `authored_code`.

Archived: [physical raw file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk/imagernn/imagernn_utils.py). SHA-256: `0cd7e9c7f9159abafaa587518745813d100175f3796364cca90fd6d33b33194a`.

## Source account

```text
for numerical stability shift into good numerical range
```

Dispatches to the generic generator and evaluates caption perplexity in batches using shifted softmax probabilities and base-two log likelihood, excluding out-of-vocabulary words and adding END tokens. Empty evaluation splits would leave a zero denominator. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk/imagernn/imagernn_utils.py).

## Limits

Code not executed; configured checks are not passing test evidence. This source does not independently establish Karpathy personal beliefs. Raw unchanged.
