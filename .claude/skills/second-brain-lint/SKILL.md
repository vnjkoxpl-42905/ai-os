---
name: second-brain-lint
description: >
  Check wiki health when asked to "lint my wiki", "check knowledge links",
  "find stale wiki claims", or "find contradictions in my second brain".
  General AI OS scoring belongs to audit, not this knowledge-health workflow.
allowed-tools: Bash Read Write Edit Glob Grep
---

# Check links, evidence, and accumulated knowledge

## Resolve the vault and schema first

Find the vault root from the current workspace and its nearest instruction files.
Read `system/schema/llm-wiki.md` relative to that root. It is the authority for
folder conventions, page metadata, provenance, index, log, and ingest/query/lint
workflows. Do not assume a saved Windows or Mac path. If no schema exists in the
target vault, report that gap before changing its structure; never initialize a
second vault to solve a request about an existing one.

1. Read the schema and curated `wiki/index.md` navigation, then use bounded
   searches of its generated catalog and relevant linked domain indexes.
   Establish the requested scope. Structural checks cover indexed knowledge
   and existing wiki pages, including legacy flat pages; do not assume every
   page lives in entities/concepts/sources/synthesis.
2. In ai-os run `py system/scripts/wiki-maintenance.py --lint` for structural
   checks. Its generated findings are a starting point, not semantic verification.
   Beyond links, provenance and orphans it reports, on curated pages: thin pages,
   new pages missing aliases or evidence fields, evidence drift, quotes not found
   in their evidence (`ungrounded-quote`), open `contradictions:` and
   duplicate-name candidates. For a broad lint also run `--evidence`, which
   re-hashes every `raw/sources/` archive against its `SHA256SUMS`; any mismatch
   means preserved evidence changed and is reported before anything else.
   Check heading anchors, frontmatter aliases, index completeness and cross-domain
   coverage separately; the helper does not establish these or factual accuracy.
   Use `py system/scripts/wiki-maintenance.py --index` when index repair is
   authorized. Check both Markdown links and vault wikilinks, including path-qualified
   targets, aliases and anchors. Resolve targets against actual vault paths;
   avoid false broken-link reports from headings, code blocks, or external URLs.
3. Check index coverage and metadata/provenance on new schema pages. Detect
   missing targets, duplicate subject pages, unindexed pages, and orphans.
   Distinguish navigation-only inbound links from useful knowledge connections.
4. Check related pages for contradictions, unsupported claims, missing source
   citations, confusing facts versus judgments, and stale operational snapshots.
   Age alone is not proof a claim is false. Cite both sources for disagreements.
   Check the context that loads every session too: `CLAUDE.md`, `AGENTS.md`, the
   memory index and `wiki/hot.md`. Report stale or conflicting lines and any file
   that has grown past its purpose; context that loads every time costs the most
   when it is wrong. After any logged rename of a skill, folder or page, `rg` the
   old name across the schema, root instructions, every `hot.md` and
   `references/`; history records (logs, decisions, research) keep old names.
5. Identify missing useful cross-references, significant subjects lacking pages,
   source coverage gaps, and unanswered questions. Suggest specific evidence to
   investigate. Do not create empty pages or launch bulk web research as a lint.
   List entity candidates: a person, product or tool that appears in three or
   more source summaries without its own page. Joshua approves each one before
   a page is made. When a folder of curated pages passes about 50 pages, propose
   a hub page or subfolder; never move pages without approval.
6. Report actionable errors, warnings, and questions with file/line evidence,
   proposed fixes, and the inspected scope. Label anything not inspected; a
   structural pass is not verification of every factual claim in the vault.
7. Apply routine reversible link/index corrections when authorized by a request
   to maintain or fix the wiki. A check-only request stays diagnostic. Preserve
   conflicts until adjudicated; no deletion, source modification, or invented
   facts. Use owning generators for generated content and compare-and-swap.
   Fix in causal order, because earlier fixes change later findings: wrong
   content, aliases, approved duplicate merges, dead links, orphans, thin pages,
   tags. Before an approved merge, retarget every inbound link found with `rg`.
   Fix an orphan with a one-sentence link from one to three related pages. Fill
   a thin page only from evidence. Never rewrite a page marked `reviewed: true`.
8. Append `## [YYYY-MM-DD] lint | Scope` to `wiki/log.md` with coverage, findings,
   fixes actually applied, and unresolved items. Verify affected links/indexes.

Run on request, after a substantial ingest batch, or when persistent gaps emerge.
No recurring automation is created by this skill. Source compilation is `second-brain-ingest`;
answer synthesis is `second-brain-query`.
