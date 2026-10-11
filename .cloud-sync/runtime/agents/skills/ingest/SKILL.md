---
name: ingest
description: >
  The single front door for adding sources to the current knowledge base. Use
  for "ingest this", "process this source", "file these notes", "add this to
  my second brain", "ingest the latest clips", or a supplied document meant
  to become saved knowledge. Finds the input, checks content hashes, preserves
  provenance, and compiles it into linked wiki pages. Session write-ups and
  student-facing post-session recaps belong to post-session-recap. Student and
  consultation session transcripts belong to transcript-intake, not this pipeline.
allowed-tools: Bash Read Write Edit Glob Grep
---


## Local execution contract (2026-10-10)

Use current project ingest as single durable intake route. Student/session transcript routing uses current transcript-intake/post-session-recap, not absent lsat-session-lesson. Preserve immutable sources/hashes and current wiki/domain schema.

## Workflow

# Resolve the current vault workflow

This existing user-level entrypoint is a compatibility dispatcher, not an
independent knowledge or student-intake pipeline. Find the target vault from the
current workspace and its applicable instructions. Do not assume a saved machine
path, initialize a new vault, or use another project's records.

Read its `system/schema/llm-wiki.md`. For this runtime, read and follow the vault's
`.agents/skills/ingest/SKILL.md` and its referenced resources.
If that project entrypoint is unavailable, use its `skills/codex/ingest/SKILL.md`
catalog copy. Resolve all sibling skill references from that chosen skills root,
not this user-level folder. If the schema or workflow is missing, report the exact
missing route instead of reviving a legacy workflow.

Student/session transcripts use that vault's `transcript-intake`; student-facing
lessons use `post-session-recap`. Public clips and reusable knowledge use `ingest`;
questions use `second-brain-query` and health checks use `second-brain-lint`.
Respect the requested scope and stop conditions in the resolved project skill.
