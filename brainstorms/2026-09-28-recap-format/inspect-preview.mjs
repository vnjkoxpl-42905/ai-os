import { chromium } from "file:///C:/Program%20Files/WindowsApps/OpenAI.CodexPrimaryRuntime.v26-923-495-0_26.923.495.0_x64__3k8sg7r9htsxt/dependencies/node/node_modules/playwright/index.mjs";
import { pathToFileURL } from "node:url";
import path from "node:path";
const browser = await chromium.launch({ executablePath: "C:/Program Files/Google/Chrome/Application/chrome.exe", headless: true });
const page = await browser.newPage({ viewport: { width: 430, height: 900 } });
await page.goto(pathToFileURL(path.resolve("brainstorms/2026-09-28-recap-format/07-quantity-statements-preview.html")).href);
await page.screenshot({ path: "C:/Users/Joshu/AppData/Local/Temp/lsatu-quantity-preview-mobile-playwright.png" });
console.log(await page.evaluate(() => Object.fromEntries(["html", "body", ".classroom-root", ".classroom-stage", ".classroom-column", ".quantity-note", ".quantity-note p"].map((selector) => { const node = document.querySelector(selector); const rect = node.getBoundingClientRect(); return [selector, {left:rect.left,width:rect.width,scrollWidth:node.scrollWidth,style:getComputedStyle(node).minWidth}]}))));
await browser.close();
