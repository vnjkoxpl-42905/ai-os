# restore.ps1 - put the whole Claude Code setup onto a NEW Windows laptop.
# Prereqs on the new laptop: Google Drive for Desktop signed in (G:\My Drive), Git, Node, then `npm i -g @anthropic-ai/claude-code`.
# Run from anywhere:  powershell -ExecutionPolicy Bypass -File "G:\My Drive\CLAUDE-CODE-BACKUP - START HERE\restore.ps1"
# Optional: -Target <dir> to restore into a test folder instead of the real home (used for proving the backup works).
param([string]$Target = $env:USERPROFILE, [switch]$SkipInstall)
$ErrorActionPreference = 'Stop'
$Drive = 'G:\My Drive\CLAUDE-CODE-BACKUP - START HERE'
$Cur   = Join-Path $Drive 'current'
if (-not (Test-Path $Cur)) { throw "Backup not found at $Cur. Is Google Drive signed in and finished syncing?" }
$info = Get-Content (Join-Path $Cur 'machine-info.json') -Raw | ConvertFrom-Json
Write-Host "Restoring backup from $($info.machine) taken $($info.backedUpAt) into $Target"

function Put($src, $dst) {
    if (-not (Test-Path $src)) { Write-Host "  skip (not in backup): $src"; return }
    New-Item -ItemType Directory -Force -Path $dst | Out-Null
    & robocopy $src $dst /E /XJ /R:2 /W:2 /NFL /NDL /NP /NJH | Out-Null
    Write-Host "  restored $dst"
}
Put (Join-Path $Cur 'claude')       (Join-Path $Target '.claude')
Copy-Item (Join-Path $Cur 'claude.json') (Join-Path $Target '.claude.json') -Force
Put (Join-Path $Cur 'codex')        (Join-Path $Target '.codex')
Put (Join-Path $Cur 'ai-os')        (Join-Path $Target 'dev\ai-os')
Put (Join-Path $Cur 'superwhisper') (Join-Path $env:LOCALAPPDATA 'Superwhisper')
Put (Join-Path $Cur 'dotfiles\gws') (Join-Path $env:APPDATA 'gws')
Put (Join-Path $Cur 'dotfiles\gh')  (Join-Path $env:APPDATA 'gh')
Put (Join-Path $Cur 'dotfiles\config') (Join-Path $Target '.config')
foreach ($f in '.gitconfig','.npmrc','.bashrc','.bash_profile') {
    $p = Join-Path $Cur "dotfiles\$f"; if (Test-Path $p) { Copy-Item $p $Target -Force }
}

# Rewrite the transcript folder names so `claude --resume` finds old chats at the new path.
# Claude Code names each project folder by its path with \ : / turned into -  e.g. C--Users-Joshu-dev-ai-os
$oldPrefix = ($info.home -replace '[\:/]', '-')
$newPrefix = ($Target   -replace '[\:/]', '-')
if ($oldPrefix -ne $newPrefix) {
    Get-ChildItem (Join-Path $Target '.claude\projects') -Directory | Where-Object { $_.Name.StartsWith($oldPrefix) } | ForEach-Object {
        $new = $newPrefix + $_.Name.Substring($oldPrefix.Length)
        Rename-Item $_.FullName $new -Force; Write-Host "  renamed transcripts: $($_.Name) -> $new"
    }
    # Paths inside settings/config that pointed at the old home.
    foreach ($f in '.claude.json', '.claude\settings.json') {
        $p = Join-Path $Target $f
        if (Test-Path $p) { (Get-Content $p -Raw).Replace($info.home, $Target).Replace(($info.home -replace '\','\\'), ($Target -replace '\','\\')) | Set-Content $p -NoNewline }
    }
}

if (-not $SkipInstall) {
    $lsatu = Join-Path $Target 'dev\ai-os\projects\lsatu'
    if ((Test-Path $lsatu) -and (Get-Command npm -ErrorAction SilentlyContinue)) { Push-Location $lsatu; npm install; Pop-Location }
    # Re-register the 10-minute backup on this machine.
    & (Join-Path $Target 'dev\ai-os\setup\backup\install-task.ps1')
}
Write-Host "`nDone. Open Claude Code in $Target\dev\ai-os and run: claude --resume"
Write-Host "If gh / gws / claude ask you to sign in again, do so once; everything else is already in place."
