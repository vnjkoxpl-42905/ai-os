# Work order for Codex: raise Ore's two flaw notes to Joshua's visual quality bar

Status: revised 2026-11-14 after Codex plan review round 1 (REVISE, 4 findings, all accepted). Written by Claude. Run through claudex-loop: Codex builds, Claude inspects.
Student: Oreoluwa (`students/ore`). Nothing here posts or assigns anything.

## Where to work (set up 2026-11-14)

Work only in the isolated checkout `C:/Users/Joshu/dev/ai-os-codex-ore` (branch `codex/ore-notes-2026-11-14`, baseline commit `ecfe5128`). Every path below that starts with `C:/Users/Joshu/dev/ai-os/` means the same relative path inside that checkout; read and write there, never in `C:/Users/Joshu/dev/ai-os`. `build.py` there already points `ROOT` at the checkout. The checkout holds only the inputs this order names, including the Taste skill at `.agents/skills/design-taste-frontend/`. This work order is NOT in the checkout; you are reading the supplied copy. If a named input is missing, report it; do not go looking in the real vault. Do not commit or push. Claude inspects the uncommitted changes against the baseline.

## What Joshua said

Joshua reviewed the 2026-11-14 rebuild of Ore's recap and reference and called it "low quality" and "much less quality" than his standard. His earlier direction on the same notes: the flaw list must be organized, with each flaw and its example laid out clearly and properly spaced, "much more visually engaging and clear structure", and the sufficient-versus-necessary teaching and the main fallacies drawn from his own notes and the second brain.

## What the current build gets wrong (Claude's reading, to confirm)

1. It is text in boxes. Each flaw is a heading, a sentence, a one-line arrow and two small cards. Nothing shows the flaw happening, so the structure is tidy but not engaging.
2. The four flaws have no visual identity. They differ only by a number, so a student cannot recognise them at a glance or tell them apart in memory.
3. Sufficient versus necessary, the most common flaw, is explained in prose and two sentences. It needs a picture of the rule, the fact, and what does and does not follow, because the whole flaw is a direction error.
4. The reference note is tables and cards. It should work as a one-glance poster a student keeps beside a drill.
5. Length: the recap is about 1,940 words against a 1,100 to 1,600 standard.

## The quality bar

Read these first, in order. Follow them; do not substitute a generic style.

1. `C:/Users/Joshu/dev/ai-os/design/README.md`, then `design/principles.md#material-depth-and-a-richer-layered-feel` (warm-paper and charcoal reference, purposeful layers, no decoration without a job).
2. `C:/Users/Joshu/dev/ai-os/.claude/skills/post-session-recap/references/session-desk/SPEC.md`, the approved Session Desk design. Sections 3, 4, 7, 8 and 9 are the standard for structure, pieces, effects, writing and practice checks.
3. The model note: `C:/Users/Joshu/dev/ai-os/wiki/homework-assigning/model-note/Lanae - Finding the Conclusion by Asking Why.html`. Open it in a browser and keep it beside the draft. It is the standard, not a template to copy.
4. `C:/Users/Joshu/dev/ai-os/CONTEXT.md`, section "Teaching after a session". Use its terms: post-session note, teaching note, quality bar, adapted note. Students see "note".
5. `C:/Users/Joshu/dev/ai-os/references/lsat-teaching-voice-standard.md` and `wiki/teaching-voice.md` for wording. No em dashes, no en dashes, no tildes, none of the words in `wiki/COPY-CORRECTIONS.md`.
6. Taste skill: WAIVED for this build. `design/README.md` says to use tasteskill v2, but every installed copy of `design-taste-frontend` in the vault is the older "High-Agency Frontend Skill" entry point, so the v2 guidance is not available locally. The copy in the checkout at `.agents/skills/design-taste-frontend/` is that older version. You may read it for ideas, but it is not authoritative. The authorities are items 1 to 5 above: the design hub principles, the Session Desk spec, the Lanae model note, the CONTEXT.md terms and the voice standard. Report that you did not use v2.

## Content sources (use them, do not invent)

- Ore's session facts and her own words: `brainstorms/2026-11-11-ore-post-session/PRIVATE-source-map.md` and `students/ore/transcript-downloads/2026-11-11-ore-notes-by-gemini.md`.
- Joshua's earlier notes on the same flaws: `wiki/homework-assigning/notes-archive/yahunatan-zetvy/2026-08-19-the-famous-flaws-the-most-common-ones-104256.html`. Reuse its ranking, tells and real-test-style examples (documentary, soldiers' physiques, rat poison, Billy's uncle, comics survey) and its six distractor flaws.
- Sufficient versus necessary: `brainstorms/2026-10-09-sufficient-condition-lesson.md` (the raffle and bicycle anchor is approved; breathing and air, apple and fruit, ready and packed are rejected), `wiki/sources/lsat-demon-sufficient-necessary.md`, `corpus/lr-explanations/models/Flaw.md` (picks 3, 6, 9, 13: reversal and negation, the lottery analogy, conclusion-first disguises).
- The current build: `brainstorms/2026-11-11-ore-post-session/build.py`, `recap.html`, `reference-four-flaws.html`. Backups of the version Ore holds: `v1-posted-2026-11-14/`.

## What to build

Two self-contained HTML files, same names and same lesson markers as today: `recap.html` (`ore-2026-11-11-naming-the-flaw`) and `reference-four-flaws.html` (`ore-2026-11-11-four-flaws-reference`). Keep the "Before you start" note as it is.

### Recap, goals

- Each of the four flaws gets its own recognisable visual: a small, purposeful diagram that shows the move, not decoration. Examples to consider: for sufficient versus necessary, a rule drawn as a one-way path with the two illegal moves shown as the path walked backwards and the path cut off, using the raffle and bicycle rule; for correlation versus causation, two things joined by a line with three possible stories branching from it; for part versus whole, a group and its members with the trait arrow running the wrong way; for unproven versus proven false, a "not shown" state set against a "shown false" state. Choose the form that makes the idea fastest to see.
- The four flaws read as a family: same anatomy in the same order, a consistent colour and numeral for each, so a student can find one at a glance.
- Real depth and clear hierarchy per the design hub: layers with a job, one focal surface per section, accent colours that carry meaning.
- Keep what already works and is approved: the hero and 3D stage (no overlap at any width), the two-switch check, the credit quote in Ore's own words, tap-to-check practice, the next-steps list. Bring length to 1,100 to 1,600 words with practice answers included.

### Reference, goals

- A one-glance poster, usable at a phone width and printable: the four flaws as four visual cards with their diagram, the wording tell and the question to ask; sampling as the one to learn last; the six distractor flaws as a compact cross-out row, not a long table.
- It must still answer, in one screen of scrolling, "which flaw is this?"

### The primer must not change

`before-you-start-flaw-first-taste.html` is protected. `build.py` writes all three files, and its `build()` function currently injects shared CSS into every document. Scope every new style, script and markup change to the two target lesson IDs, or exclude the primer from writing. After your final build, `sha256sum` of the primer must equal `2b001ccd26fcaed8c501fa2c990a495803d1066adf8ff125f1e5e9cab46c2f1f` (the committed baseline). Report the value. If it differs, fix `build.py` until it matches.

### New pieces

The approved Session Desk has no diagram piece. You may add new pieces, but only in `build.py` as local CSS and inline SVG for these two notes. Do not edit `wiki/homework-assigning/model-note/note-shell.html`, `session-desk.css` or `session-desk.js`. List every new piece, its job and its limits in a short `NEW-PIECES.md` in the same folder, for Joshua's approval.

## Tooling note

In this sandbox (Codex `mxc` mode on Windows) the command is `python`. The `py` launcher does not work there. `Get-FileHash` and PowerShell profiles are unavailable, so use Python's `hashlib` for SHA-256. There is no network access.

## Hard limits

- Each HTML file is a complete self-contained document under 500 KB, with its `lsatu-interactive-lesson` meta tag. Fonts are already embedded and take most of the budget, so SVG must be small.
- No external requests, images, iframes or outside scripts. The LSAT U preflight rejects non-embedded resources.
- Respect reduced motion; keyboard reachable controls with visible focus; text stays crisp, nothing blurred behind a paragraph; rotation no more than 2 degrees on anything holding a sentence.
- Every claim, example and hidden answer needs a counterexample check. The raffle example must say only what the rule supports.
- Do not post, assign, message anyone or touch LSAT U. Do not edit `students/`, `wiki/`, `CONTEXT.md` or any skill.

## Acceptance and proof

1. `python -I brainstorms/2026-11-11-ore-post-session/build.py` runs and writes all files.
2. Headless Chrome screenshots of both notes at 375, 640, 1000 and 1400 pixels wide, saved beside the build, with no overlapping elements and no horizontal page scroll.
3. Browser console shows no errors; each interaction works by mouse and keyboard.
4. Word counts and a banned-phrase scan reported as numbers.
5. Local checks of file size (under 500 KB each), the lesson marker meta tag present and unchanged in each note, and no external URLs, images, iframes or outside scripts in either file. Report each as a number or yes/no.
6. A written report that states what was checked and what was not.

The LSAT U preflight is NOT yours. This checkout has scripts from 2026-10-01 that cannot run it, and you must not touch LSAT U. Claude runs the preflight from the real vault after inspection, using a validation copy of the plan that points at your output.

Claude will independently open both notes in a browser, run the proof and the LSAT U preflight, compare against the model note, and inspect every changed and untracked file before Joshua sees anything. Joshua approves the result before any re-post.
