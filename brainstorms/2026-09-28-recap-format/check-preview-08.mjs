import { chromium } from "file:///C:/Program%20Files/WindowsApps/OpenAI.CodexPrimaryRuntime.v26-923-495-0_26.923.495.0_x64__3k8sg7r9htsxt/dependencies/node/node_modules/playwright/index.mjs";
const browser = await chromium.launch({ executablePath: "C:/Program Files/Google/Chrome/Application/chrome.exe", headless: true });
const url = "http://127.0.0.1:8765/brainstorms/2026-09-28-recap-format/08-quantity-statements-visual-preview.html";
const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
await page.goto(url);
for (const [name, selector] of [["some", "#some"], ["inferences", "#inferences"], ["drill", "#drill"]]) {
  await page.locator(selector).scrollIntoViewIfNeeded();
  await page.screenshot({ path: `C:/Users/Joshu/AppData/Local/Temp/quantity-08-${name}.png` });
}
const imageStatus = await page.locator(".quantity-note img").evaluateAll((images) => images.map((image) => ({ loaded: image.complete && image.naturalWidth > 0, alt: image.alt })));
const revealCount = await page.locator(".quantity-note details").count();
await page.locator(".quantity-check details").first().locator("summary").click();
const firstRevealWorks = await page.locator(".quantity-check details").first().evaluate((details) => details.open);
const mobile = await browser.newPage({ viewport: { width: 430, height: 900 } });
await mobile.goto(url);
await mobile.screenshot({ path: "C:/Users/Joshu/AppData/Local/Temp/quantity-08-mobile.png" });
const overflow = await mobile.evaluate(() => document.documentElement.scrollWidth - innerWidth);
console.log(JSON.stringify({ imageStatus, revealCount, firstRevealWorks, mobileOverflowPixels: overflow }, null, 2));
await browser.close();
