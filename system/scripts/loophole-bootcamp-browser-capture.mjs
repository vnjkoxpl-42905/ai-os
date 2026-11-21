// Run through CUA REPL with the selected Loophole tab. No network/session APIs.
// import { captureDrill } from this module; pass { tab, fs, base, drill }.
export async function snapshotQuestion(tab) {
  return tab.playwright.evaluate(() => {
    const h = Array.from(document.querySelectorAll('h2')).find(e => /^Question \d+$/.test(e.innerText.trim()) && e.getBoundingClientRect().width);
    if (!h) return null;
    const r = h.parentElement.parentElement;
    return {
      number: Number(h.innerText.match(/\d+/)[0]), text: r.innerText, html: r.outerHTML,
      buttons: Array.from(r.querySelectorAll('button')).filter(b => /^[A-Z](?:\s|$)/.test(b.innerText.trim())).map(b => ({ label: b.innerText.trim().replace(/\s+/g, ' '), disabled: b.disabled, html: b.outerHTML })),
      images: Array.from(r.querySelectorAll('img')).map(e => ({src: e.src, alt: e.alt})),
      pageText: document.body.innerText,
    };
  });
}

export async function captureDrill({tab, fs, base, drill: d, maxQuestions = 4}) {
  const slug = new URL(d.url).pathname.split('/').slice(-2).join('/');
  const dir = base + '/' + slug;
  await fs.mkdir(dir, {recursive:true});
  if (await tab.url() !== d.url) await tab.goto(d.url);
  try { await tab.playwright.getByRole('button', {name:'Show question 1', exact:true}).waitFor({state:'visible'}); } catch {}
  await tab.playwright.domSnapshot();
  await tab.playwright.domSnapshot();
  const labels = await tab.playwright.evaluate(() => Array.from(document.querySelectorAll('button[aria-label]')).map(b => b.getAttribute('aria-label')).filter(x => /^Show question \d+$/.test(x)));
  const total = new Set(labels).size;
  if (!total) throw Error('No question navigation: ' + d.url);
  let prior;
  try { prior = JSON.parse(await fs.readFile(dir + '/source.json', 'utf8')); } catch {}
  const out = {...d, total, capturedAt: new Date().toISOString(), questions: prior?.questions || [], errors: []};
  let processed = 0;
  for (let n = 1; n <= total; n++) {
    if (out.questions.find(q => q.number === n && q.resolved && !(q.final?.buttons?.length === 0 && q.final?.images?.length > 0))) continue;
    if (processed >= maxQuestions) break;
    processed++;
    try {
      await tab.playwright.getByRole('button', {name: 'Show question ' + n, exact:true}).click();
      await tab.playwright.domSnapshot();
      let state = await snapshotQuestion(tab);
      if (!state || state.number !== n) throw Error('Question navigation mismatch');
      const q = {number:n, initial:state, attempts:[]};
      const previous = out.questions.findIndex(q => q.number === n);
      if (previous >= 0) out.questions[previous] = q; else out.questions.push(q);
      for (let k = 0; k < state.buttons.length; k++) {
        if (state.buttons.every(b => b.disabled)) break;
        const option = state.buttons[k];
        if (!option || option.disabled) continue;
        await tab.playwright.getByRole('button', {name:option.label, exact:true}).click();
        await tab.playwright.domSnapshot();
        state = await snapshotQuestion(tab);
        q.attempts.push({selected:option.label, state});
      }
      q.final = state;
      q.informational = state.buttons.length === 0;
      q.resolved = q.informational || state.buttons.every(b => b.disabled);
      await fs.writeFile(dir + '/source.json', JSON.stringify(out, null, 2));
      if (!q.resolved) {out.errors.push('Unresolved ' + n); break;}
    } catch (e) {out.errors.push('Question ' + n + ': ' + e.message); break;}
  }
  await fs.writeFile(dir + '/source.json', JSON.stringify(out, null, 2));
  await fs.writeFile(dir + '/last-state.png', await tab.screenshot({fullPage:false}));
  return {slug, total, captured:out.questions.length, resolved:out.questions.filter(q => q.resolved).length, errors:out.errors};
}
