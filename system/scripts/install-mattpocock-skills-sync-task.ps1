param([switch]$VerifyOnly)
$ErrorActionPreference = 'Stop'

$TaskName = 'AI OS - Matt Pocock Skills Sync'
$VaultRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
$SyncScript = Join-Path $PSScriptRoot 'sync-mattpocock-skills.py'
$PythonPath = (Get-Command python.exe -ErrorAction Stop).Source
$GhPath = (Get-Command gh.exe -ErrorAction Stop).Source

if (!(Test-Path -LiteralPath $SyncScript)) { throw "Sync script missing: $SyncScript" }
if ($VerifyOnly) {
    Get-ScheduledTask -TaskName $TaskName -ErrorAction Stop | Get-ScheduledTaskInfo
    exit
}

# Confirm the scheduled user's GitHub CLI can read the upstream repository.
& $GhPath auth status | Out-Null
if ($LASTEXITCODE -ne 0) { throw 'GitHub CLI authentication is unavailable; task was not registered.' }

$TaskArguments = '"{0}"' -f $SyncScript
$Action = New-ScheduledTaskAction -Execute $PythonPath -Argument $TaskArguments -WorkingDirectory $VaultRoot
$DailyTrigger = New-ScheduledTaskTrigger -Daily -At '6:30AM'
$LogonTrigger = New-ScheduledTaskTrigger -AtLogOn -User ([System.Security.Principal.WindowsIdentity]::GetCurrent().Name)
$Settings = New-ScheduledTaskSettingsSet -MultipleInstances IgnoreNew -StartWhenAvailable -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -ExecutionTimeLimit (New-TimeSpan -Hours 2) -Hidden
$Principal = New-ScheduledTaskPrincipal -UserId ([System.Security.Principal.WindowsIdentity]::GetCurrent().Name) -LogonType Interactive -RunLevel Limited

Register-ScheduledTask -TaskName $TaskName -Action $Action -Trigger @($DailyTrigger, $LogonTrigger) -Settings $Settings -Principal $Principal -Description 'Updates clean Matt Pocock skill copies and installs new upstream skills without overwriting local customizations.' -Force | Select-Object TaskName, State
