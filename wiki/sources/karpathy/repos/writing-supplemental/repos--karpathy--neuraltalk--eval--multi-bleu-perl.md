---
type: source
subject: Karpathy repository source context
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [llm-wiki, karpathy, source-context]
sources:
  - ../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk/eval/multi-bleu.perl
---

# repos/karpathy/neuraltalk/eval/multi-bleu.perl

Original: [captured source](https://github.com/karpathy/neuraltalk). Capture: 2026-10-08T09:35:06.509260Z. Attribution: karpathy; classification: `evaluation_utility_attribution_unresolved`.

Archived: [physical raw file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk/eval/multi-bleu.perl). SHA-256: `023a6f92773858d8851dc55dee5f545c44e6a389a7615daaff7536d296ea518e`.

## Source account

```text
Reads the references from reference or reference0, reference1, ...
```

Perl evaluator computes clipped corpus n-gram precision with multiple references and closest-reference lengths. It reports separate geometric BLEU-1 through BLEU-4 values. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk/eval/multi-bleu.perl).

```text
my $brevity_penalty = 1;
```

Brevity penalty remains fixed at one because its update is commented out; scores differ from standard brevity-penalized BLEU. This imported/modified evaluation utility has no author attribution in the captured header. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk/eval/multi-bleu.perl).

## Limits

Code not executed; configured checks are not passing test evidence. This source does not independently establish Karpathy personal beliefs. Raw unchanged.
