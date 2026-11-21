"""Capture, upload, verify and evict local backup payloads; preserve metadata."""
import json, msvcrt, subprocess, sys, time, os
from pathlib import Path
import argparse
from new_machine_offload import offload_generation
here=Path(__file__).resolve().parent
runtime=here/'new-machine-runtime.json'
runtime_config=json.loads(runtime.read_text(encoding='utf-8-sig')) if runtime.exists() else {}
if runtime_config: os.environ['GWS_EXECUTABLE']=runtime_config['gws']
python_binary=runtime_config.get('python',sys.executable)
hidden=subprocess.CREATE_NO_WINDOW if os.name=='nt' else 0
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--maintenance-only',action='store_true',help='Upload/offload existing generations without capturing new files')
parser.add_argument('--offload-existing-only',action='store_true',help='Only verify and evict already-uploaded local payloads')
parser.add_argument('--keep-local',action='store_true',help='Do not evict local payloads on this run')
parser.add_argument('--resume-core',help='Reuse a validated partial core archive; capture rechecks its ZIP CRC before reuse')
args=parser.parse_args()
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
    def event(message,**details):
        out.write(json.dumps({'utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),'event':message,**details})+'\n'); out.flush()
    def generations():
        import re
        return [d for d in sorted(stage.iterdir()) if re.fullmatch(r'\d{8}-\d{6}',d.name) and d.is_dir() and not d.is_symlink() and not d.is_junction() and (d/'manifest.json').exists()]
    def evict(generation):
        if args.keep_local or not verified_receipt(generation): return
        has_snapshots=any(p.is_file() for p in (generation/'sqlite-snapshots').rglob('*'))
        if not (generation/'payload.zip').exists() and not any((generation/'cloud-parts').glob('payload.zip.part*')) and not has_snapshots: return
        event('verify-before-local-offload',generation=generation.name)
        result=offload_generation(stage,generation,apply=True,lock_held=True)
        event('local-offload-complete',**result)
    def upload(generation):
        manifest=json.loads((generation/'manifest.json').read_text())
        # The uploader revalidates existing receipts against live Drive metadata.
        command=[python_binary,str(here/'new-machine-cloud.py'),'--generation',str(generation)]
        if not manifest['complete']: command.append('--preserve-incomplete')
        event('upload-existing-capture',generation=generation.name,capture_complete=manifest['complete'])
        result=subprocess.run(command,stdout=out,stderr=out,creationflags=hidden)
        if result.returncode: raise RuntimeError('Cloud upload/verification failed: '+generation.name)
        if not verified_receipt(generation): raise RuntimeError('Cloud receipt missing: '+generation.name)
        evict(generation)
    # Reclaim only independently proven cloud copies before requiring capture headroom.
    for generation in generations():
        try: evict(generation)
        except Exception as error:
            failures.append('Local offload refused: '+generation.name+' ('+type(error).__name__+')')
            event('local-offload-refused',generation=generation.name,error_type=type(error).__name__)
    if not args.offload_existing_only:
        # Finish pending complete captures first; failed captures remain explicit history.
        for generation in generations():
            if not json.loads((generation/'manifest.json').read_text()).get('complete'): continue
            if not (generation/'payload.zip').exists() and verified_receipt(generation): continue
            try: upload(generation)
            except Exception as error:
                failures.append(str(error)); event('upload-refused',generation=generation.name,error_type=type(error).__name__)
        if not args.maintenance_only:
            for scope in ['core','personal']:
                before={d.name for d in generations()}
                event('capture-start',scope=scope)
                capture_command=[python_binary,str(here/'new-machine-backup.py'),'--stage',str(stage),'--scope',scope]
                if scope=='core' and args.resume_core: capture_command.extend(['--resume-base',args.resume_core])
                capture=subprocess.run(capture_command,stdout=out,stderr=out,creationflags=hidden)
                if capture.returncode: failures.append('Capture failed: '+scope)
                for generation in generations():
                    if generation.name in before: continue
                    try: upload(generation)
                    except Exception as error:
                        failures.append(str(error)); event('upload-refused',generation=generation.name,error_type=type(error).__name__)
        # Publish current complete restore points before potentially long historical uploads.
        event('publish-current-restore-index')
        index_result=subprocess.run([python_binary,str(here/'new-machine-publish-index.py')],stdout=out,stderr=out,creationflags=hidden)
        if index_result.returncode: failures.append('Restore index publication failed')
        # Preserve failed captures as incomplete archives, including historical revisions.
        for generation in generations():
            if json.loads((generation/'manifest.json').read_text()).get('complete'): continue
            if not (generation/'payload.zip').exists(): continue
            try: upload(generation)
            except Exception as error:
                failures.append(str(error)); event('history-preservation-refused',generation=generation.name,error_type=type(error).__name__)
        # Preserve interrupted payload bytes even when no capture manifest was finalized.
        import re
        for generation in sorted(stage.iterdir()):
            if not re.fullmatch(r'\d{8}-\d{6}',generation.name) or not generation.is_dir() or generation.is_symlink() or generation.is_junction(): continue
            if (generation/'manifest.json').exists() or not (generation/'payload.zip').is_file(): continue
            event('preserve-unindexed-payload',generation=generation.name)
            command=[python_binary,str(here/'new-machine-cloud.py'),'--generation',str(generation),'--preserve-unindexed']
            result=subprocess.run(command,stdout=out,stderr=out,creationflags=hidden)
            if result.returncode:
                failures.append('Unindexed preservation failed: '+generation.name); continue
            try: evict(generation)
            except Exception as error:
                failures.append('Unindexed local offload refused: '+generation.name)
                event('local-offload-refused',generation=generation.name,error_type=type(error).__name__)
    if failures:
        out.write('\n'.join(failures)+'\n')
        raise SystemExit('Backup incomplete; see '+str(log))
    if args.offload_existing_only or args.maintenance_only:
        event('existing-cloud-offload-finished')
        print('Existing backup maintenance finished; no new source capture claimed; see '+str(log))
        raise SystemExit(0)
    (stage/'LATEST-CLOUD-SUCCESS.txt').write_text(time.strftime('%Y-%m-%d %H:%M:%S')+'\n'+str(log),encoding='utf-8')
print('Scheduled backup capture, cloud verification and local offload finished')
