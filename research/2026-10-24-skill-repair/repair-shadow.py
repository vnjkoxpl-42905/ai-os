from pathlib import Path
import hashlib
import json
import re
import zipfile

ROOT = Path(__file__).resolve().parents[2]
HOME = Path.home()
OUT = Path(__file__).parent
NAMES = 'bootcamp-builder general-video hyperframes hyperframes-animation hyperframes-cli hyperframes-core hyperframes-studio impeccable media-use'.split()
ROOTS = [ROOT/'skills/claude', ROOT/'skills/codex', ROOT/'.claude/skills', ROOT/'.agents/skills', HOME/'.claude/skills', HOME/'.agents/skills', HOME/'.codex/skills']

def tree(folder):
    result = {}
    for p in folder.rglob('*'):
        if p.is_symlink():
            raise RuntimeError(f'Review symlink before continuing: {p}')
        if p.is_file():
            result[p.relative_to(folder).as_posix()] = p.read_bytes()
    return result

def digest(blob):
    return hashlib.sha256(blob).hexdigest()

plans = {}
sources = {}
for name in NAMES:
    catalog = tree(ROOT/'skills/claude'/name)
    assert catalog == tree(ROOT/'skills/codex'/name), name
    newer = tree(HOME/'.claude/skills'/name)
    if name == 'bootcamp-builder':
        desired = catalog.copy()
        authority = 'catalog: current drill entry contract and complete teaching preference ledger'
    elif name == 'impeccable':
        desired = catalog.copy()
        desired['reference/critique.md'] = newer['reference/critique.md']
        authority = 'catalog entry contract; home critique detector fix'
    else:
        desired = catalog | newer
        authority = 'home Claude complete current support tree; preserved catalogue-only files'
    old_entry = catalog['SKILL.md'].decode('utf-8')
    entry = desired['SKILL.md'].decode('utf-8')
    route = re.search(r'<!-- BEGIN GENERATED DESIGN HUB ROUTE -->.*?<!-- END GENERATED DESIGN HUB ROUTE -->', old_entry, re.S)
    if route and '<!-- BEGIN GENERATED DESIGN HUB ROUTE -->' not in entry:
        entry = entry.rstrip()+'\n\n'+route.group()+'\n'
    desired['SKILL.md'] = entry.encode('utf-8')
    if name == 'hyperframes-cli':
        for rel in ['SKILL.md','references/lint-validate-inspect.md']:
            content = desired[rel].decode('utf-8')
            content = content.replace('When disk is tight, run `npx hyperframes clean` (`--dry-run` to list first);', 'When disk is tight, inspect `npx hyperframes clean --dry-run` first; run any cleanup that deletes files only after explicit user approval. The cleanup command')
            content = content.replace('then remove only that owned directory.', 'then remove only that owned directory after explicit user approval.')
            content = content.replace('and remove that folder after inspecting it.', 'and remove that folder after inspecting it only with explicit user approval.')
            content = content.replace('use it only when that evidence is no longer needed.', 'use it only after explicit user approval and when that evidence is no longer needed.')
            desired[rel] = content.encode('utf-8')
    sources[name] = authority
    for base in ROOTS:
        folder = base/name
        if folder.exists():
            plans[folder] = desired

# Required storyboard support, without widening entrypoint synchronization.
for base in ROOTS:
    folder = base/'hyperframes-creative'
    if folder.exists():
        plans[folder] = {rel:(HOME/'.claude/skills/hyperframes-creative'/rel).read_bytes() for rel in ['references/storyboard-recipe.md','references/story-spine.md']}

original = {folder:tree(folder) for folder in plans}
backup = OUT/'shadow-before.snapshot.zip'
assert not backup.exists(), 'Do not overwrite an earlier snapshot'
with zipfile.ZipFile(backup,'x',zipfile.ZIP_DEFLATED) as archive:
    for i,(folder,files) in enumerate(original.items()):
        for rel,blob in files.items():
            archive.writestr(f'{i:02}/{rel}',blob)
    archive.writestr('MANIFEST.json', json.dumps({str(i):str(folder) for i,folder in enumerate(original)},indent=2))

# Compare every target against its captured generation before the first write.
for folder, expected in original.items():
    assert tree(folder)==expected, f'Concurrent edit: {folder}'

receipts=[]
for folder,desired in plans.items():
    changed=[]
    for rel,blob in desired.items():
        dest=folder/rel
        expected=original[folder].get(rel)
        actual=dest.read_bytes() if dest.exists() else None
        assert actual==expected, f'Concurrent edit: {dest}'
        if actual!=blob:
            dest.parent.mkdir(parents=True,exist_ok=True)
            dest.write_bytes(blob)
            changed.append({'file':rel,'before':digest(actual) if actual is not None else None,'after':digest(blob)})
        assert dest.read_bytes()==blob
    after=tree(folder)
    assert all(after[rel]==blob for rel,blob in desired.items())
    assert set(original[folder]).issubset(after), 'No existing extras may be removed'
    receipts.append({'folder':str(folder),'verified_files':len(desired),'changed_files':changed,'preserved_extra_files':sorted(set(after)-set(desired))})
summary={'authority':sources,'snapshot':str(backup),'snapshot_sha256':digest(backup.read_bytes()),'receipts':receipts}
(OUT/'shadow-receipts.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'folders':len(receipts),'files_changed':sum(len(r['changed_files']) for r in receipts),'snapshot':str(backup)},indent=2))
