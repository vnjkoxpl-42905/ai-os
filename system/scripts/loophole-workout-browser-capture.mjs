/** User-authorized rendered-UI capture. No network, credentials or backend access.
 * Inject documented CUA operations from the current cua_repl session. This module
 * intentionally cannot discover a browser or invent selectors on its own.
 */
export function readDetailDOM(document, request = {kind: 'metadata'}) {
  const heading = document.querySelector('h1');
  const root = heading?.closest('header')?.parentElement;
  if (!root) throw new Error('Observed detail root not found; inspect current page');
  if (request.kind === 'length') return request.field === 'html' ? root.outerHTML.length : root.innerText.length;
  if (request.kind === 'slice') {
    const value = request.field === 'html' ? root.outerHTML : root.innerText;
    return value.slice(request.start, request.end);
  }
  return {
    name: heading.innerText,
    links: Array.from(root.querySelectorAll('a[href]'), a => ({text: a.innerText, url: a.href})),
    images: Array.from(root.querySelectorAll('img'), img => ({url: img.currentSrc || img.src, alt: img.alt})),
    sections: Array.from(root.querySelectorAll('h1,h2,h3,h4,h5,h6'), h => ({level: h.tagName, text: h.innerText})),
  };
}

export async function readDetailChunked(ui, chunkSize = 50000) {
  if (chunkSize > 50000 || chunkSize < 1) throw new Error('Use chunks between 1 and 50000 characters');
  const result = await ui.readDetailPart({kind: 'metadata'});
  for (const field of ['text', 'html']) {
    const length = await ui.readDetailPart({kind: 'length', field});
    const parts = [];
    for (let start = 0; start < length; start += chunkSize) {
      const part = await ui.readDetailPart({kind: 'slice', field, start, end: Math.min(length, start + chunkSize)});
      if (typeof part !== 'string' || part.includes('[Truncated]')) throw new Error(`Truncated ${field} chunk`);
      parts.push(part);
    }
    result[field] = parts.join('');
    if (result[field].length !== length) throw new Error(`Length mismatch rebuilding ${field}`);
    if (await ui.readDetailPart({kind: 'length', field}) !== length) throw new Error(`Page changed during ${field} capture`);
  }
  return result;
}

export function makeWorkoutCapture({ ui, checkpoint, observe, catalogUrl,
  pageButtons = [1, 2, 3, 4].map(number => ({number, name: `Page ${number}`})) }) {
  if (!ui || !checkpoint || !observe || !catalogUrl) throw new Error('Missing explicit capture adapters');
  const overviews = [], details = [], prepPoints = [], footnotes = [], failures = [];
  const flush = async () => checkpoint({overviews, details, prepPoints, footnotes, failures});
  const navigateIfNeeded = async url => {
    if (await ui.currentUrl() !== url) await ui.navigate(url);
  };
  async function retry(label, action) {
    try { return await action(); }
    catch (first) {
      await observe(await ui.refresh());
      try { return await action(); }
      catch (second) {
        failures.push({label, first: String(first), error: String(second)});
        await flush();
        throw second;
      }
    }
  }
  async function expandAll() {
    for (const name of ['Show More', 'Show more', 'Expand section']) {
      for (let steps = 0; ; steps++) {
        const count = await ui.countButton(name);
        if (!count) break;
        if (steps >= 200) throw new Error(`Expansion guard reached: ${name}`);
        await retry(`expand ${name}`, () => ui.clickButton(name, 0));
        await observe(await ui.refresh());
        if (await ui.countButton(name) >= count) throw new Error(`Expander did not disappear: ${name}`);
      }
    }
  }
  async function captureCatalog() {
    await navigateIfNeeded(catalogUrl);
    await observe(await ui.refresh());
    for (const page of pageButtons) {
      // Only these four page controls were observed. Stop and inspect if absent.
      if (await ui.isButtonEnabled(page.name)) {
        await retry(`page ${page.number}`, () => ui.clickButton(page.name));
      } else if (!await ui.isCurrentPage(page.number)) {
        throw new Error(`Disabled pagination button is not the selected page: ${page.name}`);
      }
      await observe(await ui.refresh());
      const observedRows = await ui.readOverviewRows();
      for (const observedRow of observedRows) {
        await retry(`overview page ${page.number}`, () => ui.openOverview(observedRow));
        await observe(await ui.refresh());
        const row = await ui.readExpandedOverview();
        if (!row?.name || !row?.text || !row?.html) throw new Error('Expanded row missing source content');
        const detailLink = row.links.find(link => link.url.includes('/workouts-and-routines/workouts/'));
        if (!detailLink) throw new Error(`No observed detail link: ${row.name}`);
        if (overviews.some(r => r.links.some(l => l.url === detailLink.url))) throw new Error(`Duplicate row: ${detailLink.url}`);
        overviews.push({page: page.number, ...row});
        await flush();
        // Iterate the observed row identities, so accordion auto-collapse cannot
        // accidentally send us back to the first already captured workout.
      }
    }
    return overviews;
  }
  async function capturePage(url, type) {
    await retry(`navigate ${url}`, () => navigateIfNeeded(url));
    await observe(await ui.refresh());
    await ui.waitForDetailHeading();
    await observe(await ui.refresh());
    if (await ui.isObservedSourceError()) {
      const value = await ui.readSourceError();
      const record = {url, ...value, status: 'source-error'};
      (type === 'prep' ? prepPoints : details).push(record);
      await flush();
      return record;
    }
    await expandAll();
    const value = await readDetailChunked(ui);
    if (!value?.name || !value?.text || !value?.html) throw new Error(`Empty captured page: ${url}`);
    const remaining = await ui.countButton('Show More') + await ui.countButton('Show more') + await ui.countButton('Expand section');
    const record = {url, ...value, status: 'captured', remaining_expanders: remaining};
    if (remaining) throw new Error(`Unexpanded source sections at ${url}`);
    (type === 'prep' ? prepPoints : details).push(record);
    await flush();
    if (type !== 'prep') {
      const triggers = await ui.readFootnoteTriggers();
      const entry = {name: value.name, url, count: triggers.length, notes: []};
      for (const trigger of triggers) {
        await retry(`reveal footnote ${url}`, () => ui.revealFootnote(trigger));
        await observe(await ui.refresh());
        const note = await ui.readVisibleFootnote();
        if (!note?.text || !note?.html) throw new Error(`Empty inline footnote: ${url}`);
        entry.notes.push(note);
        await ui.dismissFootnote();
      }
      footnotes.push(entry);
      await flush();
    }
    return record;
  }
  async function captureDetails(sourceOverviews = overviews) {
    for (const row of sourceOverviews) {
      const url = row.links.find(l => l.url.includes('/workouts-and-routines/workouts/'))?.url;
      if (!url) throw new Error(`No observed workout URL: ${row.name}`);
      if (!details.some(d => d.url === url)) await capturePage(url, 'workout');
    }
    return details;
  }
  async function capturePrepPoints(sourceOverviews = overviews, sourceDetails = details) {
    const urls = [...new Set([...sourceOverviews, ...sourceDetails].flatMap(r => r.links || [])
      .map(l => l.url).filter(url => url.includes('/prep-map/')))];
    for (const url of urls) if (!prepPoints.some(p => p.url === url)) await capturePage(url, 'prep');
    return prepPoints;
  }
  return {captureCatalog, captureDetails, capturePrepPoints, capturePage,
    state: {overviews, details, prepPoints, footnotes, failures}};
}
