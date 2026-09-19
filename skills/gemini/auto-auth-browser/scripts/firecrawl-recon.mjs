#!/usr/bin/env node
// firecrawl-recon.mjs: Link discovery and syllabus reconnaissance using Firecrawl API.

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

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
      env[trimmed.slice(0, eqIdx).trim()] = trimmed.slice(eqIdx + 1).trim();
    }
  }
  return env;
}

const env = loadEnv();
const apiKey = env.FIRECRAWL_API_KEY;

if (!apiKey) {
  console.error('[Firecrawl Recon Error] Missing FIRECRAWL_API_KEY in .env');
  process.exit(1);
}

const args = process.argv.slice(2);
const query = args[0] || 'sufficient assumption';

async function searchLinks() {
  console.log(`[Firecrawl Recon] Searching for lesson links matching: "${query}"...`);

  // Target base course map or sitemap
  const targetUrl = 'https://new.theloophole.com/training-camp';
  const res = await fetch('https://api.firecrawl.dev/v1/scrape', {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer ' + apiKey,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      url: targetUrl,
      formats: ['links', 'markdown']
    })
  });

  const json = await res.json();
  if (!json.success) {
    console.error('[Firecrawl Recon Error]', json.error);
    process.exit(1);
  }

  const links = json.data?.links || [];
  const matches = links.filter(l => l.toLowerCase().includes(query.toLowerCase().replace(/\s+/g, '-')));

  console.log(`[Firecrawl Recon] Found ${matches.length} matching link(s):`);
  matches.forEach(m => console.log(' -', m));

  return matches;
}

searchLinks().catch(err => console.error(err));
