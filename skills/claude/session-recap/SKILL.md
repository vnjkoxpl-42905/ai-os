---
name: session-recap
description: Find, verify, and file an LSAT tutoring-session transcript and its student record. Use whenever Joshua mentions a student's session, Gemini notes, or a transcript, including recap intake. For "make a recap," "session notes," or any student-facing write-up, also activate lsat-session-lesson; that skill owns the lecture lesson and interactive preview. Drafts by default; post or assign only when Joshua explicitly asks.
---

# Session recap

For a request to make or improve a student-facing recap, note, or lesson from a session, use `lsat-session-lesson` for the teaching content and this skill for transcript intake, assignment accuracy, and filing. This handoff applies even when Joshua simply says “make a recap” or names a student and says “session.” A request only to find or inspect a transcript stops at the narrower task.

After every session Joshua wants a durable set of lecture notes. The student should be
able to return several days later, understand the lesson without remembering a specific
question, and apply the method to new work. It is teaching content, not an email or a
session summary.

Read `skills/reference/session-recap-quality-reference.md` before drafting. Its Sofia
note is the quality bar for depth, hierarchy, nuance, and practical usefulness. Copy the
method, not the conditional-logic headings.

Draft and file the note by default. If Joshua explicitly says to post, assign, publish,
or send it to the student, complete that as a separate LSAT U platform action after the
draft is ready and verify what landed. Never infer posting permission from a request to
write a note.

## 1. Get the transcript on disk first

Transcripts come from Google Meet's Gemini notes. The calendar event carries the Drive
doc as an attachment; some sessions have the doc in Drive but never got it attached.
Check both.

```bash
# events in the window (guest email is the join key, never the event title)
gws calendar events list --params '{"calendarId":"primary","timeMin":"YYYY-MM-DDT00:00:00Z","timeMax":"YYYY-MM-DDT00:00:00Z","singleEvents":true,"orderBy":"startTime","maxResults":100}' --format json

# docs Gemini wrote in the window, attached or not ("Meeting started ..." = untitled event)
gws drive files list --params '{"q":"name contains '"'"'Notes by Gemini'"'"' and modifiedTime > '"'"'YYYY-MM-DDT00:00:00'"'"'","fields":"files(id,name,createdTime)","orderBy":"createdTime desc","pageSize":50}' --format json

# export as plain text (NOT text/markdown: that build is 10x larger and escapes everything)
gws drive files export --params '{"fileId":"<id>","mimeType":"text/plain"}' -o <scratch>/<name>.txt
```

The Drive result can include Markdown copies uploaded by an earlier intake. Count native
Google Docs as source transcripts and use the file ID to deduplicate. Do not count an
uploaded `YYYY-MM-DD-<slug>-notes-by-gemini.md` copy as another session. Reconcile the
full week against Calendar before exporting so unattached docs and events with no doc
both remain visible in the report.

File to `students/<slug>/transcript-downloads/YYYY-MM-DD-<slug>-notes-by-gemini.md`.
Resolve the person with `students/_aliases.md`; for a "Meeting started" doc, count
speaker labels in the transcript (`grep -o -E "^[A-Z][a-z]+( [A-Z][a-z]+)?:" | sort | uniq -c`).
Consultations and people without a folder go to `students/_other-sessions/`.
**Never create a student folder without asking.** Skip anything already on disk.

The Google Classroom calendars (`c_classroom...`) have been empty since 2026; the
primary calendar holds every session.

## 2. Read the whole transcript, not the Gemini summary

The Gemini "Quick notes" flatten what he said. Read the transcript section. It is 40
to 90 KB; that is the cost of a recap that is true.

Extract:

- the governing concept and distinctions Joshua taught;
- the student's actual confusion or decision point;
- the reasoning procedure, including why each step works;
- legal and illegal moves, edge cases, diagnostic checks, and shortcuts;
- examples that can stand alone outside the original question; and
- the exact practice and follow-ups that were assigned.

Do not write a play-by-play of answer choices. A detail from a specific question belongs
only when it demonstrates a reusable move. If the explanation needs more support, search
Joshua's corpus first. Use an authoritative outside source only when Joshua points to it
or the corpus cannot resolve the concept. Keep source research outside the student note.
The session transcript remains the authority for what happened and what was assigned.

## 3. Write the recap

Path: `students/<slug>/recaps/YYYY-MM-DD-recap.md`. One file per session. Primary
record: never regenerate over an existing one; a redo gets a dated correction section.

```markdown
---
title: Recap · <Student> · YYYY-MM-DD
type: recap
record_kind: primary
student: <slug>
session_date: YYYY-MM-DD
source: transcript-downloads/YYYY-MM-DD-<slug>-notes-by-gemini.md
status: draft
posted: false
posted_at:
---

# <Concept the student needs>

<Open directly with the governing distinction or decision. One short orientation
paragraph. No greeting, sign-off, praise, generic scene-setting, "Today...", or recap of
which answers were correct.>

## <A descriptive header that teaches the first part of the method>

<Define the idea before applying it. Build a reusable reference with the combination of
short explanation, numbered steps, a compact table, or a spaced example that best fits
the material.>

## <The next conceptual move>

<Explain why it works, how to recognize when to use it, what does not follow, and how
the student can check the move. Add boundary cases or common traps when they mattered in
the session.>

## <A repeatable process>

1. <A decision the student can actually make.>
2. <The next observable check.>
3. <How to verify the inference or reject the trap.>

## Before next session

- [ ] <What was actually assigned, as the student would recognise it.>
- [ ] <Only what the transcript supports. No invented drills.>

---

## Notes for me (not posted)

- **Weak spots:** <tags>
- **Follow-ups on my side:** <things Joshua promised: send materials, assign a drill, schedule>
- **Watch:** <a teaching judgment worth carrying into teaching-notes.md if it repeats>
```

Everything above the `---` rule is the student note and must stand alone when pasted.
Everything below is admin-only.

The headings above are scaffolding, not a mandatory outline. Organize around the lesson's
logic. Use enough depth to teach the method fully, but remove any section that does not
help the student use it.

## Voice rules (from `wiki/teaching-voice.md`, Coaching register)

- A post-session note is a set of lecture notes, not an email. Use a concept title,
  descriptive headers, numbered procedures, and spaced examples. Do not use a greeting
  or sign-off.
- Open with Joshua's concrete explanation of the concept. Define the words the student
  needs in plain language before diagrams or inference rules. Do not invent abstract
  umbrella wording such as “how much of a group fits a description” when the direct
  definition is “some means at least one; most means more than half; all means every one.”
- Short sentences. One idea per line. Air between ideas.
- Write for a student returning days later. Do not rely on "remember that question" or
  unexplained references to a person, scenario, or answer choice.
- Teach the reasoning; never just state the answer. "A reverses the timeline: the
  symptom stops, then the boss assumes the cause was fixed" beats "A was wrong".
- Praise only when it names a durable skill or meaningful change and ties to their
  history. Never praise the mere fact that an answer was correct.
- Honest about the test, never blunt about the student. When it slipped, say it is a
  normal place to slip and move to the fix.
- **No em dashes, ever.** Periods, colons, the middot (·).
- No "unlock", "dive deep", "elevate", "game-changer", "seamless", "robust", no emoji.
- No internal vocabulary: no "beat", no "door", no tool or model names, no "transcript"
  or "Gemini" in the student note.
- Only what the transcript supports. If he did not assign it, it is not in "Before
  next session".
- Read `wiki/COPY-CORRECTIONS.md` before writing; every past wording fix is there.
- For conditional LSAT notes, distinguish an asserted fact from a general rule. A
  rule states what follows if its trigger is present; it does not establish that the
  trigger occurred. Some stimuli contain rules and no facts. Never invent a fact to
  trigger a rule.

## 4. Validate, log, and hand back

Before handoff, check that:

- the opening begins with content rather than commentary about the session;
- the note explains both the move and the reason it is valid;
- examples make sense without the original question;
- hierarchy is visible at a glance;
- practice matches the transcript; and
- the student-facing portion contains no private context, transcript references, or
  administrative follow-ups.

- Append the session line to the student's `transcripts.md` if one exists (primary,
  append-only), and any promise he made to `open-loops.md`.
- Append one line to `wiki/log.md`: `## YYYY-MM-DD recap | <students>` with paths.
- Report: which recaps were written, which sessions had no transcript (list them, with
  the reason if known), and anything that needs his call (a new name, a folder to
  create). If Joshua explicitly requested a platform action, report its verification
  separately from the draft.
