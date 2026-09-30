---
name: second-brain
description: >
  Initialize a genuinely new knowledge vault only when explicitly asked.
  Existing-vault adaptation follows its schema and preserves existing files.
  This setup skill does not ingest sources or answer knowledge queries.
allowed-tools: Bash Read Write Edit Glob Grep
---

# Set up a new vault without replacing an existing brain

## Resolve the vault and schema first

Find the vault root from the current workspace and its nearest instruction files.
Read `system/schema/llm-wiki.md` relative to that root. It is the authority for
folder conventions, page metadata, provenance, index, log, and ingest/query/lint
workflows. Do not assume a saved Windows or Mac path. If no schema exists in the
target vault, report that gap before changing its structure; never initialize a
second vault to solve a request about an existing one.

1. Resolve the intended workspace. If it is an existing vault, read its
   instruction files and schema and adapt them in place under the user's
   request. Never create a parallel vault, run the old scaffold script, or
   overwrite existing `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, index, or log.
   Ordinary current-vault knowledge operations use ingest/query/lint instead.
2. For an explicitly requested new vault, establish its name, location, domain,
   and selected agents using context first. Ask for material missing choices.
   Reject overwriting a populated target. Resolve paths on the current machine.
3. Co-author a schema with raw immutable sources, compiled wiki pages, folder
   and naming conventions, factual source summaries, citations, useful links,
   explicit conflicts, metadata, content index, and chronological append-only
   ingest/query/lint log. Use this workspace's `system/schema/llm-wiki.md` as a
   pattern only when available, adapting domain-specific folders to the new vault.
4. Create the agreed folders and initial index/log only in the new target.
   Write compact agent instruction pointers to the shared schema: Codex uses
   `AGENTS.md`, Claude uses `CLAUDE.md`, Gemini uses `GEMINI.md`, Cursor uses its
   project rules. Agent names and files must match; do not generate two Codex
   templates in place of Claude support. Read back the files and verify links.
5. Show the resulting paths, explain ingest/query/lint with one concrete source,
   and complete the requested first ingest using the new schema.

Bundled legacy scaffold scripts and templates are historical aids, not authority
over existing-vault instructions. No optional search tool, browser extension,
plugin, or package installation is required or authorized by initialization alone.
Index navigation is sufficient until scale demonstrates a search need. Preserve
all originals and request explicit authorization for any deletion or move.
