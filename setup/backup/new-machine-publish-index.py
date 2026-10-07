"""Publish an immutable index selecting only fully verified core and personal chains."""
import hashlib, json, os, shutil, subprocess, time, uuid
from pathlib import Path
stage=Path.home()/'LaptopBackups'/'2026-10-07'
root_id='1vQ_Xm9GqDd7SlahE4sp6znQKiYkW8xOe'
binary=os.environ.get('GWS_EXECUTABLE') or shutil.which('gws')
if not binary: raise SystemExit('gws unavailable')
hidden=subprocess.CREATE_NO_WINDOW if os.name=='nt' else 0
def call(*args):
    result=subprocess.run([binary,*args],capture_output=True,text=True,cwd=stage,timeout=300,creationflags=hidden)
    if result.returncode: raise RuntimeError('gws index publication request failed')
    return json.loads(result.stdout)
if call('drive','about','get','--params',json.dumps({'fields':'user(emailAddress)'}))['user']['emailAddress'].lower()!='contact@aspiringattorneys.com':
    raise SystemExit('Wrong Google account')
def proof(directory):
    try:
        receipt=json.loads((directory/'CLOUD-VERIFIED.json').read_text())
        if receipt.get('complete') is not True or receipt.get('account')!='contact@aspiringattorneys.com' or receipt.get('generation')!=directory.name: return None
        if not receipt.get('files') or not all(f.get('id') and len(f.get('md5Checksum',''))==32 for f in receipt['files']): return None
        return receipt
    except (OSError,ValueError,TypeError): return None
selected={}
for path in sorted(stage.glob('*/manifest.json'),reverse=True):
    manifest=json.loads(path.read_text())
    scope=manifest['scope']
    if scope not in ['core','personal'] or scope in selected or not manifest['complete']: continue
    dependencies={r['generation'] for r in manifest['files'].values()}|{path.parent.name}
    if not all(proof(stage/dependency) for dependency in dependencies): continue
    receipt=proof(path.parent)
    selected[scope]={'generation':path.parent.name,'folder_id':receipt['folder_id'],
        'files':len(manifest['files']),'archive_bytes':manifest['archive_bytes'],
        'dependencies':sorted(dependencies)}
if set(selected)!= {'core','personal'}: raise SystemExit('Both verified backup scopes are required')
stamp=time.strftime('%Y%m%d-%H%M%S')+'-'+uuid.uuid4().hex[:6]
index=stage/('Restore-Index-'+stamp+'.json')
index.write_text(json.dumps({'created':time.strftime('%Y-%m-%d %H:%M:%S'),'account':'contact@aspiringattorneys.com','root_folder_id':root_id,'scopes':selected},indent=2))
guide=stage/('Restore-Guide-'+stamp+'.md')
guide.write_text('''# Restore the verified replacement laptop backup

Download the generation folders listed below from this private folder:
https://drive.google.com/drive/folders/'''+root_id+'''

Keep every generation folder name unchanged inside one local folder, such as C:\\Backups.
Download every dependency listed in the index, including partial historical generation
folders: their verified archive files are required by the final complete manifest.
Install Python 3.12 or newer. Use new-machine-restore.py from the selected core folder.

```powershell
python C:\\Backups\\'''+selected['core']['generation']+'''\\new-machine-restore.py --generation C:\\Backups\\'''+selected['core']['generation']+''' --output C:\\RestoredCore
python C:\\Backups\\'''+selected['core']['generation']+'''\\new-machine-restore.py --generation C:\\Backups\\'''+selected['personal']['generation']+''' --output C:\\RestoredPersonal
```

Both output folders must be new. The script verifies parts, reassembles archives and
verifies every restored file SHA256. Map RestoredCore's ai-os to your new user's dev/ai-os;
use manifest roots for Codex, Claude, Superwhisper and the other folders. Apply database
files only while the corresponding app is closed. Copy personal folders separately.
Review saved user environment paths before applying them, especially Git Bash and PATH.
Install apps and reconnect accounts when Windows-bound credentials cannot be reused.

The index selects only generations whose whole dependency chain was cloud verified.
Use the newest Restore-Index and matching Restore-Guide in the root folder, rather than
selecting an in-flight generation solely by its timestamp. No files are deleted by these
scripts. No credential or personal file is sent to GitHub.
''',encoding='utf-8')
remote=[]
for path in [index,guide]:
    digest=hashlib.md5(path.read_bytes()).hexdigest(); size=path.stat().st_size
    params={'q':"trashed=false and '%s' in parents and name='%s'"%(root_id,path.name),'fields':'files(id,name,size,md5Checksum)','pageSize':100}
    found=call('drive','files','list','--params',json.dumps(params))['files']
    matching=[f for f in found if f.get('md5Checksum')==digest and int(f.get('size',-1))==size]
    result=matching[0] if matching else call('drive','files','create','--json',json.dumps({'name':path.name,'parents':[root_id]}),'--upload',str(path),'--params',json.dumps({'fields':'id,name,size,md5Checksum'}))
    verified=call('drive','files','get','--params',json.dumps({'fileId':result['id'],'fields':'id,name,size,md5Checksum'}))
    if verified.get('md5Checksum')!=digest or int(verified.get('size',-1))!=size: raise SystemExit('Index upload checksum mismatch')
    remote.append(verified)
print(json.dumps({'verified_restore_index':str(index),'scopes':selected,'cloud_files':remote}))
