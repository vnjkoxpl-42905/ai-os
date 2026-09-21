// C:\Users\Joshu\Tools\LSATU-Agent\verify_control_drill.mjs
// Phase 7: Comprehensive Read-Only Control Verification on /classroom/drill?section=lr

import { createRequire } from 'module';
const require = createRequire('c:/Users/Joshu/dev/ai-os/projects/lsatu/package.json');
const { chromium } = require('playwright-core');

const TARGET_URL = 'https://lsatprep.study/classroom/drill?section=lr';

console.log('Connecting to Chrome on 127.0.0.1:9223...');
const browser = await chromium.connectOverCDP('http://127.0.0.1:9223');
const context = browser.contexts()[0] || await browser.newContext();
const page = context.pages().find(p => p.url().includes('lsatprep.study')) || await context.newPage();

// 1. Collect Console Messages
const consoleLogs = [];
page.on('console', msg => {
    consoleLogs.push({ type: msg.type(), text: msg.text() });
});

// 2. Track Network Requests
const networkRequests = [];
page.on('request', req => {
    networkRequests.push({ url: req.url(), method: req.method() });
});

console.log(`Navigating to ${TARGET_URL}...`);
await page.goto(TARGET_URL, { waitUntil: 'domcontentloaded', timeout: 20000 });
await page.waitForTimeout(3000);

const title = await page.title();
const url = page.url();
console.log(`Current page title: "${title}", URL: "${url}"`);

// 3. Inspect DOM elements
const domInspection = await page.evaluate(() => {
    const headings = Array.from(document.querySelectorAll('h1, h2, h3')).map(h => h.innerText.trim()).filter(Boolean);
    const buttons = Array.from(document.querySelectorAll('button')).map(b => b.innerText.trim()).filter(Boolean);
    const cards = Array.from(document.querySelectorAll('[class*="card"], [class*="hero"], [class*="observatory"]')).length;
    return {
        headings: headings.slice(0, 8),
        sampleButtons: buttons.slice(0, 10),
        interactiveElementCount: buttons.length,
        observatoryCardsCount: cards
    };
});

console.log('\n--- DOM Inspection ---');
console.log(JSON.stringify(domInspection, null, 2));

// 4. Test Viewport Resizing / Emulation
console.log('\n--- Viewport Resizing Test ---');
console.log('Testing 1440x900...');
await page.setViewportSize({ width: 1440, height: 900 });
await page.waitForTimeout(500);
await page.screenshot({ path: 'C:/Users/Joshu/Tools/LSATU-Agent/drill_1440x900.png' });

console.log('Testing 1024x768...');
await page.setViewportSize({ width: 1024, height: 768 });
await page.waitForTimeout(500);
await page.screenshot({ path: 'C:/Users/Joshu/Tools/LSATU-Agent/drill_1024x768.png' });

// 5. Harmless Non-destructive Click Test (e.g. click a tab or non-mutating view control)
console.log('\n--- Harmless Interaction Test ---');
const clickResult = await page.evaluate(() => {
    // Find a filter or tab button that does not submit data
    const nonDestructiveBtn = Array.from(document.querySelectorAll('button')).find(b => {
        const txt = b.innerText.toLowerCase();
        return (txt.includes('all') || txt.includes('type') || txt.includes('overview') || txt.includes('filter')) && !txt.includes('delete') && !txt.includes('sign out');
    });
    if (nonDestructiveBtn) {
        nonDestructiveBtn.click();
        return { clicked: true, text: nonDestructiveBtn.innerText };
    }
    return { clicked: false, note: 'No specific filter button clicked to preserve safety' };
});
console.log('Interaction result:', JSON.stringify(clickResult));

// 6. Return to Starting State (1440x900)
console.log('\n--- Restoring Default State ---');
await page.setViewportSize({ width: 1440, height: 900 });
await page.waitForTimeout(500);

// Report summary
console.log('\n--- Summary Report ---');
console.log(`Console messages captured: ${consoleLogs.length}`);
console.log(`Network requests tracked: ${networkRequests.length}`);
console.log(`Initial URL: ${TARGET_URL}`);
console.log(`Final URL: ${page.url()}`);
console.log('Screenshots saved:');
console.log(' - C:/Users/Joshu/Tools/LSATU-Agent/drill_1440x900.png');
console.log(' - C:/Users/Joshu/Tools/LSATU-Agent/drill_1024x768.png');

await browser.close().catch(() => {});
console.log('Phase 7 Verification Complete!');
