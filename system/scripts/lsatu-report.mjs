#!/usr/bin/env node
// Read-only LSAT U reports, headless. Signs in as the admin account from the
// root .env (same path as projects/lsatu/scripts/assign.ts) and reads through
// PostgREST under normal admin RLS. Never writes.
//
//   node system/scripts/lsatu-report.mjs status  "Celia"
//   node system/scripts/lsatu-report.mjs qtypes  "Celia" [--days 30]
//   node system/scripts/lsatu-report.mjs sections "Celia" [--limit 10]
//   node system/scripts/lsatu-report.mjs overdue
//   node system/scripts/lsatu-report.mjs quiet   [--days 7]
//   node system/scripts/lsatu-report.mjs students
//   node system/scripts/lsatu-report.mjs inbox   [--days 7]
//   node system/scripts/lsatu-report.mjs thread  "Celia" [--limit 20]
//
// Add --json to any command for machine-readable output.
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
const env = { ...readEnv(path.join(ROOT, "projects/lsatu/.env")), ...readEnv(path.join(ROOT, ".env")) };
const URL_ = env.VITE_SUPABASE_URL;
const KEY = env.VITE_SUPABASE_PUBLISHABLE_KEY;

const argv = process.argv.slice(2);
const cmd = argv[0];
const flag = (n, d) => { const i = argv.indexOf(`--${n}`); return i >= 0 ? argv[i + 1] : d; };
const asJson = argv.includes("--json");
const who = argv[1] && !argv[1].startsWith("--") ? argv[1] : undefined;

if (!cmd || !["status", "qtypes", "sections", "overdue", "quiet", "students", "inbox", "thread"].includes(cmd)) {
  console.error("usage: lsatu-report.mjs (status|qtypes|sections|thread) <student> | inbox [--days N] | overdue | quiet [--days N] | students  [--json]");
  process.exit(2);
}
if (!URL_ || !KEY) { console.error("lsatu-report: VITE_SUPABASE_URL / _PUBLISHABLE_KEY not found in projects/lsatu/.env"); process.exit(2); }
if (!env.LSATPREP_ADMIN_EMAIL || !env.LSATPREP_ADMIN_PASSWORD) { console.error("lsatu-report: LSATPREP_ADMIN_* missing from root .env"); process.exit(2); }

const tok = await (await fetch(`${URL_}/auth/v1/token?grant_type=password`, {
  method: "POST",
  headers: { apikey: KEY, "content-type": "application/json" },
  body: JSON.stringify({ email: env.LSATPREP_ADMIN_EMAIL, password: env.LSATPREP_ADMIN_PASSWORD }),
})).json();
if (!tok.access_token) { console.error(`lsatu-report: sign-in failed: ${tok.error_description ?? tok.msg ?? "unknown"}`); process.exit(1); }
const ADMIN_ID = JSON.parse(Buffer.from(tok.access_token.split(".")[1], "base64url")).sub;
const H = { apikey: KEY, authorization: `Bearer ${tok.access_token}` };

async function rest(q) {
  const r = await fetch(`${URL_}/rest/v1/${q}`, { headers: H });
  const j = await r.json();
  if (!r.ok) throw new Error(`${q.split("?")[0]}: ${j.message ?? r.status}`);
  return j;
}
async function users() {
  const r = await fetch(`${URL_}/functions/v1/admin-manage-users`, { headers: H });
  if (!r.ok) throw new Error(`admin-manage-users: ${r.status}`);
  return r.json();
}
const nameOf = (u) => u.display_name || u.email || u.class_id;
const day = (s) => (s ? String(s).slice(0, 10) : "-");
const oneLine = (s, n = 140) => { const t = String(s ?? "").replace(/<[^>]+>/g, " ").replace(/\s+/g, " ").trim(); return t.length > n ? t.slice(0, n - 1) + "…" : t; };
const pct = (n, d) => (d ? `${Math.round((100 * n) / d)}%` : "-");

async function resolve(q) {
  if (!q) { console.error("lsatu-report: name a student"); process.exit(2); }
  const all = await users();
  const needle = q.toLowerCase();
  const exact = all.filter((u) => [u.email, u.display_name].some((v) => v && v.toLowerCase() === needle));
  const hits = exact.length ? exact : all.filter((u) => [u.email, u.display_name].some((v) => v && v.toLowerCase().includes(needle)));
  if (hits.length === 1) return hits[0];
  console.error(hits.length ? `"${q}" is ambiguous:\n${hits.map((u) => `  ${nameOf(u)} <${u.email}>`).join("\n")}` : `no account matches "${q}"`);
  process.exit(1);
}
const out = (data, text) => console.log(asJson ? JSON.stringify(data, null, 2) : text());

if (cmd === "students") {
  const all = await users();
  out(all.map((u) => ({ name: nameOf(u), email: u.email, last_seen: u.last_seen_at ?? null })), () =>
    all.map((u) => `${nameOf(u).padEnd(28)} ${String(u.email).padEnd(36)} seen ${day(u.last_seen_at)}`).join("\n"));
} else if (cmd === "status") {
  const u = await resolve(who);
  const id = u.class_id;
  const [items, prof, secs] = await Promise.all([
    rest(`classroom_items?student_id=eq.${id}&select=type,title,status,unlock_at,due_at,completed_at,created_at&order=created_at.desc&limit=25`),
    rest(`profiles?class_id=eq.${id}&select=overall_answered,overall_correct,last_seen_at,last_practice_date,streak_current`),
    rest(`section_history?class_id=eq.${id}&select=pt,section,initial_score,initial_total,br_score,br_total,completed_at,mode&order=completed_at.desc&limit=5`),
  ]);
  const p = prof[0] ?? {};
  const open = items.filter((i) => i.status !== "completed");
  const now = new Date().toISOString();
  out({ student: nameOf(u), email: u.email, profile: p, open, recent_sections: secs }, () => [
    `${nameOf(u)} <${u.email}>`,
    `  last seen ${day(p.last_seen_at)} · last practice ${day(p.last_practice_date)}`,
    `\nOpen work (${open.length}):`,
    ...(open.length ? open.map((i) => `  ${i.due_at && i.due_at < now ? "OVERDUE " : ""}[${i.type}] ${i.title} · ${i.status} · assigned ${day(i.created_at)}${i.due_at ? ` · due ${day(i.due_at)}` : ""}`) : ["  none"]),
    `\nRecent sections:`,
    ...(secs.length ? secs.map((s) => `  PT${s.pt}.S${s.section} ${day(s.completed_at)}: ${s.initial_score}/${s.initial_total ?? "?"}${s.br_score != null ? ` · BR ${s.br_score}/${s.br_total ?? "?"}` : ""} (${s.mode ?? "-"})`) : ["  none"]),
  ].join("\n"));
} else if (cmd === "qtypes") {
  const u = await resolve(who);
  const days = Number(flag("days", 30));
  const since = new Date(Date.now() - days * 864e5).toISOString();
  const rows = await rest(`attempts?class_id=eq.${u.class_id}&timestamp_iso=gte.${since}&select=qtype,correct,time_ms&limit=10000`);
  const by = {};
  for (const r of rows) { const k = r.qtype || "(untyped)"; (by[k] ??= { n: 0, c: 0, ms: 0 }); by[k].n++; by[k].c += r.correct ? 1 : 0; by[k].ms += r.time_ms || 0; }
  const list = Object.entries(by).map(([qtype, v]) => ({ qtype, answered: v.n, correct: v.c, accuracy: v.n ? v.c / v.n : 0, avg_sec: v.n ? Math.round(v.ms / v.n / 1000) : 0 })).sort((a, b) => a.accuracy - b.accuracy);
  out({ student: nameOf(u), days, total: rows.length, by_qtype: list }, () => [
    `${nameOf(u)}: ${rows.length} questions in the last ${days} days, weakest first`,
    ...list.map((l) => `  ${l.qtype.padEnd(34)} ${String(l.correct).padStart(3)}/${String(l.answered).padEnd(4)} ${pct(l.correct, l.answered).padStart(4)}${l.avg_sec ? `  ${l.avg_sec}s avg` : ""}`),
  ].join("\n"));
} else if (cmd === "sections") {
  const u = await resolve(who);
  const secs = await rest(`section_history?class_id=eq.${u.class_id}&select=pt,section,initial_score,initial_total,br_score,br_total,avg_time_ms,unanswered_count,completed_at,mode&order=completed_at.desc&limit=${Number(flag("limit", 10))}`);
  out({ student: nameOf(u), sections: secs }, () => [
    `${nameOf(u)}: last ${secs.length} sections`,
    ...secs.map((s) => `  ${day(s.completed_at)} PT${s.pt}.S${s.section}  ${s.initial_score}/${s.initial_total ?? "?"}${s.br_score != null ? `  BR ${s.br_score}/${s.br_total ?? "?"}` : ""}  ${s.avg_time_ms ? Math.round(s.avg_time_ms / 1000) + "s/q" : ""}  ${s.unanswered_count ? s.unanswered_count + " blank" : ""}  (${s.mode ?? "-"})`),
  ].join("\n"));
} else if (cmd === "overdue") {
  const now = new Date().toISOString();
  const [items, all] = await Promise.all([
    rest(`classroom_items?due_at=lt.${now}&status=neq.completed&visible_to_student=eq.true&select=student_id,type,title,status,due_at&order=due_at.asc&limit=500`),
    users(),
  ]);
  const names = Object.fromEntries(all.map((u) => [u.class_id, nameOf(u)]));
  out(items.map((i) => ({ ...i, student: names[i.student_id] ?? i.student_id })), () =>
    items.length ? items.map((i) => `${(names[i.student_id] ?? i.student_id).padEnd(24)} due ${day(i.due_at)}  [${i.type}] ${i.title} · ${i.status}`).join("\n") : "Nothing overdue.");
} else if (cmd === "inbox") {
  // Messages students sent, newest first. Excludes everything the admin sent.
  const days = Number(flag("days", 7));
  const since = new Date(Date.now() - days * 864e5).toISOString();
  const [msgs, all] = await Promise.all([
    rest(`messages?created_at=gte.${since}&sender_id=neq.${ADMIN_ID}&select=conversation_id,sender_id,body,created_at&order=created_at.desc&limit=200`),
    users(),
  ]);
  const names = Object.fromEntries(all.map((u) => [u.class_id, nameOf(u)]));
  out(msgs.map((m) => ({ ...m, student: names[m.sender_id] ?? m.sender_id })), () =>
    msgs.length ? msgs.map((m) => `${day(m.created_at)} ${String(m.created_at).slice(11, 16)}  ${(names[m.sender_id] ?? m.sender_id).padEnd(22)} ${oneLine(m.body)}`).join("\n") : `No student messages in the last ${days} days.`);
} else if (cmd === "thread") {
  // Every message between the admin and one student, oldest first.
  const u = await resolve(who);
  const parts = await rest(`conversation_participants?user_id=eq.${u.class_id}&select=conversation_id`);
  const ids = [...new Set(parts.map((p) => p.conversation_id))];
  const msgs = ids.length
    ? await rest(`messages?conversation_id=in.(${ids.join(",")})&select=id,sender_id,body,created_at&order=created_at.desc&limit=${Number(flag("limit", 20))}`)
    : [];
  msgs.reverse();
  out({ student: nameOf(u), messages: msgs }, () =>
    msgs.length ? msgs.map((m) => `${argv.includes("--ids") ? m.id + "  " : ""}${day(m.created_at)} ${String(m.created_at).slice(11, 16)}  ${m.sender_id === ADMIN_ID ? "You" : nameOf(u)}: ${oneLine(m.body, 300)}`).join("\n") : `No messages with ${nameOf(u)}.`);
} else if (cmd === "quiet") {
  const days = Number(flag("days", 7));
  const cutoff = new Date(Date.now() - days * 864e5).toISOString();
  const [open, all, profs] = await Promise.all([
    rest(`classroom_items?status=neq.completed&visible_to_student=eq.true&select=student_id&limit=2000`),
    users(),
    rest(`profiles?select=class_id,last_seen_at,last_practice_date`),
  ]);
  const withWork = new Set(open.map((i) => i.student_id));
  const pmap = Object.fromEntries(profs.map((p) => [p.class_id, p]));
  const quiet = all.filter((u) => withWork.has(u.class_id)).map((u) => ({ name: nameOf(u), email: u.email, last_seen: pmap[u.class_id]?.last_seen_at ?? null }))
    .filter((u) => !u.last_seen || u.last_seen < cutoff).sort((a, b) => String(a.last_seen).localeCompare(String(b.last_seen)));
  out(quiet, () => quiet.length ? `Students with open work, not seen in ${days}+ days:\n` + quiet.map((q) => `  ${q.name.padEnd(28)} last seen ${day(q.last_seen)}`).join("\n") : `Everyone with open work was seen in the last ${days} days.`);
}
