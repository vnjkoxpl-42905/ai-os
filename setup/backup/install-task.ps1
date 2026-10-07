# install-task.ps1 - register the "Claude Code Backup" scheduled tasks (every 10 min, and at logon).
# Works without admin rights (per-user tasks via schtasks).
$script = Join-Path $env:USERPROFILE 'dev\ai-os\setup\backup\backup.ps1'
$tr = "powershell.exe -NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -File \`"$script\`""
schtasks.exe /Create /F /TN 'Claude Code Backup' /SC MINUTE /MO 10 /TR $tr | Out-Null
schtasks.exe /Create /F /TN 'Claude Code Backup (logon)' /SC ONLOGON /TR $tr | Out-Null
schtasks.exe /Query /TN 'Claude Code Backup' /FO LIST | Select-String 'Status|Next Run'
Write-Host "Scheduled tasks registered: every 10 minutes and at logon."
