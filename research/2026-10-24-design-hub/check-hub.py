from pathlib import Path
import re,hashlib,json
ROOT=Path(__file__).resolve().parents[2]
paths=list((ROOT/'design').glob('*.md'))
errors=[];links=0
for p in paths:
 text=p.read_text(encoding='utf-8-sig')
 for target in re.findall(r'\[[^\]\n]+\]\((<[^>]+>|[^)\n]+)\)',text):
  target=target.strip('<>').split('#')[0]
  if not target or '://' in target:continue
  links+=1
  if not (p.parent/target).exists():errors.append({'page':str(p.relative_to(ROOT)),'target':target})
skills=[]
for skill in ['second-brain-ingest','design-resource-library']:
 for runtime,active,home in [('codex','.agents','C:/Users/Joshu/.agents'),('claude','.claude','C:/Users/Joshu/.claude')]:
  canonical=ROOT/'skills'/runtime/skill/'SKILL.md'
  expected=hashlib.sha256(canonical.read_bytes()).hexdigest()
  for candidate in [ROOT/active/'skills'/skill/'SKILL.md',Path(home)/'skills'/skill/'SKILL.md']:
   if not candidate.exists():continue
   actual=hashlib.sha256(candidate.read_bytes()).hexdigest()
   skills.append({'skill':skill,'runtime':runtime,'path':str(candidate),'matching':actual==expected})
   if actual!=expected:errors.append({'skill_mismatch':str(candidate)})
route='Design knowledge, skills, repositories, references and new design clips: start at `design/README.md`.'
for name in ['AGENTS.md','CLAUDE.md']:
 if route not in (ROOT/name).read_text(encoding='utf-8-sig'):errors.append({'route_missing':name})
result={'hub_files':len(paths),'links_checked':links,'skill_copies':skills,'errors':errors}
(ROOT/'research/2026-10-24-design-hub/hub-check.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({'hub_files':len(paths),'links_checked':links,'matching_skill_copies':len(skills),'errors':errors}))
if errors:raise SystemExit(1)
