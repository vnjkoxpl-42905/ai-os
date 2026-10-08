---
type: source
subject: "GitHub source repos/karpathy/cryptos/getnewaddress.py"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/cryptos/getnewaddress.py]
semantic-status: complete-named-text-read
---

# repos/karpathy/cryptos/getnewaddress.py

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/cryptos/getnewaddress.py), SHA-256 `19b1bb755e28ffa6207f12193999410400bc8ce6164bb9bb392fe9990ed6c42c`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "\"\"\" A cli tool that generates and prints a new Bitcoin address. Specifically, the tool".

Transaction source decomposes variable integers, lazy cached Blockstream retrieval with calculated transaction-ID verification, legacy and SegWit decoding/encoding, inputs/outputs and locking/unlocking scripts. Disk caching explicitly avoids stressing the API provider. Validation rejects SegWit support and implements only standard P2PKH with SIGHASH_ALL, not a general script interpreter; seventy-five-byte script pushes fall through encoder ranges. The new-address CLI prints secret keys and must not be executed or adopted as a secure workflow. Tests check block decode/encode/id/difficulty, tampered proof-of-work, retarget and genesis constants, plus signature rejection/acceptance through an accessible adversarial narrative and DER round trips credited to Programming Bitcoin. Empty tests initializer has no content. Tests were read only; no API calls, key generation or payment action performed.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
"""
A cli tool that generates and prints a new Bitcoin address.
Specifically, the tool prints:
- a new secret key
- the associated public key
- the bitcoin address
"""

from cryptos.keys import gen_secret_key, PublicKey
from cryptos.bitcoin import BITCOIN

if __name__ == '__main__':

    # generate a secret/public key pair
[REDACTED CREDENTIAL]
    public_key = PublicKey.from_sk(secret_key)
    print('generated secret key:')
    print(hex(secret_key))
    print('corresponding public key:')
    print('x:', format(public_key.x, '064x').upper())
    print('y:', format(public_key.y, '064x').upper())

    # get the associated bitcoin address
    addr = public_key.address(net='main', compressed=True)
    print('compressed bitcoin address (b58check format):')
    print(addr)

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
