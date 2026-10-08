---
type: source
subject: Karpathy autoresearch README
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, ai-workspace, experiments]
sources: [../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/autoresearch/README.md]
semantic-status: compiled-readme-only
---

# Autoresearch bounds an experiment loop

Original: [autoresearch README](https://github.com/karpathy/autoresearch), repository owner Andrej Karpathy; individual passage authorship not independently verified. Publication date unknown; collection and compilation date 2026-10-08. The complete preserved README text was read, including platform constraints and forks. This is not a semantic review of the repository's code.

[Raw evidence](../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/autoresearch/README.md). SHA-256: `3958fd4195ac2f98ed35c4eaa4f3028a335165ee24945e96426c408d25793a41`. Captured commit and collector license information are recorded in the [GitHub manifest](../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json); they were not independently fetched here.

## What the README says

The introduction describes an iterative evaluation loop:

> It modifies the code, trains for 5 minutes, checks if the result improved, keeps or discards, and repeats.

“Design choices” restricts the mutable code surface:

> The agent only touches `train.py`. This keeps the scope manageable and diffs reviewable.

“How it works” names the objective:

> The metric is **val_bpb** (validation bits per byte) — lower is better, and vocab-size-independent so architectural changes are fairly compared.

## Interpretation and limits

A useful local research pattern is to choose a bounded edit surface, comparable run budget and explicit objective before automation. This is an interpretation of this project, not yet a universal Karpathy rule. No GPU compatibility, training outcome, dependency installation or runtime safety claim was tested. The README's permissions advice remains quoted source content and does not replace this workspace's permissions. The teaser image, linked tweets, forks and implementation files were not reviewed here. Cross-hardware comparison limitations in the README remain relevant; a fixed duration alone does not normalize different machines.

Related: [index](../../karpathy/index.md), [principles](../../karpathy/principles.md), [methods](../../karpathy/methods.md).
