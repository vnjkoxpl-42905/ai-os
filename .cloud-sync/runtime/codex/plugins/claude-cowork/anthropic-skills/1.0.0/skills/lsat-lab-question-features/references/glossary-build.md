# Glossary build

Use this when the user wants the full **definitions** of all question features, not
a per-set mapping. Output is a single file `Question Features Glossary.md` in the
`LSAT Lab - Question Features` folder.

## Open the glossary

On any `app.lsatlab.com/my` (or in-app) page, the left sidebar has **Logical
Reasoning → Glossary**. The sidebar expands on hover over the Logical Reasoning
(scale) icon. Clicking **Glossary** opens a modal titled "Logical Reasoning Glossary"
with a "Question Features" accordion. If a click doesn't seem to register because the
hover-sidebar collapses, hover the Logical Reasoning icon and click the Glossary link
while it's expanded; then screenshot to confirm the modal is open.

## Extract all features (Bootstrap accordion)

The accordion is Bootstrap collapse: each feature is a `button.btn-link` header whose
description sits in a sibling `.collapse` panel — all present in the DOM even while
collapsed.

```js
window.__qf = [...document.querySelectorAll('button.btn-link')].map(b => {
  const card = b.closest('.card') || b.parentElement;
  const panel = card ? card.querySelector('.collapse') : null;
  return {
    title: b.textContent.trim(),
    body: panel ? panel.innerText.trim().replace(/\n{2,}/g, '\n\n') : ''
  };
});
JSON.stringify({ count: window.__qf.length, titles: window.__qf.map(x => x.title) });
```

## Handle output truncation

`javascript_tool` truncates long returns (~1000 chars). Descriptions are long and
there are 60+ of them, so chunk before reading:

```js
window.__chunks = [];
const CS = 800;
window.__qf.forEach((x, i) => {
  for (let p = 0; p < x.body.length; p += CS)
    window.__chunks.push(`[${i}|${x.title}|${p}] ${x.body.slice(p, p + CS)}`);
});
window.__chunks.length;
```

Then retrieve chunks in batches with `browser_batch` (e.g., 15–20 `javascript_tool`
calls each returning `window.__chunks[k]` in one round trip). Reassemble per title.

## Write the file

One `##` section per feature, title as heading, full description below, in the order
LSAT Lab lists them. Preserve wording verbatim (this is a transcription). Then present
the file.
