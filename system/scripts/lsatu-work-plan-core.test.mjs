import test from 'node:test';
import assert from 'node:assert/strict';
import { validDay, boundary, validatePlan, resolveExact, resolveActivity, assertExistingOnly, oneVisible, sameTime, activityCandidates } from './lsatu-work-plan-core.mjs';
process.env.TZ = 'America/Toronto';
const plan = assignments => ({ student: 'student@example.com', assignments });
test('Gregorian dates and Toronto daylight saving boundaries', () => {
  assert.equal(validDay('2026-02-29'), false);
  assert.equal(validDay('2028-02-29'), true);
  assert.equal(validDay('2026-04-31'), false);
  assert.equal(boundary('2026-03-08'), '2026-03-08T05:00:00.000Z');
  assert.equal(boundary('2026-03-08', true), '2026-03-09T03:59:59.000Z');
  assert.equal(boundary('2026-11-01'), '2026-11-01T04:00:00.000Z');
  assert.equal(boundary('2026-11-01', true), '2026-11-02T04:59:59.000Z');
  assert.equal(boundary(undefined), null);
});
test('all entries validate before work, mixed kinds and explicit guided dates', () => {
  assert.throws(() => validatePlan(plan([{ kind: 'activity', activity: 'x' }, { kind: 'guided_drill', drill: 'y' }])));
  assert.throws(() => validatePlan(plan([{ kind: 'activity', activity: 'x', schedule: '2026-04-31' }])));
  assert.throws(() => validatePlan(plan([{ kind: 'guided_drill', drill: 'x', schedule: '2026-10-25', due: '2026-10-24' }])));
  assert.throws(() => validatePlan(plan([{ kind: 'interactive_note', html_file: 'x.html', title: 'x', due: '2026-10-25' }])));
  assert.throws(() => validatePlan(plan(Array.from({ length: 21 }, (_, i) => ({ kind: 'activity', activity: String(i) })))));
  assert.equal(validatePlan(plan([{ kind: 'activity', activity: 'x' }, { kind: 'bootcamp', bootcamp: 'y' }, { kind: 'interactive_note', title: 'z', html_file: 'z.html' }])).assignments.length, 3);
});
test('duplicate or ambiguous references fail rather than guessing', () => {
  assert.throws(() => validatePlan(plan([{ kind: 'activity', activity: 'x' }, { kind: 'activity', activity: 'x' }])));
  assert.throws(() => resolveExact([{ id: '1', title: 'Same' }, { id: '2', title: 'Same' }], 'same'));
  assert.equal(resolveExact([{ id: '1', title: 'Same' }], '1').title, 'Same');
  assert.throws(() => oneVisible([{ id: 'a', visible_to_student: true }, { id: 'b', visible_to_student: true }], 'duplicate'));
  assert.throws(() => oneVisible([{ id: 'a', status: 'archived', visible_to_student: true }], 'archived'));
});
test('verify-existing refuses any possible writer action and accepts completed work', () => {
  assert.throws(() => assertExistingOnly([{ action: 'would_assign', title: 'new' }]), /refuses mutations/);
  assert.throws(() => assertExistingOnly([{ action: 'already_assigned' }, { action: 'would_update', title: 'new bytes' }]), /refuses mutations/);
  assert.doesNotThrow(() => assertExistingOnly([{ action: 'already_assigned', status: 'completed' }, { action: 'already_current' }]));
  assert.equal(sameTime(null, null), true);
  assert.equal(sameTime(null, '2026-10-25T04:00:00Z'), false);
});
test('legacy activity label resolves only the verified live identity', () => {
  const live = { id: '7946f46b-e7f8-4c60-b405-4ece9c409deb', title: 'Conditional Rephrase', slug: 'conditional-rephrase' };
  assert.equal(resolveActivity([live], 'General Conditionals'), live);
  assert.equal(resolveActivity([live], 'general-conditionals'), live);
  assert.equal(resolveActivity([live], 'conditional-rephrase'), live);
  assert.throws(() => resolveActivity([{ id: 'other', title: 'General Conditionals' }], 'General Conditionals'), /absent from live/);
});
test('activity identity preserves historical completions and frozen titles', () => {
  const due = boundary('2026-11-01', true);
  const base = { source_table: 'activity_assignments', source_id: 'assignment', unlock_at: null, visible_to_student: true };
  const old = { ...base, id: 'old', status: 'completed', due_at: boundary('2026-10-01', true), title: 'Old name' };
  const current = { ...base, id: 'current', status: 'assigned', due_at: due, title: 'Frozen name' };
  assert.deepEqual(activityCandidates([old, current], new Set(['assignment']), null, due), [current]);
  assert.deepEqual(activityCandidates([{ ...current, status: 'completed' }], new Set(['assignment']), null, due).map(c => c.title), ['Frozen name']);
  assert.throws(() => activityCandidates([{ ...old, status: 'assigned' }, current], new Set(['assignment']), null, due), /conflicts with requested due/);
});
