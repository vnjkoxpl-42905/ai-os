// Immediate local MCP client while a chat still has the older tool snapshot.
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { pathToFileURL } from 'node:url';
import { vaultRoot } from './project-paths.mjs';
const req = createRequire(new URL('../runtime/lsatu-mcp/package.json', import.meta.url));
const [{ Client }, { StdioClientTransport }] = await Promise.all([
  import(pathToFileURL(req.resolve('@modelcontextprotocol/sdk/client/index.js')).href),
  import(pathToFileURL(req.resolve('@modelcontextprotocol/sdk/client/stdio.js')).href),
]);
const [name, flag, value] = process.argv.slice(2);
const allowed = ['search_guided_drills', 'preview_guided_drill_batch', 'assign_guided_drill_batch', 'assign_student_work', 'search_assignable_work', 'publish_interactive_lesson', 'list_student_classroom_items'];
if (!allowed.includes(name) || !['--file', '--json'].includes(flag) || !value) throw new Error('Usage: node lsatu-mcp-call.mjs <LSAT U tool> --file <arguments.json> | --json <single-line JSON>');
const args = JSON.parse(flag === '--file' ? fs.readFileSync(path.resolve(value), 'utf8') : value);
const transport = new StdioClientTransport({ command: process.execPath, args: [path.join(vaultRoot, 'system/scripts/lsatu-lesson-mcp.mjs')], cwd: vaultRoot, stderr: 'inherit' });
const client = new Client({ name: 'ai-os-guided-operator', version: '1.0.0' });
try {
  await client.connect(transport);
  const result = await client.callTool({ name, arguments: args }, undefined, { timeout: 360000 });
  if (result.isError) process.exitCode = 1;
  console.log(JSON.stringify(result.structuredContent ?? result));
} finally {
  await client.close();
}
