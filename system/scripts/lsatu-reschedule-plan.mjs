import { boundary, validDay } from './lsatu-work-plan-core.mjs';

const sameTime = (a, b) => a == null || b == null ? a == null && b == null : new Date(a).toISOString() === new Date(b).toISOString();
const uuid = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;
const stable = row => JSON.stringify(Object.fromEntries(Object.entries(row).filter(([key]) => !['unlock_at', 'due_at', 'scheduled_for', 'updated_at'].includes(key)).sort(([a], [b]) => a.localeCompare(b))));
const exact = row => JSON.stringify(Object.entries(row).sort(([a], [b]) => a.localeCompare(b)));
const equalField = (key, a, b) => key.endsWith('_at') ? sameTime(a, b) : a === b;
const filter = (key, value) => `${key}=${value == null ? 'is.null' : 'eq.' + encodeURIComponent(value)}`;
function where(row, identity, dates) {
  return [...new Set([...identity, 'status', ...dates, ...(Object.hasOwn(row, 'updated_at') ? ['updated_at'] : [])])].map(key => filter(key, row[key])).join('&');
}

export function validateReschedulePlan(plan) {
  if (!plan || !/^[a-zA-Z0-9][a-zA-Z0-9_-]{0,99}$/.test(plan.id ?? '') || !uuid.test(plan.student_id ?? '') || typeof plan.student !== 'string' || !plan.student.includes('@') || !/^students\/[a-z0-9_-]+$/.test(plan.student_folder ?? '') || !Array.isArray(plan.items) || plan.items.length < 1 || plan.items.length > 20) throw new Error('Provide plan id, exact student email/id/folder and 1-20 items');
  const ids = new Set();
  for (const item of plan.items) {
    if (!uuid.test(item.card_id ?? '') || ids.has(item.card_id) || !['homework', 'activity', 'drill'].includes(item.type) || typeof item.source_id !== 'string' || !item.source_id || typeof item.source_table !== 'string' || !item.expected || !['assigned', 'in_progress'].includes(item.expected.status)) throw new Error('Invalid or duplicate target identity/status');
    ids.add(item.card_id);
    if (item.source_table !== { homework: 'homework_assignments', activity: 'activity_assignments', drill: 'guided_drill_assignments' }[item.type] || !uuid.test(item.source_id)) throw new Error('Source identity/table does not match target kind');
    for (const key of ['unlock_at', 'due_at']) if (!Object.hasOwn(item.expected, key) || (item.expected[key] !== null && !Number.isFinite(Date.parse(item.expected[key])))) throw new Error('Expected old dates required');
    if (!validDay(item.schedule) || !validDay(item.due) || item.due < item.schedule) throw new Error('Invalid Toronto schedule/deadline');
    if (item.type === 'drill' && (!uuid.test(item.source_id) || item.source_table !== 'guided_drill_assignments' || !validDay(item.expected.scheduled_for) || !Object.hasOwn(item.expected, 'source_unlock_at'))) throw new Error('Guided source expected dates required');
  }
}

// Existing-row edits only. The injected REST function uses the admin CLI session.
export async function reschedulePlan(plan, { rest, audit, dryRun = false }) {
  validateReschedulePlan(plan);
  const report = { plan_id: plan.id, student_id: plan.student_id, dry_run: dryRun, notifications: 'none; prior notifications retain their original dates', completion_dependency: false, preflight: [], writes: [], rollback: [], status: 'preflight' };
  const save = () => audit(structuredClone(report));
  const read = async (table, id) => {
    const rows = await rest(`${table}?id=eq.${encodeURIComponent(id)}&student_id=eq.${plan.student_id}&select=*`);
    if (!Array.isArray(rows) || rows.length !== 1) throw new Error(`Expected exactly one owned ${table} row: ${id}`);
    return rows[0];
  };
  const prepared = [];
  try {
    await save();
    for (const item of plan.items) {
      const card = await read('classroom_items', item.card_id);
      if (card.type !== item.type || card.source_id !== item.source_id || card.source_table !== item.source_table || card.status !== item.expected.status || card.visible_to_student !== true) throw new Error(`Identity/status conflict: ${item.card_id}`);
      const target = { unlock_at: boundary(item.schedule), due_at: boundary(item.due, true) };
      const cardOld = ['unlock_at', 'due_at'].every(key => equalField(key, card[key], item.expected[key]));
      const cardNew = Object.keys(target).every(key => equalField(key, card[key], target[key]));
      if (!cardOld && !cardNew) throw new Error(`Date conflict: ${item.card_id}`);
      const rows = [{ table: 'classroom_items', before: card, target, identity: ['id', 'student_id', 'type', 'source_id', 'source_table'] }];
      if (item.type === 'drill') {
        const source = await read('guided_drill_assignments', item.source_id);
        if (source.status !== item.expected.status) throw new Error('Guided source status conflict');
        const sourceTarget = { scheduled_for: item.schedule, unlock_at: target.unlock_at };
        const old = source.scheduled_for === item.expected.scheduled_for && sameTime(source.unlock_at, item.expected.source_unlock_at);
        const current = source.scheduled_for === item.schedule && sameTime(source.unlock_at, target.unlock_at);
        if ((!old && !current) || (cardNew && !cardOld && !current) || (current && !old && !cardNew)) throw new Error('Guided source/card dates conflict');
        rows.unshift({ table: 'guided_drill_assignments', before: source, target: sourceTarget, identity: ['id', 'student_id'] });
      }
      prepared.push(...rows);
      report.preflight.push({ card_id: item.card_id, rows: structuredClone(rows) });
    }
    report.status = dryRun ? 'dry_run_verified' : 'writing';
    await save();
    if (dryRun) return report;
    for (const entry of prepared) {
      const current = await read(entry.table, entry.before.id);
      if (exact(current) !== exact(entry.before)) throw new Error(`Changed after preflight: ${entry.before.id}`);
      if (Object.entries(entry.target).every(([key, value]) => equalField(key, current[key], value))) continue;
      report.pending_write = { table: entry.table, id: current.id, target: entry.target };
      await save();
      const result = await rest(`${entry.table}?${where(current, entry.identity, Object.keys(entry.target))}`, { method: 'PATCH', body: JSON.stringify(entry.target) });
      if (Array.isArray(result) && result.length === 0) { delete report.pending_write; throw new Error(`Compare-and-swap conflict: ${current.id}`); }
      if (!Array.isArray(result) || result.length !== 1) throw new Error(`Unexpected write response; inspect ${current.id}`);
      const after = result[0];
      report.writes.push({ ...entry, after });
      delete report.pending_write;
      await save();
      if (stable(after) !== stable(current) || !Object.entries(entry.target).every(([key, value]) => equalField(key, after[key], value))) throw new Error('Write changed non-schedule fields or did not save requested dates');
    }
    report.readback = [];
    for (const entry of prepared) {
      const saved = await read(entry.table, entry.before.id);
      if (stable(saved) !== stable(entry.before) || !Object.entries(entry.target).every(([key, value]) => equalField(key, saved[key], value))) throw new Error(`Final readback conflict: ${entry.before.id}`);
      report.readback.push({ table: entry.table, row: saved });
    }
    report.status = 'verified';
    await save();
    return report;
  } catch (error) {
    report.error = error.message;
    for (const write of [...report.writes].reverse()) {
      try {
        const current = await read(write.table, write.before.id);
        if (exact(current) !== exact(write.after)) throw new Error('Intervening change; rollback skipped');
        const target = Object.fromEntries(Object.keys(write.target).map(key => [key, write.before[key]]));
        const result = await rest(`${write.table}?${where(current, write.identity, Object.keys(target))}`, { method: 'PATCH', body: JSON.stringify(target) });
        if (!Array.isArray(result) || result.length !== 1 || stable(result[0]) !== stable(write.before) || !Object.entries(target).every(([key, value]) => equalField(key, result[0][key], value))) throw new Error('Rollback compare-and-swap/readback failed');
        report.rollback.push({ id: write.before.id, status: 'rolled_back' });
      } catch (rollbackError) { report.rollback.push({ id: write.before.id, status: 'unresolved', error: rollbackError.message }); }
    }
    report.status = report.pending_write || report.rollback.some(row => row.status === 'unresolved') ? 'unresolved_partial_state' : 'failed_rolled_back';
    await save();
    throw Object.assign(new Error(`${report.error}; ${report.status}`), { report });
  }
}
