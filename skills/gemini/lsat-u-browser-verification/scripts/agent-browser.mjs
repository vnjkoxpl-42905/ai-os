// C:\Users\Joshu\Tools\LSATU-Agent\agent-browser.mjs
// Playwright CDP connector for LSAT U Agent Browser on port 9223

import { createRequire } from 'module';

const require = createRequire(new URL('../../../../../ai-os-projects/lsatu/package.json', import.meta.url));
const { chromium } = require('playwright-core');

const PORT = 9223;
const CDP_URL = `http://127.0.0.1:${PORT}`;

export async function connectAgentBrowser() {
    const browser = await chromium.connectOverCDP(CDP_URL);
    const contexts = browser.contexts();
    const context = contexts[0] || await browser.newContext();
    const pages = context.pages();
    
    // Find the LSAT U page or pick first page
    let page = pages.find(p => p.url().includes('lsatprep.study') || p.url().includes('localhost'));
    if (!page && pages.length > 0) {
        page = pages[0];
    } else if (!page) {
        page = await context.newPage();
    }
    
    return { browser, context, page };
}

export async function captureScreenshot(outputFile, width = 1440, height = 900) {
    const { browser, page } = await connectAgentBrowser();
    await page.setViewportSize({ width, height });
    await page.screenshot({ path: outputFile, fullPage: false });
    const currentUrl = page.url();
    const title = await page.title();
    // Do NOT close browser, just disconnect CDP
    await browser.close().catch(() => {});
    return { currentUrl, title, width, height, outputFile };
}

export async function inspectState() {
    const { browser, page } = await connectAgentBrowser();
    const url = page.url();
    const title = await page.title();
    
    const authState = await page.evaluate(() => {
        const keys = Object.keys(localStorage);
        const hasAuth = keys.some(k => k.includes('sb-') || k.includes('auth-token') || k.includes('supabase'));
        return {
            hasLocalStorageAuth: hasAuth,
            cookieCount: document.cookie.split(';').filter(Boolean).length,
            title: document.title,
            bodyLength: document.body ? document.body.innerHTML.length : 0
        };
    });
    
    await browser.close().catch(() => {});
    return { url, title, authState };
}

// CLI entry point
if (process.argv[1] && process.argv[1].replace(/\\/g, '/').endsWith('agent-browser.mjs')) {
    const action = process.argv[2] || 'status';
    if (action === 'status') {
        const state = await inspectState();
        console.log(JSON.stringify(state, null, 2));
    } else if (action === 'screenshot') {
        const out = process.argv[3] || 'C:/Users/Joshu/Tools/LSATU-Agent/current.png';
        const w = parseInt(process.argv[4] || '1440', 10);
        const h = parseInt(process.argv[5] || '900', 10);
        const res = await captureScreenshot(out, w, h);
        console.log(`Screenshot saved: ${res.outputFile} (${res.width}x${res.height}) at ${res.currentUrl}`);
    }
}
