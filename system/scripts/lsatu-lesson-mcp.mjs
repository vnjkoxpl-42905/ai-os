// Local MCP entry point. Content operations live in AI OS, so changing this
// server never requires an LSAT U app deployment.
import { projectPath } from './project-paths.mjs';
import { createRequire } from 'node:module';
import { pathToFileURL, fileURLToPath } from 'node:url';
import { execFile } from 'node:child_process';
import { promisify } from 'node:util';
import path from 'node:path';

const vault = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const appRequire = createRequire(projectPath('lsatu', 'package.json'));
const [{ McpServer }, { StdioServerTransport }, { z }] = await Promise.all([
  import(pathToFileURL(appRequire.resolve('@modelcontextprotocol/sdk/server/mcp.js')).href),
  import(pathToFileURL(appRequire.resolve('@modelcontextprotocol/sdk/server/stdio.js')).href),
  import(pathToFileURL(appRequire.resolve('zod')).href),
]);
const run = promisify(execFile);
const admin = path.join(vault, 'system', 'scripts', 'lsatu-admin.mjs');
const server = new McpServer({ name: 'lsat-u-lessons', version: '1.1.0' });

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
