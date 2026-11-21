/* Focused offline render proof for the actual generated Amanda recap. */
const fs = require('fs');
const path = require('path');
const assert = require('assert/strict');
const { chromium } = require('C:/Users/Joshu/dev/ai-os-projects/lsatu-role-home-20261022/node_modules/playwright');

const folder = __dirname;
const htmlPath = path.join(folder, 'recap.html');
const output = path.join(folder, 'render-evidence');
const fileUrl = require('url').pathToFileURL(htmlPath).href;
const words = text => text.trim().split(/\s+/).filter(Boolean).length;

(async () => {
  fs.mkdirSync(output, { recursive: true });
  const browser = await chromium.launch({ channel: 'msedge', headless: true });
  const report = { artifact: htmlPath, checks: [], screenshots: [], errors: [], counts: {} };
  try {
    const page = await browser.newPage({ viewport: { width: 1280, height: 900 }, deviceScaleFactor: 1 });
    page.on('pageerror', error => report.errors.push(String(error)));
    page.on('console', message => { if (message.type() === 'error' || message.type() === 'warning') report.errors.push(message.text()); });
    await page.goto(fileUrl);
    report.counts.defaultVisibleWordsBeforeInteraction = words(await page.locator('body').innerText());
    report.counts.coreVisibleWords = report.counts.defaultVisibleWordsBeforeInteraction;
    assert.equal(await page.locator('h1').count(), 1);
    assert.equal(await page.locator('meta[name="lsatu-interactive-lesson"]').getAttribute('content'), 'amanda-2026-10-21-rules-and-facts');
    for (const id of ['sentence-types', 'two-jobs', 'fact-cases', 'same-pieces', 'and-trap', 'practice', 'homework']) {
      assert.equal(await page.locator('#' + id).count(), 1, 'required section ' + id);
    }
    assert.equal(await page.locator('#sentence-types tbody tr').count(), 6, 'six explained sentence types');
    assert.equal(await page.locator('[data-fact-case]').count(), 4, 'four separate facts');
    for (const type of ['Fact', 'Rule', 'Causal', 'Correlation', 'Normative', 'Quantity']) {
      assert.ok((await page.locator('#sentence-types').innerText()).includes(type), type + ' definition');
    }
    assert.ok(/(?:types|descriptions|categories) (?:can |may )?overlap|(?:sentence|example) (?:can|may) (?:fit|be|have|belong)[^.]*more than one/i.test(await page.locator('#sentence-types').innerText()), 'visible declarative overlap caveat');
    const stateTeaching = [];
    const teachingTexts = locator => locator.evaluateAll(nodes => nodes.map(node => {
      const walker = document.createTreeWalker(node, NodeFilter.SHOW_TEXT);
      const parts = [];
      while (walker.nextNode()) parts.push(walker.currentNode.textContent);
      return parts.join(' ');
    }));
    const teachingSelector = 'h1,h2,h3,h4,p,caption,th,td,summary,.kicker,.sec-kicker,.cs-half,.result,.callout,.quote,li';
    const teachingBlocksFrom = (targetPage, visibleOnly = false) => targetPage.locator(teachingSelector).evaluateAll((nodes, {visibleOnly,teachingSelector}) => {
      const excluded = 'button,[role="tablist"],svg,.concept-mobile,.trace-mobile,.enhanced-controls,.sr-only,#application-explorer h3,#application-prompt,#application-announcement,#application-result,#application-conclusion';
      return nodes.filter(node => !node.closest(excluded) && (!visibleOnly || node.getClientRects().length) && !node.parentElement.closest(teachingSelector)).map(node => {
        const clone = node.cloneNode(true);
        clone.querySelectorAll(excluded).forEach(child => child.remove());
        const walker = document.createTreeWalker(clone,NodeFilter.SHOW_TEXT);
        const parts = [];
        while(walker.nextNode()) parts.push(walker.currentNode.textContent);
        return parts.join(' ');
      }).filter(text => text.trim());
    }, {visibleOnly,teachingSelector});
    const captureState = async () => stateTeaching.push(...await teachingBlocksFrom(page,true));
    const tabs = page.locator('#concept-explorer [role="tab"]');
    assert.equal(await tabs.count(), 6, 'six accessible concept tabs');
    for (const key of ['fact','rule','causal','correlation','normative','quantity']) {
      const tab = page.locator(`#concept-explorer [role="tab"][data-concept="${key}"]`);
      await tab.click();
      assert.equal(await tab.getAttribute('aria-selected'), 'true');
      assert.equal(await tab.getAttribute('tabindex'), '0');
      assert.equal(await page.locator('#concept-explorer [role="tab"][aria-selected="true"]').count(), 1);
      const panel = page.locator('#panel-' + key);
      assert.ok(await panel.isVisible(), 'selected concept panel ' + key);
      assert.equal(await tab.getAttribute('aria-controls'), 'panel-' + key);
      assert.ok(words(await panel.innerText()) >= 20, 'substantive concept explanation ' + key);
      assert.ok(await panel.locator('svg').count() >= 1, 'purposeful illustration ' + key);
      await captureState();
    }
    await tabs.last().focus();
    await page.keyboard.press('Home');
    assert.equal(await tabs.first().getAttribute('aria-selected'), 'true');
    await page.keyboard.press('ArrowRight');
    assert.equal(await tabs.nth(1).getAttribute('aria-selected'), 'true');
    await page.keyboard.press('ArrowLeft');
    assert.equal(await tabs.first().getAttribute('aria-selected'), 'true');
    await page.keyboard.press('End');
    assert.equal(await tabs.last().getAttribute('aria-selected'), 'true');
    report.checks.push('six illustrated panels, selected/linked states, roving tabindex and Home/End/arrow keyboard navigation');
    const association = page.locator('#panel-correlation .association');
    assert.equal(await association.count(), 1, 'one association connector rather than equals sign');
    assert.equal(await association.getAttribute('marker-end'), null, 'association does not have causal arrow');
    assert.ok(await association.getAttribute('stroke-dasharray'), 'association is dotted');
    assert.ok((await page.locator('#panel-correlation svg').textContent()).includes('Associated'), 'association explicitly labelled');
    const table = page.locator('#sentence-types table');
    assert.equal(await table.getAttribute('role'), 'table');
    assert.equal(await table.locator('th[scope="col"][role="columnheader"]').count(), 4);
    assert.equal(await table.locator('tbody tr[role="row"]').count(), 6);
    assert.equal(await table.locator('tbody td[role="cell"]').count(), 24);
    for (const key of ['left-true','right-false','right-true','left-false']) {
      const choice = page.locator(`[data-supplied-fact="${key}"]`);
      await choice.click();
      assert.equal(await choice.getAttribute('aria-pressed'), 'true');
      assert.equal(await page.locator('[data-supplied-fact][aria-pressed="true"]').count(), 1);
      assert.ok(await page.locator('#application-result').isHidden(), 'switch resets revealed answer ' + key);
      assert.equal(await page.locator('#show-application-reasoning').getAttribute('aria-expanded'), 'false');
      assert.equal(await page.locator('#application-conclusion').innerText(), 'Think first.');
      await page.locator('#show-application-reasoning').click();
      assert.ok(await page.locator('#application-result').isVisible());
      const expected = await page.locator(`[data-fact-case="${key}"] p`).innerText();
      assert.equal(await page.locator('#application-result').innerText(), expected);
      assert.equal(await page.locator('#contrapositive-rule').isVisible(), key === 'right-false');
      assert.equal(await page.locator('#application-connector').getAttribute('data-direction'), ['left-true','right-false'].includes(key) ? 'forward' : null);
      await captureState();
    }
    report.checks.push('all four fact choices reset hidden answers and reveal authored explanations; only negative requirement shows contrapositive');
    const assertFocus = async control => {
      await control.focus();
      await control.press('Tab');
      await page.keyboard.press('Shift+Tab');
      const state = await control.evaluate(node => ({focused:document.activeElement===node,width:parseFloat(getComputedStyle(node).outlineWidth),style:getComputedStyle(node).outlineStyle}));
      assert.ok(state.focused && state.width >= 2 && state.style !== 'none', 'keyboard control visible focus');
    };
    for (const key of ['Enter','Space']) {
      const selectedFact = page.locator('[data-supplied-fact="right-true"]');
      await page.locator('[data-supplied-fact="left-true"]').click();
      await assertFocus(selectedFact);
      await selectedFact.press(key);
      assert.equal(await selectedFact.getAttribute('aria-pressed'),'true','fact choice keyboard '+key);
      const reasoning = page.locator('#show-application-reasoning');
      await assertFocus(reasoning);
      await reasoning.press(key);
      assert.equal(await reasoning.getAttribute('aria-expanded'),'true','reasoning keyboard '+key);
      assert.ok(await page.locator('#application-result').isVisible());
      await reasoning.press(key);
      assert.equal(await reasoning.getAttribute('aria-expanded'),'false','reasoning closes keyboard '+key);
    }
    const trail = page.locator('[data-given-fact="trail"]');
    const guide = page.locator('[data-given-fact="guide"]');
    for (const state of ['00','10','01','11']) {
      for (const [index, button] of [trail,guide].entries()) {
        if ((await button.getAttribute('aria-pressed') === 'true') !== (state[index] === '1')) await button.click();
        assert.equal(await button.locator('.supply-status').innerText(), state[index] === '1' ? 'Supplied' : 'Not supplied (unknown)');
      }
      const active = page.locator(`[data-and-state="${state}"]`);
      assert.ok(await active.isVisible());
      assert.equal(await page.locator('[data-and-state]:visible').count(), 1);
      assert.match(await active.innerText(), state === '11' ? /hike must go ahead/i : /unknown/i);
      await captureState();
    }
    report.checks.push('all four AND supplied-fact combinations distinguish unknown from false and require both for guarantee');
    for (const key of ['Enter','Space']) {
      await assertFocus(trail);
      const prior = await trail.getAttribute('aria-pressed');
      await trail.press(key);
      assert.notEqual(await trail.getAttribute('aria-pressed'),prior,'AND toggle keyboard '+key);
      await trail.press(key);
      assert.equal(await trail.getAttribute('aria-pressed'),prior,'AND toggle restored keyboard '+key);
    }
    report.checks.push('fact choices, reasoning reveal and AND toggle passed Tab focus, Enter and Space');
    await page.locator('#trace-chain button').click();
    await page.waitForTimeout(100);
    assert.ok(await page.locator('.trace-line').evaluateAll(nodes => nodes.some(n => n.getAnimations().some(a => a.playState === 'running'))), 'finite trace starts');
    await page.waitForTimeout(1400);
    assert.equal(await page.locator('.trace-line').evaluateAll(nodes => nodes.flatMap(n => n.getAnimations()).filter(a => a.playState === 'running').length), 0, 'trace ends');
    await page.locator('#trace-chain button').click();
    await page.waitForTimeout(100);
    await page.emulateMedia({ reducedMotion: 'reduce' });
    await page.waitForTimeout(100);
    assert.equal(await page.evaluate(() => document.getAnimations().filter(a => a.playState === 'running').length), 0, 'dynamic reduced motion cancels every running document animation, including emphasis');
    await page.emulateMedia({ reducedMotion: 'no-preference' });
    report.checks.push('chain trace runs finitely, replays, and cancels on dynamic reduced-motion change');
    report.counts.interactedStateVisibleWords = words(await page.locator('body').innerText());
    const summaries = page.locator('details > summary:visible');
    const count = await summaries.count();
    assert.ok(count >= 6, 'meaningful explanation disclosures');
    for (let i = 0; i < count; i++) {
      const summary = summaries.nth(i);
      const disclosure = summary.locator('..');
      const initial = await disclosure.getAttribute('open') !== null;
      await summary.click();
      assert.equal(await disclosure.getAttribute('open') !== null, !initial, 'pointer opens/closes reveal ' + i);
      await summary.focus();
      await summary.press('Tab');
      await page.keyboard.press('Shift+Tab');
      const focus = await summary.evaluate(element => ({
        focused: document.activeElement === element,
        outlineWidth: parseFloat(getComputedStyle(element).outlineWidth),
        outlineStyle: getComputedStyle(element).outlineStyle,
      }));
      assert.ok(focus.focused && focus.outlineWidth >= 2 && focus.outlineStyle !== 'none', 'visible focus ' + i);
      await summary.press('Enter');
      assert.equal(await disclosure.getAttribute('open') !== null, initial, 'Enter toggles reveal ' + i);
      await summary.press('Space');
      assert.equal(await disclosure.getAttribute('open') !== null, !initial, 'Space toggles reveal ' + i);
      await summary.press('Enter');
      assert.equal(await disclosure.getAttribute('open') !== null, initial, 'restored reveal ' + i);
    }
    report.checks.push(`${count} native disclosures passed pointer, Enter, Space and visible-focus checks`);
    report.counts.disclosures = count;
    for (let i = 0; i < count; i++) {
      const summary = summaries.nth(i);
      if (await summary.locator('..').getAttribute('open') === null) await summary.click();
    }
    report.counts.allExplanationsWords = words(await page.locator('body').innerText());
    const allTeaching = await page.locator('body').innerText();
    const canonicalFile = path.resolve(folder, '../../students/amanda/recaps/2026-10-21-recap.md');
    const fullCanonical = fs.readFileSync(canonicalFile, 'utf8').replace(/\r\n/g, '\n');
    const beforeCanonical = fs.readFileSync(path.join(folder, 'before-refinement-canonical-recap.md'), 'utf8').replace(/\r\n/g, '\n');
    const divider = '<!-- PRIVATE CONTINUATION';
    assert.ok(fullCanonical.split(divider)[1].startsWith(beforeCanonical.split(divider)[1]), 'prior private continuation retained exactly');
    assert.ok(/^posted: false$/m.test(fullCanonical) && /^status: draft$/m.test(fullCanonical), 'canonical remains unposted draft');
    const canonical = fullCanonical.split(divider)[0].replace(/^---[\s\S]*?---/, '');
    const forbidden = /\b(?:classif(?:y|ies|ied|ication)|statements?|establish(?:es|ed|ing)?|preserv(?:e|es|ed|ing)|stipulated|briefing|intake|chunks?|beats?|phases?|patterns?|cards?|targets?)\b|\bmoves?\b(?!\s+on\b)|concept lesson|the other one|[—–~]/ig;
    for (const [label, text] of [['HTML teaching', allTeaching], ['canonical student text', canonical]]) {
      assert.deepEqual(text.match(forbidden) || [], [], label + ' copy-correction vocabulary/punctuation');
    }
    const normalize = text => (text.normalize('NFKC').toLowerCase().match(/[\p{L}\p{N}]+/gu) || []).join(' ');
    const canonicalWords = normalize(canonical);
    for (const status of ['Think first.', 'Not supplied (unknown)', 'Supplied']) {
      assert.ok(fs.readFileSync(path.join(folder, 'recap.src.html'), 'utf8').includes(status), 'authored HTML includes dynamic status ' + status);
    }
    let headingPosition = -1;
    for (const heading of await teachingTexts(page.locator('h1,h2'))) {
      const next = canonicalWords.indexOf(normalize(heading), headingPosition + 1);
      assert.ok(next > headingPosition, 'canonical section order ' + heading);
      headingPosition = next;
    }
    const teachingBlocks = [...stateTeaching, ...await teachingBlocksFrom(page)];
    for (const block of teachingBlocks) {
      assert.ok(canonicalWords.includes(normalize(block)), 'canonical includes teaching block: ' + block.slice(0, 120));
    }
    report.checks.push('all visible/revealed teaching and every interactive state match canonical Markdown; student copy vocabulary and punctuation pass');
    for (let i = count - 1; i >= 0; i--) {
      const summary = summaries.nth(i);
      if (await summary.locator('..').getAttribute('open') !== null) await summary.click();
    }
    for (const width of [1280, 838, 390, 320]) {
      await page.setViewportSize({ width, height: 900 });
      const size = await page.evaluate(() => ({ scroll: document.documentElement.scrollWidth, client: document.documentElement.clientWidth }));
      assert.ok(size.scroll <= size.client + 1, 'no document overflow at ' + width + ': ' + JSON.stringify(size));
      report.checks.push('no horizontal document overflow at ' + width + 'px');
    }
    await page.setViewportSize({ width: 838, height: 900 });
    await page.locator('header.hero').screenshot({ path: path.join(output, 'after-hero-desktop.png') });
    report.screenshots.push('after-hero-desktop.png');
    for (const id of ['sentence-types', 'two-jobs', 'fact-cases', 'same-pieces', 'and-trap', 'practice', 'homework']) {
      const image = `after-${id}-desktop.png`;
      await page.locator('#' + id).screenshot({ path: path.join(output, image) });
      report.screenshots.push(image);
    }
    await page.setViewportSize({ width: 390, height: 844 });
    await page.locator('header.hero').screenshot({ path: path.join(output, 'after-hero-phone.png') });
    report.screenshots.push('after-hero-phone.png');
    for (const id of ['sentence-types', 'two-jobs', 'fact-cases', 'same-pieces', 'and-trap', 'practice', 'homework']) {
      const image = `after-${id}-phone.png`;
      await page.locator('#' + id).screenshot({ path: path.join(output, image) });
      report.screenshots.push(image);
    }
    for (const width of [838,390]) {
      await page.setViewportSize({ width, height: 844 });
      for (const key of ['fact','rule','causal','correlation','normative','quantity']) {
        await page.locator(`[role="tab"][data-concept="${key}"]`).click();
        const image = `interactive-concept-${key}-${width}.png`;
        await page.locator('#concept-explorer').screenshot({path:path.join(output,image)});
        report.screenshots.push(image);
      }
      for (const key of ['left-true','right-false','right-true','left-false']) {
        await page.locator(`[data-supplied-fact="${key}"]`).click();
        await page.locator('#show-application-reasoning').click();
        if (width === 390) {
          const transform = await page.locator('#application-connector').evaluate(node => getComputedStyle(node).transform);
          if (['left-true','right-false'].includes(key)) assert.notEqual(transform, 'none', 'valid arrow rotates downward on phone');
          else assert.equal(transform, 'none', 'invalid question mark stays upright on phone');
        }
        const image = `interactive-fact-${key}-${width}.png`;
        await page.locator('#application-explorer').screenshot({path:path.join(output,image)});
        report.screenshots.push(image);
      }
      for (const state of ['00','10','01','11']) {
        for (const [index,button] of [trail,guide].entries()) {
          if ((await button.getAttribute('aria-pressed') === 'true') !== (state[index] === '1')) await button.click();
        }
        const image = `interactive-and-${state}-${width}.png`;
        await page.locator('#and-explorer').screenshot({path:path.join(output,image)});
        report.screenshots.push(image);
      }
    }
    await page.addStyleTag({ content: 'body { font-size: 200% !important; } p,li,td,th,summary,details,.what,.test { font-size: inherit !important; }' });
    const enlarged = await page.evaluate(() => ({ scroll: document.documentElement.scrollWidth, client: document.documentElement.clientWidth }));
    assert.ok(enlarged.scroll <= enlarged.client + 1, 'no overflow at enlarged text');
    await page.screenshot({ path: path.join(output, 'after-enlarged-phone.png'), fullPage: true });
    report.checks.push('390px enlarged-text layout has no horizontal document overflow');
    await page.emulateMedia({ reducedMotion: 'reduce' });
    const motion = await page.locator('summary').first().evaluate(element => ({ transition: getComputedStyle(element).transitionDuration, animation: getComputedStyle(element).animationDuration }));
    assert.ok(motion.transition.split(',').every(value => parseFloat(value) === 0), 'reduced-motion transition');
    report.checks.push('reduced-motion disables disclosure-control transitions');

    const noJs = await browser.newContext({ javaScriptEnabled: false, viewport: { width: 390, height: 844 } });
    const noJsPage = await noJs.newPage();
    await noJsPage.goto(fileUrl);
    let teachingPosition = -1;
    const authoredTeaching = await teachingBlocksFrom(noJsPage);
    for (const block of authoredTeaching) {
      const normalized = normalize(block);
      const next = canonicalWords.indexOf(normalized, teachingPosition + 1);
      assert.ok(next > teachingPosition, 'canonical sequential teaching order: ' + block.slice(0,120));
      teachingPosition = next + normalized.length - 1;
    }
    report.checks.push(`${authoredTeaching.length} authored teaching blocks match canonical in sequential order; UI chrome and duplicate illustration labels excluded`);
    report.counts.allAuthoredWordsIncludingOptionalPanelsAndFallback = words(await noJsPage.locator('body').evaluate(body => {
      const clone = body.cloneNode(true);
      clone.querySelectorAll('script,style').forEach(node => node.remove());
      return clone.textContent;
    }));
    assert.equal(await noJsPage.locator('#sentence-types tbody tr').count(), 6);
    for (const id of ['concept-explorer','application-explorer','and-explorer']) assert.ok(await noJsPage.locator('#'+id).isHidden(), 'enhancement hidden without JS '+id);
    assert.ok(await noJsPage.locator('#fact-case-fallback').isVisible(), 'native fact fallback visible without JS');
    for (const value of ['left-true', 'right-false', 'right-true', 'left-false']) {
      const item = noJsPage.locator(`[data-fact-case="${value}"]`);
      await item.locator('summary').click();
      assert.notEqual(await item.getAttribute('open'), null, 'native fact answer opens without JS ' + value);
      assert.ok(words(await item.innerText()) > 15, 'reasoned fact-case answer without JS ' + value);
    }
    report.checks.push('six definitions and all four fact-case explanations reachable with JavaScript disabled');
    await noJs.close();
    assert.equal(report.errors.length, 0, 'clean browser console/page errors');

    const source = fs.readFileSync(path.join(folder, 'recap.src.html'), 'utf8');
    const built = fs.readFileSync(htmlPath, 'utf8');
    const body = text => text.match(/<body[^>]*>([\s\S]*?)<\/body>/i)[1].replace(/\r\n/g, '\n');
    assert.equal(body(source), body(built), 'generated body matches authored source');
    assert.ok(Buffer.byteLength(built, 'utf8') < 500000, 'under publisher size limit');
    assert.ok(!/\b(?:src|href)\s*=\s*["']https?:/i.test(built), 'no external asset references');
    assert.ok(!built.includes('PRIVATE CONTINUATION'), 'no private record in delivered HTML');
    report.checks.push('source/generated body parity, stable marker, self-contained assets and size verified');
    report.status = 'PASS';
    fs.writeFileSync(path.join(output, 'verification.json'), JSON.stringify(report, null, 2));
    console.log(JSON.stringify(report, null, 2));
  } finally {
    await browser.close();
  }
})().catch(error => { console.error(error); process.exitCode = 1; });

