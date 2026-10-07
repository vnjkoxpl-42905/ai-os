# Assign guided drills through the local MCP

Use this branch for guided-drill selection, difficulty matching, or a multi-day schedule. Other LSAT U operations keep their existing global skill route.

## Before executing

1. Reuse the student's verified identity, dates and teaching goal from this chat. One explicitly named student is authorized; reads and preview do not need approval. Retrieve student context only when the teaching goal is unclear. Check live existing assignments through batch preview rather than repeatedly reading every ledger or transcript.
2. Search `search_guided_drills` on the existing local `lsat-u-lessons` MCP. Send a short query and return a small candidate list. The generated [catalog](../../../../references/lsatu-guided-drill-catalog.md) maps every drill; its JSON holds complete cards and filters. Refresh with `node system/scripts/refresh-guided-drill-catalog.mjs` when the snapshot is old, content changed, or no suitable candidate appears. Assignment preflight always reads live records and the deployed merged question bank.
3. Prefer existing drills. Match the actual eligible pool and difficulty ceiling, not only “Easier,” “Medium,” or a catalog level. Beginner is 1–3; intermediate is 2–4; advanced is 3–5. With sufficient in-band questions the app selects only that band. Example: a native 3–4 drill at beginner becomes difficulty 3 only. Preview refuses insufficient in-band pools and any selectable question above `max_difficulty`.
4. Build one structured plan containing the exact student and all dates/slugs. Keep the native question count unless Joshua specifies a shorter drill. A count override does not rewrite the existing instruction card. Exact catalog pins override level/count, so preview verifies their actual content. Pool drills redraw on reattempt and can overlap other drills; do not promise unique questions across days.
5. Run `preview_guided_drill_batch` once. Completion criterion: every item resolves to the intended student, published content, enough eligible questions, correct effective difficulty/count, valid unlock/due dates, and either a new assignment or a matching existing one. Preflight all entries before any write. Use one writer at a time against the operational checkout.

## Execute and verify

Call `assign_guided_drill_batch` once with the same plan. It syncs the pinned operational checkout once, signs in once, resolves the student once, reads the catalog and deployed bank once, and calls the app's own `assignWork()` serially. It verifies source rows, Classroom visibility, local unlock/due dates, and bell count. Each new assignment retains normal inbox, bell and email notification behavior.

A repeat returns matching existing rows without notifying again. Conflicting existing content, unexpected assignment pins, duplicates, or ambiguous identity fail explicitly. Partial failures preserve completed assignment IDs and notification results. Inspect uncertain state before retrying. A failed notification channel does not justify reassignment. Email OK is platform send acceptance, not independently verified receipt. Headless verification is not a browser runner launch.

New tools may need a fresh chat/MCP connection before appearing in the model's tool list. Immediate fallback uses the same local MCP, without a browser:

```powershell
node system/scripts/lsatu-mcp-call.mjs preview_guided_drill_batch --file students/<student>/assignments/<plan>.json
node system/scripts/lsatu-mcp-call.mjs assign_guided_drill_batch --file students/<student>/assignments/<plan>.json
```

Plan shape:

```json
{
  "id": "student-conditionals-YYYY-MM-DD",
  "student": "Exact platform name",
  "assignments": [
    {
      "drill": "exact-existing-slug",
      "schedule": "YYYY-MM-DD",
      "due": "YYYY-MM-DD",
      "level": "beginner",
      "max_difficulty": 3
    }
  ]
}
```

Store plans and result evidence under the student's `assignments/` folder. Log assignments and notification sends once; update the session handoff. Keep Friday/day-off dates and session-day exclusions explicit.

## After executing

Report assigned work, effective difficulty/count, dates and material notification limitations. Use returned metrics to review the pathway: repeated setup, broad retrieval, custom content that an existing drill could cover, or duplicate verification. Fix deterministic mistakes in the tool; add only a short new instruction for a judgment rule. Prefer one shared batch operation and a catalog pointer over more per-day commands or copied drill metadata.

## Authored content exception

Only when existing drills cannot meet the requested content, use the existing `--guided-spec <absolute JSON path>` alongside `--drill <matching slug>`. This authored-spec path currently validates conditional Must Be True questions; it is not the general conditionals catalog path. Use the app's assignment function, then `verify-guided-spec.mjs`. Do not hand-write assignment rows or claim browser QA. No Lovable/app deployment is needed for these local content operations.
