// C:\Users\Joshu\Tools\LSATU-Agent\verify-viewports.mjs
// Standard Viewport Presets verification runner for LSAT U

import { createRequire } from 'module';
import path from 'path';
import fs from 'fs';

const require = createRequire(new URL('../../../../../ai-os-projects/lsatu/package.json', import.meta.url));
const { chromium } = require('playwright-core');

const PORT = 9223;
const CDP_URL = `http://127.0.0.1:${PORT}`;

export const STANDARD_VIEWPORTS = [
    { name: 'desktop-1440', width: 1440, height: 900, label: 'Standard Desktop (1440x900)' },
    { name: 'laptop-1366',  width: 1366, height: 768, label: 'Laptop Standard (1366x768)' },
    { name: 'laptop-1280',  width: 1280, height: 800, label: 'Compact Laptop (1280x800)' },
    { name: 'tablet-1024',  width: 1024, height: 768, label: 'Tablet Landscape (1024x768)' },
    { name: 'mobile-390',   width: 390,  height: 844, label: 'Mobile iPhone (390x844)' }
];

export async function runViewportSweep(targetUrl, outputDir = 'C:/Users/Joshu/Tools/LSATU-Agent/snapshots') {
    fs.mkdirSync(outputDir, { recursive: true });
    
    const browser = await chromium.connectOverCDP(CDP_URL);
    const context = browser.contexts()[0] || await browser.newContext();
    const page = context.pages().find(p => p.url().includes('lsatprep.study') || p.url().includes('localhost')) || await context.newPage();

    if (targetUrl && page.url() !== targetUrl) {
        console.log(`Navigating to ${targetUrl}...`);
        await page.goto(targetUrl, { waitUntil: 'domcontentloaded', timeout: 15000 });
        // Give client-side React hydration 2 seconds to stabilize
        await page.waitForTimeout(2000);
    }

    const currentUrl = page.url();
    const pageTitle = await page.title();
    console.log(`Testing viewports on: ${currentUrl} ("${pageTitle}")`);

    const results = [];
    for (const vp of STANDARD_VIEWPORTS) {
        await page.setViewportSize({ width: vp.width, height: vp.height });
        // Allow CSS transitions and layout recalculations to settle
        await page.waitForTimeout(500);

        const screenshotPath = path.join(outputDir, `${vp.name}.png`);
        await page.screenshot({ path: screenshotPath, fullPage: false });

        // Check if there is vertical scrolling needed (scrollable height > viewport height)
        const scrollMetrics = await page.evaluate(() => {
            const doc = document.documentElement;
            return {
                scrollHeight: doc.scrollHeight,
                clientHeight: doc.clientHeight,
                requiresScroll: doc.scrollHeight > doc.clientHeight + 5
            };
        });

        results.push({
            name: vp.name,
            label: vp.label,
            width: vp.width,
            height: vp.height,
            screenshotPath,
            ...scrollMetrics
        });

        console.log(`[${vp.name}] ${vp.width}x${vp.height} -> Saved: ${screenshotPath} (Requires scroll: ${scrollMetrics.requiresScroll})`);
    }

    await browser.close().catch(() => {});
    return { currentUrl, pageTitle, results };
}

// CLI execution
if (process.argv[1] && process.argv[1].replace(/\\/g, '/').endsWith('verify-viewports.mjs')) {
    const target = process.argv[2] || null;
    const outDir = process.argv[3] || 'C:/Users/Joshu/Tools/LSATU-Agent/snapshots';
    const report = await runViewportSweep(target, outDir);
    console.log('\n--- VIEWPORT SWEEP REPORT ---');
    console.log(JSON.stringify(report, null, 2));
}
