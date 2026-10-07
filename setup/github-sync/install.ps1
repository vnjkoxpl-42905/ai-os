param([switch]$VerifyOnly)
$ErrorActionPreference = 'Stop'
$taskName = 'AI OS - Private GitHub Sync'
$syncScript = Join-Path $PSScriptRoot 'run_sync.py'
$syncConfig = Join-Path $PSScriptRoot 'config.json'
$pythonPath = (Get-Command python.exe -ErrorAction Stop).Source
if (!(Test-Path -LiteralPath $syncScript)) { throw 'Sync script is missing.' }
if ($VerifyOnly) {
    Get-ScheduledTask -TaskName $taskName -ErrorAction Stop | Get-ScheduledTaskInfo
    exit
}
$taskArguments = '"{0}" --once --config "{1}"' -f $syncScript, $syncConfig
$taskAction = New-ScheduledTaskAction -Execute $pythonPath -Argument $taskArguments -WorkingDirectory $PSScriptRoot
$repeatTrigger = New-ScheduledTaskTrigger -Once -At (Get-Date).AddMinutes(2) -RepetitionInterval (New-TimeSpan -Minutes 2)
$logonTrigger = New-ScheduledTaskTrigger -AtLogOn -User ([System.Security.Principal.WindowsIdentity]::GetCurrent().Name)
$taskSettings = New-ScheduledTaskSettingsSet -MultipleInstances IgnoreNew -StartWhenAvailable -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -ExecutionTimeLimit (New-TimeSpan -Minutes 90) -Hidden
$taskPrincipal = New-ScheduledTaskPrincipal -UserId ([System.Security.Principal.WindowsIdentity]::GetCurrent().Name) -LogonType Interactive -RunLevel Limited
Register-ScheduledTask -TaskName $taskName -Action $taskAction -Trigger @($repeatTrigger, $logonTrigger) -Settings $taskSettings -Principal $taskPrincipal -Description 'Filtered project and conversation snapshots to private GitHub branches and verified Google Drive archives.' -Force | Select-Object TaskName, State
