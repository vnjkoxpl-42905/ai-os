#!/usr/bin/env node
// edge-daemon.mjs: Persistent background daemon maintaining Microsoft Edge with CDP enabled on port 9223.

import { createRequire } from 'module';
import { fileURLToPath } from 'url';
import path from 'path';
import fs from 'fs';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const possiblePaths = [
  path.resolve(__dirname, '../../../../projects/lsatu/package.json'),
  path.resolve(process.cwd(), 'projects/lsatu/package.json'),
  'C:/Users/Joshu/dev/ai-os/projects/lsatu/package.json'
];
let pkgPath = possiblePaths.find(p => fs.existsSync(p)) || possiblePaths[0];
const requireLsatu = createRequire(pkgPath);
const { chromium } = requireLsatu('playwright');

const port = parseInt(process.env.EDGE_PORT || '9223', 10);
const profileDir = path.resolve(process.env.USERPROFILE, '.edge-live-profile');

const initialUrl = process.argv[2] || 'https://new.theloophole.com/training-camp/browse/stage/learn/video/conditional-sufficient-assumption-sa-strategy';

async function main() {
  console.log(`[Edge Daemon] Starting Microsoft Edge with CDP on port ${port}...`);
  console.log(`[Edge Daemon] User profile: ${profileDir}`);

  // Launch persistent context
  const context = await chromium.launchPersistentContext(profileDir, {
    channel: 'msedge',
    headless: false,
    viewport: null,
    args: [
      `--remote-debugging-port=${port}`,
      '--start-maximized'
    ]
  });

  const page = context.pages()[0] || await context.newPage();
  if (initialUrl && initialUrl !== 'about:blank') {
    console.log(`[Edge Daemon] Opening initial URL: ${initialUrl}`);
    await page.goto(initialUrl).catch(err => console.log(`[Edge Daemon] Navigation notice: ${err.message}`));
  }

  console.log(`[Edge Daemon] EDGE_DAEMON_READY on port ${port}`);

  // Keep daemon alive
  process.on('SIGINT', async () => {
    console.log('[Edge Daemon] Shutting down...');
    await context.close();
    process.exit(0);
  });

  process.on('SIGTERM', async () => {
    console.log('[Edge Daemon] Terminating...');
    await context.close();
    process.exit(0);
  });

  // Keep event loop active
  setInterval(() => {}, 10000);
}

main().catch(err => {
  console.error('[Edge Daemon] Fatal error:', err);
  process.exit(1);
});
