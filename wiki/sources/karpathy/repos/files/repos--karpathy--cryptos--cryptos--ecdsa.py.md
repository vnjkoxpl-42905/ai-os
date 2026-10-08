---
type: source
subject: "GitHub source repos/karpathy/cryptos/cryptos/ecdsa.py"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/cryptos/cryptos/ecdsa.py]
semantic-status: complete-named-text-read
---

# repos/karpathy/cryptos/cryptos/ecdsa.py

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/cryptos/cryptos/ecdsa.py), SHA-256 `0267e189182fb97d64ede742095429c608dd7feb6b453f0e854efc1d8ef62fd6`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
""" Elliptic Curve Digital Signature Algorithm (ECDSA) Functions that sign/verify digital signatures and related utilities
```

Cryptos implements Bitcoin secp256k1 constants and transparent educational primitives: finite-field point addition, double-and-add scalar multiplication, public-key compression, hash160 and Base58Check addresses, DER signature encoding, double-SHA256 ECDSA and eighty-byte block headers. Curves credit Wikipedia for extended Euclid; modular inverse does not check coprimality and point operations do not validate curve membership. ECDSA explicitly leaves deterministic nonce and constant-time protection as TODOs; validation is basic, uses raw x rather than explicit modulo-n reduction and is not production cryptography. Block validation only tests proof-of-work, with target-field validation TODO; retarget caps elapsed interval and maximum target. Empty package initializer has no semantic content. Keys use OS randomness with rejection sampling and address checksum validation. Full read without running cryptographic or financial actions.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
"""
Elliptic Curve Digital Signature Algorithm (ECDSA)
Functions that sign/verify digital signatures and related utilities
"""

from dataclasses import dataclass
from io import BytesIO

from .sha256 import sha256
from cryptos.bitcoin import BITCOIN
from cryptos.curves import inv, Point
from cryptos.keys import gen_secret_key, PublicKey
# -----------------------------------------------------------------------------

@dataclass
class Signature:
    r: int
    s: int

    @classmethod
    def decode(cls, der: bytes):
        """
        According to https://en.bitcoin.it/wiki/BIP_0062#DER_encoding DER has the following format:
        0x30 [total-length] 0x02 [R-length] [R] 0x02 [S-length] [S] [sighash-type]

        total-length: 1-byte length descriptor of everything that follows, excluding the sighash byte.
        R-length: 1-byte length descriptor of the R value that follows.
        R: arbitrary-length big-endian encoded R value. It cannot start with any 0x00 bytes, unless the first byte that follows is 0x80 or higher, in which case a single 0x00 is required.
        S-length: 1-byte length descriptor of the S value that follows.
        S: arbitrary-length big-endian encoded S value. The same rules apply as for R.
        sighash-type: 1-byte hashtype flag (only 0x01, 0x02, 0x03, 0x81, 0x82 and 0x83 are allowed).

        NOTE: the sighash type is just appended at the end of the DER signature at the end in
        Bitcoin transactions, and isn't actually part of the DER signature. Here we already assume
        it has been cropped out.
        """
        s = BytesIO(der)
        assert s.read(1)[0] == 0x30
        # read and validate the total length of the encoding
        length = s.read(1)[0]
        assert length == len(der) - 2 # -2 to exclude 1) the starting 0x30, 2) total-length byte
        assert s.read(1)[0] == 0x02
        # read r
        rlength = s.read(1)[0]
        rval = int.from_bytes(s.read(rlength), 'big')
        assert s.read(1)[0] == 0x02
        # read s
        slength = s.read(1)[0]
        sval = int.from_bytes(s.read(slength), 'big')
        # validate total length and return
        assert len(der) == 6 + rlength + slength # 6 is the sum of misc / metadata bytes in the DER signature
        return cls(rval, sval)

    def encode(self) -> bytes:
        """ return the DER encoding of this signature """

        def dern(n):
            nb = n.to_bytes(32, byteorder='big')
            nb = nb.lstrip(b'\x00') # strip leading zeros
            nb = (b'\x00' if nb[0] >= 0x80 else b'') + nb # preprend 0x00 if first byte >= 0x80
            return nb

        rb = dern(self.r)
        sb = dern(self.s)
        content = b''.join([bytes([0x02, len(rb)]), rb, bytes([0x02, len(sb)]), sb])
        frame = b''.join([bytes([0x30, len(content)]), content])
        return frame

def sign(secret_key: int, message: bytes) -> Signature:

    n = BITCOIN.gen.n

    # hash the message and convert to integer
    # TODO: do we want to do this here? or outside? probably not here
    z = int.from_bytes(sha256(sha256(message)), 'big')

    # generate a new secret/public key pair at random
    # TODO: make deterministic
    # TODO: make take constant time to mitigate timing attacks
    k = gen_secret_key(n)
    P = PublicKey.from_sk(k)

    # calculate the signature
    r = P.x
    s = inv(k, n) * (z + secret_key * r) % n
    if s > n / 2:
        s = n - s

    sig = Signature(r, s)
    return sig

def verify(public_key: Point, message: bytes, sig: Signature) -> bool:

    n = BITCOIN.gen.n

    # some super basic verification
    assert isinstance(sig.r, int) and 1 <= sig.r < n
    assert isinstance(sig.s, int) and 1 <= sig.s < n

    # hash the message and convert to integer
    z = int.from_bytes(sha256(sha256(message)), 'big')

    # verify signature
    w = inv(sig.s, n)
    u1 = z * w % n
    u2 = sig.r * w % n
    P = (u1 * BITCOIN.gen.G) + (u2 * public_key)
    match = P.x == sig.r

    return match


```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
