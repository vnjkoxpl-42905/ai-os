---
type: source
subject: "Karpathy video zduSFxRajkE"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, youtube]
sources: ["../../../../raw/sources/karpathy-brain/raw/youtube/transcripts/zduSFxRajkE.md"]
semantic-status: bounded-semantic-review
---

# Let's build the GPT Tokenizer

Original: https://www.youtube.com/watch?v=zduSFxRajkE. Author/channel Andrej Karpathy, except interviewer passages. Upload date is preserved in raw metadata. Captured and compiled2026-10-08. Automatic English captions. Audio accuracy not independently verified.

[Physical raw Markdown](../../../../raw/sources/karpathy-brain/raw/youtube/transcripts/zduSFxRajkE.md). SHA-256: `b26c7f9c389350834dd6d764050164546c7331b5be54cfdb2645f62d58d63dbb`.

## Reviewed evidence

The reviewed sequential core builds BPE from a tiny symbolic sequence through UTF-8 bytes, counts, merging, training, decoding and encoding. It checks predicted length changes, exposes invalid UTF-8 using token128, uses replacement decoding, fixes empty/single-token input, and verifies text round trips on training and unseen text. Encoding uses learned merge rank rather than current frequency. Tokenizer training is separate from LLM training. These demonstrations have not been locally reproduced.

> [00:28:29] try to write that function yourself

> [00:55:56] try to encode it and then decode it back

> [00:55:58] you'd expect to get the same string back

## Coverage and interpretation

Status: **bounded-semantic-review**. Reviewed lines 1-159, 694-1529. Remaining sections are unreviewed. Hashing and indexing do not establish full semantic understanding. Caption errors are preserved. No linked code, papers, diagrams or media was independently executed or inspected. Host introductions are not Karpathy quotations. Mirror timings do not certify every spoken word.

Related: [Karpathy index](../../../karpathy/index.md), [principles](../../../karpathy/principles.md), [methods](../../../karpathy/methods.md).
