import { chromium } from "file:///C:/Program%20Files/WindowsApps/OpenAI.CodexPrimaryRuntime.v26-923-495-0_26.923.495.0_x64__3k8sg7r9htsxt/dependencies/node/node_modules/playwright/index.mjs";
const browser = await chromium.launch({ executablePath: "C:/Program Files/Google/Chrome/Application/chrome.exe", headless: true });
const url = "http://127.0.0.1:8765/brainstorms/2026-09-28-recap-format/08-quantity-statements-visual-preview.html";
const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
await page.goto(url);
await page.screenshot({ path: "C:/Users/Joshu/AppData/Local/Temp/quantity-08-top.png" });
for (const [name, selector] of [["some", "#some"], ["inferences", "#inferences"], ["drill", "#drill"]]) {
  await page.locator(selector).scrollIntoViewIfNeeded();
  await page.screenshot({ path: `C:/Users/Joshu/AppData/Local/Temp/quantity-08-${name}.png` });
}
const imageStatus = await page.locator(".quantity-note img").evaluateAll((images) => images.map((image) => ({ loaded: image.complete && image.naturalWidth > 0, alt: image.alt })));
const revealCount = await page.locator(".quantity-note details").count();
await page.locator(".quantity-check details").first().locator("summary").click();
const firstRevealWorks = await page.locator(".quantity-check details").first().evaluate((details) => details.open);
const sliderStates = [];
for (const value of [0, 1, 4, 5, 8]) {
  await page.locator("#quantity-slider").fill(String(value));
  sliderStates.push(await page.evaluate(() => ({
    count: Number(document.querySelector("#quantity-count").textContent),
    books: document.querySelectorAll(".quantity-lab-book.is-hardcover").length,
    trueRules: [...document.querySelectorAll(".quantity-lab-verdicts .is-true")].map((element) => element.dataset.rule),
  })));
}
const overlapCounts = [Number(await page.locator("#quantity-overlap-count").textContent())];
for (let index = 0; index < 4; index++) {
  await page.locator("#quantity-overlap-shuffle").click();
  overlapCounts.push(Number(await page.locator("#quantity-overlap-count").textContent()));
}
await page.locator(".quantity-overlap-lab").scrollIntoViewIfNeeded();
await page.screenshot({ path: "C:/Users/Joshu/AppData/Local/Temp/quantity-08-overlap.png" });
await page.locator("#quantity-quiz").scrollIntoViewIfNeeded();
await page.screenshot({ path: "C:/Users/Joshu/AppData/Local/Temp/quantity-08-quiz.png" });
const quizAnswers = ["Yes, every B is C.", "No, these parts of A can miss.", "No, the B could be outside A.", "No, the A can be in the minority.", "No, they could be different B.", "Yes, two majorities of A overlap.", "No, A might be empty."];
await page.locator("#quantity-quiz-input").fill("Maybe they overlap.");
await page.locator("#quantity-quiz-form button").click();
const invalidAnswerPrompt = await page.locator("#quantity-quiz-error").textContent();
const quizChecks = [];
for (let index = 0; index < quizAnswers.length; index++) {
  await page.locator("#quantity-quiz-input").fill(quizAnswers[index]);
  await page.locator("#quantity-quiz-form button").click();
  quizChecks.push(await page.locator("#quantity-quiz-feedback-label").textContent());
  if (index === 0) { await page.waitForTimeout(500); await page.screenshot({ path: "C:/Users/Joshu/AppData/Local/Temp/quantity-08-quiz-feedback.png" }); }
  await page.locator("#quantity-quiz-next").click();
}
const quizScore = await page.locator("#quantity-quiz-score").textContent();
await page.locator("#quantity-quiz-restart").click();
await page.locator("#quantity-quiz-input").fill("No, because I disagree.");
await page.locator("#quantity-quiz-form button").click();
const mismatchFeedback = await page.locator("#quantity-quiz-feedback-label").textContent();
const mobile = await browser.newPage({ viewport: { width: 430, height: 900 } });
await mobile.goto(url);
await mobile.screenshot({ path: "C:/Users/Joshu/AppData/Local/Temp/quantity-08-mobile.png" });
await mobile.locator(".quantity-overlap-lab").scrollIntoViewIfNeeded();
await mobile.screenshot({ path: "C:/Users/Joshu/AppData/Local/Temp/quantity-08-overlap-mobile.png" });
await mobile.locator("#quantity-quiz").scrollIntoViewIfNeeded();
await mobile.screenshot({ path: "C:/Users/Joshu/AppData/Local/Temp/quantity-08-quiz-mobile.png" });
const overflow = await mobile.evaluate(() => document.documentElement.scrollWidth - innerWidth);
console.log(JSON.stringify({ imageStatus, revealCount, firstRevealWorks, sliderStates, overlapCounts, invalidAnswerPrompt, quizChecks, quizScore, mismatchFeedback, mobileOverflowPixels: overflow }, null, 2));
await browser.close();
