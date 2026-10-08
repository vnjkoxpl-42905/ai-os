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

def run(*args, cwd=None, env=None, timeout=180):
    p = subprocess.run(args, cwd=cwd, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout, creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0)
    if p.returncode:
        diagnostic = p.stderr.decode('utf-8', errors='replace').lower()
        categories = [label for markers, label in [
            (('gh013', 'push protection', 'secret scanning', 'repository rule violations'), 'GitHub repository policy rejected upload'),
            (('non-fast-forward', 'fetch first'), 'remote advanced; fast-forward rejected'),
            (('rpc failed', 'http 50', 'http 40', 'remote end hung up', 'unexpected disconnect', 'connection reset'), 'network or HTTP transfer failed'),
            (('authentication failed', 'could not read username', 'permission denied'), 'authentication failed'),
            (('exceeds github', 'large files detected', 'gh001'), 'GitHub file-size limit'),
        ] if any(marker in diagnostic for marker in markers)]
        detail = '; '.join(categories) or 'command failed; diagnostic output suppressed to protect credentials'
        raise RuntimeError(f'{args[0]} failed ({p.returncode}): {detail}')
    return p.stdout.decode('utf-8', errors='replace').strip()

def git(root, *args, env=None, timeout=180):
    environment = os.environ.copy() if env is None else env.copy()
    environment.update(GIT_TERMINAL_PROMPT='0', GCM_INTERACTIVE='never')
    return run('git', '-c', 'core.longpaths=true', '-C', str(root), *args, env=environment, timeout=timeout)

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
        if len(value) < 12 or any(x in value for x in (b'example', b'placeholder', b'redacted', b'changeme', b'your_', b'your-', b'${', b'process.env', b'os.environ', b'<', b'undefined', b'null')):
            continue
        if re.fullmatch(rb'[a-z0-9_./\\-]+', value) and not any(c in value for c in b'0123456789'):
            continue
        return 'credential assignment'
    return None

def _redact_text_pass(data):
    parts = data.decode('utf-8').split('\n')
    lines = [part + '\n' for part in parts[:-1]] + parts[-1:]
    affected = set()
    matches = [match for _, pattern in PATTERNS for match in pattern.finditer(data)]
    matches.extend(match for match in ASSIGNMENT.finditer(data) if secret_kind(match.group(0)))
    for match in matches:
        end = match.end()
        if b'PRIVATE KEY-----' in match.group(0):
            closing = re.search(rb'-----END (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----', data[end:])
            if closing: end += closing.end()
        start_line = data[:match.start()].count(b'\n')
        end_line = data[:max(match.start(), end - 1)].count(b'\n')
        affected.update(range(start_line, min(end_line + 1, len(lines))))
    for position in affected:
        line = lines[position]
        ending = '\r\n' if line.endswith('\r\n') else '\n' if line.endswith('\n') else ''
        lines[position] = '[REDACTED CREDENTIAL]' + ending
    return ''.join(lines).encode('utf-8')

def redact_known_text(data):
    for _ in range(64):
        cleaned = _redact_text_pass(data)
        if not secret_kind(cleaned): return cleaned
        if cleaned == data: return cleaned
        data = cleaned
    return data

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

def copy_filtered(root, destination, max_size=MAX_SIZE, originals=None, prefix=''):
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
            original_data = data
            if b'\0' not in data and TOKEN_PATTERN.search(data):
                data = TOKEN_PATTERN.sub(b'REDACTED_CREDENTIAL', data)
                report.append({'path': relative.as_posix(), 'reason': 'API token redacted in snapshot'})
            kind = secret_kind(data)
            if kind:
                try:
                    if b'\0' in data: raise UnicodeError()
                    data = redact_known_text(data)
                    if secret_kind(data): raise RuntimeError('Text credential redaction failed: ' + relative.as_posix())
                    report.append({'path': relative.as_posix(), 'reason': kind + ' redacted in snapshot'})
                except UnicodeError:
                    report.append({'path': relative.as_posix(), 'reason': kind + ' binary file omitted'})
                    continue
            target = destination / relative
            if originals is not None and data != original_data and path.suffix.lower() != '.jsonl':
                try:
                    original_data.decode('utf-8')
                    originals[prefix + relative.as_posix()] = original_data
                except UnicodeError:
                    pass
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
    return report

def discover(config):
    candidates = [Path(config['ai_os'])]
    projects = Path(config['projects_root'])
    # This sibling is an upstream tooling clone used by skill maintenance, not
    # Joshua's application workspace. Skip it before repository initialization
    # or publishing; its upstream remote must never be approved implicitly.
    excluded_projects = {name.casefold() for name in config.get('exclude_project_directories', ['claudex-loop'])}
    if projects.exists():
        for project in sorted(projects.iterdir()):
            if not project.is_dir() or is_link(project):
                continue
            if project.name.casefold() in excluded_projects:
                config.setdefault('_discovery_skipped', []).append({'folder': project.name, 'status': 'skipped', 'reason': 'Excluded tooling directory'})
                continue
            candidates.append(project)
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

def scan(destination, executable, originals=None, prefix=''):
    destination = long_path(destination)
    if not executable or not Path(executable).is_file():
        raise RuntimeError('Mandatory gitleaks scanner is unavailable')
    report_path = destination.parent / 'gitleaks.json'
    p = subprocess.run([str(executable), 'dir', str(destination), '--redact=100', '--no-banner', '--report-format', 'json', '--report-path', str(report_path)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=180, creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0)
    removed = []
    if p.returncode == 1 and report_path.exists():
        findings_by_file = {}
        for finding in json.loads(report_path.read_text(encoding='utf-8')):
            path = Path(finding['File'])
            if not path.is_absolute(): path = destination / path
            path = long_path(path).resolve()
            try: relative = path.relative_to(destination.resolve())
            except ValueError: raise RuntimeError('Unexpected scanner path; upload blocked')
            findings_by_file.setdefault(path, []).append((relative, finding))
        for path, findings in findings_by_file.items():
            data = path.read_bytes() if path.exists() else b''
            try:
                if b'\0' in data: raise UnicodeError()
                text = data.decode('utf-8')
                if originals is not None and path.suffix.lower() != '.jsonl':
                    originals.setdefault(prefix + findings[0][0].as_posix(), data)
                parts = text.split('\n')
                lines = [part + '\n' for part in parts[:-1]] + parts[-1:]
                affected = set()
                for relative, finding in findings:
                    start, end = finding.get('StartLine', 0), finding.get('EndLine', 0)
                    if not isinstance(start, int) or not isinstance(end, int) or not (1 <= start <= end <= len(lines)):
                        raise RuntimeError('Scanner returned invalid text coordinates; upload blocked')
                    affected.update(range(start - 1, end))
                for line in affected:
                    ending = '\r\n' if lines[line].endswith('\r\n') else '\n' if lines[line].endswith('\n') else ''
                    lines[line] = '[REDACTED CREDENTIAL]' + ending
                path.write_bytes(''.join(lines).encode('utf-8'))
                for relative, finding in findings:
                    removed.append({'path': relative.as_posix(), 'reason': 'gitleaks credential redacted in snapshot: ' + finding.get('RuleID', 'secret')})
            except UnicodeError:
                if path.exists(): path.unlink()
                for relative, finding in findings:
                    removed.append({'path': relative.as_posix(), 'reason': 'gitleaks binary file omitted: ' + finding.get('RuleID', 'secret')})
        retry_report = destination.parent / 'gitleaks-rescan.json'
        retry = subprocess.run([str(executable), 'dir', str(destination), '--redact=100', '--no-banner', '--report-format', 'json', '--report-path', str(retry_report)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=180, creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0)
        if retry.returncode:
            details = []
            if retry_report.exists():
                for item in json.loads(retry_report.read_text(encoding='utf-8'))[:5]:
                    candidate = Path(item['File'])
                    if not candidate.is_absolute(): candidate = destination / candidate
                    try: safe_path = long_path(candidate).resolve().relative_to(destination.resolve()).as_posix()
                    except ValueError: safe_path = 'unexpected path'
                    details.append(safe_path + ' (' + item.get('RuleID', 'secret') + ')')
            raise RuntimeError('Mandatory gitleaks rescan failed; upload blocked' + (': ' + ', '.join(details) if details else ''))
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
        visible_originals = {}
        progress(config, repository, 'copy filtered source')
        report = copy_filtered(root, staging, config.get('max_file_bytes', MAX_SIZE), visible_originals, root.name + '/')
        registry = {'repository': repository, 'source_head': git(root, 'rev-parse', 'HEAD'), 'source_branch': git(root, 'branch', '--show-current'), 'snapshot_branch': branch}
        generated = staging / '.cloud-sync'
        generated.mkdir(exist_ok=True)
        (generated / 'workspace.json').write_text(json.dumps(registry, indent=2) + '\n', encoding='utf-8')
        if root == Path(config['ai_os']) and (config.get('credential_sources') or config.get('auto_credential_sources')):
            progress(config, repository, 'encrypt portable credentials')
            credential_spec = importlib.util.spec_from_file_location('credential_bundle', Path(__file__).parent / 'credential_bundle.py')
            credential_adapter = importlib.util.module_from_spec(credential_spec)
            credential_spec.loader.exec_module(credential_adapter)
            registry['credential_bundle'] = credential_adapter.export_bundle(generated / 'private', config)
            (generated / 'workspace.json').write_text(json.dumps(registry, indent=2) + '\n', encoding='utf-8')
        if root == Path(config['ai_os']) and config.get('export_runtime'):
            progress(config, repository, 'export runtime skills and memories')
            runtime_spec = importlib.util.spec_from_file_location('runtime_export', Path(__file__).parent / 'runtime_export.py')
            runtime_adapter = importlib.util.module_from_spec(runtime_spec)
            runtime_spec.loader.exec_module(runtime_adapter)
            registry['runtime_export'] = runtime_adapter.export_runtime(generated / 'runtime', config)
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
            conversation_report = copy_filtered(conversation_state, generated / 'conversations', originals=visible_originals, prefix=root.name + '/.cloud-sync/conversations/')
            report.extend({'path': '.cloud-sync/conversations/' + item['path'], 'reason': item['reason']} for item in conversation_report)
            registry['conversation_export'] = {'session_count': len(export_report.get('sessions', [])), 'errors': export_report.get('errors', [])}
            (generated / 'workspace.json').write_text(json.dumps(registry, indent=2) + '\n', encoding='utf-8')
        (staging / 'CLOUD-WORKSPACE.md').write_text('This branch is an automatically generated filtered local workspace snapshot.\n\nRead .cloud-sync/workspace.json for the original source branch and commit. Work on a separate branch and return a pull request. Never write to the snapshot branch. Conversation exports in the AI OS snapshot provide handoff history; they do not recreate native chat sessions.\n', encoding='utf-8')
        progress(config, repository, 'scan secrets')
        report.extend(scan(staging, config.get('gitleaks') or os.environ.get('GITLEAKS') or str(Path(__file__).parent / 'tools/gitleaks.exe'), visible_originals, root.name + '/'))
        if visible_originals:
            credential_spec = importlib.util.spec_from_file_location('credential_bundle', Path(__file__).parent / 'credential_bundle.py')
            credential_adapter = importlib.util.module_from_spec(credential_spec)
            credential_spec.loader.exec_module(credential_adapter)
            private_state = Path(config['_state_dir']) / 'private'
            cache_id = __import__('hashlib').sha256(str(root).encode('utf-8')).hexdigest()[:20]
            registry['encrypted_original_context'] = credential_adapter.bundle([], private_state / 'context-cache' / cache_id, generated / 'private', 'redacted-context', visible_originals, key_state=private_state)
            (generated / 'workspace.json').write_text(json.dumps(registry, indent=2) + '\n', encoding='utf-8')
            report.extend(scan(staging, config.get('gitleaks') or os.environ.get('GITLEAKS') or str(Path(__file__).parent / 'tools/gitleaks.exe')))
            if not (generated / 'private/redacted-context.enc').exists():
                raise RuntimeError('Encrypted context failed final scanner check; upload blocked')
        report.sort(key=lambda item: (item['path'], item['reason']))
        (generated / 'exclusions.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
        conversation_index = generated / 'conversations/index.json'
        if conversation_index.exists():
            omitted = [item for item in report if item['path'].startswith('.cloud-sync/conversations/') and 'redacted' not in item['reason']]
            index = json.loads(conversation_index.read_text(encoding='utf-8'))
            removed = {item['path'].removeprefix('.cloud-sync/conversations/') for item in omitted}
            index['sessions'] = [item for item in index.get('sessions', []) if item.get('file') not in removed]
            index['snapshot_exclusions'] = omitted
            conversation_index.write_text(json.dumps(index, indent=2) + '\n', encoding='utf-8')
            if 'conversation_export' in registry:
                registry['conversation_export']['session_count'] = len(index['sessions'])
                registry['conversation_export']['snapshot_omitted_count'] = len(removed)
                (generated / 'workspace.json').write_text(json.dumps(registry, indent=2) + '\n', encoding='utf-8')
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
        git(root, 'push', 'origin', f'{commit}:refs/heads/{branch}', timeout=config.get('push_timeout_seconds', 900))
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
        results = list(config.get('_discovery_errors', [])) + list(config.get('_discovery_skipped', []))
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
