# Run in an external PowerShell terminal after closing Codex and Claude.
[CmdletBinding()]
param([Parameter(Mandatory)][string]$BackupFolder, [string]$StageFolder,
      [switch]$Apply, [string]$ProfileFolder = $env:USERPROFILE)
$ErrorActionPreference = 'Stop'
$BackupFolder = (Resolve-Path -LiteralPath $BackupFolder).Path
if (!$StageFolder) { $StageFolder = Join-Path $BackupFolder ('restored-' + (Get-Date -Format 'yyyyMMdd-HHmmss')) }
$StageFolder = [IO.Path]::GetFullPath($StageFolder)
if ((Test-Path -LiteralPath $StageFolder) -and @(Get-ChildItem -LiteralPath $StageFolder -Force).Count) { throw 'StageFolder must be new or empty.' }
$seven = (Get-Command 7z.exe -ErrorAction SilentlyContinue).Source
if (!$seven -and (Test-Path 'C:\Program Files\7-Zip\7z.exe')) { $seven = 'C:\Program Files\7-Zip\7z.exe' }
if (!$seven) { throw 'Install 7-Zip first, then run this helper again.' }
$manifest = Join-Path $BackupFolder 'CLOUD-VERIFIED-SHA256SUMS.txt'
if (!(Test-Path -LiteralPath $manifest)) { throw 'Missing cloud-verified SHA256 manifest.' }
$files = @{}
foreach ($line in Get-Content -LiteralPath $manifest) {
    if (!$line.Trim() -or $line.StartsWith('#')) { continue }
    if ($line -notmatch '^([a-fA-F0-9]{64})\s+\*?([^/\\]+)$') { throw 'Invalid manifest line.' }
    $name = $Matches[2].Trim(); $expected = $Matches[1]
    if ($name -eq '.' -or $name -eq '..' -or $name.Contains(':') -or $files.ContainsKey($name)) { throw 'Unsafe or duplicate manifest filename.' }
    $path = Join-Path $BackupFolder $name
    if (!(Test-Path -LiteralPath $path -PathType Leaf)) { throw "Missing verified file: $name" }
    if ((Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash -ne $expected) { throw "SHA256 mismatch: $name" }
    $files[$name] = $path
}
if (!$files.Count) { throw 'Manifest contains no files.' }
$categories = @('runtime-final','second-brain','development','app-data','sqlite-live-raw','personal-files','extra-settings','additional-profile','codex-final-delta')
$active = @($categories | Where-Object { $files.ContainsKey("$_.7z.001") -or $files.ContainsKey("$_.7z") })
if ('runtime-final' -notin $active -or 'second-brain' -notin $active) { throw 'Verified runtime-final and second-brain archives are required.' }
# Require every volume on disk to be verified before letting 7-Zip open the set.
foreach ($category in $active) {
    foreach ($volume in Get-ChildItem -LiteralPath $BackupFolder -Filter "$category.7z*" -File) {
        if ($volume.Name -match '\.7z(\.\d+)?$' -and !$files.ContainsKey($volume.Name)) { throw "Unverified archive volume: $($volume.Name)" }
    }
    $first = if ($files.ContainsKey("$category.7z.001")) { $files["$category.7z.001"] } else { $files["$category.7z"] }
    & $seven t $first -bsp0 | Out-Null
    if ($LASTEXITCODE -ne 0) { throw "Archive test failed: $category" }
}
New-Item -ItemType Directory -Path $StageFolder -Force | Out-Null
foreach ($category in $active) {
    $first = if ($files.ContainsKey("$category.7z.001")) { $files["$category.7z.001"] } else { $files["$category.7z"] }
    & $seven x $first ("-o" + (Join-Path $StageFolder $category)) -y -bsp0 | Out-Null
    if ($LASTEXITCODE -ne 0) { throw "Extraction failed: $category" }
}
Write-Host "Verified archives extracted to: $StageFolder"
if (!$Apply) { Write-Host 'Stage only. No profile files changed. Read the restore guide before using -Apply.'; return }
if (Get-Process -Name '*codex*','*claude*' -ErrorAction SilentlyContinue) { throw 'Close Codex and Claude, including terminal agents, then rerun from an external terminal with a NEW StageFolder.' }
$ProfileFolder = [IO.Path]::GetFullPath($ProfileFolder)
$preexisting = Join-Path $ProfileFolder ('preexisting-before-restore-' + (Get-Date -Format 'yyyyMMdd-HHmmss-fff'))
New-Item -ItemType Directory -Path $preexisting | Out-Null
function Copy-Safe([string]$Source, [string]$Target) {
    if (!(Test-Path -LiteralPath $Source)) { return }
    $item = Get-Item -LiteralPath $Source -Force
    if ($item.Attributes -band [IO.FileAttributes]::ReparsePoint) { return }
    if ((Test-Path -LiteralPath $Target) -and ((Get-Item -LiteralPath $Target -Force).Attributes -band [IO.FileAttributes]::ReparsePoint)) { throw "Target reparse point requires manual restore: $Target" }
    if ($item.PSIsContainer) {
        if ($item.Name -in @('node_modules','.venv','venv','__pycache__','.sandbox','.sandbox-bin','.sandbox-secrets','mcp-oauth-locks','project-metadata-locks','thread-writer-locks','rollout-migrations','.tmp','tmp')) { return }
        if ((Test-Path -LiteralPath $Target) -and !(Get-Item -LiteralPath $Target -Force).PSIsContainer) { throw "File blocks directory: $Target" }
        New-Item -ItemType Directory -Path $Target -Force | Out-Null
        foreach ($child in Get-ChildItem -LiteralPath $Source -Force) { Copy-Safe $child.FullName (Join-Path $Target $child.Name) }
        return
    }
    $runtimeSource = $Source -match '[\\/]runtime[\\/]'
    $gitSource = $Source -match '[\\/]\.git[\\/]'
    $dependencyLock = $item.Name -in @('yarn.lock','uv.lock','poetry.lock','Cargo.lock','Pipfile.lock','bun.lock')
    if (!$dependencyLock -and ($runtimeSource -or $gitSource) -and ($item.Name -like '*.lock' -or $item.Name -eq 'lockfile')) { return }
    if ($runtimeSource -and ($item.Name -like '*-wal' -or $item.Name -like '*-shm')) { return }
    if ((Test-Path -LiteralPath $Target) -and (Get-Item -LiteralPath $Target -Force).PSIsContainer) { throw "Directory blocks file: $Target" }
    New-Item -ItemType Directory -Path (Split-Path -Parent $Target) -Force | Out-Null
    $relative = $Target.Substring($ProfileFolder.TrimEnd('\').Length).TrimStart('\')
    if (Test-Path -LiteralPath $Target) {
        $old = Join-Path $preexisting $relative
        if (!(Test-Path -LiteralPath $old)) { New-Item -ItemType Directory -Path (Split-Path -Parent $old) -Force | Out-Null; Copy-Item -LiteralPath $Target -Destination $old -Force }
    }
    # Existing SQLite sidecars belong to the old database, so preserve them out of its way.
    if ($runtimeSource -and ($item.Name -like '*.sqlite' -or $item.Name -like '*.sqlite3' -or $item.Name -like '*.db')) {
        foreach ($suffix in @('-wal','-shm')) {
            $side = $Target + $suffix
            if (Test-Path -LiteralPath $side) { $saved = Join-Path $preexisting ($relative + $suffix); New-Item -ItemType Directory -Path (Split-Path -Parent $saved) -Force | Out-Null; if (Test-Path -LiteralPath $saved) { throw "Duplicate SQLite sidecar: $side" }; Move-Item -LiteralPath $side -Destination $saved }
        }
    }
    Copy-Item -LiteralPath $Source -Destination $Target -Force
}
function Get-CategoryRoot([string]$Category, [string]$Inner) {
    $outer = Join-Path $StageFolder $Category
    $nested = Join-Path $outer $Inner
    if (Test-Path -LiteralPath $nested) { return $nested }
    return $outer
}
$runtime = Get-CategoryRoot 'runtime-final' 'runtime'
foreach ($child in Get-ChildItem -LiteralPath $runtime -Force) { Copy-Safe $child.FullName (Join-Path $ProfileFolder $child.Name) }
foreach ($category in @('second-brain','development')) {
    $root = Get-CategoryRoot $category $category
    Copy-Safe (Join-Path $root 'dev') (Join-Path $ProfileFolder 'dev')
}
$personal = Get-CategoryRoot 'personal-files' 'personal-files'
foreach ($name in @('Documents','Desktop','Downloads','Pictures','Music','Videos','OneDrive','Favorites','Tools')) { Copy-Safe (Join-Path $personal $name) (Join-Path $ProfileFolder $name) }
$extra = Get-CategoryRoot 'extra-settings' 'extra-settings'
if (Test-Path -LiteralPath (Join-Path $extra 'home')) { foreach ($child in Get-ChildItem -LiteralPath (Join-Path $extra 'home') -Force) { Copy-Safe $child.FullName (Join-Path $ProfileFolder $child.Name) } }
if ('codex-final-delta' -in $active) {
    $delta = Get-CategoryRoot 'codex-final-delta' 'codex-final-delta'
    Copy-Safe (Join-Path $delta 'second-brain\dev') (Join-Path $ProfileFolder 'dev')
    if (Test-Path -LiteralPath (Join-Path $delta 'runtime')) { $delta = Join-Path $delta 'runtime' }
    if (Test-Path -LiteralPath (Join-Path $delta '.codex')) { Copy-Safe (Join-Path $delta '.codex') (Join-Path $ProfileFolder '.codex') } else { throw 'Unexpected final delta layout. Keep apps closed and restore it manually using the staged evidence.' }
}
Write-Host "Core files restored. Preexisting conflicts preserved: $preexisting"
Write-Host 'AppData and sqlite-live-raw remain staged. Reinstall apps/tools, sign in, and review old absolute paths before opening Codex.'
