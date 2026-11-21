#!/usr/bin/env node
// Read-only export of everything Joshua has assigned, every student, from LSAT U.
// Writes wiki/homework-assigning/data/ (generated) and notes-archive/ (note HTML).
// Uses the same saved admin login as lsatu-admin.mjs. Posts and changes nothing.
//
//   node system/scripts/lsatu-assignment-export.mjs
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { projectPath } from "./project-paths.mjs";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const OUT = path.join(ROOT, "wiki", "homework-assigning");
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
const env = { ...readEnv(projectPath("lsatu", ".env")), ...readEnv(path.join(ROOT, ".env")) };
const U = env.VITE_SUPABASE_URL, K = env.VITE_SUPABASE_PUBLISHABLE_KEY;
const tok = await (await fetch(`${U}/auth/v1/token?grant_type=password`, {
  method: "POST", headers: { apikey: K, "content-type": "application/json" },
  body: JSON.stringify({ email: env.LSATPREP_ADMIN_EMAIL, password: env.LSATPREP_ADMIN_PASSWORD }),
})).json();
if (!tok.access_token) { console.error("sign-in failed"); process.exit(1); }
const H = { apikey: K, authorization: `Bearer ${tok.access_token}` };
const get = async (q) => {
  const r = await fetch(`${U}/rest/v1/${q}`, { headers: H });
  const j = await r.json();
  if (!r.ok) throw new Error(`${q.split("?")[0]}: ${j.message ?? r.status}`);
  return j;
};

const usersRes = await (await fetch(`${U}/functions/v1/admin-manage-users`, { headers: H })).json();
const users = Array.isArray(usersRes) ? usersRes : usersRes.users ?? [];

const slugify = (s) => String(s ?? "").toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
const folders = fs.readdirSync(path.join(ROOT, "students"), { withFileTypes: true })
  .filter((d) => d.isDirectory() && !d.name.startsWith("_")).map((d) => d.name);
const norm = (s) => String(s ?? "").toLowerCase().replace(/[^a-z0-9]+/g, "");
const aliasFile = path.join(ROOT, "students", "_aliases.md");
const aliases = new Map();
if (fs.existsSync(aliasFile)) for (const m of fs.readFileSync(aliasFile, "utf8").matchAll(/^- (.+?) -> ([a-z0-9-]+)\s*$/gm)) aliases.set(norm(m[1]), m[2]);
const TEST_ACCOUNTS = new Set(["josh", "lsatmaster", "tester", "joshuafisseha"]);
function slugFor(u) {
  const a = aliases.get(norm(u.display_name)) ?? aliases.get(norm(u.email));
  if (a && folders.includes(a)) return a;
  const full = slugify(u.display_name), first = slugify((u.display_name || u.email || "").split(/[ @]/)[0]);
  if (folders.includes(full)) return full;
  if (folders.includes(first)) return first;
  const hit = folders.filter((f) => f.split("-")[0] === first);
  return hit.length === 1 ? hit[0] : null;
}

const PAGE = 1000;
let items = [];
for (let from = 0; ; from += PAGE) {
  const page = await get(`classroom_items?select=id,student_id,type,title,status,due_at,unlock_at,created_at,description,source_table,source_id,visible_to_student&order=created_at.asc&limit=${PAGE}&offset=${from}`);
  items = items.concat(page);
  if (page.length < PAGE) break;
}

const byId = new Map(users.map((u) => [u.class_id, u]));
const unmapped = new Set();
const rows = [];
const NOTE = new Set(["note", "session_recap", "smartboard_recap", "interactive_note"]);
fs.mkdirSync(path.join(OUT, "data"), { recursive: true });
fs.mkdirSync(path.join(OUT, "notes-archive"), { recursive: true });

for (const it of items) {
  const u = byId.get(it.student_id);
  if (!u) continue;
  if (TEST_ACCOUNTS.has(norm(u.display_name))) continue;
  const slug = slugFor(u);
  if (!slug) unmapped.add(u.display_name || u.email);
  const key = slug ?? `no-folder-${slugify(u.display_name || u.email)}`;
  let archive = null, outline = null;
  if (NOTE.has(it.type) && it.status !== "archived") {
    const [full] = await get(`classroom_items?id=eq.${it.id}&select=content_html,content_markdown`);
    const body = full?.content_html || full?.content_markdown || "";
    if (body) {
      const ext = full.content_html ? "html" : "md";
      const dir = path.join(OUT, "notes-archive", key);
      fs.mkdirSync(dir, { recursive: true });
      const name = `${it.created_at.slice(0, 10)}-${slugify(it.title).slice(0, 70)}-${it.id.slice(0, 6)}.${ext}`;
      fs.writeFileSync(path.join(dir, name), body);
      archive = path.relative(OUT, path.join(dir, name)).replace(/\\/g, "/");
      if (ext === "html") {
        const b = body.replace(/<style[\s\S]*?<\/style>|<script[\s\S]*?<\/script>/gi, "");
        outline = [...b.matchAll(/<h[12][^>]*>([\s\S]*?)<\/h[12]>/gi)].map((m) => m[1].replace(/<[^>]+>/g, "").replace(/\s+/g, " ").trim()).filter(Boolean);
      }
    }
  }
  rows.push({
    id: it.id, student: u.display_name || u.email, slug, key, type: it.type, title: it.title, status: it.status,
    added: it.created_at.slice(0, 10), unlock: it.unlock_at?.slice(0, 10) ?? null, due: it.due_at?.slice(0, 10) ?? null,
    source_table: it.source_table, source_id: it.source_id, archive, outline,
  });
}
fs.writeFileSync(path.join(OUT, "data", "assignments.generated.json"), JSON.stringify({ generated: new Date().toISOString(), count: rows.length, rows }, null, 1));
const stat = {};
for (const r of rows) stat[r.key] = (stat[r.key] ?? 0) + 1;
console.log(JSON.stringify({ items: rows.length, students: Object.keys(stat).length, perStudent: stat, unmapped: [...unmapped] }, null, 1));
