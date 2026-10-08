# Karpathy writings: mechanism, measurement and operating burden

Compiled 2026-10-08. This is agent synthesis of explicitly read texts, not a claim to reproduce Karpathy's private thinking. The [coverage ledger](blog-semantic-coverage.jsonl) inventories all 79 preserved Markdown files with current SHA-256 checks. This pass fully read and compiled 24 texts; one additional article has a prior source page. The remaining 54 have not yet been semantically read in this pass. HTML counterparts are not counted as independent sources. CS231n pages need course/team attribution, not automatic sole-author attribution.

## Rules supported by distinct writings

| Candidate rule | Concrete behavior | Supporting sources | Limits |
|---|---|---|---|
| Understand the mechanism before relying on the abstraction | Explain the inputs, transformation, output and failure mode; reproduce a minimal operation when diagnosis requires it. | [Backprop](../../wiki/sources/karpathy/blog/understand-backprop.md) and [microgpt](../../wiki/sources/karpathy/blog/microgpt.md) | Mechanism literacy is not a requirement to reinvent every production dependency. |
| Make one correct small case, then extend it | Establish a simple end-to-end baseline, predict the next change and check whether the measured result agrees. | [Recipe](../../wiki/sources/karpathy/blog/recipe.md) and [microgpt](../../wiki/sources/karpathy/blog/microgpt.md) | Educational minimality and production capacity are separate objectives. |
| Build a trustworthy feedback loop | Specify an attempt, an observable result and an efficient way to evaluate it before optimizing. | [Recipe](../../wiki/sources/karpathy/blog/recipe.md) and [Verifiability](../../wiki/sources/karpathy/blog/verifiability.md) | Automated reward can be wrong. Preserve human judgment for unverified objectives. |
| Inspect the evidence/data, not only the code | Look for duplicates, label problems, outliers and the exact inputs seen by the system. | [Recipe](../../wiki/sources/karpathy/blog/recipe.md) and [Software 2.0](../../wiki/sources/karpathy/blog/software-2-0.md) | A clean local collection is not proof of complete source coverage. |
| Teach for reconstruction rather than recognition | Have the learner explain or rebuild a concrete mechanism without merely rereading a finished answer. | [Study advice](../../wiki/sources/karpathy/blog/undergraduate-study-advice.md) and [Backprop](../../wiki/sources/karpathy/blog/understand-backprop.md) | This is a teaching interpretation; it does not overwrite Joshua's LSAT pedagogy. |
| Minimize unnecessary dependency and operating burden | Ask whether a smaller local artifact or simpler interface can deliver the job before adding accounts and services. | [Calculator](../../wiki/sources/karpathy/blog/calculator.md) and [microgpt](../../wiki/sources/karpathy/blog/microgpt.md) | Necessary integrations remain necessary; this is not a ban on cloud services. |
| Verify the real operating path, not only the attractive demo | Check identity mapping, configuration, persistence and failure behavior as separate acceptance stages. | [MenuGen](../../wiki/sources/karpathy/blog/vibe-coding-menugen.md) and [Recipe](../../wiki/sources/karpathy/blog/recipe.md) | The neural-training recipe is supporting analogy; MenuGen directly reports web-app integration failures. |

These are distinct articles, but some explicitly cite earlier work. They are separate evidence artifacts, not independent experimental replications. No claimed rule depends on two syndicated copies of the same post.

## Useful additional patterns with narrower evidence

- [Append and review](../../wiki/sources/karpathy/blog/append-and-review.md): keep capture easy, then repeatedly rescue, merge and reconsider valuable ideas. His one-note preference differs from the current vault and does not authorize flattening it.
- [Auto-grading Hacker News](../../wiki/sources/karpathy/blog/auto-grade-hn.md): validate one example manually, then collect evidence, require parseable output and render readable results. Model grades remain judgments, not truth. Its paid reproduction is not part of this work.
- [Space of minds](../../wiki/sources/karpathy/blog/space-of-minds.md): reason about an AI system's objective and distribution instead of assuming animal motives. The article is conceptual and speculative.
- [Power to the people](../../wiki/sources/karpathy/blog/power-to-the-people.md): use broad quasi-expertise to extend an individual's reach, with checks for shallow or fallible performance.
- [Forward Pass](../../wiki/sources/karpathy/blog/forward-pass-fiction.md) is fiction. It can illustrate plausibility versus correctness but cannot substantiate consciousness claims.
- [Books](../../wiki/sources/karpathy/blog/books-preferences.md) describes Karpathy's taste, not Joshua's taste or a universal style prescription.
- [Manual CIFAR-10 classification](../../wiki/sources/karpathy/blog/manual-cifar10.md) independently illustrates direct data inspection and keeps an explicit correction to an overconfident performance forecast. [Hacker News collection in 2013](../../wiki/sources/karpathy/blog/hacker-news-collection-2013.md) likewise records actual downtime gaps instead of claiming complete coverage from the title.
- [Jekyll migration](../../wiki/sources/karpathy/blog/switching-to-jekyll.md) supports portable Markdown and separated generated output. Historical course [Terminal setup](../../wiki/sources/karpathy/blog/cs231n-terminal-tutorial.md) and [transfer learning](../../wiki/sources/karpathy/blog/cs231n-transfer-learning.md) are course material, not automatic sole-author evidence or current infrastructure instructions.

## What has not been silently promoted

No raw source was modified. No source instruction became an agent command. No provider/version claim was reclassified as current capability. No student teaching policy, personal memory, canonical route, active skill, persona or hook was changed by this compilation. Source images, remote links and companion HTML were not visually reviewed. The interview announcement, Medium announcement and About page are fully read routing stubs; the absent linked interview was not represented as collected content.

The remaining unread inventory is explicit in the ledger. Do not treat an inventory/hash pass as a semantic full read or claim the entire 79-article corpus has been distilled yet.
