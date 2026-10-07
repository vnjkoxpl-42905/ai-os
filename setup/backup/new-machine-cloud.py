"""Upload immutable generation chunks to private Drive; verify MD5 and size."""
import argparse, concurrent.futures, hashlib, json, shutil, subprocess, sys, os, uuid
from pathlib import Path
p=argparse.ArgumentParser()
p.add_argument('--generation',required=True)
p.add_argument('--parent',default='1UtlkMAzoo4dMMWgj2kTw9U4QR9p-sAUf')
p.add_argument('--dependency-of', help='Complete manifest that requires valid files in a partial base archive')
a=p.parse_args()
generation=Path(a.generation).resolve()
gws_binary=os.environ.get('GWS_EXECUTABLE') or shutil.which('gws')
if not gws_binary: raise SystemExit('gws executable is missing; reconnect the CLI first')
hidden=subprocess.CREATE_NO_WINDOW if os.name=='nt' else 0
def gws(*args):
    r=subprocess.run([gws_binary,*args],capture_output=True,text=True,timeout=300,cwd=generation,creationflags=hidden)
    if r.returncode: raise RuntimeError(r.stderr[:1000] or r.stdout[:1000])
    return json.loads(r.stdout)
about=gws('drive','about','get','--params',json.dumps({'fields':'user(emailAddress)'}))
if about['user']['emailAddress'].lower()!='contact@aspiringattorneys.com':
    raise SystemExit('Wrong Google account; upload refused')
manifest=json.loads((generation/'manifest.json').read_text())
def verified_receipt(previous):
    try:
        receipt=json.loads((previous/'CLOUD-VERIFIED.json').read_text())
        return receipt.get('complete') is True and receipt.get('generation')==previous.name and receipt.get('account')=='contact@aspiringattorneys.com' and bool(receipt.get('files')) and all(r.get('id') and len(r.get('md5Checksum',''))==32 and int(r.get('size',-1))>=0 for r in receipt['files'])
    except (OSError,ValueError,TypeError): return False
if manifest['complete']:
    for dependency in sorted({r['generation'] for r in manifest['files'].values()}-{generation.name}):
        previous=generation.parent/dependency
        if not verified_receipt(previous):
            subprocess.run([sys.executable,str(Path(__file__)), '--generation',str(previous),
                '--parent',a.parent,'--dependency-of',str(generation/'manifest.json')],check=True,creationflags=hidden)
        if not verified_receipt(previous): raise SystemExit('Dependency cloud receipt is not valid')
if not manifest['complete']:
    if not a.dependency_of: raise SystemExit('Incomplete capture; upload refused')
    final=json.loads(Path(a.dependency_of).read_text())
    required={k:v for k,v in final['files'].items() if v['generation']==generation.name}
    if not final['complete'] or not required: raise SystemExit('No complete dependent manifest')
    if any(manifest['files'].get(k)!=v for k,v in required.items()): raise SystemExit('Dependency records mismatch')
    import zipfile
    with zipfile.ZipFile(generation/'payload.zip') as valid:
        if valid.testzip(): raise SystemExit('Dependency archive CRC failed')
def folder(name,parent):
    q="trashed = false and '%s' in parents and name = '%s' and mimeType = 'application/vnd.google-apps.folder'"%(parent,name)
    found=gws('drive','files','list','--params',json.dumps({'q':q,'fields':'files(id,name)','pageSize':100}))['files']
    if len(found)>1: raise RuntimeError('Duplicate destination folder: '+name)
    if found: return found[0]['id']
    return gws('drive','files','create','--json',json.dumps({'name':name,'parents':[parent],'mimeType':'application/vnd.google-apps.folder'}),'--params',json.dumps({'fields':'id'}))['id']
root=folder('Replacement Laptop Backups',a.parent)
destination=folder(generation.name,root)
parts=generation/'cloud-parts'
parts.mkdir(exist_ok=True)
records=[]
with (generation/'payload.zip').open('rb') as src:
    n=1
    while chunk:=src.read(128*1024*1024):
        target=parts/('payload.zip.part%04d'%n)
        md5=hashlib.md5(chunk).hexdigest(); sha=hashlib.sha256(chunk).hexdigest()
        if target.exists():
            if hashlib.sha256(target.read_bytes()).hexdigest()!=sha: raise RuntimeError('Existing part differs')
        else: target.write_bytes(chunk)
        records.append({'name':target.name,'bytes':len(chunk),'md5':md5,'sha256':sha}); n+=1
(generation/'parts-manifest.json').write_text(json.dumps({'archive_sha256':manifest['archive_sha256'],'parts':records},indent=2))
here=Path(__file__).parent
for name in ['new-machine-backup.py','new-machine-restore.py','new-machine-cloud.py','new-machine-README.md']:
    if not (generation/name).exists(): shutil.copyfile(here/name,generation/name)
targets=[parts/r['name'] for r in records]+[generation/n for n in ['manifest.json','parts-manifest.json','SHA256SUMS.txt','new-machine-backup.py','new-machine-restore.py','new-machine-cloud.py','new-machine-README.md']]
def upload_once(path):
    h=hashlib.md5()
    with path.open('rb') as f:
        while chunk:=f.read(1024*1024): h.update(chunk)
    digest=h.hexdigest(); size=path.stat().st_size
    params={'q':"trashed=false and '%s' in parents and name='%s'"%(destination,path.name),'fields':'files(id,name,size,md5Checksum)','pageSize':100}
    existing=gws('drive','files','list','--params',json.dumps(params))['files']
    match=[r for r in existing if r.get('md5Checksum')==digest and int(r.get('size',-1))==size]
    if match: result=match[0]
    else:
        if existing: raise RuntimeError('Same-name cloud file differs: '+path.name)
        # Unknown upload outcome: subsequent rerun queries checksum before retry.
        result=gws('drive','files','create','--json',json.dumps({'name':path.name,'parents':[destination]}),'--upload',str(path),'--params',json.dumps({'fields':'id,name,size,md5Checksum'}))
    verified=gws('drive','files','get','--params',json.dumps({'fileId':result['id'],'fields':'id,name,size,md5Checksum'}))
    if verified.get('md5Checksum')!=digest or int(verified.get('size',-1))!=size: raise RuntimeError('Cloud checksum failed: '+path.name)
    print('Verified cloud file:',path.name,flush=True)
    return verified
def upload(path):
    failure=None
    for attempt in range(3):
        try: return upload_once(path)
        except (RuntimeError, subprocess.TimeoutExpired) as error:
            failure=error
            print('Retry after cloud request failure:',path.name,'attempt',attempt+1,flush=True)
    raise RuntimeError('Three upload attempts failed for '+path.name) from failure
verified=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
    for result in pool.map(upload,targets): verified.append(result)
receipt={'complete':True,'capture_complete':manifest['complete'],'dependency_of':a.dependency_of,
    'account':'contact@aspiringattorneys.com','root_id':root,'folder_id':destination,'generation':generation.name,'files':verified}
receipt_path=generation/'CLOUD-VERIFIED.json'
receipt_before=receipt_path.read_bytes() if receipt_path.exists() else None
temporary=generation/('CLOUD-VERIFIED-'+uuid.uuid4().hex+'.tmp')
temporary.write_text(json.dumps(receipt,indent=2))
if (receipt_path.read_bytes() if receipt_path.exists() else None)!=receipt_before:
    raise RuntimeError('Cloud receipt changed concurrently; compare-and-swap refused')
os.replace(temporary,receipt_path)
print(json.dumps({'complete':True,'folder_id':destination,'files':len(verified)}))
