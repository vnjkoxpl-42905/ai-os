// Notify one existing Reading Center assignment through the app's own helper.
// No assignment writes. Dry-run first; never replay after a partial send.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { projectPath } from './project-paths.mjs';
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const app = projectPath('lsatu');
const apply = process.argv.includes('--apply');
const studentId = '749e2eae-7969-464f-bf96-a4d4cfafe2bf';
const email = 'celiacutler@gmail.com';
const route = '/reading-center';
const title = 'Reading Center';
const description = 'Open Reading Center in your sidebar, below My Work. Your three passages are ready under Added By Me: 1. Plants and Geological Time; 2. Work and Quiet Desperation; 3. Ion and Poetic Inspiration.';
const receipt = path.join(root, 'students/celia-cutler/reading-center-notification-2026-10-15.json');
const lock = receipt + '.lock';
const { createServer } = await import(pathToFileURL(path.join(app, 'node_modules/vite/dist/node/index.js')).href);
const server = await createServer({ root: app, configFile: false, appType: 'custom',
  resolve: { alias: { '@': path.join(app, 'src') } }, server: { middlewareMode: true, watch: null } });
let locked = false;
let client;
try {
  const { supabase } = await server.ssrLoadModule('/src/integrations/supabase/client.ts');
  client = supabase;
  const env = Object.fromEntries(fs.readFileSync(path.join(root, '.env'), 'utf8').split(/\r?\n/)
    .map((s) => /^\s*([^#=\s]+)\s*=\s*(.*?)\s*$/.exec(s)).filter(Boolean)
    .map((m) => [m[1], m[2].replace(/^["']|["']$/g, '')]));
  const { data: auth, error } = await supabase.auth.signInWithPassword({ email: env.LSATPREP_ADMIN_EMAIL, password: env.LSATPREP_ADMIN_PASSWORD });
  if (error || !auth.user) throw new Error('Admin login failed');
  const adminId = auth.user.id;
  const checked = async (query) => { const r = await query; if (r.error) throw r.error; return r.data; };
  const users = await checked(supabase.functions.invoke('admin-manage-users', { method: 'GET' }));
  const exact = users.filter((u) => u.email?.toLowerCase() === email);
  if (exact.length !== 1 || exact[0].class_id !== studentId) throw new Error('Celia identity mismatch');
  const getItems = () => checked(supabase.from('classroom_items').select('id,status,unlock_at,visible_to_student').eq('student_id', studentId).eq('source_table', 'reading_center').eq('source_id', 'library').eq('visible_to_student', true).in('status', ['assigned','in_progress','completed']));
  const items = await getItems();
  if (items.length !== 1 || (items[0].unlock_at && Date.parse(items[0].unlock_at) > Date.now())) throw new Error('Exactly one active immediate assignment is required');
  const bells = await checked(supabase.from('notifications').select('id,title,body,link,read,created_at').eq('user_id',studentId).eq('type','assignment').eq('link',route));
  const studentParts = await checked(supabase.from('conversation_participants').select('conversation_id').eq('user_id', studentId));
  const myParts = await checked(supabase.from('conversation_participants').select('conversation_id').eq('user_id', adminId));
  const conversations = studentParts.filter((p) => myParts.some((m) => m.conversation_id === p.conversation_id)).map((p) => p.conversation_id);
  const priorMessages = conversations.length ? await checked(supabase.from('messages').select('id,body,created_at').in('conversation_id', conversations).eq('sender_id',adminId).ilike('body','%Reading Center%')) : [];
  console.log(JSON.stringify({ dry_run: !apply, student: email, assignment: items[0], prior_notifications: bells, prior_reading_center_messages: priorMessages, planned_description: description, route },null,2));
  if (apply) {
    if (bells.length || priorMessages.length || fs.existsSync(receipt)) throw new Error('Prior Reading Center notification, message, or send receipt exists; inspect rather than resend');
    fs.mkdirSync(lock); locked = true;
    // Persist intent before sending: ambiguous/partial outcomes require inspection, never replay.
    fs.writeFileSync(receipt, JSON.stringify({ status:'sending', started_at:new Date().toISOString(), student_id:studentId, title, description, route },null,2)+'\n','utf8');
    const { notifyStudentOfClassroomItem } = await server.ssrLoadModule('/src/lib/classroomNotify.ts');
    const result = await notifyStudentOfClassroomItem({ adminUserId:adminId,studentId,title,description,route,assignmentType:'reading practice' });
    const afterItems = await getItems();
    const afterBells = await checked(supabase.from('notifications').select('id,title,body,link,read,created_at').eq('user_id',studentId).eq('type','assignment').eq('link',route).eq('body',description));
    const afterMessages = conversations.length ? await checked(supabase.from('messages').select('id,body,created_at').in('conversation_id',conversations).eq('sender_id',adminId).ilike('body','%'+description+'%')) : [];
    const output = { status:'completed', verified_at:new Date().toISOString(), student_email:email,student_id:studentId,assignment_id:items[0].id,
      assignment_unchanged:afterItems.length===1 && afterItems[0].id===items[0].id,description,route,result,notifications:afterBells,messages:afterMessages,
      verification: { exactly_one_bell:afterBells.length===1, exactly_one_inbox_message:afterMessages.length===1, email_provider_accepted:result.email_ok } };
    fs.writeFileSync(receipt,JSON.stringify(output,null,2)+'\n','utf8');
    console.log(JSON.stringify(output,null,2));
    if (!output.assignment_unchanged || !output.verification.exactly_one_bell || !output.verification.exactly_one_inbox_message) throw new Error('Notification readback incomplete; inspect receipt, do not replay');
  }
} finally {
  if (client) await client.auth.signOut({ scope: 'local' });
  await server.close();
  if (locked) fs.rmdirSync(lock);
}
