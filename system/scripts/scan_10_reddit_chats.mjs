import { createRequire } from 'module';
const require = createRequire('c:/Users/Joshu/dev/ai-os/projects/lsatu/package.json');
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
    'deleted'
];

async function scanChats() {
    const browser = await chromium.connectOverCDP('http://127.0.0.1:9223');
    const context = browser.contexts()[0] || await browser.newContext();
    const page = context.pages().find(p => p.url().includes('reddit.com'));
    
    if (!page) {
        console.error('Reddit page not found');
        await browser.close();
        return;
    }

    const conversations = [];

    for (const user of USERS) {
        try {
            console.log(`Looking for user: ${user}...`);
            const loc = page.getByText(user).first();
            const count = await loc.count();
            if (count === 0) {
                console.log(`Could not find ${user} in sidebar.`);
                continue;
            }

            await loc.click({ timeout: 4000 });
            await page.waitForTimeout(2500);

            // Extract all text in the main pane
            const chatText = await page.evaluate(() => {
                // Find all message items or text in right panel
                // On Reddit chat, messages often live in role="presentation" or main area
                const mainArea = document.querySelector('main') || document.body;
                return mainArea.innerText;
            });

            conversations.push({
                user,
                chatText
            });

            console.log(`Extracted chat for ${user} (${chatText.length} chars)`);
        } catch (e) {
            console.log(`Error reading chat for ${user}: ${e.message}`);
        }
    }

    fs.writeFileSync('C:/Users/Joshu/Tools/Reddit-Agent/analyzed_reddit_chats.json', JSON.stringify(conversations, null, 2), 'utf-8');
    console.log('Saved to C:/Users/Joshu/Tools/Reddit-Agent/analyzed_reddit_chats.json');

    await browser.close();
}

scanChats().catch(console.error);
