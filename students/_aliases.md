---
title: Student name aliases
type: operating-layer
tags: [students, operating-layer]
created: 2026-07-20
updated: 2026-09-08
status: active
subject: Student name aliases
aliases: []
---

# Student name aliases

Maps the names that show up in transcript filenames, calendar invites, and email
to the canonical student folder slug in `students/`.

It exists because Gemini names its exports from the meeting title, which is
whatever was typed at booking time: `Sofia`, `sofia`, `Sofia Minassian`,
`LSAT Session between Joshua and Meghan Mullins` all mean one student. Without
this file every pass re-derives the same mapping by hand and gets it slightly
differently.

Read by `system/scripts/transcript-inventory.py`. Format is one bullet per
alias, `alias -> folder-slug`. Matching is case- and punctuation-insensitive,
so only add entries the automatic matcher cannot get on its own (exact slug,
first name, and unambiguous containment are already handled).

## Aliases

- Adriana -> adriana-varea
- Adriana Varea -> adriana-varea
- Isabella Lorenzo -> bella-lorenzo
- Kaden Forges -> kaden-forges
- Thaniuska Vivas -> thaniuska-vivas
- Yahunathan -> yahunatan-zetvy
- YahuNathan -> yahunatan-zetvy
- Yahunatan -> yahunatan-zetvy
- Ore -> ore
- Oreoluwa -> ore
- Oreoluwa James -> ore
- Yahunatan Zetvy -> yahunatan-zetvy
- Asia -> asia
- Celia -> celia-cutler
- Celia Cutler -> celia-cutler
- Charles -> charles-moore
- Charles Moore -> charles-moore
- Fernande -> fernande-charleus
- Fernande charleus -> fernande-charleus
- Steven -> steven-morris
- Steven Morris -> steven-morris
- Vinay -> vinay-kalva
- Vinay Kalva -> vinay-kalva
- Whit -> whit-wilson
- Whit Wilson -> whit-wilson

## Prospects, no record yet

Consulted but never taught, so they have not earned a student record (see
`CONTEXT.md`: a taught session is what earns a folder). They are **still
prospects on the same path as everyone else** and remain worth following up.
This section previously read "Not students", which was wrong: Yahunatan was a
consultation on 2026-07-07 and a paying student by 2026-07-15.

Listed here so they stop surfacing as unresolved on every inventory run, and so
follow-up stays possible. Move a name into a folder once they are taught.

- Kaia Reid
- Kristin silva
- Susan — flagged in `references/automation-backlog.md` as a consultation with
  no follow-up ever sent

## Unresolved — needs Joshua

Real recurring sessions with no folder and no decision yet. These are the
actual gap; each is a person who was taught but has no record home.

- Andrew — 2026-05-02. **Ambiguous, needs Joshua.** Gemini captured no summary
  ("not enough conversation in a supported language") and the transcript ends at
  12:02, so there is no evidence a session was actually taught. A folder is
  earned by teaching, so none was created. Email on the invite:
  `airmanr863@gmail.com`.
