import { createRequire } from 'module';
const require = createRequire('c:/Users/Joshu/dev/ai-os/projects/lsatu/package.json');
const { chromium } = require('playwright-core');
import fs from 'fs';
import path from 'path';

const PORT = 9223;
const CDP_URL = `http://127.0.0.1:${PORT}`;
const OUTPUT_DIR = 'C:/Users/Joshu/Tools/LSATU-Agent/verification_evidence';

async function verifyAllTabs() {
    if (!fs.existsSync(OUTPUT_DIR)) {
        fs.mkdirSync(OUTPUT_DIR, { recursive: true });
    }

    console.log(`Connecting to CDP on ${CDP_URL}...`);
    const browser = await chromium.connectOverCDP(CDP_URL);
    const context = browser.contexts()[0] || await browser.newContext();
    const pages = context.pages();

    console.log(`Found ${pages.length} total open tab(s).`);

    const results = [];

    for (let i = 0; i < pages.length; i++) {
        const page = pages[i];
        const url = page.url();
        const title = await page.title();

        let domain = 'other';
        if (url.includes('lsatprep.study') || url.includes('localhost')) domain = 'lsat_u';
        else if (url.includes('facebook.com') || url.includes('messenger.com')) domain = 'facebook';
        else if (url.includes('reddit.com')) domain = 'reddit';
        else if (url.includes('7sage.com')) domain = '7sage';

        // Evaluate cookies for this page's origin
        const pageCookies = await context.cookies([url]);
        const cookieNames = pageCookies.map(c => c.name);

        // Evaluate DOM indicators
        const domInfo = await page.evaluate(() => {
            const text = document.body ? document.body.innerText : '';
            return {
                textLength: text.length,
                hasPasswordInput: !!document.querySelector('input[type="password"]'),
                hasLoginText: text.includes('Log In') || text.includes('Sign In'),
                userMenuCandidate: !!document.querySelector('[aria-label*="account" i], [aria-label*="profile" i], [data-testid*="user" i], .avatar, .user-avatar, #user-dropdown')
            };
        });

        const screenshotPath = path.join(OUTPUT_DIR, `tab_${i + 1}_${domain}.png`).replace(/\\/g, '/');
        await page.screenshot({ path: screenshotPath, fullPage: false }).catch(() => {});

        results.push({
            tabIndex: i + 1,
            domain,
            url,
            title,
            cookieCount: pageCookies.length,
            keyCookies: cookieNames.slice(0, 10),
            domInfo,
            screenshotPath
        });
    }

    await browser.close().catch(() => {});
    return results;
}

verifyAllTabs().then(res => {
    console.log(JSON.stringify(res, null, 2));
}).catch(err => {
    console.error('Error during verification:', err);
});
