---
name: lsat-lab-mega-set
description: Build one consolidated LSAT Lab Logical Reasoning practice set containing EVERY LR question for a SINGLE PrepTest, in correct order, driving Joshua's logged-in Chrome via the claude-in-chrome extension end to end (create, select-all, rename to "PT### LR (S...)", start, capture URL, log). Use when Joshua gives a bare PrepTest number to turn into a set, e.g. "create set 154", "mega set 154", "LSAT Lab set 154", "make a set for PT 154", "build the LR set for PT 154", "make an LR set for 154". Runs autonomously to completion. NOT for a CSV/list of specific questions (that is lsat-lab-set-builder) and NOT for transcribing written explanations (that is lsat-lab-transcribe).
---

## Current AI OS execution contract

Use the active host-supported browser and current Windows/project log homes. Wrongly created sets are preserved and flagged until deletion is explicitly authorized; do not delete as automatic recovery. Verify count and set identity before declaring success.

# lsat-lab-mega-set

Build one consolidated Logical Reasoning (LR) practice set containing **every LR question for one PrepTest (PT)**, in correct order, on LSAT Lab (app.lsatlab.com), driving Joshua's logged-in Chrome. Written so any agent or human can execute it perfectly on the first try.

## Scope boundary (do not confuse with sibling skills)

One thing only: **PT number in -> one full-PT LR mega set out.** Not the other two LSAT Lab skills.

| If Joshua says... | Use | Why not this skill |
|---|---|---|
| `create set <num>`, `mega set <num>`, "build the LR set for PT 154" | **this skill (`lsat-lab-mega-set`)** | single PT, all its LR questions, in order |
| "split my missing questions into sets", "build a set from this CSV/list", "add these questions" | `lsat-lab-set-builder` | arbitrary CSV list split into 100-question chunks across many PTs |
| "transcribe PT###", "pull the explanations" | `lsat-lab-transcribe` | captures written explanations, does not build sets |

If the request is a **CSV/list of specific questions**, hand off to `lsat-lab-set-builder` and do not run this skill. This skill takes only a **PT number**.

## Activation (auto-run trigger)

Fire this skill, end to end and autonomously, when Joshua gives a **bare PT number** to turn into a set:
- `create set <num>`
- `mega set <num>` / `LSAT Lab set <num>`
- `make a set for PT <num>` / `build PT <num> LR set` / `make an LR set for <num>`

Do NOT fire on a CSV/list of questions (that is `lsat-lab-set-builder`) or on "transcribe" (that is `lsat-lab-transcribe`).

The number in the message is the PT. On trigger:
- **Do not ask for confirmation and do not pause between steps.** Execute steps 1 through 11 straight through, including create, rename, open, capture URL, and log.
- **Only stop to ask Joshua if a GATE fails and its listed recovery does not resolve it** (e.g. the PT filter count is impossible, or the dialog count keeps mismatching after a retry). Otherwise, run to completion and report the 4-line result at the end.
- If multiple numbers are given (`create sets 154, 155`), run the full procedure once per PT in sequence, logging each.
- End-of-run report (only output, after completion):
  ```
  Built: PT <num> LR (S<...>) - <total> questions across <k> LR sections
  Order: verified (each section Q1..last, sections ascending)
  URL: <started-set URL>
  Logged: docs/from-output/lsat-lab-set-log.md (LSAT U app)
  Next: say "transcribe PT <num>" to capture explanations (lsat-lab-transcribe reads this log and jumps straight in)
  ```

## Preconditions

- Chrome is open and **already logged in** to LSAT Lab. Do not enter credentials.
- Load the claude-in-chrome tools via ToolSearch if deferred: `tabs_context_mcp, navigate, computer, read_page, find, javascript_tool`.
- Work in a new tab in the same Chrome profile (shares the login session).

## Input / Output

- **Input:** a single PT number. ("Make a set for PT 154" means PT = 154.) Everything else is fixed by this skill.
- **Output:**
  1. A saved practice set named `PT <num> LR (S<a>, S<b>, ...)` containing all LR questions for that PT, in order.
  2. A new entry in the data log at `docs/from-output/lsat-lab-set-log.md` in the LSAT U app checkout (`../ai-os-projects/lsatu/` from the AI OS root; the app's git rules apply) with sections found, per-section counts, total, qsid, and the exact started-set URL.

## Execution rules (read before acting)

These exist because the site is a re-rendering SPA and every one was learned from a real miss:

1. **Screenshot before every click.** Never reuse coordinates from an earlier screenshot; the layout shifts between actions. A stale click can silently select nothing or open the wrong set.
2. **Never proceed past a failed GATE.** Each gate below has a recovery. Fix, re-verify, then continue.
3. **Verify by reading data, not by eyeballing.** For anything with more than ~10 rows, use the JS snippets in the Appendix.
4. **Prefer element refs over pixels.** Use find ("Create button at bottom of the form, not the Create tab") and scroll_to when a target is off-screen.
5. **Identify sets by qsid, never by row position.** Row clicks are subject to re-render races: a double-click on "the top row" once opened a different PT's set. The safe way to open a specific set is its direct URL (Appendix A4).
6. **JS output gets censored.** The javascript bridge blocks returns containing URLs or long strings (`[BLOCKED: Cookie/query string data]`). Return compact JSON summaries (counts, booleans, short arrays). Read the page URL from the tool result's "Tab Context" line, not from `window.location`.
7. **Tabs may need two clicks.** The In Progress tab often highlights on the first click and renders its list only on the second.
8. **Write actions allowed:** create your set, select questions, rename your set, start your set. **Never** delete or modify other sets, change account settings, or touch credentials.

## Procedure

### 1. Open the Create form
- Navigate to `https://app.lsatlab.com/practice-sets/`.
- The **Create** tab is default; header reads "Create a practice set".

### 2. Base settings (left column)
- **Section** = Logical Reasoning
- **Time** = Unlimited
- **Show answers** = After each question
- These are usually already the defaults; confirm visually anyway.
- Ignore the **Questions** number field (defaults to 10; step 6 overwrites it automatically).

### 3. Customize filters (right column, "Refine your set")
- Click **Customize** to expand. Set:
  - **Question types** = Any
  - **Question features** = Any
  - **Reasoning type** = Any
  - **Status** = **Any**  <- default is "Fresh (never seen)"; you MUST change it or the set silently drops every question Joshua has seen
  - **Difficulty** = Adaptive (leave default)

**GATE 1 - Status took effect:** the "N questions available with these filters" count jumps sharply after Status = Any (e.g. ~967 -> ~5,054 across all tests). If it did not jump, the dropdown click missed; reopen Status and pick Any again.

### 4. Select the test
- Click the **Tests** field to open the test grid.
- Click the **+** next to "Include more tests" to reveal PTs 141-159 (hidden by default to preserve them for timed practice).
- Click **Clear**, then click the one requested PT tile. Zoom on the tile after clicking to confirm it is the only highlighted one.
- Click the Tests bar to collapse the grid.

**GATE 2 - Filter count is plausible:** "N questions available" must now equal the PT's full LR count. Expected ranges: **~50-51** (PT with 2 LR sections) or **~76-77** (PT with 3 LR sections, one experimental). If N is outside 45-80, something is off (wrong tile, extra tile still selected, or Status reverted). Reopen the grid and fix before continuing.

### 5. Show the full question list
- Click **Pick questions** to expand the table.
- Set **Show entries** to **100** so all rows render on one page. The dropdown is a native `<select>`; pixel-clicking it is unreliable. Use the JS setter in Appendix A1, then confirm the visible value reads 100.

### 6. Verify order programmatically, then select all
- Columns: **PT | S | Q | Preview | Type | Level | Attempts**. Default sort is Section then Question ascending, which is exactly the required order.
- Run the order-verification snippet (Appendix A2). It must report: total = filter count, each section contiguous from Q1 with no gaps, sections in ascending order. Record the section numbers and per-section counts; the log entry and the set name need them.
- Screenshot, then click the **header checkbox** (top-left of the table) to select all.

**GATE 3 - The count trap (most dangerous step):** after select-all, three numbers must agree:
1. the badge reads **"N selected"**,
2. the left-column **Questions** field auto-changed from 10 to **N**,
3. N equals the filter count from Gate 2.
If the badge still says "0 selected", the click missed the checkbox (this happened; the page had shifted). Re-screenshot, click the checkbox at its current position, re-verify. **Skipping select-all yields a 10-question adaptive set, not the mega set.**

### 7. Create the set
- Locate the **Create** button (outline style) at the form bottom; use find + scroll_to rather than blind scrolling. Do NOT click **Start** (blue), which launches immediately.
- Click **Create**.

**GATE 4 - Dialog count:** the "Practice set created" dialog states the question count: `Created "LR Practice Set - <date, time>" with N questions.` N must equal Gate 2/3's N. If it says 10 (or anything else), the set is wrong: click OK, preserve and flag that set; request explicit removal authorization before deleting it, then redo from step 6 without altering other sets.
- Click **OK**. You land on the **In Progress** tab; your set is the top row.

### 8. Rename the set
- Format (approved, fixed): `PT <num> LR (S<a>, S<b>, ...)` using the real section numbers from step 6. Example: `PT 154 LR (S1, S2, S4)`.
- The **Name** cell is inline-editable: **single-click** the name text; the active element becomes a text input pre-filled with the auto-name.
  - Do NOT double-click: double-click opens/starts a set, and thanks to re-render races it may not even be the set you aimed at.
- Cmd+A, Delete, type the new name.
- Press **Enter** to commit. Side effect: Enter also opens/starts the set. That is fine; it is the next step anyway.

### 9. Verify the opened set and capture the URL
- The practice view loads. **Verify identity by content, not by trust:** footer chip must read `PrepTest <num> - S1 - Q1` and the header counter `1 of N`. If either is wrong, you opened the wrong set: recover via Appendix A4 (open by qsid) and re-verify.
- Capture the exact URL from the tool result's Tab Context line (see rule 6). A started set looks like:
  `https://app.lsatlab.com/practice?type=LR&questionsetid=<qsid>&questionsetattemptid=<attemptid>`
- Also note the bare open-set form for the log: `https://app.lsatlab.com/practice?type=LR&questionsetid=<qsid>`.

### 10. Confirm the rename saved
- Navigate back to `https://app.lsatlab.com/practice-sets/`, click **In Progress** (twice if needed).
- Top row must show the new name, N questions. Zoom to confirm the exact text.

### 11. Log the run
- Append a per-PT entry to `docs/from-output/lsat-lab-set-log.md` in the LSAT U app checkout (`../ai-os-projects/lsatu/` from the AI OS root; the app's git rules apply):
  - PT number; set name
  - number of LR sections found; their section numbers; per-section question counts; total
  - qsid; attempt id; exact started-set URL
  - build date
- Update that file's `updated:` frontmatter date.
- Two files, two jobs: **this skill** = reusable how-to; **the log** = per-PT data captured each run.
- The log is a shared ledger: `lsat-lab-transcribe` reads each PT's entry to auto-locate the set and pre-load its structure, and appends a `- **Transcribed:** ...` line to the entry when transcription finishes. Never remove or reformat existing entry fields; other skills key off them.

## Failure recovery (quick table)

| Symptom | Cause | Fix |
|---|---|---|
| Filter count did not jump at Gate 1 | Status still "Fresh" | Reopen Status dropdown, click Any, re-check |
| Filter count ~5,000 at Gate 2 | Clear not pressed / grid never filtered | Reopen Tests grid, Clear, select the one PT |
| Filter count 45-80 but wrong | Wrong tile or a second tile selected | Reopen grid, zoom to inspect, fix |
| "0 selected" after select-all click | Stale coordinates, click missed | Fresh screenshot, click header checkbox again |
| Dialog says 10 questions | Select-all skipped | OK -> flag and preserve the bad set -> redo step 6; delete only with explicit permission |
| Opened set shows wrong PT in footer | Row-click race opened another set | Open by qsid directly (A4), verify footer |
| JS returns `[BLOCKED: ...]` | Output contained URL/long string | Re-run returning compact JSON only; get URLs from Tab Context |
| JS finds no `<table>` rows | Grid is div-based, tables elsewhere on page | Use the leaf-node technique in A2 |
| In Progress tab shows Create form | First click only highlighted the tab | Click the tab again |

## Appendix: robust JS techniques (javascript_tool)

**A1 - Set a native select to 100 (Show entries):**
```js
(() => {
  const sels = [...document.querySelectorAll('select')];
  const t = sels.find(s => [...s.options].some(o => o.value === '100' || o.text.trim() === '100'));
  if (!t) return 'no select with 100';
  Object.getOwnPropertyDescriptor(window.HTMLSelectElement.prototype, 'value').set.call(t, '100');
  t.dispatchEvent(new Event('change', { bubbles: true }));
  t.dispatchEvent(new Event('input', { bubbles: true }));
  return 'set to ' + t.value;
})()
```

**A2 - Verify all rows and ordering (works on the div-based grid; `<table>` queries fail):**
```js
(() => {
  // every leaf element whose text is exactly the PT number marks one row
  const PT = '154'; // replace with the target PT
  const leaves = [...document.querySelectorAll('body *')]
    .filter(e => e.children.length === 0 && e.textContent.trim() === PT);
  const rows = [];
  for (const lf of leaves) {
    const c = [...lf.parentElement.children].map(x => x.textContent.trim());
    const i = c.indexOf(PT);
    if (/^\d+$/.test(c[i+1]) && /^\d+$/.test(c[i+2])) rows.push([+c[i+1], +c[i+2]]); // [section, question]
  }
  const secs = [];
  for (const [s, q] of rows) {
    let g = secs[secs.length - 1];
    if (!g || g.s !== s) { g = { s, qs: [] }; secs.push(g); }
    g.qs.push(q);
  }
  return JSON.stringify({
    total: rows.length,
    sectionOrder: secs.map(g => g.s),
    sectionSizes: secs.map(g => g.qs.length),
    eachStartsAt1AndContiguous: secs.map(g => g.qs[0] === 1 && g.qs.every((v, i) => i === 0 || v === g.qs[i-1] + 1)),
    sectionsAscending: secs.every((g, i) => i === 0 || g.s > secs[i-1].s)
  });
})()
```
Expected result shape (PT 154): `{"total":77,"sectionOrder":[1,2,4],"sectionSizes":[26,25,26],"eachStartsAt1AndContiguous":[true,true,true],"sectionsAscending":true}`
Note: one extra leaf equals the Tests field itself; the row filter above excludes it automatically.

**A3 - Confirm the rename input is focused (after single-clicking the name):**
```js
(() => { const a = document.activeElement; return JSON.stringify({ tag: a.tagName, type: a.type, val: (a.value||'').slice(0, 50) }); })()
```
Expect `{"tag":"INPUT","type":"text","val":"LR Practice Set ..."}` before typing.

**A4 - Open a specific set safely (bypasses row-click races):**
- Get the qsid once from the row's kebab menu -> **Edit**: the URL is `.../practice/overview?type=LR&tab=tab_practice&mode=editpracticeset&qsid=<qsid>`. Cancel out of Edit (it edits questions; it has no name field).
- Then navigate to `https://app.lsatlab.com/practice?type=LR&questionsetid=<qsid>` and verify the footer chip.

## Verification checklist (run every time)

- [ ] LR / Unlimited / After each question
- [ ] Types, Features, Reasoning = Any; **Status = Any** (Gate 1: count jumped)
- [ ] Grid: + expanded, Clear pressed, exactly one PT tile selected
- [ ] Gate 2: filter count in expected range (~50-51 or ~76-77) and recorded
- [ ] Show = 100; all rows rendered
- [ ] A2 snippet: total matches, sections contiguous from Q1, ascending; section numbers recorded
- [ ] Gate 3: "N selected" == Questions field == filter count
- [ ] Create (not Start) clicked; Gate 4: dialog count == N
- [ ] Renamed to `PT <num> LR (S...)`; Enter committed
- [ ] Opened set verified by footer `PrepTest <num> - S1 - Q1` and `1 of N`
- [ ] URL captured from Tab Context (has questionsetid and questionsetattemptid)
- [ ] Rename confirmed on In Progress list
- [ ] log entry appended to docs/from-output/lsat-lab-set-log.md in the LSAT U app

## Gotchas (context)

- **LR section count varies.** A PT surfaces 2 or 3 LR sections here (one may be the unscored/experimental section). Include every LR question the filter returns. Section numbers can skip (e.g. 1, 2, 4) because RC occupies the gap; expected, not an error.
- **Auto-name.** New sets are auto-named `LR Practice Set - <date, time>`; the create form has no name field. Renaming happens on the list afterward (step 8).
- **Starting a set marks it IN PROGRESS.** Harmless and expected once you open it in step 9.
- **PTs 141-159 are hidden by default** in the test grid ("to save them for practice tests and timed sections"); the + reveals them. Selecting one for a set is intentional here per Joshua's instruction.
