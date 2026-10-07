"""Scheduled private backup coordinator. No source changes or pruning."""
import json, msvcrt, subprocess, sys, time, os
from pathlib import Path
here=Path(__file__).resolve().parent
runtime=here/'new-machine-runtime.json'
runtime_config=json.loads(runtime.read_text(encoding='utf-8-sig')) if runtime.exists() else {}
if runtime_config: os.environ['GWS_EXECUTABLE']=runtime_config['gws']
python_binary=runtime_config.get('python',sys.executable)
hidden=subprocess.CREATE_NO_WINDOW if os.name=='nt' else 0
def verified_receipt(generation):
    try:
        receipt=json.loads((generation/'CLOUD-VERIFIED.json').read_text())
        return receipt.get('complete') is True and receipt.get('generation')==generation.name and receipt.get('account')=='contact@aspiringattorneys.com' and bool(receipt.get('files')) and all(r.get('id') and len(r.get('md5Checksum',''))==32 and int(r.get('size',-1))>=0 for r in receipt['files'])
    except (OSError,ValueError,TypeError): return False
stage=Path.home()/'LaptopBackups'/'2026-10-07'
stage.mkdir(parents=True,exist_ok=True)
lock=(stage/'scheduled.lock').open('a+b')
try: msvcrt.locking(lock.fileno(),msvcrt.LK_NBLCK,1)
except OSError: raise SystemExit('Another scheduled run is active')
log=stage/('run-'+time.strftime('%Y%m%d-%H%M%S')+'.log')
with log.open('x',encoding='utf-8') as out:
    failures=[]
    for scope in ['core','personal']:
        capture=subprocess.run([python_binary,str(here/'new-machine-backup.py'),'--stage',str(stage),'--scope',scope],stdout=out,stderr=out,creationflags=hidden)
        if capture.returncode: failures.append('Capture failed: '+scope)
    for generation in sorted(stage.iterdir()):
        if not generation.is_dir() or not (generation/'manifest.json').exists(): continue
        manifest=json.loads((generation/'manifest.json').read_text())
        if not manifest['complete']: continue
        dependencies={r['generation'] for r in manifest['files'].values()}|{generation.name}
        if all(verified_receipt(stage/dep) for dep in dependencies): continue
        cloud=subprocess.run([python_binary,str(here/'new-machine-cloud.py'),'--generation',str(generation)],stdout=out,stderr=out,creationflags=hidden)
        if cloud.returncode: failures.append('Cloud upload failed: '+generation.name)
        elif not all(verified_receipt(stage/dep) for dep in dependencies): failures.append('Cloud receipt chain failed: '+generation.name)
    if failures:
        out.write('\n'.join(failures)+'\n')
        raise SystemExit('Backup incomplete; see '+str(log))
    subprocess.run([python_binary,str(here/'new-machine-publish-index.py')],stdout=out,stderr=out,check=True,creationflags=hidden)
    (stage/'LATEST-CLOUD-SUCCESS.txt').write_text(time.strftime('%Y-%m-%d %H:%M:%S')+'\n'+str(log),encoding='utf-8')
print('All complete generations verified on private Drive')
