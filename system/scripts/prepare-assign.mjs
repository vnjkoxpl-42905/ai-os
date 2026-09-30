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
let generated = source.replace(needle, `readEnv(${JSON.stringify(path.join(vaultRoot, '.env'))})`);
generated = 'import { isDeepStrictEqual } from "node:util";\n' + generated;
// Optional teacher-authored guided content. Assignment rows still go through
// the app's assignWork, including its scheduling, notifications and rollback.
const drillNeedle = 'const d = await resolveDrill(drillQuery);';
if (source.split(drillNeedle).length !== 2) throw new Error('assign.ts drill resolver changed; review before running.');
generated = generated.replace(drillNeedle, 'const d = arg("guided-spec") ? await resolveGuidedSpec(arg("guided-spec")!) : await resolveDrill(drillQuery);');
const homeworkNeedle = 'if (item.kind === "homework_set") {';
if (source.split(homeworkNeedle).length !== 2) throw new Error('assign.ts homework guard changed; review before running.');
generated = generated.replace(homeworkNeedle, `
  if (item.kind === "guided_drill" && arg("guided-spec") && item.drillId !== '(new)') {
    let query = supabase.from('guided_drill_assignments').select('id,status,scheduled_for').eq('student_id', student.class_id).eq('guided_drill_id', item.drillId);
    query = scheduleFor ? query.eq('scheduled_for', scheduleFor) : query.is('scheduled_for', null);
    const { data: existing, error } = await query;
    if (error) throw error;
    if (existing?.length) throw new Error('This guided spec is already assigned for this date; verify it instead of reassigning: ' + existing[0].id);
  }
  if (item.kind === "homework_set") {`);
const mainNeedle = 'async function main() {';
if (source.split(mainNeedle).length !== 2) throw new Error('assign.ts main entry changed; review before running.');
generated = generated.replace(mainNeedle, `
async function resolveGuidedSpec(file: string) {
  const spec = JSON.parse(fs.readFileSync(path.resolve(file), 'utf8'));
  if (spec.slug !== drillQuery || !spec.title || !Array.isArray(spec.question_qids) || spec.question_qids.length < 1) throw new Error('Invalid guided spec or slug mismatch');
  if (spec.question_count !== spec.question_qids.length || !Number.isInteger(spec.difficulty_min) || !Number.isInteger(spec.difficulty_max) || spec.difficulty_min < 1 || spec.difficulty_max > 5 || spec.difficulty_min > spec.difficulty_max) throw new Error('Invalid guided count or difficulty range');
  if (new Set(spec.question_qids).size !== spec.question_qids.length) throw new Error('Duplicate question IDs in guided spec');
  for (const qid of spec.question_qids) {
    const m = /^PT(\\d+)-S(\\d+)-Q(\\d+)$/.exec(qid);
    if (!m) throw new Error('Invalid question ID: ' + qid);
    const rows = JSON.parse(fs.readFileSync(path.join(REPO, 'public/data', 'PT' + m[1] + '-S' + m[2] + '-LR.json'), 'utf8'));
    const q = rows.find((q: any) => q.questionNumber === Number(m[3]));
    if (!q || String(q.questionType).toLowerCase() !== 'must be true' || !(q.reasoningType || []).includes('Conditional Reasoning') || q.questionDifficulty < spec.difficulty_min || q.questionDifficulty > spec.difficulty_max) throw new Error('Question does not satisfy spec: ' + qid);
    if (!q.stimulus || !q.questionStem || !q.correctAnswer || Object.keys(q.answerChoices || {}).length !== 5) throw new Error('Incomplete question: ' + qid);
  }
  const { data: prior, error: readError } = await supabase.from('guided_drills').select('*').eq('slug', spec.slug).maybeSingle();
  if (readError) throw readError;
  if (prior) {
    for (const key of Object.keys(spec)) if (!isDeepStrictEqual(prior[key], spec[key])) throw new Error('Existing guided content differs: ' + key);
    return prior;
  }
  console.log('  validated ' + spec.question_qids.length + ' conditional Must Be True questions, difficulty ' + spec.difficulty_min + '-' + spec.difficulty_max);
  if (dryRun) return { id: '(new)', title: spec.title, slug: spec.slug };
  const { data, error } = await supabase.from('guided_drills').insert(spec).select('id,title,slug').single();
  if (error) throw error;
  return data;
}

async function main() {`);
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
