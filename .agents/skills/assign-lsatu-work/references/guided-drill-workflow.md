# Guided-drill selection for the unified batch

Use the authoritative [one-call workflow](../../../../references/lsatu-work-batch.md). Normal delivery is one `assign_student_work` call that preflights every item, assigns serially, verifies and saves generated evidence. A separate preview is optional. Existing guided-only tool names are compatibility routes to the same engine, not an extra required stage.

## Select without rebuilding content

1. Reuse the exact student, teaching goal, dates and approvals established in the conversation. One student's assignment request authorizes that work and its normal app notifications, not unrelated messages or other students.
2. Prefer live `search_assignable_work` for current content and renamed activities. `search_guided_drills` and the generated `references/lsatu-guided-drill-catalog.md` can narrow candidates by difficulty/pool metadata, but their snapshot is not live authority. The unified engine rechecks published rows and the deployed bank. Routine mixed work does not need a manual catalog refresh.
3. Match the actual eligible pool, not the word Easier or the catalog level. Beginner is 1-3, intermediate 2-4 and advanced 3-5. The engine rejects insufficient in-band pools or any selectable question above `max_difficulty`. Pinned content is validated directly and its pins override level/count selection.
4. Keep native counts unless Joshua asks otherwise. A count override does not rewrite the instruction card. Pool reattempts redraw and can overlap other work; do not promise unique questions across days.
5. Put all approved guided drills and companion work/notes in the same plan. Each guided entry includes `kind: guided_drill`, exact slug, schedule, due and any requested level/ceiling. Respect stated exclusions and session days. Do not invent a larger workload.

## Execute once

Call `assign_student_work` after authorization. Its internal preflight validates every entry before any write. Reuse matching existing rows without another notification. Stop on ambiguous/conflicting existing content. Partial results preserve saved IDs; an email failure does not justify reassignment. Email OK means platform acceptance, not independently confirmed receipt.

Use `dry_run: true` only for an optional preview or unresolved plan. Use `verify_existing: true` for a mutation-free audit that refuses any missing/changed item. Neither mode authorizes a later write.

If the chat has older MCP definitions, call the same new MCP immediately:

```powershell
node system/scripts/lsatu-mcp-call.mjs assign_student_work --file students/<student>/assignments/<plan>.json
```

```json
{
  "id":"student-conditionals-YYYY-MM-DD",
  "student":"Exact platform email",
  "student_folder":"students/<existing-student-folder>",
  "assignments":[
    {"kind":"guided_drill","drill":"exact-published-slug","schedule":"YYYY-MM-DD","due":"YYYY-MM-DD","level":"beginner","max_difficulty":3}
  ]
}
```

The generated `audit_file` is the machine delivery evidence. Do not create another student-specific transport or repeat successful operational checks. Add relevant human context to the existing ledger rather than copying the whole result across several documents.

## Authored content exception

Only when no existing drill meets the request, use the existing `--guided-spec` route documented by the global skill. It currently validates authored conditional Must Be True content, not arbitrary question types. Prefer existing published drills; do not hand-write assignment rows or claim browser QA. No Lovable deployment is needed for normal assignment operations.
