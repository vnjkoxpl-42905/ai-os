---
type: source
subject: Karpathy repository source context
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [llm-wiki, karpathy, source-context]
sources:
  - ../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanoGPT/train.py
---

# repos/karpathy/nanoGPT/train.py

Original: [captured source](https://github.com/karpathy/nanoGPT). Capture: 2026-10-08T09:35:04.154472Z. Attribution: karpathy; classification: `authored_code`.

Archived: [physical raw file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanoGPT/train.py). SHA-256: `413bd97b40bb400a2a0d01230e2946f056c263ebac1b7281c2367d964a123085`.

## Source account

```text
in DDP training we only need to sync gradients at the last micro step.
```

Training supports single GPU/DDP, rank-scaled accumulation, memmapped random next-token batches, scratch/resume/pretrained initialization, mixed precision, optional compilation, evaluation and validation checkpoints. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanoGPT/train.py).

```text
approximating the true total loss (exact would have been a sum)
```

Logged loss approximates accumulation from the last microbatch. Checkpoints preserve model/optimizer/config/iteration but omit RNG, loader and GradScaler state, so resumed execution is not established as bit-identical. Evaluation is rank-zero rather than globally aggregated. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanoGPT/train.py).

## Limits

Code not executed; configured checks are not passing test evidence. This source does not independently establish Karpathy personal beliefs. Raw unchanged.
