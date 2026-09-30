import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { execFile } from 'node:child_process';
import { promisify } from 'node:util';
import { projectPath, vaultRoot } from './project-paths.mjs';

const run = promisify(execFile);
const ops = projectPath('.lsatu-ops');
const relative = 'scripts/.ai-os-guided-plan.generated.ts';
const argv = process.argv.slice(2);
if (argv.includes('--help')) {
  console.log('Usage: node system/scripts/lsatu-guided-plan.mjs --file <plan.json> [--dry-run]\n       node system/scripts/lsatu-guided-plan.mjs --json <single-line plan JSON> [--dry-run]');
  process.exit(0);
}
if (!argv.includes('--file') && !argv.includes('--json')) throw new Error('Provide --file or --json');
if (argv.some(arg => /[\r\n]/.test(arg))) throw new Error('Multiline arguments are refused; use a file');
const childOptions = { windowsHide: true, maxBuffer: 4 * 1024 * 1024, timeout: 120000 };
async function git(args) { return (await run('git', ['-C', ops, ...args], childOptions)).stdout.trim(); }
const dirty = await git(['status', '--porcelain', '--untracked-files=no']);
if (dirty) throw new Error('Operational checkout has tracked edits; not running');
await git(['fetch', '-q', 'origin', 'main']);
await git(['checkout', '-q', '--detach', 'origin/main']);
const excludeName = await git(['rev-parse', '--git-path', 'info/exclude']);
const excludeFile = path.resolve(ops, excludeName);
const exclusion = '/' + relative;
const excludes = fs.readFileSync(excludeFile, 'utf8');
if (!excludes.split(/\r?\n/).includes(exclusion)) fs.appendFileSync(excludeFile, '\n' + exclusion + '\n');
const source = fs.readFileSync(path.join(vaultRoot, 'system/scripts/lsatu-guided-plan.ts'), 'utf8');
if (source.split('__VAULT_ROOT__').length !== 2) throw new Error('Expected one vault placeholder');
fs.writeFileSync(path.join(ops, relative), source.replace("'__VAULT_ROOT__'", JSON.stringify(vaultRoot)));
const appRequire = createRequire(path.join(ops, 'package.json'));
const vite = path.join(path.dirname(appRequire.resolve('vite-node/package.json')), 'vite-node.mjs');
const runtimeArgs = [...argv];
const fileFlag = runtimeArgs.indexOf('--file');
if (fileFlag >= 0) runtimeArgs[fileFlag + 1] = path.resolve(vaultRoot, runtimeArgs[fileFlag + 1]);
try {
  const { stdout, stderr } = await run(process.execPath, [vite, relative, '--', ...runtimeArgs], { ...childOptions, cwd: ops, env: { ...process.env, TZ: 'America/Toronto' } });
  const resultLine = stdout.split(/\r?\n/).find(line => line.startsWith('LSATU_GUIDED_RESULT='));
  if (!resultLine) throw new Error('Runner returned no structured result');
  if (stderr.trim()) process.stderr.write(stderr);
  console.log(resultLine.slice('LSATU_GUIDED_RESULT='.length));
} catch (error) {
  process.stderr.write(String(error.stderr || error.message).trim() + '\n');
  process.exitCode = 1;
} finally {
  await git(['restore', 'supabase/functions/mcp/index.ts']);
}
