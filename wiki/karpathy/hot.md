---
type: synthesis
subject: Karpathy reviewed evidence hot page
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, llm-wiki]
sources: [../sources/karpathy/llm-wiki.md, ../sources/karpathy/autoresearch-readme.md, ../sources/karpathy/micrograd-readme.md, ../sources/karpathy/jobs-readme.md, ../sources/karpathy/animals-vs-ghosts.md]
---

# Use the reviewed method and preserve its limits

Prompt 2 remains partial: source pages and explicit coverage now span writings, repositories, lectures and X. A first working method uses [seven corroborated rules](rules.md); it does not represent a complete account of Karpathy. Joshua's own instructions and teaching voice remain authoritative. [Execution status](../../research/karpathy-brain-2026-10-08/VIDEO-PROMPT-EXECUTION.md) distinguishes local validation from native runtime acceptance.

**Compile and maintain knowledge.** The LLM Wiki gist says: “The knowledge is compiled once and then *kept current*, not re-derived on every query.” [Raw gist](../../raw/sources/karpathy-brain/raw/github/gists/442a6bf555914893e9891c11519de94f/llm-wiki.md), The core idea section.

**Make experiments inspectable.** autoresearch says: “The agent only touches `train.py`. This keeps the scope manageable and diffs reviewable.” [Raw README](../../raw/sources/karpathy-brain/raw/github/repos/karpathy/autoresearch/README.md), Design choices section. This is one project's design, not an established universal rule.

**Use small educational mechanisms.** micrograd describes its implementation: “Both are tiny, with about 100 and 50 lines of code respectively.” It adds: “Potentially useful for educational purposes.” [Raw README](../../raw/sources/karpathy-brain/raw/github/repos/karpathy/micrograd/README.md), opening. Static reading does not certify execution.

**Preserve limits around model judgments.** jobs says: “The scores are rough LLM estimates (Gemini Flash via OpenRouter), not rigorous predictions.” [Raw README](../../raw/sources/karpathy-brain/raw/github/repos/karpathy/jobs/README.md), What AI Exposure is NOT section. BLS data is third-party evidence, not his personal beliefs.

**Keep uncertainty explicit.** Animals vs Ghosts says: “And I say both of these with double digit percent uncertainty and cheer the work of those who disagree, especially those a lot more ambitious bitter lesson wise.” [Raw article](../../raw/sources/karpathy-brain/raw/blog/md/bearblog/karpathy.bearblog.dev_animals-vs-ghosts.md), author's own discussion.

For teaching, reconstruct a mechanism, begin with a correct small baseline, predict/run/compare, expose a useful counterexample, prove relevant behavior, state assumptions and retain justified simplicity. Exact quotes and two-source support for each rule live in [rules](rules.md). These are operational interpretations, not his endorsement.

The project `karpathy-teach` skill delegates to the Karpathy-method agent in Claude and provides the same reviewed workflow in Codex. Claude's revised project Stop gate has 18 passing tests; native acceptance remains pending. Codex uses workflow receipts rather than a claimed Claude hook. New teaching code belongs outside the vault in `ai-os-projects/karpathy-method-tools/examples/`. Existing `ingest` remains the single front door for new sources.

[Index and coverage](index.md), [principles](principles.md), [methods](methods.md). Sources and new captured evidence remain immutable; corpus-wide reading, media review and exhaustive X coverage remain open.
