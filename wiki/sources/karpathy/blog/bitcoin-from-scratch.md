---
type: source
subject: Bitcoin from scratch: learning versus production boundaries
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, source-compilation]
sources:
  - ../../../../raw/sources/karpathy-brain/raw/blog/md/github-blog/karpathy.github.io_2021_06_21_blockchain.md
semantic-status: compiled-text
---

# Bitcoin from scratch: learning versus production boundaries

Author: Andrej Karpathy. Published: 2021-06-21. Captured: 2026-10-08T09:34:58.574395Z.
Original: [Bitcoin from scratch: learning versus production boundaries](https://karpathy.github.io/2021/06/21/blockchain/). Complete preserved Markdown text read on 2026-10-08, including its code, tables and prose where present. This does not claim complete visual or linked-source review.

[Archived evidence](../../../../raw/sources/karpathy-brain/raw/blog/md/github-blog/karpathy.github.io_2021_06_21_blockchain.md). SHA-256: `24574bddd1427a9998c0344645ee4bcd95c82c32f08ac19fa54df3a7b641c647`.

## What this source says

Karpathy reconstructs a legacy P2PKH test-network transaction from Python data structures. The tutorial walks through elliptic-curve identities, modular arithmetic, double-and-add multiplication, handwritten SHA256 and adapted RIPEMD160, compressed keys and checksum addresses, whole-UTXO consumption with change, locking/unlocking scripts, byte-order/variable-length serialization and ECDSA signatures. He reports two broadcast transactions and explains a final consolidation across independently signed inputs. The conclusion distinguishes cryptographic primitives from serialization and compatibility complexity, excludes validation/mining implementation, and says not to roll production cryptography.

Short exact evidence from the [archived text](../../../../raw/sources/karpathy-brain/raw/blog/md/github-blog/karpathy.github.io_2021_06_21_blockchain.md):

> Please don’t use this anywhere close to anything that touches production.

## Interpretation and limits

This independently supports learning by rebuilding an end-to-end mechanism while keeping educational code out of production. The tutorial knowingly uses public reproducible test identities and unsafe signing randomness; those examples are not credentials or acceptable operational implementations. No funds were accessed, transaction broadcast, code run, or historical transaction verified here. Financial, protocol and ecosystem claims remain attributed to 2021; the notebook is a format duplicate, not independent evidence. His quoted understanding maxim is an attribution, not an original aphorism claim. The companion HTML is a format counterpart, not an independent supporting article. Statements are attributed to the captured source; no changing external capability was verified live in this compilation.

Related: [Karpathy collection](../../../karpathy/index.md) and [blog synthesis](../../../../research/karpathy-brain-2026-10-08/blog-synthesis.md).
