// C:\Users\Joshu\Tools\LSATU-Agent\check_auth.mjs
import { createRequire } from 'module';
const require = createRequire('c:/Users/Joshu/dev/ai-os/projects/lsatu/package.json');
const { chromium } = require('playwright-core');

const browser = await chromium.connectOverCDP('http://127.0.0.1:9223');
const context = browser.contexts()[0] || await browser.newContext();
let page = context.pages().find(p => p.url().includes('lsatprep.study')) || context.pages()[0];

console.log(`Current page URL: ${page.url()}`);
console.log('Navigating to https://lsatprep.study...');
await page.goto('https://lsatprep.study', { waitUntil: 'domcontentloaded', timeout: 15000 });
await page.waitForTimeout(3000);

const finalUrl = page.url();
const title = await page.title();
console.log(`Landed on: ${finalUrl} ("${title}")`);

// Inspect localStorage and cookies for Supabase auth session
const authData = await page.evaluate(() => {
    const keys = Object.keys(localStorage);
    const authKeys = keys.filter(k => k.includes('sb-') || k.includes('auth-token') || k.includes('supabase'));
    const isAuth = authKeys.length > 0;
    
    // Check for user elements in DOM (e.g. avatar, navigation, drill links)
    const hasLogoutOrUser = document.body.innerText.includes('Sign Out') || 
                            document.body.innerText.includes('Log Out') ||
                            document.body.innerText.includes('Classroom') ||
                            document.body.innerText.includes('Observatory') ||
                            document.querySelector('[data-testid="user-menu"]') !== null;

    return {
        isAuth,
        authKeys,
        hasLogoutOrUser,
        url: window.location.href,
        storageKeyCount: keys.length
    };
});

console.log('Auth Evaluation Result:');
console.log(JSON.stringify(authData, null, 2));

await page.screenshot({ path: 'C:/Users/Joshu/Tools/LSATU-Agent/authenticated_state.png', fullPage: false });
console.log('Screenshot saved to: C:/Users/Joshu/Tools/LSATU-Agent/authenticated_state.png');

await browser.close().catch(() => {});
