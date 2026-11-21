// Run the application's official assignment CLI in the shared isolated runtime.
// Retains the section/homework-set paths not yet supported by the mixed MCP.
import fs from 'node:fs/promises';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import { vaultRoot, projectsRoot } from './project-paths.mjs';
import { executeOps } from './lsatu-ops-runtime.mjs';

const app = path.join(projectsRoot, 'lsatu');
const args = process.argv.slice(2);
if (!args.includes('--section') && !args.includes('--set')) throw new Error('Use mixed MCP for other assignment types');
let source = execFileSync('git', ['-C', app, 'show', 'origin/main:scripts/assign.ts'], { encoding: 'utf8', windowsHide: true });
function replaceOnce(before, after) {
  if (source.split(before).length !== 2) throw new Error('Official CLI changed; review adapter before running');
  source = source.replace(before, after);
}
replaceOnce('readEnv(path.resolve(REPO, "../../.env"))', "readEnv(path.join('__VAULT_ROOT__', '.env'))");
// Sparse runtime deliberately omits public/. Read the same deployed section data.
const start = source.indexOf('  const dataDir = path.join(REPO, "public", "data");');
const end = source.indexOf('  const qids = rows', start);
if (start < 0 || end < start) throw new Error('Section reader changed');
source = source.slice(0, start) + `  const file = 'PT' + pt + '-S' + section + '-LR.json';
  const rows = deployedSections.find(s => s.filename.split('/').pop() === file)?.questions;
  if (!Array.isArray(rows) || !rows.length) throw new Error('Missing deployed LR section: ' + file);
` + source.slice(end);
source = `const deployedResponse = await fetch('https://lsatprep.study/data/_bank.generated.json');
if (!deployedResponse.ok) throw new Error('Deployed section bank unavailable');
const deployedSections = await deployedResponse.json();
if (!Array.isArray(deployedSections)) throw new Error('Invalid deployed bank');
` + source;
const folder = path.join(vaultRoot, 'system/scripts/.generated');
await fs.mkdir(folder, { recursive: true });
const sourcePath = path.join(folder, 'official-section-assign.ts');
await fs.writeFile(sourcePath, source);
const result = await executeOps({ sourcePath, scriptName: 'official-section-assign.generated.ts', args });
process.stdout.write(result.stdout);
if (result.stderr) process.stderr.write(result.stderr);
console.log(JSON.stringify({ runtime: { commit: result.ops_commit, timings: result.timings } }));
