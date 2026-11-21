---
type: source
subject: "GitHub source repos/karpathy/cryptos/cryptos/bitcoin.py"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/cryptos/cryptos/bitcoin.py]
semantic-status: complete-named-text-read
---

# repos/karpathy/cryptos/cryptos/bitcoin.py

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/cryptos/cryptos/bitcoin.py), SHA-256 `aded07116d0031c83567ad896dc2cb33b7999ffaea345e141ac1e6ec33664219`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
""" Bitcoin-specific functions, classes, utilities and parameters """ from dataclasses import dataclass from .curves import
```

Cryptos implements Bitcoin secp256k1 constants and transparent educational primitives: finite-field point addition, double-and-add scalar multiplication, public-key compression, hash160 and Base58Check addresses, DER signature encoding, double-SHA256 ECDSA and eighty-byte block headers. Curves credit Wikipedia for extended Euclid; modular inverse does not check coprimality and point operations do not validate curve membership. ECDSA explicitly leaves deterministic nonce and constant-time protection as TODOs; validation is basic, uses raw x rather than explicit modulo-n reduction and is not production cryptography. Block validation only tests proof-of-work, with target-field validation TODO; retarget caps elapsed interval and maximum target. Empty package initializer has no semantic content. Keys use OS randomness with rejection sampling and address checksum validation. Full read without running cryptographic or financial actions.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
"""
Bitcoin-specific functions, classes, utilities and parameters
"""

from dataclasses import dataclass
from .curves import Curve, Point, Generator

# -----------------------------------------------------------------------------
# public API
__all__ = ['BITCOIN']

# -----------------------------------------------------------------------------

@dataclass
class Coin:
    gen: Generator

# -----------------------------------------------------------------------------

def bitcoin_gen():
    # Bitcoin uses secp256k1: http://www.oid-info.com/get/1.3.132.0.10
    p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
    a = 0x0000000000000000000000000000000000000000000000000000000000000000
    b = 0x0000000000000000000000000000000000000000000000000000000000000007
    Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
    Gy = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8
    n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
    curve = Curve(p, a, b)
    G = Point(curve, Gx, Gy)
    gen = Generator(G, n)
    return gen

# create an object that can be imported from other modules
BITCOIN = Coin(bitcoin_gen())

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
