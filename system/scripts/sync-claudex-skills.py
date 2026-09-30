"""Update explicitly installed Claudex copies; preserve backups and local edits."""
import argparse
import datetime
import hashlib
import json
import pathlib
import shutil
import subprocess
import uuid

VAULT = pathlib.Path(__file__).resolve().parents[2]
HOME = pathlib.Path.home()
REPO = VAULT.parent / 'ai-os-projects' / 'claudex-loop'
STATE = HOME / '.agents' / 'claudex-sync-state.json'
BACKUPS = HOME / '.agents' / 'claudex-backups'
ROOTS = [HOME / '.agents/skills', HOME / '.codex/skills', HOME / '.claude/skills',
         VAULT / '.agents/skills', VAULT / '.claude/skills',
         VAULT / 'skills/codex', VAULT / 'skills/claude']
SKILLS = {'claudex-loop': 'skills', 'claudex-route': 'skills',
          'codex-review': 'skills', 'codex-build': 'skills'}
ALIASES = ('grill-me-codex', 'grill-with-docs-codex')
OVERRIDES = VAULT / 'system/skill-overrides/claudex'


def git(*args):
    return subprocess.check_output(['git', '-C', str(REPO), *args], text=True).strip()


def digest(folder):
    if folder.is_symlink() or getattr(folder, 'is_junction', lambda: False)():
        raise RuntimeError(f'Linked directory requires manual review: {folder}')
    h = hashlib.sha256()
    for p in sorted(folder.rglob('*')):
        if '__pycache__' in p.parts or p.suffix == '.pyc':
            continue
        if p.is_symlink() or getattr(p, 'is_junction', lambda: False)():
            raise RuntimeError(f'Symlink requires manual review: {p}')
        if p.is_file():
            h.update(p.relative_to(folder).as_posix().encode())
            h.update(b'\0' + p.read_bytes().replace(b'\r\n', b'\n') + b'\0')
    return h.hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--install', action='store_true', help='Explicit initial adoption of existing copies')
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--offline', action='store_true')
    args = parser.parse_args()
    if git('remote', 'get-url', 'origin').removesuffix('.git') not in (
            'https://github.com/chaseai-yt/claudex-loop', 'git@github.com:chaseai-yt/claudex-loop'):
        raise RuntimeError('Unexpected upstream remote')
    if git('status', '--porcelain'):
        raise RuntimeError('Upstream checkout has local edits; update stopped')
    if not args.offline:
        subprocess.run(['git', '-C', str(REPO), 'pull', '--ff-only'], check=True, timeout=120)
    sha = git('rev-parse', 'HEAD')
    prior = STATE.read_bytes() if STATE.exists() else None
    state = json.loads(prior) if prior else {'copies': {}}
    stamp = datetime.datetime.now().strftime('%Y%m%d-%H%M%S') + '-' + uuid.uuid4().hex[:8]
    changed = 0
    conflicts = []
    sources = [(name, REPO / group / name, REPO / group)
               for name, group in SKILLS.items()]
    sources.extend((name, OVERRIDES / name, OVERRIDES) for name in ALIASES)
    for name, source, source_root in sources:
        if source.is_symlink() or getattr(source, 'is_junction', lambda: False)():
            raise RuntimeError(f'Linked upstream skill requires manual review: {source}')
        source.resolve().relative_to(source_root.resolve())
        if not (source / 'SKILL.md').is_file():
            raise RuntimeError(f'Missing upstream skill: {name}')
        new = digest(source)
        for root in ROOTS:
            target = root / name
            key = str(target)
            if target.is_symlink() or getattr(target, 'is_junction', lambda: False)():
                conflicts.append(key)
                continue
            old = digest(target) if target.exists() else None
            if old != new and old is not None and not args.install and old != state['copies'].get(key):
                conflicts.append(key)
                continue
            if old != new:
                print(f'UPDATE {target}')
                changed += 1
                if not args.dry_run:
                    root.mkdir(parents=True, exist_ok=True)
                    stage = root / ('.claudex-stage-' + name + '-' + stamp)
                    shutil.copytree(source, stage, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
                    if digest(stage) != new or (digest(target) if target.exists() else None) != old:
                        raise RuntimeError(f'Concurrent modification or staging mismatch: {target}')
                    if target.exists():
                        root_key = hashlib.sha256(str(root).encode()).hexdigest()[:12]
                        backup = BACKUPS / stamp / root_key / name
                        backup.parent.mkdir(parents=True, exist_ok=True)
                        for candidate in (target, stage):
                            candidate.resolve().relative_to(root.resolve())
                        backup.resolve().relative_to(BACKUPS.resolve())
                        target.rename(backup)
                    stage.rename(target)
                    assert digest(target) == new
            state['copies'][key] = new
    state.update({'repository': 'chaseai-yt/claudex-loop', 'commit': sha,
                  'checked_at': datetime.datetime.now(datetime.timezone.utc).isoformat()})
    if not args.dry_run:
        STATE.parent.mkdir(parents=True, exist_ok=True)
        if (STATE.read_bytes() if STATE.exists() else None) != prior:
            raise RuntimeError('Concurrent sync state modification')
        staged_state = STATE.with_suffix('.new-' + uuid.uuid4().hex)
        staged_state.write_text(json.dumps(state, indent=2), encoding='utf-8')
        staged_state.replace(STATE)
    for conflict in conflicts:
        print(f'PRESERVED LOCAL EDIT: {conflict}')
    print(f'Commit {sha}: {changed} copies changed; {len(conflicts)} local conflicts.')
    if conflicts:
        raise SystemExit(2)


if __name__ == '__main__':
    main()
