#!/usr/bin/env node
// LSAT U account and Classroom admin, headless. Same admin login and the same
// edge functions the admin dashboard calls, so every rule the UI enforces
// (admin-account guards, flag whitelist, RLS) still applies. No Lovable.
//
//   signups [--days 30]                      new signups, with their access state
//   access  "Name"                           show every access flag
//   access  "Name" --template standard       trial | standard | full (what the dashboard applies)
//   access  "Name" --grant drill,activity    turn flags on  (short names or has_*_access)
//   access  "Name" --revoke chat             turn flags off
//   access  "Name" --all-off                 shut every door
//   archive "Name" [--reason "..."]  |  unarchive "Name"
//   items   "Name" [--all]                   Classroom items with ids (for due / unassign)
//   due     <item-id> YYYY-MM-DD             move a due date (end of that local day)
//   unassign <item-id>                       hide an item from her Classroom (archived, not deleted)
//   passes  ["Name"]                         booking passes: credits used / total, status
//   notifications [--all]                    your unread admin notifications
//   read    "Name"                           mark your thread with her as read
//
// Every write prints what it changed. --dry-run on any write shows the change and stops.
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
const pos = argv[1] && !argv[1].startsWith("--") ? argv[1] : undefined;
const pos2 = argv[2] && !argv[2].startsWith("--") ? argv[2] : undefined;
const flag = (n, d) => { const i = argv.indexOf(`--${n}`); return i >= 0 ? argv[i + 1] : d; };
const has = (n) => argv.includes(`--${n}`);
const dry = has("dry-run");
const CMDS = ["signups", "access", "archive", "unarchive", "items", "due", "unassign", "passes", "credit", "notifications", "read", "drafts", "draft", "draft-set", "uploads", "upload-review", "notes", "note-resolve", "note-discard", "scan-notes", "plans", "unsend", "unsend-last"];
if (!CMDS.includes(cmd)) { console.error(fs.readFileSync(fileURLToPath(import.meta.url), "utf8").split("\n").slice(5, 20).join("\n")); process.exit(2); }

const tok = await (await fetch(`${URL_}/auth/v1/token?grant_type=password`, {
  method: "POST",
  headers: { apikey: KEY, "content-type": "application/json" },
  body: JSON.stringify({ email: env.LSATPREP_ADMIN_EMAIL, password: env.LSATPREP_ADMIN_PASSWORD }),
})).json();
if (!tok.access_token) { console.error(`lsatu-admin: sign-in failed: ${tok.error_description ?? tok.msg ?? "unknown"}`); process.exit(1); }
const ADMIN_ID = JSON.parse(Buffer.from(tok.access_token.split(".")[1], "base64url")).sub;
const H = { apikey: KEY, authorization: `Bearer ${tok.access_token}` };

async function rest(q, init = {}) {
  const r = await fetch(`${URL_}/rest/v1/${q}`, { ...init, headers: { ...H, "content-type": "application/json", prefer: "return=representation", ...(init.headers ?? {}) } });
  const txt = await r.text();
  const j = txt ? JSON.parse(txt) : null;
  if (!r.ok) throw new Error(`${q.split("?")[0]}: ${j?.message ?? r.status}`);
  return j;
}
async function fn(name, body, method = "POST") {
  const r = await fetch(`${URL_}/functions/v1/${name}`, { method, headers: { ...H, "content-type": "application/json" }, body: body ? JSON.stringify(body) : undefined });
  const j = await r.json().catch(() => ({}));
  if (!r.ok || j.error) throw new Error(`${name}: ${j.error ?? r.status}`);
  return j;
}
const users = () => fn("admin-manage-users", undefined, "GET");
const nameOf = (u) => u.display_name || u.email || u.class_id;
const day = (s) => (s ? String(s).slice(0, 10) : "-");
async function resolve(q) {
  if (!q) { console.error("lsatu-admin: name a student"); process.exit(2); }
  const all = await users();
  const needle = q.toLowerCase();
  const exact = all.filter((u) => [u.email, u.display_name].some((v) => v && v.toLowerCase() === needle));
  const hits = exact.length ? exact : all.filter((u) => [u.email, u.display_name].some((v) => v && v.toLowerCase().includes(needle)));
  if (hits.length === 1) return hits[0];
  console.error(hits.length ? `"${q}" is ambiguous:\n${hits.map((u) => `  ${nameOf(u)} <${u.email}>`).join("\n")}` : `no account matches "${q}"`);
  process.exit(1);
}

// Flags, mirrored from src/lib/adminUsers.ts. The edge function rejects anything else.
const FLAGS = ["has_practice_access", "has_drill_access", "has_classroom_access", "has_bootcamp_access", "has_analytics_access", "has_schedule_access",
  "has_waj_access", "has_journal_access", "has_flagged_access", "has_chat_access", "has_export_access", "has_ta_access", "has_activity_access"];
const DEFAULT_ON = FLAGS.filter((f) => !["has_practice_access", "has_drill_access"].includes(f));
const tmpl = (on) => Object.fromEntries(FLAGS.map((f) => [f, on.includes(f) || DEFAULT_ON.includes(f)]));
const TEMPLATES = {
  trial: tmpl(["has_practice_access", "has_drill_access"]),
  standard: tmpl(["has_practice_access", "has_drill_access", "has_classroom_access", "has_bootcamp_access"]),
  full: tmpl(FLAGS),
};
const short = (f) => f.replace(/^has_|_access$/g, "");
const toFlag = (s) => { const f = s.startsWith("has_") ? s : `has_${s}_access`; if (!FLAGS.includes(f)) { console.error(`unknown flag "${s}". Known: ${FLAGS.map(short).join(", ")}`); process.exit(2); } return f; };
const accessLine = (u) => `on: ${FLAGS.filter((f) => u[f]).map(short).join(", ") || "nothing"}\n  off: ${FLAGS.filter((f) => !u[f]).map(short).join(", ") || "nothing"}`;

if (cmd === "signups") {
  const days = Number(flag("days", 30));
  const since = new Date(Date.now() - days * 864e5).toISOString();
  const [notes, all] = await Promise.all([
    rest(`notifications?user_id=eq.${ADMIN_ID}&type=eq.signup&created_at=gte.${since}&select=id,body,read,created_at&order=created_at.desc`),
    users(),
  ]);
  if (!notes.length) { console.log(`No signups in the last ${days} days.`); process.exit(0); }
  for (const n of notes) {
    const nm = String(n.body).replace(/ just joined the platform\.?$/, "");
    const matches = all.filter((u) => nameOf(u) === nm);
    const u = matches.length === 1 ? matches[0] : null;
    const state = u ? (FLAGS.some((f) => u[f]) ? `access: ${FLAGS.filter((f) => u[f]).map(short).join(", ")}` : "NO ACCESS YET") : `${matches.length} accounts named "${nm}"`;
    console.log(`${day(n.created_at)}  ${n.read ? " " : "*"} ${nm.padEnd(24)} ${u ? `<${u.email}>`.padEnd(36) : "".padEnd(36)} ${state}`);
  }
  console.log(`\n* = unread. Give access: lsatu access "<name>" --template standard`);
} else if (cmd === "access") {
  const u = await resolve(pos);
  const t = flag("template");
  let updates = null;
  if (t) { if (!TEMPLATES[t]) { console.error(`template must be trial, standard or full`); process.exit(2); } updates = TEMPLATES[t]; }
  else if (has("all-off")) updates = Object.fromEntries(FLAGS.map((f) => [f, false]));
  else if (flag("grant") || flag("revoke")) {
    updates = {};
    for (const s of (flag("grant") ?? "").split(",").filter(Boolean)) updates[toFlag(s.trim())] = true;
    for (const s of (flag("revoke") ?? "").split(",").filter(Boolean)) updates[toFlag(s.trim())] = false;
  }
  if (!updates) { console.log(`${nameOf(u)} <${u.email}>${u.archived_at ? `  ARCHIVED ${day(u.archived_at)}` : ""}\n  ${accessLine(u)}`); process.exit(0); }
  const changes = Object.entries(updates).filter(([f, v]) => Boolean(u[f]) !== v);
  if (!changes.length) { console.log(`${nameOf(u)}: already set, nothing to change.`); process.exit(0); }
  console.log(`${nameOf(u)} <${u.email}>\n  ${changes.map(([f, v]) => `${v ? "+" : "-"}${short(f)}`).join("  ")}`);
  if (dry) { console.log("(dry run — nothing changed)"); process.exit(0); }
  await fn("admin-manage-users", { action: "apply_template", class_id: u.class_id, flags: Object.fromEntries(changes) });
  const after = (await users()).find((x) => x.class_id === u.class_id);
  console.log(`Done.\n  ${accessLine(after)}`);
} else if (cmd === "archive" || cmd === "unarchive") {
  const u = await resolve(pos);
  console.log(`${cmd} ${nameOf(u)} <${u.email}>`);
  if (dry) { console.log("(dry run — nothing changed)"); process.exit(0); }
  await fn("admin-manage-users", { action: `${cmd}_student`, class_id: u.class_id, ...(cmd === "archive" ? { reason: flag("reason", null) } : {}) });
  console.log("Done.");
} else if (cmd === "items") {
  const u = await resolve(pos);
  const rows = await rest(`classroom_items?student_id=eq.${u.class_id}${has("all") ? "" : "&status=not.in.(completed,archived)"}&select=id,type,title,status,due_at,unlock_at,created_at&order=created_at.desc&limit=100`);
  console.log(`${nameOf(u)}: ${rows.length} item(s)`);
  for (const i of rows) console.log(`  ${i.id}  [${i.type}] ${i.title} · ${i.status}${i.due_at ? ` · due ${day(i.due_at)}` : ""}${i.unlock_at ? ` · unlocks ${day(i.unlock_at)}` : ""}`);
} else if (cmd === "due" || cmd === "unassign") {
  if (!pos || !/^[0-9a-f-]{36}$/.test(pos)) { console.error(`lsatu-admin: ${cmd} needs a classroom item id (lsatu items "<name>")`); process.exit(2); }
  const [item] = await rest(`classroom_items?id=eq.${pos}&select=id,student_id,title,status,due_at`);
  if (!item) { console.error("no classroom item with that id"); process.exit(1); }
  let patch;
  if (cmd === "due") {
    if (!pos2 || !/^\d{4}-\d{2}-\d{2}$/.test(pos2)) { console.error("due date must be YYYY-MM-DD"); process.exit(2); }
    const [y, m, d] = pos2.split("-").map(Number);
    patch = { due_at: new Date(y, m - 1, d, 23, 59, 59).toISOString() }; // end of that local day, as assign.ts does
    console.log(`"${item.title}": due ${day(item.due_at)} -> ${pos2}`);
  } else {
    patch = { status: "archived", visible_to_student: false };
    console.log(`"${item.title}": hide from her Classroom (status ${item.status} -> archived; the row and her work stay)`);
  }
  if (dry) { console.log("(dry run — nothing changed)"); process.exit(0); }
  await rest(`classroom_items?id=eq.${pos}`, { method: "PATCH", body: JSON.stringify({ ...patch, updated_at: new Date().toISOString() }) });
  console.log("Done.");
} else if (cmd === "passes") {
  const { passes = [] } = await fn("booking-pass-admin", { action: "list" });
  let list = passes;
  if (pos) { const u = await resolve(pos); list = passes.filter((p) => p.student_id === u.class_id); }
  if (!list.length) { console.log(pos ? "No booking pass for that student." : "No booking passes."); process.exit(0); }
  for (const p of list) console.log(`${String(p.student_name ?? p.student_email).padEnd(22)} ${p.used_credits}/${p.total_credits} used · ${p.total_credits - p.used_credits} owed · ${p.session_length_minutes} min · ${p.status}${p.expires_at ? ` · expires ${day(p.expires_at)}` : ""}`);
  console.log(`\nNew pass or link: use the booking-link skill (scripts/booking-link.ts).`);
} else if (cmd === "credit") {
  const u = await resolve(pos);
  const { passes = [] } = await fn("booking-pass-admin", { action: "list" });
  const active = passes.filter((p) => p.student_id === u.class_id && p.status === "active");
  if (active.length !== 1) throw new Error(`Expected one active booking pass for ${nameOf(u)}; found ${active.length}. Nothing changed.`);
  const pass = active[0];
  const nextTotal = pass.total_credits + 1;
  console.log(`${nameOf(u)}: ${pass.total_credits - pass.used_credits} -> ${nextTotal - pass.used_credits} remaining credits (${pass.used_credits}/${pass.total_credits} -> ${pass.used_credits}/${nextTotal} used/total)`);
  if (dry) { console.log("(dry run — nothing changed)"); process.exit(0); }
  await fn("booking-pass-admin", { action: "update", pass_id: pass.id, total_credits: nextTotal });
  const { passes: updated = [] } = await fn("booking-pass-admin", { action: "list" });
  const actual = updated.find((p) => p.id === pass.id);
  if (!actual || actual.total_credits !== nextTotal || actual.used_credits !== pass.used_credits) throw new Error("Credit update returned, but the pass balance did not verify. Check the account before retrying.");
  console.log(`Verified: ${actual.total_credits - actual.used_credits} remaining credits.`);
} else if (cmd === "notifications") {
  const rows = await rest(`notifications?user_id=eq.${ADMIN_ID}${has("all") ? "" : "&read=eq.false"}&select=type,title,body,created_at&order=created_at.desc&limit=50`);
  if (!rows.length) console.log("No unread notifications.");
  for (const n of rows) console.log(`${day(n.created_at)}  [${n.type}] ${n.title}${n.body ? ` — ${String(n.body).replace(/\s+/g, " ").slice(0, 110)}` : ""}`);
} else if (cmd === "drafts") {
  // AI TA drafts. Default: the ones waiting on review.
  const st = flag("status", "draft");
  const [rows, all] = await Promise.all([
    rest(`ai_ta_drafts?${st === "all" ? "" : `status=eq.${st}&`}select=id,student_id,draft_type,status,draft_markdown,created_at&order=created_at.desc&limit=50`),
    users(),
  ]);
  const names = Object.fromEntries(all.map((u) => [u.class_id, nameOf(u)]));
  if (!rows.length) console.log(`No AI TA drafts with status ${st}.`);
  for (const d of rows) console.log(`${d.id}  ${day(d.created_at)}  ${(names[d.student_id] ?? "?").padEnd(18)} [${d.draft_type}] ${d.status}\n    ${String(d.draft_markdown ?? "").replace(/\s+/g, " ").slice(0, 160)}`);
} else if (cmd === "draft") {
  const [d] = await rest(`ai_ta_drafts?id=eq.${pos}&select=*`);
  if (!d) { console.error("no draft with that id"); process.exit(1); }
  if (has("json")) { const u = (await users()).find((x) => x.class_id === d.student_id); console.log(JSON.stringify({ ...d, student_email: u?.email ?? null })); process.exit(0); }
  console.log(`${d.id} · ${d.draft_type} · ${d.status}\n\n${d.draft_markdown ?? JSON.stringify(d.draft_json, null, 2)}`);
} else if (cmd === "draft-set") {
  // draft-set <id> approved|rejected|posted  (same fields useAITADrafts writes)
  if (!["approved", "rejected", "posted", "draft"].includes(pos2)) { console.error("status must be approved, rejected, posted or draft"); process.exit(2); }
  const patch = { status: pos2, updated_at: new Date().toISOString() };
  if (pos2 === "approved") Object.assign(patch, { approved_by: ADMIN_ID, approved_at: new Date().toISOString() });
  if (pos2 === "posted") patch.posted_at = new Date().toISOString();
  if (dry) { console.log(`would set draft ${pos} -> ${pos2}`); process.exit(0); }
  await rest(`ai_ta_drafts?id=eq.${pos}`, { method: "PATCH", body: JSON.stringify(patch) });
  console.log(`Draft ${pos} -> ${pos2}.`);
} else if (cmd === "uploads") {
  const [rows, all] = await Promise.all([
    rest(`external_work_uploads?${has("all") ? "" : "reviewed_at=is.null&"}select=id,student_id,file_name,source_platform,upload_type,processing_status,reviewed_at,created_at&order=created_at.desc&limit=50`),
    users(),
  ]);
  const names = Object.fromEntries(all.map((u) => [u.class_id, nameOf(u)]));
  if (!rows.length) console.log(has("all") ? "No uploads." : "No unreviewed uploads.");
  for (const r of rows) console.log(`${r.id}  ${day(r.created_at)}  ${(names[r.student_id] ?? "?").padEnd(18)} ${r.file_name} · ${r.source_platform ?? "-"}/${r.upload_type ?? "-"} · ${r.processing_status}${r.reviewed_at ? ` · reviewed ${day(r.reviewed_at)}` : ""}`);
} else if (cmd === "upload-review") {
  // upload-review <id> parsed|needs_review|failed  (what TeacherUploads writes)
  if (!["parsed", "needs_review", "failed"].includes(pos2)) { console.error("status must be parsed, needs_review or failed"); process.exit(2); }
  if (dry) { console.log(`would mark upload ${pos} ${pos2}`); process.exit(0); }
  await rest(`external_work_uploads?id=eq.${pos}`, { method: "PATCH", body: JSON.stringify({ processing_status: pos2, reviewed_at: new Date().toISOString() }) });
  console.log(`Upload ${pos} -> ${pos2}.`);
} else if (cmd === "notes") {
  // Session-note ingestion ledger. Default: rows waiting on a human.
  const rows = await rest(`session_ingestions?${has("all") ? "" : "status=in.(needs_match,error,ingested)&"}select=*&order=created_at.desc&limit=50`);
  if (!rows.length) console.log(has("all") ? "No session notes in the ledger." : "No session notes waiting on you.");
  for (const r of rows) console.log(`${r.id}  ${day(r.created_at)}  ${r.status.padEnd(11)} ${r.doc_title ?? r.title ?? r.gdrive_doc_id ?? ""}${r.error_message ? `  (${String(r.error_message).slice(0, 80)})` : ""}`);
} else if (cmd === "note-resolve" || cmd === "note-discard") {
  if (!pos) { console.error(`${cmd} needs a ledger id (lsatu notes)`); process.exit(2); }
  let body;
  if (cmd === "note-resolve") {
    const u = await resolve(pos2);
    body = { action: "resolve", ledger_id: pos, student_class_id: u.class_id };
    console.log(`file note ${pos} under ${nameOf(u)} <${u.email}>`);
  } else {
    body = { action: "discard", ledger_id: pos, discard_reason: flag("reason", "discarded_by_admin") };
    console.log(`discard note ${pos}`);
  }
  if (dry) { console.log("(dry run — nothing changed)"); process.exit(0); }
  const r = await fn("scan-session-notes", body);
  console.log(`Done. ${r.status ?? ""}${r.already_resolved ? " (already resolved)" : ""}`);
} else if (cmd === "scan-notes") {
  if (dry) { console.log("would scan Drive for new session notes"); process.exit(0); }
  console.log(JSON.stringify(await fn("scan-session-notes", { action: "scan" }), null, 2));
} else if (cmd === "plans") {
  const u = await resolve(pos);
  const plans = await rest(`weekly_plans?student_id=eq.${u.class_id}&select=id,title,week_start,week_end,status,published_at&order=week_start.desc&limit=${Number(flag("limit", 4))}`);
  if (!plans.length) { console.log(`No weekly plans for ${nameOf(u)}.`); process.exit(0); }
  const items = await rest(`weekly_plan_items?weekly_plan_id=in.(${plans.map((p) => p.id).join(",")})&select=weekly_plan_id,day_date,title,status,estimated_minutes&order=day_date.asc,sort_order.asc`);
  for (const p of plans) {
    console.log(`${p.week_start} to ${p.week_end}  ${p.title} · ${p.status}`);
    for (const i of items.filter((x) => x.weekly_plan_id === p.id)) console.log(`   ${i.day_date}  ${i.title}${i.estimated_minutes ? ` (~${i.estimated_minutes} min)` : ""} · ${i.status}`);
  }
} else if (cmd === "unsend" || cmd === "unsend-last") {
  // Delete one of YOUR messages so the student never sees it (same delete the
  // inbox UI does). Only your own messages; a student's message is never touched.
  let msg;
  if (cmd === "unsend") {
    if (!pos || !/^[0-9a-f-]{36}$/.test(pos)) { console.error("unsend needs a message id (lsatu thread \"Name\" --ids)"); process.exit(2); }
    [msg] = await rest(`messages?id=eq.${pos}&select=id,conversation_id,sender_id,body,created_at`);
  } else {
    const u = await resolve(pos);
    const hers = await rest(`conversation_participants?user_id=eq.${u.class_id}&select=conversation_id`);
    if (hers.length) [msg] = await rest(`messages?conversation_id=in.(${hers.map((h) => h.conversation_id).join(",")})&sender_id=eq.${ADMIN_ID}&select=id,conversation_id,sender_id,body,created_at&order=created_at.desc&limit=1`);
  }
  if (!msg) { console.error("no such message"); process.exit(1); }
  if (msg.sender_id !== ADMIN_ID) { console.error("That message was sent by the student. unsend only removes your own messages."); process.exit(1); }
  const parts = await rest(`conversation_participants?conversation_id=eq.${msg.conversation_id}&user_id=neq.${ADMIN_ID}&select=user_id,last_read_at`);
  const seen = parts.some((p) => p.last_read_at && p.last_read_at >= msg.created_at);
  console.log(`${day(msg.created_at)} ${String(msg.created_at).slice(11, 16)}  "${String(msg.body).replace(/\s+/g, " ").slice(0, 200)}"`);
  console.log(seen ? "  ! She has already opened this thread since it was sent; removing it now cannot un-read it." : "  Not opened yet: removing it means she never sees it.");
  if (dry) { console.log("(dry run — nothing removed)"); process.exit(0); }
  await rest(`messages?id=eq.${msg.id}&sender_id=eq.${ADMIN_ID}`, { method: "DELETE" });
  const [still] = await rest(`messages?id=eq.${msg.id}&select=id`);
  if (still) { console.error("Delete did not land (RLS refused it). Message is still there."); process.exit(1); }
  console.log("Unsent. The message is gone from her inbox.");
} else if (cmd === "read") {
  const u = await resolve(pos);
  const mine = await rest(`conversation_participants?user_id=eq.${ADMIN_ID}&select=conversation_id`);
  const hers = await rest(`conversation_participants?user_id=eq.${u.class_id}&select=conversation_id`);
  const shared = hers.map((h) => h.conversation_id).filter((c) => mine.some((m) => m.conversation_id === c));
  if (!shared.length) { console.log(`No thread with ${nameOf(u)}.`); process.exit(0); }
  if (dry) { console.log(`would mark ${shared.length} thread(s) read`); process.exit(0); }
  await rest(`conversation_participants?user_id=eq.${ADMIN_ID}&conversation_id=in.(${shared.join(",")})`, { method: "PATCH", body: JSON.stringify({ last_read_at: new Date().toISOString() }) });
  console.log(`Marked ${shared.length} thread(s) with ${nameOf(u)} read.`);
}
