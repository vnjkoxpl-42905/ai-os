---
type: source
subject: Karpathy repository source context
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [llm-wiki, karpathy, source-context]
sources:
  - ../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk/imagernn/lstm_generator.py
---

# repos/karpathy/neuraltalk/imagernn/lstm_generator.py

Original: [captured source](https://github.com/karpathy/neuraltalk). Capture: 2026-10-08T09:35:06.538030Z. Attribution: karpathy; classification: `authored_code`.

Archived: [physical raw file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk/imagernn/lstm_generator.py). SHA-256: `40959a8e1ebf28b0ae7616c317ef0c3c2a32896ba984e6873b81f2cda513d160`.

## Source account

```text
Google paper concatenates the image to the word vectors as the first word vector
```

Manual NumPy multimodal LSTM prepends the image vector, applies sigmoid gates/candidate tanh, optional cell-output tanh, inverted encoder/decoder dropout, vocabulary decoder and explicit reverse-time gradients. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk/imagernn/lstm_generator.py).

```text
I am not very confident in this implementation
```

Inference uses greedy or cumulative-log-probability beam search, preserving completed beams and stopping at twenty steps. The source explicitly qualifies its beam handling; no search correctness or training result is established. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk/imagernn/lstm_generator.py).

## Limits

Code not executed; configured checks are not passing test evidence. This source does not independently establish Karpathy personal beliefs. Raw unchanged.
