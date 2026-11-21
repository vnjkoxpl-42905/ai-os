// Copy existing teacher-owned Reading Center texts to one student's private library.
// Dry-run by default. Normal admin authentication and table RLS remain enforced.
import fs from 'node:fs';
import path from 'node:path';
import { createHash } from 'node:crypto';
import { fileURLToPath } from 'node:url';
import { projectPath } from './project-paths.mjs';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const argv = process.argv.slice(2);
const arg = (key) => { const i = argv.indexOf(`--${key}`); return i < 0 ? undefined : argv[i + 1]; };
const email = arg('student');
const manifestPath = arg('manifest');
const receiptPath = arg('receipt');
if (!email || !manifestPath) throw new Error('Required: --student EMAIL --manifest PATH [--apply] [--receipt PATH]');
const envFile = (file) => Object.fromEntries(fs.readFileSync(file, 'utf8').split(/\r?\n/)
  .map((s) => s.trim()).filter((s) => s && !s.startsWith('#') && s.includes('='))
  .map((s) => [s.slice(0, s.indexOf('=')).trim(), s.slice(s.indexOf('=') + 1).trim().replace(/^["']|["']$/g, '')]));
const env = { ...envFile(projectPath('lsatu', '.env')), ...envFile(path.join(root, '.env')) };
const url = env.VITE_SUPABASE_URL;
const key = env.VITE_SUPABASE_PUBLISHABLE_KEY;
const authResponse = await fetch(`${url}/auth/v1/token?grant_type=password`, {
  method: 'POST', headers: { apikey: key, 'content-type': 'application/json' },
  body: JSON.stringify({ email: env.LSATPREP_ADMIN_EMAIL, password: env.LSATPREP_ADMIN_PASSWORD }),
});
const auth = await authResponse.json();
if (!authResponse.ok || !auth.access_token) throw new Error('Admin sign-in failed');
const headers = { apikey: key, authorization: `Bearer ${auth.access_token}`, 'content-type': 'application/json' };
async function request(route, init = {}) {
  const response = await fetch(`${url}/${route}`, { ...init, headers: { ...headers, ...init.headers } });
  const data = await response.json();
  if (!response.ok) throw new Error(`${route.split('?')[0]}: ${data.message ?? data.error ?? response.status}`);
  return data;
}
const users = await request('functions/v1/admin-manage-users');
const matches = users.filter((u) => u.email?.toLowerCase() === email.toLowerCase());
if (matches.length !== 1) throw new Error('Exact student email did not resolve uniquely');
const student = matches[0];
const studentId = student.class_id;
if (!studentId || studentId === auth.user.id) throw new Error('Expected a distinct student account');
const items = await request(`rest/v1/classroom_items?student_id=eq.${studentId}&source_table=eq.reading_center&source_id=eq.library&visible_to_student=eq.true&status=in.(assigned,in_progress,completed)&select=id,status,unlock_at,metadata_json`);
const active = items.filter((i) => !i.unlock_at || Date.parse(i.unlock_at) <= Date.now());
if (active.length !== 1) throw new Error('Student needs exactly one immediately available Reading Center grant');
const manifest = JSON.parse(fs.readFileSync(path.resolve(manifestPath), 'utf8'));
if (!Array.isArray(manifest) || !manifest.length || manifest.length > 20) throw new Error('Manifest must contain 1–20 passages');
const library = await request(`rest/v1/reading_center_passages?owner_id=eq.${studentId}&select=*`);
const normalize = (s) => s.replace(/\r\n/g, '\n');
const digest = (s) => createHash('sha256').update(normalize(s)).digest('hex');
const planned = [];
for (const input of manifest) {
  if (!input.title || !input.body?.trim()) throw new Error('Missing title or complete passage body');
  const slug = new URL(input.url).pathname.split('/').pop();
  const originals = await request(`rest/v1/reading_center_passages?slug=eq.${encodeURIComponent(slug)}&select=*`);
  if (originals.length !== 1) throw new Error(`Original missing: ${input.title}`);
  const original = originals[0];
  if (original.owner_id !== auth.user.id || original.title !== input.title || digest(original.body) !== digest(input.body)) throw new Error(`Original identity/text mismatch: ${input.title}`);
  const copySlug = `student-${studentId.slice(0, 8)}-${original.id}`;
  const existing = library.filter((p) => p.slug === copySlug || (p.title === input.title && digest(p.body) === digest(input.body)));
  if (existing.length > 1) throw new Error(`Multiple existing student copies: ${input.title}`);
  const row = existing[0];
  if (row && (row.title !== input.title || digest(row.body) !== digest(input.body) || row.owner_id !== studentId || !row.is_published)) throw new Error(`Student copy differs: ${input.title}`);
  planned.push({ original, existing: row, row: {
    slug: copySlug, owner_id: studentId, title: input.title, body: original.body,
    author: original.author, genre: original.genre, cover_url: original.cover_url,
    word_count: original.word_count, sort_order: Number(input.title.match(/^\d+/)?.[0] ?? planned.length + 1),
    is_published: true,
  } });
}
if (new Set(planned.map((p) => p.original.id)).size !== planned.length) throw new Error('Duplicate source passages in manifest');
console.log(JSON.stringify({ dry_run: !argv.includes('--apply'), student: email, student_id: studentId, assignment_id: active[0].id,
  passages: planned.map((p) => ({ title: p.row.title, words: p.row.word_count, action: p.existing ? 'reuse verified copy' : 'create private student copy' })) }, null, 2));
if (!argv.includes('--apply')) process.exit(0);
const missing = planned.filter((p) => !p.existing).map((p) => p.row);
// One atomic insert; deterministic unique slugs make retries fail closed rather than duplicate.
if (missing.length) await request('rest/v1/reading_center_passages', {
  method: 'POST', headers: { prefer: 'return=representation' }, body: JSON.stringify(missing),
});
const after = await request(`rest/v1/reading_center_passages?owner_id=eq.${studentId}&select=*`);
const receipt = { verified_at: new Date().toISOString(), student_email: email, student_id: studentId,
  assignment: active[0], verification_scope: 'Normal-admin saved data and production student route conditions; not a signed-in student session', passages: [] };
for (const plan of planned) {
  const hits = after.filter((p) => p.slug === (plan.existing?.slug ?? plan.row.slug));
  if (hits.length !== 1 || hits[0].owner_id !== studentId || hits[0].title !== plan.row.title || digest(hits[0].body) !== digest(plan.row.body) || !hits[0].is_published) throw new Error(`Readback failed: ${plan.row.title}`);
  const saved = hits[0];
  const stillOriginal = await request(`rest/v1/reading_center_passages?id=eq.${plan.original.id}&select=*`);
  if (JSON.stringify(stillOriginal[0]) !== JSON.stringify(plan.original)) throw new Error('Original changed during copy; investigate before any retry');
  receipt.passages.push({ id: saved.id, title: saved.title, word_count: saved.word_count, body_sha256: digest(saved.body),
    owner_id: saved.owner_id, is_published: saved.is_published, source_passage_id: plan.original.id,
    url: `https://lsatprep.study/reading-center/read/${saved.slug}`, full_text_matches_original: true, original_unchanged: true });
}
if (receiptPath) fs.writeFileSync(path.resolve(receiptPath), JSON.stringify(receipt, null, 2) + '\n', 'utf8');
console.log(JSON.stringify(receipt, null, 2));
