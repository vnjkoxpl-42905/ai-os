---
name: second-brain-ingest
description: >
  Compatibility name for ingest. When explicitly invoked, run the current
  vault ingest workflow; it does not own a competing source-processing pipeline.
allowed-tools: Bash Read Write Edit Glob Grep
---

# Use the single ingest workflow

## Resolve the vault and schema first

Find the vault root from the current workspace and its nearest instruction files.
Read `system/schema/llm-wiki.md` relative to that root. It is the authority for
folder conventions, page metadata, provenance, index, log, and ingest/query/lint
workflows. Do not assume a saved Windows or Mac path. If no schema exists in the
target vault, report that gap before changing its structure; never initialize a
second vault to solve a request about an existing one.

Resolve the current vault, then read its active `ingest/SKILL.md` and follow it
through completion, including `ingest/references/wiki-compilation.md`.
If only catalog copies exist, use the matching runtime's `skills/<runtime>/ingest/`
workflow. Existing global activation may use its sibling `ingest/` only after
resolving the target vault and schema. If that dependency is missing, report the
missing workflow rather than improvising a parallel intake procedure.

Public activation phrases belong to `ingest`: "ingest this", "add this to my
second brain", "file these notes", and "process this source". This old explicit
name remains compatible without asking the user to invoke another skill.
