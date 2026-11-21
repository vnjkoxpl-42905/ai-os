---
title: Homework proposal for Oreoluwa, 2026-11-11 session
student: ore
session: 2026-11-11
status: assigned 2026-11-14 (Joshua approved the proposal as written)
internal: true
created: 2026-11-14
---

# Homework proposal · 2026-11-11 session

Internal only. Nothing here is assigned or posted. Joshua approves before anything goes to LSAT U.

Source: [transcript](../transcript-downloads/2026-11-11-ore-notes-by-gemini.md), blocks 00:26:28, 00:49:02 and 00:49:51 to 00:50:51.
Checked against: [already assigned](already-assigned/index.md) (refreshed 2026-11-14) and a live `lsatu-admin.mjs items "Oreoluwa" --all` read on 2026-11-14 (14 items, latest added 2026-10-26). Drills resolved with `search_assignable_work` on 2026-11-14.

## What Joshua promised, and what is on her account

| Promise | Where | On her account today |
|---|---|---|
| Send the list of fallacies | 00:26:28, 00:28:57, 00:49:02 | No. The reference note in this package is that list. |
| "Assign you that": flaw questions worked with the fallacy list beside them | 00:49:02 to 00:49:51 | No flaw item of any kind. |
| Send a complete note on what was discussed, with the study instructions | 00:50:51 | No. The recap note in this package is that note. |
| Ore: 1 or 2 Reading Comprehension passages every other day | 00:49:51 to 00:50:51 | Not covered. Her five "Read, Recall, Colour" items are Logical Reasoning sections (see below). |

The promises were made on 2026-11-11 and nothing has reached her account in the three days since. Flagging it as a miss, not a default.

## Proposed tasks (outside the note)

Dates assume Joshua approves by 2026-11-15. Sunday stays free, as in her 2026-10-25 package. If approval is later, shift every date by the same amount.

| # | Drill (library slug) | Level | Questions | Unlock | Due | Why it fits |
|---|---|---|---|---|---|---|
| 1 | **Flaw - First Taste** (`w1-07-flaw-first-taste`) | beginner, difficulty 1 to 3 | 7 | Mon 2026-11-16 | Thu 2026-11-19 | First contact with flaw drills. Catalog tags: Flaw, Famous Flaws. She works it with the reference beside her, as Joshua asked. |
| 2 | **Famous Flaw (Easier) Set 1** (`w4-08-famous-flaw-easier-set-1`) | beginner, difficulty 1 to 3 | 12 | Wed 2026-11-18 | Sat 2026-11-21 | More reps on the four flaws taught. Same tags as task 1. |
| 3 | **Abstract + Flaw (set 1)** (`w2-02-abstract-flaw-set-1`) | intermediate, difficulty 2 to 4 | 10 | Fri 2026-11-20 | Tue 2026-11-24 | Her named sticking point was abstract answer-choice language (A versus E). Catalog tags: Abstract Answers, Famous Flaws, Flaw. |

If Joshua wants a lighter week, drop task 3 first.

## Dropped because already assigned

- **Anything on flaw, fallacies or causation.** Nothing of that kind was on her account, so no flaw item is dropped. The 2026-10-26 note "Keep the evidence separate" covers causal scope in assumption questions; it overlaps the causal part of this session only lightly, so it stays and is not repeated.

## Open item for Joshua: Reading Comprehension

Joshua asked her to read 1 or 2 RC passages every other day. **That is not covered by anything on her account.** An earlier draft of this proposal dropped it as already assigned. That was wrong: the Read, Recall, Colour items she holds (PT21 Section 3, PT1 Section 3, PT102 Section 3, PT101 Section 2, and the open section library item) are Logical Reasoning sections. LR Recall is the Read, Recall, Colour activity; RC Recall has no Classroom item and runs through the Reading Center (`node system/scripts/lsatu-admin.mjs reading-center "Ore"`), as with Zeina on 2026-11-13. Source for her passages is undecided, so the recap note says only "Any Reading Comprehension passage works for this." Joshua's call: reading-center assignment, or leave it as her own task.

## Not proposed, and why

- **Fallacy Homework worksheet** (`corpus/Curriculum/Flaw and Famous Flaws/Homework/Fallacy Homework.md`). It is Joshua's paper worksheet: name the fallacy in the stimulus and in every answer choice, Stage 1 Set 1.1 is five PrepTest questions. It matches "practice with the list beside you" closely, but it is not a platform item and Joshua did not name it in the session. His call.
- **Negation Station and Conditional Rephrase.** The rules say these follow necessary-assumption or weak-conditional work. This session was flaw recognition, and he promised nothing of the kind.

## Flags for Joshua

- **Three items from her 2026-10-25 package still read "assigned" past their dates:** PT104.S1 (due 2026-10-27), The Core Connection (due 2026-10-30) and Read, Recall, Colour PT104 Section 1 (due 2026-11-01). If those are still open, three new drills on top of them may be too much. I did not change them.
- **`already-assigned/index.md` lists 11 items; the live read returns 14.** The three extra are completed (the Intro to LR bootcamp module and two timed Logical Reasoning sections from 2026-08-30). Not a problem for this proposal.
- **Three study instructions in the note are mine, not said in the session:** write the reason for each cut choice, write the flaw name next to the answer, and log misses by flaw. The first two echo his "keep the list beside you"; the log is from the earlier Famous Flaws reference note. Cut them if he does not want them.
- **The Famous Flaws note's "What to do next" names these three drills.** If you change the homework, the note's first step must change with it.

## Plan file (not run)

```json
{
  "id": "ore-2026-11-11-session-package",
  "student": "oreoluwavjames@gmail.com",
  "student_folder": "students/ore",
  "assignments": [
    {"kind":"interactive_note","html_file":"C:/Users/Joshu/dev/ai-os/brainstorms/2026-11-11-ore-post-session/famous-flaws-full/famous-flaws-ore.html","title":"Famous Flaws"},
    {"kind":"interactive_note","html_file":"C:/Users/Joshu/dev/ai-os/brainstorms/2026-11-11-ore-post-session/before-you-start-flaw-first-taste.html","title":"Before you start: Flaw - First Taste"},
    {"kind":"guided_drill","drill":"w1-07-flaw-first-taste","schedule":"2026-11-16","due":"2026-11-19","level":"beginner","max_difficulty":3},
    {"kind":"guided_drill","drill":"w4-08-famous-flaw-easier-set-1","schedule":"2026-11-18","due":"2026-11-21","level":"beginner","max_difficulty":3},
    {"kind":"guided_drill","drill":"w2-02-abstract-flaw-set-1","schedule":"2026-11-20","due":"2026-11-24","level":"intermediate","max_difficulty":4}
  ]
}
```

Her exact email comes from `ore.md`. Not run through `assign_student_work` and not dry-run through `post-lesson`.

## States

| State | Status |
|---|---|
| Preparation | Done. Two notes (Famous Flaws, Before you start) built and checked, and this proposal exists. |
| Approval | Not given. |
| Assignment | Nothing assigned. |
| Posting | Nothing posted. |
