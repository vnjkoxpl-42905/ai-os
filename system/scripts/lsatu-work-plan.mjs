import fs from 'node:fs';
import path from 'node:path';
import { randomUUID } from 'node:crypto';
import { executeOps } from './lsatu-ops-runtime.mjs';
import { vaultRoot } from './project-paths.mjs';
import { validatePlan } from './lsatu-work-plan-core.mjs';

const args = process.argv.slice(2);
if (args.includes('--help')) {
  console.log('Usage: node system/scripts/lsatu-work-plan.mjs --file <plan.json> [--dry-run | --verify-existing]\nKinds: guided_drill, activity, bootcamp, interactive_note. Guided drills require schedule/due. Other work defaults to immediate availability and no due date.');
  process.exit(0);
}
const flag = name => { const index = args.indexOf('--' + name); return index < 0 ? undefined : args[index + 1]; };
if (Boolean(flag('file')) === Boolean(flag('json'))) throw new Error('Provide exactly one --file or --json');
const runtimeArgs = [...args];
if (flag('file')) runtimeArgs[runtimeArgs.indexOf('--file') + 1] = path.resolve(vaultRoot, flag('file'));
const plan = validatePlan(JSON.parse(flag('json') ?? fs.readFileSync(path.resolve(vaultRoot, flag('file')), 'utf8')));
for (const [field, option] of [['dry_run', '--dry-run'], ['verify_existing', '--verify-existing']]) {
  if (plan[field] != null && typeof plan[field] !== 'boolean') throw new Error(field + ' must be a boolean');
  if (plan[field] && !runtimeArgs.includes(option)) runtimeArgs.push(option);
}
if (runtimeArgs.includes('--dry-run') && runtimeArgs.includes('--verify-existing')) throw new Error('Choose dry-run or verify-existing');
function artifactDirectory() {
  if (plan.student_folder != null) {
    const students = fs.realpathSync(path.join(vaultRoot, 'students'));
    const folder = fs.realpathSync(path.resolve(vaultRoot, plan.student_folder));
    const relative = path.relative(students, folder);
    if (!relative || relative.startsWith('..') || path.isAbsolute(relative) || !fs.statSync(folder).isDirectory()) throw new Error('student_folder must be an existing folder inside students');
    return path.join(folder, 'assignments', plan.id ?? 'work-plan');
  }
  return path.join(vaultRoot, 'system/runtime/lsatu-work', plan.id ?? 'work-plan');
}
const directory = artifactDirectory();
const artifact = path.join(directory, new Date().toISOString().replace(/[:.]/g, '-') + '-' + randomUUID().slice(0, 8) + '.generated.json');
let operationResult;
try {
  const runtime = await executeOps({ sourcePath: 'system/scripts/lsatu-work-plan.ts', scriptName: 'ai-os-work-plan.generated.ts', args: runtimeArgs });
  const line = runtime.stdout.split(/\r?\n/).find(line => line.startsWith('LSATU_WORK_RESULT='));
  if (!line) throw new Error('Runner returned no structured result');
  const result = operationResult = JSON.parse(line.slice('LSATU_WORK_RESULT='.length));
  result.runtime = { ...runtime.timings, cache_hit: runtime.cache_hit, ops_commit: runtime.ops_commit, source_sha256: runtime.source_sha256 };
  result.audit_file = artifact;
  fs.mkdirSync(directory, { recursive: true });
  fs.writeFileSync(artifact, JSON.stringify(result, null, 2) + '\n', { flag: 'wx' });
  console.log(JSON.stringify(result));
} catch (error) {
  const output = String(error.stderr ?? error.message);
  const line = output.split(/\r?\n/).find(line => line.startsWith('LSATU_WORK_ERROR='));
  const successLine = String(error.stdout ?? '').split(/\r?\n/).find(line => line.startsWith('LSATU_WORK_RESULT='));
  const saved = operationResult ?? (successLine ? JSON.parse(successLine.slice('LSATU_WORK_RESULT='.length)) : undefined);
  const result = line ? JSON.parse(line.slice('LSATU_WORK_ERROR='.length)) : { error: error.message, completed_results: saved?.results ?? [], ...(saved ? { operation_completed: true } : {}), instruction: 'Inspect saved IDs before retrying. Never replay notification failures automatically.' };
  let auditWritten = false;
  let auditError;
  try { fs.mkdirSync(directory, { recursive: true }); fs.writeFileSync(artifact, JSON.stringify(result, null, 2) + '\n', { flag: 'wx' }); auditWritten = true; }
  catch (writeError) { auditError = writeError.message; }
  console.error(JSON.stringify({ ...result, ...(auditWritten ? { audit_file: artifact } : { audit_write_failed: auditError }) }));
  process.exitCode = 1;
}
