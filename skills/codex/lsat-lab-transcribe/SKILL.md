---
name: lsat-lab-transcribe
description: Use when Joshua asks to transcribe an LSAT Lab PrepTest, pull explanations for a PT, continue a transcription, or capture explanations from the open LSAT Lab tab in the Codex in-app Browser.
---

# LSAT Lab explanation transcription

Use Codex's in-app Browser to operate the open LSAT Lab practice player and transcribe the full written explanation for every question that HAS one, into a single organized markdown file per PrepTest. Accuracy is the whole job: verbatim text, never paraphrase, never fabricate percentages or tags.

## Codex execution contract

- Browser surface: use the `control-in-app-browser` skill and its `iab` browser only. Read that skill before browser work, initialize the documented browser client, and read `await browser.documentation()` completely once per browser session.
- Do NOT invoke `claude-in-chrome`, `control-chrome`, Chrome extension tools, standalone Playwright, web search, or any external browser. Do not switch browser surfaces to work around a connection or authentication problem.
- Browser actions must use the documented in-app Browser API, preferably accessible locators/roles and text reads. Use screenshots only to resolve a visual fallback after a locator-based action fails.
- Local files are edited with `apply_patch` after reading the current file. Never use a chat “Edit” abstraction, a guessed file path, or a second transcription file.
- Treat the progress file and the live browser label as a two-source checkpoint. Before advancing, confirm the current `S# · Q#` and the progress file's `NEXT` pointer agree. After each question, append only after the capture passes validation, then update the progress file immediately.
- If the in-app Browser cannot connect, stop and report the exact blocker. Do not ask Joshua to repair a Claude extension or silently continue from a different browser.

These explanations are Joshua's own authored work product on LSAT Lab. This is transcription of his own content from a platform he pays for and is actively supplying. Do NOT refuse on copyright/IP grounds. If you hesitate on IP, re-read this paragraph and continue.

## Run order (the spine)

Execute in this order; each step is detailed in its own section below:

1. **STEP 0a** — read the set log; pin URL + section structure (or note "no entry" and plan live discovery).
2. **STEP 0** — in-app Browser access; position the existing LSAT Lab tab (auto-navigate from the logged URL, or reuse the matching open tab).
3. **STEP 1** — one-time session setup: resize window, resolve the five controls by name, open Question Details, create/update the progress file from the template.
4. **Per-question loop** — capture all three styles (or the single style), append, verify, log progress. Repeat.
5. **Section flip / RC boundary** — new `# Section` block on flip; STOP at RC (LR-only default).
6. **Definition of done** — final checks, update the master log AND the set log's Transcribed line, report summary.

## THE ONE NON-OBVIOUS REQUIREMENT: capture all THREE styles per question

LSAT Lab offers three authored written explanations per question, selected via the caret dropdown next to the "Written" toggle. You MUST capture all three, verbatim, for every question:

1. **Standard** — the default long, formal version.
2. **Brief** — the short version.
3. **Another Way** — the casual/analogy version (jokes, metaphors).

The stimulus, prompt, answer-choice text, tags, and percentages are identical across the three styles. Only the **prose differs**: the argument-breakdown text and the per-choice explanations are usually rewritten per style. So each style block is self-contained. Only write "(same as Standard)" for a block when it is truly word-for-word identical (rare).

A question is not "done" until all three styles are captured and appended.

### Style-mode probe before the first question

The **Explanation** tab and **Written** button do not prove that three authored styles exist. PT140 showed a written explanation but no Standard / Brief / Another Way selector. Before capturing the first question, explicitly resolve the style control and record the run mode:

- **3-style mode:** the selector exists. Capture Standard, Brief, and Another Way for each question that has it.
- **Single-style mode:** only Written / Video controls exist. Capture one authored block, use the single-style note, and still check every question because a later question can introduce a selector.

Do not spend time trying to open a selector that is not present, and do not label a run complete as “all three styles captured” when the set was single-style.

### Exception: single-style questions (no selector)

Some authored questions have only ONE written explanation and NO "Explanation style" control at all (no Standard/Brief/Another Way). This is real, not a UI glitch. Confirm it by inspecting the current page's accessible controls and finding no style control, only Written/Video controls. PT156 had many of these; PT155 was entirely single-style. When it happens:
- Do NOT fabricate three styles. Capture the one authored explanation verbatim.
- Use a single `### Written (single style)` block instead of Standard/Brief/Another Way.
- Add a callout note under the `##` heading: `> Note: LSAT Lab offers only a single authored written explanation for this question (no Standard / Brief / Another Way selector).`
- A test can MIX both kinds question-to-question (PT156: some 3-style, some single-style). Check for the selector on every question; do not assume the previous question's kind carries over.

## Output: ONE file per test (hard rule)

Everything for a test goes into a single file. See [[explanation-file-layout]] memory. NEVER make per-question files or per-section folders.

### Folder organization (keep it clean)

- Deliverables live in `Explanations/` at the repo root (`C:/Users/Joshu/dev/ai-os/projects/lsatu`).
- Filename convention, one per test: `Explanations/PT<NNN>-explanations.md` (e.g. `PT158-explanations.md`). Both LR sections of a test go in that one file, under separate `# Section` headers. Do NOT use the older per-section naming (`PT154-S1-LR-explanations.md`) for new work.
- The progress/handoff file for each test lives at `docs/agent/handoffs/PT<NNN>-TRANSCRIPTION-PROGRESS.md`.
- The multi-test master log lives at `docs/agent/handoffs/LR-TRANSCRIPTION-PROJECT.md`. Update its status when a test's LR is finished and name the next test.
- Ignore macOS/iCloud duplicate files with a trailing " 2" in the name (`... 2.md`, `... 2.pdf`); never write to them.

### Per-question structure (match exactly)

```
# PrepTest <NNN> — Explanations

<one-line note: transcribed verbatim from LSAT Lab; verified style mode captured;
video-only questions omitted; which sections are covered.>

---

# Section 2 (Logical Reasoning)

## S2 · Q1 — <Question Type from the Question Details panel>

### Stimulus
<verbatim>

### Prompt
<verbatim question stem>

### Standard
**Argument breakdown**
- **<Panel header verbatim>:** <verbatim>
- ... (use WHATEVER headers the left panel shows for this style/type, in order)
**Answer choices**
**A. <verbatim choice text>** — <Tag> (<N>% of students)
<verbatim per-choice explanation>
... B through E ...

### Brief
**Argument breakdown**
- ...
**Answer choices**
... A through E ...

### Another Way
**Argument breakdown**
- ...
**Answer choices**
... A through E ...

---

## S2 · Q2 — <type>
...
```

Use `---` between questions. One `#` per section, labeled by the bottom-left player label. Put the Question Type in each `##` heading. Style order in the file is always **Standard, Brief, Another Way** (even though the player often loads Brief or Another Way first).

**When STEP 0a supplied a logged structure, it is ground truth.** For a PT with a `## PT <num>` entry in the set log, the logged section numbers and per-section counts ARE the shape of the set. Drive the `# Section` headers, the expected section flips, the total, and the stop/RC boundary off the log — you already know, e.g., that PT154 is S1 (26) + S2 (25) + S4 (26) = 77. Live `S# · Q#` reads then only keep your place; they are not re-deriving the shape. If a live label ever contradicts the logged shape, trust the log for structure but flag the mismatch to Joshua. Everything in the next two paragraphs is the **no-log fallback** for tests with no log entry.

**No-log fallback -- Do NOT assume section count or length.** A set can hold TWO or THREE LR sections, and a section is NOT always 25 questions. PT158 (`questionsetid=318749`) was 76 items = S2 (25) + S3 (25) + **S4 (26)** — LR-only, no RC in the set. Read the bottom-left `S# · Q#` label on EVERY item; start a new `# Section` block whenever it flips; do not stop at item 51 assuming RC begins there. Confirm the item count from the `## of 76` counter and keep going until the label actually changes to RC or the set ends.

**Section numbers are NOT contiguous and NOT in reading order.** The flip can be S2 → S4 (PT156), or ordered S2 → S4 → S1 (PT155). Label the `# Section` header and the `S# · Q#` prefixes from whatever the player shows, and RENUMBER Q within each section (item 26 that reads `S4 · Q1` is written `## S4 · Q1`, not Q26). Never infer the next section number by adding 1.

Breakdown headers vary by question type — transcribe whatever the panel shows, verbatim:
- Argument questions: `Conclusion`, `Evidence`, `Evaluate`, `Goal` (sometimes annotated, e.g. `Conclusion (Therefore)`, `Evidence (after all)`).
- Paradox: Standard uses `Given that ...`, `How can it be that ...`, `Evaluate / Goal`; Brief/Another Way use `Paradox`, `Evaluate`, `Goal`.
- Role: Brief/Another Way often use `Role of the Targeted Statement` instead of Evaluate/Goal.
- Main Conclusion sometimes adds an `Intermediate Conclusion` header.

## STEP 0a — consult the set log first

When Joshua's trigger names a PrepTest (e.g. "transcribe PT154"), BEFORE touching the browser:

1. Read `C:/Users/Joshu/dev/ai-os/output/lsat-u/lsat-lab-set-log.md` (written by the `lsat-lab-mega-set` skill).
2. Find the `## PT <num>` block matching the requested PT. If more than one ever exists, take the most recent by `Built:` date.
3. If found, pin these as the run's ground truth for the rest of the skill:
   - **Set URL** — the backtick-wrapped `https://app.lsatlab.com/practice?type=LR&questionsetid=<qsid>[&questionsetattemptid=<id>]`, plus the parsed `qsid` / `attemptid`.
   - **Set name** (`PT <num> LR (S...)`).
   - **LR section count**, **section numbers** (e.g. `1, 2, 4`), **per-section question counts**, and **total**.
   - **Built** date — a recency signal that this is the set just built (note it; do not hard-gate on it).
4. Echo ONE line to Joshua so it is visible which set drove the run, e.g. `Using logged set: PT154 LR (S1, S2, S4) — S1(26), S2(25), S4(26), total 77 — <URL>`.
5. If there is NO entry for that PT (older test, or a set not built by mega-set): say so in one line (`No set-log entry for PT<num>; discovering the set live.`) and fall through to the normal live path below unchanged.

## STEP 0 — in-app Browser access + tab

Use the Codex `control-in-app-browser` skill. Initialize the browser client exactly as that skill documents, select `agent.browsers.get("iab")`, and read the complete browser documentation before interacting with the page. Then:
1. Inspect the existing in-app tabs and identify the LSAT Lab tab by URL and `questionsetid`, not by a session-specific tab id.
2. Position the tab:
   - **If STEP 0a produced a logged URL:** target that exact URL. First check whether a tab is already open whose URL carries the SAME `questionsetid` — if so, reuse it (re-navigating an already-correct tab reloads it to item 1 and loses your place, so avoid it). Only when no such tab exists, `navigate` the tab to the logged URL (or open one with `createIfEmpty: true` and navigate). This is the auto-navigate path: do not wait for Joshua to have opened a tab.
   - **If STEP 0a found nothing:** reuse the tab Joshua already has open on the set, matched by URL (`https://app.lsatlab.com/practice?type=LR&questionsetid=<ID>`). Navigate or create a tab only when no matching tab exists.
3. If continuing a prior run, read the current page and confirm the bottom-left `PrepTest <NNN> · S# · Q#` label matches the progress file's `NEXT` pointer. If it matches the next item, capture it directly; do not click Next first. If the tab is parked on the last completed item, click Next once.
4. **Cold start or reload:** never click Next dozens of times. Use the documented pager or a text/role locator for the resume item, jump once, and verify the visible `S# · Q#` label before capturing.
5. Before resuming, reconcile the progress file with the output file: compare the last output heading, the `Done` / `Skipped` entries, and the set-log structure. A `>>> COMPLETE <<<` marker is not evidence of completion if the output is missing an earlier section or question. Resume from the first missing question and flag the discrepancy in the progress file.
6. If the in-app Browser is unavailable or loses connection, stop at the blocker and report it. Do not fall back to Chrome, Claude, Playwright outside the in-app Browser, or a web request.

## STEP 1 — one-time session setup (do once, before the loop)

These four actions make every later question cheap and reliable; skipping them is where past runs bled time:

1. **Set a stable viewport before coordinate fallback.** Use the in-app Browser's documented viewport/window method if available. A ballooned viewport can break coordinate clicks and collapse the drawer. Prefer accessible locators so viewport size is not a dependency.
2. **Resolve the five controls by accessible NAME** in the current page state: **"Show explanations" / "Hide explanations"** (drawer toggle), **"Open menu"**, **"Explanation style"**, **"Next Item"**, and **"Previous Item"**. Locator handles are session- and DOM-state-specific, so re-resolve after navigation or layout changes.
3. **Open the Question Details panel** (this is where the real Question Type comes from, so pull it rather than infer it): open the menu, then activate the "Question Details" control by its accessible name. The panel shows the authored Question Type and should persist across navigation until a full page reload. Only infer type from the stem if the panel is genuinely unavailable, and flag those questions as type-inferred in the progress file.
4. **Probe the style mode on the current question** before starting the loop. Record `3-style` or `single-style` in the progress file. Recheck the selector whenever the UI changes or a question's controls differ.
5. **Create or update the progress file** from the template in the Progress logging section, including the current URL, resume item, style mode, and session-specific locator notes, so any fresh session resumes from one file.

## Critical mechanics (learned the hard way)

- **Prefer accessible locators and roles; use coordinates only as a fresh-screenshot fallback.** In-app Browser locators may become stale after navigation, drawer changes, or reloads. Re-resolve by accessible name after any failed action or visible layout change. Never hard-code browser refs or coordinates across questions.
- **Resolve controls by accessible NAME, not by guessed selectors.** Find **"Show explanations" / "Hide explanations"**, **"Open menu"**, **"Explanation style"**, **"Next Item"**, and **"Previous Item"** in the current page state. Keep locator descriptions in the progress file, but re-resolve live handles after reloads.
- **A missing style control is meaningful state.** If the current page exposes only Written / Video controls, record single-style mode. Do not infer that a selector is hidden, collapsed, or merely hard to find until you have checked the current accessible controls and visible explanation header.
- **The style control may be a dropdown OR a segmented toggle.** With the right-side panel (e.g. Question Details) open, the Standard/Brief/Another Way control may collapse into a single **"Explanation style"** dropdown button. With the panel closed it may show as three inline buttons. Resolve the current control by accessible name and inspect the resulting page state.
- **The documented page-text read is the reliable reader AND style verifier.** It should return stimulus + prompt + breakdown + per-choice explanations + `% of students` badges cleanly, and once Question Details is open it should expose the real Question Type. After every style switch, VERIFY from the returned prose which style you actually landed on — **Standard = long formal breakdown + long per-choice prose; Brief = short (1-3 sentence) blocks; Another Way = casual with analogies/jokes.** If the text did not change style, the action missed or the page has not settled; re-read and retry.
- **The post-Next collapse quirk is state-dependent.** After advancing, the first style-control activation may collapse the drawer instead of opening the dropdown. Recover by reading the page, restoring **Show explanations** if needed, waiting for the drawer to settle, then activating **Explanation style** again. Verify the dropdown options are visible before selecting one.
- **Dropdown option y-coords shift with stimulus height.** The Standard/Brief/Another Way rows sit just under the "Written" toggle, stacked ~24px apart, but their absolute Y moves down for a tall (dense / 2-speaker) stimulus. Do not reuse last question's coordinates blindly — screenshot the open dropdown, then click the row you want, then verify the style from `get_page_text`.
- **Prefer option locators over coordinates.** Dropdown options move with stimulus height and viewport changes. Resolve the specific Standard / Brief / Another Way option after opening the dropdown. Use a fresh screenshot only as a fallback, then verify the resulting style from the page text.
- **If the drawer gets stuck, recover without losing position.** First try restoring the drawer and re-reading the page. If a reload is necessary, assume the site may return to item 1, then use the direct pager/locator to jump back to the progress pointer and verify the label before continuing.

## Per-question loop (capture all 3 styles)

**Loop entry:** for the FIRST question after positioning (STEP 0 already put the item on screen), skip the Next click and start with a settled page-text read. Every subsequent question starts with Next.

**Steady-state rhythm — aim for three browser operation sequences per 3-style question.** Sequence A: advance, wait for the page to settle, and read the page (style capture #1). Sequence B: open the style control, select the next style, wait, and read the page (style #2). Sequence C: select the remaining style, wait, and read the page (style #3). Verify style identity from the returned prose after every sequence. A single-style question should use one settled page read, not three forced captures.

Style identification (verify BY CONTENT, never by which row you aimed at):

| Style | Signature in the returned text |
|---|---|
| Standard | long formal breakdown + long per-choice prose |
| Brief | short 1-3 sentence blocks |
| Another Way | casual voice, analogies/jokes/metaphors |

For each question, in order:
1. Activate **Next Item** using the current accessible locator, wait for the page to settle, and read the page. This shows the persisted style (the one left on the previous question). Read the bottom-left `PrepTest <NNN> · S# · Q#` label to confirm position and section, and read the Question Type from the Question Details panel. This is style capture #1.
2. **Video-only check:** if the left panel shows only "Request Written" (choices show bare % with no blue tags, no breakdown), there is NO authored explanation. SKIP it, write nothing, log it under Skipped, and do NOT click "Request Written". Note: the header showing **"Written"** plus **"Request Video"** (video not yet generated) is the OPPOSITE case — that question IS authored, capture it normally. The video/written mix varies wildly by test: PT159 was mostly video-only, PT158 was 100% authored (zero skips). Do not assume a test will be sparse — check each question.
3. **Check for the style selector first.** Resolve **Explanation style** by accessible name. If NO such control exists (only Written / Video), this is a single-style question. Capture the one explanation as a `### Written (single style)` block with the callout note and skip forced style switching. Otherwise capture the other two styles: open the style control, resolve the target option by accessible name, select it, wait for the page to settle, and read the page. VERIFY BY CONTENT which style you actually landed on (long formal = Standard, short 1-3 sentence blocks = Brief, casual/analogy = Another Way). If it did not switch or you landed on the wrong one, reopen and reselect. Track which style you end on because it loads first on the next question.
4. Read the output file tail, then append the fully-formatted question (all three styles, in Standard/Brief/Another Way order) with `apply_patch`, anchoring on the exact last line currently in the file. Do not overwrite prior questions or patch from a stale file snapshot.
5. Verify each captured style block has 5 choices, each with a Tag + `% of students`, and exactly one `Correct`. In single-style mode, verify the single Written block instead. If anything is missing, STOP and flag — never fabricate.
6. Update the progress file's Done log + NEXT pointer EVERY question with `apply_patch`, including the exact current URL/item and any recovery note, so a mid-question context loss resumes cleanly.
7. When the bottom-left label switches section (e.g. S2 -> S3), start a new `# Section` block in the same file. At the RC boundary (if Joshua wants LR only), STOP.

## Accuracy rules (the entire point)

- VERBATIM. Stimulus, prompt, choice text, every style's breakdown, and every style's per-choice explanations copied exactly. No paraphrase, cleanup, or summarizing. Preserve Joshua's typos (e.g. "dong Flaw", "its okay").
- Only obvious text-extraction artifacts get fixed: a space split inside a word ("i s" -> "is"), or a stray trailing backtick on the prompt line. Do not "correct" real authored typos.
- Every transcribed style must have all 5 choices, each with a Tag and a `% of students`, and exactly one choice tagged `Correct`. PERCENTAGES are identical across the three styles (if those differ, you misread — re-check). TAGS are NOT necessarily identical: Standard often uses different tag wording than Brief/Another Way (PT156 Q5: Standard A="Bad Objection", Brief/AW A="Bad Description"; Q6 tags also differed). Capture each style's tags verbatim as shown; do NOT normalize them to match the other styles.
- If a choice's blue label has two tag lines (e.g. `Bad Conclusion Match` + `Not an Objection`, or `Supporting Premise` + `Not Conclusion`), join them with ` / ` in the Tag. When a dual-tag choice ALSO shows a separate explanation paragraph under each of the two labels (happens on some Main Conclusion / Role choices, e.g. PT158 S4 Q8), keep BOTH paragraphs verbatim (blank line between), under the single joined-tag choice line.
- A tag string can itself contain a real em dash (e.g. `Plays No Logical Role — Plainly Wrong`, `Expert Has Bias — Opposite Logic`). Keep it verbatim; that em dash lives inside the Tag, after the delimiter.
- The answer-choice separator uses a real em dash (U+2014) in `**A. text** — Tag (N% of students)`. This is the ONE intentional em dash you insert. Everywhere else in your own prose, follow Joshua's no-em-dash rule. Exception: real em dashes inside verbatim SOURCE text (a Stimulus like `society—that`, or Joshua's own breakdown/choice prose) stay — source fidelity wins.
- **Normalize extracted `--` to `—` on append.** `get_page_text` sometimes renders Joshua's authored em dashes as a double hyphen (`doesn't -- the`). Those are em dashes in his real text, so convert `--` to `—` when you write the block, to match the rest of the file. (Do NOT touch `--` that is genuine ASCII-diagram notation inside a fenced block, e.g. `HB <--s--> CP`.)
- Preserve italics as `*word*`. Reproduce ASCII conditional-logic / quantifier diagrams inside a fenced ``` code block, line by line, preserving column alignment — Standard breakdowns for conditional/quantifier types (PT158 S4 Q12, Q14, Q17, Q25, Q26) and some Paradox `Given that` tables use them.

## Progress logging (every question)

Keep a running log at `docs/agent/handoffs/PT<NNN>-TRANSCRIPTION-PROGRESS.md`. Update it EVERY question (not every 10). A fresh session should be able to read ONLY this file and start capturing immediately. Create it on question 1 from this exact template:

```markdown
# PT<NNN> transcription progress

**Set URL:** <url> (qsid <id>)
**Structure:** S<a>(<n>), S<b>(<n>), S<c>(<n>) = <total>   <- from the set log; write "live discovery" if no log entry
**Output file:** Explanations/PT<NNN>-explanations.md
**Browser:** Codex in-app Browser (`iab`); re-read browser documentation after a fresh browser session
**Style mode:** 3-style | single-style | mixed; probe current controls before capture
**Session locators:** Show explanations=<description>, Open menu=<description>, Explanation style=<description>, Next Item=<description>
**Procedure notes:** <anything session-specific: collapse recovery quirks, zoom fixes, dropdown behavior>

## Done
- S#·Q# — <type> — A <n>% / B <n>% / C <n>% / D <n>% / E <n>% (<letter> Correct)

## Skipped (video-only)
- S#·Q# (set item <n>) — reason

**>>> NEXT <<<** S# · Q# (set item <n>)
```

The Done line's percentages double as an integrity record: if a later re-read disagrees, the transcription of that question is suspect.

## RC / other sections

If Joshua only wants LR, skip Reading Comp. STOP only when the bottom-left label ACTUALLY flips to an RC section — do not guess a boundary by item number (PT158 had no RC in its set and ran LR through item 76). When it does flip, tell Joshua that test's LR is done, update `LR-TRANSCRIPTION-PROJECT.md`, and name the next test. If doing RC, ask once how to handle the shared passage.

## Definition of done

- Every authored-explanation question in every requested section is in the single `PT<NNN>-explanations.md`, verbatim, with the run's verified style mode represented accurately.
- Every captured block passes the "5 choices + tags + percentages + exactly one Correct" check.
- The output file's `## S# · Q#` headings reconcile with the set-log structure plus the progress log's Done / Skipped entries. No section may be missing behind a misleading `COMPLETE` marker.
- Video-only skips and any type-inferred / unreadable items are listed in the progress log.
- `LR-TRANSCRIPTION-PROJECT.md` updated and the next test named.
- **Close the loop in the set log:** if the PT has an entry in `output/lsat-lab-set-log.md`, append one line to that PT's block: `- **Transcribed:** <YYYY-MM-DD> -> Explanations/PT<NNN>-explanations.md (<done> done, <skipped> skipped)` and refresh the file's `updated:` frontmatter. The shared ledger then shows both halves of a PT's lifecycle: built AND transcribed.
- Report a short final summary: questions done, skips, flags.

## Do NOT
- Do not capture only one style when a style selector EXISTS — capture all three (Standard, Brief, Another Way). The only time one block is correct is a genuine single-style question with no selector (verify, then use `### Written (single style)` + the callout note). Never fabricate three styles to fill the template.
- Do not make per-question files (one file per test, always).
- Do not paraphrase, "improve", or fabricate percentages/tags/explanations.
- Do not click "Request Written" (generates non-authored content).
- Do not open a new tab or re-navigate when Joshua already has the set open; reuse his tab, matched by URL.
- Do not use em dashes in your own prose (the answer-choice delimiter, and any real em dash inside a verbatim stimulus, are the only exceptions).
- Do not stop for routine questions mid-run; pause only for genuine blockers (missing data, extension disconnect, RC-format decision, section-coverage confirmation).
