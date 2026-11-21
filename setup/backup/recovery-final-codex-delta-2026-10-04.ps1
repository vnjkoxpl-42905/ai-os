param([switch]$Resume)
$ErrorActionPreference = 'Stop'
$taskRoot = 'C:\Users\Joshu\laptop-recovery-2026-10-04'
$taskDelta = Join-Path $taskRoot 'staging\codex-final-delta'
if ((Test-Path -LiteralPath $taskDelta) -and -not $Resume) { throw 'Final delta already exists; choose a new dated folder, or explicitly resume this unfinished staging.' }
if (Test-Path -LiteralPath (Join-Path $taskRoot 'archives\codex-final-delta.7z.001')) { throw 'A finished delta archive exists; never replace it.' }
New-Item -ItemType Directory -Force -Path $taskDelta | Out-Null
$taskCutoff = Get-Date -Format o
@'
import os,sys,shutil,datetime,json
source,target=sys.argv[1:]
if os.name=='nt':
    source='\\\\?\\'+os.path.abspath(source)
    target='\\\\?\\'+os.path.abspath(target)
cutoff=datetime.datetime(2026,10,4,14,48,tzinfo=datetime.timezone(datetime.timedelta(hours=-4))).timestamp()
copied=[]
errors=[]
for base,dirs,files in os.walk(source,followlinks=False):
    dirs[:]=[d for d in dirs if not os.path.islink(os.path.join(base,d)) and not os.path.isjunction(os.path.join(base,d)) and d not in ('node_modules','.venv','venv','__pycache__')]
    for name in files:
        src=os.path.join(base,name)
        if name.endswith(('.sqlite','.sqlite-wal','.sqlite-shm','.sqlite-journal','.sqlite3','.sqlite3-wal','.sqlite3-shm','.sqlite3-journal','.db','.db-wal','.db-shm','.db-journal')): continue
        if name in ('.sqlite-maintenance.lock','instance.lock','session.lock') or (name.endswith('.lock') and '.git' in os.path.relpath(base,source).split(os.sep)): continue
        try:
            if os.path.getmtime(src)<cutoff or os.path.islink(src): continue
            rel=os.path.relpath(src,source); dst=os.path.join(target,rel)
            os.makedirs(os.path.dirname(dst),exist_ok=True)
            shutil.copy2(src,dst); copied.append(rel)
        except Exception as e: errors.append({'file':src,'error':str(e)})
with open(os.path.join(os.path.dirname(os.path.dirname(target)),'changed-files.json'),'w',encoding='utf-8') as f: json.dump({'baseline':'2026-10-04T14:48:00-04:00','copied':copied,'errors':errors},f,indent=2)
if errors: print(json.dumps(errors)); sys.exit(1)
'@ | Set-Content -LiteralPath (Join-Path $taskRoot 'codex-delta-copy.py') -Encoding UTF8
& python (Join-Path $taskRoot 'codex-delta-copy.py') (Join-Path $env:USERPROFILE '.codex') (Join-Path $taskDelta 'runtime\.codex')
if ($LASTEXITCODE -ne 0) { throw 'Delta file copy errors; see changed-files.json' }
& python (Join-Path $taskRoot 'sqlite-snapshot.py') (Join-Path $env:USERPROFILE '.codex') (Join-Path $taskDelta 'runtime\.codex') (Join-Path $taskDelta 'forensic-sqlite')
if ($LASTEXITCODE -ne 0) { throw 'Delta SQLite snapshot errors' }
@'
import os,sys,shutil,datetime,json,time
source,target,report=sys.argv[1:]
if os.name=='nt':
    source='\\\\?\\'+os.path.abspath(source)
    target='\\\\?\\'+os.path.abspath(target)
    report='\\\\?\\'+os.path.abspath(report)
cutoff=datetime.datetime(2026,10,4,14,48,tzinfo=datetime.timezone(datetime.timedelta(hours=-4))).timestamp()
started=time.monotonic()
excluded={'node_modules','.venv','venv','.vite','.turbo','.next','__pycache__','dist','coverage','.cache'}
files=[]; errors=[]; size=0
for base,dirs,names in os.walk(source,followlinks=False):
    dirs[:]=[d for d in dirs if d not in excluded and not os.path.islink(os.path.join(base,d)) and not os.path.isjunction(os.path.join(base,d))]
    if time.monotonic()-started>300:
        with open(report,'w',encoding='utf-8') as f: json.dump({'blocked':'scan exceeded five minutes','candidate_bytes_so_far':size,'files_so_far':len(files)},f,indent=2)
        sys.exit(2)
    for name in names:
        src=os.path.join(base,name); rel=os.path.relpath(src,source)
        if os.path.islink(src) or (name.endswith('.lock') and '.git' in rel.split(os.sep)): continue
        try:
            stat=os.stat(src)
            if stat.st_mtime<cutoff: continue
            files.append((src,rel,stat.st_size)); size+=stat.st_size
        except Exception as e: errors.append({'path':rel,'scan_error':str(e)})
preflight={'candidate_bytes':size,'candidate_files':len(files),'baseline':'2026-10-04T14:48:00-04:00','excluded_directories':sorted(excluded),'errors':errors}
with open(report,'w',encoding='utf-8') as f: json.dump(preflight,f,indent=2)
print(json.dumps({'candidate_bytes':size,'candidate_files':len(files),'scan_seconds':time.monotonic()-started}),flush=True)
if size>2*1024**3: sys.exit(2)
copied=[]
for src,rel,expected_size in files:
    if time.monotonic()-started>300:
        errors.append({'copy_error':'copy exceeded five minutes; remaining files not copied'})
        break
    dst=os.path.join(target,rel)
    try:
        os.makedirs(os.path.dirname(dst),exist_ok=True); shutil.copy2(src,dst); copied.append(rel)
    except Exception as e: errors.append({'path':rel,'copy_error':str(e)})
preflight.update({'copied':copied,'errors':errors,'elapsed_seconds':time.monotonic()-started})
with open(report,'w',encoding='utf-8') as f: json.dump(preflight,f,indent=2)
sys.exit(1 if errors else 0)
'@ | Set-Content -LiteralPath (Join-Path $taskRoot 'dev-delta-copy.py') -Encoding UTF8
& python (Join-Path $taskRoot 'dev-delta-copy.py') (Join-Path $env:USERPROFILE 'dev\ai-os') (Join-Path $taskDelta 'second-brain\dev\ai-os') (Join-Path $taskDelta 'dev-changed-files.json')
if ($LASTEXITCODE -eq 2) { throw 'Dev delta preflight exceeded two GiB or five minutes; inspect dev-changed-files.json before proceeding.' }
if ($LASTEXITCODE -ne 0) { throw 'Dev delta copy errors; inspect dev-changed-files.json' }
@"
Captured final Codex delta started $taskCutoff and finished $(Get-Date -Format o).
Apply codex-final-delta/runtime/.codex to the restored profile's .codex AFTER runtime-final, with Codex closed and after preserving existing restored files. This supersedes only the selected runtime files and databases. All databases were captured with SQLite backup and checked. Do not restore forensic-sqlite over the checked snapshots. changed-files.json lists files modified since2026-10-04T14:48:00-04:00, the start of the original copy window, to include changes that happened while the baseline was being captured. The ongoing chat's messages after this capture are necessarily outside the cutoff. The baseline full runtime-final remains required.
Apply second-brain/dev/ai-os from this delta to the restored dev/ai-os directory after the second-brain baseline. dev-changed-files.json records ai-os files modified since2026-10-04T14:48:00-04:00, including .env where changed, Git metadata and brain records. Other application repositories are outside the user's final required scope. Dependency environments, build caches, dist and coverage outputs are omitted from the delta; the earlier full baselines remain required. Files changed after the final capture are outside this backup.
"@ | Set-Content -LiteralPath (Join-Path $taskDelta 'DELTA-RESTORE.md') -Encoding UTF8
foreach ($name in 'RESTORE - START HERE.md','KNOWN-ISSUES-AND-RESOLUTIONS.txt','CODEX-DATABASE-VERIFICATION.json') {
    $src = Join-Path $taskRoot $name
    if (Test-Path -LiteralPath $src) { Copy-Item -LiteralPath $src -Destination $taskDelta }
}
$updatedScripts = Join-Path $taskDelta 'second-brain\dev\ai-os\setup\backup'
New-Item -ItemType Directory -Force -Path $updatedScripts | Out-Null
Get-ChildItem -LiteralPath (Join-Path $env:USERPROFILE 'dev\ai-os\setup\backup') -File | Where-Object { $_.Extension -in '.ps1','.sh','.md','.json' } | ForEach-Object { Copy-Item -LiteralPath $_.FullName -Destination $updatedScripts }
Copy-Item -LiteralPath (Join-Path $taskRoot 'sqlite-snapshot.py') -Destination $taskDelta
$latestWikiLog = Join-Path $taskDelta 'second-brain\dev\ai-os\wiki'
New-Item -ItemType Directory -Force -Path $latestWikiLog | Out-Null
Copy-Item -LiteralPath (Join-Path $env:USERPROFILE 'dev\ai-os\wiki\log.md') -Destination $latestWikiLog
$output = Join-Path $taskRoot 'archives\codex-final-delta.7z'
& 'C:\Program Files\7-Zip\7z.exe' a -t7z -mx=1 -mmt=4 -v256m -snl $output $taskDelta | Out-File (Join-Path $taskRoot 'logs\codex-final-delta-archive.log')
if ($LASTEXITCODE -ne 0) { throw "Delta archive exit $LASTEXITCODE" }
& 'C:\Program Files\7-Zip\7z.exe' t ($output+'.001') | Out-File (Join-Path $taskRoot 'logs\codex-final-delta-test.log')
if ($LASTEXITCODE -ne 0) { throw "Delta test exit $LASTEXITCODE" }
Get-ChildItem -LiteralPath (Join-Path $taskRoot 'archives') -Filter 'codex-final-delta.7z.*' | ForEach-Object {
    $hash=(Get-FileHash -LiteralPath $_.FullName -Algorithm SHA256).Hash
    "$hash  $($_.Name)" | Add-Content (Join-Path $taskRoot 'SHA256SUMS.txt')
}
'READY codex-final-delta' | Add-Content (Join-Path $taskRoot 'PROGRESS.txt')
