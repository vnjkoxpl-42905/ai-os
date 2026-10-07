# Extraction scripts (per-set)

Run these with `mcp__Claude_in_Chrome__javascript_tool` (action `javascript_exec`)
on the practice-set tab. Paste them in order.

## 1. Define the extractor

Reads the authoritative bottom-left label (`PrepTest N · S# · Q#`) and the feature
chips as leaf elements so individual tags aren't concatenated.

```js
window.__extract = () => {
  const all = [...document.querySelectorAll('*')];
  const lblEl = all.find(e => e.children.length === 0 &&
    /PrepTest\s*\d+\s*·\s*S\d+\s*·\s*Q\d+/.test(e.textContent));
  const label = lblEl ? lblEl.textContent.replace(/\s+/g, ' ').trim() : null;
  const qfEl = all.find(e => e.children.length === 0 &&
    e.textContent.trim() === 'Question Features');
  let features = [];
  if (qfEl) {
    const row = qfEl.parentElement;            // row = label + chips
    features = [...row.querySelectorAll('*')]
      .filter(e => e.children.length === 0)    // leaf chips only
      .map(e => e.textContent.trim())
      .filter(t => t && t !== 'Question Features');
    features = [...new Set(features)];
  }
  return { label, features };
};
JSON.stringify(window.__extract());
```

Run it once to sanity-check it returns the current question's label + features.

## 2. Run the loop (writes to window, then poll)

```js
window.__results = [];
window.__done = false;
window.__err = null;
(async () => {
  try {
    const sleep = ms => new Promise(r => setTimeout(r, ms));
    const n = document.querySelectorAll('button.qb-v2__pill').length;
    for (let i = 0; i < n; i++) {
      document.querySelectorAll('button.qb-v2__pill')[i].click();
      let tries = 0;
      while (tries < 40) {                       // wait for label to show Q(i+1)
        await sleep(120);
        const lblEl = [...document.querySelectorAll('*')].find(e =>
          e.children.length === 0 &&
          /PrepTest\s*\d+\s*·\s*S\d+\s*·\s*Q\d+/.test(e.textContent));
        const label = lblEl ? lblEl.textContent.replace(/\s+/g, ' ').trim() : null;
        if (label && new RegExp('Q' + (i + 1) + '$').test(label)) break;
        tries++;
      }
      await sleep(400);                          // settle so chips repaint
      const r = window.__extract();
      window.__results.push({ pos: i + 1, label: r.label, features: r.features });
    }
  } catch (e) { window.__err = String(e); }
  window.__done = true;
})();
'started';
```

Then poll until finished (a 25-question set takes roughly 30–60s):

```js
JSON.stringify({ done: window.__done, err: window.__err, count: window.__results.length });
```

Use `computer` action `wait` (~10s) between polls. When `done` is true, read it all:

```js
JSON.stringify(window.__results.map(r => ({ q: r.pos, label: r.label, f: r.features })));
```

If the result string is long and gets truncated by the tool, read it in slices, e.g.
`JSON.stringify(window.__results.slice(0,13)...)` then `.slice(13)`.

## 3. Verify empties

For each question whose `f` is empty, navigate and zoom the panel to confirm:

```js
document.querySelectorAll('button.qb-v2__pill')[Q_INDEX].click(); 'clicked';
```

(`Q_INDEX` is question number minus 1.) Then `computer` `zoom` with
`region:[1110,120,1460,330]`. A genuine empty shows the "Question Features" heading
with no chips beneath it.

## Selector reference

- Question pills: `button.qb-v2__pill` (one per question, all in DOM)
- Prev/Next buttons: `button.qb-v2__nav-btn`
- Bottom-left label leaf: matches `/PrepTest \d+ · S\d+ · Q\d+/`
- Open the panel: top-right hamburger **Menu** → **Question Details** menu item
