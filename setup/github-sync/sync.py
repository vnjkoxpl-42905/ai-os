"""Publish filtered working-tree snapshots without changing the working checkout."""
from __future__ import annotations
import argparse, importlib.util, json, os, re, shutil, subprocess, tempfile
from datetime import datetime, timezone
from contextlib import contextmanager
from pathlib import Path

OWNER = 'vnjkoxpl-42905'
MAX_SIZE = 95 * 1024 * 1024
EXCLUDED_DIRS = {'.git', 'node_modules', '.venv', 'venv', 'dist', '__pycache__', '.cache', '.next', '.nuxt', 'coverage', 'raw', 'credentials', 'secrets'}
EXCLUDED_SUFFIXES = {'.db', '.sqlite', '.sqlite3', '.pem', '.key', '.p12', '.pfx', '.zip', '.bundle', '.7z', '.tar', '.gz', '.log'}
TOKEN_PATTERN = re.compile(rb'(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{40,}|sk-(?:proj-|ant-)?[A-Za-z0-9_-]{30,}|AKIA[A-Z0-9]{16}|AIza[A-Za-z0-9_-]{30,})')
PATTERNS = [('private key', re.compile(rb'-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----')), ('API token', TOKEN_PATTERN)]
ASSIGNMENT = re.compile(rb'''(?im)^\s*["']?[\w.-]*(?:api[_-]?key|secret|password|access[_-]?token|refresh[_-]?token)[\w.-]*["']?\s*[:=]\s*["']?([^\s"',;#}{]+)''')

def run(*args, cwd=None, env=None):
    p = subprocess.run(args, cwd=cwd, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=180)
    if p.returncode:
        raise RuntimeError(f'{args[0]} failed ({p.returncode})')
    return p.stdout.decode('utf-8', errors='replace').strip()

def git(root, *args, env=None):
    environment = os.environ.copy() if env is None else env.copy()
    environment.update(GIT_TERMINAL_PROMPT='0', GCM_INTERACTIVE='never')
    return run('git', '-c', 'core.longpaths=true', '-C', str(root), *args, env=environment)

def long_path(path):
    path = Path(path).absolute()
    text = str(path)
    if os.name == 'nt' and not text.startswith('\\\\?\\'):
        return Path('\\\\?\\UNC\\' + text[2:] if text.startswith('\\\\') else '\\\\?\\' + text)
    return path

def git_path(path):
    """Git's lock-file implementation rejects Win32 extended path prefixes."""
    text = str(path)
    if text.startswith('\\\\?\\UNC\\'): return '\\\\' + text[8:]
    if text.startswith('\\\\?\\'): return text[4:]
    return text

def slug(value):
    return re.sub(r'[^a-z0-9_-]+', '-', value.lower()).strip('-') or 'checkout'

@contextmanager
def process_lock(path):
    """The operating system releases this lock when the process exits or crashes."""
    handle = open(path, 'a+b')
    try:
        handle.seek(0, os.SEEK_END)
        if handle.tell() == 0:
            handle.write(b'0'); handle.flush()
        handle.seek(0)
        try:
            if os.name == 'nt':
                import msvcrt
                msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
            else:
                import fcntl
                fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError:
            yield False
            return
        try:
            yield True
        finally:
            handle.seek(0)
            if os.name == 'nt':
                msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
    finally:
        handle.close()

def is_link(path):
    return path.is_symlink() or bool(getattr(path.lstat(), 'st_file_attributes', 0) & 0x400)

def excluded(path):
    name = path.name.lower()
    if name.startswith('.env'):
        return not (name.endswith('.example') or name.endswith('.template'))
    return (path.suffix.lower() in EXCLUDED_SUFFIXES or name in {'.git', 'auth.json', 'tokens.json', 'credentials.json', 'session.json', 'sessions.json', '.npmrc', '.pypirc'} or name.startswith('id_rsa') or name.startswith('id_ed25519'))

def secret_kind(data):
    for kind, pattern in PATTERNS:
        if pattern.search(data):
            return kind
    for match in ASSIGNMENT.finditer(data):
        value = match.group(1).lower()
        if len(value) < 12 or any(x in value for x in (b'example', b'placeholder', b'changeme', b'your_', b'your-', b'${', b'process.env', b'os.environ', b'<', b'undefined', b'null')):
            continue
        if re.fullmatch(rb'[a-z0-9_./\\-]+', value) and not any(c in value for c in b'0123456789'):
            continue
        return 'credential assignment'
    return None

def initialize_private_project(root, config):
    """Initialize only a new checkout; never stage source or publish its main branch."""
    created_git = not (root / '.git').exists()
    if created_git:
        run('git', 'init', '-b', 'main', str(root))
        with tempfile.TemporaryDirectory(prefix='github-sync-baseline-') as folder:
            staging = Path(folder) / 'files'; staging.mkdir()
            tree = create_tree(root, staging)
            env = os.environ.copy()
            env.update(GIT_AUTHOR_NAME='Local workspace sync', GIT_AUTHOR_EMAIL='sync@localhost', GIT_COMMITTER_NAME='Local workspace sync', GIT_COMMITTER_EMAIL='sync@localhost')
            commit = git(root, 'commit-tree', tree, '-m', 'Initialize local project baseline', env=env)
            git(root, 'update-ref', 'refs/heads/main', commit)
    repository = config.get('owner', OWNER) + '/local-' + slug(root.name)
    # Creation must fail on collision. Do not attach an existing unrelated repository.
    run('gh', 'repo', 'create', repository, '--private', '--source', str(root), '--remote', 'origin')
    verify_private(repository)
    config.setdefault('_created_repositories', []).append(repository)

def copy_filtered(root, destination, max_size=MAX_SIZE):
    root, destination = long_path(root), long_path(destination)
    report = []
    for directory, dirs, files in os.walk(root, followlinks=False):
        current = Path(directory)
        for name in list(dirs):
            path = current / name
            relative = path.relative_to(root)
            reason = None
            if is_link(path): reason = 'link'
            elif name.lower() in EXCLUDED_DIRS: reason = 'excluded directory'
            elif current == root and name.lower() in {'temp', 'tmp', 'scratch', '.firecrawl'}: reason = 'root runtime directory'
            elif relative.as_posix().lower() in {'setup/github-sync/tools', 'setup/github-sync/state', '.cloud-sync', 'system/logs', '.obsidian/cache', '.claude/projects', '.codex/sessions', '.codex/log', '.codex/logs'}: reason = 'generated runtime directory'
            elif (path / '.git').exists(): reason = 'nested repository'
            if reason:
                dirs.remove(name)
                report.append({'path': relative.as_posix(), 'reason': reason})
        for name in files:
            path = current / name
            relative = path.relative_to(root)
            reason = None
            if is_link(path): reason = 'link'
            elif excluded(path): reason = 'excluded file'
            elif relative.parent.as_posix() == '.obsidian' and name.startswith('workspace') and name.endswith('.json'): reason = 'editor runtime state'
            elif path.stat().st_size > max_size: reason = 'GitHub size limit'
            if reason:
                report.append({'path': relative.as_posix(), 'reason': reason})
                continue
            data = path.read_bytes()
            if b'\0' not in data and TOKEN_PATTERN.search(data):
                data = TOKEN_PATTERN.sub(b'REDACTED_CREDENTIAL', data)
                report.append({'path': relative.as_posix(), 'reason': 'API token redacted in snapshot'})
            kind = secret_kind(data)
            if kind:
                report.append({'path': relative.as_posix(), 'reason': kind})
                continue
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
    return report

def discover(config):
    candidates = [Path(config['ai_os'])]
    projects = Path(config['projects_root'])
    if projects.exists():
        candidates += sorted(p for p in projects.iterdir() if p.is_dir() and not is_link(p))
    result = []
    for root in candidates:
        is_project = root != Path(config['ai_os'])
        if not (root / '.git').exists():
            if is_project and config.get('auto_create_private_repositories'):
                try: initialize_private_project(root, config)
                except Exception:
                    config.setdefault('_discovery_errors', []).append({'folder': root.name, 'status': 'blocked', 'error': 'Private repository initialization failed; check repository-name collision or GitHub access'})
                    continue
            else:
                config.setdefault('_discovery_errors', []).append({'folder': root.name, 'status': 'blocked', 'error': 'No Git repository configured'})
                continue
        try: url = git(root, 'remote', 'get-url', 'origin')
        except RuntimeError:
            if is_project and config.get('auto_create_private_repositories'):
                try:
                    initialize_private_project(root, config)
                    url = git(root, 'remote', 'get-url', 'origin')
                except Exception:
                    config.setdefault('_discovery_errors', []).append({'folder': root.name, 'status': 'blocked', 'error': 'Private repository creation failed; existing repositories are never attached automatically'})
                    continue
            else:
                config.setdefault('_discovery_errors', []).append({'folder': root.name, 'status': 'blocked', 'error': 'No origin remote configured'})
                continue
        match = re.fullmatch(r'(?:https://github\.com/|git@github\.com:)([^/]+)/([^/]+?)(?:\.git)?', url)
        if not match or match[1].lower() != config.get('owner', OWNER).lower():
            config.setdefault('_discovery_errors', []).append({'folder': root.name, 'status': 'blocked', 'error': 'Unapproved remote'})
            continue
        result.append((root.resolve(), f'{match[1]}/{match[2]}'))
    return result

def verify_private(repository):
    metadata = json.loads(run('gh', 'api', f'repos/{repository}'))
    if metadata.get('private') is not True:
        raise RuntimeError(f'Repository must be private: {repository}')

def scan(destination, executable):
    if not executable or not Path(executable).is_file():
        raise RuntimeError('Mandatory gitleaks scanner is unavailable')
    report_path = destination.parent / 'gitleaks.json'
    p = subprocess.run([str(executable), 'dir', str(destination), '--redact=100', '--no-banner', '--report-format', 'json', '--report-path', str(report_path)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=180)
    removed = []
    if p.returncode == 1 and report_path.exists():
        for finding in json.loads(report_path.read_text(encoding='utf-8')):
            path = Path(finding['File'])
            if not path.is_absolute(): path = destination / path
            path = long_path(path).resolve()
            try: relative = path.relative_to(destination.resolve())
            except ValueError: raise RuntimeError('Unexpected scanner path; upload blocked')
            data = path.read_bytes() if path.exists() else b''
            cleaned = TOKEN_PATTERN.sub(b'REDACTED_CREDENTIAL', data) if b'\0' not in data else data
            if cleaned != data:
                path.write_bytes(cleaned)
                removed.append({'path': relative.as_posix(), 'reason': 'gitleaks token redacted in snapshot'})
            else:
                if path.exists(): path.unlink()
                removed.append({'path': relative.as_posix(), 'reason': 'gitleaks: ' + finding.get('RuleID', 'secret')})
        retry = subprocess.run([str(executable), 'dir', str(destination), '--redact=100', '--no-banner'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=180)
        if retry.returncode: raise RuntimeError('Mandatory gitleaks rescan failed; upload blocked')
    elif p.returncode:
        raise RuntimeError('Mandatory gitleaks scan failed; upload blocked')
    return removed

def remote_tip(root, branch):
    output = git(root, 'ls-remote', 'origin', f'refs/heads/{branch}')
    return output.split()[0] if output else None

def persist_state(config, state):
    if not config.get('_state_path'):
        raise RuntimeError('Durable snapshot state path is required for upload')
    path = Path(config['_state_path'])
    temporary = path.with_suffix('.tmp')
    temporary.write_text(json.dumps(state, indent=2), encoding='utf-8')
    os.replace(temporary, path)

def reconcile_pending(entry, remote):
    pending = entry.get('pending_commit')
    if pending:
        if remote == pending:
            entry['commit'] = pending
        elif remote != entry.get('prior_remote'):
            raise RuntimeError('Snapshot branch changed externally during pending upload')
        entry.pop('pending_commit', None)
        entry.pop('prior_remote', None)
    return entry.get('commit')

def progress(config, repository, phase):
    if not config.get('_state_dir'): return
    path = Path(config['_state_dir']) / 'progress.json'
    path.write_text(json.dumps({'repository': repository, 'phase': phase, 'updated': datetime.now(timezone.utc).isoformat()}), encoding='utf-8')

def create_tree(root, staging):
    index = staging.parent / 'snapshot-index'
    env = os.environ.copy()
    env['GIT_INDEX_FILE'] = git_path(index)
    args = ('--work-tree=' + git_path(staging),)
    git(root, *args, 'read-tree', '--empty', env=env)
    paths = [p.relative_to(staging).as_posix() for p in staging.rglob('*') if p.is_file()]
    listing = staging.parent / 'paths'
    listing.write_bytes(b''.join(p.encode('utf-8') + b'\0' for p in paths))
    if paths:
        git(root, *args, 'add', '-f', '--pathspec-from-file=' + git_path(listing), '--pathspec-file-nul', env=env)
    return git(root, 'write-tree', env=env)

def publish(root, repository, config, state, dry_run=False):
    progress(config, repository, 'verify private repository')
    verify_private(repository)
    branch = f"codex/local-sync/{slug(config.get('machine', os.environ.get('COMPUTERNAME', 'machine')))}/{slug(root.name)}"
    progress(config, repository, 'check remote snapshot')
    prior = remote_tip(root, branch)
    key = str(root)
    entry = state.get(key, {})
    had_pending = bool(entry.get('pending_commit'))
    expected = reconcile_pending(entry, prior)
    if had_pending and not dry_run:
        persist_state(config, state)
    if prior != expected:
        raise RuntimeError(f'Snapshot branch changed externally: {repository}/{branch}')
    temporary_directory = tempfile.TemporaryDirectory(prefix='github-sync-')
    temporary_directory.name = str(long_path(temporary_directory.name))
    with temporary_directory as folder:
        staging = long_path(Path(folder) / 'files')
        staging.mkdir()
        progress(config, repository, 'copy filtered source')
        report = copy_filtered(root, staging, config.get('max_file_bytes', MAX_SIZE))
        registry = {'repository': repository, 'source_head': git(root, 'rev-parse', 'HEAD'), 'source_branch': git(root, 'branch', '--show-current'), 'snapshot_branch': branch}
        generated = staging / '.cloud-sync'
        generated.mkdir(exist_ok=True)
        (generated / 'workspace.json').write_text(json.dumps(registry, indent=2) + '\n', encoding='utf-8')
        if config.get('export_conversations') and root == Path(config['ai_os']):
            progress(config, repository, 'export conversations')
            adapter_path = root / 'system/scripts/github-sync/chat_export.py'
            if not adapter_path.is_file(): raise RuntimeError('Conversation export adapter unavailable')
            spec = importlib.util.spec_from_file_location('chat_export', adapter_path)
            adapter = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(adapter)
            allowed = [Path(candidate) for candidate in config['_allowed_roots']]
            conversation_state = Path(config['_state_dir']) / 'conversations'
            export_report = adapter.export_conversations(conversation_state, allowed)
            report.extend(copy_filtered(conversation_state, generated / 'conversations'))
            registry['conversation_export'] = {'session_count': len(export_report.get('sessions', [])), 'errors': export_report.get('errors', [])}
            (generated / 'workspace.json').write_text(json.dumps(registry, indent=2) + '\n', encoding='utf-8')
        (staging / 'CLOUD-WORKSPACE.md').write_text('This branch is an automatically generated filtered local workspace snapshot.\n\nRead .cloud-sync/workspace.json for the original source branch and commit. Work on a separate branch and return a pull request. Never write to the snapshot branch. Conversation exports in the AI OS snapshot provide handoff history; they do not recreate native chat sessions.\n', encoding='utf-8')
        progress(config, repository, 'scan secrets')
        report.extend(scan(staging, config.get('gitleaks') or os.environ.get('GITLEAKS') or str(Path(__file__).parent / 'tools/gitleaks.exe')))
        progress(config, repository, 'create Git snapshot tree')
        tree = create_tree(root, staging)
        if dry_run: return dict(registry, tree=tree, skipped=report, status='dry-run')
        if prior:
            git(root, 'fetch', '--no-tags', 'origin', f'refs/heads/{branch}')
            if git(root, 'rev-parse', 'FETCH_HEAD') != prior: raise RuntimeError('Snapshot changed during fetch')
            if git(root, 'show', '-s', '--format=%T', prior) == tree:
                return dict(registry, skipped=report, status='unchanged')
        env = os.environ.copy()
        env.update(GIT_AUTHOR_NAME='Local workspace sync', GIT_AUTHOR_EMAIL='sync@localhost', GIT_COMMITTER_NAME='Local workspace sync', GIT_COMMITTER_EMAIL='sync@localhost')
        commit = git(root, 'commit-tree', tree, *(['-p', prior] if prior else []), '-m', 'Update filtered local workspace snapshot', env=env)
        if remote_tip(root, branch) != prior: raise RuntimeError('Snapshot changed before push')
        state[key] = {'commit': prior, 'pending_commit': commit, 'prior_remote': prior, 'branch': branch, 'repository': repository}
        persist_state(config, state)
        progress(config, repository, 'push snapshot')
        git(root, 'push', 'origin', f'{commit}:refs/heads/{branch}')
        state[key] = {'commit': commit, 'branch': branch, 'repository': repository}
        persist_state(config, state)
        return dict(registry, commit=commit, skipped=report, status='published')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', required=True)
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--once', action='store_true')
    args = parser.parse_args()
    config_path = Path(args.config).resolve()
    config = json.loads(config_path.read_text(encoding='utf-8-sig'))
    if args.dry_run: config['auto_create_private_repositories'] = False
    config['ai_os'] = str((config_path.parent / config.get('vault', config.get('ai_os', '../..'))).resolve())
    config['projects_root'] = str((config_path.parent / config.get('projects', config.get('projects_root', '../../../ai-os-projects'))).resolve())
    state_dir = config_path.parent / 'state'
    state_dir.mkdir(parents=True, exist_ok=True)
    lock = state_dir / 'sync.lock'
    with process_lock(lock) as acquired:
        if not acquired:
            print(json.dumps({'status': 'busy'})); return
        state_path = state_dir / 'state.json'
        config['_state_path'] = str(state_path)
        state = json.loads(state_path.read_text()) if state_path.exists() else {}
        repositories = discover(config)
        config['_allowed_roots'] = [str(root) for root, _ in repositories]
        config['_state_dir'] = str(state_dir)
        results = list(config.get('_discovery_errors', []))
        for root, repository in repositories:
            try:
                results.append(publish(root, repository, config, state, args.dry_run))
                if not args.dry_run:
                    persist_state(config, state)
            except Exception as error:
                results.append({'repository': repository, 'status': 'blocked', 'error': str(error)})
        now = datetime.now(timezone.utc).isoformat()
        status_path = state_dir / 'status.json'
        previous = json.loads(status_path.read_text()) if status_path.exists() else {}
        status = {'last_attempt': now, 'last_success': previous.get('last_success'), 'results': results}
        if not args.dry_run and not any(x['status'] == 'blocked' for x in results): status['last_success'] = now
        status_path.write_text(json.dumps(status, indent=2), encoding='utf-8')
        print(json.dumps(results, indent=2))
        if any(x['status'] == 'blocked' for x in results): raise SystemExit(1)

if __name__ == '__main__': main()
