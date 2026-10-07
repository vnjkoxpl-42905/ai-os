$ErrorActionPreference = 'Stop'
$Stage = Join-Path $env:USERPROFILE 'LaptopBackups\2026-10-07'
$Receipts = @(Get-ChildItem -LiteralPath $Stage -Filter CLOUD-VERIFIED.json -Recurse -File)
if ($Receipts.Count -eq 0) { throw 'No cloud verification receipt exists. Task registration refused.' }
function Test-CloudReceipt([string]$GenerationDirectory) {
    try {
        $Receipt = Get-Content -LiteralPath (Join-Path $GenerationDirectory 'CLOUD-VERIFIED.json') -Raw | ConvertFrom-Json
        if (-not $Receipt.complete -or $Receipt.account -ne 'contact@aspiringattorneys.com' -or $Receipt.generation -ne (Split-Path $GenerationDirectory -Leaf) -or $Receipt.files.Count -lt 1) { return $false }
        foreach ($File in $Receipt.files) { if (-not $File.id -or $File.md5Checksum -notmatch '^[0-9a-f]{32}$' -or [long]$File.size -lt 0) { return $false } }
        return $true
    } catch { return $false }
}
$VerifiedScopes = @($Receipts | ForEach-Object {
    $Directory = $_.DirectoryName
    $Manifest = Get-Content -LiteralPath (Join-Path $Directory 'manifest.json') -Raw | ConvertFrom-Json
    $ChainValid = Test-CloudReceipt $Directory
    if ($Manifest.complete -and $ChainValid) {
        $Dependencies = @($Manifest.files.PSObject.Properties.Value.generation | Select-Object -Unique)
        foreach ($Dependency in $Dependencies) { if (-not (Test-CloudReceipt (Join-Path $Stage $Dependency))) { $ChainValid = $false } }
        if ($ChainValid) { $Manifest.scope }
    }
})
if ('core' -notin $VerifiedScopes -or 'personal' -notin $VerifiedScopes) { throw 'Both core and personal cloud backup must verify before scheduling.' }
$PythonPath = (Get-Command python -ErrorAction Stop).Source
$PythonWindowlessPath = Join-Path (Split-Path $PythonPath -Parent) 'pythonw.exe'
if (-not (Test-Path -LiteralPath $PythonWindowlessPath)) { $PythonWindowlessPath = $PythonPath }
$GwsPath = (Get-Command gws -ErrorAction Stop).Source
$RunnerPath = Join-Path $PSScriptRoot 'new-machine-run.py'
$TaskName = 'Private Laptop Backup - Replacement'
if (Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue) { throw 'Task already exists; inspect before changing it.' }
@{ python = $PythonPath; gws = $GwsPath; generated = (Get-Date -Format 'yyyy-MM-dd HH:mm:ss') } | ConvertTo-Json | Set-Content -LiteralPath (Join-Path $PSScriptRoot 'new-machine-runtime.json') -Encoding UTF8
$Action = New-ScheduledTaskAction -Execute $PythonWindowlessPath -Argument ('"' + $RunnerPath + '"') -WorkingDirectory $PSScriptRoot
$Triggers = @(New-ScheduledTaskTrigger -Daily -At '7:00PM'; New-ScheduledTaskTrigger -AtLogOn -User ([System.Security.Principal.WindowsIdentity]::GetCurrent().Name))
$Principal = New-ScheduledTaskPrincipal -UserId ([System.Security.Principal.WindowsIdentity]::GetCurrent().Name) -LogonType Interactive -RunLevel Limited
$Settings = New-ScheduledTaskSettingsSet -MultipleInstances IgnoreNew -ExecutionTimeLimit (New-TimeSpan -Hours 4) -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable
Register-ScheduledTask -TaskName $TaskName -Action $Action -Trigger $Triggers -Principal $Principal -Settings $Settings -Description 'Non-deleting dated private Google Drive backup; explicit account and cloud checksum verification; never commits or prunes.' | Out-Null
Write-Output 'Registered daily 19:00 local and at logon. Old recovery tasks are untouched.'
