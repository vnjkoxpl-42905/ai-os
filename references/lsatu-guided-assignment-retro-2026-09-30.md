# Guided assignment now uses a catalog and one batch

Joshua requested faster guided assignment after the first Yahunatan run. The [ask-matt](../../../.agents/skills/ask-matt/SKILL.md) router points this work toward an environment retrospective: fix navigation and tooling rather than rely on remembering more details.

## Before the second execution

- Repeated per-day commands were syncing the operational checkout, starting vite-node, signing in and resolving identity each time. The batch now performs each once and preflights all entries before the first write.
- Existing conditional guided sets already fit the new request. The [catalog](lsatu-guided-drill-catalog.md) maps all 119 drills, with actual deployed pool counts, native bands, level eligibility, complete cards and exact-pin summaries. New catalog content is an exception.
- Local-copy disagreements and hand-written schema guesses caused rework. Selection uses the deployed merged bank with the app's own question-type normalizer. Source rows still come from the app's own assignWork; the batch verifies actual deployed schema fields.
- The local MCP already existed. Extended it with search_guided_drills, preview_guided_drill_batch and assign_guided_drill_batch; no hosted deployment, browser or new credentials.

## What the second execution verified

[One plan](../students/yahunatan-zetvy/assignments/2026-09-30-additional-conditional-plan.json) assigned three existing conditional drills. All source rows, effective bands, dates, Classroom visibility and bell counts passed. Inbox/bell/email returned OK. The runner took 15,296 ms with one sign-in and student lookup; checkout synchronization is outside that measurement. The first run has no comparable recorded end-to-end baseline, so no percentage speedup is claimed.

Repeating the same MCP assignment returned the same IDs, zero writes and no notifications. A live preview rejected a difficulty-3 pool under a ceiling of 2. [Result evidence](../students/yahunatan-zetvy/assignments/2026-09-30-additional-conditional-result.json) records exact IDs and limitations.

## Improvements made after execution

- Search now prioritizes titles and ordinary reusable pool drills, returns small results, accepts a level plus minimum/maximum difficulty, and treats exact pins separately because pins ignore level/count.
- Catalog refresh builds filter sets once per drill, rather than once per question. Snapshot metadata includes catalog/bank hashes and normalization-source commit.
- Partial failures preserve assignment IDs and channel outcomes. Reuse checks reject unexpected assignment pins and conflicting unlock/due dates.
- The [project skill](../.agents/skills/assign-lsatu-work/SKILL.md) now routes routine guided schedules to a short local recipe, bypassing the long global reference. Codex activation and both runtime catalog copies match.

Use one writer per operational checkout. The MCP serializes calls within its process; cross-process concurrent writers are not supported. New tool names need a fresh MCP connection to appear in a chat's tool list; lsatu-mcp-call.mjs invokes the same server immediately. Independent email receipt and student-session runner launch remain unverified. Tasks status, app code and deployment are outside this operation.
