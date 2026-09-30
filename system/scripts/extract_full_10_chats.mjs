import { projectPath } from './project-paths.mjs';
import { createRequire } from 'module';
const require = createRequire(projectPath('lsatu', 'package.json'));
const { chromium } = require('playwright-core');
import fs from 'fs';

const USERS = [
    'ConstantPlenty7292',
    'jeemby',
    'Strict_Potential3221',
    'Alone-Rip4037',
    'PrinLeiAsh17',
    'Adventurous-Boss-882',
    'laylahkk',
    'ethiopianqueen13',
    'Buck_Denver',
    'carliezz'
];

async function extractFullChats() {
    const browser = await chromium.connectOverCDP('http://127.0.0.1:9223');
    const context = browser.contexts()[0] || await browser.newContext();
    const page = context.pages().find(p => p.url().includes('reddit.com'));

    if (!page) {
        console.error('Reddit tab not found!');
        await browser.close();
        return;
    }

    const conversations = {};

    for (const username of USERS) {
        try {
            console.log(`Clicking thread for ${username}...`);
            const item = page.getByText(username).first();
            await item.click({ timeout: 4000 });
            await page.waitForTimeout(2500);

            const rawText = await page.evaluate(() => {
                function getDeepText(node) {
                    let res = '';
                    if (!node) return res;
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
            
            conversations[username] = rawText;
            console.log(`Captured ${rawText.length} chars for ${username}`);
        } catch (e) {
            console.log(`Failed on ${username}: ${e.message}`);
        }
    }

    fs.writeFileSync('C:/Users/Joshu/Tools/Reddit-Agent/raw_10_conversations.json', JSON.stringify(conversations, null, 2), 'utf-8');
    console.log('Saved all to C:/Users/Joshu/Tools/Reddit-Agent/raw_10_conversations.json');
    await browser.close();
}

extractFullChats().catch(console.error);
