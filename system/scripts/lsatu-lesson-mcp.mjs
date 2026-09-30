// Local MCP entry point. Content operations live in AI OS, so changing this
// server never requires an LSAT U app deployment.
import { projectPath } from './project-paths.mjs';
import { createRequire } from 'node:module';
import { pathToFileURL, fileURLToPath } from 'node:url';
import { execFile } from 'node:child_process';
import { promisify } from 'node:util';
import path from 'node:path';
import fs from 'node:fs';

const vault = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const appRequire = createRequire(projectPath('lsatu', 'package.json'));
const [{ McpServer }, { StdioServerTransport }, { z }] = await Promise.all([
  import(pathToFileURL(appRequire.resolve('@modelcontextprotocol/sdk/server/mcp.js')).href),
  import(pathToFileURL(appRequire.resolve('@modelcontextprotocol/sdk/server/stdio.js')).href),
  import(pathToFileURL(appRequire.resolve('zod')).href),
]);
const run = promisify(execFile);
const admin = path.join(vault, 'system', 'scripts', 'lsatu-admin.mjs');
const server = new McpServer({ name: 'lsat-u-lessons', version: '1.2.0' });

async function command(args) {
  try {
    const { stdout } = await run(process.execPath, [admin, ...args], {
      cwd: vault, windowsHide: true, maxBuffer: 2 * 1024 * 1024, timeout: 120000,
    });
    return { content: [{ type: 'text', text: stdout.trim() }] };
  } catch (error) {
    return { isError: true, content: [{ type: 'text', text: String(error.stderr || error.message).trim() }] };
  }
}

const guidedPlan = path.join(vault, 'system/scripts/lsatu-guided-plan.mjs');
// Serialize guided writes within this MCP process. No automatic write retries.
let guidedQueue = Promise.resolve();
async function guidedCommand(plan, dryRun) {
  const operation = guidedQueue.then(async () => {
    try {
      const { stdout } = await run(process.execPath, [guidedPlan, '--json', JSON.stringify(plan), ...(dryRun ? ['--dry-run'] : [])], {
        cwd: vault, windowsHide: true, maxBuffer: 4 * 1024 * 1024, timeout: 180000,
      });
      const result = JSON.parse(stdout.trim());
      return { content: [{ type: 'text', text: JSON.stringify(result) }], structuredContent: result };
    } catch (error) {
      return { isError: true, content: [{ type: 'text', text: String(error.stderr || error.message).trim() }] };
    }
  });
  guidedQueue = operation.then(() => undefined, () => undefined);
  return operation;
}

const guidedAssignment = z.object({
  drill: z.string().min(2).describe('Exact published guided drill slug from search_guided_drills.'),
  schedule: z.string().regex(/^\d{4}-\d{2}-\d{2}$/),
  due: z.string().regex(/^\d{4}-\d{2}-\d{2}$/),
  level: z.enum(['beginner', 'intermediate', 'advanced']).nullable().optional(),
  count: z.number().int().min(1).max(50).optional().describe('Omit to retain the existing drill size and matching instruction card.'),
  max_difficulty: z.number().int().min(1).max(5).optional().describe('Hard preflight ceiling on every question that can be drawn at the requested level.'),
});
const guidedSchema = {
  id: z.string().optional(),
  student: z.string().min(2).describe('One exact student name or email.'),
  assignments: z.array(guidedAssignment).min(1).max(14),
};

server.registerTool('search_guided_drills', {
  title: 'Find matching LSAT U guided drills',
  description: 'Search the mapped guided drill catalog by title, question type, reasoning, feature, or slug. Returns compact difficulty/pool metadata and snapshot time; assignment preflight rechecks live data.',
  inputSchema: { query: z.string().default(''), level: z.enum(['beginner', 'intermediate', 'advanced']).optional(), min_difficulty: z.number().int().min(1).max(5).optional(), max_difficulty: z.number().int().min(1).max(5).optional(), include_pinned: z.boolean().default(false), limit: z.number().int().min(1).max(30).default(12) },
  annotations: { readOnlyHint: true },
}, ({ query, level, min_difficulty, max_difficulty, include_pinned, limit }) => {
  const catalog = JSON.parse(fs.readFileSync(path.join(vault, 'references/lsatu-guided-drill-catalog.json'), 'utf8'));
  const words = query.toLowerCase().trim().split(/\s+/).filter(Boolean);
  function eligible(d) {
    if (d.pool_summary.pinned_qids) return { min: d.pool_summary.pinned_difficulty_min, max: d.pool_summary.pinned_difficulty_max, count: d.pool_summary.pinned_known_count };
    const band = level ? catalog.bands[level] : [1, 5];
    const difficulties = Object.entries(d.pool_summary.difficulty_counts).filter(([difficulty, count]) => count > 0 && Number(difficulty) >= band[0] && Number(difficulty) <= band[1]);
    return { min: difficulties.length ? Number(difficulties[0][0]) : null, max: difficulties.length ? Number(difficulties.at(-1)[0]) : null, count: difficulties.reduce((sum, [, count]) => sum + count, 0) };
  }
  const matching = catalog.drills.filter(d => {
    const selected = eligible(d);
    return d.is_published && (include_pinned || !d.pool_summary.pinned_qids) && !d.pool_summary.missing_pinned_qids.length && words.every(word => JSON.stringify([d.slug, d.title, d.bank_filter, d.reasoning_types]).toLowerCase().includes(word)) && selected.count >= (d.pool_summary.pinned_qids || d.question_count || 1) && (min_difficulty == null || (selected.min != null && selected.min >= min_difficulty)) && (max_difficulty == null || (selected.max != null && selected.max <= max_difficulty));
  }).sort((a, b) => Number(words.every(word => b.title.toLowerCase().includes(word))) - Number(words.every(word => a.title.toLowerCase().includes(word))));
  const result = { snapshot: catalog.meta.generated_at, total_matches: matching.length, drills: matching.slice(0, limit).map(d => ({ slug: d.slug, title: d.title, count: d.pool_summary.pinned_qids || d.question_count, minutes: d.estimated_minutes, catalog_level: d.level, native_band: [d.bank_filter.difficulty_min, d.bank_filter.difficulty_max], selectable_at_level: d.pool_summary.pinned_qids ? 'exact pins; level ignored' : level ?? 'native', eligible: eligible(d), pool_difficulty_counts: d.pool_summary.difficulty_counts, pinned_count: d.pool_summary.pinned_qids })) };
  return { content: [{ type: 'text', text: JSON.stringify(result) }], structuredContent: result };
});

server.registerTool('preview_guided_drill_batch', {
  title: 'Preflight a guided drill schedule',
  description: 'Read-only live preflight for one student and up to 14 guided assignments. Resolves identity/access, published drills, deployed question pools, difficulty ceilings, dates, and existing assignments. One sync and login for the whole plan.',
  inputSchema: guidedSchema,
  annotations: { readOnlyHint: true },
}, plan => guidedCommand(plan, true));

server.registerTool('assign_guided_drill_batch', {
  title: 'Assign and verify a guided drill schedule',
  description: 'Assign existing guided drills to one named student through the app assignWork. Preflights every item before writes, verifies saved assignments and Classroom dates/visibility, and reports inbox/bell/email results. A repeat returns matching existing assignments without notifying again. No browser or app deployment.',
  inputSchema: guidedSchema,
  annotations: { readOnlyHint: false, destructiveHint: false, idempotentHint: true },
}, plan => guidedCommand(plan, false));

server.registerTool('publish_interactive_lesson', {
  title: 'Assign an interactive LSAT U lesson',
  description: 'Assign a complete HTML lesson directly to one student. Verifies byte-for-byte content, visibility, and one active copy; replaces only prior versions of the same lesson. No browser or Lovable publish.',
  inputSchema: {
    student: z.string().min(2).describe('Exact student email or unambiguous name.'),
    html_file: z.string().min(1).describe('Absolute path to marked, self-contained HTML within AI OS.'),
    title: z.string().min(1).max(160),
    dry_run: z.boolean().optional(),
  },
  annotations: { readOnlyHint: false, destructiveHint: true, idempotentHint: true },
}, ({ student, html_file, title, dry_run }) => command([
  'post-lesson', student, html_file, '--title', title, ...(dry_run ? ['--dry-run'] : []),
]));

server.registerTool('list_student_classroom_items', {
  title: 'List a student’s LSAT U Classroom items',
  description: 'Read the current Classroom items and IDs for one student.',
  inputSchema: { student: z.string().min(2) },
  annotations: { readOnlyHint: true },
}, ({ student }) => command(['items', student]));

await server.connect(new StdioServerTransport());
