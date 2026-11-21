---
type: source
subject: "Karpathy video t3YJ5hKiMQ0"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, youtube]
sources: ["../../../../raw/sources/karpathy-brain/raw/youtube/transcripts/t3YJ5hKiMQ0.md"]
semantic-status: complete-preserved-text-no-media-review
---

# Building makemore Part 5: Building a WaveNet

Original: https://www.youtube.com/watch?v=t3YJ5hKiMQ0. Author/channel Andrej Karpathy. Upload date is preserved in raw metadata. Captured and compiled 2026-10-08. Automatic English captions. Audio accuracy not independently verified.

[Physical raw Markdown](../../../../raw/sources/karpathy-brain/raw/youtube/transcripts/t3YJ5hKiMQ0.md). SHA-256: `5d6450c1b3279add0d84a77034f521fab185582b641ee165ddadf86914edc38e`.

Physical byte hash differs from the older manifest. CRLF-to-LF normalized SHA-256 matches `fa9e915139f3cd0bdd131efdefabec0f8662d2a1026081d37cd28a521de78b39` exactly. Raw bytes preserved.

## Reviewed evidence

The opening expands prior MLP context and uses deeper hierarchical fusion to motivate a WaveNet-like model; starter code reuses prior work.

## Full preserved-text compilation

At 00:02-00:06, modules are composable building blocks with deliberately similar PyTorch interfaces. BatchNorm brings state, running statistics, train/eval modes and coupling between examples, creating correctness hazards beyond a pure forward function. The initial model gives validation loss around 2.10, with generated names inspected as qualitative evidence.

At 00:07-00:15, averaged groups of loss values make a noisy training curve easier to read. Embedding and flatten operations become layers, then a Sequential container eliminates scattered special cases. After refactoring, the first training iteration is run before proceeding. Sampling exposes a train/eval state error: the changed cell had not been run, so BatchNorm still used batch statistics on a single example. Executing the state change fixes it. Merely editing a notebook cell does not execute its effect.

At 00:17-00:21, increasing context from three to eight characters improves the flat baseline to roughly 2.02. A hierarchical model should fuse consecutive pairs progressively rather than compress all characters immediately. This is a proposed architectural rationale, not yet evidence of superiority. Karpathy maintains a performance log and calls the flat result a rough baseline with further tuning left open.

At 00:21-00:35, a small scratch batch exposes tensor shapes at each layer. Linear operations use the last input dimension and preserve leading batch dimensions. Pair embeddings are packed into groups, first through explicit even/odd indexing and concatenation, then through a cheaper reshape. Element-wise equality verifies that the two layouts agree. The custom FlattenConsecutive is named differently because its behavior departs from PyTorch Flatten. Explicit shape formulas and a specified squeeze dimension catch departures from expectations instead of relying on permissive inferred dimensions.

At 00:35-00:45, the model becomes a three-level hierarchy. Holding parameter count near 22,000 gives roughly equal validation performance, 2.029 versus 2.027. He does not claim a win. An existing BatchNorm layer accepts the new three-dimensional input through broadcasting but normalizes the wrong dimensions, maintaining separate statistics for positions instead of channels. Inspecting running-statistic shape reveals the error. Reducing over both batch and position dimensions fixes it; a single step checks expected state shapes before retraining. His NLC convention differs from PyTorch BatchNorm1d's NCL, explicitly disclosed.

At 00:45-00:47, the fix gives a small improvement to 2.022 that he says may not be statistically significant. More embeddings and hidden units increase parameters and training time and produce roughly 1.993 validation loss. These demonstrations lack a systematic experimental harness, so they do not establish the best hyperparameters or prove the hierarchy universally better.

At 00:47-end, the lesson implements only WaveNet's hierarchical structure, excluding its gated layer, residual and skip connections. Convolution is explained as an efficient sliding implementation that can reuse overlapping computations. Notebook prototypes inspect layer behavior and tensor shapes before code is moved into the training repository and experiments are launched. Proper tuning would track both training and validation losses across experiment populations. He invites attempts to beat 1.993 and explicitly leaves open whether a sufficiently tuned original flat model could beat the hierarchy.

Useful additional evidence, preserving automatic-caption errors:

> [00:38:45] um uh that because it runs but does it

> [00:38:49] do the right thing

## Coverage and interpretation

Status: **complete-preserved-text-no-media-review**. Reviewed lines 1-1630, covering all metadata and preserved caption cues sequentially. This is complete review of the saved text, not an audio or visual completeness certification. Caption errors are preserved. No linked code, papers, diagrams or media was independently executed or inspected. Source dates do not establish current library behavior; benchmark results belong to the demonstrated dataset and settings.

Related: [Karpathy index](../../../karpathy/index.md), [principles](../../../karpathy/principles.md), [methods](../../../karpathy/methods.md).
