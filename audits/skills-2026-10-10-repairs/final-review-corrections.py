"""Apply final independent reviewer findings; keep exact original payloads."""
from pathlib import Path
import hashlib
import json
import os
import re
import tempfile

ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).parent
scopes=[ROOT/'skills'/r for r in ('claude','codex','gemini')]
scopes += [ROOT/r/'skills' for r in ('.agents','.claude','.gemini')]
scopes += [Path.home()/r/'skills' for r in ('.agents','.codex','.claude')]
rows=[]
seen=set()

def save(p,data):
    before=p.read_bytes() if p.exists() else None
    if data==before:
        return
    backup=None
    if before is not None:
        backup=OUT/'backups/reviewer-final'/hashlib.sha256(str(p).encode()).hexdigest()[:20]/p.name
        backup.parent.mkdir(parents=True,exist_ok=True)
        backup.write_bytes(before)
    p.parent.mkdir(parents=True,exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=p.parent,prefix='.review-',delete=False) as f:
        f.write(data)
        stage=Path(f.name)
    if (p.read_bytes() if p.exists() else None)!=before:
        raise RuntimeError('Concurrent edit: '+str(p))
    os.replace(stage,p)
    rows.append(dict(path=str(p),backup=str(backup) if backup else None,
                     before_sha256=hashlib.sha256(before).hexdigest() if before else None,
                     after_sha256=hashlib.sha256(data).hexdigest()))

for scope in scopes:
    for p in scope.rglob('SKILL.md'):
        if p.parent.name not in ('watch','claude-api') or any(x in p.parts for x in ('_snapshots','_project-forks')) or p.resolve() in seen:
            continue
        seen.add(p.resolve())
        if p.parent.name=='claude-api':
            text=p.read_text(encoding='utf-8')
            text=re.sub(r'^- \*\*Don\'t research SDK types[^\n]*', '- **Resolve SDK types from evidence before writing.** Use bundled documented signatures or installed SDK definitions. Fetch the official SDK documentation for an undocumented binding when available; if access fails, disclose the assumption and use a compile/fix loop without claiming a verified API shape.',text,flags=re.M)
            text=text.replace("If the user's prompt names a model that the feature doesn't support, use a supported model instead and note the substitution in the output.", "If the selected model does not support the feature, explain the conflict and obtain authorization for a different model or feature. Do not unilaterally substitute the model or change the budget.")
            save(p,text.encode('utf-8'))
            continue
        for name in ('watch.py','whisper.py'):
            script=p.parent/'scripts'/name
            if not script.is_file() or script.resolve() in seen:
                continue
            seen.add(script.resolve())
            text=script.read_text(encoding='utf-8')
            if name=='watch.py':
                text=re.sub(r'            setup_py = SCRIPT_DIR / "setup.py"\n            print\(.*?\n            \)', '            print(f"[watch] {hint}. Optional provider setup needs explicit authorization; "\n                  "keep keys private in the project environment/.env.", file=sys.stderr)',text,flags=re.S)
            else:
                text=re.sub(r'    if backend is None or api_key is None:.*?(?=    print\(f"\[watch\] extracting audio)', '    if backend not in ("groq", "openai"):\n        raise SystemExit("Select groq or openai explicitly after upload/cost authorization")\n    if api_key is None:\n        _, api_key = load_api_key(backend)\n    if not api_key:\n        raise SystemExit("No key for the explicitly selected provider. Authorized setup uses "\n                         "the private project environment/.env; no legacy setup wizard is required.")\n\n',text,flags=re.S)
                text=text.replace('    out_path.parent.mkdir(parents=True, exist_ok=True)', '    if out_path.exists():\n        raise SystemExit("Audio output already exists; choose a fresh path")\n    out_path.parent.mkdir(parents=True, exist_ok=True)',1)
                text=text.replace('        "-y",','        "-n",')
                text=text.replace('Install with: brew install ffmpeg', 'Check installed FFmpeg and refresh PATH before installing for your platform')
            save(script,text.encode('utf-8'))

# The existing Codex-global watch activation lacked its executable payload.
source=Path.home()/'.agents/skills/watch/scripts'
target=Path.home()/'.codex/skills/watch/scripts'
for p in source.rglob('*'):
    if p.is_file() and not p.is_symlink() and '__pycache__' not in p.parts and p.suffix!='.pyc':
        dest=target/p.relative_to(source)
        if not dest.exists():
            save(dest,p.read_bytes())

(OUT/'reviewer-final-receipts.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
print(json.dumps({'changed_or_added_files':len(rows)}))
