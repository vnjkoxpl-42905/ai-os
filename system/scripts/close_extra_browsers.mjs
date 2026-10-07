import { projectPath } from './project-paths.mjs';
import { createRequire } from 'module';
const require = createRequire(projectPath('lsatu', 'package.json'));
const { chromium } = require('playwright-core');

async function closeExtraBrowsers() {
    for (const port of [9224, 9225, 9226]) {
        try {
            const browser = await chromium.connectOverCDP(`http://127.0.0.1:${port}`);
            console.log(`Sending Browser.close to port ${port}...`);
            const session = await browser.newBrowserCDPSession();
            await session.send('Browser.close');
            console.log(`Successfully closed browser on port ${port}`);
        } catch (e) {
            console.log(`Port ${port} error or already closed: ${e.message}`);
        }
    }
}

closeExtraBrowsers();
