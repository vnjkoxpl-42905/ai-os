from pathlib import Path
import json,hashlib,difflib,re,sys
root=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(root/'system/scripts'))
import importlib.util
spec=importlib.util.spec_from_file_location('checks',root/'system/scripts/check-skills.py')
checks=importlib.util.module_from_spec(spec); spec.loader.exec_module(checks)
out=[]
for runtime,home in [('claude',Path.home()/'.claude/skills'),('codex',Path.home()/'.agents/skills'),('codex',Path.home()/'.codex/skills')]:
 for d in sorted(home.iterdir()):
  a=d/'SKILL.md'; b=root/'skills'/runtime/d.name/'SKILL.md'
  if not a.is_file() or not b.is_file() or checks.entrypoints_match(a,b):continue
  x=a.read_text(encoding='utf-8');y=b.read_text(encoding='utf-8')
  diff=list(difflib.unified_diff(y.splitlines(),x.splitlines(),fromfile='catalog',tofile='home',n=2))
  out.append(dict(runtime=runtime,name=d.name,home=str(a),catalog=str(b),home_hash=hashlib.sha256(a.read_bytes()).hexdigest(),catalog_hash=hashlib.sha256(b.read_bytes()).hexdigest(),dispatcher=bool(re.search('compatibility dispatcher|This is a pointer',x+y)),diff=diff))
(Path(__file__).parent/'drift.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
for r in out:
 print(r['runtime'],r['name'],len(r['diff']), 'DISPATCH' if r['dispatcher'] else '')
 if r['name'] in ['bootcamp-builder','general-video','hyperframes','hyperframes-animation','hyperframes-cli','hyperframes-core','hyperframes-studio','impeccable','media-use']:
  print('\n'.join(r['diff'])[:12000])
