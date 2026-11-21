const { chromium } = require('C:/Users/Joshu/dev/ai-os-projects/lsatu-role-home-20261022/node_modules/playwright');
const fs = require('fs');
const path = require('path');
const rejected = ['candidate assumption', 'two complete conditions', 'grammatical shape', 'recognition drill', 'step zero', 'the finalist', 'two useful roles'];
(async () => {
  const browser = await chromium.launch({channel: 'msedge', headless: true});
  const results = [];
  try {
    for (const width of [1100, 390]) {
      for (const name of ['recap', 'primer-negation-station', 'necessary-assumption']) {
        const page = await browser.newPage({viewport: {width, height: 850}});
        const pageErrors = [], consoleErrors = [];
        page.on('pageerror', error => pageErrors.push(error.message));
        page.on('console', message => {if (message.type() === 'error') consoleErrors.push(message.text());});
        await page.goto('file:///' + path.join(__dirname, name + '.html').replaceAll('\\', '/'));
        if (await page.evaluate(() => document.documentElement.scrollWidth > innerWidth)) throw Error('Overflow: ' + name);
        // textContent includes unrevealed answers; innerText checks the initial visible surface.
        const copy = await page.evaluate(() => ({title: document.title, visible: document.body.innerText, all: document.body.textContent}));
        for (const surface of Object.values(copy)) {
          for (const phrase of rejected) if (surface.toLowerCase().includes(phrase)) throw Error('Rejected phrase: ' + phrase);
          if (/\bmanual\b/i.test(surface)) throw Error('Internal design name');
        }
        if (name === 'recap') {
          for (const phrase of ['probably go to Tokyo', 'Sufficient assumption', '2026-10-28', '2026-11-01']) if (!copy.all.includes(phrase)) throw Error('Missing reviewed teaching/date: ' + phrase);
        }
        if (name === 'primer-negation-station' && (!copy.all.includes('both be false') || !copy.all.includes('both be true'))) throw Error('Missing two-way negation check');
        for (const chip of await page.locator('.chip').all()) {
          await chip.click(); if (await chip.getAttribute('aria-expanded') !== 'true') throw Error('click');
          await chip.focus(); await page.keyboard.press('Enter'); if (await chip.getAttribute('aria-expanded') !== 'false') throw Error('Enter');
          await page.keyboard.press('Space'); if (await chip.getAttribute('aria-expanded') !== 'true') throw Error('Space');
        }
        for (const detail of await page.locator('details').all()) {
          await detail.locator('summary').click(); if (!await detail.evaluate(element => element.open)) throw Error('details');
        }
        if (pageErrors.length || consoleErrors.length) throw Error(JSON.stringify({pageErrors, consoleErrors}));
        await page.screenshot({path: path.join(__dirname, `${name}-accuracy-${width}.png`), fullPage: true});
        if (name === 'recap') await page.locator('section').nth(2).screenshot({path: path.join(__dirname, `claude-fixed-strength-${width}.png`)});
        results.push({name, width, chips: await page.locator('.chip').count(), details: await page.locator('details').count(), pageErrors, consoleErrors, phraseScan: 'title, initial visible text and all hidden answers', reviewedContentAssertions: 'passed'});
        await page.close();
      }
    }
  } finally { await browser.close(); }
  fs.writeFileSync(path.join(__dirname, 'accuracy-verification.generated.json'), JSON.stringify({results, limits: 'Layout, console, interactions and scoped phrase/content assertions checked. Voice and teaching emphasis reviewed by human-readable source comparison; these tests cannot certify voice.'}, null, 2));
  console.log(JSON.stringify(results));
})().catch(error => { console.error(error); process.exitCode = 1; });
