import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import { vaultRoot } from './project-paths.mjs';

const ops = path.resolve(process.argv[2]);
const relative = 'scripts/.ai-os-assign.generated.ts';
const source = fs.readFileSync(path.join(ops, 'scripts/assign.ts'), 'utf8');
const needle = 'readEnv(path.resolve(REPO, "../../.env"))';
if (source.split(needle).length !== 2) {
  throw new Error('assign.ts credential reader changed; review before running.');
}
const generated = source.replace(needle, `readEnv(${JSON.stringify(path.join(vaultRoot, '.env'))})`);
const exclude = execFileSync('git', ['-C', ops, 'rev-parse', '--git-path', 'info/exclude'], {
  encoding: 'utf8', windowsHide: true,
}).trim();
const excludePath = path.resolve(ops, exclude);
const existing = fs.existsSync(excludePath) ? fs.readFileSync(excludePath, 'utf8') : '';
if (!existing.split(/\r?\n/).includes(`/${relative}`)) {
  fs.mkdirSync(path.dirname(excludePath), { recursive: true });
  fs.writeFileSync(excludePath, `${existing.replace(/\s*$/, '')}\n/${relative}\n`);
}
fs.writeFileSync(path.join(ops, relative), generated);
