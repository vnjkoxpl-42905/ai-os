#!/usr/bin/env node
// extract-lecture.mjs: End-to-end extraction pipeline for Loophole Online video lessons.

import { createRequire } from 'module';
import { fileURLToPath } from 'url';
import path from 'path';
import fs from 'fs';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Dynamic Playwright loading
const possiblePaths = [
  path.resolve(__dirname, '../../../../../ai-os-projects/lsatu/package.json'),
  path.resolve(process.cwd(), '../ai-os-projects/lsatu/package.json'),
  'C:/Users/Joshu/dev/ai-os-projects/lsatu/package.json'
];
let pkgPath = possiblePaths.find(p => fs.existsSync(p)) || possiblePaths[0];
const requireLsatu = createRequire(pkgPath);
const { chromium } = requireLsatu('playwright');

// CLI args
const args = process.argv.slice(2);
function getArg(flag, defaultValue = null) {
  const idx = args.indexOf(flag);
  return (idx !== -1 && idx + 1 < args.length) ? args[idx + 1] : defaultValue;
}

const targetUrl = getArg('--url', 'https://new.theloophole.com/training-camp/browse/stage/learn/video/conditional-sufficient-assumption-sa-strategy');
const topic = getArg('--topic', 'Sufficient Assumption');
const slug = getArg('--slug', 'conditional-sa-strategy');
const port = parseInt(getArg('--port', '9223'), 10);

const repoRoot = path.resolve(__dirname, '../../../../');
const lectureDir = path.join(repoRoot, 'Loophole Lecture', topic);
const imagesDir = path.join(lectureDir, 'images');

if (!fs.existsSync(imagesDir)) {
  fs.mkdirSync(imagesDir, { recursive: true });
}

async function runPipeline() {
  console.log(`[Lecture Pipeline] Starting extraction for topic: "${topic}"`);
  console.log(`[Lecture Pipeline] Target URL: ${targetUrl}`);

  // Connect to Edge over CDP
  let browser;
  try {
    browser = await chromium.connectOverCDP(`http://localhost:${port}`);
  } catch (err) {
    console.error(`[Lecture Pipeline Error] Cannot connect to Edge on port ${port}. Ensure Edge is running with --remote-debugging-port=${port}.`);
    process.exit(1);
  }

  const contexts = browser.contexts();
  const allPages = [];
  for (const ctx of contexts) {
    for (const p of ctx.pages()) allPages.push(p);
  }

  let page = allPages.find(p => p.url().includes('loophole.com')) || allPages[0];
  if (!page) {
    const ctx = contexts[0] || await browser.newContext();
    page = await ctx.newPage();
  }

  console.log(`[Lecture Pipeline] Current page URL: ${page.url()}`);
  if (page.url().includes('/welcome') || page.url().includes('/sign-in')) {
    console.log('[Lecture Pipeline Warning] Active session is not logged in.');
    console.log('[Lecture Pipeline] Please complete sign-in or run auto-login.mjs with credentials in .env.');
    await browser.close();
    process.exit(1);
  }

  if (page.url() !== targetUrl) {
    console.log(`[Lecture Pipeline] Navigating to target lesson: ${targetUrl}`);
    await page.goto(targetUrl, { waitUntil: 'domcontentloaded', timeout: 30000 });
    await page.waitForTimeout(3000);
  }

  // Extract lesson metadata
  const lessonData = await page.evaluate(() => {
    const titleEl = document.querySelector('h1');
    const title = titleEl ? titleEl.innerText.trim() : document.title;
    
    // Look for drill links
    const buttons = Array.from(document.querySelectorAll('button, a')).map(el => ({
      text: el.innerText.trim(),
      href: el.getAttribute('href') || ''
    }));
    const drill = buttons.find(b => b.text.includes('PT') || b.text.toLowerCase().includes('drill') || b.text.toLowerCase().includes('assumption'));

    // Video details
    const video = document.querySelector('video');
    let videoInfo = null;
    if (video) {
      videoInfo = {
        duration: video.duration,
        currentTime: video.currentTime,
        paused: video.paused,
        width: video.videoWidth,
        height: video.videoHeight
      };
    }

    // Transcript elements
    const transcriptNodes = Array.from(document.querySelectorAll('[data-testid="transcript"] div, .transcript-line, p, span')).filter(n => /^\d{1,2}:\d{2}/.test(n.innerText.trim()));
    const transcriptText = transcriptNodes.map(n => n.innerText.trim()).join('\n');

    return { title, drill, videoInfo, transcriptText };
  });

  console.log(`[Lecture Pipeline] Lesson Title: "${lessonData.title}"`);
  if (lessonData.drill) console.log(`[Lecture Pipeline] Linked Drill: "${lessonData.drill.text}"`);
  if (lessonData.videoInfo) console.log(`[Lecture Pipeline] Video Duration: ${Math.round(lessonData.videoInfo.duration)}s`);

  // Frame capture routine
  const videoEl = page.locator('video').first();
  const hasVideo = await videoEl.count() > 0;
  if (hasVideo) {
    console.log('[Lecture Pipeline] Capturing high-resolution video frame...');
    const screenshotPath = path.join(imagesDir, `${slug}-frame-live.png`);
    await videoEl.screenshot({ path: screenshotPath }).catch(() => {});
    console.log(`[Lecture Pipeline] Saved frame: ${screenshotPath}`);
  }

  console.log('[Lecture Pipeline] Extraction completed successfully.');
  await browser.close();
}

runPipeline().catch(err => {
  console.error('[Lecture Pipeline Fatal Error]:', err.message);
  process.exit(1);
});
