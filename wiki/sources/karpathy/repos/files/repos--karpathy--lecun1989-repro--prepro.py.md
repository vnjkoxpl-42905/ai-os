---
type: source
subject: "GitHub source repos/karpathy/lecun1989-repro/prepro.py"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/lecun1989-repro/prepro.py]
semantic-status: complete-named-text-read
---

# repos/karpathy/lecun1989-repro/prepro.py

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/lecun1989-repro/prepro.py), SHA-256 `db6fd6fcd677c704d38c987c41c16e352f88af8e3e675f6341d361c488fc24a5`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
""" Preprocess today's MNIST dataset into 1989 version's size/format (approximately) http://yann.lecun.com/exdb/publis/pdf/lecun-89e.pdf Some relevant notes for
```

All three LeCun reproduction scripts fully read. Prepro downsamples seeded MNIST to 16x16 normalized minus1-to1 and samples7291 train2007 test with plus1/minus1 labels, explicitly approximate historical data. Repro explicit sparse overlapping H2 connections, shape/parameter-count assertions, target-biased output initialization, single-example SGD23epochs, deterministic seeds, fullsplit eval and saved args/model. Modern retains size while uses ReLU, training-only one-pixel torch.roll shifts, dropout, logits crossentropy, AdamW decayed LR80epochs; notes coupled changes and historical metrics. Critical modern.eval_split computes loss using stale lowercase yhat/y from last training example rather than current uppercase Yhat/Y, explaining identical reported train/test losses, while error uses correct split tensors. Outputs are source reports not rerun validation; never copy that evaluation bug into new methods.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
"""
Preprocess today's MNIST dataset into 1989 version's size/format (approximately)
http://yann.lecun.com/exdb/publis/pdf/lecun-89e.pdf

Some relevant notes for this part:
- 7291 digits are used for training
- 2007 digits are used for testing
- each image is 16x16 pixels grayscale (not binary)
- images are scaled to range [-1, 1]
- paper doesn't say exactly, but reading between the lines I assume label targets to be {-1, 1}
"""

import numpy as np
import torch
import torch.nn.functional as F
from torchvision import datasets

# -----------------------------------------------------------------------------

torch.manual_seed(1337)
np.random.seed(1337)

for split in {'train', 'test'}:

    data = datasets.MNIST('./data', train=split=='train', download=True)

    n = 7291 if split == 'train' else 2007
    rp = np.random.permutation(len(data))[:n]

    X = torch.full((n, 1, 16, 16), 0.0, dtype=torch.float32)
    Y = torch.full((n, 10), -1.0, dtype=torch.float32)
    for i, ix in enumerate(rp):
        I, yint = data[int(ix)]
        # PIL image -> numpy -> torch tensor -> [-1, 1] fp32
        xi = torch.from_numpy(np.array(I, dtype=np.float32)) / 127.5 - 1.0
        # add a fake batch dimension and a channel dimension of 1 or F.interpolate won't be happy
        xi = xi[None, None, ...]
        # resize to (16, 16) images with bilinear interpolation
        xi = F.interpolate(xi, (16, 16), mode='bilinear')
        X[i] = xi[0] # store

        # set the correct class to have target of +1.0
        Y[i, yint] = 1.0

    torch.save((X, Y), split + '1989.pt')

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
