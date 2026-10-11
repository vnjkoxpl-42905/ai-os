"""Read-back hashes, backup integrity, frontmatter and bounded regressions."""
from pathlib import Path
import hashlib
import json
import re
import yaml

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[1]
def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

canonical=json.loads((OUT/'CANONICAL.json').read_text(encoding='utf-8'))
globals_=json.loads((OUT/'global-repairs.json').read_text(encoding='utf-8'))
stages=[canonical['changes'],globals_]
for name in ('parent-scaffold-repairs.json','parent-reference-repairs.json','parent-validator-baseline.json',
             'final-direct-receipts.json','activation-final-receipts.json','claudex-final-receipts.json',
             'watch-prose-receipts.json','reviewer-final-receipts.json','frontmatter-final-receipts.json'):
    stages.append(json.loads((OUT/name).read_text(encoding='utf-8')))
trace=ROOT.parent/'ai-os-projects/karpathy-method-tools/trace_runner.py'
trace_backup=OUT/'backups/parent/karpathy-method-tools/trace_runner.py'
stages.append([dict(path=str(trace),backup=str(trace_backup),before_sha256=sha(trace_backup))])
errors=[]
combined={}
for stage in stages:
    for row in stage:
        path=Path(row['path'])
        before=row.get('before_sha256',row.get('before'))
        backup=row.get('backup')
        if backup:
            if not Path(backup).is_file() or sha(backup).lower()!=str(before).lower():
                errors.append('Invalid backup: '+str(path))
        if not path.is_file():
            errors.append('Missing repaired file: '+str(path))
            continue
        key=str(path.resolve()).lower()
        if key not in combined:
            combined[key]=dict(path=str(path),before_sha256=before,backup=backup,
                               after_sha256=sha(path),created=before is None)

frontmatter_count=0
frontmatter_targets={Path(row['path']).resolve() for row in combined.values() if Path(row['path']).name=='SKILL.md'}
scopes=[ROOT/'skills'/rt for rt in ('claude','codex','gemini')]
scopes += [ROOT/rt/'skills' for rt in ('.agents','.claude','.gemini')]
scopes += [Path.home()/rt/'skills' for rt in ('.agents','.codex','.claude')]
for scope in scopes:
    if scope.exists():
        frontmatter_targets.update(p.resolve() for p in scope.rglob('SKILL.md')
                                  if not any(part in p.parts for part in ('_snapshots','_project-forks','_inactive')))
for p in sorted(frontmatter_targets):
    text=p.read_text(encoding='utf-8-sig')
    try:
        m=re.match(r'\A---\s*\n(.*?)\n---(?:\s*\n|$)',text,re.S)
        if not m:
            raise ValueError('No frontmatter block')
        data=yaml.safe_load(m.group(1))
        if not isinstance(data,dict) or not all(isinstance(data.get(k),str) and data[k].strip() for k in ('name','description')):
            raise ValueError('Missing string name/description')
        frontmatter_count+=1
    except (ValueError,yaml.YAMLError) as exc:
        errors.append(f'Frontmatter {p}: {exc}')

# Reconcile each frozen catalog disposition without changing its audit judgment.
for row in canonical['changes']:
    row['after']=sha(row['path'])
for row in globals_:
    row['after_sha256']=sha(row['path'])
    suffix='; final readback/frontmatter and independent corrections reconciled'
    if suffix not in row['validation']:
        row['validation']+=suffix
for row in canonical['literal_checks']:
    p=Path(row['path'])
    row['pass']=row['removed'] not in p.read_text(encoding='utf-8')
    if not row['pass']:
        errors.append('Literal regression: '+str(p)+': '+row['removed'])

known_forbidden={
 'chat-export':['Always trigger this skill proactively','**Reconstruct the full transcript**','/Users/joshuaf/ai-os/handoffs/'],
 'youtube-full':['Use when YouTube is or could be relevant','required_environment_variables:'],
 'claude-api':['**ALWAYS use `claude-opus-5`','**Don\'t research SDK types','use a supported model instead and note the substitution'],
 'gws-shared':['**Always** confirm with user before executing write/delete'],
 'watch':['clean up the working directory when you\'re done','default: prefer Groq if both keys exist','The Read tool renders JPEGs directly']
}
regressions=0
for row in combined.values():
    p=Path(row['path'])
    if p.name=='SKILL.md' and p.parent.name in known_forbidden:
        text=p.read_text(encoding='utf-8')
        for literal in known_forbidden[p.parent.name]:
            regressions+=1
            if literal in text:
                errors.append(f'Direct regression {p}: {literal}')

old=json.loads((ROOT/'audits/skills-2026-10-09/all-skill-dispositions.json').read_text(encoding='utf-8'))
preserved=0
for row in old:
    if '_snapshots' in Path(row['path']).parts:
        expected=row.get('sha256',row.get('hash'))
        if expected and Path(row['path']).is_file() and sha(row['path']).lower()==expected.lower():
            preserved+=1
        else:
            errors.append('Historical snapshot changed: '+row['path'])

report=dict(changes=list(combined.values()),changed_files=len(combined),frontmatter_checked=frontmatter_count,
            direct_regression_checks=regressions,literal_checks=len(canonical['literal_checks']),
            original_catalog_dispositions=len(canonical['mapping']),historical_snapshots_preserved=preserved,errors=errors)
(OUT/'FINAL-VERIFICATION.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
if not errors:
    (OUT/'CANONICAL.json').write_text(json.dumps(canonical,indent=2),encoding='utf-8')
    (OUT/'global-repairs.json').write_text(json.dumps(globals_,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='changes'},indent=2))
raise SystemExit(1 if errors else 0)
