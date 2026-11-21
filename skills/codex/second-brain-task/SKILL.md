---
name: second-brain-task
description: >
  Work the second-brain task queues: the AI action queue and the LSAT U idea
  queue that second-brain-ingest fills from ingested sources. Use for "second
  brain task", "what's in my AI queue", "show my LSAT U ideas", "approve AQ-012",
  "decline that one", "build the next approved item", or "add this to my queue".
  Shows open items, records approvals, builds an approved item, then clears it
  from the queue and records it on its source page.
allowed-tools: Bash Read Write Edit Glob Grep
---

# Work the queues of things your sources say to do

Ingest finds ideas worth acting on. This skill is where they wait and where they
get done. Each queue item points to the source summary it came from, and each
summary points to the archived original, so every task can be traced to its
evidence. Read `system/schema/llm-wiki.md` from the vault root first.

## The two queues

| Queue | File | Holds | IDs |
|---|---|---|---|
| AI action queue | `references/ai-workspace/action-queue.md` | Skills, repos, automations, settings, workflow changes, product updates to verify, prompts to save | `AQ-001`, `AQ-002`, ... |
| LSAT U idea queue | `wiki/lsatu-idea-queue.md` | Platform features, drill formats, teaching methods to adopt, outside tools or platforms to try | `LQ-001`, `LQ-002`, ... |

LSAT teaching knowledge itself is compiled into `corpus/` by ingest; the LSAT U
queue only holds what someone has to build or do. `wiki/tasks.md` stays for work
Joshua has agreed to; an item there may cite a queue item, but the queues are
never copied into it.

A queue holds open work only. Finished and declined items are removed. Their
record lives on the source summary and in `wiki/log.md`.

## Item format

Every item uses exactly this shape. Ingest writes new items in it; this skill
reads and updates them.

```markdown
### AQ-012 · Mine 30 days of session logs for skill ideas
- Type: workflow change
- From: [Chase AI's Claude OS](../../wiki/sources/jev-claude-os-chase-ai.md) at 12:04
- Value: finds the tasks done by hand every week, so new skills target real work.
- Already here: level-up reads decisions and the log, not session history.
- Steps:
  1. Add a session-history input to level-up's "Inputs to read first".
  2. Sync the loaded copies.
  3. Check: the next level-up run lists candidates with transcript evidence.
- Effort: small · Status: new (2026-10-14)
```

- **Type:** skill, repo, automation, setting, workflow change, product update to
  verify, prompt, or (LSAT U queue) platform feature, drill format, teaching
  method, outside tool.
- **From:** a relative link from the queue file to the source summary in
  `wiki/sources/`, plus a timestamp or section. Several sources proposing the
  same thing share one item with several links.
- **Value:** one sentence on what it gets Joshua.
- **Already here:** what the vault has today, checked on disk, so the steps start
  from the real state.
- **Steps:** numbered, concrete enough to follow without rereading the source.
  The last step is always `Check:` with the evidence that proves it worked.
- **Status:** `new` or `approved`, with the date it was set.

The file header carries `Next ID:`. IDs are never reused. Sections are
`## Approved` then `## New`, newest first inside each.

## What this skill does

1. **Show.** Read the requested queue (both if unspecified). Report approved items
   first, then new ones: ID, title, type, effort, source. Give counts. Do not load
   the source summaries unless an item is opened.
2. **Approve or decline.** On Joshua's word, move an item to `## Approved` with
   today's date, or decline it: remove it from the queue and add
   `Declined YYYY-MM-DD: <item title>. <reason>` under a `## Queue record` section
   at the end of its source summary.
3. **Build.** Only an approved item, or one Joshua names with "build" or "do".
   Re-check `Already here` on disk, then follow the steps under the vault's
   existing rules (skill copies for both runtimes, `skills/PARITY.md`, Lovable
   credit confirmation, send only on "send"). Run the `Check:` step and report
   what came out. If the check fails, say so and leave the item in the queue
   with a dated note under it.
4. **Clear.** After a passing check, remove the item from the queue and add
   `Done YYYY-MM-DD: <item title>. <what changed, with file links>` under
   `## Queue record` on each source summary it links. Append a `system` entry to
   `wiki/log.md` naming the item ID, the files changed and the check.
5. **Add by hand.** Joshua can add an item without ingesting a source. Use the
   same format; `From:` names where the idea came from, or "Joshua".

## Rules

- Never build from the `## New` section without Joshua's word for that item.
- One item per build unless Joshua names several.
- Edit queue files in place, preserving their line endings. Never delete a queue
  file. Removing a finished line from a queue is the intended clearing.
- The queues are not a decision log. A choice that locks direction also goes to
  `decisions/log.md`.
- Ingest is the only automatic writer; it adds items, never changes status.

Sources enter through `second-brain-ingest`. Questions use `second-brain-query`.
Health checks use `second-brain-lint`.
