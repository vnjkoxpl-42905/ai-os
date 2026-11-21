import test from 'node:test';
import assert from 'node:assert/strict';
import { reschedulePlan } from './lsatu-reschedule-plan.mjs';

process.env.TZ = 'America/Toronto';

const owner = '37fc00a6-3c8a-4785-b005-fa277c72cbca';
const ids = ['e8db2765-86f2-4a0d-805a-93e6d1261ca0', '66fcdc93-855a-43b9-85a8-f80a9d4d4611'];
const sources = ['85452492-d37a-48f7-a86f-6d1900c046cb', 'bcb3668b-e72e-411d-9c7e-8df2675c3796'];
const old = { unlock_at: '2026-10-26T04:00:00+00:00', due_at: '2026-11-02T04:59:59+00:00' };
const plan = () => ({ id: 'test-reschedule', student: 'ore@example.com', student_id: owner, student_folder: 'students/ore', items: ids.map((card_id, index) => ({ card_id, type: index ? 'activity' : 'drill', source_id: sources[index], source_table: index ? 'activity_assignments' : 'guided_drill_assignments', expected: { ...old, status: 'assigned', ...(index ? {} : { scheduled_for: '2026-10-26', source_unlock_at: old.unlock_at }) }, schedule: index ? '2026-10-30' : '2026-10-28', due: index ? '2026-10-31' : '2026-10-29' })) });
function fixture(hook = () => {}) {
  const p = plan();
  const db = { classroom_items: p.items.map(item => ({ id: item.card_id, student_id: owner, type: item.type, source_id: item.source_id, source_table: item.source_table, status: 'assigned', visible_to_student: true, ...old, metadata_json: { progress: 0 } })), guided_drill_assignments: [{ id: sources[0], student_id: owner, status: 'assigned', scheduled_for: '2026-10-26', unlock_at: old.unlock_at, question_count: 7, question_ids: null }] };
  let patches = 0;
  const audits = [];
  const rest = async (query, init = {}) => {
    const [table, params] = query.split('?');
    const filter = new URLSearchParams(params);
    const found = db[table].filter(row => [...filter].every(([key, value]) => key === 'select' || (value === 'is.null' ? row[key] == null : String(row[key]) === value.slice(3))));
    await hook({ table, filter, init, db, patches, found });
    if (init.method === 'PATCH') { patches++; for (const row of found) Object.assign(row, JSON.parse(init.body)); }
    return structuredClone(found);
  };
  return { p, db, rest, audit: async report => { audits.push(report); }, audits, patches: () => patches };
}
test('dry run preflights all records without writes', async () => { const f = fixture(); const r = await reschedulePlan(f.p, { ...f, dryRun: true }); assert.equal(r.status, 'dry_run_verified'); assert.equal(r.preflight.length, 2); assert.equal(f.patches(), 0); });
test('later preflight identity conflict causes zero writes', async () => { const f = fixture(); f.db.classroom_items[1].source_id = sources[0]; await assert.rejects(reschedulePlan(f.p, f), /Identity/); assert.equal(f.patches(), 0); assert.ok(f.audits.at(-1).error); });
test('Toronto boundaries, preserved status/configuration, and idempotence', async () => { const f = fixture(); const r = await reschedulePlan(f.p, f); assert.equal(r.status, 'verified'); assert.equal(f.db.classroom_items[0].unlock_at, '2026-10-28T04:00:00.000Z'); assert.equal(f.db.classroom_items[1].due_at, '2026-11-01T03:59:59.000Z'); assert.equal(f.db.guided_drill_assignments[0].question_count, 7); assert.equal(f.db.classroom_items[0].status, 'assigned'); const count = f.patches(); const again = await reschedulePlan(f.p, f); assert.equal(again.writes.length, 0); assert.equal(f.patches(), count); });
test('CAS conflict rolls back only completed writes', async () => { const f = fixture(({ table, init, patches, found }) => { if (init.method === 'PATCH' && table === 'classroom_items' && patches === 1) found.splice(0); }); await assert.rejects(reschedulePlan(f.p, f), /Compare-and-swap/); assert.equal(f.audits.at(-1).rollback[0].status, 'rolled_back'); assert.equal(f.db.guided_drill_assignments[0].scheduled_for, '2026-10-26'); });
test('partial failure will not overwrite intervening progress', async () => { const f = fixture(({ table, init, patches, db }) => { if (init.method === 'PATCH' && table === 'classroom_items' && patches === 1) { db.guided_drill_assignments[0].status = 'completed'; throw new Error('simulated failure'); } }); await assert.rejects(reschedulePlan(f.p, f), /unresolved_partial_state/); assert.equal(f.db.guided_drill_assignments[0].status, 'completed'); assert.equal(f.audits.at(-1).rollback[0].status, 'unresolved'); assert.equal(f.audits.at(-1).writes[0].before.id, sources[0]); });
test('invalid Gregorian day is rejected before any reads/writes', async () => { const f = fixture(); f.p.items[0].due = '2026-02-30'; await assert.rejects(reschedulePlan(f.p, f), /Invalid Toronto/); assert.equal(f.patches(), 0); });
