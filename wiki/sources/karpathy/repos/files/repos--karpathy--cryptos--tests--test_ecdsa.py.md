---
type: source
subject: "GitHub source repos/karpathy/cryptos/tests/test_ecdsa.py"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/cryptos/tests/test_ecdsa.py]
semantic-status: complete-named-text-read
---

# repos/karpathy/cryptos/tests/test_ecdsa.py

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/cryptos/tests/test_ecdsa.py), SHA-256 `db90e610a235e30e02f57120f1e79624557f383bdc20d50cbc0c369e7a2a59c3`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
""" Test our ability to sign and verify digital signatures """ import os from io
```

Transaction source decomposes variable integers, lazy cached Blockstream retrieval with calculated transaction-ID verification, legacy and SegWit decoding/encoding, inputs/outputs and locking/unlocking scripts. Disk caching explicitly avoids stressing the API provider. Validation rejects SegWit support and implements only standard P2PKH with SIGHASH_ALL, not a general script interpreter; seventy-five-byte script pushes fall through encoder ranges. The new-address CLI prints secret keys and must not be executed or adopted as a secure workflow. Tests check block decode/encode/id/difficulty, tampered proof-of-work, retarget and genesis constants, plus signature rejection/acceptance through an accessible adversarial narrative and DER round trips credited to Programming Bitcoin. Empty tests initializer has no content. Tests were read only; no API calls, key generation or payment action performed.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
"""
Test our ability to sign and verify digital signatures
"""

import os
from io import BytesIO

from cryptos.bitcoin import BITCOIN
from cryptos.keys import gen_key_pair
from cryptos.ecdsa import Signature, sign, verify
from cryptos.transaction import Tx

def test_ecdsa():

    # let's create two identities
    sk1, pk1 = gen_key_pair()
    sk2, pk2 = gen_key_pair() # pylint: disable=unused-variable

    message = ('user pk1 would like to pay user pk2 1 BTC kkthx').encode('ascii')

    # an evil user2 attempts to submit the transaction to the network with some totally random signature
    sig = Signature(int.from_bytes(os.urandom(32), 'big'), int.from_bytes(os.urandom(32), 'big'))
    # a few seconds later a hero miner inspects the candidate transaction
    is_legit = verify(pk1, message, sig)
    assert not is_legit
    # unlike user2, hero miner is honest and discards the transaction, all is well

    # evil user2 does not give up and tries to sign with his key pair
    sig = sign(sk2, message)
    is_legit = verify(pk1, message, sig)
    assert not is_legit
    # denied, again!

    # lucky for user2, user1 feels sorry for them and the hardships they have been through recently
    sig = sign(sk1, message)
    is_legit = verify(pk1, message, sig)
    assert is_legit
    # hero miner validates the transaction and adds it to their block
    # user2 happy, buys a Tesla, and promises to turn things around

    # the end.

def test_sig_der():

    # a transaction used as an example in programming bitcoin
    raw = bytes.fromhex('0100000001813f79011acb80925dfe69b3def355fe914bd1d96a3f5f71bf8303c6a989c7d1000000006b483045022100ed81ff192e75a3fd2304004dcadb746fa5e24c5031ccfcf21320b0277457c98f02207a986d955c6e0cb35d446a89d3f56100f4d7f67801c31967743a9c8e10615bed01210349fc4e631e3624a545de3f89f5d8684c7b8138bd94bdd531d2e213bf016b278afeffffff02a135ef01000000001976a914bc3b654dca7e56b04dca18f2566cdaf02e8d9ada88ac99c39800000000001976a9141c4bc762dd5423e332166702cb75f40df79fea1288ac19430600')
    tx = Tx.decode(BytesIO(raw))
    der = tx.tx_ins[0].script_sig.cmds[0][:-1] # this is the DER signature of the first input on this tx. :-1 crops out the sighash-type byte
    sig = Signature.decode(der) # making sure no asserts get tripped up inside this call

    # from programming bitcoin chapter 4
    der = bytes.fromhex('3045022037206a0610995c58074999cb9767b87af4c4978db68c06e8e6e81d282047a7c60221008ca63759c1157ebeaec0d03cecca119fc9a75bf8e6d0fa65c841c8e2738cdaec')
    sig = Signature.decode(der)
    assert sig.r == 0x37206a0610995c58074999cb9767b87af4c4978db68c06e8e6e81d282047a7c6
    assert sig.s == 0x8ca63759c1157ebeaec0d03cecca119fc9a75bf8e6d0fa65c841c8e2738cdaec

    # test that we can also recover back the same der encoding
    der2 = sig.encode()
    assert der == der2

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
