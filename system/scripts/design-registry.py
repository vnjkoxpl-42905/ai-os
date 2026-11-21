"""Render hub registries from reviewed inventories, with compare-before-write."""
from pathlib import Path
from datetime import date
import json,os
ROOT=Path(__file__).resolve().parents[2]
HUB=ROOT/'design'
AUDIT=ROOT/'research/2026-10-24-design-completeness'
START='<!-- BEGIN GENERATED DESIGN CATALOG -->'
END='<!-- END GENERATED DESIGN CATALOG -->'
def link(path,label=None):
 p=Path(path);rel=os.path.relpath(p,HUB).replace('\\','/')
 return f'[{label or p.name}](<{rel}>)'
def render(name,title,lines):
 p=HUB/name;old=p.read_bytes() if p.exists() else None
 text=old.decode('utf-8-sig').replace('\r\n','\n') if old else '# '+title+'\n\n'
 block=START+'\n'+'\n'.join(lines)+'\n'+END
 if START in text:
  a=text.index(START)
  if END not in text[a:]:raise RuntimeError('Unclosed generated section')
  b=text.index(END,a)+len(END);text=text[:a]+block+text[b:]
 else:text+=block+'\n'
 if p.exists() and p.read_bytes()!=old:raise RuntimeError('Concurrent edit '+str(p))
 p.write_bytes(text.encode('utf-8'))
def load(name):
 data=json.loads((AUDIT/(name+'.json')).read_text(encoding='utf-8-sig'))
 return data.get('records',data.get('skills',[]))
def main():
 skills=load('skills');docs=load('documents');repos=load('repos')
 stamp=f'Rendered {date.today().isoformat()} from the scoped 2026-10-24 audits. Counts are paths/records, including runtime copies, not unique capabilities. Rendering does not rescan or authenticate tools.'
 sl=[stamp,'','See [skill routing audit](skill-routing-audit.md). Vendor/plugin caches remain read-only; shared global instructions provide their hub route.','']
 for kind in ['primary','supporting']:
  group=[r for r in skills if r.get('classification')==kind];sl += [f'## {kind.title()} design skills ({len(group)} paths)','']
  for r in sorted(group,key=lambda x:x['path'].lower()):
   p=Path(r['path'])
   if not p.exists():raise RuntimeError('Missing audited path '+str(p))
   sl.append(f'- {link(p,p.parent.name+" / "+str(r.get("runtime",r.get("root","installed copy"))))}: {r.get("reason","See audit.")}')
  sl.append('')
 dl=[stamp,'','Linked in place. Indexed does not mean fully ingested or approved. See [document coverage](document-routing-audit.md).','']
 for status in sorted({r.get('status','reference') for r in docs if r['classification']!='excluded'}):
  group=[r for r in docs if r['classification']!='excluded' and r.get('status','reference')==status];dl += [f'## {status.title()} ({len(group)})','']
  for r in sorted(group,key=lambda x:x['path'].lower()):
   p=Path(r['path'])
   if not p.exists():raise RuntimeError('Missing audited path '+str(p))
   dl.append(f'- {link(p,r.get("title") or p.name)}: {r.get("reason","Existing document.")} Coverage: {r.get("coverage","See audit")}.')
  dl.append('')
 rl=[stamp,'','See [repository guide and licence distinctions](repositories.md). Metadata review is not a full code or runtime audit.','']
 for kind in ['design-resource','design-project','general']:
  group=[r for r in repos if r['classification']==kind];rl += [f'## {kind} ({len(group)})','']
  for r in group:
   p=Path(r['path'])
   if not p.exists():raise RuntimeError('Missing audited path '+str(p))
   rl.append(f'- {link(p,p.name)}: {r.get("reason","See audit")}.')
  rl.append('')
 render('skills.generated.md','Design skill registry',sl);render('documents.generated.md','Design document registry',dl);render('repos.generated.md','Repository and project registry',rl)
 refs={}
 for r in skills:
  if r.get('classification') not in ['primary','supporting']:continue
  base=Path(r['path']).parent
  if base.is_symlink():continue
  for current,dirs,files in os.walk(base,followlinks=False):
   dirs[:]=[d for d in dirs if d not in ['node_modules','.git','_snapshots','test-corpus'] and not (Path(current)/d).is_symlink()]
   for name in files:
    p=Path(current)/name
    if p.suffix.lower()=='.md' and p.name!='SKILL.md' and not p.is_symlink():refs[str(p)]=base
 ref_lines=[stamp,'','Supporting Markdown listed beneath semantically selected skills. These are existing instructions, examples and resources, not newly ingested video sources or individually reviewed principles. Follow the owning SKILL.md before applying them. Frozen snapshots, dependency trees and test corpora are excluded.','']
 for path,base in sorted(refs.items()):
  ref_lines.append(f'- {link(path,base.name+" / "+Path(path).relative_to(base).as_posix())}')
 render('skill-references.generated.md','Skill reference document registry',ref_lines)
 selected=sum(r.get('classification') in ['primary','supporting'] for r in skills)
 lines=[stamp,'','## Open the relevant registry','',f'- [Skills](skills.generated.md): {len(skills)} entries considered; {selected} primary/supporting design paths. [Routing audit](skill-routing-audit.md).',f'- [Documents](documents.generated.md): {len(docs)} candidates. [Principles](principles.md) and [coverage](document-routing-audit.md).',f'- [Skill supporting Markdown](skill-references.generated.md): {len(refs)} existing reference/example/resource files; indexed rather than individually ingested.',f'- [Repositories](repos.generated.md): {len(repos)} records. [Readable guide](repositories.md).','- [Preserved source ingestion](sources.md): canonical summaries, archives, coverage and limits.','- [Methods](methods.md): reference selection, refinement, motion and critique.','','## Evidence and exclusions','',link(AUDIT/'skills.json','Full skill inventory'),'',link(AUDIT/'documents.json','Document inventory and coverage'),'',link(AUDIT/'repos.json','Repository/project inventory'),'', 'These registries use reviewed semantic classifications rather than filename matching. Update the relevant inventory during new ingestion or a scoped rescan; rendering alone does not discover newly installed files.']
 render('catalog.generated.md','Design file catalogue',lines)
 print(json.dumps({'skill_entries':len(skills),'design_skill_paths':selected,'document_candidates':len(docs),'skill_support_documents':len(refs),'repository_records':len(repos)}))
if __name__=='__main__':main()
