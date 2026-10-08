---
type: source
subject: "repos/karpathy/randomfun/lectures/makemore/makemore_part1_bigrams.ipynb"
created: 2026-10-08
updated: 2026-10-08
tags: [karpathy, github, source]
semantic-status: complete-authored-cell-source-and-text-output-read
---

# repos/karpathy/randomfun/lectures/makemore/makemore_part1_bigrams.ipynb

[Immutable raw notebook](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/randomfun/lectures/makemore/makemore_part1_bigrams.ipynb). SHA-256 `db2f139409bad2966baac06581b6ca8ec9a03668df50dd073577fd98b3be0045`. Manifest hash match: True. Repository ownership does not establish individual authorship.

## Reviewed content

Builds a name bigram model from explicit character-pair counts, visualized transition matrix, add-one smoothing and row normalization, then samples until the shared start/end marker. The goal connects likelihood, log likelihood and average negative log likelihood. One-hot linear logits and exponentiation recover the same transition probabilities with learned weights; explicit target-probability examples precede backward and full-dataset gradient descent with weight regularization. Saved notebook state includes exploratory mismatched displayed shapes and a one-iteration loop alongside previously trained-looking outputs, so it is not a verified linear rerun.

> GOAL: maximize likelihood

## Limits

Reviewed all 60 decoded cell sources and saved text outputs; serialized metadata and image payloads not semantically reviewed. Saved outputs are historical evidence, not a fresh execution. Embedded image pixels and notebook serialization metadata were not reviewed. No captured code executed.

## Duplicate provenance

This physical path is byte-identical to the fully reviewed notebook `repos/karpathy/nn-zero-to-hero/lectures/makemore/makemore_part1_bigrams.ipynb`. The complete decoded-content review is reused because the physical bytes are identical; this is not an independent execution or additional authored evidence.
