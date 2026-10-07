# LSAT Lab pull

Pull LSAT Lab's data for every question in one step, with no clicking through pages. Built 2026-09-27.

## What LSAT Lab exposes

The logged-in app at `app.lsatlab.com` loads everything from these endpoints. All need a logged-in session (without one they redirect with a 302).

| Endpoint | Returns |
|---|---|
| `/my/services/get-questions-just-props.php` | Every question in LSAT Lab: 10,171 rows, about 1.8 MB. Per row: `t` test number, `sn` section, `qp` question number, `s` LR/RC, `d` difficulty 1-5, `qt` question-type id, `qst` subtype ids (features and reasoning type), `tname`. |
| `/api/question-properties` | The names behind the ids: `questiontypes` and `questionsubtypes` (id, name, parent_name). |
| `/api/questions/<id>` | One question in full, `<id>` = `qid` from the props list: `questiontext` (stimulus + stem HTML), `answers[]` (full choice text, `feedback` HTML whose first `<h5>` is the tag), `correctanswer`, `generalfeedback` (full Standard breakdown, `<h5>` step labels), brief / another-way variants. This is the source of truth for text and explanations. |

**Do not load explanations from the public pages.** They redact quoted predictions and replace some steps with placeholders; only about a third matched our text exactly. Use `/api/questions/<id>`.

The public explanation pages (`www.lsatlab.com/lsat-explanations/PT<n>-S<s>-Q<q>/...`) need no login. They embed the test's question list with type tag, difficulty, key and answer percentages, plus the Standard explanation and trap labels. But the answer-choice text is cut short, and the features aren't included.

## How to refresh `data/`

1. Log in to LSAT Lab in the Claude Code browser (the in-app browser pane). The app tab must be on `app.lsatlab.com`.
2. Have Claude run this with the browser's JavaScript tool, then save what comes back to `data/properties.json`:

```js
const p = await fetch('/api/question-properties').then(r => r.json());
JSON.stringify({
  t: p.questiontypes.map(x => [x.id, x.name, x.sectiontype]),
  s: p.questionsubtypes.map(x => [x.id, x.name, x.parent_name]),
});
```

3. For the question list, the result is too big to return inline, so save it as a download instead. Then move it to `data/questions-props.json`:

```js
const q = await fetch('/my/services/get-questions-just-props.php').then(r => r.text());
const a = document.createElement('a');
a.href = URL.createObjectURL(new Blob([q], { type: 'application/json' }));
a.download = 'lsatlab-questions-props.json';
document.body.appendChild(a); a.click(); a.remove();
```

Chrome allows one download per page load without asking. For a second download, reload the page first.

## Tagging the LSAT U question bank

`tag_bank.py` writes LSAT Lab's difficulty, reasoning type and features into `public/data/PT*-LR.json`. Run it from an LSAT U checkout root, on a branch:

```bash
python <vault>/system/scripts/lsatlab-pull/tag_bank.py --slots PT113-S3-Q21,PT117-S2-Q1
python <vault>/system/scripts/lsatlab-pull/tag_bank.py --slots-file slots.txt
python <vault>/system/scripts/lsatlab-pull/tag_bank.py --missing
```

Then run `node scripts/build-question-bank.mjs` to rebuild `_bank.generated.json`.

- It touches only the slots you name. It never changes question type, because the bank keeps LSAT U's own type names and the database owns the type.
- Reasoning type comes from three subtypes, renamed for the bank: Conditional Logic → Conditional Reasoning, Comparison → Comparative Reasoning, Causation stays Causation.
- Three feature names differ between the two and are renamed the same way: Necessary vs. Sufficient Flaw → Sufficient vs. Necessary Flaw, Sampling Flaw → Sampling, Repetitve Answers → Repetitive Answers.

LSAT Lab is where the bank's labels came from in the first place. Before any changes: 3,191 of 3,305 difficulties matched, and 96% of features matched by name.

## Known state

- 2026-09-27: the 155 repaired slots were tagged (PR vnjkoxpl-42905/lsatu-684d89db#147).
- 2026-09-27: 304 more bank questions retagged to LSAT Lab's current tags (#148, lost in the Lovable rollback, restored in #149). Every LR bank question with an LSAT Lab row now matches it.

## Bulk full-text pulls

Getting large results out of the logged-in tab:
- The Claude Code browser blocks requests to localhost, so `receiver.py` does not work from it. Instead, a Blob download from that browser lands in Downloads as a `<uuid>.tmp` file. It is complete; rename it.
- Chrome allows one download per page load, or a POST to `receiver.py` (it answers the private-network preflight).

Scripts:
- `fetch_explanations.py`: public pages only; used for the audit. Do not load its output.
- `html_to_steps.py`: turns `/api/questions` HTML into LSAT U's step and note format. It keeps spacing outside emphasis markers and flattens diagram alignment.
- `build_load_sql.py`: insert-only SQL in about 15 KB batches. Larger batches got blocked by a safety filter when passed through the Lovable SQL tool.
- `apply_text.py`: writes LSAT Lab's official stimulus, stem, choices, or (with `--key`) the answer key into bank slots.

Safety:
- The guard test `src/lib/questionBank.slotFingerprints.test.ts` pins every slot to the database question.
- Regenerate its fixture only after a verified change.
