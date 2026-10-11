"""Persist approved Claude-host entrypoint fixes in existing updater overlays."""
from pathlib import Path
import hashlib
import json
import os
import tempfile

ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).parent
rows=[]
for name in ('codex-build','codex-review'):
    data=(Path.home()/'.claude/skills'/name/'SKILL.md').read_bytes()
    for p in (ROOT/'skills/claude'/name/'SKILL.md', ROOT/'.claude/skills'/name/'SKILL.md',
              ROOT/'system/skill-overrides/claudex/claude'/name/'SKILL.md'):
        before=p.read_bytes() if p.exists() else None
        if before==data:
            continue
        backup=None
        if before is not None:
            backup=OUT/'backups'/'claudex-final'/p.relative_to(ROOT)
            backup.parent.mkdir(parents=True,exist_ok=True)
            backup.write_bytes(before)
        p.parent.mkdir(parents=True,exist_ok=True)
        with tempfile.NamedTemporaryFile(dir=p.parent,prefix='.claudex-repair-',delete=False) as f:
            f.write(data)
            stage=Path(f.name)
        if (p.read_bytes() if p.exists() else None)!=before:
            raise RuntimeError('Concurrent edit: '+str(p))
        os.replace(stage,p)
        rows.append(dict(path=str(p),backup=str(backup) if backup else None,
                         before_sha256=hashlib.sha256(before).hexdigest() if before else None,
                         after_sha256=hashlib.sha256(data).hexdigest()))
(OUT/'claudex-final-receipts.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
print(json.dumps({'changed_or_added_files':len(rows)}))
