import test from 'node:test';
import assert from 'node:assert/strict';
import { formatLocalDay } from './lsatu-calendar.mjs';
test('formats local due days across DST without taking the UTC date slice', () => {
 assert.equal(formatLocalDay('2026-11-02T04:59:59+00:00'), '2026-11-01');
 assert.equal(formatLocalDay('2026-10-26T03:59:59Z'), '2026-10-25');
 assert.equal(formatLocalDay('2026-11-02T05:00:00Z'), '2026-11-02');
 assert.equal(formatLocalDay(null), '-');
 assert.throws(() => formatLocalDay('bad timestamp'), /Invalid/);
});
