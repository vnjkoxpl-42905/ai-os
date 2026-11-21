from pathlib import Path
import hashlib
import json
import re

ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).parent
scopes=[ROOT/'skills'/r for r in ('claude','codex','gemini')]
scopes += [ROOT/r/'skills' for r in ('.agents','.claude','.gemini')]
scopes += [Path.home()/r/'skills' for r in ('.agents','.codex','.claude')]
rows=[]
seen=set()
for scope in scopes:
    for p in scope.rglob('SKILL.md'):
        if p.parent.name!='watch' or any(x in p.parts for x in ('_snapshots','_project-forks')) or p.resolve() in seen:
            continue
        seen.add(p.resolve())
        before=p.read_bytes()
        text=before.decode('utf-8')
        text=re.sub(r'- `--whisper groq\|openai`[^\n]*', '- `--whisper groq|openai` enables only that provider after upload/cost authorization. Default: free captions only.',text)
        text=re.sub(r'\*\*Step 3[^\n]*', '**Step 3: view the frames with an available host image-viewing tool.** Inspect every frame relevant to the requested claim; disclose any unsampled ranges. Use chronological timestamps to compare images and captions. Do not claim visual verification from filenames alone.',text)
        text=re.sub(r'Keep keys in the current project central .env[^\n]*', 'Keep keys in the current project central .env/environment. The repaired loader no longer reads the legacy ~/.config/watch/.env store. Do not run the legacy installer. Paid fallback needs explicit provider, upload and cost authorization; ordinary extraction remains free.',text)
        text=text.replace('--fps 3','--fps 2')
        text=text.replace('so Codex can `Read` them','so the current host can view them with its supported image tool')
        if text.encode('utf-8')==before:
            continue
        backup=OUT/'backups/watch-prose'/hashlib.sha256(str(p).encode()).hexdigest()[:20]/'SKILL.md'
        backup.parent.mkdir(parents=True,exist_ok=True)
        backup.write_bytes(before)
        if p.read_bytes()!=before:
            raise RuntimeError('Concurrent edit')
        p.write_text(text,encoding='utf-8')
        rows.append(dict(path=str(p),backup=str(backup),before_sha256=hashlib.sha256(before).hexdigest(),after_sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
(OUT/'watch-prose-receipts.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
print(len(rows),'watch entrypoints corrected')
