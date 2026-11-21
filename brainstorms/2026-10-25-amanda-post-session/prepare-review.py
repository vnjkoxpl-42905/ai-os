from pathlib import Path
import hashlib,json,shutil
root=Path(__file__).resolve().parents[2]
folder=Path(__file__).resolve().parent
review=Path('C:/Users/Joshu/AppData/Local/Temp/codex-amanda-review-20261025-01')
manifest=folder/'recap-source-manifest.json'
paths={e['path'] for e in json.loads(manifest.read_text(encoding='utf-8-sig'))}
extra=['design/methods.md','recap-review-log.md','recap-source-review.md','recap-improvement-plan.md','verify-recap.cjs','before-21st-recap.src.html','before-21st-recap.html','before-21st-canonical-recap.md']
for name in extra:
 p=root/name if name.startswith('design/') else folder/name
 paths.add(p.relative_to(root).as_posix())
for directory in ['component-references','render-evidence']:
 for p in (folder/directory).rglob('*'):
  if p.is_file(): paths.add(p.relative_to(root).as_posix())
entries=[]
for rel in sorted(paths):
 p=root/rel
 if not p.is_file(): raise RuntimeError('Missing '+rel)
 dest=review/rel
 dest.parent.mkdir(parents=True,exist_ok=True)
 shutil.copy2(p,dest)
 digest=hashlib.sha256(p.read_bytes()).hexdigest()
 assert hashlib.sha256(dest.read_bytes()).hexdigest()==digest
 entries.append({'path':rel,'sha256':digest})
manifest.write_text(json.dumps(entries,indent=2)+'\n',encoding='utf-8')
shutil.copy2(manifest,review/manifest.relative_to(root))
print('Frozen review mirror: '+str(len(entries))+' byte-verified files.')
