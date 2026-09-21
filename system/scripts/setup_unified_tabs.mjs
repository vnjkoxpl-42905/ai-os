import { createRequire } from 'module';
const require = createRequire('c:/Users/Joshu/dev/ai-os/projects/lsatu/package.json');
const { chromium } = require('playwright-core');

const TARGETS = [
    { name: "LSAT U", url: "https://lsatprep.study/auth", match: "lsatprep.study" },
    { name: "Reddit", url: "https://chat.reddit.com", match: "reddit.com" },
    { name: "7Sage", url: "https://7sage.com/accounts/login", match: "7sage.com" },
    { name: "Facebook", url: "https://www.facebook.com/messages", match: "facebook.com" }
];

async function setupUnifiedTabs() {
    console.log("Connecting to agent browser on port 9223...");
    const browser = await chromium.connectOverCDP('http://127.0.0.1:9223');
    const context = browser.contexts()[0] || await browser.newContext();
    const existingPages = context.pages();

    console.log(`Existing pages count: ${existingPages.length}`);

    for (const target of TARGETS) {
        let page = existingPages.find(p => p.url().includes(target.match));
        if (page) {
            console.log(`Found existing tab for ${target.name}: ${page.url()}`);
            if (target.name === "7Sage" && !page.url().includes("login") && !page.url().includes("app")) {
                await page.goto(target.url, { waitUntil: 'domcontentloaded' }).catch(() => {});
            }
        } else {
            console.log(`Opening new tab for ${target.name} (${target.url})...`);
            page = await context.newPage();
            await page.goto(target.url, { waitUntil: 'domcontentloaded' }).catch(err => {
                console.log(`Note on ${target.name}: ${err.message}`);
            });
        }
    }

    // Close any stray localhost tabs if present
    for (const page of context.pages()) {
        if (page.url().includes("localhost:8080")) {
            console.log("Closing unused localhost tab...");
            await page.close().catch(() => {});
        }
    }

    console.log("\nCurrent open tabs in Agent Browser:");
    const pages = context.pages();
    for (let i = 0; i < pages.length; i++) {
        const p = pages[i];
        console.log(`  Tab ${i + 1}: ${await p.title()} (${p.url()})`);
    }

    await browser.close().catch(() => {});
}

setupUnifiedTabs().catch(console.error);
