from pathlib import Path
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[2]
slugs=['17-claude-design-use-cases-austin-marchese','25-claude-design-tricks-robonuggets','claude-design-fifteen-hacks-jack','astra-website-design-loop-jack','astra-blender-web-design-chase-ai','astra-web-design-taste-vault-chase-ai','higgsfield-clone-albert-olgaard','rea-feature-investigation-chase-ai','rea-output-first-workflow-nate-herk','claude-now-does-video-free-javascript','100-github-repos-for-claude-nate-herk']
related={
'17-claude-design-use-cases-austin-marchese':['25-claude-design-tricks-robonuggets','claude-design-fifteen-hacks-jack'],
'25-claude-design-tricks-robonuggets':['17-claude-design-use-cases-austin-marchese','claude-design-fifteen-hacks-jack'],
'claude-design-fifteen-hacks-jack':['astra-web-design-taste-vault-chase-ai','astra-website-design-loop-jack'],
'astra-web-design-taste-vault-chase-ai':['claude-design-fifteen-hacks-jack','astra-website-design-loop-jack'],
'astra-website-design-loop-jack':['astra-blender-web-design-chase-ai','higgsfield-clone-albert-olgaard'],
'astra-blender-web-design-chase-ai':['astra-web-design-taste-vault-chase-ai'],
'higgsfield-clone-albert-olgaard':['astra-website-design-loop-jack'],
'rea-feature-investigation-chase-ai':['rea-output-first-workflow-nate-herk'],
'rea-output-first-workflow-nate-herk':['rea-feature-investigation-chase-ai','astra-website-design-loop-jack']}
def cas(path,old,new):
 if path.read_bytes()!=old: raise RuntimeError('Concurrent write '+str(path))
 path.write_bytes(new.encode('utf-8'))
def clean(b):
 # Correct repeated CR translation in compiled Markdown only. Never touch evidence.
 while b'\r\r\n' in b:b=b.replace(b'\r\r\n',b'\r\n')
 return b.decode('utf-8-sig').replace('\r\n','\n')
for slug in slugs:
 p=ROOT/'wiki/sources'/f'{slug}.md';old=p.read_bytes();text=clean(old)
 if slug in related and '## Related design sources (2026-10-24)' not in text:
  text+='\n\n## Related design sources (2026-10-24)\n\nComplementary captured accounts, not independent verification of product claims: '+', '.join(f'[{s}]({s}.md)' for s in related[slug])+'. Compare their concrete methods through the [design hub](../../design/README.md).\n'
 cas(p,old,text)
q=ROOT/'references/ai-workspace/action-queue.md';old=q.read_bytes();cas(q,old,clean(old))
# Keep the new navigation in curated index text rather than below the generated catalogue.
p=ROOT/'wiki/index.md';old=p.read_bytes();text=clean(old)
m=re.search(r'<!-- DESIGN HUB NAVIGATION -->.*?<!-- END DESIGN HUB NAVIGATION -->',text,re.S)
if m:
 block=m.group(0);text=text[:m.start()]+text[m.end():]
 text=text.replace('## Hubs','## Hubs\n\n'+block,1);cas(p,old,text)
receipts=[]
for slug in slugs:
 p=ROOT/'wiki/sources'/f'{slug}.md';text=p.read_text(encoding='utf-8-sig')
 ev=re.search(r'^evidence:\s*["\']?([^\n"\']+)',text,re.M);sha=re.search(r'^sha256:\s*["\']?([a-fA-F0-9]{64})',text,re.M)
 if not(ev and sha):raise RuntimeError('Missing evidence '+slug)
 evidence=(p.parent/ev.group(1).strip()).resolve();actual=hashlib.sha256(evidence.read_bytes()).hexdigest()
 if actual!=sha.group(1).lower():raise RuntimeError('Evidence hash '+slug)
 quotes=re.findall(r'^> "(.*?)"',text,re.M)
 source=evidence.read_text(encoding='utf-8-sig')
 for quote in quotes:
  if quote not in source:raise RuntimeError('Quote '+slug+' '+quote)
 receipts.append({'source':str(p.relative_to(ROOT)),'evidence':str(evidence.relative_to(ROOT)),'sha256':actual,'quotes_checked':len(quotes)})
# Verify every newly archived generation against its manifest AND a retained inbox original.
inbox={hashlib.sha256(p.read_bytes()).hexdigest():p for p in (ROOT/'raw/inbox').glob('*.md')}
archive_receipts=[]
archive_dirs=[(ROOT/r['evidence']).parent for r in receipts[:9]]
c=json.loads((ROOT/'research/2026-10-24-design-hub/ingest-c-archives.json').read_text())
archive_dirs += [ROOT/x['archive'] for x in c]
for folder in archive_dirs:
 for line in (folder/'SHA256SUMS').read_text().splitlines():
  if not line.strip():continue
  digest,name=line.split(maxsplit=1);name=name.lstrip('*').strip();file=folder/name
  actual=hashlib.sha256(file.read_bytes()).hexdigest()
  if actual!=digest:raise RuntimeError('Manifest mismatch '+str(file))
  if actual not in inbox:raise RuntimeError('No unchanged inbox original '+str(file))
  archive_receipts.append({'archive':str(file.relative_to(ROOT)),'input':str(inbox[actual].relative_to(ROOT)),'sha256':actual})
out=ROOT/'research/2026-10-24-design-hub/verification.json'
out.write_text(json.dumps({'source_checks':receipts,'archive_checks':archive_receipts},indent=2),encoding='utf-8')
log=ROOT/'wiki/log.md';old=log.read_bytes();text=old.decode('utf-8-sig')
for row in receipts:
 slug=Path(row['source']).stem;marker=f'## [2026-10-24] ingest | Design batch: {slug}'
 if marker not in text:
  text+='\n\n'+marker+'\n\n- Source: [summary](sources/'+slug+'.md); SHA-256 `'+row['sha256']+'`.\n- Preserved evidence and exact quotes checked; originals unchanged. New/revised state, full transcript coverage and limitations: [batch report](../research/2026-10-24-design-hub/REPORT.md).\n- Connected to [design hub](../design/README.md), related source methods and existing action queue. Proposals are not implementations.\n'
cas(log,old,text.replace('\r\n','\n'))
print(f'Verified {len(receipts)} source summaries and {len(archive_receipts)} exact archived input generations; logs appended.')
