#!/usr/bin/env node
// edge-control.mjs: Comprehensive live browser control for Microsoft Edge via Playwright CDP.

import { createRequire } from 'module';
import { fileURLToPath } from 'url';
import path from 'path';
import fs from 'fs';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Resolve Playwright from ../ai-os-projects/lsatu
let chromium;
try {
  const possiblePaths = [
    path.resolve(__dirname, '../../../../../ai-os-projects/lsatu/package.json'),
    path.resolve(process.cwd(), '../ai-os-projects/lsatu/package.json'),
    'C:/Users/Joshu/dev/ai-os-projects/lsatu/package.json'
  ];
  let pkgPath = possiblePaths.find(p => fs.existsSync(p));
  if (!pkgPath) pkgPath = possiblePaths[0];

  const requireLsatu = createRequire(pkgPath);
  const pw = requireLsatu('playwright');
  chromium = pw.chromium;
} catch (e) {
  try {
    const pw = await import('playwright');
    chromium = pw.chromium;
  } catch (err) {
    console.error('Failed to load Playwright. Ensure ../ai-os-projects/lsatu has playwright installed. Details:', e.message);
    process.exit(1);
  }
}

// Parse command line arguments
const args = process.argv.slice(2);
const command = args[0] || 'help';

function getArg(flag, defaultValue = null) {
  const idx = args.indexOf(flag);
  if (idx !== -1 && idx + 1 < args.length) {
    return args[idx + 1];
  }
  return defaultValue;
}

function hasArg(flag) {
  return args.includes(flag);
}

const port = parseInt(getArg('--port', '9223'), 10);
const cdpUrl = `http://localhost:${port}`;

async function checkPortStatus() {
  try {
    const res = await fetch(`${cdpUrl}/json/version`);
    if (!res.ok) return { ok: false, status: res.status };
    const data = await res.json();
    return { ok: true, data };
  } catch (err) {
    return { ok: false, error: err.message };
  }
}

async function connectToBrowser() {
  const status = await checkPortStatus();
  if (!status.ok) {
    throw new Error(`Cannot connect to Edge on port ${port}. Edge may not be running with --remote-debugging-port=${port}.`);
  }
  return await chromium.connectOverCDP(cdpUrl);
}

async function findTargetPage(browser, matchPattern = null, targetIndex = null) {
  const contexts = browser.contexts();
  const allPages = [];
  for (const ctx of contexts) {
    for (const page of ctx.pages()) {
      allPages.push(page);
    }
  }

  if (allPages.length === 0) {
    throw new Error('No open pages or tabs found in Edge.');
  }

  if (targetIndex !== null) {
    const idx = parseInt(targetIndex, 10);
    if (idx >= 0 && idx < allPages.length) {
      return allPages[idx];
    }
    throw new Error(`Target index ${idx} out of range (0 to ${allPages.length - 1}).`);
  }

  if (matchPattern) {
    const patternLower = matchPattern.toLowerCase();
    for (const page of allPages) {
      const url = page.url().toLowerCase();
      const title = (await page.title()).toLowerCase();
      if (url.includes(patternLower) || title.includes(patternLower)) {
        return page;
      }
    }
    throw new Error(`No open tab found matching pattern: "${matchPattern}".`);
  }

  return allPages[0];
}

async function listTabs(browser) {
  const contexts = browser.contexts();
  const results = [];
  let index = 0;
  for (const ctx of contexts) {
    for (const page of ctx.pages()) {
      results.push({
        index: index++,
        title: await page.title(),
        url: page.url()
      });
    }
  }
  return results;
}

async function run() {
  switch (command) {
    case 'status': {
      const status = await checkPortStatus();
      if (status.ok) {
        console.log(`Edge CDP is ACTIVE on port ${port}:`);
        console.log(JSON.stringify(status.data, null, 2));
      } else {
        console.log(`Edge CDP is INACTIVE on port ${port}.`);
        if (status.error) console.log(`Details: ${status.error}`);
        process.exit(1);
      }
      break;
    }

    case 'tabs': {
      const browser = await connectToBrowser();
      const tabs = await listTabs(browser);
      if (hasArg('--json')) {
        console.log(JSON.stringify(tabs, null, 2));
      } else {
        console.log(`Found ${tabs.length} open tab(s) in Edge:`);
        tabs.forEach(t => {
          console.log(`[${t.index}] ${t.title || 'Untitled'}`);
          console.log(`    URL: ${t.url}`);
        });
      }
      await browser.close();
      break;
    }

    case 'inspect': {
      const browser = await connectToBrowser();
      const match = getArg('--match');
      const idx = getArg('--index');
      const page = await findTargetPage(browser, match, idx);

      const title = await page.title();
      const url = page.url();
      const selector = getArg('--selector');

      console.log(`Connected to tab: "${title}"`);
      console.log(`URL: ${url}`);
      console.log('----------------------------------------------------');

      if (selector) {
        const elements = await page.locator(selector).all();
        console.log(`Found ${elements.length} match(es) for selector "${selector}":`);
        for (let i = 0; i < elements.length; i++) {
          const text = await elements[i].innerText().catch(() => '');
          console.log(`[#${i}] ${text.trim()}`);
        }
      } else if (hasArg('--text-only')) {
        const bodyText = await page.locator('body').innerText();
        console.log(bodyText);
      } else {
        // Deep structured inspection: headings, buttons, forms, main text
        const inspection = await page.evaluate(() => {
          const headings = Array.from(document.querySelectorAll('h1, h2, h3')).map(h => ({
            tag: h.tagName.toLowerCase(),
            text: h.innerText.trim()
          }));
          const buttons = Array.from(document.querySelectorAll('button, a[role="button"]')).map(b => b.innerText.trim()).filter(Boolean);
          const videos = Array.from(document.querySelectorAll('video')).map(v => ({
            src: v.currentSrc || v.src,
            duration: v.duration,
            currentTime: v.currentTime,
            paused: v.paused
          }));
          const textSnippet = document.body.innerText.slice(0, 1000);
          return { headings, buttons, videos, textSnippet };
        });

        console.log('Headings:');
        inspection.headings.forEach(h => console.log(`  <${h.tag}>: ${h.text}`));
        console.log('\nButtons:', inspection.buttons.slice(0, 15).join(' | '));
        if (inspection.videos.length > 0) {
          console.log('\nVideos found:', inspection.videos);
        }
        console.log('\nText Preview (first 1000 chars):\n', inspection.textSnippet);
      }

      await browser.close();
      break;
    }

    case 'video': {
      const browser = await connectToBrowser();
      const match = getArg('--match');
      const idx = getArg('--index');
      const page = await findTargetPage(browser, match, idx);

      console.log(`Inspecting media on tab: "${await page.title()}"`);

      const mediaReport = await page.evaluate(async () => {
        const report = {
          videos: [],
          textTracks: [],
          playerContext: {}
        };

        const videoEls = Array.from(document.querySelectorAll('video'));
        for (let i = 0; i < videoEls.length; i++) {
          const v = videoEls[i];
          const vData = {
            index: i,
            currentSrc: v.currentSrc || v.src,
            duration: v.duration,
            currentTime: v.currentTime,
            paused: v.paused,
            playbackRate: v.playbackRate,
            videoWidth: v.videoWidth,
            videoHeight: v.videoHeight,
            tracks: []
          };

          if (v.textTracks && v.textTracks.length > 0) {
            for (let t = 0; t < v.textTracks.length; t++) {
              const track = v.textTracks[t];
              const cues = [];
              if (track.cues) {
                for (let c = 0; c < track.cues.length; c++) {
                  const cue = track.cues[c];
                  cues.push({
                    start: cue.startTime,
                    end: cue.endTime,
                    text: cue.text
                  });
                }
              }
              vData.tracks.push({
                label: track.label,
                language: track.language,
                kind: track.kind,
                mode: track.mode,
                cuesCount: cues.length,
                cues: cues.slice(0, 100)
              });
            }
          }

          report.videos.push(vData);
        }

        // Check for embedded iframes (Vimeo, Wistia, YouTube)
        const iframes = Array.from(document.querySelectorAll('iframe')).map(f => ({
          src: f.src,
          id: f.id,
          title: f.title
        }));
        report.iframes = iframes;

        // Check global player objects
        if (window.Wistia) report.playerContext.hasWistia = true;
        if (window.Vimeo) report.playerContext.hasVimeo = true;

        return report;
      });

      console.log('Media Extraction Report:');
      console.log(JSON.stringify(mediaReport, null, 2));

      await browser.close();
      break;
    }

    case 'click': {
      const browser = await connectToBrowser();
      const match = getArg('--match');
      const idx = getArg('--index');
      const page = await findTargetPage(browser, match, idx);

      const selector = getArg('--selector');
      const text = getArg('--text');

      if (!selector && !text) {
        throw new Error('Please specify either --selector <css> or --text <content> to click.');
      }

      if (selector) {
        console.log(`Clicking selector "${selector}"...`);
        await page.locator(selector).first().click();
      } else {
        console.log(`Clicking element with text "${text}"...`);
        await page.getByText(text, { exact: false }).first().click();
      }

      console.log('Click executed successfully.');
      await browser.close();
      break;
    }

    case 'navigate': {
      const browser = await connectToBrowser();
      const url = getArg('--url');
      if (!url) throw new Error('Specify target URL using --url <url>.');

      const match = getArg('--match');
      const idx = getArg('--index');
      let page;
      try {
        page = await findTargetPage(browser, match, idx);
      } catch {
        const ctx = browser.contexts()[0] || await browser.newContext();
        page = await ctx.newPage();
      }

      console.log(`Navigating to ${url}...`);
      await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 30000 });
      console.log(`Navigation complete: "${await page.title()}"`);

      await browser.close();
      break;
    }

    case 'eval': {
      const browser = await connectToBrowser();
      const match = getArg('--match');
      const idx = getArg('--index');
      const page = await findTargetPage(browser, match, idx);

      const code = getArg('--code');
      if (!code) throw new Error('Specify code to evaluate with --code "<javascript>".');

      const result = await page.evaluate((js) => {
        return eval(js);
      }, code);

      console.log('Result:', JSON.stringify(result, null, 2));
      await browser.close();
      break;
    }

    case 'screenshot': {
      const browser = await connectToBrowser();
      const match = getArg('--match');
      const idx = getArg('--index');
      const page = await findTargetPage(browser, match, idx);

      const outPath = getArg('--out', path.resolve(__dirname, '../../../.gemini/output/edge-tab.png'));
      const dir = path.dirname(outPath);
      if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });

      const fullPage = hasArg('--full-page');
      await page.screenshot({ path: outPath, fullPage });
      console.log(`Screenshot saved to: ${outPath}`);

      await browser.close();
      break;
    }

    default:
      console.log(`
Edge Live Control CLI

Usage:
  node edge-control.mjs <command> [options]

Commands:
  status                               Check if Edge CDP is active
  tabs [--json]                        List open tabs
  inspect [--match <pattern>]          Inspect tab content and DOM
  video [--match <pattern>]            Extract video players, tracks, cues
  click --selector <css> | --text <t>  Click element
  navigate --url <url>                 Navigate tab to URL
  eval --code "<javascript>"           Execute JS in tab
  screenshot [--out <path>]            Save screenshot of tab

Options:
  --port <port>                        CDP port (default: 9223)
  --match <pattern>                    Match tab by URL or title substring
  --index <n>                          Target tab by index
`);
  }
}

run().catch(err => {
  console.error('Execution Error:', err.message);
  process.exit(1);
});
