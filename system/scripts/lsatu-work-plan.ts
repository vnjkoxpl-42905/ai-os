// Runs in the operational app checkout through lsatu-ops-runtime.mjs.
import fs from 'node:fs';
import path from 'node:path';
import { pathToFileURL } from 'node:url';
import { createHash } from 'node:crypto';
import { performance } from 'node:perf_hooks';
import { supabase } from '@/integrations/supabase/client';
import { assignWork } from '@/lib/assignWork';
import { BOOTCAMPS } from '@/lib/bootcamps';
import { resolveConditionalAssignment } from '@/lib/conditionalBootcampAssignment';
import { resolveLeveledDrillQids } from '@/lib/guidedDrillLevel';
import { normalizeQType } from '@/lib/questionLoader';
import { levelBand, isInBand } from '@/lib/studentLevel';
import { resolvePool } from './lib/drill-pool.mjs';

const VAULT = '__VAULT_ROOT__';
const core = await import(pathToFileURL(path.join(VAULT, 'system/scripts/lsatu-work-plan-core.mjs')).href);
const { validateInteractiveLesson, lessonMarkerId } = await import(pathToFileURL(path.join(VAULT, 'system/scripts/lsatu-lesson-validate.mjs')).href);
const { validatePlan, boundary, sameTime, confinedFile, resolveExact, resolveActivity, oneVisible, assertExistingOnly, activityCandidates } = core;
const started = performance.now();
const arg = (name: string) => { const i = process.argv.indexOf('--' + name); return i < 0 ? undefined : process.argv[i + 1]; };
const dryRun = process.argv.includes('--dry-run');
const verifyOnly = process.argv.includes('--verify-existing');
const completed: any[] = [];
async function query(value: any): Promise<any> { const { data, error } = await value; if (error) throw error; return data; }
async function allRows(table: string, configure: (q: any) => any = q => q) {
  const rows: any[] = [];
  let expected: number | undefined;
  while (rows.length < 10000) {
    const offset = rows.length;
    const { data: batch, error, count } = await configure(supabase.from(table as any).select('*', { count: 'exact' })).order('id').range(offset, offset + 499);
    if (error) throw error;
    if (!Number.isInteger(count) || count < 0 || count >= 10000 || (expected !== undefined && count !== expected)) throw new Error('Incomplete or changing read for ' + table);
    expected = count;
    if (!Array.isArray(batch) || (!batch.length && rows.length < expected)) throw new Error('Truncated read for ' + table);
    rows.push(...batch);
    if (rows.length === expected) return rows;
    if (rows.length > expected) throw new Error('Unexpected row count for ' + table);
  }
  throw new Error('Read limit reached for ' + table + '; refusing incomplete duplicate check');
}
function envFrom(file: string) {
  const out: Record<string, string> = {};
  for (const line of fs.readFileSync(file, 'utf8').split(/\r?\n/)) { const m = /^\s*([^#=\s]+)\s*=\s*(.*?)\s*$/.exec(line); if (m) out[m[1]] = m[2].replace(/^["']|["']$/g, ''); }
  return out;
}
function checkCard(card: any, entry: any, studentId: string) {
  if (card.student_id !== studentId || !card.visible_to_student || card.status === 'archived' || (entry.kind !== 'activity' && card.title !== entry.title) || !sameTime(card.unlock_at, entry.unlock) || !sameTime(card.due_at, entry.due)) throw new Error('Classroom item conflicts with plan: ' + card.id);
}
async function main() {
  if (dryRun && verifyOnly) throw new Error('Choose dry-run or verify-existing');
  const plan = validatePlan(JSON.parse(arg('json') ?? fs.readFileSync(path.resolve(arg('file') ?? ''), 'utf8')));
  // Local files and all static validation happen before authentication.
  const localNotes = new Map<any, any>();
  for (const item of plan.assignments) if (item.kind === 'interactive_note') {
    const file = confinedFile(VAULT, item.html_file, '.html');
    const html = fs.readFileSync(file, 'utf8');
    if (Buffer.byteLength(html) > 500000) throw new Error('Lesson exceeds 500 KB');
    localNotes.set(item, { html, lessonId: validateInteractiveLesson(html), sha256: createHash('sha256').update(html).digest('hex') });
  }
  const noteIds = [...localNotes.values()].map(note => note.lessonId);
  if (new Set(noteIds).size !== noteIds.length) throw new Error('Duplicate lesson marker in plan');
  const env = envFrom(path.join(VAULT, '.env'));
  const { data: auth, error: authError } = await supabase.auth.signInWithPassword({ email: env.LSATPREP_ADMIN_EMAIL, password: env.LSATPREP_ADMIN_PASSWORD });
  if (authError || !auth.user) throw new Error('Admin sign-in failed');
  const users = await query(supabase.functions.invoke('admin-manage-users', { method: 'GET' }));
  if (!Array.isArray(users)) throw new Error('Student lookup failed');
  const needle = plan.student.trim().toLowerCase();
  const exact = users.filter((u: any) => [u.class_id, u.email, u.display_name].some(v => v?.toLowerCase() === needle));
  const hits = exact.length ? exact : users.filter((u: any) => [u.email, u.display_name].some(v => v?.toLowerCase().includes(needle)));
  if (hits.length !== 1) throw new Error('Student does not resolve uniquely');
  const student = hits[0];
  if (!student.has_classroom_access) throw new Error('Student lacks Classroom access');
  // Bootcamps unlock from the assigned Classroom item (BootcampGate), and the 2026-10-02 profile trigger forces has_bootcamp_access false, so only Classroom access applies.
  // Activities open through ActivityAssignmentGate (assignmentOnly: the student owns the assignment row), and the 2026-10-02 profile trigger forces has_activity_access false on every access write ("activities and bootcamps are assigned per item"), so the flag is not a precondition. Only guided drills need their flag.
  for (const kind of ['guided_drill']) if (plan.assignments.some((i: any) => i.kind === kind) && !student[{ guided_drill: 'has_drill_access' }[kind]!]) throw new Error('Student lacks access for ' + kind);
  const needsGuided = plan.assignments.some((i: any) => i.kind === 'guided_drill');
  const needsActivity = plan.assignments.some((i: any) => i.kind === 'activity');
  const [drills, activities, cards, profile] = await Promise.all([
    needsGuided ? allRows('guided_drills') : [],
    needsActivity ? allRows('activities') : [],
    allRows('classroom_items', q => q.eq('student_id', student.class_id)),
    needsGuided ? query(supabase.from('profiles').select('proficiency_level').eq('class_id', student.class_id).single()) : null,
  ]);
  if (cards.length >= 10000) throw new Error('Classroom read reached limit; refusing incomplete duplicate check');
  const [priorGuided, priorActivities] = await Promise.all([
    needsGuided ? allRows('guided_drill_assignments', q => q.eq('student_id', student.class_id)) : [],
    needsActivity ? allRows('activity_assignments', q => q.eq('student_id', student.class_id)) : [],
  ]);
  if (priorGuided.length >= 10000 || priorActivities.length >= 10000) throw new Error('Assignment read reached limit');
  const bank = new Map<string, any>();
  if (needsGuided) {
    const response = await fetch('https://lsatprep.study/data/_bank.generated.json');
    if (!response.ok) throw new Error('Deployed question bank read failed');
    const sections = await response.json();
    if (!Array.isArray(sections) || !sections.length) throw new Error('Invalid deployed bank');
    for (const section of sections) {
      const match = /PT(\d+)-S(\d+)/.exec(section.filename ?? '');
      if (!match || !Array.isArray(section.questions)) throw new Error('Invalid deployed bank section');
      for (const q of section.questions) {
        if (q.status === 'removed' || !q.answerChoices || !q.correctAnswer || !q.questionStem) continue;
        bank.set(`PT${match[1]}-S${match[2]}-Q${q.questionNumber || 0}`, { ...q, questionType: normalizeQType(q.questionType || '', q.questionStem), questionDifficulty: q.questionDifficulty || q.Question_Difficulty || 3, reasoningType: Array.isArray(q.reasoningType) ? q.reasoningType : q.reasoningType ? [q.reasoningType] : [] });
      }
    }
  }
  const knownQids = new Set<string>(bank.keys());
  const prepared: any[] = [];
  const resolvedKeys = new Set<string>();
  for (const item of plan.assignments) {
    const entry: any = { item, kind: item.kind, unlock: boundary(item.schedule), due: boundary(item.due, true) };
    if (item.kind === 'interactive_note') {
      Object.assign(entry, localNotes.get(item), { title: item.title.trim() });
      entry.sameLesson = cards.filter((c: any) => c.type === 'note' && c.content_html && lessonMarkerId(c.content_html) === entry.lessonId);
      entry.previous = entry.sameLesson.filter((c: any) => c.status !== 'archived' && c.visible_to_student);
      if (entry.previous.length > 1) throw new Error('Multiple active versions of lesson: ' + entry.lessonId);
      entry.existing = entry.previous.find((c: any) => c.content_html === entry.html && c.title === entry.title);
      entry.action = entry.existing ? 'already_current' : entry.previous.length ? 'would_update' : 'would_assign';
      entry.key = 'note:' + entry.lessonId;
    } else if (item.kind === 'guided_drill') {
      const drill = resolveExact(drills, item.drill);
      if (!drill.is_published) throw new Error('Unpublished drill: ' + item.drill);
      const level = item.level !== undefined ? item.level : profile.proficiency_level;
      const count = item.count ?? drill.question_count;
      const pool = resolvePool(drill.bank_filter, bank).map((q: any) => ({ ...q, qtype: q.type }));
      const resolved = resolveLeveledDrillQids({ pool, questionCount: count, drillQids: drill.question_qids, knownQids, level, rng: () => 0.5 });
      if (resolved.qids.length !== count || resolved.outOfBandUsed > 0 || ['empty', 'out_of_level', 'partially_out_of_level'].includes(resolved.warning ?? '')) throw new Error('Insufficient in-level pool: ' + item.drill);
      const eligible = resolved.source === 'pinned' ? resolved.qids.map(qid => ({ difficulty: bank.get(qid)?.questionDifficulty })) : level ? pool.filter((q: any) => isInBand(q.difficulty, levelBand(level))) : pool;
      if (item.max_difficulty != null && eligible.some((q: any) => !Number.isFinite(q.difficulty) || q.difficulty > item.max_difficulty)) throw new Error('Drill pool exceeds difficulty ceiling: ' + item.drill);
      Object.assign(entry, { drill, title: drill.title, level, count, pool_count: pool.length, difficulty_min: Math.min(...eligible.map((q: any) => q.difficulty)), difficulty_max: Math.max(...eligible.map((q: any) => q.difficulty)), sourceTable: 'guided_drill_assignments', assignable: { kind: 'guided_drill', drillId: drill.id } });
      const prior = priorGuided.filter((a: any) => a.guided_drill_id === drill.id && a.scheduled_for === item.schedule);
      if (prior.length > 1) throw new Error('Multiple existing guided assignments: ' + item.drill);
      if (prior.length) {
        entry.assignment = prior[0];
        if (entry.assignment.question_qids?.length || entry.assignment.level !== level || entry.assignment.question_count !== (item.count ?? null) || !sameTime(entry.assignment.unlock_at, entry.unlock)) throw new Error('Existing guided assignment conflicts: ' + entry.assignment.id);
        entry.existing = oneVisible(cards.filter((c: any) => c.source_table === entry.sourceTable && c.source_id === entry.assignment.id), item.drill);
        checkCard(entry.existing, entry, student.class_id);
      }
      entry.key = 'guided:' + drill.id + ':' + item.schedule;
    } else if (item.kind === 'activity') {
      const lookup = item.activity;
      const activity = resolveActivity(activities, lookup);
      if (activity.is_published === false) throw new Error('Unpublished activity: ' + lookup);
      Object.assign(entry, { title: activity.title, sourceTable: 'activity_assignments', assignable: { kind: 'activity', activityId: activity.id } });
      const prior = priorActivities.filter((a: any) => a.activity_id === activity.id);
      const candidates = activityCandidates(cards, new Set(prior.map((a: any) => a.id)), entry.unlock, entry.due);
      if (candidates.length) {
        entry.existing = oneVisible(candidates, lookup);
        entry.assignment = prior.find((a: any) => a.id === entry.existing.source_id);
        checkCard(entry.existing, entry, student.class_id);
        entry.title = entry.existing.title;
      } else if (prior.some((a: any) => !cards.some((c: any) => c.source_table === entry.sourceTable && c.source_id === a.id))) throw new Error('Orphan activity assignment exists; inspect before assigning');
      entry.key = 'activity:' + activity.id + ':' + (item.schedule ?? 'immediate');
    } else {
      const bootcamp = resolveExact(BOOTCAMPS, item.bootcamp);
      if (item.conditional_target && bootcamp.id !== 'conditionals') throw new Error('Conditional target requires conditionals bootcamp');
      const conditional = bootcamp.id === 'conditionals' ? await resolveConditionalAssignment(item.conditional_target) : null;
      Object.assign(entry, { title: conditional?.title ?? bootcamp.title, route: conditional?.route ?? bootcamp.route, sourceTable: 'bootcamps', assignable: { kind: 'bootcamp', topicId: bootcamp.id, ...(conditional ? { conditionalTarget: conditional.target } : {}) } });
      const candidates = cards.filter((c: any) => c.source_table === 'bootcamps' && c.source_id === entry.route && c.status !== 'archived' && sameTime(c.unlock_at, entry.unlock));
      if (candidates.length) { entry.existing = oneVisible(candidates, item.bootcamp); checkCard(entry.existing, entry, student.class_id); }
      entry.key = 'bootcamp:' + entry.route + ':' + (item.schedule ?? 'immediate');
    }
    if (resolvedKeys.has(entry.key)) throw new Error('Duplicate resolved item in plan: ' + entry.title);
    resolvedKeys.add(entry.key);
    entry.action ??= entry.existing ? 'already_assigned' : 'would_assign';
    prepared.push(entry);
  }
  if (verifyOnly) assertExistingOnly(prepared);
  // All items are resolved and checked before this first possible write.
  for (const entry of prepared) {
    const summary: any = { kind: entry.kind, title: entry.title, action: entry.action, day: entry.item.schedule ?? null, due: entry.item.due ?? null, ...(entry.kind === 'guided_drill' ? { slug: entry.drill.slug, level: entry.level, count: entry.count, pool_count: entry.pool_count, difficulty_min: entry.difficulty_min, difficulty_max: entry.difficulty_max } : {}) };
    if (entry.existing) { completed.push({ ...summary, assignment_id: entry.assignment?.id ?? null, classroom_item_id: entry.existing.id, verified: true, notification: 'not_resent', ...(entry.sha256 ? { html_sha256: entry.sha256 } : {}) }); continue; }
    if (dryRun) { completed.push({ ...summary, verified: false }); continue; }
    if (entry.kind === 'interactive_note') {
      const key = 'interactive-' + createHash('sha256').update(student.class_id).update(entry.lessonId).update(entry.title).update(entry.html).update(String(entry.sameLesson.filter((c: any) => c.status === 'archived').length)).digest('hex').slice(0, 48);
      const saved = await query(supabase.rpc('mcp_post_classroom_note', { p_student_id: student.class_id, p_title: entry.title, p_content_html: entry.html, p_idempotency_key: key, p_description: `Interactive lesson [${entry.lessonId}]: ${entry.title}`, p_notify: true } as any));
      if (!saved?.ok || !saved.item_id) throw new Error('Note RPC did not confirm save');
      const outcome: any = { ...summary, action: 'posted', classroom_item_id: saved.item_id, notify: saved, html_sha256: entry.sha256, verified: false };
      completed.push(outcome);
      const card = await query(supabase.from('classroom_items').select('*').eq('id', saved.item_id).eq('student_id', student.class_id).single());
      if (!card.visible_to_student || card.status === 'archived' || card.title !== entry.title || card.content_html !== entry.html) throw new Error('Note byte/visibility verification failed; old version left visible');
      outcome.archived_previous = [];
      for (const old of entry.previous) if (old.id !== card.id) { await query(supabase.from('classroom_items').update({ status: 'archived', visible_to_student: false }).eq('id', old.id).eq('student_id', student.class_id)); outcome.archived_previous.push(old.id); }
      const active = await allRows('classroom_items', q => q.eq('student_id', student.class_id).eq('type', 'note').eq('visible_to_student', true).neq('status', 'archived'));
      const matching = active.filter((c: any) => c.content_html && lessonMarkerId(c.content_html) === entry.lessonId);
      if (active.length >= 10000 || matching.length !== 1 || matching[0].id !== card.id) throw new Error('Exactly one active lesson could not be verified');
      outcome.verified = true;
    } else {
      const priorBellIds = entry.kind === 'bootcamp' ? new Set((await query(supabase.from('notifications').select('id').eq('user_id', student.class_id).eq('type', 'assignment').eq('link', entry.route))).map((n: any) => n.id)) : null;
      const result = await assignWork({ teacherId: auth.user.id, studentIds: [student.class_id], item: entry.assignable, ...(entry.item.schedule ? { scheduledForLocalDate: entry.item.schedule } : {}), ...(entry.kind === 'guided_drill' ? { levelOverrides: { [student.class_id]: entry.level }, questionCountOverride: entry.item.count ?? null } : {}), overrides: { dueAt: entry.due, metadata: { work_plan: plan.id ?? null } } });
      if (result.failed.length || result.ok.length !== 1) throw new Error('Assignment failed; inspect state before retry: ' + (result.failed[0]?.error ?? entry.title));
      const saved = result.ok[0];
      const outcome: any = { ...summary, action: 'assigned', assignment_id: saved.assignmentId ?? null, classroom_item_id: saved.classroomItemId, route: saved.route, notify: saved.notify, verified: false };
      completed.push(outcome);
      if (!saved.classroomItemId) throw new Error('Assignment returned no Classroom ID');
      const card = await query(supabase.from('classroom_items').select('*').eq('id', saved.classroomItemId).single());
      checkCard(card, entry, student.class_id);
      if (card.source_table !== entry.sourceTable || card.source_id !== (entry.kind === 'bootcamp' ? entry.route : saved.assignmentId)) throw new Error('Assignment source verification failed');
      if (entry.kind !== 'bootcamp') {
        const row = await query(supabase.from(entry.sourceTable).select('*').eq('id', saved.assignmentId!).single());
        if (row.student_id !== student.class_id || (entry.kind === 'guided_drill' ? row.guided_drill_id !== entry.drill.id || row.level !== entry.level || row.question_count !== (entry.item.count ?? null) || row.scheduled_for !== entry.item.schedule || !sameTime(row.unlock_at, entry.unlock) : row.activity_id !== entry.assignable.activityId)) throw new Error('Assignment row verification failed');
      }
      if (saved.notify?.bell_ok) {
        const bells = await query(supabase.from('notifications').select('id').eq('user_id', student.class_id).eq('type', 'assignment').eq('link', saved.route!));
        const newBells = priorBellIds ? bells.filter((n: any) => !priorBellIds.has(n.id)) : bells;
        if (newBells.length !== 1) throw new Error('New bell count differs for ' + saved.classroomItemId);
        outcome.bell_count = newBells.length;
      }
      outcome.verified = true;
    }
  }
  return { plan_id: plan.id ?? null, student: student.display_name, student_id: student.class_id, dry_run: dryRun, verify_existing: verifyOnly, results: completed, metrics: { sign_ins: 1, student_lookups: 1, bank_reads: needsGuided ? 1 : 0, planned: prepared.length, assigned: completed.filter(r => r.action === 'assigned' || r.action === 'posted').length, elapsed_ms: Math.round(performance.now() - started) } };
}
main().then(result => console.log('LSATU_WORK_RESULT=' + JSON.stringify(result))).catch(error => { console.error('LSATU_WORK_ERROR=' + JSON.stringify({ error: error?.message ?? String(error), completed_results: completed, instruction: 'Inspect saved IDs before retrying. Never replay notification failures automatically.' })); process.exitCode = 1; });
