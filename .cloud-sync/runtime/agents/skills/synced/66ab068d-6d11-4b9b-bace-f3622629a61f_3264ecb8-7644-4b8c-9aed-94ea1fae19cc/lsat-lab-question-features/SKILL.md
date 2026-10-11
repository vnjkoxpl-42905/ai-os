---
name: lsat-lab-question-features
description: >-
  Extract LSAT Lab question-feature tags from a practice set in the browser and
  save them as an organized markdown file. The user can name one of their saved
  LSAT Lab sets and the skill will open it by name from their Created Sets list,
  then gather every question's features automatically. Use this whenever the user
  wants to pull, extract, transcribe, catalog, or "grab the question features" for
  an LSAT Lab practice set, PrepTest, or LR/RC section — for example "go to my
  'Pt 159' set and pull the question features", "extract the features for this set",
  "add PrepTest 161 to my features folder", or "go through each question and list
  its tags". Also use it to (re)build the full
  Question Features Glossary from LSAT Lab's Logical Reasoning Glossary. Trigger
  even when the user doesn't say the word "skill" and just describes the task, as
  long as it involves LSAT Lab question features. Requires the Codex-in-Chrome
  browser tools and a logged-in LSAT Lab session.
---


## Local execution contract (2026-10-10)

Use actual available browser transport and current selectors. For read-only extraction avoid Start because it creates an attempt. Save mixed-section output with exact section/question identity to prevent overwrite. Preserve source/provenance and compile through existing corpus ingest.

## Workflow

# LSAT Lab Question Feature Extractor

## What this does and why

LSAT Lab tags every Logical Reasoning and Reading Comprehension question with a
set of "Question Features" (Causation, Rebuttals, Plans / Recommendations, etc.).
These tags live in the per-question **Question Details** panel and there is no
export button, so collecting them by hand across a 25-question set is slow and
error-prone.

This skill automates that: it drives the already-open, logged-in LSAT Lab tab,
reads each question's PrepTest / Section / Question number and its feature tags,
and writes a clean markdown table into a single organized folder so the user can
build a library across many sets over time.

There are two jobs this skill supports:

1. **Per-set extraction** (the common one) — pull the features for every question
   in one practice set and append a file to the features folder.
2. **Glossary build** (occasional) — transcribe the full definitions of all
   question features from the Logical Reasoning Glossary. See
   `references/glossary-build.md`.

## Before you start: environment check

This skill needs the **Codex-in-Chrome** tools (`mcp__Claude_in_Chrome__*`).
Load them via ToolSearch if deferred:
`select:mcp__Claude_in_Chrome__tabs_context_mcp,mcp__Claude_in_Chrome__navigate,mcp__Claude_in_Chrome__computer,mcp__Claude_in_Chrome__javascript_tool,mcp__Claude_in_Chrome__browser_batch,mcp__Claude_in_Chrome__find`

Key fact about the Chrome extension: it operates in its **own tab group / window**,
which is a different window from the one the user has open. It does **not** inherit
whatever tab the user is looking at. But it shares the Chrome **profile**, so once
the user is logged into LSAT Lab anywhere in that profile, the MCP tab is logged in
too. You will navigate the MCP tab to the set URL yourself.

If after navigating you land on the logged-out marketing site (Sign In / Sign Up),
do **not** enter the password yourself — ask the user to sign in once in that
window, then continue. Never type credentials.

## Per-set extraction workflow

### Step 1 — Get to the set

`tabs_context_mcp{createIfEmpty:true}` to get/make the MCP tab. There are two ways
to reach a set; **opening by name is the normal case** because the user thinks in
terms of their saved set names, not URLs.

**By name (preferred).** The user will usually just say the set's name (e.g.,
"do Pt 159", "extract features for my 'Codex' set"). Open the Created Sets list at
`https://app.lsatlab.com/practice-sets/`. This is a paginated DataTable with a
**Search** box and columns Name / Section Type / Questions / Average Difficulty /
Created, plus a **Continue** or **Start** button per row. To find the set:

1. Type the name into the Search box so the table filters to matching rows. The DOM
   for the search input is `input[type=search]`; set its value and dispatch an
   `input` event, e.g. via `javascript_tool`:
   ```js
   const s = document.querySelector('input[type=search]');
   s.value = 'Pt 159';
   s.dispatchEvent(new Event('input', { bubbles: true }));
   'searched';
   ```
2. Screenshot and read the filtered rows. Match the **Name** column exactly to what
   the user asked for. If several rows share that name (the list can contain
   duplicates) or none match cleanly, show the user the candidates (name, section
   type, question count, created date) and ask which one — don't guess.
3. Click that row's **Continue** (or **Start**, for a not-yet-started set) button to
   open the set. `Continue` resumes the existing attempt; `Start` begins one. Either
   lands you on the practice screen.

**By URL (fallback).** If the user hands you a set URL directly
(`https://app.lsatlab.com/practice?type=LR&questionsetid=...&questionsetattemptid=...`),
just `navigate` the MCP tab to it.

Either way, screenshot to confirm the set loaded (question stem, answer choices A–E,
a timer, and a numbered pagination strip at the bottom). Note the set's **name** —
you'll want it for the summary, and it helps disambiguate if the user later asks for
"that same set."

The bottom-left of the practice screen shows a label like `PrepTest 159 · S1 · Q1`
that updates as you move between questions — this is your authoritative source for
PrepTest number, Section number, and Question number.

### Step 2 — Open the Question Details panel and keep it docked

The feature tags only render when the Question Details panel is open. Open it via
the **Menu** (the hamburger icon at the top-right of the question toolbar), then
click **Question Details**. The panel docks on the right and **updates automatically**
as you navigate questions, so you only open it once.

The panel shows: PrepTest / Section / Question header, Difficulty, Question Type,
Reasoning Types, and **Question Features** (a row of chip tags). Some questions
legitimately have an empty Question Features row (often Paradox questions) — that is
real data, not a bug.

### Step 3 — Install the extractor and loop over all questions

The questions are pagination buttons with class `qb-v2__pill`, all present in the
DOM at once. Use `javascript_tool` to define a precise extractor, then run an async
loop that clicks each pill, waits for the panel to update, and records the result.

The extraction and loop code is in `references/extraction-scripts.md`. Read that
file and paste the snippets via `javascript_tool`. The important correctness details
(learned the hard way):

- **Read feature chips as leaf elements only** (elements with no element children).
  A parent container concatenates all chips into one string like
  `"Volume DialMissing Link / Idea"`; leaf nodes give you the individual tags.
- **Settle ~400ms after the label updates** before reading chips, or fast questions
  return an empty feature list before the panel repaints.
- The async loop must **write results to a `window` variable** and set a done flag.
  Inline `async` IIFE return values are not reliably captured by the tool, so poll
  `window.__done` / `window.__results` with short `wait`s until done, then read them.

### Step 4 — Verify the empties

After the loop, re-visit any question that came back with no features and confirm
visually (navigate to it, then `zoom` the panel region, roughly
`region:[1110,120,1460,330]`). Genuine empties show the "Question Features" label with
nothing under it. This catches the rare case where a slow render produced a false
empty.

### Step 5 — Write the markdown file into the features folder

Save into a single folder named **`LSAT Lab - Question Features`** so sets accumulate
in one place. If a connected/user folder exists, write there; otherwise write to the
outputs folder and share the files. Create the folder + `README.md` if they don't
exist yet (templates in `references/folder-templates.md`).

File name: **`PrepTest <number> - Section <number>.md`**.

Use this exact structure:

```markdown
# PrepTest <N> — Section <N> (<LR or RC>)

Question features for each question in this set, pulled from LSAT Lab's Question
Details panel. <count> questions. Questions marked *(none)* had no Question Features
tags in LSAT Lab.

| Question | Question Features |
|---|---|
| 1 | Feature A, Feature B, Feature C |
| 2 | *(none)* |
...
```

Then present the file(s) with `present_files` and give a one-line summary (set name,
question count, how many had no tags). Offer to add the next set the same way.

## Glossary build

If the user instead wants the full feature definitions (not a per-set mapping), follow
`references/glossary-build.md`. It opens Logical Reasoning → Glossary and transcribes
all ~60+ features verbatim, handling the output-truncation issue by chunking.

## Notes on robustness

- Selectors (`button.qb-v2__pill`, the `qb-v2__nav-btn` Prev/Next buttons, the
  `Question Details` menu item) reflect LSAT Lab's current "Modern" question bank UI.
  If a selector stops matching, screenshot the page and re-derive it rather than
  guessing — the DOM, not assumptions, is ground truth.
- Don't click web links inside the app with raw coordinates if you're unsure of the
  destination; navigation here is all within app.lsatlab.com which is trusted.
- This is read-only extraction. Never submit answers, change settings, or click
  irreversible controls (Submit / Save & exit) while navigating.
