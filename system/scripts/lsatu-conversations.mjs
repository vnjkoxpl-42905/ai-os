#!/usr/bin/env node
// Read-only. One row per LSAT U conversation, newest activity first, with who
// spoke last. Feeds the "LSAT U messages" sidebar mod (the Claude desktop pane).
// Signs in exactly as lsatu-report.mjs does; never writes.
//
//   node system/scripts/lsatu-conversations.mjs [--days 30] [--recent 6]
//
// Output: JSON array of
//   { conversation_id, student, email, last_at, last_from: "student"|"you"|"system",
//     awaiting: boolean, waiting_count, recent: [{ from, at, body }] }
// `awaiting` is true when the student spoke after your last human reply.
// Automatic "New assignment / New note" posts are `system` and never count as a reply.
// `waiting_count` is how many student messages sit after your last reply.
import { projectPath } from './project-paths.mjs';
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
function readEnv(f) {
  if (!fs.existsSync(f)) return {};
  const out = {};
  for (const line of fs.readFileSync(f, "utf8").split(/\r?\n/)) {
    const t = line.trim();
    if (!t || t.startsWith("#") || !t.includes("=")) continue;
    const i = t.indexOf("=");
    out[t.slice(0, i).trim()] = t.slice(i + 1).trim().replace(/^["']|["']$/g, "");
  }
  return out;
}
const env = { ...readEnv(projectPath('lsatu', '.env')), ...readEnv(path.join(ROOT, ".env")) };
const URL_ = env.VITE_SUPABASE_URL;
const KEY = env.VITE_SUPABASE_PUBLISHABLE_KEY;
const argv = process.argv.slice(2);
const flag = (n, d) => { const i = argv.indexOf(`--${n}`); return i >= 0 ? argv[i + 1] : d; };
const days = Number(flag("days", 30));
const recentN = Number(flag("recent", 6));

if (!URL_ || !KEY) { console.error("lsatu-conversations: VITE_SUPABASE_URL / _PUBLISHABLE_KEY not found"); process.exit(2); }
if (!env.LSATPREP_ADMIN_EMAIL || !env.LSATPREP_ADMIN_PASSWORD) { console.error("lsatu-conversations: LSATPREP_ADMIN_* missing from root .env"); process.exit(2); }

const tok = await (await fetch(`${URL_}/auth/v1/token?grant_type=password`, {
  method: "POST",
  headers: { apikey: KEY, "content-type": "application/json" },
  body: JSON.stringify({ email: env.LSATPREP_ADMIN_EMAIL, password: env.LSATPREP_ADMIN_PASSWORD }),
})).json();
if (!tok.access_token) { console.error(`lsatu-conversations: sign-in failed: ${tok.error_description ?? tok.msg ?? "unknown"}`); process.exit(1); }
const ADMIN_ID = JSON.parse(Buffer.from(tok.access_token.split(".")[1], "base64url")).sub;
const H = { apikey: KEY, authorization: `Bearer ${tok.access_token}` };

async function rest(q) {
  const r = await fetch(`${URL_}/rest/v1/${q}`, { headers: H });
  const j = await r.json();
  if (!r.ok) throw new Error(`${q.split("?")[0]}: ${j.message ?? r.status}`);
  return j;
}
const nameOf = (u) => u.display_name || u.email || u.class_id;
const clean = (s) => String(s ?? "").replace(/<[^>]+>/g, " ").replace(/[ \t]+/g, " ").replace(/\s*\n\s*/g, "\n").trim();

const since = new Date(Date.now() - days * 864e5).toISOString();
const [msgs, usersRes] = await Promise.all([
  rest(`messages?created_at=gte.${since}&select=conversation_id,sender_id,body,created_at&order=created_at.desc&limit=1500`),
  fetch(`${URL_}/functions/v1/admin-manage-users`, { headers: H }),
]);
if (!usersRes.ok) throw new Error(`admin-manage-users: ${usersRes.status}`);
const users = await usersRes.json();
const byId = Object.fromEntries(users.map((u) => [u.class_id, u]));

const convIds = [...new Set(msgs.map((m) => m.conversation_id))];
const parts = convIds.length
  ? await rest(`conversation_participants?conversation_id=in.(${convIds.join(",")})&select=conversation_id,user_id`)
  : [];
const studentOf = {};
for (const p of parts) if (p.user_id !== ADMIN_ID && byId[p.user_id]) studentOf[p.conversation_id] = byId[p.user_id];
// Fallback: a conversation with no readable participant row takes the sender of a student message.
for (const m of msgs) if (!studentOf[m.conversation_id] && m.sender_id !== ADMIN_ID && byId[m.sender_id]) studentOf[m.conversation_id] = byId[m.sender_id];

const grouped = {};
for (const m of msgs) (grouped[m.conversation_id] ||= []).push(m); // already newest first

// Posts the platform makes on your behalf (assignment and note notices) are not replies.
const isSystem = (m) => m.sender_id === ADMIN_ID && /^\s*(New (assignment|note|guided drill|activity|homework)|Reminder:)/i.test(clean(m.body));
const fromOf = (m) => (m.sender_id !== ADMIN_ID ? "student" : isSystem(m) ? "system" : "you");

const rows = convIds.map((id) => {
  const list = grouped[id];
  const u = studentOf[id];
  const human = list.filter((m) => fromOf(m) !== "system"); // newest first
  let waiting = 0;
  for (const m of human) { if (fromOf(m) === "you") break; waiting++; }
  const newest = list[0];
  const lastHuman = human[0];
  return {
    conversation_id: id,
    student: u ? nameOf(u) : "Unknown student",
    email: u?.email ?? null,
    last_at: newest.created_at,
    last_from: lastHuman ? fromOf(lastHuman) : "system",
    awaiting: waiting > 0,
    waiting_count: waiting,
    last_student_at: list.find((m) => m.sender_id !== ADMIN_ID)?.created_at ?? null,
    recent: list.slice(0, recentN).reverse().map((m) => ({
      from: fromOf(m),
      at: m.created_at,
      body: clean(m.body).slice(0, 600),
    })),
  };
}).filter((r) => r.email);

rows.sort((a, b) => (a.awaiting === b.awaiting ? String(b.last_at).localeCompare(String(a.last_at)) : a.awaiting ? -1 : 1));
console.log(JSON.stringify(rows));
