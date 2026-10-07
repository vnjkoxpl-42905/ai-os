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
  const section = /^PT(\d+)\.S(\d+)@(\d{4}-\d{2}-\d{2})$/.exec(file);
  if (section) {
    const [, pt, number, day] = section;
    const title = `PT${pt}.S${number} (LR)`;
    const sets = await read(`rest/v1/homework_sets?title=eq.${encodeURIComponent(title)}&select=id,title,question_qids,estimated_minutes`);
    if (sets.length !== 1) throw new Error('Expected one section set');
    const set = sets[0];
    const raw = JSON.parse(fs.readFileSync(projectPath('lsatu', `public/data/PT${pt}-S${number}-LR.json`), 'utf8'));
    const expected = raw.filter(q => q.practiceTest === `PT${pt}` && q.sectionNumber === Number(number)).sort((a, b) => a.questionNumber - b.questionNumber).map(q => `PT${pt}-S${number}-Q${q.questionNumber}`);
    if (!isDeepStrictEqual(set.question_qids, expected) || set.estimated_minutes !== 35) throw new Error('Section content or timing differs');
    const rows = await read(`rest/v1/homework_assignments?student_id=eq.${student.class_id}&set_id=eq.${set.id}&select=id,status,question_qids`);
    if (rows.length !== 1 || !isDeepStrictEqual(rows[0].question_qids, expected)) throw new Error('Section assignment differs');
    const items = await read(`rest/v1/classroom_items?source_id=eq.${rows[0].id}&student_id=eq.${student.class_id}&select=id,visible_to_student,status,unlock_at,due_at`);
    if (items.length !== 1 || !items[0].visible_to_student || items[0].status === 'archived') throw new Error('Section visibility failed');
    if (new Date(items[0].unlock_at).toISOString() !== new Date(`${day}T00:00:00`).toISOString() || new Date(items[0].due_at).toISOString() !== new Date(`${day}T23:59:59`).toISOString()) throw new Error('Section dates differ');
    console.log(JSON.stringify({ day, title, assignment_id: rows[0].id, classroom_item_id: items[0].id, visible: true, exact_content: true, count: expected.length, minutes: 35 }));
    continue;
  }
  const spec = JSON.parse(fs.readFileSync(path.resolve(file), 'utf8'));
  const drills = await read(`rest/v1/guided_drills?slug=eq.${encodeURIComponent(spec.slug)}&select=*`);
  if (drills.length !== 1) throw new Error('Expected one drill: ' + spec.slug);
  const drill = drills[0];
  for (const key of Object.keys(spec)) {
    if (!isDeepStrictEqual(drill[key], spec[key])) throw new Error('Saved content differs: ' + key);
  }
  for (const qid of spec.question_qids) {
    const match = /^PT(\d+)-S(\d+)-Q(\d+)$/.exec(qid);
    if (!match) throw new Error('Invalid question ID');
    const response = await fetch(`https://lsatprep.study/data/PT${match[1]}-S${match[2]}-LR.json`);
    if (!response.ok) throw new Error('Live question file failed');
    const rows = await response.json();
    const q = rows.find(q => q.questionNumber === Number(match[3]));
    if (!q || String(q.questionType).toLowerCase() !== 'must be true' || !(q.reasoningType || []).includes('Conditional Reasoning') || q.questionDifficulty < spec.difficulty_min || q.questionDifficulty > spec.difficulty_max || !q.stimulus || Object.keys(q.answerChoices || {}).length !== 5) throw new Error('Deployed question differs: ' + qid);
  }
  const assignments = await read(`rest/v1/guided_drill_assignments?guided_drill_id=eq.${drill.id}&student_id=eq.${student.class_id}&select=id,status,scheduled_for,unlock_at`);
  if (assignments.length !== 1) throw new Error('Expected exactly one assignment: ' + spec.slug);
  const assignment = assignments[0];
  const day = /\d{4}-\d{2}-\d{2}$/.exec(spec.slug)?.[0];
  if (assignment.scheduled_for !== day) throw new Error('Scheduled date differs');
  const items = await read(`rest/v1/classroom_items?source_id=eq.${assignment.id}&student_id=eq.${student.class_id}&select=id,title,status,visible_to_student,due_at,unlock_at,metadata_json`);
  if (items.length !== 1 || !items[0].visible_to_student || items[0].status === 'archived') throw new Error('Classroom visibility failed');
  const item = items[0];
  const expectedDue = new Date(`${day}T23:59:59`).toISOString();
  const expectedUnlock = new Date(`${day}T00:00:00`).toISOString();
  if (new Date(assignment.unlock_at).toISOString() !== expectedUnlock) throw new Error('Assignment unlock differs');
  if (new Date(item.due_at).toISOString() !== expectedDue || new Date(item.unlock_at).toISOString() !== expectedUnlock) throw new Error('Local calendar dates differ');
  const notices = await read(`rest/v1/notifications?user_id=eq.${student.class_id}&type=eq.assignment&select=id,title,link,read&order=created_at.desc&limit=100`);
  const matchingNotices = notices.filter(notice => notice.link === item.metadata_json.assigned_route);
  if (matchingNotices.length !== 1) throw new Error('Expected one bell notification');
  console.log(JSON.stringify({ day, title: item.title, assignment_id: assignment.id, classroom_item_id: item.id, status: assignment.status, visible: true, due_at: item.due_at, unlock_at: item.unlock_at, count: spec.question_qids.length, difficulty: [spec.difficulty_min, spec.difficulty_max], exact_content: true, bell_count: 1, bell_unread: !matchingNotices[0].read }));
}
