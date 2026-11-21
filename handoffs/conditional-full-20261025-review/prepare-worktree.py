from pathlib import Path
import hashlib, json, shutil, subprocess

source=Path('C:/Users/Joshu/dev/ai-os-projects/lsatu-and-or-20261019')
target=Path('C:/Users/Joshu/dev/ai-os-projects/lsatu-conditional-full-20261025')
out=Path(__file__).parent
def git(root,*args):
    return subprocess.check_output(['git','-C',str(root),*args])
changed=git(source,'diff','--name-only','HEAD').decode().splitlines()
untracked=git(source,'ls-files','--others','--exclude-standard').decode().splitlines()
allowed=('src/bootcamps/conditionals/','docs/conditionals/','public/media/conditionals/and-or/')
for rel in changed+untracked:
    if not rel.startswith(allowed):
        raise SystemExit('Unexpected source change: '+rel)
patch=git(source,'diff','--binary','HEAD')
(out/'chapter2-preserved.patch').write_bytes(patch)
manifest={'source_head':git(source,'rev-parse','HEAD').decode().strip(),'target_base':git(target,'rev-parse','HEAD').decode().strip(),'files':[]}
for rel in changed+untracked:
    manifest['files'].append({'path':rel,'sha256':hashlib.sha256((source/rel).read_bytes()).hexdigest()})
(out/'chapter2-source-manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
result=subprocess.run(['git','-C',str(target),'apply','--3way',str(out/'chapter2-preserved.patch')],capture_output=True,text=True)
print(result.stdout,result.stderr)
if result.returncode:
    raise SystemExit(result.returncode)
for rel in untracked:
    dest=target/rel
    if dest.exists():
        raise SystemExit('Existing target for untracked file: '+rel)
    dest.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(source/rel,dest)
print(json.dumps({'preserved_files':len(manifest['files']),'base':manifest['target_base']}))
