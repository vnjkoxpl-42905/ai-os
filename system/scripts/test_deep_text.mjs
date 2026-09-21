import { createRequire } from 'module';
const require = createRequire('c:/Users/Joshu/dev/ai-os/projects/lsatu/package.json');
const { chromium } = require('playwright-core');

async function testDeepText() {
    const browser = await chromium.connectOverCDP('http://127.0.0.1:9223');
    const page = (browser.contexts()[0] || await browser.newContext()).pages().find(p => p.url().includes('reddit.com'));
    
    const text = await page.evaluate(() => {
        function getDeepText(node) {
            let res = '';
            if (node.nodeType === 3) { // TEXT_NODE
                const val = node.nodeValue.trim();
                if (val) res += val + '\n';
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

    console.log('--- EXTRACTED DEEP TEXT (First 1500 chars) ---');
    console.log(text.slice(0, 1500));
    console.log('\n--- TOTAL CHARS: ' + text.length + ' ---');

    await browser.close();
}

testDeepText().catch(console.error);
