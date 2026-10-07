$ErrorActionPreference = 'Stop'
$taskRoot = 'C:\Users\Joshu\laptop-recovery-2026-10-04'
function Prestage([string]$Source,[string]$Relative) {
    if (-not (Test-Path -LiteralPath $Source)) { return }
    $destination = Join-Path $taskRoot ('staging\app-data\' + $Relative)
    New-Item -ItemType Directory -Force -Path $destination | Out-Null
    $copyArgs=@($Source,$destination,'/E','/XJ','/SL','/R:0','/W:0','/MT:4','/COPY:DAT','/DCOPY:DAT','/NP','/NFL','/NDL',('/LOG+:'+(Join-Path $taskRoot 'logs\appdata-prestage.log')),'/XD','node_modules','.venv','venv','.vite','.turbo','.next','__pycache__','/XF','*.sqlite','*.sqlite-wal','*.sqlite-shm','*.sqlite3','*.sqlite3-wal','*.sqlite3-shm','*.db','*.db-wal','*.db-shm')
    & robocopy @copyArgs | Out-Null
    if ($LASTEXITCODE -ge 8) { "$Source failed with robocopy $LASTEXITCODE" | Add-Content (Join-Path $taskRoot 'APPDATA-PRESTAGE-ISSUES.txt') }
}
foreach ($name in 'Codex','Claude','Claude Code','Superwhisper','obsidian','gws','gh') {
    Prestage (Join-Path $env:APPDATA $name) ('AppData\Roaming\'+$name)
    Prestage (Join-Path $env:LOCALAPPDATA $name) ('AppData\Local\'+$name)
}
Get-ChildItem -LiteralPath (Join-Path $env:LOCALAPPDATA 'Packages') -Directory -Filter 'OpenAI.Codex*' | ForEach-Object {
    $package=$_
    foreach ($name in 'LocalState','LocalCache','RoamingState','Settings','AppData') { Prestage (Join-Path $package.FullName $name) ('AppData\Local\Packages\'+$package.Name+'\'+$name) }
}
"DONE $(Get-Date -Format o); SQLite files excluded, consistent snapshots captured by main" | Set-Content (Join-Path $taskRoot 'APPDATA-PRESTAGE-PROGRESS.txt')
