# 1. Terminate background process 22320 if running on 9222
$conn = Get-NetTCPConnection -LocalPort 9222 -ErrorAction SilentlyContinue
if ($conn) {
    Write-Output "Stopping process on port 9222: PID $($conn.OwningProcess)"
    Stop-Process -Id $conn.OwningProcess -Force -ErrorAction SilentlyContinue
    Start-Sleep -Seconds 2
}

# 2. Create persistent directory
$profileDir = "$env:LOCALAPPDATA\LSATU-Agent-Chrome"
if (-not (Test-Path $profileDir)) {
    New-Item -ItemType Directory -Path $profileDir -Force | Out-Null
    Write-Output "Created directory: $profileDir"
} else {
    Write-Output "Directory already exists: $profileDir"
}

# 3. Create Windows Shortcut on Desktop and Start Menu
$chromeExe = "C:\Program Files\Google\Chrome\Application\chrome.exe"
$chromeArgs = "--remote-debugging-port=9222 --remote-debugging-address=127.0.0.1 --user-data-dir=`"$profileDir`" --no-first-run --no-default-browser-check"

$wsh = New-Object -ComObject WScript.Shell

# Desktop shortcut
$desktopPath = [Environment]::GetFolderPath("Desktop")
$shortcutDesktop = $wsh.CreateShortcut("$desktopPath\LSAT U Agent Browser.lnk")
$shortcutDesktop.TargetPath = $chromeExe
$shortcutDesktop.Arguments = $chromeArgs
$shortcutDesktop.Description = "Dedicated Chrome instance for LSAT U visual verification in Antigravity"
$shortcutDesktop.IconLocation = "$chromeExe,0"
$shortcutDesktop.Save()
Write-Output "Created shortcut: $desktopPath\LSAT U Agent Browser.lnk"

# Start Menu Programs shortcut
$startMenuPrograms = [Environment]::GetFolderPath("Programs")
$shortcutStart = $wsh.CreateShortcut("$startMenuPrograms\LSAT U Agent Browser.lnk")
$shortcutStart.TargetPath = $chromeExe
$shortcutStart.Arguments = $chromeArgs
$shortcutStart.Description = "Dedicated Chrome instance for LSAT U visual verification in Antigravity"
$shortcutStart.IconLocation = "$chromeExe,0"
$shortcutStart.Save()
Write-Output "Created shortcut: $startMenuPrograms\LSAT U Agent Browser.lnk"

# 4. Check port 9222 availability
$check = Get-NetTCPConnection -LocalPort 9222 -ErrorAction SilentlyContinue
if ($check) {
    Write-Output "Port 9222 still in use by PID $($check.OwningProcess)"
} else {
    Write-Output "Port 9222 is now FREE and ready for LSAT U Agent Browser"
}
