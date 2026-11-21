import fs from 'node:fs';
import path from 'node:path';

export function validDay(day) {
  if (typeof day !== 'string' || !/^\d{4}-\d{2}-\d{2}$/.test(day)) return false;
  const [y, m, d] = day.split('-').map(Number);
  const date = new Date(Date.UTC(y, m - 1, d));
  return date.getUTCFullYear() === y && date.getUTCMonth() + 1 === m && date.getUTCDate() === d;
}
export function boundary(day, end = false) {
  if (day == null) return null;
  if (!validDay(day)) throw new Error('Invalid calendar date: ' + day);
  if (process.env.TZ !== 'America/Toronto') throw new Error('Runner must use America/Toronto timezone');
  return new Date(day + (end ? 'T23:59:59' : 'T00:00:00')).toISOString();
}
export function sameTime(left, right) {
  return left == null || right == null ? left == null && right == null : new Date(left).toISOString() === right;
}
export function validatePlan(plan) {
  if (typeof plan?.student !== 'string' || !plan.student.trim() || !Array.isArray(plan.assignments) || plan.assignments.length < 1 || plan.assignments.length > 20) throw new Error('Provide one student and 1-20 assignments');
  if (plan.id != null && (typeof plan.id !== 'string' || !/^[a-zA-Z0-9][a-zA-Z0-9_-]{0,99}$/.test(plan.id))) throw new Error('Invalid plan id');
  const allowed = { guided_drill: 'drill', activity: 'activity', bootcamp: 'bootcamp', interactive_note: 'html_file' };
  const keys = new Set();
  for (const item of plan.assignments) {
    const field = allowed[item?.kind];
    if (!field || typeof item[field] !== 'string' || !item[field].trim()) throw new Error('Invalid assignment kind or identifier');
    if (item.kind === 'interactive_note') {
      if (typeof item.title !== 'string' || !item.title.trim() || item.title.length > 300) throw new Error('Note needs title');
      if (item.schedule != null || item.due != null) throw new Error('Interactive notes publish immediately; omit schedule/due');
    } else {
      if (item.kind === 'guided_drill' && (!item.schedule || !item.due)) throw new Error('Guided drills require schedule and due dates');
      for (const key of ['schedule', 'due']) if (item[key] != null && !validDay(item[key])) throw new Error('Invalid calendar date');
      if (item.schedule && item.due && item.due < item.schedule) throw new Error('Due date precedes schedule');
    }
    if (item.level != null && !['beginner', 'intermediate', 'advanced'].includes(item.level)) throw new Error('Invalid level');
    if (item.count != null && (!Number.isInteger(item.count) || item.count < 1 || item.count > 50)) throw new Error('Invalid question count');
    if (item.max_difficulty != null && (!Number.isInteger(item.max_difficulty) || item.max_difficulty < 1 || item.max_difficulty > 5)) throw new Error('Invalid difficulty ceiling');
    const key = JSON.stringify([item.kind, item[field], item.schedule ?? null, item.conditional_target ?? null]);
    if (keys.has(key)) throw new Error('Duplicate item in plan');
    keys.add(key);
  }
  return plan;
}
export function confinedFile(root, input, extension) {
  const resolved = fs.realpathSync(path.resolve(root, input));
  const relative = path.relative(fs.realpathSync(root), resolved);
  if (relative.startsWith('..') || path.isAbsolute(relative) || path.extname(resolved).toLowerCase() !== extension) throw new Error('File must remain inside workspace: ' + input);
  return resolved;
}
export function resolveExact(rows, needle, fields = ['id', 'slug', 'title']) {
  const key = needle.trim().toLowerCase();
  const hits = rows.filter(row => fields.some(field => typeof row[field] === 'string' && row[field].toLowerCase() === key));
  if (hits.length !== 1) throw new Error('Catalog item missing or ambiguous: ' + needle);
  return hits[0];
}
export function resolveActivity(rows, needle) {
  const key = needle.trim().toLowerCase();
  if (['general conditionals', 'general-conditionals'].includes(key)) {
    const stableId = '7946f46b-e7f8-4c60-b405-4ece9c409deb';
    if (!rows.some(row => row.id === stableId)) throw new Error('Legacy General Conditionals activity is absent from live catalog');
    return resolveExact(rows, stableId);
  }
  return resolveExact(rows, needle);
}
export function oneVisible(cards, label) {
  if (cards.length !== 1 || !cards[0].visible_to_student || cards[0].status === 'archived') throw new Error('Expected exactly one visible Classroom item: ' + label);
  return cards[0];
}
export function assertExistingOnly(prepared) {
  const missing = prepared.filter(entry => entry.action !== 'already_assigned' && entry.action !== 'already_current');
  if (missing.length) throw new Error('verify-existing refuses mutations: ' + missing.map(entry => entry.title).join(', '));
}
export function activityCandidates(cards, assignmentIds, unlock, due) {
  const related = cards.filter(card => card.source_table === 'activity_assignments' && assignmentIds.has(card.source_id) && card.status !== 'archived' && sameTime(card.unlock_at, unlock));
  const conflicting = related.filter(card => !['completed', 'done'].includes(card.status) && !sameTime(card.due_at, due));
  if (conflicting.length) throw new Error('Active activity assignment conflicts with requested due date: ' + conflicting.map(card => card.id).join(', '));
  return related.filter(card => sameTime(card.due_at, due));
}
