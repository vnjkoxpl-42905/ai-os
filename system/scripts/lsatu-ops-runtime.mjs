import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';
import { execFile } from 'node:child_process';
import { promisify } from 'node:util';
import { createRequire } from 'node:module';
import { performance } from 'node:perf_hooks';
import { vaultRoot, projectsRoot } from './project-paths.mjs';

const run = promisify(execFile);
const delay = ms => new Promise(resolve => setTimeout(resolve, ms));
const options = { windowsHide: true, timeout: 120000, maxBuffer: 8 * 1024 * 1024 };
const generatedConfig = 'scripts/.ai-os-runtime.generated.config.mjs';
export const RUNTIME_CACHE_PROFILE = 'sparse-v1';
const sha256 = value => crypto.createHash('sha256').update(value).digest('hex');

export function cacheKey(commit) {
  if (!/^[a-f0-9]{40,64}$/.test(commit)) throw new Error('Invalid runtime commit');
  return `${RUNTIME_CACHE_PROFILE}-${commit}`;
}

export function runtimeFailure(message, cause, result) {
  const error = new Error(message, { cause });
  Object.assign(error, result, { runtime_result: result });
  return error;
}

export function sparseSetupCommands(app, ops, commit) {
  return [
    { cwd: app, args: ['worktree', 'add', '-q', '--detach', '--no-checkout', ops, commit] },
    { cwd: ops, args: ['sparse-checkout', 'set', '--cone', 'src', 'scripts'] },
    { cwd: ops, args: ['checkout', '-q', '--detach', commit] },
  ];
}

export async function verifiedArtifacts(ops, artifacts) {
  const allowed = new Set(['node_modules']);
  for (const [name, expected] of Object.entries(artifacts)) {
    if (!(name === generatedConfig || /^scripts\/\.[a-zA-Z0-9._-]+\.generated\.ts$/.test(name))) continue;
    try { if (sha256(await fs.readFile(path.join(ops, name))) === expected) allowed.add(name); }
    catch (error) { if (error.code !== 'ENOENT') throw error; }
  }
  return allowed;
}

export function confined(root, candidate) {
  const resolved = path.resolve(root, candidate);
  const relative = path.relative(root, resolved);
  if (relative === '..' || relative.startsWith('..' + path.sep) || path.isAbsolute(relative)) throw new Error('Source must be inside the vault');
  return resolved;
}

export function prepareSource(source, root) {
  const count = source.split('__VAULT_ROOT__').length - 1;
  if (!count) return source;
  if (count !== 1 || !source.includes("'__VAULT_ROOT__'")) throw new Error('Expected exactly one quoted vault placeholder');
  return source.replace("'__VAULT_ROOT__'", JSON.stringify(root));
}

export function validateInvocation(scriptName, args) {
  if (!/^[a-zA-Z0-9][a-zA-Z0-9._-]*\.generated\.ts$/.test(scriptName)) throw new Error('Use a safe filename ending .generated.ts');
  if (!Array.isArray(args) || args.some(arg => typeof arg !== 'string' || /[\r\n\0]/.test(arg))) throw new Error('Arguments must be single-line strings; use a JSON file for multiline content');
}

export function runtimeConfig(ops, app) {
  // Do not load the app config: its MCP plugin rewrites a tracked Edge Function.
  return `export default { root: ${JSON.stringify(ops)}, envDir: ${JSON.stringify(app)}, resolve: { alias: { '@': ${JSON.stringify(path.join(ops, 'src'))} } }, plugins: [] };\n`;
}

export async function acquireLock(file, { waitMs = 120000, pollMs = 100, isAlive = pid => {
  try { process.kill(pid, 0); return true; } catch (error) { return error.code !== 'ESRCH'; }
} } = {}) {
  const started = performance.now();
  const token = crypto.randomUUID();
  const content = JSON.stringify({ pid: process.pid, token, created: new Date().toISOString() });
  while (true) {
    try {
      const handle = await fs.open(file, 'wx');
      await handle.writeFile(content);
      await handle.close();
      return async () => {
        if (await fs.readFile(file, 'utf8') === content) await fs.unlink(file);
      };
    } catch (error) {
      if (error.code !== 'EEXIST') throw error;
      let previous;
      try { previous = await fs.readFile(file, 'utf8'); } catch (readError) { if (readError.code === 'ENOENT') continue; throw readError; }
      let owner;
      try { owner = JSON.parse(previous); } catch { /* A partial or foreign lock is never removed. */ }
      if (Number.isInteger(owner?.pid) && owner.pid > 0 && !isAlive(owner.pid)) {
        // Serialize reapers so a second stale observer cannot remove a newly acquired lock.
        let reaper;
        const reaperFile = file + '.reaping';
        try {
          reaper = await fs.open(reaperFile, 'wx');
          await reaper.writeFile(content);
        } catch (claimError) {
          if (claimError.code !== 'EEXIST') throw claimError;
          // A killed recovery process must not permanently block subsequent runs.
          let reaperContent;
          try {
            reaperContent = await fs.readFile(reaperFile, 'utf8');
            const reaperOwner = JSON.parse(reaperContent);
            if (Number.isInteger(reaperOwner.pid) && reaperOwner.pid > 0 && !isAlive(reaperOwner.pid)
                && await fs.readFile(reaperFile, 'utf8') === reaperContent) await fs.unlink(reaperFile);
          } catch (reaperError) {
            if (reaperError.code !== 'ENOENT' && !(reaperError instanceof SyntaxError)) throw reaperError;
          }
        }
        if (reaper) {
          try {
            if (await fs.readFile(file, 'utf8') === previous) await fs.unlink(file);
          } catch (unlinkError) { if (unlinkError.code !== 'ENOENT') throw unlinkError; }
          finally { await reaper.close(); if (await fs.readFile(reaperFile, 'utf8') === content) await fs.unlink(reaperFile); }
          continue;
        }
      }
      if (performance.now() - started >= waitMs) throw new Error(`Operational runtime is busy; lock wait exceeded ${waitMs} ms (${file})`);
      await delay(pollMs);
    }
  }
}

export function unexpectedPaths(status, allowed) {
  const entries = status.split('\0').filter(Boolean);
  const unexpected = [];
  for (let index = 0; index < entries.length; index++) {
    const entry = entries[index];
    const code = entry.slice(0, 2);
    const name = entry.slice(3).replaceAll('\\', '/');
    if (code !== '??' || !allowed.has(name)) unexpected.push(name);
    if (/[RC]/.test(code)) index++;
  }
  return unexpected;
}

/** Run a vault-owned TypeScript operation against an isolated immutable main checkout. */
export async function executeOps({ sourcePath, scriptName, args = [] }) {
  validateInvocation(scriptName, args);
  const started = performance.now();
  const realVault = await fs.realpath(vaultRoot);
  const sourceFile = await fs.realpath(confined(realVault, sourcePath));
  confined(realVault, sourceFile); // Reject a vault symlink escaping the vault.
  const source = prepareSource(await fs.readFile(sourceFile, 'utf8'), realVault);
  const app = path.join(projectsRoot, 'lsatu');
  const cache = path.join(projectsRoot, '.lsatu-automation');
  if (path.relative(realVault, cache).split(path.sep)[0] !== '..') throw new Error('Operational runtime must be outside the vault');
  await fs.mkdir(cache, { recursive: true });
  const release = await acquireLock(path.join(cache, 'runtime.lock'));
  const timings = { lock_ms: Math.round(performance.now() - started) };
  let operationResult;
  let primaryError;
  const git = async (cwd, ...argv) => (await run('git', ['-C', cwd, ...argv], options)).stdout.trim();
  try {
    const fetchStarted = performance.now();
    const stampFile = path.join(cache, 'fetch.json');
    let stamp;
    try { stamp = JSON.parse(await fs.readFile(stampFile, 'utf8')); } catch (error) { if (error.code !== 'ENOENT' && !(error instanceof SyntaxError)) throw error; }
    if (!stamp || stamp.app !== app || Date.now() - stamp.at >= 60000 || stamp.at > Date.now()) {
      await git(app, 'fetch', '-q', 'origin', 'main');
      stamp = { app, at: Date.now() };
      await fs.writeFile(stampFile, JSON.stringify(stamp));
    }
    const commit = await git(app, 'rev-parse', 'origin/main');
    if (!/^[a-f0-9]{40,64}$/.test(commit)) throw new Error('Invalid origin/main commit');
    timings.fetch_ms = Math.round(performance.now() - fetchStarted);
    const setupStarted = performance.now();
    const relativeScript = 'scripts/.' + scriptName;
    let ops = path.join(cache, cacheKey(commit));
    let cacheHit = false;
    let artifacts = {};
    const artifactFile = target => path.join(cache, path.basename(target) + '.artifacts.json');
    try {
      await fs.access(path.join(ops, '.git'));
      try { artifacts = JSON.parse(await fs.readFile(artifactFile(ops), 'utf8')); } catch (error) { if (error.code !== 'ENOENT' && !(error instanceof SyntaxError)) throw error; }
      const head = await git(ops, 'rev-parse', 'HEAD');
      const status = (await run('git', ['-C', ops, 'status', '--porcelain', '-z', '--untracked-files=all'], options)).stdout;
      const allowed = await verifiedArtifacts(ops, artifacts);
      let artifactsClean = Object.keys(artifacts).every(name => allowed.has(name));
      for (const name of [relativeScript, generatedConfig]) {
        try { await fs.access(path.join(ops, name)); if (!allowed.has(name)) artifactsClean = false; }
        catch (error) { if (error.code !== 'ENOENT') throw error; }
      }
      if (head === commit && artifactsClean && unexpectedPaths(status, allowed).length === 0) cacheHit = true;
      else ops += '-' + crypto.randomUUID(); // Preserve dirty checkouts in full.
    } catch (error) { if (error.code !== 'ENOENT') throw error; }
    if (!cacheHit) {
      artifacts = {};
      // Question banks under public are fetched by the engine from the deployed site.
      // Materialize only the runtime code and root configuration/package files.
      for (const command of sparseSetupCommands(app, ops, commit)) await git(command.cwd, ...command.args);
    }
    const modules = path.join(ops, 'node_modules');
    try { await fs.access(modules); } catch (error) {
      if (error.code !== 'ENOENT') throw error;
      await fs.access(path.join(app, 'node_modules'));
      await fs.symlink(path.join(app, 'node_modules'), modules, process.platform === 'win32' ? 'junction' : 'dir');
    }
    if (await fs.realpath(modules) !== await fs.realpath(path.join(app, 'node_modules'))) throw new Error(`Unexpected dependency link; preserved: ${modules}`);
    if (await git(ops, 'ls-files', '--', relativeScript, generatedConfig)) throw new Error('Generated runtime filenames collide with tracked app files');
    await fs.mkdir(path.join(ops, 'scripts'), { recursive: true });
    await fs.writeFile(path.join(ops, relativeScript), source);
    const config = runtimeConfig(ops, app);
    await fs.writeFile(path.join(ops, generatedConfig), config);
    artifacts[relativeScript] = sha256(source);
    artifacts[generatedConfig] = sha256(config);
    await fs.writeFile(artifactFile(ops), JSON.stringify(artifacts));
    const require = createRequire(path.join(ops, 'package.json'));
    const vite = path.join(path.dirname(require.resolve('vite-node/package.json')), 'vite-node.mjs');
    timings.setup_ms = Math.round(performance.now() - setupStarted);
    const executeStarted = performance.now();
    let result;
    let executionError;
    try {
      result = await run(process.execPath, [vite, '--config', generatedConfig, relativeScript, '--', ...args], { ...options, cwd: ops, env: { ...process.env, TZ: 'America/Toronto' } });
    } catch (error) { executionError = error; }
    timings.execute_ms = Math.round(performance.now() - executeStarted);
    timings.total_ms = Math.round(performance.now() - started);
    operationResult = { stdout: result?.stdout ?? executionError?.stdout ?? '', stderr: result?.stderr ?? executionError?.stderr ?? '', ops_commit: commit, ops_path: ops, cache_hit: cacheHit, source_sha256: sha256(source), timings };
    const tracked = await git(ops, 'status', '--porcelain', '--untracked-files=no');
    if (tracked) throw runtimeFailure(`Unexpected tracked edits in isolated runtime; preserved for inspection: ${ops}\n${tracked}`, executionError, operationResult);
    if (executionError) throw runtimeFailure(executionError.message, executionError, operationResult);
    return operationResult;
  } catch (error) {
    primaryError = operationResult && !error.runtime_result ? runtimeFailure(error.message, error, operationResult) : error;
    throw primaryError;
  } finally {
    try { await release(); }
    catch (error) {
      if (primaryError) primaryError.cleanup_error = error.message;
      else throw runtimeFailure(`Operation completed but runtime lock cleanup failed: ${error.message}`, error, operationResult);
    }
  }
}
