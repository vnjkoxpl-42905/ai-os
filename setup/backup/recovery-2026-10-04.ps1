param([string]$Root = 'C:\Users\Joshu\laptop-recovery-2026-10-04')
$ErrorActionPreference = 'Stop'
$SevenZip = 'C:\Program Files\7-Zip\7z.exe'
if (-not (Test-Path -LiteralPath $SevenZip)) { throw '7-Zip is required.' }
if (Test-Path -LiteralPath $Root) { throw "Recovery root already exists: $Root. Use a new root; this script never replaces an existing backup." }
New-Item -ItemType Directory -Path $Root | Out-Null
$stage = Join-Path $Root 'staging'
$archives = Join-Path $Root 'archives'
$logs = Join-Path $Root 'logs'
New-Item -ItemType Directory -Path $stage,$archives,$logs | Out-Null
$userRoot = $env:USERPROFILE
$issues = [Collections.Generic.List[string]]::new()
$excludeDirs = @('node_modules','.venv','venv','.vite','.turbo','.next','__pycache__')
$dbExclude = @('*.sqlite','*.sqlite-wal','*.sqlite-shm','*.sqlite3','*.sqlite3-wal','*.sqlite3-shm','*.db','*.db-wal','*.db-shm')
function Save-Tree([string]$Source,[string]$Relative,[switch]$Database) {
    if (-not (Test-Path -LiteralPath $Source)) { "MISSING optional source: $Source" | Add-Content (Join-Path $logs 'sources.log'); return }
    $dest = Join-Path $stage $Relative
    New-Item -ItemType Directory -Force -Path $dest | Out-Null
    Write-Host "Copying $Source"
    $safeName = $Relative.Replace('\','_').Replace('/','_')
    $args = @($Source,$dest,'/E','/XJ','/SL','/R:0','/W:0','/MT:12','/COPY:DAT','/DCOPY:DAT','/NP','/NFL','/NDL',('/LOG:' + (Join-Path $logs ($safeName + '.log'))),'/XD') + $excludeDirs
    if ($Database) { $args += '/XF'; $args += $dbExclude }
    & robocopy @args | Out-Null
    $rc = $LASTEXITCODE
    "$Source -> $Relative rc=$rc" | Add-Content (Join-Path $logs 'sources.log')
    if ($rc -ge 8) { $issues.Add("Copy failed for $Source (robocopy $rc); see $safeName.log") }
    if ($Database) {
        & python (Join-Path $Root 'sqlite-snapshot.py') $Source $dest (Join-Path $stage ('sqlite-live-raw\' + $Relative))
        if ($LASTEXITCODE -ne 0) { $issues.Add("SQLite snapshot errors for $Source") }
    }
}
function Save-File([string]$Source,[string]$Relative) {
    if (Test-Path -LiteralPath $Source -PathType Leaf) {
        $dest = Join-Path $stage $Relative
        New-Item -ItemType Directory -Force -Path (Split-Path $dest -Parent) | Out-Null
        Copy-Item -LiteralPath $Source -Destination $dest
    }
}
function Pack-Category([string]$Name) {
    Write-Host "Archiving $Name into 256 MB volumes"
    $output = Join-Path $archives ($Name + '.7z')
    & $SevenZip a -t7z -mx=1 -mmt=4 -v256m -snl $output (Join-Path $stage $Name) | Out-File (Join-Path $logs ($Name + '-archive.log'))
    if ($LASTEXITCODE -eq 1) { $issues.Add("Archive warning: $Name; inspect $Name-archive.log for omitted files") }
    if ($LASTEXITCODE -gt 1) { $issues.Add("Archive failed: $Name"); throw "Archive failed: $Name" }
    & $SevenZip t ($output + '.001') | Out-File (Join-Path $logs ($Name + '-test.log'))
    if ($LASTEXITCODE -ne 0) { $issues.Add("Archive test failed: $Name"); throw "Archive test failed: $Name" }
    Get-ChildItem -LiteralPath $archives -Filter ($Name + '.7z.*') | ForEach-Object {
        $hash = (Get-FileHash -LiteralPath $_.FullName -Algorithm SHA256).Hash
        "$hash  $($_.Name)" | Add-Content (Join-Path $Root 'SHA256SUMS.txt')
    }
    "READY $Name $(Get-Date -Format o)" | Add-Content (Join-Path $Root 'PROGRESS.txt')
    Write-Host "READY $Name"
}
@'
import os, sys, sqlite3, shutil, json
source, destination, raw = sys.argv[1:]
errors = []
count = 0
for base, dirs, files in os.walk(source, followlinks=False):
    dirs[:] = [d for d in dirs if not os.path.islink(os.path.join(base, d)) and not os.path.isjunction(os.path.join(base, d)) and d not in ('node_modules', '.venv', 'venv', '__pycache__')]
    for name in files:
        if not name.endswith(('.sqlite', '.sqlite3', '.db')):
            continue
        src = os.path.join(base, name)
        rel = os.path.relpath(src, source)
        out = os.path.join(destination, rel)
        rawout = os.path.join(raw, rel)
        os.makedirs(os.path.dirname(rawout), exist_ok=True)
        for suffix in ('', '-wal', '-shm', '-journal'):
            if os.path.isfile(src + suffix):
                try: shutil.copy2(src + suffix, rawout + suffix)
                except Exception as e: errors.append({'path': src + suffix, 'raw_copy_error': str(e)})
        try:
            with open(src, 'rb') as f: header = f.read(16)
            os.makedirs(os.path.dirname(out), exist_ok=True)
            if header != b'SQLite format 3\x00':
                shutil.copy2(src, out)
                continue
            read = sqlite3.connect('file:' + src.replace('\\', '/') + '?mode=ro', uri=True, timeout=30)
            write = sqlite3.connect(out)
            read.execute('BEGIN')
            read.execute('SELECT count(*) FROM sqlite_master').fetchone()
            deadline = __import__('time').monotonic() + 120
            def progress(status, remaining, total):
                if __import__('time').monotonic() > deadline: raise TimeoutError('SQLite backup exceeded 120 seconds')
            read.backup(write, pages=1024, sleep=0.05, progress=progress)
            result = write.execute('PRAGMA quick_check').fetchone()[0]
            write.close(); read.rollback(); read.close()
            if result != 'ok': raise RuntimeError(result)
            count += 1
        except Exception as e:
            errors.append({'path': src, 'snapshot_error': str(e)})
report = {'source': source, 'snapshotted_databases': count, 'errors': errors}
os.makedirs(raw, exist_ok=True)
with open(os.path.join(raw, 'sqlite-report.json'), 'w', encoding='utf-8') as f: json.dump(report, f, indent=2)
print(json.dumps(report))
sys.exit(1 if errors else 0)
'@ | Set-Content -LiteralPath (Join-Path $Root 'sqlite-snapshot.py') -Encoding UTF8
@'
# Restore the 2026-10-04 laptop recovery

These private archives include passwords, local credentials, student records, and personal files. Keep them in your private Google Drive. The accompanying SHA256SUMS.txt and archive test logs establish the saved archive contents. A cloud upload still needs a separate verification.

1. On the new Windows computer install 7-Zip, Git, Node.js LTS, Python, Codex desktop, Claude Code, Obsidian, Google Drive for Desktop, and any other apps you use. Sign in to Google Drive using contact@aspiringattorneys.com.
2. Download ALL numbered volumes for each category into the same folder. Open the .7z.001 file with 7-Zip and extract into a NEW empty recovery folder. Keep every volume; later volumes are required.
3. runtime contains user-profile directories such as .codex, .claude, .agents, .config and dotfiles. second-brain contains dev\ai-os. development contains other dev folders, including ai-os-projects. app-data contains AppData directories. Combine these under the new user profile only after backing up any existing target files. No automatic restore is run and nothing is deleted.
4. Prefer the same Windows username (Joshu), keeping C:\Users\Joshu\dev\ai-os and C:\Users\Joshu\dev\ai-os-projects. If the username differs, restore into the new profile then repair old absolute paths in Codex/Claude settings and Git worktree metadata. Do not blindly replace text in databases. Run git worktree repair in each main repository with its restored worktree paths. Codex managed worktrees live inside .codex\worktrees, and must remain with their main repositories.
5. The regular runtime/app-data SQLite files were captured through SQLite's backup API and checked with PRAGMA quick_check. sqlite-live-raw is forensic evidence of the original live database plus WAL files, and must not be copied over the consistent snapshots. The raw files are separately retained; source applications were open during backup.
6. Reinstall dependencies in each project using its lockfile and package manager. node_modules, Python virtual environments, build caches, and __pycache__ were omitted. Project source, Git history, uncommitted work, raw sources, .env, and local AI configuration were included. Symbolic links/junctions are not traversed. Inspect logs and ISSUES.txt for any inaccessible or failed files.
7. Sign in again where requested. Windows keyring/DPAPI secrets, browser cookies, Store app settings, OAuth sessions, and credentials bound to this computer may not work on a new computer. Reinstall apps instead of restoring their binaries. For Codex Store package user data, consult the saved AppData category; copying it requires the app closed and may require matching the newly installed package directory.
8. Verify student folders, raw sources, .env, recent Codex and Claude chats, automemory, project branches, uncommitted work and worktrees before returning or wiping the old laptop. The current Codex chat may still be writing during capture and may require a final capture after work ends.

This is a file/data recovery backup, not a full bootable Windows image. Programs, licenses, OS settings and machine-bound secrets require installation or sign-in. See inventory and exclusions for personal-file coverage.
'@ | Set-Content -LiteralPath (Join-Path $Root 'RESTORE - START HERE.md') -Encoding UTF8
Save-Tree (Join-Path $userRoot '.codex') 'runtime\.codex' -Database
Save-Tree (Join-Path $userRoot '.claude') 'runtime\.claude' -Database
Save-Tree (Join-Path $userRoot '.agents') 'runtime\.agents'
Save-Tree (Join-Path $userRoot '.config') 'runtime\.config' -Database
Save-Tree (Join-Path $userRoot '.ssh') 'runtime\.ssh'
Save-Tree (Join-Path $userRoot '.aws') 'runtime\.aws'
Save-Tree (Join-Path $userRoot '.azure') 'runtime\.azure'
foreach ($name in '.gemini','.notebooklm','.herdr','.kling','.local','Tools') { Save-Tree (Join-Path $userRoot $name) ('runtime\' + $name) -Database }
foreach ($name in '.claude.json','.gitconfig','.npmrc','.bashrc','.bash_profile','.profile','.netrc') { Save-File (Join-Path $userRoot $name) ('runtime\' + $name) }
Pack-Category 'runtime'
Save-Tree (Join-Path $userRoot 'dev\ai-os') 'second-brain\dev\ai-os'
Pack-Category 'second-brain'
Get-ChildItem -LiteralPath (Join-Path $userRoot 'dev') -Directory -Force | Where-Object { $_.Name -ne 'ai-os' -and -not ($_.Attributes -band [IO.FileAttributes]::ReparsePoint) } | ForEach-Object { Save-Tree $_.FullName ('development\dev\' + $_.Name) }
Get-ChildItem -LiteralPath (Join-Path $userRoot 'dev') -File -Force | ForEach-Object { Save-File $_.FullName ('development\dev\' + $_.Name) }
Pack-Category 'development'
foreach ($name in 'Codex','Claude','Claude Code','Superwhisper','obsidian','gws','gh') {
    Save-Tree (Join-Path $env:APPDATA $name) ('app-data\AppData\Roaming\' + $name) -Database
    Save-Tree (Join-Path $env:LOCALAPPDATA $name) ('app-data\AppData\Local\' + $name) -Database
}
Get-ChildItem -LiteralPath (Join-Path $env:LOCALAPPDATA 'Packages') -Directory -Filter 'OpenAI.Codex*' | ForEach-Object {
    $package = $_
    foreach ($name in 'LocalState','LocalCache','RoamingState','Settings','AppData') { Save-Tree (Join-Path $package.FullName $name) ('app-data\AppData\Local\Packages\' + $package.Name + '\' + $name) -Database }
}
Pack-Category 'app-data'
if (Test-Path -LiteralPath (Join-Path $stage 'sqlite-live-raw')) { Pack-Category 'sqlite-live-raw' }
foreach ($name in 'Desktop','Documents','Downloads','OneDrive','Pictures','Videos','Music') { Save-Tree (Join-Path $userRoot $name) ('personal-files\' + $name) }
Pack-Category 'personal-files'
if ($issues.Count) { $issues | Set-Content (Join-Path $Root 'ISSUES.txt') } else { 'No copy/archive/database errors recorded for included sources.' | Set-Content (Join-Path $Root 'ISSUES.txt') }
'Excluded: node_modules, .venv, venv, .vite, .turbo, .next, __pycache__. Junction targets not traversed. Personal folders Desktop, Documents, Downloads, OneDrive, Pictures, Videos, Music copied where present; cloud placeholders require provider hydration and failures appear in logs. Installed programs and Windows are not included.' | Set-Content (Join-Path $Root 'EXCLUSIONS.txt')
"DONE $(Get-Date -Format o)" | Add-Content (Join-Path $Root 'PROGRESS.txt')
