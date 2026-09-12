# install-task.ps1 - register the "Claude Code Backup" scheduled task (every 10 min + at logon).
$script = Join-Path $env:USERPROFILE 'dev\ai-os\setup\backup\backup.ps1'
$action = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument "-NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -File `"$script`""
$t1 = New-ScheduledTaskTrigger -Once -At (Get-Date).AddMinutes(1) -RepetitionInterval (New-TimeSpan -Minutes 10)
$t2 = New-ScheduledTaskTrigger -AtLogOn
$settings = New-ScheduledTaskSettingsSet -MultipleInstances IgnoreNew -ExecutionTimeLimit (New-TimeSpan -Hours 1) -StartWhenAvailable -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries
Register-ScheduledTask -TaskName 'Claude Code Backup' -Action $action -Trigger $t1,$t2 -Settings $settings -Force | Out-Null
Write-Host "Scheduled task 'Claude Code Backup' registered: every 10 minutes and at logon."
