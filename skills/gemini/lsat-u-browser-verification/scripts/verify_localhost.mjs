// C:\Users\Joshu\Tools\LSATU-Agent\verify_localhost.mjs
// Phase 8: Verify Localhost Dev Server via Agent Browser CDP

import { createRequire } from 'module';
const require = createRequire('c:/Users/Joshu/dev/ai-os/projects/lsatu/package.json');
const { chromium } = require('playwright-core');

const LOCAL_URL = 'http://localhost:8080/classroom/drill?section=lr';
const SCREENSHOT_PATH = 'C:/Users/Joshu/Tools/LSATU-Agent/localhost_drill.png';

console.log('Connecting to Agent Chrome on 127.0.0.1:9223...');
const browser = await chromium.connectOverCDP('http://127.0.0.1:9223');
const context = browser.contexts()[0] || await browser.newContext();

// Create new page or use existing
const page = await context.newPage();

const consoleErrors = [];
page.on('console', msg => {
    if (msg.type() === 'error') {
        consoleErrors.push(msg.text());
    }
});

console.log(`Navigating to ${LOCAL_URL}...`);
await page.goto(LOCAL_URL, { waitUntil: 'domcontentloaded', timeout: 30000 });
await page.waitForTimeout(4000);

const title = await page.title();
const url = page.url();
console.log(`Page Title: "${title}", URL: "${url}"`);

const pageStats = await page.evaluate(() => {
    const headings = Array.from(document.querySelectorAll('h1, h2, h3')).map(h => h.innerText.trim()).filter(Boolean);
    const buttons = Array.from(document.querySelectorAll('button')).map(b => b.innerText.trim()).filter(Boolean);
    const cards = Array.from(document.querySelectorAll('[class*="card"], [class*="observatory"], [class*="hero"]')).length;
    return {
        headings: headings.slice(0, 5),
        sampleButtons: buttons.slice(0, 5),
        cardsCount: cards,
        bodyHtmlLength: document.body ? document.body.innerHTML.length : 0
    };
});

console.log('DOM Evaluation:');
console.log(JSON.stringify(pageStats, null, 2));

console.log(`Console Errors (${consoleErrors.length}):`, consoleErrors.slice(0, 3));

await page.setViewportSize({ width: 1440, height: 900 });
await page.screenshot({ path: SCREENSHOT_PATH });
console.log(`Screenshot saved to ${SCREENSHOT_PATH}`);

// Close tab only, not browser
await page.close();
await browser.close().catch(() => {});
console.log('Localhost dev server verification complete.');
