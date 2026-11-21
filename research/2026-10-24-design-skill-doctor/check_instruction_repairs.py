from pathlib import Path
import json,hashlib,zipfile,difflib
root=Path('C:/Users/Joshu/dev/ai-os'); out=root/'research/2026-10-24-design-skill-doctor'
r=json.loads((out/'instruction-repair-receipts.json').read_text()); latest={x['path']:x for x in r['changes']}
checks=[]
for name,x in latest.items():
 p=Path(name); t=p.read_text(encoding='utf-8'); kind=p.parent.name
 assert hashlib.sha256(p.read_bytes()).hexdigest()==x['after'],name
 if '/impeccable/' in p.as_posix():
  assert 'node .agents/skills/impeccable/scripts/' not in t,name
  if p.name=='SKILL.md':
   assert 'explicit user delegation' in t
   assert 'node "<resolved-skill-directory>/scripts/load-context.mjs"' in t
   assert (p.parent/'scripts/load-context.mjs').is_file()
  if p.name=='shape.md': assert 'at least one user-answer round' not in t
 if '/design-taste-frontend/' in p.as_posix():
  for banned in ['transition: all','Use EXCLUSIVELY Framer','Use GSAP/ThreeJS EXCLUSIVELY','Serif fonts are strictly BANNED','NEVER** use Serif on clean Dashboards']:
   assert banned not in t,(name,banned)
  assert "project's selected engine" in t
 if '/high-end-visual-design/' in p.as_posix():
  assert 'Build the DOM strictly using' not in t
  assert 'All major cards and containers use the Double-Bezel' not in t
 if '/react-bits/' in p.as_posix():
  assert 'node scripts/' not in t
  assert (p.parent/'scripts/rb-add.mjs').is_file()
 checks.append({'path':name,'hash':'pass','instruction_checks':'pass'})
original={}
for archive in [r['backup'],r['followup_backup']]:
 with zipfile.ZipFile(archive) as z:
  for name in z.namelist(): original.setdefault(name,z.read(name))
diffs=[]
for name in latest:
 p=Path(name); key=p.as_posix().replace(':',''); old=original[key].decode('utf-8-sig').splitlines(True); new=p.read_text(encoding='utf-8').splitlines(True)
 diffs.extend(difflib.unified_diff(old,new,fromfile=name+' (before)',tofile=name+' (after)'))
(out/'instruction-repair.diff').write_text(''.join(diffs),encoding='utf-8')
(out/'instruction-repair-checks.json').write_text(json.dumps({'distinct_files':len(checks),'checks':checks,'limitations':'Static instruction/path checks only. No model behavior, animation performance or provider fetch measured.'},indent=2),encoding='utf-8')
print(f'PASS: {len(checks)} distinct files; current hashes, repaired invariants and installed helper paths verified.')
