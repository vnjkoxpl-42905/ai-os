#!/usr/bin/env node
/**
 * download_webpage.mjs
 * Comprehensive webpage capture tool for Joshua's AI OS / Antigravity Command Center.
 * 
 * Captures 5 distinct representations of any webpage:
 *   1. <slug>-standalone.html : Fully executed DOM with inlined CSS & resolved URLs (no hydration crash on file://)
 *   2. <slug>.mhtml           : RFC 2557 / MIME multipart archive (fonts, CSS, images bundled)
 *   3. <slug>-raw-source.html : Unaltered initial SSR HTML response
 *   4. <slug>-fullpage.png    : Full-page high-resolution screenshot
 *   5. <slug>-content.md      : Clean Markdown extraction of page content and hierarchy
 *
 * Primary execution: Connects over CDP to the persistent Agent Browser on port 9223.
 */

import { createRequire } from 'module';
import fs from 'fs';
import path from 'path';
import { execSync } from 'child_process';

const require = createRequire('c:/Users/Joshu/dev/ai-os-projects/lsatu/package.json');
const { chromium } = require('playwright-core');

const DEFAULT_PORT = 9223;
const AGENT_BROWSER_LAUNCHER = 'C:\\Users\\Joshu\\Tools\\LSATU-Agent\\launch-agent-browser.ps1';
const DESKTOP_DIR = 'C:/Users/Joshu/Desktop';

function parseArgs(args) {
  const options = {
    url: '',
    outDir: '',
    desktop: true,
    keepOpen: true,
    port: DEFAULT_PORT,
    width: 1440,
    height: 900,
    timeout: 60000,
    mhtml: true,
    screenshot: true,
    markdown: true,
    standalone: true,
    raw: true,
  };

  for (let i = 0; i < args.length; i++) {
    const arg = args[i];
    if (arg === '--url' && args[i + 1]) {
      options.url = args[++i];
    } else if (arg === '--out-dir' && args[i + 1]) {
      options.outDir = args[++i];
    } else if (arg === '--no-desktop') {
      options.desktop = false;
    } else if (arg === '--no-keep-open' || arg === '--close') {
      options.keepOpen = false;
    } else if (arg === '--port' && args[i + 1]) {
      options.port = parseInt(args[++i], 10);
    } else if (arg === '--width' && args[i + 1]) {
      options.width = parseInt(args[++i], 10);
    } else if (arg === '--height' && args[i + 1]) {
      options.height = parseInt(args[++i], 10);
    } else if (arg === '--no-mhtml') {
      options.mhtml = false;
    } else if (arg === '--no-screenshot') {
      options.screenshot = false;
    } else if (arg === '--no-markdown') {
      options.markdown = false;
    } else if (!arg.startsWith('-') && !options.url) {
      options.url = arg;
    }
  }

  return options;
}

function slugifyUrl(rawUrl) {
  try {
    const u = new URL(rawUrl);
    let host = u.hostname.replace(/^www\./, '').replace(/[^a-zA-Z0-9-]/g, '-');
    let pathname = u.pathname.replace(/\/$/, '').replace(/[^a-zA-Z0-9-]/g, '-');
    if (pathname && pathname !== '-') {
      return `${host}${pathname}`;
    }
    return host;
  } catch {
    return 'downloaded-page';
  }
}

async function isPortListening(port) {
  try {
    const res = await fetch(`http://127.0.0.1:${port}/json/version`);
    return res.ok;
  } catch {
    return false;
  }
}

async function ensureAgentBrowser(port) {
  const listening = await isPortListening(port);
  if (listening) {
    return true;
  }

  if (fs.existsSync(AGENT_BROWSER_LAUNCHER)) {
    console.log(`Agent Browser not running on ${port}. Launching via ${AGENT_BROWSER_LAUNCHER}...`);
    try {
      execSync(`powershell -ExecutionPolicy Bypass -File "${AGENT_BROWSER_LAUNCHER}"`, { stdio: 'pipe' });
      for (let i = 0; i < 15; i++) {
        await new Promise(r => setTimeout(r, 500));
        if (await isPortListening(port)) {
          console.log(`Agent Browser successfully started and listening on ${port}.`);
          return true;
        }
      }
    } catch (e) {
      console.warn(`Failed to spawn Agent Browser via script: ${e.message}`);
    }
  }
  return false;
}

async function main() {
  const options = parseArgs(process.argv.slice(2));

  if (!options.url) {
    console.error('Usage: node download_webpage.mjs <url> [options]');
    console.error('Options:');
    console.error('  --out-dir <path>     Target output directory (default: Desktop/<slug>-handoff)');
    console.error('  --no-desktop         Do not write <slug>.html directly to Desktop root');
    console.error('  --no-keep-open       Close the browser tab after downloading');
    console.error('  --port <number>      CDP port (default: 9223)');
    console.error('  --width <number>     Viewport width (default: 1440)');
    console.error('  --height <number>    Viewport height (default: 900)');
    process.exit(1);
  }

  const slug = slugifyUrl(options.url);
  const outDir = options.outDir || path.join(DESKTOP_DIR, `${slug}-handoff`);
  fs.mkdirSync(outDir, { recursive: true });

  console.log(`=== Webpage Download: ${options.url} ===`);
  console.log(`Output Directory: ${outDir}`);

  const browserReady = await ensureAgentBrowser(options.port);
  if (!browserReady) {
    console.error(`Cannot connect to browser on port ${options.port}. Please start Agent Browser.`);
    process.exit(1);
  }

  const browser = await chromium.connectOverCDP(`http://127.0.0.1:${options.port}`);
  const context = browser.contexts()[0] || await browser.newContext();
  const page = await context.newPage();

  const results = {
    url: options.url,
    slug,
    outDir,
    timestamp: new Date().toISOString(),
    files: {},
  };

  try {
    await page.setViewportSize({ width: options.width, height: options.height });
    console.log(`Navigating to ${options.url}...`);

    let response = null;
    try {
      response = await page.goto(options.url, { waitUntil: 'networkidle', timeout: options.timeout });
    } catch {
      console.warn('networkidle timed out (likely active long-polling or analytics). Falling back to domcontentloaded...');
      response = await page.goto(options.url, { waitUntil: 'domcontentloaded', timeout: options.timeout });
      await page.waitForTimeout(3000);
    }

    // 1. Raw Source HTML
    if (options.raw && response) {
      try {
        const rawText = await response.text();
        const rawPath = path.join(outDir, `${slug}-raw-source.html`);
        fs.writeFileSync(rawPath, rawText, 'utf8');
        results.files.rawSource = { path: rawPath, bytes: Buffer.byteLength(rawText) };
        console.log(`[1/5] Raw SSR HTML saved: ${results.files.rawSource.bytes} bytes`);
      } catch (e) {
        console.warn('Could not extract raw response text:', e.message);
      }
    }

    // 2. Progressive scroll to trigger lazy loading / animations / hydration
    console.log('Scrolling page to trigger lazy loading and observers...');
    const scrollHeight = await page.evaluate(() => document.body ? document.body.scrollHeight : 0);
    const step = 450;
    for (let y = 0; y <= scrollHeight + 1000; y += step) {
      await page.evaluate((scrollPos) => window.scrollTo(0, scrollPos), y);
      await page.waitForTimeout(120);
    }
    await page.evaluate(() => window.scrollTo(0, 0));
    await page.waitForTimeout(1000);

    // 3. CDP MHTML Snapshot
    if (options.mhtml) {
      try {
        console.log('Capturing CDP MHTML snapshot...');
        const cdp = await context.newCDPSession(page);
        const { data: mhtmlData } = await cdp.send('Page.captureSnapshot', { format: 'mhtml' });
        const mhtmlPath = path.join(outDir, `${slug}.mhtml`);
        fs.writeFileSync(mhtmlPath, mhtmlData, 'utf8');
        results.files.mhtml = { path: mhtmlPath, bytes: Buffer.byteLength(mhtmlData) };
        console.log(`[2/5] MHTML archive saved: ${results.files.mhtml.bytes} bytes`);
      } catch (e) {
        console.warn('Failed to capture MHTML snapshot:', e.message);
      }
    }

    // 4. Full-page Screenshot
    if (options.screenshot) {
      try {
        console.log('Capturing full-page screenshot...');
        const pngPath = path.join(outDir, `${slug}-fullpage.png`);
        await page.screenshot({ path: pngPath, fullPage: true });
        const stats = fs.statSync(pngPath);
        results.files.screenshot = { path: pngPath, bytes: stats.size };
        console.log(`[3/5] Full-page screenshot saved: ${results.files.screenshot.bytes} bytes`);
      } catch (e) {
        console.warn('Failed to capture screenshot:', e.message);
      }
    }

    // 5. Standalone HTML with inlined stylesheets and rewritten URLs
    if (options.standalone) {
      console.log('Building standalone HTML with inlined CSS...');
      const stylesheetUrls = await page.evaluate(() => {
        return Array.from(document.querySelectorAll('link[rel="stylesheet"]'))
          .map(l => l.href)
          .filter(Boolean);
      });

      const inlinedCss = [];
      const origin = new URL(options.url).origin;

      for (const cssUrl of stylesheetUrls) {
        try {
          const res = await fetch(cssUrl);
          if (res.ok) {
            let cssText = await res.text();
            // Rewrite relative url(...) in CSS to absolute
            cssText = cssText.replace(/url\((['"]?)(\/[^)'"]+)\1\)/g, `url($1${origin}$2$1)`);
            inlinedCss.push(`/* Inlined: ${cssUrl} */\n${cssText}`);
          }
        } catch (e) {
          console.warn(`Could not fetch stylesheet ${cssUrl}: ${e.message}`);
        }
      }

      const standaloneHtml = await page.evaluate(({ cssList, targetUrl, targetOrigin }) => {
        const docClone = document.documentElement.cloneNode(true);

        // Convert relative URLs on src, href, and srcset to absolute
        docClone.querySelectorAll('[src]').forEach(el => {
          const val = el.getAttribute('src');
          if (val && val.startsWith('/')) {
            el.setAttribute('src', targetOrigin + val);
          }
        });

        docClone.querySelectorAll('[href]').forEach(el => {
          const val = el.getAttribute('href');
          if (val && val.startsWith('/')) {
            el.setAttribute('href', targetOrigin + val);
          }
        });

        docClone.querySelectorAll('[srcset]').forEach(el => {
          const val = el.getAttribute('srcset');
          if (val) {
            const updated = val.split(',').map(part => {
              const trimmed = part.trim();
              if (trimmed.startsWith('/')) return targetOrigin + trimmed;
              return trimmed;
            }).join(', ');
            el.setAttribute('srcset', updated);
          }
        });

        // Strip external stylesheet links and preload hints
        docClone.querySelectorAll('link[rel="stylesheet"]').forEach(el => el.remove());
        docClone.querySelectorAll('link[rel="preload"]').forEach(el => el.remove());

        // Ensure base tag is present pointing to target URL
        const head = docClone.querySelector('head') || docClone.insertBefore(document.createElement('head'), docClone.firstChild);
        const base = document.createElement('base');
        base.setAttribute('href', targetUrl);
        head.insertBefore(base, head.firstChild);

        // Inject inlined stylesheets
        for (const css of cssList) {
          const styleEl = document.createElement('style');
          styleEl.setAttribute('data-download-webpage-inlined', 'true');
          styleEl.textContent = css;
          head.appendChild(styleEl);
        }

        // Remove script tags so Next.js / Vue / React hydration engines do not crash over file:// protocol
        docClone.querySelectorAll('script').forEach(el => el.remove());
        docClone.querySelectorAll('next-route-announcer').forEach(el => el.remove());

        return '<!DOCTYPE html>\n' + docClone.outerHTML;
      }, { cssList: inlinedCss, targetUrl: options.url, targetOrigin: origin });

      const standalonePath = path.join(outDir, `${slug}-standalone.html`);
      fs.writeFileSync(standalonePath, standaloneHtml, 'utf8');
      results.files.standaloneHtml = { path: standalonePath, bytes: Buffer.byteLength(standaloneHtml) };
      console.log(`[4/5] Standalone HTML saved: ${results.files.standaloneHtml.bytes} bytes`);

      if (options.desktop) {
        const desktopPath = path.join(DESKTOP_DIR, `${slug}.html`);
        fs.writeFileSync(desktopPath, standaloneHtml, 'utf8');
        results.files.desktopHtml = { path: desktopPath, bytes: Buffer.byteLength(standaloneHtml) };
        console.log(`[*] Desktop root shortcut saved: ${desktopPath}`);
      }
    }

    // 6. Clean Markdown Extraction
    if (options.markdown) {
      console.log('Extracting page text and structure into Markdown...');
      const mdContent = await page.evaluate((pageUrl) => {
        const title = document.title || 'Untitled';
        const metaDesc = document.querySelector('meta[name="description"]')?.getAttribute('content') || '';
        
        let md = `# ${title}\n\n`;
        md += `**Source URL:** [${pageUrl}](${pageUrl})\n`;
        md += `**Captured At:** ${new Date().toISOString()}\n`;
        if (metaDesc) {
          md += `**Description:** ${metaDesc}\n`;
        }
        md += `\n---\n\n`;

        // Walk headings and paragraphs
        const elements = document.querySelectorAll('h1, h2, h3, h4, p, li, blockquote');
        const lines = [];
        let lastTag = '';

        elements.forEach(el => {
          const text = el.innerText.trim();
          if (!text) return;
          const tag = el.tagName.toLowerCase();

          if (tag === 'h1') {
            lines.push(`\n# ${text}\n`);
          } else if (tag === 'h2') {
            lines.push(`\n## ${text}\n`);
          } else if (tag === 'h3') {
            lines.push(`\n### ${text}\n`);
          } else if (tag === 'h4') {
            lines.push(`\n#### ${text}\n`);
          } else if (tag === 'li') {
            lines.push(`- ${text}`);
          } else if (tag === 'blockquote') {
            lines.push(`> ${text}`);
          } else {
            lines.push(`\n${text}\n`);
          }
          lastTag = tag;
        });

        return md + lines.join('\n');
      }, options.url);

      const mdPath = path.join(outDir, `${slug}-content.md`);
      fs.writeFileSync(mdPath, mdContent, 'utf8');
      results.files.markdown = { path: mdPath, bytes: Buffer.byteLength(mdContent) };
      console.log(`[5/5] Extracted Markdown saved: ${results.files.markdown.bytes} bytes`);
    }

    if (options.keepOpen) {
      await page.bringToFront();
      console.log('Page brought to front in Agent Browser.');
    } else {
      await page.close().catch(() => {});
    }

    console.log('\n=== Download Complete ===');
    console.log(JSON.stringify(results, null, 2));

  } finally {
    await browser.close().catch(() => {});
  }
}

main().catch(err => {
  console.error('Fatal error during download:', err);
  process.exit(1);
});
