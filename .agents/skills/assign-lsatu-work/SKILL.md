---
name: assign-lsatu-work
description: Assign approved LSAT U work headlessly through one mixed MCP batch with live preflight, idempotent reuse and readback. Covers guided drills, activities, standalone drills/bootcamps and HTML notes; legacy CLI handles other account operations.
---

# Assign LSAT U work

For assignments, use the project's authoritative [one-call batch workflow](../../../references/lsatu-work-batch.md). Search `search_assignable_work` only for missing identifiers, then call `assign_student_work` once with all approved items. Preflight, assignment, verification and generated evidence are included. Do not require a separate preview or another readback after a verified result.

Reuse the student, dates and approved content already established in the conversation. An assignment request authorizes the requested student's work and normal assignment notifications. It does not authorize unrelated messages, other students, or unapproved note content.

The immediate fallback when new MCP tools are absent is `node system/scripts/lsatu-mcp-call.mjs assign_student_work --file <plan.json>`. It calls the same local MCP. Do not create a per-student shell transport, modify shared operational edits, or hand-write assignment rows.

Guided-only selection details remain in [the guided reference](references/guided-drill-workflow.md), subordinate to the batch workflow. Other account operations, progress and messages retain the full global skill at `C:/Users/Joshu/.agents/skills/assign-lsatu-work/SKILL.md`. On Windows use the supported Node entry point; never rely on the default WSL bash.
