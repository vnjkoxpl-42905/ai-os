from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
AUDIT=Path(__file__).resolve().parent
data=json.loads((AUDIT/'skills.json').read_text(encoding='utf-8-sig'))
records=data.get('records',data.get('skills',[]));errors=[];editable=readonly=0
for r in records:
 if r.get('classification') not in ['primary','supporting']:continue
 p=Path(r['path'])
 if not p.is_file():errors.append('Missing skill '+str(p));continue
 if r.get('editable'):
  editable+=1;text=p.read_text(encoding='utf-8-sig')
  if 'design/README.md' not in text:errors.append('Missing skill route '+str(p))
  if r.get('verified_sha256') and hashlib.sha256(p.read_bytes()).hexdigest()!=r['verified_sha256']:errors.append('Skill changed after audit '+str(p))
 else:readonly+=1
global_paths=[Path.home()/'.claude/CLAUDE.md',Path.home()/'.codex/AGENTS.md',Path.home()/'AGENTS.md']
for p in global_paths:
 if 'C:/Users/Joshu/dev/ai-os/design/README.md' not in p.read_text(encoding='utf-8-sig'):errors.append('Missing global route '+str(p))
for p in [ROOT/'AGENTS.md',ROOT/'CLAUDE.md']:
 if 'design/README.md' not in p.read_text(encoding='utf-8-sig'):errors.append('Missing vault route '+str(p))
result={'considered_skill_paths':len(records),'editable_routes_checked':editable,'read_only_companion_records':readonly,'global_routes_checked':len(global_paths),'vault_routes_checked':2,'errors':errors}
(AUDIT/'routing-verification.json').write_bytes(json.dumps(result,indent=2).encode('utf-8'))
print(json.dumps(result))
if errors:raise SystemExit(1)
