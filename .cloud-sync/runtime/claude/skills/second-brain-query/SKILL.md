---
name: second-brain-query
description: >
  Answer questions using saved wiki knowledge, such as "what do we know
  about X", "search my wiki", or "compare these ideas". Read the index first,
  cite evidence, and save valuable new synthesis under the vault schema.
allowed-tools: Bash Read Write Edit Glob Grep
---

# Resolve the current vault workflow

This existing user-level entrypoint is a compatibility dispatcher, not an
independent knowledge or student-intake pipeline. Find the target vault from the
current workspace and its applicable instructions. Do not assume a saved machine
path, initialize a new vault, or use another project's records.

Read its `system/schema/llm-wiki.md`. For this runtime, read and follow the vault's
`.claude/skills/second-brain-query/SKILL.md` and its referenced resources.
If that project entrypoint is unavailable, use its `skills/claude/second-brain-query/SKILL.md`
catalog copy. Resolve all sibling skill references from that chosen skills root,
not this user-level folder. If the schema or workflow is missing, report the exact
missing route instead of reviving a legacy workflow.

Student/session transcripts use that vault's `transcript-intake`; student-facing
lessons use `post-session-recap`. Public clips and reusable knowledge use `ingest`;
questions use `second-brain-query` and health checks use `second-brain-lint`.
Respect the requested scope and stop conditions in the resolved project skill.
