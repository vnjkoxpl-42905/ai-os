import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { createRequire } from 'node:module';
import { execFileSync } from 'node:child_process';
import { projectPath, vaultRoot } from './project-paths.mjs';

// Generated catalog only. Platform access is authenticated admin READS.
const destinations = ['references/lsatu-guided-drill-catalog.json', 'references/lsatu-guided-drill-catalog.md'].map(p => path.join(vaultRoot, p));
const hash = value => crypto.createHash('sha256').update(value).digest('hex');
const originalHashes = destinations.map(p => fs.existsSync(p) ? hash(fs.readFileSync(p)) : null);
function readEnv(file) {
  return Object.fromEntries(fs.readFileSync(file, 'utf8').split(/\r?\n/).flatMap(line => {
    const m = /^\s*([^#=\s]+)\s*=\s*(.*?)\s*$/.exec(line);
    return m ? [[m[1], m[2].replace(/^["']|["']$/g, '')]] : [];
  }));
}
const env = { ...readEnv(projectPath('lsatu', '.env')), ...readEnv(path.join(vaultRoot, '.env')) };
const base = env.VITE_SUPABASE_URL;
const apikey = env.VITE_SUPABASE_PUBLISHABLE_KEY;
if (!base || !apikey || !env.LSATPREP_ADMIN_EMAIL || !env.LSATPREP_ADMIN_PASSWORD) throw new Error('Missing LSAT U configuration');
const response = await fetch(`${base}/auth/v1/token?grant_type=password`, { method: 'POST', headers: { apikey, 'content-type': 'application/json' }, body: JSON.stringify({ email: env.LSATPREP_ADMIN_EMAIL, password: env.LSATPREP_ADMIN_PASSWORD }) });
const auth = await response.json();
if (!response.ok || !auth.access_token) throw new Error('Admin sign-in failed');
const ops = projectPath('.lsatu-ops');
const req = createRequire(path.join(ops, 'package.json'));
const { build } = req('esbuild');
const bundled = await build({ entryPoints: [path.join(ops, 'src/lib/questionLoader.ts')], bundle: true, write: false, platform: 'node', format: 'esm' });
const { normalizeQType } = await import(`data:text/javascript;base64,${Buffer.from(bundled.outputFiles[0].text).toString('base64')}`);
const [catalogResponse, bankResponse] = await Promise.all([
  fetch(`${base}/rest/v1/guided_drills?select=*&order=week.asc,order_in_week.asc,slug.asc&limit=10000`, { headers: { apikey, authorization: `Bearer ${auth.access_token}` } }),
  fetch('https://lsatprep.study/data/_bank.generated.json'),
]);
if (!catalogResponse.ok || !bankResponse.ok) throw new Error('Catalog or deployed bank read failed');
const catalogBytes = await catalogResponse.text();
const bankBytes = await bankResponse.text();
const drills = JSON.parse(catalogBytes);
const sections = JSON.parse(bankBytes);
if (!Array.isArray(drills) || !Array.isArray(sections) || !sections.length) throw new Error('Invalid catalog/bank');
const bank = new Map();
for (const entry of sections) {
  if (!entry.filename || !Array.isArray(entry.questions)) throw new Error('Invalid deployed bank section');
  const [, pt, section] = /PT(\d+)-S(\d+)/.exec(entry.filename) || [];
  if (!pt || !section) throw new Error('Invalid bank filename');
  for (const q of entry.questions) {
    if (q.status === 'removed' || !q.answerChoices || !q.correctAnswer || !q.questionStem) continue;
    const qid = `PT${pt}-S${section}-Q${q.questionNumber || 0}`;
    bank.set(qid, { qid, qtype: normalizeQType(q.questionType || '', q.questionStem), difficulty: q.questionDifficulty || q.Question_Difficulty || 3, questionFeatures: Array.isArray(q.questionFeatures) ? q.questionFeatures : [], reasoningType: Array.isArray(q.reasoningType) ? q.reasoningType : q.reasoningType ? [q.reasoningType] : [] });
  }
}
const all = [...bank.values()];
const bands = { beginner: [1, 3], intermediate: [2, 4], advanced: [3, 5] };
const lower = values => new Set((values || []).map(x => x.toLowerCase()));
function matches(q, filter) {
  const f = filter || {};
  const types = lower(f.qtypes), features = lower(f.features), reasoning = lower(f.reasoning_types);
  return (!types.size || types.has(q.qtype.toLowerCase())) && (!features.size || q.questionFeatures.some(x => features.has(x.toLowerCase()))) && (!reasoning.size || q.reasoningType.some(x => reasoning.has(x.toLowerCase()))) && (f.difficulty_min == null || q.difficulty >= f.difficulty_min) && (f.difficulty_max == null || q.difficulty <= f.difficulty_max);
}
const rows = drills.map(drill => {
  const pool = all.filter(q => matches(q, drill.bank_filter));
  const histogram = Object.fromEntries([1, 2, 3, 4, 5].map(d => [d, pool.filter(q => q.difficulty === d).length]));
  const count = drill.question_count ?? Math.min(pool.length, 10);
  const eligible = Object.fromEntries(Object.entries(bands).map(([level, [min, max]]) => {
    const inBand = pool.filter(q => q.difficulty >= min && q.difficulty <= max).length;
    return [level, { in_band: inBand, default_count: count, fallback_needed: inBand < Math.min(count, pool.length) }];
  }));
  return { ...drill, pool_summary: { total: pool.length, difficulty_counts: histogram, difficulty_min: pool.length ? Math.min(...pool.map(q => q.difficulty)) : null, difficulty_max: pool.length ? Math.max(...pool.map(q => q.difficulty)) : null, levels: eligible, pinned_qids: (drill.question_qids || []).length, missing_pinned_qids: (drill.question_qids || []).filter(qid => !bank.has(qid)) } };
});
const commit = execFileSync('git', ['rev-parse', 'HEAD'], { cwd: ops, encoding: 'utf8' }).trim();
const meta = { generated_at: new Date().toISOString(), source: `${base}/rest/v1/guided_drills`, question_bank: 'https://lsatprep.study/data/_bank.generated.json', catalog_sha256: hash(catalogBytes), bank_sha256: hash(bankBytes), ops_commit: commit, question_count: bank.size, drill_count: rows.length, published_count: rows.filter(d => d.is_published).length };
const json = JSON.stringify({ meta, bands, drills: rows }, null, 2) + '\n';
const escape = s => String(s ?? '').replace(/\|/g, '\\|').replace(/\r?\n/g, ' ');
const lines = ['<!-- GENERATED by system/scripts/refresh-guided-drill-catalog.mjs. Refresh, do not hand-edit. -->', '# Find and assign existing guided drills', '', `Live snapshot: ${meta.generated_at}. ${meta.drill_count} drills (${meta.published_count} published); ${meta.question_count} deployed questions.`, '', 'Refresh from the vault: `node system/scripts/refresh-guided-drill-catalog.mjs`. No browser and no platform writes. Reads all drill metadata once and the deployed merged bank once. The JSON companion includes complete filters and instruction cards.', '', 'Search this table by reasoning type, question type, feature, title, or exact slug. Use the exact slug in assignment plans. Inspect its JSON row before assigning. Existing catalog content is preferred to creating another drill.', '', 'Difficulty counts are the actual deployed pool, ordered 1/2/3/4/5. B/I/A are eligible question counts at beginner (1–3), intermediate (2–4), and advanced (3–5). These levels prefer a band and may fall back outside it; intermediate does not guarantee a ceiling of 3. A pinned list overrides level/count and must be checked independently. For strict ceilings, check the pool or resolved exact questions before writes. A title saying “Easier” is not sufficient evidence.', '', `Catalog SHA256: \`${meta.catalog_sha256}\`. Bank SHA256: \`${meta.bank_sha256}\`. App normalization source: \`${commit}\`.`, '', '| Slug | Title | Published | Level | Default count | Qtypes / reasoning / features | Filter band | Pool 1/2/3/4/5 | B/I/A | Pins |', '|---|---|---|---|---:|---|---|---|---|---:|'];
for (const d of rows) {
  const f = d.bank_filter || {}, p = d.pool_summary;
  const types = [...new Set((f.qtypes || []).map(type => normalizeQType(type)))];
  const labels = [types.join(', '), f.reasoning_types?.join(', '), f.features?.join(', ')].filter(Boolean).join(' / ') || 'All questions';
  lines.push(`| ${escape(d.slug)} | ${escape(d.title)} | ${d.is_published ? 'Yes' : 'No'} | ${d.level || 'any'} | ${d.question_count ?? 'auto'} | ${escape(labels)} | ${f.difficulty_min ?? 'any'}–${f.difficulty_max ?? 'any'} | ${Object.values(p.difficulty_counts).join('/')} | ${Object.values(p.levels).map(x => x.in_band).join('/')} | ${p.pinned_qids} |`);
}
const output = [json, lines.join('\n') + '\n'];
// Refuse overwriting another session's newer generation.
destinations.forEach((p, i) => { if ((fs.existsSync(p) ? hash(fs.readFileSync(p)) : null) !== originalHashes[i]) throw new Error(`Concurrent catalog update: ${p}`); });
destinations.forEach((p, i) => fs.writeFileSync(p, output[i]));
console.log(JSON.stringify(meta));
