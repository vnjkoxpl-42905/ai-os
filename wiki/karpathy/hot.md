---
type: synthesis
subject: Karpathy reviewed evidence hot page
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, llm-wiki]
sources: [../sources/karpathy/blog/undergraduate-study-advice.md, ../sources/karpathy/blog/recipe.md, ../sources/karpathy/blog/understand-backprop.md, ../sources/karpathy/blog/microgpt.md, ../sources/karpathy/x/claude-coding-notes.md, ../sources/karpathy/animals-vs-ghosts.md]
---

# Teach with small mechanisms and inspectable checks

The [collected sources are compiled](../../research/karpathy-brain-2026-10-08/COMPILATION-AUDIT.md). [Seven rules](rules.md) have exact quotes from two distinct original artifacts each. They are practical synthesis, with historical exceptions retained. Joshua's instructions and teaching voice remain authoritative.

**Reconstruct the mechanism.** “Reading and understanding IS NOT the same as replicating”. [Study advice](../sources/karpathy/blog/undergraduate-study-advice.md).

**Begin with a small baseline.** “get that to work, and then generalize it later making sure that I get the same result.” [Recipe](../sources/karpathy/blog/recipe.md).

**Predict, run and compare.** “make concrete hypotheses about what will happen and then either validate them with an experiment or investigate until we find some issue.” [Recipe](../sources/karpathy/blog/recipe.md).

**Repair a cause through a counterexample.** “The problem is on line 291.” [Backprop article](../sources/karpathy/blog/understand-backprop.md), the clipped-error gradient example.

**Verify relevant behavior.** “Get it to write tests first and then pass them.” [Coding notes](../sources/karpathy/x/claude-coding-notes.md). Running code alone does not establish correctness; [rules](rules.md) preserves a contrasting historical beam-search admission.

**Expose assumptions and uncertainty.** “the models make wrong assumptions on your behalf and just run along with them without checking.” [Coding notes](../sources/karpathy/x/claude-coding-notes.md). “with double digit percent uncertainty” [Animals vs Ghosts](../sources/karpathy/animals-vs-ghosts.md).

**Earn complexity.** “I cannot simplify this any further.” [Microgpt](../sources/karpathy/blog/microgpt.md). Necessary production safeguards still belong in production.

The configured teaching agent reads this page first, uses at most five wiki pages, cites source pages and applies all seven rules. The skill grades its answer before presentation. End with **What I ran**, **What came out**, **What I changed**. Teaching code belongs outside the vault in `ai-os-projects/karpathy-method-tools/examples/`.

Claude's project hook has behavioral tests and a [native blocking/recovery probe](../../research/karpathy-brain-2026-10-08/NATIVE-STOP-ACCEPTANCE.md). Its original ordered replay hit the Pro session limit; the literal tokenizer invocation remains pending. Codex's workflow is not a native Claude hook.

Use existing `ingest` for new sources. Preserve raw evidence. Foreign authors, payloads, caption errors and linked media retain their limits. [Index](index.md), [principles](principles.md), [methods](methods.md), [current status](../../research/karpathy-video-2026-10-08/VERBATIM-COMPLIANCE.md).
