# Notes and homework package

The post-session note is one part of what goes out after a session; the post-session homework is the other. A proposal covers both. This file says what else goes with it, how to choose it, and how to assign it. It was derived on 2026-11-14 from Sofia Minassian's LSAT U account (2026-10-25 to 2026-11-11) and her session transcripts. The reasons below are inferred from what was assigned and what Joshua promised in each session. They are not his own stated rules. Correct them when he does.

## What Sofia's account shows

| Session | What Joshua promised (Next steps) | What landed on her account |
|---|---|---|
| 2026-10-30 | Finish earlier drills | 3 principle guided drills (intermediate, max difficulty 4, one-day window) and 1 recap note, "Find the Rule Behind the Verdict" |
| 2026-11-01 | Send a note on weak versus strong answer choices; a drill | 2026-11-02: three notes on answer strength (Must Be True, Necessary Assumption), plus drills |
| 2026-11-02 | "More quantitative practice within 30 minutes" | Same day: three quantifier notes and quantifier drills, plus Must Be False sets and Conditional Logic |
| 2026-11-05 | "Additional weakening exercises" | 2026-11-06: three weaken and causal notes, and four weaken or science drills |
| 2026-11-08 | "Method of reasoning and flaw exercises before the end of the day" | Same day: Abstract + Flaw set 1 |
| 2026-11-09 | Joshua prepares questions for the next meeting | Nothing on 2026-11-09 or 2026-11-10. Warm-up notes on 2026-11-11 |

## Decision rules the account supports

1. **Promises set the scope.** Assign what Joshua said he would assign in the session, and nothing he did not. Read the transcript's next steps and the timestamps where he commits to practice. If he promised nothing, propose nothing.
2. **Same-day timing.** The package lands the day of the session, or inside the window he named ("within 30 minutes", "before the end of the day"). A promise carried to the next day is a miss to flag, not a default.
3. **One teaching note per topic.** It carries the session recap. A guided drill already has its own intro, so add a short note beside a drill only when the drill has none or when the note teaches the idea the drill practises (Joshua, 2026-11-14). Notes carry no due date and are assigned immediately once approved.
4. **Homework is guided drills from the library, matched to the note's topic.** Search the library before proposing. Do not invent a drill or pick one from its title alone.
5. **Pace drills, do not drop a block.** Unlock one or two a day and set due dates two to six days after unlock. Sofia's seven drills from 2026-11-02 unlock across 2026-11-01 to 2026-11-05.
6. **Level follows the concept's age.** First contact with a concept: beginner, max difficulty 3, name "First Taste". Review: intermediate, max 4. Weak spot she has already met: Medium, then Harder variants.
7. **No repeats.** Her account has duplicate "Famous Flaws" notes, one archived. Check what she already holds before proposing, and drop anything duplicated.
8. **Recall and Reading Center work is separate.** LR Recall is the "Read, Recall, Colour" activity. RC Recall (RC Training) needs the Reading Center assignment. Use `node system/scripts/lsatu-admin.mjs reading-center "Name"`.

## Procedure

1. Read the transcript's Next steps and every place Joshua offers or promises practice. Make a table: promise, timestamp, status.
2. Read `students/<slug>/homework/already-assigned/index.md` and run `node system/scripts/lsatu-admin.mjs items "<first name>" --all` (the `list_student_classroom_items` MCP tool reads the same data).
3. Resolve identifiers with `search_assignable_work`. A name that returns nothing is not assignable yet; say so.
4. Write the proposal to `students/<slug>/homework/YYYY-MM-DD-homework-proposal.md`: the note set, the drills with level, unlock and due dates, anything dropped as a repeat, anything promised that cannot be assigned. Nothing posts or assigns before Joshua approves.
5. On approval, make one plan file and call `assign_student_work` once (`node system/scripts/lsatu-mcp-call.mjs assign_student_work --file <plan.json>`). Notes use `kind: interactive_note` with an approved HTML file; drills use `kind: guided_drill` with `schedule`, `due`, `level`, `max_difficulty`; activities use `kind: activity`.
6. Use the tool's readback as verification. Then log: `students/<slug>/assignment-log.md`, `wiki/send-ledger.md`, and the row in `wiki/recap-ledger.md`. Check the Notes panel again; it reads the already-assigned index, which rebuilds from `lsatu items`.
7. Report preparation, approval, assignment and posting as four separate states.

## Plan file shape

```json
{
  "id": "<student>-<yyyy-mm-dd>-session-package",
  "student": "<exact email>",
  "student_folder": "students/<slug>",
  "assignments": [
    {"kind":"interactive_note","html_file":"C:/Users/Joshu/dev/ai-os/brainstorms/<dated-folder>/recap.html","title":"<note title>"},
    {"kind":"guided_drill","drill":"<library slug>","schedule":"YYYY-MM-DD","due":"YYYY-MM-DD","level":"intermediate","max_difficulty":4}
  ]
}
```

## Executor gotchas (2026-11-17, Sara Altuwaijri)

- `preview_guided_drill_batch` and `assign_guided_drill_batch` refuse to run while `.lsatu-ops` has tracked edits ("Operational checkout has tracked edits"). Use `assign_student_work` with `kind: guided_drill`; its runtime builds an isolated clean copy and leaves the dirty checkout alone. Do not stash or reset the checkout.
- `assign_student_work` used to refuse an activity when the student's `activity` flag was off ("Student lacks access for activity"). That check was stale: a 2026-10-02 database trigger forces `has_activity_access` false on every access write ("activities and bootcamps are assigned per item"), so the flag cannot be granted and a grant reports Done without sticking. The app opens an assigned activity through an assignment-only gate, so the flag is not needed. The check was removed on 2026-11-17. Do not try to grant the flag; assign the activity.
- Read the drill's catalog row before proposing it. `w2-07-necessary-assumption-first-taste` filters on the Defender feature only, so it practices one of the two assumption kinds, and its card says untimed.
- Posting a revision of a posted lesson used to archive the old copy and send the student a second "New note" message whose first link then pointed at a hidden note (Sara, 2026-11-17: Joshua saw two). Since 2026-11-17 `post-lesson` updates the one live copy in place: same item, same message link, no new message. Pass `--new-version` only when a fresh, notified copy is wanted. The in-place path has not yet been exercised live; check the item after the first real revision.
- Always dry-run a post (`post-lesson ... --dry-run`) and an assignment (`dry_run: true`) before the real call, and verify with a separate read (`lsatu items "Name" --all`).

## Known limits

- The decision rules above rest on one student's account. Check them against a second student before treating them as fixed.
- Sofia meets Joshua almost daily in November. A student on a weekly schedule needs longer windows; scale the pacing.
- Reading Center email delivery was not independently verified when the command was added.
