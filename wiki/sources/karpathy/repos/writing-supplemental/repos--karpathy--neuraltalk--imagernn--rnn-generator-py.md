---
type: source
subject: Karpathy repository source context
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [llm-wiki, karpathy, source-context]
sources:
  - ../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk/imagernn/rnn_generator.py
---

# repos/karpathy/neuraltalk/imagernn/rnn_generator.py

Original: [captured source](https://github.com/karpathy/neuraltalk). Capture: 2026-10-08T09:35:06.543553Z. Attribution: karpathy; classification: `authored_code`.

Archived: [physical raw file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk/imagernn/rnn_generator.py). SHA-256: `dbe0d374acfac23c6149befaeef792e23dfef642f51af5f6b6eee946ececf8e8`.

## Source account

```text
a sequence of input vectors, and produces a sequence of output vectors
```

Manual ReLU recurrent caption generator combines image, encoded words and recurrent state, optionally injecting the image only at the first step. It implements inverted dropout and explicit reverse-time gradients. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk/imagernn/rnn_generator.py).

```text
ideally the beam search would be abstracted away nicely
```

Inference duplicates LSTM beam-search structure with greedy or twenty-step beam decoding. The image encoding must be compatible with hidden width; this is historical code, not a current production recipe. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk/imagernn/rnn_generator.py).

## Limits

Code not executed; configured checks are not passing test evidence. This source does not independently establish Karpathy personal beliefs. Raw unchanged.
