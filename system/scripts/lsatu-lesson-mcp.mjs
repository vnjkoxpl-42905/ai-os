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
  inputSchema: { query: z.string().default(''), max_difficulty: z.number().int().min(1).max(5).optional(), limit: z.number().int().min(1).max(30).default(12) },
  annotations: { readOnlyHint: true },
}, ({ query, max_difficulty, limit }) => {
  const catalog = JSON.parse(fs.readFileSync(path.join(vault, 'references/lsatu-guided-drill-catalog.json'), 'utf8'));
  const words = query.toLowerCase().trim().split(/\s+/).filter(Boolean);
  const matching = catalog.drills.filter(d => d.is_published && words.every(word => JSON.stringify([d.slug, d.title, d.bank_filter, d.reasoning_types]).toLowerCase().includes(word)) && (max_difficulty == null || (d.pool_summary.difficulty_max != null && d.pool_summary.difficulty_max <= max_difficulty)));
  const result = { snapshot: catalog.meta.generated_at, total_matches: matching.length, drills: matching.slice(0, limit).map(d => ({ slug: d.slug, title: d.title, count: d.question_count, minutes: d.estimated_minutes, catalog_level: d.level, native_band: [d.bank_filter.difficulty_min, d.bank_filter.difficulty_max], pool: d.pool_summary, bank_filter: d.bank_filter })) };
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
