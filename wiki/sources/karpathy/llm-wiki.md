---
type: source
subject: Karpathy LLM Wiki gist
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, llm-wiki]
sources: [../../../raw/sources/karpathy-brain/raw/github/gists/442a6bf555914893e9891c11519de94f/llm-wiki.md]
semantic-status: compiled
---

# Compile knowledge into maintained pages

Original: [LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), Andrej Karpathy. Publication date unknown; collection and compilation date 2026-10-08. The complete preserved Markdown text was read. The gist revision was not independently established in this compilation.

[Raw evidence](../../../raw/sources/karpathy-brain/raw/github/gists/442a6bf555914893e9891c11519de94f/llm-wiki.md). SHA-256: `dc3efe98ae62f23dd08acad13aba2e95287beb20b6bec2f4af0423557fe37401`.

## What the document says

It describes a wiki that accumulates reviewed knowledge rather than reconstructing it for every question. In “The core idea”:

> The knowledge is compiled once and then *kept current*, not re-derived on every query.

Its architecture preserves source evidence. In “Architecture”:

> These are immutable — the LLM reads from them but never modifies them.

It leaves implementation choices to the user and agent. In “Note”:

> Everything mentioned above is optional and modular — pick what's useful, ignore what isn't.

## Interpretation and limits

For this workspace, the existing [LLM Wiki schema](../../../system/schema/llm-wiki.md) already owns ingest, query, lint, attribution and source preservation. This gist does not authorize replacement of Joshua's instructions or identity. Its optional plugin suggestions are source suggestions, not verified local capabilities. No plugin was installed and no linked external tool was assessed.

Related: [collection index](../../karpathy/index.md), [principles](../../karpathy/principles.md), [methods](../../karpathy/methods.md), and the earlier [LLM Wiki pattern summary](../llm-wiki-pattern.md). This page describes this specific preserved gist; the earlier summary remains the existing pattern reference.
