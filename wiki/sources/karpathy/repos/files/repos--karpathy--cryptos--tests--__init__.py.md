---
type: source
subject: "GitHub source repos/karpathy/cryptos/tests/__init__.py"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/cryptos/tests/__init__.py]
semantic-status: complete-named-text-read
---

# repos/karpathy/cryptos/tests/__init__.py

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/cryptos/tests/__init__.py), SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "".

Transaction source decomposes variable integers, lazy cached Blockstream retrieval with calculated transaction-ID verification, legacy and SegWit decoding/encoding, inputs/outputs and locking/unlocking scripts. Disk caching explicitly avoids stressing the API provider. Validation rejects SegWit support and implements only standard P2PKH with SIGHASH_ALL, not a general script interpreter; seventy-five-byte script pushes fall through encoder ranges. The new-address CLI prints secret keys and must not be executed or adopted as a secure workflow. Tests check block decode/encode/id/difficulty, tampered proof-of-work, retarget and genesis constants, plus signature rejection/acceptance through an accessible adversarial narrative and DER round trips credited to Programming Bitcoin. Empty tests initializer has no content. Tests were read only; no API calls, key generation or payment action performed.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
