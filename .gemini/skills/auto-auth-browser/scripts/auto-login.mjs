#!/usr/bin/env node
// auto-login.mjs: Instant automated authentication for Loophole Online and LSAT platforms.

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

// Read credentials from .env
function loadEnv() {
  const envPath = path.resolve(__dirname, '../../../../.env');
  if (!fs.existsSync(envPath)) return {};
  const lines = fs.readFileSync(envPath, 'utf8').split('\n');
  const env = {};
  for (const line of lines) {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith('#')) continue;
    const eqIdx = trimmed.indexOf('=');
    if (eqIdx !== -1) {
      const key = trimmed.slice(0, eqIdx).trim();
      const val = trimmed.slice(eqIdx + 1).trim();
      env[key] = val;
    }
  }
  return env;
}

const env = loadEnv();
const email = env.LOOPHOLE_EMAIL;
const password = env.LOOPHOLE_PASSWORD;

// Parse CLI args
const args = process.argv.slice(2);
function getArg(flag, defaultValue = null) {
  const idx = args.indexOf(flag);
  return (idx !== -1 && idx + 1 < args.length) ? args[idx + 1] : defaultValue;
}

const targetUrl = getArg('--target', 'https://new.theloophole.com/training-camp');
const port = parseInt(getArg('--port', '9223'), 10);
const profileDir = path.resolve(process.env.USERPROFILE, '.edge-live-profile');
const storageStatePath = path.join(profileDir, 'storageState.json');

async function getBrowserAndContext() {
  // Check if Edge CDP is running on port
  try {
    const res = await fetch(`http://localhost:${port}/json/version`);
    if (res.ok) {
      console.log(`[Auto-Login] Attaching to running Edge on port ${port}...`);
      const browser = await chromium.connectOverCDP(`http://localhost:${port}`);
      const context = browser.contexts()[0];
      const page = context.pages()[0] || await context.newPage();
      return { browser, context, page, isCDP: true };
    }
  } catch (e) {
    // Port not responding, fallback to persistent context launch
  }

  console.log(`[Auto-Login] Launching Edge with persistent profile: ${profileDir}...`);
  const context = await chromium.launchPersistentContext(profileDir, {
    channel: 'msedge',
    headless: false,
    args: [`--remote-debugging-port=${port}`]
  });
  const page = context.pages()[0] || await context.newPage();
  return { context, page, isCDP: false };
}

async function isAlreadyAuthenticated(page) {
  try {
    await page.goto('https://new.theloophole.com/training-camp', { waitUntil: 'domcontentloaded', timeout: 15000 });
    await page.waitForTimeout(2000);
    const url = page.url();
    return !url.includes('/welcome') && !url.includes('/sign-in');
  } catch (e) {
    return false;
  }
}

async function run() {
  console.log('[Auto-Login] Checking authentication status for Loophole Online...');

  const { browser, context, page, isCDP } = await getBrowserAndContext();

  const authed = await isAlreadyAuthenticated(page);
  if (authed) {
    console.log('[Auto-Login] Current session is already authenticated!');
    if (targetUrl && page.url() !== targetUrl) {
      console.log(`[Auto-Login] Navigating directly to target URL: ${targetUrl}`);
      await page.goto(targetUrl, { waitUntil: 'domcontentloaded' });
    }
    console.log(`[Auto-Login] Active page: "${await page.title()}" (${page.url()})`);
    if (isCDP) await browser.close();
    return;
  }

  // Not authenticated, verify credentials exist
  if (!email || !password) {
    console.error(`
[Auto-Login Error] Missing credentials in .env!
Please add the following lines to your root .env file:
  LOOPHOLE_EMAIL=your-email@example.com
  LOOPHOLE_PASSWORD=your-password
`);
    if (isCDP) await browser.close();
    else await context.close();
    process.exit(1);
  }

  console.log(`[Auto-Login] Performing automated sign-in for: ${email}...`);
  await page.goto('https://new.theloophole.com/sign-in', { waitUntil: 'domcontentloaded', timeout: 20000 });
  await page.waitForTimeout(1000);

  // Fill credentials
  console.log('[Auto-Login] Submitting login form...');
  await page.locator('input[type="email"], input[name="email"], input[placeholder*="Email"]').fill(email);
  await page.locator('input[type="password"], input[name="password"]').fill(password);

  // Click submit button
  const submitBtn = page.locator('button:has-text("Jump Back In"), button[type="submit"]').first();
  await submitBtn.click();

  // Wait for post-login redirect
  console.log('[Auto-Login] Waiting for post-login redirection...');
  await page.waitForURL(url => !url.href.includes('/sign-in') && !url.href.includes('/welcome'), { timeout: 15000 });
  await page.waitForTimeout(2000);

  console.log('[Auto-Login] Sign-in successful! Saving session state...');
  await context.storageState({ path: storageStatePath }).catch(() => {});

  if (targetUrl && page.url() !== targetUrl) {
    console.log(`[Auto-Login] Navigating to requested target: ${targetUrl}...`);
    await page.goto(targetUrl, { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(2000);
  }

  console.log(`[Auto-Login] Ready! Active page: "${await page.title()}" (${page.url()})`);

  if (isCDP) await browser.close();
}

run().catch(err => {
  console.error('[Auto-Login Fatal Error]:', err.message);
  process.exit(1);
});
