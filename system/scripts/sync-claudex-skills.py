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
ALIASES = ('grill-me-codex', 'grill-with-docs-codex', 'grill-by-claude')
OVERRIDES = VAULT / 'system/skill-overrides/claudex'
CLAUDE_ROOTS = {HOME / '.claude/skills', VAULT / '.claude/skills', VAULT / 'skills/claude'}
CODEX_NAMES = {'codex-review': 'claude-review', 'codex-build': 'claude-build',
               'grill-me-codex': 'grill-me-claude',
               'grill-with-docs-codex': 'grill-with-docs-claude'}


def base_entrypoint(source, name, runtime):
    """Adapt entry points while preserving the current upstream support tree."""
    original = (source / 'SKILL.md').read_text(encoding='utf-8')
    if name == 'grill-by-claude':
        return original
    custom = OVERRIDES / runtime / name / 'SKILL.md'
    if custom.is_file():
        custom.resolve().relative_to(OVERRIDES.resolve())
        return custom.read_text(encoding='utf-8')
    other = 'codex' if runtime == 'claude' else 'claude'
    direction = (f'## Installed direction: {runtime.title()} to {other.title()}\n\n'
                 f'This copy is for the {runtime.title()} host. The current {runtime.title()} '
                 f'conversation coordinates. Use `host={runtime}` in the shared runner. '
                 f'The default independent reviewer and cross-provider handoff target is '
                 f'{other.title()}. Preserve explicit user provider/model choices and authorized scope. '
                 'For the loop, the host builds by default and the other provider inspects; '
                 'the build compatibility entry point separately selects the other provider as builder.\n\n')
    split = original.split('---', 2)
    if len(split) != 3:
        raise RuntimeError(f'Invalid skill frontmatter: {source}')
    header, body = split[1], split[2]
    header_lines = header.splitlines()
    for i, line in enumerate(header_lines):
        if line.startswith('description:'):
            header_lines[i] = f'description: "{runtime.title()}-host entry point: {other.title()} handles independent review or scoped delegation. ' + line.partition(':')[2].strip().strip('"') + '"'
    return '---\n' + '\n'.join(header_lines).strip() + '\n---\n\n' + direction + body.lstrip()


def entrypoint(source, name, runtime):
    text = base_entrypoint(source, name, runtime)
    if runtime == 'codex' and name in CODEX_NAMES:
        new_name = CODEX_NAMES[name]
        text = text.replace(f'name: {name}\n', f'name: {new_name}\n')
        if name in ('codex-build', 'codex-review'):
            text = text.replace(f'The retained name `{name}` is a compatibility name.',
                                f'Invoke this Codex-side skill as `{new_name}`.')
            text = text.replace(f'Codex-host inverse of the Codex {"Build" if name == "codex-build" else "Review"} entry point.',
                                f'Codex-to-Claude {"build" if name == "codex-build" else "review"} workflow.')
    return text


def git(*args):
    return subprocess.check_output(['git', '-C', str(REPO), *args], text=True).strip()


def digest(folder, skill_text=None):
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
            content = skill_text.encode('utf-8') if skill_text is not None and p.relative_to(folder).as_posix() == 'SKILL.md' else p.read_bytes()
            h.update(b'\0' + content.replace(b'\r\n', b'\n') + b'\0')
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
        for root in ROOTS:
            runtime = 'claude' if root in CLAUDE_ROOTS else 'codex'
            skill_text = entrypoint(source, name, runtime)
            new = digest(source, skill_text)
            installed_name = CODEX_NAMES.get(name, name) if runtime == 'codex' else name
            target = root / installed_name
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
                    (stage / 'SKILL.md').write_text(skill_text, encoding='utf-8')
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
            if installed_name != name:
                obsolete = root / name
                obsolete_key = str(obsolete)
                if obsolete.exists():
                    obsolete_hash = digest(obsolete)
                    if obsolete_hash != state['copies'].get(obsolete_key):
                        conflicts.append(obsolete_key)
                        continue
                    print(f'RETIRE {obsolete}')
                    if not args.dry_run:
                        obsolete.resolve().relative_to(root.resolve())
                        root_key = hashlib.sha256(str(root).encode()).hexdigest()[:12]
                        backup = BACKUPS / stamp / root_key / ('retired-' + name)
                        backup.resolve().relative_to(BACKUPS.resolve())
                        backup.parent.mkdir(parents=True, exist_ok=True)
                        if digest(obsolete) != obsolete_hash or digest(target) != new:
                            raise RuntimeError(f'Concurrent rename migration: {obsolete}')
                        obsolete.rename(backup)
                        state['copies'].pop(obsolete_key, None)
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
