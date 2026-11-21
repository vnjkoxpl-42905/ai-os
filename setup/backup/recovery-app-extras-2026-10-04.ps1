$ErrorActionPreference = 'Stop'
$taskRoot = 'C:\Users\Joshu\laptop-recovery-2026-10-04'
$taskStage = Join-Path $taskRoot 'staging'
$taskLog = Join-Path $taskRoot 'logs\app-extras.log'
function Save-Extra([string]$Source,[string]$Relative,[string[]]$Exclude=@()) {
    if (-not (Test-Path -LiteralPath $Source)) { return }
    $destination = Join-Path $taskStage $Relative
    New-Item -ItemType Directory -Force -Path $destination | Out-Null
    $copyArgs = @($Source,$destination,'/E','/XJ','/SL','/R:0','/W:0','/MT:4','/NP','/NFL','/NDL',('/LOG+:'+$taskLog),'/XF','*.sqlite','*.sqlite-wal','*.sqlite-shm','*.sqlite3','*.sqlite3-wal','*.sqlite3-shm','*.db','*.db-wal','*.db-shm')
    if ($Exclude.Count) { $copyArgs += '/XD'; $copyArgs += $Exclude }
    & robocopy @copyArgs | Out-Null
    if ($LASTEXITCODE -ge 8) { "Copy error: $Source rc=$LASTEXITCODE" | Add-Content (Join-Path $taskRoot 'APP-EXTRAS-ISSUES.txt') }
    & python (Join-Path $taskRoot 'sqlite-snapshot.py') $Source $destination (Join-Path $taskStage ('sqlite-live-raw\'+$Relative))
    if ($LASTEXITCODE -ne 0) { "SQLite error: $Source" | Add-Content (Join-Path $taskRoot 'APP-EXTRAS-ISSUES.txt') }
}
Save-Extra (Join-Path $env:APPDATA 'Code\User') 'app-data\AppData\Roaming\Code\User'
Save-Extra (Join-Path $env:APPDATA 'Antigravity IDE\User') 'app-data\AppData\Roaming\Antigravity IDE\User'
Save-Extra (Join-Path $env:LOCALAPPDATA 'OpenAI\Codex') 'app-data\AppData\Local\OpenAI\Codex'
Save-Extra (Join-Path $env:LOCALAPPDATA 'com.superwhisper.app') 'app-data\AppData\Local\com.superwhisper.app' @('models')
$edgeSource = Join-Path $env:LOCALAPPDATA 'Microsoft\Edge\User Data\Default'
$edgeDest = Join-Path $taskStage 'app-data\AppData\Local\Microsoft\Edge\User Data\Default'
New-Item -ItemType Directory -Force -Path $edgeDest | Out-Null
foreach ($name in 'Bookmarks','Bookmarks.bak') { if (Test-Path -LiteralPath (Join-Path $edgeSource $name)) { Copy-Item -LiteralPath (Join-Path $edgeSource $name) -Destination (Join-Path $edgeDest $name) } }
"DONE $(Get-Date -Format o); excluded Superwhisper models, browser cache" | Set-Content (Join-Path $taskRoot 'APP-EXTRAS-PROGRESS.txt')
