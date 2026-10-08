---
type: source
subject: "GitHub source repos/karpathy/deep-vector-quantization/dvq/data/cifar10.py"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/deep-vector-quantization/dvq/data/cifar10.py]
semantic-status: complete-named-text-read
---

# repos/karpathy/deep-vector-quantization/dvq/data/cifar10.py

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/deep-vector-quantization/dvq/data/cifar10.py), SHA-256 `5ebc1e1c7aca3cefbbbe9b82b46bbe0ba613ed672c170d264bf9b271f317bb11`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "from torch.utils.data import DataLoader from torchvision import transforms as T from torchvision.datasets import CIFAR10 import".

Cryptos tests compare SHA256 with hashlib, RIPEMD with credited known vectors, Bitcoin addresses and SEC encodings with Mastering Bitcoin and Programming Bitcoin fixtures, wire-message round trips, legacy and SegWit parsing, fees, coinbase classification and height. Transaction tests deliberately tamper signatures and keys then restore them to show verification failure and recovery. Some tests require network lookup or live handshake and were not executed. Deep-vector-quantization empty initializers contain no information; CIFAR module uses randomized training crops/flips versus tensor-only validation, shuffled/drop-last pinned batches and reuses validation for test. Encoder/decoder explicitly credit DeepMind Sonnet VQVAE architecture. Loss module leaves logit-Laplace unimplemented and notes a tentative DeepMind factor-of-two discrepancy in normal reconstruction loss, so metric comparisons require normalizer awareness rather than assuming identical scales. Full text read, attribution retained.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
from torch.utils.data import DataLoader
from torchvision import transforms as T
from torchvision.datasets import CIFAR10

import pytorch_lightning as pl

class CIFAR10Data(pl.LightningDataModule):
    """ returns cifar-10 examples in floats in range [0,1] """

    def __init__(self, args):
        super().__init__()
        self.hparams = args

    def train_dataloader(self):
        transform = T.Compose(
            [
                T.RandomCrop(32, padding=4, padding_mode='reflect'),
                T.RandomHorizontalFlip(),
                T.ToTensor(),
            ]
        )
        dataset = CIFAR10(root=self.hparams.data_dir, train=True, transform=transform, download=True)
        dataloader = DataLoader(
            dataset,
            batch_size=self.hparams.batch_size,
            num_workers=self.hparams.num_workers,
            drop_last=True,
            pin_memory=True,
            shuffle=True,
        )
        return dataloader

    def val_dataloader(self):
        transform = T.Compose(
            [
                T.ToTensor(),
            ]
        )
        dataset = CIFAR10(root=self.hparams.data_dir, train=False, transform=transform, download=True)
        dataloader = DataLoader(
            dataset,
            batch_size=self.hparams.batch_size,
            num_workers=self.hparams.num_workers,
            drop_last=True,
            pin_memory=True,
        )
        return dataloader

    def test_dataloader(self):
        return self.val_dataloader()


```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
