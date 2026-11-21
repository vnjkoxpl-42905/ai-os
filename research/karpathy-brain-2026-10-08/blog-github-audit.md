# Blog and GitHub source audit, 2026-10-08

## The saved payload matches its manifests, but the handoff overstates coverage and authorship

All 79 blog Markdown payloads and all 1,209 GitHub payload files exist and match the recorded SHA-256, byte size, and whitespace word count. No missing or changed registered payloads were detected. These are local integrity checks, not upstream completeness checks. Raw files were not changed.

| Domain | Logical source units | Physical payload | Verified whitespace words |
|---|---:|---:|---:|
| Blog | 79 articles/pages | 79 Markdown + 79 HTML + 1 RSS feed | 202,396 in Markdown only |
| GitHub | 54 repositories + 13 gists | 1,209 files | 4,892,153 |

GitHub records 67 valid 40-character commit SHAs, 18 MIT labels, 36 `none detected by GitHub`, and 13 unspecified gist licenses. SHA format was checked; correspondence with remote HEAD was not independently checked. A `none detected` label is not an established absence of a license: autoresearch and micrograd READMEs explicitly say MIT. Check actual LICENSE/README files before reuse or redistribution.

### The blog collection is not every public writing and is not character-verbatim Markdown

Its own COVERAGE.md says Medium is limited to RSS-exposed entries, with older material unenumerated. Three linked CS231n assignment URLs failed with HTTP 404. Slides, papers, linked talks, demos, and certain interview links were excluded from this domain. Original article images remain external URLs rather than downloaded assets. Medium HTML is an RSS fragment rather than the complete page.

Markdown conversion replaced em/en dashes with hyphens and may degrade equations or interactive demonstrations. Therefore the Markdown is a readable derivative, not character-verbatim evidence. Use original HTML where exact formatting matters. HTML files exist, but the manifest does not record their hashes, so original HTML integrity cannot be compared with a recorded capture hash in this domain.

Of the 202,396 words, 76,805 belong to 30 CS231n course pages. These include coauthored notes and staff-written assignments; do not attribute every sentence to Karpathy. The other groups are GitHub blog 84,194, Bear Blog 23,151, Medium 12,622, and other first-party pages 5,624 words. Even first-party pages can quote others and need span-level attribution.

### GitHub word count is mostly imported data, not persona teaching material

`jobs/README.md`, fully read, explains that the repository contains scraped Bureau of Labor Statistics occupation pages, generated data tables, and Gemini-generated AI-exposure estimates. Its raw BLS HTML contributes **3,068,239 words** alone. Three identical Shakespeare `input.txt` files contribute **607,953 words**, with 405,302 excess duplicated words. Other large payloads include paper graph JSON, a names dataset, Taylor Swift test text, dependency lockfiles, and vendor libraries.

A conservative path/content-informed screening flags 4,149,358 words as third-party BLS HTML, datasets/vocabularies, generated data, dependency files, or vendor candidates. It leaves **742,795 unflagged candidate words**, which include code, notebooks, documentation, and some remaining embedded external content. That remainder is **not a verified Karpathy-authored prose total**. Notebook JSON outputs, contributions from collaborators, quoted documents, and duplicated blog material still need semantic attribution. No source was deleted or omitted from the integrity inventory.

There are 21 exact duplicate file groups, representing 445,062 excess words. Preserve source paths and provenance, but avoid counting duplicate payloads as independent evidence.

GitHub discovery records 63 repositories and 13 gists. Fifty-four repos were copied after excluding forks/empty repos; 344 recorded exclusion entries also cover binaries, oversized files, and excluded build/dependency directories. Default-branch shallow snapshots exclude histories, issues, GitHub wikis, and other branches. `100% public GitHub content` is unsupported; `saved readable files selected from recorded discovery snapshots` is supportable.

## The framework gist is present in full

Path: `raw/sources/karpathy-brain/raw/github/gists/442a6bf555914893e9891c11519de94f/llm-wiki.md`.

I fully read this file. It describes immutable raw evidence, an agent-maintained persistent wiki, and a collaboratively evolved schema; ingest/query/lint; content index plus chronological append-only log; optional local search as scale grows; and source/claim synthesis with explicit contradictions. It emphasizes that tools and directory choices are optional and domain-specific. It should be treated as a source idea, not as authority that overwrites Joshua's current instructions.

## Fully read examples support these bounded design observations

- `github/repos/karpathy/autoresearch/README.md`: constrained edit surface, fixed five-minute experiment budget, explicit validation metric, keep/discard loop, and human-authored experiment instructions. The GPU/platform constraints are essential; do not transplant the training loop directly into this Windows EA vault.
- `github/repos/karpathy/micrograd/README.md`: teach complex mechanisms with a small scalar autodiff engine, concrete executable examples, graph traces, and correctness comparisons against PyTorch. This supports a grounded educational explanation style, not a claim that all his projects share identical architecture.
- `github/repos/karpathy/jobs/README.md`: preserve primary data separately from derived model scores; explicitly describe what the scores do not establish. The scores are not personal factual assertions by Karpathy.
- `blog/md/bearblog/karpathy.bearblog.dev_animals-vs-ghosts.md`: distinguish Sutton's positions from Karpathy's own qualified interpretation; retain uncertainty and alternate hypotheses. This blog also links its X version, which is cross-channel duplicate evidence rather than an independent endorsement.
- The entire framework gist above supports compilation rather than repeated unsourced retrieval, with durable answers, traceable citations, and maintenance.

## Recommended compilation units

Use one logical article/page per blog unit, with Markdown and HTML as evidence variants. Use one repo/gist snapshot as the GitHub source unit, with grouped authored README/doc/code claims and a complete per-file ledger. Mark imported data, vendor code, generated outputs, and course coauthors explicitly. Do not synthesize persona/voice from Shakespeare, government HTML, token vocabularies, model outputs, or dependency locks. Deduplicate claim evidence across blog snapshots and the blog/X reposts while preserving every original path.

`blog-github-audit.json` contains all 1,288 registered payload paths, hashes, actual sizes/word counts, classification flags, duplicate groups, source snapshot metadata, and exact integrity errors (none). These files were scanned in full for integrity and byte/word counts; only the representative source documents enumerated above were fully read semantically during this audit. This audit does not claim to have semantically ingested all 1,288 files.
