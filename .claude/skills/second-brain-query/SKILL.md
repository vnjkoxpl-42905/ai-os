---
name: second-brain-query
description: >
  Answer questions using saved wiki knowledge, such as "what do we know
  about X", "search my wiki", or "compare these ideas". Read the index first,
  cite evidence, and save valuable new synthesis under the vault schema.
allowed-tools: Bash Read Write Edit Glob Grep
---

# Answer from the wiki and preserve useful synthesis

## Resolve the vault and schema first

Find the vault root from the current workspace and its nearest instruction files.
Read `system/schema/llm-wiki.md` relative to that root. It is the authority for
folder conventions, page metadata, provenance, index, log, and ingest/query/lint
workflows. Do not assume a saved Windows or Mac path. If no schema exists in the
target vault, report that gap before changing its structure; never initialize a
second vault to solve a request about an existing one.

1. Start with the curated navigation before the generated catalog in
   `wiki/index.md`. Use bounded `rg` searches within large catalogs/domain
   indexes for the subject, title or aliases, then follow relevant page links.
   The catalog prints each page's aliases after "Also:". Search by meaning, not
   only the question's literal words: try five to ten keyword variants
   (synonyms, abbreviations, the creator's or product's name). From the pages
   you find, follow outgoing links and backlinks one hop (`rg -l` for the page's
   filename finds its backlinks). Do not load a large index wholesale. Use
   `wiki/hot.md` only when session context matters. Broader search is a
   fallback for a missing route; do not dump the wiki or raw collection into
   context.
2. Read the selected pages and source summaries. Follow source evidence when
   precise wording, conflicting claims, or missing detail requires it. Distinguish
   verified facts, dated operational snapshots, interpretations, and unknowns.
3. For live scheduling, payment, correspondence, homework, or publish state,
   check the owning live backend when freshness matters. Do not treat an old
   wiki snapshot as current truth.
4. Answer directly in an appropriate format. Cite the relevant saved page or
   original source beside material claims. In chat use clickable absolute file
   links; in saved pages use unambiguous vault links. Do not invent sources.
   If no compiled page supports the answer, say so first ("not in the compiled
   wiki; nearest pages: ...") and label what comes from raw sources, live
   systems or general knowledge instead.
5. Before saving, classify the answer against the pages you read: fully
   redundant (save nothing), partially new (add only the new part to its owning
   page) or entirely new. Save a valuable new comparison, analysis, or connection
   to its existing authoritative page or an appropriate `wiki/synthesis/` page.
   This schema authorizes routine filing; do not repeatedly ask permission.
   Preserve source citations and label reasoning. Do not turn a recommendation
   into a locked decision without Joshua adopting it. Skip saving trivial
   answers, repeated explanations, mechanical operations, or content the user
   requests stay unsaved. Never rewrite a page marked `reviewed: true`; add a
   dated `## New information` section instead.
6. Update the index for saved changes and append a dated `query` log entry
   describing the question, evidence/pages read, saved output if any, and gaps.
   Do not log transient read-only answers merely to fill the log. A retrieval
   miss is not filler: when the index route failed but the answer existed
   elsewhere, log a `query` entry with a `Miss:` line naming the question and
   where the answer was found, so the route or missing page gets fixed.
   In ai-os run `py system/scripts/wiki-maintenance.py --index` to refresh its
   generated catalog when saving pages. Follow generated-section ownership and
   compare-and-swap for automated edits.
7. Verify the filed answer's links, index, and log, then report its location.

New sources enter through `second-brain-ingest`. Knowledge-health requests use
`second-brain-lint`. Do not browse or ingest new evidence silently to manufacture
confidence; identify the gap and follow the current authorization.

## Bounded compiled-page helper in ai-os (2026-10-26)

After reading the curated index navigation, the local helper can shortlist evidence without loading whole pages:

```powershell
py -3.12 system/scripts/query-brain.py --build
py -3.12 system/scripts/query-brain.py "the question" --limit 3 --chars 1400 --follow
```

Use this only when the resolved vault has that script. Rebuild after catalog/page edits or a stale-index result. The helper returns bounded candidate sections, explicit synonym matches, ambiguity, misses and safe one-hop pointers. It excludes raw/student/credential/external roots; use the student router and dedicated Loophole retrieval guide for those domains. Read complete relevant evidence before answering, and still check the owning live backend for current operational state. A shortlist is not an answer, a verified fact or proof of token savings. Missing results fall back to bounded index/alias searches rather than proving knowledge absent. See references/ai-workspace/compiled-retrieval.md for measured coverage and limits.
