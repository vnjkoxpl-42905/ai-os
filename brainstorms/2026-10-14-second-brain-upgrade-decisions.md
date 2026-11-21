# Second-brain upgrade decisions: Brainstorm / Discovery Notes
Date: 2026-10-14 · Goal: settle the three open decisions left after the second-brain source review (raw/sources lock, wiki/hot.md size, wiki/index.md size)
Status: complete (Joshua said "go" 2026-10-14; build follows)
Context sources: [adoption ledger](../references/ai-workspace/second-brain-adoptions.md), [vault schema](../system/schema/llm-wiki.md), [wiki/log.md](../wiki/log.md) entries dated 2026-10-14

## Summary / key decisions

Already done before this interview (not up for decision): seven sources ingested, 25 adoptions built into the schema, skills and lint script, all verified. See the ledger.

Decided and built 2026-10-14 (see the wiki/log.md entry "Second-brain decisions built"):
- Q1: Claude hook locks existing files under raw/sources/; PROVENANCE.md and new files allowed.
- Q2: hot.md capped (3 newest session sections plus standing sections); older sections archived; wrapup enforces it.
- Q3: index lists 5 generated capture catalogs instead of 3,831 rows.
- Q4 to Q12: new second-brain-task skill owns an AI action queue and an LSAT U idea queue; ingest adds every actionable item; finished items are removed and recorded on their source page; pickup shows one line of counts; backfilled from AI sources (8 items).
Resume point: none. Remaining flags below.

## Q&A log

### Round 1

Asked Q1 (raw/sources lock), Q2 (hot.md cap), Q3 (index collapse). Recommended 1A 2A 3A.

#### Clarification asked by Joshua (before answering)
- Asked: what is `PROVENANCE.md`; why is the folder `raw/sources/` rather than `sources/`; what do the sources say suits best.
- Answered in chat: PROVENANCE.md is the per-source record card (URL, author, dates, hash). `raw/` is Karpathy's own term ("Raw sources ... immutable"); the vault's `raw/` holds the intake queue, the evidence archive and personal exports, and `wiki/sources/` already holds the summaries, so a bare `sources/` would be ambiguous. Recommendation: keep the names.
- Found while checking: eight loose files sit directly in `raw/` (six clips, a backup zip, a workflow note), outside both `inbox/` and `sources/`. Not acted on.
- Status: Q1 to Q3 answered in Round 3.

#### Clarification asked by Joshua: what happens after ingest when a clip has something to implement
- Asked: is there a to-do or task list that ingested skills/ideas get added to; how does implementing a clipped idea work today, by source type.
- Found (verified on disk 2026-10-14): ingest does not add anything to a task list. Ideas are recorded only inside the source summary (states: source claim, proposed, implemented, deferred per `references/ai-workspace/index.md`). Two lists exist but ingest never writes to them: `references/automation-backlog.md` (ranked automation ideas, read by `level-up`) and `wiki/tasks.md` (agreed work, read by `pickup`, updated by `wrapup`). Implementation happens only when Joshua asks ("implement X from this source").
- Gap: a "proposed" idea in a source summary is easy to forget; nothing collects them.
- New question opened: Q4, below.

### Round 2 (opened by Joshua's clarification)

#### Q4 - Where should "worth implementing" ideas from an ingest go?
- Asked: should ingest collect proposed ideas into one list, and which.
- Recommended: A, one "Ideas to try" section in `references/automation-backlog.md`; ingest appends a row per idea (source link, what it would change, status `proposed`); nothing is built until Joshua picks one; `level-up` and `pickup` show the list.
- Captured (Joshua, 2026-10-14): for AI-related sources (skills, repos, anything that could update his workflow or workspace), ingest "should extract all of those things and organize them in a running markdown file of what needs to be done". Each item: "extract the value, whatever it is, and give very clear instructions on what needs to be done", and "point to the actual source that we've summarized". LSAT-related material "should go into my LSAT corpus and be handled separately". He asked what the best setup is.
- Decision: a running action list for AI sources (supersedes options A/B/C as offered). Exact design opened as Round 3.
- Found: `references/automation-backlog.md` is a July analysis of the tutoring business built from 944 emails, so it is the wrong home; 20 of 26 top-level source summaries are AI-workspace sources (backfill candidates).

### Round 3 - design of the AI action list

Joshua's answer (2026-10-14): "Go with all the recommended, except for question eight." For Q9 and the rest: "I want you to make the ultimate call."

#### Q1 - Lock raw/sources
- Captured: A. PreToolUse hook blocks Edit/Write on existing files under `raw/sources/`, except `PROVENANCE.md`. Claude only; `--evidence` remains the cross-runtime check.
#### Q2 - wiki/hot.md
- Captured: A. Keep the newest sections (about 600 words), archive older sections to a dated file after confirming each is in `wiki/log.md`, `wrapup` enforces the cap.
#### Q3 - wiki/index.md
- Captured: A. Generate one hub per Karpathy capture folder (5), list the hubs instead of 3,831 rows; schema rule becomes "every page reachable from the catalog".
#### Q5 - What counts as an item
- Captured: A. Anything actionable (skill, repo, workflow change, setting, product update to verify, prompt). Things already in place are noted in the source summary as "already have", not queued.
#### Q6 - Who moves items
- Captured: A. Ingest only adds items; Claude builds an item when Joshua approves it.
#### Q7 - Backfill
- Captured: A. Backfill from all 20 AI source summaries; items already built enter as done.
#### Q8 - Where the queue is seen
- Captured: not answered. Joshua asked what `level-up` and `pickup` do. Explained in chat. Found: `pickup` is "scoped to LSAT U work only", which bears on showing the AI queue there. Re-asked in Round 4.
#### Q9 - LSAT actionable ideas
- Captured: Joshua delegated the call: during ingest, Claude analyzes each item and decides where it goes.
- Claude's call (recommendation, accepted by delegation): teaching knowledge keeps compiling into `corpus/`. Actionable LSAT items (an LSAT U platform feature, a drill format, an outside tool or platform to try) go to a separate running list, `wiki/lsatu-idea-queue.md`, same item format as the AI queue, each pointing to its source summary and corpus page. No existing product-ideas page was found (searched wiki, references, brainstorms, context); `wiki/tasks.md` stays for agreed work only.

### Round 4
#### Q8 (re-asked) - where the queues are shown
- Recommended (superseded, see below): `level-up` reads both queues to pick its candidate; `pickup` shows one line with counts of new and approved items in the LSAT U queue only (it is scoped to LSAT U); the AI queue is shown when asked or by `level-up`.
- Captured (Joshua, 2026-10-14): confused why `level-up` is involved; level-up "is just to see what I've done during the week" (the Three Ms review). Pickup "would make more sense", but "does pick up not have another job as well that's separate from this?" He does not want unrelated jobs blended.
- Revised recommendation: no blending. Neither skill reads the queues. The queues are standalone files; ingest writes them, and Joshua sees them by asking ("what's in my AI queue?"), handled by reading the file directly. Re-asked as Q8b.
- Note: "girls' movement" in the dictation was read as "the Three Ms" (level-up's framework). Not confirmed.
#### Q8b - see the queues on request only?
- Captured (Joshua, 2026-10-14): wants a new skill, `second-brain-task`, named alongside `second-brain-ingest`, `-query` and `-lint`. "It should point to the queues and the queue should point to the source we ingested, and it should keep all of it and clear the queue as we go." On pickup: "/pickup should be able to access it", but open to keeping it separate if Claude thinks so.
- Decision: new skill `second-brain-task` owns both queues (supersedes Q8b as offered).
- Interpretation (to confirm in Round 5): "clear the queue as we go" = finished or declined items leave the open queue but are kept, with date and evidence, in a done file.

### Round 5
#### Q10 - What pickup does with the queues
- Recommended: one line only, e.g. "Queues: AI 4 new, 1 approved; LSAT U 2 new. Say 'second-brain-task' to work them." Pickup reads counts; second-brain-task does the work.
- Captured: yes ("go", 2026-10-14).
#### Q11 - Where finished items are kept
- Recommended (superseded): a companion done file per queue (`action-queue-done.md`, `lsatu-idea-queue-done.md`), newest first, each item with date, what changed and proof. The open queue only ever shows new and approved items.
- Captured (Joshua, 2026-10-14): unclear on the done-file idea. His meaning: "the queue should be cleared as we go through the second-brain-task; once we've completed the AI task it should be cleared from the queue."
- Revised recommendation: no done files. When `second-brain-task` finishes an item, it removes it from the queue and writes one "Done" line on the item's source summary (date, what changed). The log entry records the build. The queue holds only open work.
- Captured: yes ("go", 2026-10-14). Applied to backfill too: only open items enter the queue; already-built items are not queued.

#### Restatement by Joshua (2026-10-14)
- Captured: when he ingests an AI source, `second-brain-ingest` does the normal ingest as today, and in addition adds every skill, automation, setup step or other "how to do" item from that source to the `second-brain-task` list. Matches the agreed design. His message ended with "and then", possibly unfinished.
#### Q12 - What second-brain-task can do
- Recommended: show the queues; approve or decline items; build an approved item (follow its steps, verify, then move it to done); add an item by hand. Ingest adds items using the format the skill defines.
- Captured: yes ("go", 2026-10-14).
#### Confirm shared understanding before building
- Captured: confirmed. Joshua replied "go" after being asked whether "and then" had more.

## Open flags (pending input)
- ~~Q1 raw/sources hook~~ decided A (Round 3)
- ~~Q2 wiki/hot.md cap~~ decided A (Round 3)
- ~~Q3 wiki/index.md collapse~~ decided A (Round 3)
- Q8 where the queues are shown -> Joshua
- Confirmation to build -> Joshua
- Eight loose files directly in `raw/` (six clips, a backup zip, a workflow note) -> Joshua, after this interview
