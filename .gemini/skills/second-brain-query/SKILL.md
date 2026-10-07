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

1. Read `wiki/index.md` first. Follow relevant page and domain-index links;
   use `wiki/hot.md` for session context when needed. Search with `rg` only when
   the index leaves a gap. No whole-wiki or whole-raw dump is needed.
2. Read the selected pages and source summaries. Follow source evidence when
   precise wording, conflicting claims, or missing detail requires it. Distinguish
   verified facts, dated operational snapshots, interpretations, and unknowns.
3. For live scheduling, payment, correspondence, homework, or publish state,
   check the owning live backend when freshness matters. Do not treat an old
   wiki snapshot as current truth.
4. Answer directly in an appropriate format. Cite the relevant saved page or
   original source beside material claims. In chat use clickable absolute file
   links; in saved pages use unambiguous vault links. Do not invent sources.
5. Save a valuable new comparison, analysis, or connection to its existing
   authoritative page or an appropriate `wiki/synthesis/` page. This schema
   authorizes routine filing; do not repeatedly ask permission. Preserve source
   citations and label reasoning. Do not turn a recommendation into a locked
   decision without Joshua adopting it. Skip saving trivial answers, repeated
   explanations, mechanical operations, or content the user requests stay unsaved.
6. Update the index for saved changes and append a dated `query` log entry
   describing the question, evidence/pages read, saved output if any, and gaps.
   Do not log transient read-only answers merely to fill the log.
   In ai-os run `py system/scripts/wiki-maintenance.py --index` to refresh its
   generated catalog when saving pages. Follow generated-section ownership and
   compare-and-swap for automated edits.
7. Verify the filed answer's links, index, and log, then report its location.

New sources enter through `ingest`. Knowledge-health requests use
`second-brain-lint`. Do not browse or ingest new evidence silently to manufacture
confidence; identify the gap and follow the current authorization.
