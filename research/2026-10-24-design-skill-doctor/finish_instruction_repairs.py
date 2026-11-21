exec(compile(open('research/2026-10-24-design-skill-doctor/repair_instructions.py',encoding='utf-8').read().split('stamp=datetime')[0],'<definitions>','exec'))
import re
receipt=json.loads((out/'instruction-repair-receipts.json').read_text())
with zipfile.ZipFile(out/'instruction-backup-followup.zip','w',zipfile.ZIP_DEFLATED) as z:
 for base in roots:
  paths=[base/'impeccable/SKILL.md',base/'design-taste-frontend/SKILL.md']
  refs=base/'impeccable/reference'
  if refs.is_dir(): paths+=list(refs.glob('*.md'))
  for p in paths:
   if not p.is_file() or p.is_symlink() or p.parent.is_symlink() or p.parent.parent.is_symlink(): continue
   old=p.read_bytes(); t=old.decode('utf-8-sig'); n=t
   if p.parent.name=='reference':
    n=re.sub(r'node \.agents/skills/impeccable/scripts/([\w-]+\.mjs)',r'node "<resolved-skill-directory>/scripts/\1"',n)
   n=n.replace("don't also run `load-context.mjs\"`", "don't also run `load-context.mjs`")
   n=n.replace('Use Framer Motion hooks. NEVER', "Use the project's selected engine (for example GSAP ScrollTrigger or Motion hooks). NEVER")
   if n==t: continue
   new=n.encode('utf-8'); z.writestr(p.as_posix().replace(':',''),old)
   assert p.read_bytes()==old
   p.write_bytes(new)
   receipt['changes'].append({'path':str(p),'before':hashlib.sha256(old).hexdigest(),'after':hashlib.sha256(new).hexdigest(),'kind':'followup path and wording consistency'})
receipt['followup_backup']=str(out/'instruction-backup-followup.zip')
(out/'instruction-repair-receipts.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(len(receipt['changes']))
