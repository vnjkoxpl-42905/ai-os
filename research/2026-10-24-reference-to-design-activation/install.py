from pathlib import Path
import hashlib,json,re,subprocess
ROOT=Path(__file__).resolve().parents[2]
SOURCE=ROOT.parent/'ai-os-projects/taste-vault/skills/reference-to-design'
NAME='reference-to-design'
targets=[ROOT/'skills/claude'/NAME,ROOT/'skills/codex'/NAME,ROOT/'.claude/skills'/NAME,ROOT/'.agents/skills'/NAME,Path.home()/'.claude/skills'/NAME,Path.home()/'.agents/skills'/NAME,Path.home()/'.codex/skills'/NAME]
files={p.relative_to(SOURCE):p.read_bytes() for p in SOURCE.rglob('*') if p.is_file() and not p.is_symlink()}
route='\n\n<!-- BEGIN GENERATED DESIGN HUB ROUTE -->\nShared design knowledge: first read `C:/Users/Joshu/dev/ai-os/design/README.md`. Follow the current user brief, then the relevant principles, references and tools.\n<!-- END GENERATED DESIGN HUB ROUTE -->\n'
files[Path('SKILL.md')]+=route.encode('utf-8')
files[Path('LICENSE')]=(SOURCE.parents[1]/'LICENSE').read_bytes()
sha=subprocess.check_output(['git','-C',str(SOURCE.parents[1]),'rev-parse','HEAD'],text=True).strip()
receipt=[]
for target in targets:
 if target.exists():raise RuntimeError('Existing install needs comparison: '+str(target))
 target.mkdir(parents=True)
 for rel,blob in files.items():
  dest=target/rel;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(blob)
  assert hashlib.sha256(dest.read_bytes()).digest()==hashlib.sha256(blob).digest()
 receipt.append({'path':target.as_posix(),'files':len(files),'sha256':hashlib.sha256((target/'SKILL.md').read_bytes()).hexdigest()})
inventory=ROOT/'research/2026-10-24-design-completeness/skills.json';old=inventory.read_bytes();data=json.loads(old.decode('utf-8-sig'))
labels=['catalog-claude','catalog-codex','project-claude','project-codex','home-claude','home-agents','home-codex']
for target,label in zip(targets,labels):
 p=target/'SKILL.md';digest=hashlib.sha256(p.read_bytes()).hexdigest()
 data['records'].append({'path':p.as_posix(),'root':label,'name':NAME,'classification':'primary','reason':'Reference-led frontend design exploration and refinement; explicitly activated by Joshua.','editable':True,'readonly':False,'routed':True,'route':'activated-2026-10-24','sha256':digest,'verified_sha256':digest})
if inventory.read_bytes()!=old:raise RuntimeError('Concurrent inventory edit')
inventory.write_bytes(json.dumps(data,indent=2,ensure_ascii=False).encode('utf-8'))
out=Path(__file__).parent/'receipt.json';out.write_bytes(json.dumps({'source':SOURCE.as_posix(),'commit':sha,'targets':receipt},indent=2).encode('utf-8'))
print(f'Installed {NAME}: {len(targets)} matching catalogue/activation copies, {len(files)} files each; source commit {sha}.')
