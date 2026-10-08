---
type: source
subject: "GitHub source repos/karpathy/arxiv-sanity-preserver/schema.sql"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/arxiv-sanity-preserver/schema.sql]
semantic-status: complete-named-text-read
---

# repos/karpathy/arxiv-sanity-preserver/schema.sql

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/arxiv-sanity-preserver/schema.sql), SHA-256 `3f0e7baae2842678795e203328b07f757eb3170214d20c6b54fd370b307050a1`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
drop table if exists user; create table user ( user_id integer primary key autoincrement, username
```

The preserver pipeline fetches versioned arXiv records incrementally with an explicit gentle wait and a stated early-stop assumption. PDFs are cached with timeouts; failed PDF conversion creates an empty marker, so attempted acquisition is not successful extraction. Analyze filters suspicious text lengths, fits TF-IDF on a seeded subset for memory efficiency, transforms the complete retained corpus and precomputes nearest neighbors. Buildsvm balances positive libraries against other papers. Make_cache precomputes dates, popularity and weighted lexical search to speed startup; its comments acknowledge missing bigram search. SQL defines user and library tables and contains destructive initialization statements that were read but never executed. Historical cache correctness, platform portability and completeness were not verified.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
drop table if exists user;
create table user (
  user_id integer primary key autoincrement,
  username text not null,
  pw_hash text not null,
  creation_time integer
);
drop table if exists library;
create table library (
  lib_id integer primary key autoincrement,
  paper_id text not null,
  user_id integer not null,
  update_time integer
);

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
