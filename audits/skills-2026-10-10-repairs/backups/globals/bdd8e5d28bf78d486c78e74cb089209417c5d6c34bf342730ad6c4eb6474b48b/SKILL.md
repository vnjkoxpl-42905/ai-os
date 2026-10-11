---
name: lsat-lab-set-builder
description: Build LSAT Lab practice sets from a CSV of questions by splitting the list into evenly sized sets and selecting the exact questions in the LSAT Lab web app via Codex in Chrome. Use when Joshua wants to turn a CSV/list of LSAT questions (columns like practiceTest, section, question) into one or more saved practice sets on app.lsatlab.com, "make a set", "build set 2", "split my missing questions into sets", or "add these questions to LSAT Lab". Handles the full browser flow: Create Practice Set, LR/RC, test-range filter, per-question checkbox matching, verification, naming, and Submit.
---

# LSAT Lab Set Builder

Turn a CSV of LSAT questions into named practice sets inside LSAT Lab (app.lsatlab.com), one set at a time, by selecting the exact questions and clicking Create. The hard part is reliably ticking the right ~100 individual questions out of a 600+ question bank, so this skill drives selection through the page's DataTable rather than by eye.

## Input file

A CSV with one row per question. Expected columns (header row):

`file, practiceTest, section, question, questionType, difficulty, stem`

Only three fields matter for selection: `practiceTest` (e.g. `PT103`), `section` (e.g. `2`), `question` (e.g. `26`). On the LSAT Lab page these map to the columns **TEST** (`103`, i.e. PT stripped), **S** (section), **Q** (question).

## Step 1 — Split into sets

Default: sets of 100 in file order, with the remainder as a smaller final set. Confirm the split method and size with Joshua before building (he may want sequential, balanced by type, or balanced by difficulty). Use `scripts/split_sets.py`:

```
python3 scripts/split_sets.py "path/to/questions.csv" --size 100 --out "path/to/output_dir"
```

This writes `Set_1.csv … Set_N.csv` and prints, for each set, the question count and the PT range (first → last). Note that a practice test can straddle a boundary (e.g. PT109 ends Set 1 and starts Set 2) — that is expected with a clean row cut.

**Always build ONE set, then stop and wait for confirmation** before doing the next. Do not batch all sets without checking in.

## Step 2 — Open the LR (or RC) builder

Use the Codex in Chrome tools (load via ToolSearch: `tabs_context_mcp`, `navigate`, `computer`, `read_page`, `javascript_tool`). The user must have LSAT Lab open and logged in; a new tab in the same Chrome profile shares the session.

1. `navigate` to `https://app.lsatlab.com/practice-sets/`.
2. Click **Create Practice Set** (top right).
3. In the modal, click **LR** (or **RC**).
4. You land on the Logical Reasoning builder. There is a **test-range filter** (a dropdown showing something like `ALL TESTS` or `101-109`). Set it to cover the PT range of the current set. If the set spans more tests than one preset range, pick/select all the needed test numbers in that dropdown.

## Step 3 — Select the exact questions (the reliable method)

The question bank is a jQuery DataTable. Selection state lives in React; checking a row's checkbox adds it to the left **Practice Set** panel. Key facts learned the hard way:

- `document.querySelectorAll('table')[1]` is the **question bank**; `table[0]` is the left selected panel.
- Each bank row's cells: `td[0]`=checkbox, `td[1]`=TEST, `td[2]`=S, `td[3]`=Q, `td[4]`=NAME, `td[5]`=DIFFICULTY.
- All rows are loaded client-side: `window.jQuery(table).DataTable().rows().nodes().toArray()` returns every `<tr>` (e.g. 608), even ones not on the current page. Use this for **verification**.
- **Only click checkboxes on the currently rendered page.** Detached/non-visible rows may not fire the React handler. So you must page through.
- `input[type=checkbox].click()` correctly registers selection (fires React onChange).

### Pitfalls (do these or it breaks)

- **Do not use in-script `await`/`setTimeout` loops for pagination.** They cause CDP `Runtime.evaluate` 45s timeouts / "renderer may be frozen". Instead: process the current page in one `javascript_tool` call, then advance with the next-button in a **separate** call. The gap between tool calls gives React time to re-render.
- **Do not return `outerHTML`, hrefs, or anything with URLs** from `javascript_tool` — the bridge blocks it as "Cookie/query string data". Return only numeric/text cell values and counts.
- The REPL **persists top-level declarations** across calls, so a second `const rowKey = …` throws "already declared". Stash helpers on `window.__…` and reuse them.

### Procedure

1. Set the bank's rows-per-page select to **100**: find the `.dataTables_wrapper` for `table[1]`, set its length `<select>` value to `'100'` and dispatch a `change` event.
2. Stash the target set and a row-key helper on `window`:
   - `window.__targets = new Set([...])` of `"TEST-S-Q"` strings (TEST = PT number without `PT`).
   - `window.__rk = tr => {const td=tr.querySelectorAll('td'); return [td[1].innerText.trim(),td[2].innerText.trim(),td[3].innerText.trim()].join('-');}`
   - `window.__selected = new Set()`
3. **Per page**, in one call: for each `tbody tr`, if `window.__targets.has(rk)` and not already selected, click its checkbox and add to `window.__selected`. Return the count added and running total.
4. In a **separate** call: click the next-page button — `table[1].closest('.dataTables_wrapper').querySelector('.paginate_button.next').click()`.
5. Repeat 3–4 until you've covered all pages (e.g. 7 pages for ~608 rows). Re-read `.paginate_button.active` to track which page you're on.

See `scripts/selection_snippets.js` for copy-paste JavaScript for each of these.

## Step 4 — Verify before creating

In one call over `DataTable().rows().nodes()`, collect the keys of every **checked** row, then compute:
- `extras` = checked keys not in `window.__targets` (must be empty),
- `missing` = targets not checked.

A target can be **missing because LSAT Lab's bank doesn't contain it** (e.g. their PT103 LR section 2 ends at Q25, so a CSV row for `103-2-26` has no match). That is a real data discrepancy, not a bug. Surface it to Joshua: report which questions are missing and why (confirm by scanning the bank for that TEST+S — if the max Q is lower than the CSV's, the question simply isn't there). Ask whether to create with the found subset or hold. Never silently substitute a different question.

## Step 5 — Name and submit

1. Click the left panel's **Create** button (the enabled one, not the greyed top-right `Create Practice Set`).
2. A dialog appears with **Name**, **Countdown Timer**, **Shuffle Questions**. Type a clear name, e.g. `Set 1 - Missing Qs PT101-109`. Leave timer and shuffle off unless asked.
3. Click **Submit**. Confirm the "Success! We've created your practice set." screen with a screenshot.
4. Mark the set done and tell Joshua the final count (e.g. "99 of 100; PT103 S2 Q26 not in bank"). Offer to build the next set; remind him of its PT range and that the test-range filter must be reset.

## Defaults & conventions

- Set size: 100, remainder smaller. Order: file order (sequential) unless told otherwise.
- Section type: LR unless the CSV/Joshua indicates RC.
- Name pattern: `Set <n> - Missing Qs PT<first>-<last>`.
- One set per run; pause for confirmation between sets.
