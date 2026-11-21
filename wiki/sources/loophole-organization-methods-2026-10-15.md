---
type: comparison
subject: Primary organization methods supporting Loophole library integration
created: 2026-10-15
updated: 2026-10-15
aliases: [Loophole organization methods, Karpathy Nate Herk routing review]
tags: [ai-workspace, loophole, navigation, llm-wiki]
evidence: ../../raw/sources/loophole-organization-methods-2026-10-15/karpathy-llm-wiki.md
sha256: dc3efe98ae62f23dd08acad13aba2e95287beb20b6bec2f4af0423557fe37401
contradictions: []
sources:
  - ../../raw/sources/loophole-organization-methods-2026-10-15/PROVENANCE.md
  - ../../raw/sources/loophole-organization-methods-2026-10-15/nate-README.md
  - ../../raw/sources/loophole-organization-methods-2026-10-15/nate-AGENTS.md
---

# Integrate the Loophole library through existing routes

Checked 2026-10-15. These organization references support the [existing Loophole integration](../../corpus/loophole-online/organization.md), not adoption of its teaching prescriptions. The [adoption ledger](../../references/ai-workspace/second-brain-adoptions.md) remains the broader decision record.

## What the primary sources support

**Karpathy:** the [original LLM Wiki idea file](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) separates immutable evidence, maintained Markdown knowledge and schema. An index supports retrieval; an append-only log records changes. Ingest, query and lint keep the collection connected. The directory design depends on the domain. [Captured original bytes](../../raw/sources/loophole-organization-methods-2026-10-15/karpathy-llm-wiki.md).

**Nate Herk:** the current [official starter-kit README](https://github.com/nateherkai/AIS-OS/blob/ce9cb93a1145da5daba84ea37208ec35fd03606e/README.md) describes adding a small useful route to existing manuals or indexes and checking it resolves. Its audit uses retrieval probes, freshness and source-authority checks rather than counting folders. [Archived README](../../raw/sources/loophole-organization-methods-2026-10-15/nate-README.md), SHA-256 `517ff2ae35888ca9da1f1c32c51c79756f068e8e034903867f141cd0474c069f`; [matching AGENTS](../../raw/sources/loophole-organization-methods-2026-10-15/nate-AGENTS.md), SHA-256 `139087ea433cf7dff3998473d101e25aecd465a9e2a3399b398a1347fe1e218c`.

## Mentions in source

> "These are immutable" (Karpathy, Architecture)

> "This document is intentionally abstract." (Karpathy, Note)

## Our implementation and its boundaries

Preserve one vault and the RC, LR and shared-method homes. Publish hash-verified question transcripts and MP3s into the existing Loophole reading library with relative links. Retain Desktop as processing evidence, not a second editable reading authority. Route lectures, Camo, workouts, routines and prep-map captures from their existing hubs. This is our design choice; neither author prescribes this layout.

Verify navigation with representative retrieval paths and byte comparisons. Preserve missing-source, silence and subtitle exceptions. Machine transcripts remain unreviewed unless separately checked against audio. Source filing does not approve curriculum, publishing or student assignments.

The [Camo capture](loophole-how-to-camo-2026-10-15.md) and [LR recording publication](loophole-lr-recordings-2026-10-15.md) are concrete applications: the former needed a route into shared methods, while the latter needed portable files and verified source identities. Their content claims remain attributed to their own sources.

## Snapshot limits and intake outcome

Nate's pinned commit is `ce9cb93a1145da5daba84ea37208ec35fd03606e`, committed 2026-09-07T01:16:39Z. This is the official branch snapshot retrieved on 2026-10-15, not proof of the newest video date. Karpathy's official page reported one revision created 2026-04-04; the revision API returned HTTP 502, so no revision SHA is claimed. The raw file is pinned by its actual SHA-256. Third-party Gist comments were excluded.

[Provenance, capture metadata and checksums](../../raw/sources/loophole-organization-methods-2026-10-15/PROVENANCE.md) preserve all three primary files. Five archive hashes and three inbox/archive byte pairs matched. Prior source summaries were left unchanged. This comparison is complementary to the adoption ledger; no new service, skill, scheduled automation or curriculum queue item is proposed.

Schema suggestion: retain one publication manifest linking every delivered transcript and audio file to its captured source and verified hash.
