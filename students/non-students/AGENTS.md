# non-students — former students

Every folder in here belonged to someone Joshua no longer teaches. They were moved
out of `students/` on 2026-09-10 after he confirmed each one by name.

## What this folder means

- **Not a student.** Do not assign work, mint booking links, draft check-in emails,
  or include anyone here in a "current students" list, roster, or sweep.
- **Records are preserved, not deleted.** Transcripts, teaching notes, correspondence
  indexes, and homework stay exactly as they were. Nothing in here is ever deleted
  without Joshua's explicit confirmation, same as the rest of the vault.
- **Read-only by default.** Only touch a folder here if Joshua asks about that person.

## Coming back

If a former student returns, move their folder back up to `students/<slug>/`, set
`status: active` and `lifecycle: active` in `<slug>.md`, and regenerate the roster
(`python3 system/scripts/build-roster.py`).

## Why this exists

Before 2026-09-10 former students sat beside current ones with only a frontmatter
flag telling them apart, and that flag was wrong at least three times (Steven,
Adriana, Amanda). A separate folder makes the distinction physical: anything that
globs `students/*/` now sees only current students.

## Moved 2026-09-10

bella-lorenzo, c-alexander, kaden-forges, lexi, lydia, meghan, thaniuska-vivas
