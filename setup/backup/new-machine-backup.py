"""Non-deleting, incremental, private backup. Python 3.12+, Windows."""
import argparse, hashlib, json, os, sqlite3, time, zipfile
from contextlib import closing
from pathlib import Path

p = argparse.ArgumentParser()
p.add_argument('--stage', required=True)
p.add_argument('--scope', choices=['core', 'personal', 'all'], default='core')
p.add_argument('--resume-base', help='Reuse checksum-recorded files from a partial generation after CRC verification')
a = p.parse_args()
home = Path.home()
stage = Path(a.stage).resolve()
stage.mkdir(parents=True, exist_ok=True)
stamp = time.strftime('%Y%m%d-%H%M%S')
run = stage / stamp
run.mkdir(exist_ok=False)
roots = {k: home / v for k, v in {
    'ai-os': 'dev/ai-os', 'projects': 'dev/ai-os-projects',
    'codex': '.codex', 'claude': '.claude', 'agents': '.agents',
    'config': '.config', 'superwhisper': 'AppData/Local/com.superwhisper.app',
    'codex-app': 'AppData/Roaming/Codex', 'obsidian': 'AppData/Roaming/obsidian',
    'vscode-user': 'AppData/Roaming/Code/User', 'gh': 'AppData/Roaming/gh',
    'gws': 'AppData/Roaming/gws',
}.items()}
if a.scope == 'personal': roots = {}
if a.scope in ('all', 'personal'):
    roots.update({k: home / k for k in ['Documents', 'Downloads', 'Desktop', 'Pictures']})
excluded = {'node_modules', '.venv', 'venv', '__pycache__', '.cache', 'cache',
    'Cache', 'Code Cache', 'GPUCache', 'logs', 'log', 'tmp', '.tmp', '.sandbox',
    '.sandbox-bin', 'EBWebView', 'EBWebView_Main', 'models', 'Crashpad', 'browser',
    'backups', 'pre-restore', 'recovery-toolchain-20261006', 'web', '_cacache'}
previous = {}
if a.resume_base:
    base=Path(a.resume_base).resolve()
    if base.parent != stage: raise SystemExit('Resume base must be in the same generation store')
    doc=json.loads((base/'manifest.json').read_text())
    if doc['scope'] != a.scope: raise SystemExit('Resume scope mismatch')
    with zipfile.ZipFile(base/'payload.zip') as valid:
        if valid.testzip(): raise SystemExit('Partial baseline archive CRC failed')
    previous=doc['files']
for old in sorted(stage.glob('*/manifest.json'), reverse=True):
    if previous: break
    doc = json.loads(old.read_text(encoding='utf-8'))
    if doc.get('scope') == a.scope and doc.get('complete'):
        previous = doc['files']; break
files, errors, skips = {}, [], []
archive = run / 'payload.zip'
machine = {'home':str(home),'machine':os.environ.get('COMPUTERNAME'),
    'python':str(Path(os.__file__).parent.parent),'user_environment':{}}
if os.name == 'nt':
    import winreg
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER,'Environment') as registry:
            for i in range(winreg.QueryInfoKey(registry)[1]):
                name,value,kind = winreg.EnumValue(registry,i)
                machine['user_environment'][name] = {'value':value,'registry_type':kind}
    except OSError as error: errors.append({'path':'HKCU/Environment','error':str(error)})
machine_path=run/'machine-info.json'
machine_path.write_text(json.dumps(machine,indent=2),encoding='utf-8')
def candidates():
    yield 'system/machine-info.json',machine_path
    for label, root in roots.items():
        if not root.exists():
            skips.append({'path': str(root), 'reason': 'missing'}); continue
        def walk_error(error):
            errors.append({'path': error.filename, 'error': str(error)})
        walkroot = Path('\\\\?\\'+str(root.resolve())) if os.name=='nt' else root
        for parent, dirs, names in os.walk(walkroot, followlinks=False, onerror=walk_error):
            base = Path(parent)
            dirs[:] = [d for d in dirs if d not in excluded
                and not (base / d).is_junction() and not (base / d).is_symlink()
                and not (base / d).resolve().is_relative_to(stage)
                and not (label == 'Documents' and d == 'work' and 'in-x20' in base.parts)]
            for name in names:
                source = base / name
                if source.is_symlink() or name.endswith(('-wal', '-shm', '.lock', '.tmp')):
                    continue
                if label == 'codex' and name.startswith('logs_'): continue
                yield label + '/' + source.relative_to(walkroot).as_posix(), source
    for name in ([] if a.scope == 'personal' else ['.claude.json', '.gitconfig', '.npmrc', '.bashrc']):
        source = home / name
        if source.exists(): yield 'dotfiles/' + name, source

with zipfile.ZipFile(archive, 'x', compression=zipfile.ZIP_DEFLATED, compresslevel=1, allowZip64=True) as z:
    for key, source in candidates():
        try:
            st = source.stat()
            old = previous.get(key)
            isdb = source.suffix in ('.sqlite', '.db')
            if old and not isdb and old['size'] == st.st_size and old['mtime_ns'] == st.st_mtime_ns:
                files[key] = old; continue
            copyfrom = source
            database_info={}
            if isdb:
                # backup() reads a consistent snapshot including committed WAL data.
                snap = run / 'sqlite-snapshots' / key
                snap.parent.mkdir(parents=True, exist_ok=True)
                uri_source=Path(str(source).removeprefix('\\\\?\\'))
                with closing(sqlite3.connect(uri_source.as_uri() + '?mode=ro', uri=True, timeout=5)) as src:
                    with closing(sqlite3.connect(snap)) as dst:
                        # Pin one read-only WAL snapshot so live writes cannot restart every page batch.
                        src.execute('BEGIN')
                        src.execute('SELECT count(*) FROM sqlite_master').fetchone()
                        deadline = time.monotonic() + 300
                        def progress(status, remaining, total):
                            if time.monotonic() > deadline:
                                raise TimeoutError('SQLite snapshot exceeded 300 seconds; retry later')
                        src.backup(dst, pages=1024, progress=progress)
                        src.rollback()
                        # Checkpoint only the generated destination before archiving its main file.
                        dst.execute('PRAGMA wal_checkpoint(TRUNCATE)')
                        if dst.execute('PRAGMA quick_check').fetchone()[0] != 'ok':
                            raise RuntimeError('SQLite integrity check failed')
                # Reopen the CLOSED generated main file with WAL ignored to prove portability.
                with closing(sqlite3.connect(snap.as_uri()+'?mode=ro&immutable=1',uri=True)) as independent:
                    if independent.execute('PRAGMA quick_check').fetchone()[0]!='ok':
                        raise RuntimeError('Closed SQLite main-file integrity check failed')
                    page_count=independent.execute('PRAGMA page_count').fetchone()[0]
                    page_size=independent.execute('PRAGMA page_size').fetchone()[0]
                    if snap.stat().st_size != page_count*page_size:
                        raise RuntimeError('SQLite main-file size/page-count mismatch')
                    database_info={'sqlite_main_file_verified':True,'sqlite_pages':page_count,'sqlite_page_size':page_size}
                copyfrom = snap
            digest = hashlib.sha256()
            with copyfrom.open('rb') as f, z.open(key, 'w', force_zip64=True) as out:
                while chunk := f.read(1024 * 1024):
                    digest.update(chunk); out.write(chunk)
            if not isdb and source.stat().st_mtime_ns != st.st_mtime_ns:
                raise RuntimeError('changed during capture; retry next run')
            files[key] = {'size': copyfrom.stat().st_size, 'mtime_ns': st.st_mtime_ns,
                'sha256': digest.hexdigest(), 'generation': stamp, **database_info}
            if len(files) % 500 == 0: print('Captured', len(files), 'files', flush=True)
        except Exception as e:
            errors.append({'path': str(source), 'error': str(e)})
with zipfile.ZipFile(archive) as check:
    if check.testzip(): errors.append({'error': 'archive CRC validation failed'})
h = hashlib.sha256()
with archive.open('rb') as f:
    while chunk := f.read(1024 * 1024): h.update(chunk)
manifest = {'format': 1, 'generation': stamp, 'scope': a.scope, 'machine': os.environ.get('COMPUTERNAME'),
    'home': str(home), 'roots': {k: str(v) for k,v in roots.items()},
    'complete': not errors, 'files': files, 'errors': errors, 'skipped_roots': skips,
    'exclusions': sorted(excluded), 'archive_sha256': h.hexdigest(), 'archive_bytes': archive.stat().st_size}
(run / 'manifest.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')
(run / 'SHA256SUMS.txt').write_text(h.hexdigest() + '  payload.zip\n', encoding='utf-8')
print(json.dumps({'generation':str(run), 'files':len(files), 'errors':len(errors), 'archive_bytes':archive.stat().st_size}))
raise SystemExit(1 if errors else 0)
