---
type: source
subject: "GitHub source repos/karpathy/deep-vector-quantization/dvq/model/loss.py"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/deep-vector-quantization/dvq/model/loss.py]
semantic-status: complete-named-text-read
---

# repos/karpathy/deep-vector-quantization/dvq/model/loss.py

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/deep-vector-quantization/dvq/model/loss.py), SHA-256 `49b4d2cf4aa22f32ab5091cd5f9471f51afc8dd48c8e4c93c419aec2cde3bd49`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "\"\"\" VQVAE losses, used for the reconstruction term in the ELBO \"\"\" import math import".

Cryptos tests compare SHA256 with hashlib, RIPEMD with credited known vectors, Bitcoin addresses and SEC encodings with Mastering Bitcoin and Programming Bitcoin fixtures, wire-message round trips, legacy and SegWit parsing, fees, coinbase classification and height. Transaction tests deliberately tamper signatures and keys then restore them to show verification failure and recovery. Some tests require network lookup or live handshake and were not executed. Deep-vector-quantization empty initializers contain no information; CIFAR module uses randomized training crops/flips versus tensor-only validation, shuffled/drop-last pinned batches and reuses validation for test. Encoder/decoder explicitly credit DeepMind Sonnet VQVAE architecture. Loss module leaves logit-Laplace unimplemented and notes a tentative DeepMind factor-of-two discrepancy in normal reconstruction loss, so metric comparisons require normalizer awareness rather than assuming identical scales. Full text read, attribution retained.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
"""
VQVAE losses, used for the reconstruction term in the ELBO
"""

import math
import torch

# -----------------------------------------------------------------------------

class LogitLaplace:
    """ the Logit Laplace distribution log likelihood from OpenAI's DALL-E paper """
    logit_laplace_eps = 0.1

    @classmethod
    def inmap(cls, x):
        # map [0,1] range to [eps, 1-eps]
        return (1 - 2 * cls.logit_laplace_eps) * x + cls.logit_laplace_eps

    @classmethod
    def unmap(cls, x):
        # inverse map, from [eps, 1-eps] to [0,1], with clamping
        return torch.clamp((x - cls.logit_laplace_eps) / (1 - 2 * cls.logit_laplace_eps), 0, 1)

    @classmethod
    def nll(cls, x, mu_logb):
        raise NotImplementedError # coming right up


class Normal:
    """
    simple normal distribution with fixed variance, as used by DeepMind in their VQVAE
    note that DeepMind's reconstruction loss (I think incorrectly?) misses a factor of 2,
    which I have added to the normalizer of the reconstruction loss in nll(), we'll report
    number that is half of what we expect in their jupyter notebook
    """
    data_variance = 0.06327039811675479 # cifar-10 data variance, from deepmind sonnet code

    @classmethod
    def inmap(cls, x):
        return x - 0.5 # map [0,1] range to [-0.5, 0.5]

    @classmethod
    def unmap(cls, x):
        return torch.clamp(x + 0.5, 0, 1)

    @classmethod
    def nll(cls, x, mu):
        return ((x - mu)**2).mean() / (2 * cls.data_variance) #+ math.log(math.sqrt(2 * math.pi * cls.data_variance))

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
