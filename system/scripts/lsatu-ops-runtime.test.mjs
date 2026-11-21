import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import crypto from 'node:crypto';
import { confined, prepareSource, validateInvocation, runtimeConfig, runtimeFailure, cacheKey, RUNTIME_CACHE_PROFILE, sparseSetupCommands, unexpectedPaths, verifiedArtifacts, acquireLock } from './lsatu-ops-runtime.mjs';

test('confines paths and accepts only safe generated filenames and single-line arguments', () => {
  const root = path.resolve('vault');
  assert.equal(confined(root, 'system/script.ts'), path.join(root, 'system/script.ts'));
  assert.throws(() => confined(root, '../outside.ts'));
  assert.throws(() => confined(root, path.resolve('outside.ts')));
  validateInvocation('assignment-plan.generated.ts', ['--json', '{"ok":true}']);
  for (const name of ['../escape.generated.ts', 'plain.ts', 'a/b.generated.ts']) assert.throws(() => validateInvocation(name, []));
  assert.throws(() => validateInvocation('a.generated.ts', ['hello\n--dry-run']));
});

test('replaces one literal vault placeholder without interpreting Windows escapes', () => {
  const root = 'C:\\Users\\Example\\vault';
  assert.equal(prepareSource("const root = '__VAULT_ROOT__';", root), `const root = ${JSON.stringify(root)};`);
  assert.equal(prepareSource('const value = 1;', root), 'const value = 1;');
  assert.throws(() => prepareSource("'__VAULT_ROOT__' + '__VAULT_ROOT__'", root));
  assert.throws(() => prepareSource('"__VAULT_ROOT__"', root));
});

test('isolated config uses app env and ops alias, never the app Vite plugin', () => {
  const config = runtimeConfig('/cache/commit', '/projects/lsatu');
  assert.match(config, /plugins: \[\]/);
  assert.match(config, /envDir: "\/projects\/lsatu"/);
  assert.match(config, /\/cache\/commit/);
  assert.doesNotMatch(config, /mcpPlugin|vite.config/);
});

test('cold checkout materializes runtime directories without the public question banks', () => {
  const commands = sparseSetupCommands('/app', '/cache/commit', 'abc123');
  assert.deepEqual(commands, [
    { cwd: '/app', args: ['worktree', 'add', '-q', '--detach', '--no-checkout', '/cache/commit', 'abc123'] },
    { cwd: '/cache/commit', args: ['sparse-checkout', 'set', '--cone', 'src', 'scripts'] },
    { cwd: '/cache/commit', args: ['checkout', '-q', '--detach', 'abc123'] },
  ]);
  assert.equal(commands.some(command => command.args.includes('public')), false);
});

test('sparse cache profile preserves old full checkouts under their previous names', () => {
  const commit = 'a'.repeat(40);
  assert.equal(RUNTIME_CACHE_PROFILE, 'sparse-v1');
  assert.equal(cacheKey(commit), `sparse-v1-${commit}`);
  assert.notEqual(cacheKey(commit), commit);
  assert.throws(() => cacheKey('../other'));
});

test('dirty cache detection permits only explicit untracked runtime artifacts', () => {
  const allowed = new Set(['scripts/.a.generated.ts', 'node_modules']);
  assert.deepEqual(unexpectedPaths('?? scripts/.a.generated.ts\0?? node_modules\0', allowed), []);
  assert.deepEqual(unexpectedPaths(' M supabase/functions/mcp/index.ts\0?? notes.txt\0', allowed), ['supabase/functions/mcp/index.ts', 'notes.txt']);
  assert.deepEqual(unexpectedPaths('R  new.ts\0old.ts\0', allowed), ['new.ts']);
});

test('cached generated artifacts are reusable only while their recorded bytes match', async () => {
  const dir = await fs.mkdtemp(path.join(os.tmpdir(), 'lsatu-artifact-test-'));
  await fs.mkdir(path.join(dir, 'scripts'));
  const name = 'scripts/.a.generated.ts';
  await fs.writeFile(path.join(dir, name), 'original');
  const manifest = { [name]: crypto.createHash('sha256').update('original').digest('hex') };
  assert.equal((await verifiedArtifacts(dir, manifest)).has(name), true);
  await fs.writeFile(path.join(dir, name), 'another session edited this');
  assert.equal((await verifiedArtifacts(dir, manifest)).has(name), false);
  assert.equal((await verifiedArtifacts(dir, {})).has(name), false);
});

test('post-execution errors retain completed IDs and all runtime evidence', () => {
  const result = { stdout: 'LSATU_ASSIGNMENT_RESULT={"saved_ids":["saved-1"]}', stderr: '', ops_commit: 'abc', ops_path: '/runtime', cache_hit: true, timings: { total_ms: 1 } };
  const cause = new Error('cleanup failed');
  const error = runtimeFailure('Unexpected tracked edits', cause, result);
  assert.equal(error.stdout, result.stdout);
  assert.equal(error.runtime_result, result);
  assert.equal(error.ops_path, '/runtime');
  assert.equal(error.cause, cause);
});

test('lock serializes callers, bounds waiting and recovers only dead owners', async () => {
  const dir = await fs.mkdtemp(path.join(os.tmpdir(), 'lsatu-runtime-test-'));
  const file = path.join(dir, 'runtime.lock');
  const release = await acquireLock(file);
  await assert.rejects(acquireLock(file, { waitMs: 15, pollMs: 5 }), /busy/);
  let acquired = false;
  const next = acquireLock(file, { waitMs: 1000, pollMs: 5 }).then(unlock => { acquired = true; return unlock; });
  assert.equal(acquired, false);
  await release();
  await (await next)();
  await fs.writeFile(file, JSON.stringify({ pid: 999999, token: 'dead' }));
  await (await acquireLock(file, { isAlive: () => false }))();
  await fs.writeFile(file, JSON.stringify({ pid: 999999, token: 'dead' }));
  await fs.writeFile(file + '.reaping', JSON.stringify({ pid: 999998, token: 'dead-reaper' }));
  await (await acquireLock(file, { waitMs: 1000, pollMs: 5, isAlive: () => false }))();
  await fs.writeFile(file, 'partial lock');
  await assert.rejects(acquireLock(file, { waitMs: 10, pollMs: 5, isAlive: () => false }), /busy/);
  assert.equal(await fs.readFile(file, 'utf8'), 'partial lock');
  // Temporary fixtures are intentionally preserved; production files are never removed by tests.
});
