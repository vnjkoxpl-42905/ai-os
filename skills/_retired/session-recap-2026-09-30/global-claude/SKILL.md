---
name: session-recap
description: Write the post-session recap note for a student, in Joshua's voice, from the Gemini transcript, and file it in the student's folder WITHOUT posting it. Use when Joshua says "recap note", "write the recap", "take a recap for <student>", "recaps for this week", or after a transcript has just been ingested. Never posts, sends, or assigns anything. Also covers pulling the past week's Gemini transcripts from Calendar into student folders.
---

# Session recap

After every session Joshua wants one note he can read, edit, and then post to the
student himself. The note is drafted here, in his voice, and stays a draft. Posting is
his click (Teacher Desk, or `lsat-u-platform-actions`), never this skill's.

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

File to `students/<slug>/transcript-downloads/YYYY-MM-DD-<slug>-notes-by-gemini.md`.
Resolve the person with `students/_aliases.md`; for a "Meeting started" doc, count
speaker labels in the transcript (`grep -o -E "^[A-Z][a-z]+( [A-Z][a-z]+)?:" | sort | uniq -c`).
Consultations and people without a folder go to `students/_other-sessions/`.
**Never create a student folder without asking.** Skip anything already on disk.

The Google Classroom calendars (`c_classroom...`) have been empty since 2026; the
primary calendar holds every session.

## 2. Read the whole transcript, not the Gemini summary

The Gemini "Quick notes" flatten what he said. The recap has to name the student's
actual moves (the answer they picked, the line they misread, what they said when it
clicked). Read the transcript section. It is 40 to 90 KB; that is the cost of a recap
that is true.

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

# Session recap · YYYY-MM-DD

Hey <Name>,

<One or two lines. What we did, in the student's own terms. Specific, not "great session".>

## What we worked on

- <3 to 5 bullets. The concepts, in plain words. Name the question when it matters.>

## The one thing to hold onto

<The reasoning move of the session, taught, not asserted. Two to five sentences.
This is the part the student re-reads. The reasoning is the product.>

## Where it slipped

<Honest, gentle, specific. The exact move that went wrong and why it is a normal
place to slip. Bluntness at the material, warmth at the person. Omit if nothing slipped.>

## Before next session

- [ ] <What was actually assigned, as the student would recognise it.>
- [ ] <Only what the transcript supports. No invented drills.>

## Next time

<One line: the agenda and any promise he made ("extra time for accommodations").>

Best,
Joshua

---

## Notes for me (not posted)

- **Weak spots:** <tags>
- **Follow-ups on my side:** <things Joshua promised: send materials, assign a drill, schedule>
- **Watch:** <a teaching judgment worth carrying into teaching-notes.md if it repeats>
```

Everything above the `---` rule is the student note and must stand alone when pasted.
Everything below is admin-only.

## Voice rules (from `wiki/teaching-voice.md`, Coaching register)

- "Hey <Name>," for established students, "Hi <Name>," for a first or second session.
  Sign "Joshua". "Best," is the default close.
- Short sentences. One idea per line. Air between ideas.
- Teach the reasoning; never just state the answer. "A reverses the timeline: the
  symptom stops, then the boss assumes the cause was fixed" beats "A was wrong".
- Praise names the exact skill and ties to their history. No "great job".
- Honest about the test, never blunt about the student. When it slipped, say it is a
  normal place to slip and move to the fix.
- **No em dashes, ever.** Periods, colons, the middot (·).
- No "unlock", "dive deep", "elevate", "game-changer", "seamless", "robust", no emoji.
- No internal vocabulary: no "beat", no "door", no tool or model names, no "transcript"
  or "Gemini" in the student note.
- Only what the transcript supports. If he did not assign it, it is not in "Before
  next session".
- Read `wiki/COPY-CORRECTIONS.md` before writing; every past wording fix is there.

## 4. Log and hand back

- Append the session line to the student's `transcripts.md` if one exists (primary,
  append-only), and any promise he made to `open-loops.md`.
- Append one line to `wiki/log.md`: `## YYYY-MM-DD recap | <students>` with paths.
- Report: which recaps were written, which sessions had no transcript (list them, with
  the reason if known), and anything that needs his call (a new name, a folder to
  create). Do not post. Do not assign. Do not email.
