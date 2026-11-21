---
type: source
subject: Karpathy repository source context
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [llm-wiki, karpathy, source-context]
sources:
  - ../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk/imagernn/generic_batch_generator.py
---

# repos/karpathy/neuraltalk/imagernn/generic_batch_generator.py

Original: [captured source](https://github.com/karpathy/neuraltalk). Capture: 2026-10-08T09:35:06.533022Z. Attribution: karpathy; classification: `authored_code`.

Archived: [physical raw file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk/imagernn/generic_batch_generator.py). SHA-256: `b33a82efb1ad9a2852a94b9004a0661cdca1c60007258dd0053fff26012c230e`.

## Source account

```text
we do the encoding here across all images/words in batch in single matrix
```

Separates image/word encoding from per-caption LSTM or RNN recurrence. Batched 4096-feature image projection feeds generators, while cached indices permit accumulating word-embedding and image-encoder gradients. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk/imagernn/generic_batch_generator.py).

```text
raise Exception('generator %s is not yet supported' % (base_generator_str,))
```

Unknown-generator error references undefined base_generator_str. LSTM initialization requires matching image/word encoding dimensions; source is legacy NumPy/Python 2, not executed. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk/imagernn/generic_batch_generator.py).

## Limits

Code not executed; configured checks are not passing test evidence. This source does not independently establish Karpathy personal beliefs. Raw unchanged.
