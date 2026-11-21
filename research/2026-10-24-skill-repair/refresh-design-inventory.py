from pathlib import Path
import copy,hashlib,json
ROOT=Path(__file__).resolve().parents[2]
path=ROOT/'research/2026-10-24-design-completeness/skills.json'
old=path.read_bytes();data=json.loads(old.decode('utf-8-sig'))
backup=Path(__file__).parent/'design-inventory-before-repair.json'
if not backup.exists():backup.write_bytes(old)
records=data['records'];known={str(Path(r['path'])) for r in records};changed=0;added=0
for r in records:
 p=Path(r['path'])
 if not p.is_file():continue
 digest=hashlib.sha256(p.read_bytes()).hexdigest()
 if digest!=r.get('verified_sha256',r.get('sha256')):
  r['prior_audit_sha256']=r.get('verified_sha256',r.get('sha256'))
  if 'preserved_original_bytes' in r:r['prior_audit_preserved_original_bytes']=r.pop('preserved_original_bytes')
  r['repair_snapshot']='research/2026-10-24-skill-repair/shadow-before.snapshot.zip'
  r['sha256']=digest;r['verified_sha256']=digest;r['reconciled_on']='2026-10-24 skill repair';changed+=1
for name in ['chrome-extensions','modern-web-guidance']:
 source=next(r for r in records if Path(r['path']).parent.name==name and r.get('root')=='project-codex')
 for label,folder in [('catalog-claude','skills/claude'),('catalog-codex','skills/codex'),('project-claude','.claude/skills')]:
  p=ROOT/folder/name/'SKILL.md'
  if str(p) in known:continue
  if not p.is_file():raise RuntimeError('Missing repair entry '+str(p))
  r=copy.deepcopy(source);r['path']=p.as_posix();r['root']=label;r['editable']=True;r['readonly']=False
  r['sha256']=hashlib.sha256(p.read_bytes()).hexdigest();r['verified_sha256']=r['sha256'];r['routed']='design/README.md' in p.read_text(encoding='utf-8-sig')
  r['route']='catalogued-and-activated-2026-10-24';r['reason']='Existing complete skill tree mirrored for Claude/Codex parity; '+r['reason']
  for key in ['before_sha256','preserved_original_bytes','prior_audit_sha256']:r.pop(key,None)
  records.append(r);known.add(str(p));added+=1
data['last_targeted_refresh']='2026-10-24: known skill repair paths rehashed and six new catalog/activation entries added; full nine-root metadata audit remains the earlier scoped pass.'
if path.read_bytes()!=old:raise RuntimeError('Concurrent inventory edit')
path.write_bytes(json.dumps(data,indent=2,ensure_ascii=False).encode('utf-8'))
print(json.dumps({'records':len(records),'rehashed':changed,'newly_registered':added}))
