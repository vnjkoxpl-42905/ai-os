---
type: source
subject: "GitHub source repos/karpathy/cryptos/cryptos/curves.py"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/cryptos/cryptos/curves.py]
semantic-status: complete-named-text-read
---

# repos/karpathy/cryptos/cryptos/curves.py

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/cryptos/cryptos/curves.py), SHA-256 `4d90292572ff4e8be581f92428dbcffbd2da43d94c2b2b4dee81003d51caf3e5`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
""" Core functions for math over Elliptic Curves over Finite Fields, especially the ability to
```

Cryptos implements Bitcoin secp256k1 constants and transparent educational primitives: finite-field point addition, double-and-add scalar multiplication, public-key compression, hash160 and Base58Check addresses, DER signature encoding, double-SHA256 ECDSA and eighty-byte block headers. Curves credit Wikipedia for extended Euclid; modular inverse does not check coprimality and point operations do not validate curve membership. ECDSA explicitly leaves deterministic nonce and constant-time protection as TODOs; validation is basic, uses raw x rather than explicit modulo-n reduction and is not production cryptography. Block validation only tests proof-of-work, with target-field validation TODO; retarget caps elapsed interval and maximum target. Empty package initializer has no semantic content. Keys use OS randomness with rejection sampling and address checksum validation. Full read without running cryptographic or financial actions.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
"""
Core functions for math over Elliptic Curves over Finite Fields,
especially the ability to define Points on Curves and perform
addition and scalar multiplication.
"""

from __future__ import annotations # PEP 563: Postponed Evaluation of Annotations
from dataclasses import dataclass

# -----------------------------------------------------------------------------
# public API

__all__ = ['Curve', 'Point', 'Generator']

# -----------------------------------------------------------------------------
# Related math utilities

def extended_euclidean_algorithm(a, b):
    """
    Returns (gcd, x, y) s.t. a * x + b * y == gcd
    This function implements the extended Euclidean
    algorithm and runs in O(log b) in the worst case,
    taken from Wikipedia.
    """
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    return old_r, old_s, old_t

def inv(n, p):
    """ returns modular multiplicate inverse m s.t. (n * m) % p == 1 """
    gcd, x, y = extended_euclidean_algorithm(n, p) # pylint: disable=unused-variable
    return x % p

# -----------------------------------------------------------------------------
# Core data structures to represent curves and generators

@dataclass
class Curve:
    """
    Elliptic Curve over the field of integers modulo a prime.
    Points on the curve satisfy y^2 = x^3 + a*x + b (mod p).
    """
    p: int
    a: int
    b: int

@dataclass
class Point:
    """ An integer point (x,y) on a Curve """
    curve: Curve
    x: int
    y: int

    def __add__(self, other: Point) -> Point:
        # handle special case of P + 0 = 0 + P = 0
        if self == INF:
            return other
        if other == INF:
            return self
        # handle special case of P + (-P) = 0
        if self.x == other.x and self.y != other.y:
            return INF
        # compute the "slope"
        if self.x == other.x: # (self.y = other.y is guaranteed too per above check)
            m = (3 * self.x**2 + self.curve.a) * inv(2 * self.y, self.curve.p)
        else:
            m = (self.y - other.y) * inv(self.x - other.x, self.curve.p)
        # compute the new point
        rx = (m**2 - self.x - other.x) % self.curve.p
        ry = (-(m*(rx - self.x) + self.y)) % self.curve.p
        return Point(self.curve, rx, ry)

    def __rmul__(self, k: int) -> Point:
        assert isinstance(k, int) and k >= 0
        result = INF
        append = self
        while k:
            if k & 1:
                result += append
            append += append
            k >>= 1
        return result

@dataclass
class Generator:
    """
    A generator over a curve: an initial point and the (pre-computed) order
    """
    G: Point     # a generator point on the curve
    n: int       # the order of the generating point, so 0*G = n*G = INF

INF = Point(None, None, None)

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
