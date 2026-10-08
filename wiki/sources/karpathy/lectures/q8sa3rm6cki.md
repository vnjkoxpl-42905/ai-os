---
type: source
subject: "Karpathy video q8SA3rM6ckI"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, youtube]
sources: ["../../../../raw/sources/karpathy-brain/raw/youtube/transcripts/q8SA3rM6ckI.md"]
semantic-status: complete-preserved-text-no-media-review
---

# Building makemore Part 4: Becoming a Backprop Ninja

Original: https://www.youtube.com/watch?v=q8SA3rM6ckI. Author/channel Andrej Karpathy, except interviewer passages. Upload date is preserved in raw metadata. Captured and compiled2026-10-08. Automatic English captions. Audio accuracy not independently verified.

[Physical raw Markdown](../../../../raw/sources/karpathy-brain/raw/youtube/transcripts/q8SA3rM6ckI.md). SHA-256: `254e1c28cb39d1f2ac5b25a676015db119687a8070fb1b0ca67f6b9d9901f625`.

Physical byte hash differs from the older manifest. CRLF-to-LF normalized SHA-256 matches `178a8864b2efbf02576d99d3849a4254d75263b8985a20101bbe4c8b3f8f29f3` exactly. Raw bytes preserved.

## Reviewed evidence

He initializes biases with small random values instead of zeros to expose derivative bugs otherwise masked by a simpler expression. The redundant pre-normalization bias is retained deliberately for an exercise, not recommended as the default architecture.

> [00:07:49] ourselves and we're going to have

He recommends attempting the supplied notebook exercises before watching his answers, then checking intermediate gradients against PyTorch. The comparison distinguishes exact equality, numerical closeness and maximum absolute difference.

> [00:12:45] these derivatives or gradients yourself

He repeatedly derives tensor behavior from tiny scalar examples, beginning with the derivative of a negative mean. Shape inspection precedes each operation; broadcasting in the forward pass requires summing repeated uses in the backward pass.

> [00:14:47] so I always like to work with simpler

A value used through two graph branches cannot receive its final gradient until both contributions are accumulated. He explicitly expects incomplete gradients to fail comparison, which also checks that the comparison helper can actually detect an error.

> [00:26:57] so

Subtracting the same value from every logit leaves probabilities unchanged. The near-zero derivative through the maximum-offset branch gives an interpretive sanity check, with small floating-point residuals distinguished from a conceptual error.

> [00:36:37] these logents for any one of these

Matrix derivatives are reconstructed from a fully written two-by-two multiplication and scalar chain rules. Matching dimensions helps recover the resulting transpose operations, after the underlying pattern has been derived.

> [00:43:02] and you might think that we need to go

He discusses biased-versus-unbiased variance and objects to the batch-normalization train/test discrepancy. This is his stated preference and criticism in the lecture, not a settled proof that every standard implementation is incorrect.

> [01:07:33] 1D the documentation again is kind of

Embedding lookup backpropagation routes derivatives to the original table rows and adds repeated-index contributions. He uses a clear Python loop while acknowledging a more efficient implementation might exist.

> [01:23:33] and now what's happening is that we have

Only after deriving the atomic backward operations does he collapse cross entropy into its shorter analytic form. He checks the fused forward loss and accepts tiny non-bitwise numerical differences in backward results.

> [01:27:18] loss

He interprets cross-entropy gradients as balanced push and pull on correct versus incorrect logits; a correct one-hot prediction produces zero correction. The pulley analogy is explanatory, not a literal mechanical model.

> [01:33:52] position of the correct index has a

Batch-normalization derivation is simplified on paper, then translated to a parallel tensor formula while carefully handling indices, neurons, sums and broadcasting. The final implementation is checked against the reference gradients.

> [01:49:10] so this expression has to in parallel

He first runs a short training interval with reference gradient checks. Only after confidence is established does he remove autograd, use the manual gradients, enable no-grad execution and run full optimization with calibration and sampling.

> [01:51:41] against pytorch

The exercise exposes how backward passes work, while he still recommends production autograd in practice. Architectural expansion follows this understanding exercise rather than replacing it.

> [01:54:13] each one of these layers is like three

## Coverage and interpretation

Status: **complete-preserved-text-no-media-review**. Reviewed line ranges: 1-3152 sequentially in bounded chunks. All preserved caption text was read. Original audio/video accuracy and omitted speech were not verified.

Related: [Karpathy index](../../../karpathy/index.md), [principles](../../../karpathy/principles.md), [methods](../../../karpathy/methods.md).
