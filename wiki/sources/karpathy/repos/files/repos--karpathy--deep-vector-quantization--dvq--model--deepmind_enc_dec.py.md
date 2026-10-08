---
type: source
subject: "GitHub source repos/karpathy/deep-vector-quantization/dvq/model/deepmind_enc_dec.py"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/deep-vector-quantization/dvq/model/deepmind_enc_dec.py]
semantic-status: complete-named-text-read
---

# repos/karpathy/deep-vector-quantization/dvq/model/deepmind_enc_dec.py

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/deep-vector-quantization/dvq/model/deepmind_enc_dec.py), SHA-256 `005d1127185528fe6db2557a890e6ee29ace88c5e25c4b8934b181a63c7bdd79`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "\"\"\" Patch Encoders / Decoders as used by DeepMind in their sonnet repo example: https://github.com/deepmind/sonnet/blob/v2/examples/vqvae_example.ipynb".

Cryptos tests compare SHA256 with hashlib, RIPEMD with credited known vectors, Bitcoin addresses and SEC encodings with Mastering Bitcoin and Programming Bitcoin fixtures, wire-message round trips, legacy and SegWit parsing, fees, coinbase classification and height. Transaction tests deliberately tamper signatures and keys then restore them to show verification failure and recovery. Some tests require network lookup or live handshake and were not executed. Deep-vector-quantization empty initializers contain no information; CIFAR module uses randomized training crops/flips versus tensor-only validation, shuffled/drop-last pinned batches and reuses validation for test. Encoder/decoder explicitly credit DeepMind Sonnet VQVAE architecture. Loss module leaves logit-Laplace unimplemented and notes a tentative DeepMind factor-of-two discrepancy in normal reconstruction loss, so metric comparisons require normalizer awareness rather than assuming identical scales. Full text read, attribution retained.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
"""
Patch Encoders / Decoders as used by DeepMind in their sonnet repo example:
https://github.com/deepmind/sonnet/blob/v2/examples/vqvae_example.ipynb
"""

import torch
from torch import nn, einsum
import torch.nn.functional as F

# -----------------------------------------------------------------------------

class ResBlock(nn.Module):
    def __init__(self, input_channels, channel):
        super().__init__()

        self.conv = nn.Sequential(
            nn.Conv2d(input_channels, channel, 3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(channel, input_channels, 1),
        )

    def forward(self, x):
        out = self.conv(x)
        out += x
        out = F.relu(out)
        return out


class DeepMindEncoder(nn.Module):

    def __init__(self, input_channels=3, n_hid=64):
        super().__init__()

        self.net = nn.Sequential(
            nn.Conv2d(input_channels, n_hid, 4, stride=2, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(n_hid, 2*n_hid, 4, stride=2, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(2*n_hid, 2*n_hid, 3, padding=1),
            nn.ReLU(),
            ResBlock(2*n_hid, 2*n_hid//4),
            ResBlock(2*n_hid, 2*n_hid//4),
        )

        self.output_channels = 2 * n_hid
        self.output_stide = 4

    def forward(self, x):
        return self.net(x)


class DeepMindDecoder(nn.Module):

    def __init__(self, n_init=32, n_hid=64, output_channels=3):
        super().__init__()

        self.net = nn.Sequential(
            nn.Conv2d(n_init, 2*n_hid, 3, padding=1),
            nn.ReLU(),
            ResBlock(2*n_hid, 2*n_hid//4),
            ResBlock(2*n_hid, 2*n_hid//4),
            nn.ConvTranspose2d(2*n_hid, n_hid, 4, stride=2, padding=1),
            nn.ReLU(inplace=True),
            nn.ConvTranspose2d(n_hid, output_channels, 4, stride=2, padding=1),
        )

    def forward(self, x):
        return self.net(x)

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
