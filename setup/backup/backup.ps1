# backup.ps1 - mirror the whole Claude Code setup into Google Drive.
# Runs every 10 minutes from a Scheduled Task ("Claude Code Backup").
# Source of truth for this script: C:\Users\Joshu\dev\ai-os\setup\backup\backup.ps1
# Safe to run by hand:  powershell -ExecutionPolicy Bypass -File backup.ps1

$ErrorActionPreference = 'Continue'
$Home_  = $env:USERPROFILE
$Vault  = Join-Path $Home_ 'dev\ai-os'
$Drive  = 'G:\My Drive\CLAUDE-CODE-BACKUP - START HERE'
$Cur    = Join-Path $Drive 'current'
$Snaps  = Join-Path $Drive 'snapshots'
$LogDir = Join-Path $Drive 'logs'
$Stamp  = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'

# One run at a time: skip if another backup is still going.
$mutex = New-Object System.Threading.Mutex($false, 'Global\ClaudeCodeBackup')
if (-not $mutex.WaitOne(0)) { Write-Host 'Another backup is running - skipping'; exit 0 }

if (-not (Test-Path 'G:\My Drive')) { Write-Host "Google Drive not mounted at G:\My Drive - skipping"; exit 1 }
foreach ($d in $Cur, $Snaps, $LogDir) { New-Item -ItemType Directory -Force -Path $d | Out-Null }
$Log = Join-Path $LogDir ("backup-" + (Get-Date -Format 'yyyy-MM-dd') + ".log")
"=== $Stamp backup start ===" | Out-File -Append $Log

# robocopy /MIR = make destination identical to source. /XJ skips junctions, /FFT tolerates Drive timestamps.
$common = @('/MIR','/XJ','/FFT','/R:1','/W:1','/NFL','/NDL','/NP','/NJH','/MT:8')
function Mirror($src, $dst, $xd) {
    if (-not (Test-Path $src)) { "skip (missing): $src" | Out-File -Append $Log; return }
    $args = @($src, $dst) + $common
    if ($xd) { $args += '/XD'; $args += $xd }
    $out = & robocopy @args 2>&1
    $rc = $LASTEXITCODE   # robocopy: 0-7 = success codes, 8+ = failures
    "$src -> $dst  rc=$rc" | Out-File -Append $Log
    if ($rc -ge 8) { $out | Select-Object -Last 15 | Out-File -Append $Log }
}

# 1. Claude Code: transcripts, skills, plugins, settings, memory, everything.
Mirror (Join-Path $Home_ '.claude') (Join-Path $Cur 'claude') @()
# 2. Claude Code global config (MCP servers, OAuth). Included on purpose - user decision 2026-09-11.
Copy-Item (Join-Path $Home_ '.claude.json') (Join-Path $Cur 'claude.json') -Force -ErrorAction SilentlyContinue
# 3. Codex CLI config + auth.
Mirror (Join-Path $Home_ '.codex') (Join-Path $Cur 'codex') @('cache')
# 4. Superwhisper app data (modes, vocabulary, settings).
Mirror (Join-Path $env:LOCALAPPDATA 'Superwhisper') (Join-Path $Cur 'superwhisper') @()
# 5. The vault, including code repos, minus dependency caches that reinstall.
Mirror $Vault (Join-Path $Cur 'ai-os') @('node_modules','.vite','.turbo','.next','dist','__pycache__','.cache')
# 6. Other dotfiles that matter on a new machine.
$dot = Join-Path $Cur 'dotfiles'; New-Item -ItemType Directory -Force -Path $dot | Out-Null
foreach ($f in '.gitconfig','.npmrc','.bashrc','.bash_profile') {
    $p = Join-Path $Home_ $f; if (Test-Path $p) { Copy-Item $p $dot -Force }
}
Mirror (Join-Path $env:APPDATA 'gws') (Join-Path $dot 'gws') @()
Mirror (Join-Path $env:APPDATA 'gh')  (Join-Path $dot 'gh')  @()
Mirror (Join-Path $Home_ '.config')   (Join-Path $dot 'config') @()

# 7. Machine info so restore can rewrite paths.
@{ machine=$env:COMPUTERNAME; user=$env:USERNAME; home=$Home_; vault=$Vault; os='windows'; backedUpAt=$Stamp;
   claudeVersion=(try { (& claude --version 2>$null) } catch { '' }) } |
  ConvertTo-Json | Out-File (Join-Path $Cur 'machine-info.json') -Encoding utf8
"Last successful backup: $Stamp  (from $env:COMPUTERNAME)`r`nRestore instructions: see README - START HERE.md" |
  Out-File (Join-Path $Drive 'LAST-BACKUP.txt') -Encoding utf8

# 8. Git: auto-commit + push the vault (private GitHub repo). Never blocks the Drive copy.
if (Test-Path (Join-Path $Vault '.git')) {
    Push-Location $Vault
    & git add -A 2>&1 | Out-Null
    $dirty = & git status --porcelain
    if ($dirty) {
        & git commit -q -m "auto-backup $Stamp" 2>&1 | Out-File -Append $Log
        & git push -q 2>&1 | Out-File -Append $Log
        "git: committed + pushed" | Out-File -Append $Log
    }
    Pop-Location
}

# 9. Daily snapshot zip (vault minus raw/projects + claude config), keep 30 days.
$today = Get-Date -Format 'yyyy-MM-dd'
$zip = Join-Path $Snaps "snapshot-$today.zip"
if (-not (Test-Path $zip)) {
    $tmp = Join-Path $env:TEMP "cc-snap-$today"
    Remove-Item $tmp -Recurse -Force -ErrorAction SilentlyContinue
    New-Item -ItemType Directory -Force -Path $tmp | Out-Null
    & robocopy $Vault (Join-Path $tmp 'ai-os') /MIR /XJ /R:0 /W:0 /NFL /NDL /NP /NJH /XD raw projects node_modules tmp .obsidian | Out-Null
    & robocopy (Join-Path $Home_ '.claude') (Join-Path $tmp 'claude') /MIR /XJ /R:0 /W:0 /NFL /NDL /NP /NJH /XD plugins shell-snapshots | Out-Null
    Copy-Item (Join-Path $Home_ '.claude.json') $tmp -Force -ErrorAction SilentlyContinue
    Compress-Archive -Path (Join-Path $tmp '*') -DestinationPath $zip -Force
    Remove-Item $tmp -Recurse -Force -ErrorAction SilentlyContinue
    Get-ChildItem $Snaps -Filter 'snapshot-*.zip' | Sort-Object Name -Descending | Select-Object -Skip 30 | Remove-Item -Force
    "snapshot: $zip" | Out-File -Append $Log
}
"=== backup done ===" | Out-File -Append $Log
