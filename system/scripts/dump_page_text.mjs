import { projectPath } from './project-paths.mjs';
import { createRequire } from 'module';
const require = createRequire(projectPath('lsatu', 'package.json'));
const { chromium } = require('playwright-core');
import fs from 'fs';

async function dumpPageText() {
    const browser = await chromium.connectOverCDP('http://127.0.0.1:9223');
    const page = (browser.contexts()[0] || await browser.newContext()).pages().find(p => p.url().includes('reddit.com'));
    
    const text = await page.evaluate(() => {
        function getDeepText(node) {
            let res = '';
            if (node.nodeType === 3) {
                const val = node.nodeValue.trim();
                if (val && !val.startsWith('.snoo-') && !val.startsWith('SML.load')) res += val + '\n';
            }
            if (node.shadowRoot) {
                for (const child of node.shadowRoot.childNodes) {
                    res += getDeepText(child);
                }
            }
            if (node.childNodes) {
                for (const child of node.childNodes) {
                    res += getDeepText(child);
                }
            }
            return res;
        }
        return getDeepText(document.body);
    });

    fs.writeFileSync('C:/Users/Joshu/Tools/Reddit-Agent/current_page_text.txt', text, 'utf-8');
    console.log('Saved ' + text.length + ' chars to current_page_text.txt');
    await browser.close();
}

dumpPageText().catch(console.error);
