---
type: source
subject: "GitHub source repos/karpathy/cryptos/tests/test_hash.py"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/cryptos/tests/test_hash.py]
semantic-status: complete-named-text-read
---

# repos/karpathy/cryptos/tests/test_hash.py

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/cryptos/tests/test_hash.py), SHA-256 `0efbf77467b1cf8652eb3acfe868781c0141b7d4aa44ce7a38fd422666ee0941`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "import hashlib from cryptos.sha256 import sha256 from cryptos.ripemd160 import ripemd160 def test_sha256(): test_bytes = \\[".

Cryptos tests compare SHA256 with hashlib, RIPEMD with credited known vectors, Bitcoin addresses and SEC encodings with Mastering Bitcoin and Programming Bitcoin fixtures, wire-message round trips, legacy and SegWit parsing, fees, coinbase classification and height. Transaction tests deliberately tamper signatures and keys then restore them to show verification failure and recovery. Some tests require network lookup or live handshake and were not executed. Deep-vector-quantization empty initializers contain no information; CIFAR module uses randomized training crops/flips versus tensor-only validation, shuffled/drop-last pinned batches and reuses validation for test. Encoder/decoder explicitly credit DeepMind Sonnet VQVAE architecture. Loss module leaves logit-Laplace unimplemented and notes a tentative DeepMind factor-of-two discrepancy in normal reconstruction loss, so metric comparisons require normalizer awareness rather than assuming identical scales. Full text read, attribution retained.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
import hashlib
from cryptos.sha256 import sha256
from cryptos.ripemd160 import ripemd160

def test_sha256():

    test_bytes = [
        b'',
        b'abc', # as seen in NIST docs
        b'hello',
        b'a longer message to make sure that a larger number of blocks works okay too'*15
    ]

    for b in test_bytes:
        gt = hashlib.sha256(b).hexdigest()
        yolo = sha256(b).hex()
        assert gt == yolo

def test_ripemd160():

    # taken from the ripemd160 docs
    # https://homes.esat.kuleuven.be/~bosselae/ripemd160/pdf/AB-9601/AB-9601.pdf
    test_pairs = [
        ('', '9c1185a5c5e9fc54612808977ee8f548b2258d31'),
        ('a', '0bdc9d2d256b3ee9daae347be6f4dc835a467ffe'),
        ('abc', '8eb208f7e05d987a9b044a8e98c6b087f15a0bfc'),
        ('message digest', '5d0689ef49d2fae572b881b123a85ffa21595f36'),
        ('1234567890'*8, '9b752e45573d4b39f4dbd3323cab82bf63326bfb'),
        # ('a'*1000000, '52783243c1697bdbe16d37f97f68f08325dc1528'), # can take a while to compute
        ('a'*1000, 'aa69deee9a8922e92f8105e007f76110f381e9cf'), # I made this shorter one up instead
    ]

    for b, gt in test_pairs:
        yolo = ripemd160(b.encode('ascii')).hex()
        assert gt == yolo

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
