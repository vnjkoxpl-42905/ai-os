"""Align existing activation drift while preserving originals and extra payloads."""
from pathlib import Path
import hashlib
import json
import os
import tempfile

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).parent
rows = []

def write(p, data):
    before = p.read_bytes() if p.exists() else None
    if data == before:
        return
    backup = None
    if before is not None:
        backup = OUT/'backups'/'activation-final'/p.relative_to(ROOT)
        backup.parent.mkdir(parents=True, exist_ok=True)
        backup.write_bytes(before)
    p.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=p.parent, prefix='.align-',delete=False) as f:
        f.write(data)
        staged = Path(f.name)
    try:
        if (p.read_bytes() if p.exists() else None) != before:
            raise RuntimeError(f'Concurrent modification: {p}')
        os.replace(staged,p)
    finally:
        if staged.exists():
            staged.unlink()
    rows.append(dict(path=str(p),backup=str(backup) if backup else None,
                     before_sha256=hashlib.sha256(before).hexdigest() if before else None,
                     after_sha256=hashlib.sha256(data).hexdigest()))

# Existing compatibility activations are retained and explicitly catalogued.
for name in ('codex-build','codex-review'):
    src = ROOT/'.agents/skills'/name/'SKILL.md'
    dst = ROOT/'skills/codex'/name/'SKILL.md'
    if not dst.exists():
        write(dst,src.read_bytes())

# Previously uncatalogued Gemini-specific skills remain Gemini-specific.
for name in ('7sage-browser-operations','facebook-browser-operations','reddit-browser-operations'):
    src = ROOT/'.gemini/skills'/name/'SKILL.md'
    dst = ROOT/'skills/gemini'/name/'SKILL.md'
    if src.exists() and not dst.exists():
        text = src.read_text(encoding='utf-8').replace('remains permanently saved across reboots.', 'may persist across reboots; verify the rendered signed-in session before use.')
        write(src,text.encode('utf-8'))
        write(dst,src.read_bytes())

for rt,active in (('codex','.agents'),('claude','.claude'),('gemini','.gemini')):
    root = ROOT/active/'skills'
    if not root.exists():
        continue
    for target in root.iterdir():
        if target.name.startswith(('.','_')) or target.is_symlink() or not target.is_dir():
            continue
        source = ROOT/'skills'/rt/target.name
        if not (source/'SKILL.md').is_file() or not (target/'SKILL.md').is_file():
            continue
        if (source/'SKILL.md').read_text(encoding='utf-8').replace('\r\n','\n') == (target/'SKILL.md').read_text(encoding='utf-8').replace('\r\n','\n'):
            continue
        for p in source.rglob('*'):
            if p.is_file() and not p.is_symlink() and not any(x in p.parts for x in ('__pycache__','.git','_snapshots')):
                write(target/p.relative_to(source),p.read_bytes())

(OUT/'activation-final-receipts.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
print(json.dumps({'changed_or_catalogued_files':len(rows)}))
