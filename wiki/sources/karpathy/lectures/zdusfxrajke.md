---
type: source
subject: "Karpathy video zduSFxRajkE"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, youtube]
sources: ["../../../../raw/sources/karpathy-brain/raw/youtube/transcripts/zduSFxRajkE.md"]
semantic-status: complete-preserved-text-no-media-review
---

# Let's build the GPT Tokenizer

Original: https://www.youtube.com/watch?v=zduSFxRajkE. Author/channel Andrej Karpathy, except interviewer passages. Upload date is preserved in raw metadata. Captured and compiled2026-10-08. Automatic English captions. Audio accuracy not independently verified.

[Physical raw Markdown](../../../../raw/sources/karpathy-brain/raw/youtube/transcripts/zduSFxRajkE.md). SHA-256: `b26c7f9c389350834dd6d764050164546c7331b5be54cfdb2645f62d58d63dbb`.

Physical byte hash differs from the older manifest. CRLF-to-LF normalized SHA-256 matches `f204d9f7630627627e7b1b4a82d6ccfacd5de313008b05080e4bae65ec174133` exactly. Raw bytes preserved.

## Reviewed evidence

The reviewed sequential core builds BPE from a tiny symbolic sequence through UTF-8 bytes, counts, merging, training, decoding and encoding. It checks predicted length changes, exposes invalid UTF-8 using token128, uses replacement decoding, fixes empty/single-token input, and verifies text round trips on training and unseen text. Encoding uses learned merge rank rather than current frequency. Tokenizer training is separate from LLM training. These demonstrations have not been locally reproduced.

> [00:28:29] try to write that function yourself

> [00:55:56] try to encode it and then decode it back

> [00:55:58] you'd expect to get the same string back


## The full lecture extends the basic tokenizer carefully

The opening demonstrates how spaces, uppercase/lowercase, numbers, Korean text and Python indentation produce different token sequences. It connects representation density to usable context length. These are dated demonstrations from the2024 recording, not current product benchmarks. Unicode code points differ from byte encodings; raw UTF-8 bytes support arbitrary text but produce long sequences, motivating compression. Tokenization-free architectures are presented as a research hope, not a solved production replacement.

After basic BPE, the lecture introduces regex chunk boundaries to prevent undesired cross-category merges. It shows contraction/case and Unicode-apostrophe quirks, and admits uncertainty about unreleased GPT-2 tokenizer training rules. The released inference code and tiktoken are distinguished from training code. Special tokens provide document or conversation structure outside ordinary BPE; adding them requires corresponding embedding/output changes in a model.

The minbpe exercise progresses in stages toward reference-compatible encoding, decoding and training. SentencePiece is contrasted with byte-level BPE: merging code points, byte fallback for unseen characters, optional normalization, dummy prefixes, and many configuration choices. The demonstration toggles byte fallback off to show unknown-token collapse. His preference for preserving raw text is contextual to language modeling rather than a mandate to skip all data validation.

Vocabulary size trades shorter sequences against bigger embedding/output matrices, compute cost and rare-token undertraining. Prompt compression with learned gist tokens and multimodal token representations are described as separate research directions. These do not mean ordinary text prompts can create trained special tokens without model changes.

The closing demonstrations revisit spelling/reversal, non-English density, arithmetic segmentation, indentation, special-token handling and incomplete token prefixes. The SolidGoldMagikarp explanation is explicitly a hypothesis about mismatched tokenizer/model training distributions, not a definitively established account. His format-efficiency comparison is an example rather than a universal guarantee that YAML is always smaller or preferable. Measure the actual representation instead. The final library recommendations reflect the recording date and have not been verified as current recommendations.

## Coverage and interpretation

Status: **complete-preserved-text-no-media-review**. All3506 preserved lines were read sequentially, including metadata and final outtakes. Truncated tool-output gaps were explicitly reread. Audio, video frames, linked code and external documentation remain unreviewed. Hashing and indexing do not establish full semantic understanding. Caption errors are preserved. No linked code, papers, diagrams or media was independently executed or inspected. Host introductions are not Karpathy quotations. Mirror timings do not certify every spoken word.

Related: [Karpathy index](../../../karpathy/index.md), [principles](../../../karpathy/principles.md), [methods](../../../karpathy/methods.md).
