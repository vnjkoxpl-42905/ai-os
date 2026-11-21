/** Rendered-UI capture only. Inject documented operations from an authorized CUA tab.
 * No network, credentials, guessed URLs, hidden stores, or browser discovery.
 */
export function readRoutineDOM(document, request = {kind: 'metadata'}) {
  const heading = document.querySelector('h1');
  const root = heading?.closest('header')?.parentElement;
  if (!root) throw new Error('Observed routine detail root missing; inspect the page');
  if (request.kind === 'length' || request.kind === 'slice') {
    const value = request.field === 'html' ? root.outerHTML : root.innerText;
    return request.kind === 'length' ? value.length : value.slice(request.start, request.end);
  }
  return {name: heading.innerText,
    links: Array.from(root.querySelectorAll('a[href]'), a => ({text:a.innerText,url:a.href})),
    images: Array.from(root.querySelectorAll('img'), i => ({url:i.currentSrc || i.src,alt:i.alt})),
    sections: Array.from(root.querySelectorAll('h1,h2,h3,h4,h5,h6'), h => ({level:h.tagName,text:h.innerText}))};
}

/** readPart handles metadata, length and slice requests for the SAME observed root. */
export async function captureChunked(readPart, chunkSize = 50000) {
  if (!Number.isInteger(chunkSize) || chunkSize < 1 || chunkSize > 50000) throw new Error('Chunk size must be 1..50000');
  const record = await readPart({kind:'metadata'});
  for (const field of ['text','html']) {
    const length = await readPart({kind:'length',field});
    if (!Number.isSafeInteger(length) || length < 0) throw new Error(`Invalid ${field} length`);
    const parts = [];
    for (let start=0; start<length; start+=chunkSize) {
      const end = Math.min(length,start+chunkSize);
      const part = await readPart({kind:'slice',field,start,end});
      if (typeof part !== 'string' || part.length !== end-start || part.includes('[Truncated]')) throw new Error(`Incomplete ${field} slice at ${start}`);
      parts.push(part);
    }
    record[field] = parts.join('');
    if (record[field].length !== length || await readPart({kind:'length',field}) !== length) throw new Error(`Changed or incomplete ${field}`);
  }
  return record;
}

export function makeRoutineCapture({ui,checkpoint,observe,catalogUrl,
  pageButtons=[1,2,3].map(number=>({number,name:`Page ${number}`})),initialState={}}) {
  if (!ui || !checkpoint || !observe || !catalogUrl) throw new Error('Explicit capture adapters required');
  const state = Object.fromEntries(['overviews','details','facets','footnotes','failures'].map(key=>[key,[...(initialState[key] || [])]]));
  const flush = () => checkpoint(state);
  const refresh = async () => observe(await ui.refresh());
  const navigate = async url => {if (await ui.currentUrl() !== url) await ui.navigate(url); await refresh();};
  async function attempt(label,action) {
    try {return await action();} catch (first) {
      await refresh();
      try {return await action();} catch (error) {
        state.failures.push({label,first:String(first),error:String(error)}); await flush(); throw error;
      }
    }
  }
  async function expandAll() {
    for (const name of ['Show More','Show more','Expand section']) {
      for (let n=0; await ui.countButton(name); n++) {
        if (n>=200) throw new Error(`Expansion guard: ${name}`);
        const before=await ui.countButton(name);
        await attempt(`expand ${name}`,()=>ui.clickButton(name,0)); await refresh();
        if (await ui.countButton(name)>=before) throw new Error(`Expander remained: ${name}`);
      }
    }
  }
  const detailUrl = row => row.links?.find(l=>l.url.includes('/workouts-and-routines/routines/'))?.url;
  async function captureCatalog() {
    await navigate(catalogUrl);
    for (const page of pageButtons) {
      if (await ui.isButtonEnabled(page.name)) await attempt(page.name,()=>ui.clickButton(page.name));
      else if (!await ui.isCurrentPage(page.number)) throw new Error(`Unexpected disabled ${page.name}`);
      await refresh();
      for (const identity of await ui.readOverviewRows()) {
        await attempt('open routine overview',()=>ui.openOverview(identity)); await refresh();
        const row = await ui.readExpandedOverview();
        const url = detailUrl(row);
        if (!row.name || !row.text || !row.html || !url) throw new Error('Incomplete routine overview');
        const existing=state.overviews.find(r=>detailUrl(r)===url);
        if (existing && existing.page!==page.number) throw new Error(`Duplicate routine across pages: ${url}`);
        if (!existing) {state.overviews.push({page:page.number,...row}); await flush();}
      }
    }
    return state.overviews;
  }
  async function captureRoutine(url) {
    // Only observed listing anchors may be navigated by this helper.
    if (!state.overviews.some(r=>detailUrl(r)===url)) throw new Error('Routine URL not observed in captured catalog');
    const saved=state.details.find(r=>r.url===url && r.status==='captured');
    if (saved) return saved;
    await attempt(`navigate ${url}`,()=>navigate(url));
    await ui.waitForDetailHeading(); await refresh(); await expandAll();
    const identities = await ui.readScheduleRows();
    if (!identities.length) throw new Error(`No observed schedule rows: ${url}`);
    // Ordered indices are identity. Repeated workout names MUST NOT be deduplicated.
    const sequence=[];
    for (let index=0; index<identities.length; index++) {
      const identity=identities[index];
      await attempt(`schedule row ${index+1}`,()=>ui.openScheduleRow(identity,index));
      await refresh(); await expandAll();
      const step=await captureChunked(request=>ui.readSchedulePart(identity,index,request));
      if (!step.name || !step.text || !step.html) throw new Error(`Empty schedule step ${index+1}`);
      sequence.push({order:index+1,...step});
      // Partial state is separate from completed details, so resume cannot skip it.
      state.partial={url,sequence:[...sequence],expected_steps:identities.length}; await flush();
    }
    const detail=await captureChunked(request=>ui.readDetailPart(request));
    const record={url,...detail,sequence,expected_steps:identities.length,status:'captured',
      sequence_authority:'sequence array; parent HTML may contain only the final open schedule row'};
    if (sequence.length!==identities.length) throw new Error('Schedule coverage mismatch');
    const notes=[];
    for (const trigger of await ui.readFootnoteTriggers()) {
      await ui.revealFootnote(trigger); await refresh();
      const note=await ui.readVisibleFootnote();
      if (!note?.text || !note?.html) throw new Error('Empty routine footnote');
      notes.push(note); await ui.dismissFootnote();
    }
    state.footnotes.push({url,count:notes.length,notes});
    state.details.push(record); delete state.partial; await flush(); return record;
  }
  async function captureDetails() {for (const row of state.overviews) await captureRoutine(detailUrl(row)); return state.details;}
  async function captureFacets(observedGroups) {
    for (const group of observedGroups) {
      await ui.openFilter(group); await refresh();
      const value=await ui.readOpenFilter(group);
      if (!value?.text || !value?.html || !Array.isArray(value.options)) throw new Error(`Incomplete filter: ${group}`);
      const index=state.facets.findIndex(f=>f.group===group);
      const record={group,...value};
      if (index<0) state.facets.push(record); else state.facets[index]=record;
      await ui.closeFilter(group); await flush();
    }
    return state.facets;
  }
  return {state,captureCatalog,captureRoutine,captureDetails,captureFacets};
}
