import { createRequire } from 'module';
const require = createRequire('c:/Users/Joshu/dev/ai-os/projects/lsatu/package.json');
const { chromium } = require('playwright-core');
import fs from 'fs';

const PORT = 9223;

async function extractConversations() {
    console.log('Connecting to browser on port 9223...');
    const browser = await chromium.connectOverCDP(`http://127.0.0.1:${PORT}`);
    const context = browser.contexts()[0] || await browser.newContext();
    const pages = context.pages();
    
    let page = pages.find(p => p.url().includes('reddit.com'));
    if (!page) {
        console.log('Opening Reddit chat page...');
        page = await context.newPage();
        await page.goto('https://chat.reddit.com', { waitUntil: 'domcontentloaded', timeout: 30000 });
    } else {
        await page.bringToFront();
        if (!page.url().includes('chat.reddit.com')) {
            await page.goto('https://chat.reddit.com', { waitUntil: 'domcontentloaded', timeout: 30000 });
        }
    }

    console.log('Waiting for chat interface to settle...');
    await page.waitForTimeout(5000);

    const chatRows = page.locator('[role="row"]');
    const rowCount = await chatRows.count();
    console.log(`Found ${rowCount} chat rows.`);

    const conversations = [];
    const limit = Math.min(rowCount, 10);

    for (let i = 0; i < limit; i++) {
        try {
            const row = chatRows.nth(i);
            const rowText = await row.innerText().catch(() => '');
            const lines = rowText.split('\n').map(l => l.trim()).filter(Boolean);
            const username = lines[0] || `User_${i}`;

            console.log(`\nClicking row ${i + 1}/${limit}: ${username}...`);
            await row.click();
            await page.waitForTimeout(2000);

            // Extract messages in the active thread
            const threadData = await page.evaluate(() => {
                // Find all message containers
                const messages = [];
                // Look for text in the right-side chat pane
                const main = document.querySelector('main') || document.querySelector('[role="main"]') || document.body;
                
                // Get all message items
                const elements = main.querySelectorAll('[role="presentation"], [data-testid*="message"], shreddit-chat-message, div[tabindex]');
                
                // Also pull all paragraphs and text blocks with authors
                const textDump = main.innerText;
                
                return {
                    textDump: textDump
                };
            });

            conversations.push({
                index: i + 1,
                user: username,
                preview: lines.join(' | '),
                history: threadData.textDump
            });

        } catch (e) {
            console.error(`Error on thread ${i}:`, e.message);
        }
    }

    fs.writeFileSync('C:/Users/Joshu/Tools/Reddit-Agent/reddit_10_conversations.json', JSON.stringify(conversations, null, 2), 'utf-8');
    console.log('\nExtracted conversations saved to C:/Users/Joshu/Tools/Reddit-Agent/reddit_10_conversations.json');

    await browser.close().catch(() => {});
    return conversations;
}

extractConversations().catch(console.error);
