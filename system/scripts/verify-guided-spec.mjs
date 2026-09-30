import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { isDeepStrictEqual } from 'node:util';
import { projectPath } from './project-paths.mjs';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
function readEnv(file) {
  const out = {};
  for (const line of fs.readFileSync(file, 'utf8').split(/\r?\n/)) {
    const match = /^\s*([^#=\s]+)\s*=\s*(.*?)\s*$/.exec(line);
    if (match) out[match[1]] = match[2].replace(/^["']|["']$/g, '');
  }
  return out;
}
const env = { ...readEnv(projectPath('lsatu', '.env')), ...readEnv(path.join(root, '.env')) };
const base = env.VITE_SUPABASE_URL;
const key = env.VITE_SUPABASE_PUBLISHABLE_KEY;
const authResponse = await fetch(`${base}/auth/v1/token?grant_type=password`, {
  method: 'POST', headers: { apikey: key, 'content-type': 'application/json' },
  body: JSON.stringify({ email: env.LSATPREP_ADMIN_EMAIL, password: env.LSATPREP_ADMIN_PASSWORD }),
});
const auth = await authResponse.json();
if (!authResponse.ok || !auth.access_token) throw new Error('Admin sign-in failed');
const headers = { apikey: key, authorization: `Bearer ${auth.access_token}` };
async function read(route) {
  const response = await fetch(`${base}/${route}`, { headers });
  const data = await response.json();
  if (!response.ok) throw new Error(data.message || data.error || 'Read failed');
  return data;
}
const [name, ...files] = process.argv.slice(2);
if (!name || !files.length) throw new Error('Usage: node verify-guided-spec.mjs <exact student name> <spec.json> ...');
const users = await read('functions/v1/admin-manage-users');
const hits = users.filter(user => user.display_name?.toLowerCase() === name.toLowerCase());
if (hits.length !== 1) throw new Error('Student is not an exact unique match');
const student = hits[0];
if (!student.has_classroom_access || !student.has_drill_access) throw new Error('Student lacks access');
for (const file of files) {
  const spec = JSON.parse(fs.readFileSync(path.resolve(file), 'utf8'));
  const drills = await read(`rest/v1/guided_drills?slug=eq.${encodeURIComponent(spec.slug)}&select=*`);
  if (drills.length !== 1) throw new Error('Expected one drill: ' + spec.slug);
  const drill = drills[0];
  for (const key of Object.keys(spec)) {
    if (!isDeepStrictEqual(drill[key], spec[key])) throw new Error('Saved content differs: ' + key);
  }
  const assignments = await read(`rest/v1/guided_drill_assignments?guided_drill_id=eq.${drill.id}&student_id=eq.${student.class_id}&select=id,status,scheduled_for,unlock_at`);
  if (assignments.length !== 1) throw new Error('Expected exactly one assignment: ' + spec.slug);
  const assignment = assignments[0];
  const day = /\d{4}-\d{2}-\d{2}$/.exec(spec.slug)?.[0];
  if (assignment.scheduled_for !== day) throw new Error('Scheduled date differs');
  const items = await read(`rest/v1/classroom_items?source_id=eq.${assignment.id}&student_id=eq.${student.class_id}&select=id,title,status,visible_to_student,due_at,unlock_at,metadata`);
  if (items.length !== 1 || !items[0].visible_to_student || items[0].status === 'archived') throw new Error('Classroom visibility failed');
  const item = items[0];
  const expectedDue = new Date(`${day}T23:59:59`).toISOString();
  const expectedUnlock = new Date(`${day}T00:00:00`).toISOString();
  if (new Date(item.due_at).toISOString() !== expectedDue || new Date(item.unlock_at).toISOString() !== expectedUnlock) throw new Error('Local calendar dates differ');
  const notices = await read(`rest/v1/notifications?user_id=eq.${student.class_id}&type=eq.assignment&select=id,title,link,is_read&order=created_at.desc&limit=100`);
  const matchingNotices = notices.filter(notice => notice.link === item.metadata.assigned_route);
  if (matchingNotices.length !== 1) throw new Error('Expected one bell notification');
  console.log(JSON.stringify({ day, title: item.title, assignment_id: assignment.id, classroom_item_id: item.id, status: assignment.status, visible: true, due_at: item.due_at, unlock_at: item.unlock_at, count: spec.question_qids.length, difficulty: [spec.difficulty_min, spec.difficulty_max], exact_content: true, bell_count: 1, bell_unread: !matchingNotices[0].is_read }));
}
