import { createRequire } from 'module';
const require = createRequire('c:/Users/Joshu/dev/ai-os/projects/lsatu/package.json');
const { chromium } = require('playwright-core');

const PORT = 9223;

async function scanRedditThreads() {
    console.log('Connecting to browser on port 9223...');
    const browser = await chromium.connectOverCDP(`http://127.0.0.1:${PORT}`);
    const context = browser.contexts()[0] || await browser.newContext();
    const pages = context.pages();
    
    let page = pages.find(p => p.url().includes('reddit.com'));
    if (!page) {
        console.error('Reddit page not found among open tabs.');
        await browser.close().catch(() => {});
        return;
    }

    console.log(`Found Reddit tab: ${page.url()}`);
    await page.bringToFront();
    await page.waitForTimeout(1000);

    // Get list of threads in sidebar
    const threadLocators = page.locator('a[href*="/chat/room/"], a[href*="/chat/channel/"], [role="row"]');
    const count = await threadLocators.count();
    console.log(`Found ${count} thread items in sidebar.`);

    const threadAnalysis = [];

    // Scan up to 12 threads to get at least 10 different people
    const scanLimit = Math.min(count, 12);

    for (let i = 0; i < scanLimit; i++) {
        try {
            const threadItem = threadLocators.nth(i);
            const rawSidebarText = await threadItem.innerText().catch(() => '');
            const threadLines = rawSidebarText.split('\n').map(s => s.trim()).filter(Boolean);
            const otherUser = threadLines[0] || `User_${i}`;

            console.log(`\n[${i + 1}/${scanLimit}] Clicking thread: ${otherUser}...`);
            await threadItem.click({ timeout: 5000 }).catch(async () => {
                await threadItem.dispatchEvent('click').catch(() => {});
            });
            await page.waitForTimeout(2000);

            // Extract chat messages in the active main pane
            const messages = await page.evaluate(() => {
                const msgs = [];
                // Look for message bubbles or text containers
                const msgElements = document.querySelectorAll('[role="presentation"] [tabindex], [data-testid*="message"], shreddit-chat-message, [class*="message"], [role="listitem"]');
                
                // Also get all paragraphs or visible text blocks in the chat history
                const mainArea = document.querySelector('main') || document.querySelector('[role="main"]') || document.body;
                const textNodes = Array.from(mainArea.querySelectorAll('p, [data-testid*="message-content"], span')).map(el => el.innerText.trim()).filter(t => t.length > 5);

                return {
                    fullText: mainArea ? mainArea.innerText : '',
                    snippets: textNodes.slice(-15)
                };
            });

            threadAnalysis.push({
                index: i + 1,
                user: otherUser,
                sidebarSummary: threadLines.join(' | '),
                chatData: messages
            });

        } catch (err) {
            console.error(`Error processing thread ${i}:`, err.message);
        }
    }

    // Capture screenshot of the current view
    await page.screenshot({ path: 'C:/Users/Joshu/Tools/Reddit-Agent/thread_scan_view.png' });

    await browser.close().catch(() => {});
    return threadAnalysis;
}

scanRedditThreads().then(data => {
    import('fs').then(fs => {
        fs.writeFileSync('C:/Users/Joshu/Tools/Reddit-Agent/thread_scan_data.json', JSON.stringify(data, null, 2), 'utf-8');
        console.log('\nScan complete! Saved raw data to C:/Users/Joshu/Tools/Reddit-Agent/thread_scan_data.json');
    });
}).catch(console.error);
