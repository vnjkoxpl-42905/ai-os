---
type: reference
subject: Bounded deterministic retrieval from compiled knowledge
created: 2026-10-26
updated: 2026-10-26
aliases: [brain search, query brain, section retrieval]
tags: [ai-workspace, retrieval, second-brain]
sources:
  - ../../wiki/sources/ultimate-second-brain-arms-robonuggets.md
  - ../../wiki/sources/obsidian-in-24-minutes-tina-huang.md
---

# Find candidate evidence without loading whole pages

`system/scripts/query-brain.py` adds a small local retrieval helper to the existing catalog route. It indexes the pages linked from the wiki, AI workspace, corpus and design entry points. It does not replace those catalogs or answer a question itself. Raw inputs, student records, credentials and external paths are outside its allowed roots. Student questions retain the student router; Loophole questions retain their dedicated retrieval guide.

Run from the vault root:

```powershell
py -3.12 system/scripts/query-brain.py --build
py -3.12 system/scripts/query-brain.py "apology emails" --limit 3 --chars 1400 --follow
```

The build writes only `system/generated/brain-search.generated.json` and uses a hash comparison before replacing that generated file. Query reads local evidence, emits scored candidate paths and bounded sections, and can list up to five safe one-hop pointers. It explicitly reports ties, misses, truncation and stale content. Read the relevant full section and underlying source before drawing a conclusion; a top-ranked candidate is not an adjudicated answer.

The index stores titles, aliases, subjects and headings. Query combines meaningful words, a small explicit synonym map and inverse-frequency weights. It checks catalog membership/hashes and indexed-page timestamps/sizes before ranking, then re-hashes selected evidence before displaying it. A changed catalog or indexed page requires rebuilding; the helper does not silently present its old ranking as current. Unindexed new pages still require catalog maintenance first. Preserving both a page's old timestamp and size can evade the metadata precheck for an unranked page; this is a local performance check, not an adversarial tamper-proof index. Selected-page hashes still prevent returning changed bytes as a verified old excerpt.

The helper's evidence does not establish current bookings, balances, correspondence, assignments or publication. Those questions still require the owning live backend. Smart Connections remains an optional separate aid; this change neither installs embeddings nor declares a new semantic-search policy.

## What has actually been checked

Ten meaningful regression tests cover alias and synonym-only candidates, explicit misses, changed catalogs, newly added catalogs, stale matching and previously unranked pages, ambiguous matches, safe pointer paths and raw/outside/credential exclusions. An independent review reproduced two defects before the corresponding fixes and regression tests were added.

The [local benchmark](../../research/2026-10-26-source-implementation/retrieval-benchmark.json) records repeatable candidate correctness, timing and returned character counts. These are local script measurements. No claim of actual model-token savings or superiority to a complete human/agent catalog session is made; that comparison remains the narrowed remainder of AQ-034.

## Apply the source's useful part

The [ARMS source](../../wiki/sources/ultimate-second-brain-arms-robonuggets.md) proposes deterministic candidate ranking, section reads and pointer following. Those parts are implemented here. Its claimed 40% saving is not a target borrowed into our results. The practical test is whether a question reaches supporting evidence with a smaller, readable result and an honest failure when the route is stale or missing.
