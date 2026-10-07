// C:\Users\Joshu\Tools\LSATU-Agent\test_persistence_cycle.mjs
import { execSync } from 'child_process';
import { createRequire } from 'module';

const require = createRequire(new URL('../../../../../ai-os-projects/lsatu/package.json', import.meta.url));
const { chromium } = require('playwright-core');

console.log('=== Step 1: Closing dedicated Chrome browser completely ===');
const stopCmd = `pwsh -Command "Get-CimInstance Win32_Process | Where-Object { \\$_.CommandLine -like '*LSATU-Agent-Chrome*' } | ForEach-Object { Stop-Process -Id \\$_.ProcessId -Force -ErrorAction SilentlyContinue }"`;
try {
    execSync(stopCmd, { stdio: 'inherit' });
} catch (e) {
    console.log('Stop process command executed.');
}
console.log('Process stopped.');

// Wait 3 seconds
execSync('pwsh -Command "Start-Sleep -Seconds 3"');

console.log('=== Step 2: Relaunching dedicated Chrome via launch_browser.py ===');
execSync('python C:\\Users\\Joshu\\Tools\\LSATU-Agent\\launch_browser.py https://lsatprep.study', { stdio: 'inherit' });

console.log('=== Step 3: Connecting to relaunched Chrome on 127.0.0.1:9223 ===');
const browser = await chromium.connectOverCDP('http://127.0.0.1:9223');
const context = browser.contexts()[0] || await browser.newContext();
let page = context.pages().find(p => p.url().includes('lsatprep.study')) || context.pages()[0];

console.log(`Current URL after relaunch: ${page.url()}`);
// Give page 3 seconds to complete any client-side auth check
await page.waitForTimeout(3000);

const finalUrl = page.url();
const title = await page.title();
console.log(`Landed on: ${finalUrl} ("${title}")`);

const authCheck = await page.evaluate(() => {
    const keys = Object.keys(localStorage);
    const authKey = keys.find(k => k.includes('sb-') || k.includes('auth-token'));
    const isClassroom = window.location.pathname.startsWith('/classroom');
    const greeting = document.body.innerText.includes('Good evening') || 
                     document.body.innerText.includes('Joshua') ||
                     document.body.innerText.includes('Classroom');
    return {
        isClassroom,
        hasAuthKey: !!authKey,
        authKeyName: authKey,
        greetingDetected: greeting,
        path: window.location.pathname
    };
});

console.log('Persistence Check Result:');
console.log(JSON.stringify(authCheck, null, 2));

await page.screenshot({ path: 'C:/Users/Joshu/Tools/LSATU-Agent/persistence_verified.png' });
console.log('Screenshot saved to C:/Users/Joshu/Tools/LSATU-Agent/persistence_verified.png');

await browser.close().catch(() => {});

if (authCheck.isClassroom || authCheck.hasAuthKey) {
    console.log('\n>>> PERSISTENCE TEST: PASSED! User remained logged in across full browser restart. <<<');
} else {
    console.error('\n>>> PERSISTENCE TEST: FAILED! User was logged out after restart. <<<');
    process.exit(1);
}
