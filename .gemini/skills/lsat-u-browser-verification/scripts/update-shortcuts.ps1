$chromeExe = "C:\Program Files\Google\Chrome\Application\chrome.exe"
$profileDir = "$env:LOCALAPPDATA\LSATU-Agent-Chrome"
$chromeArgs = "--remote-debugging-port=9223 --remote-debugging-address=127.0.0.1 --remote-allow-origins=* --user-data-dir=`"$profileDir`" --no-first-run --no-default-browser-check https://lsatprep.study"

$wsh = New-Object -ComObject WScript.Shell

# Desktop shortcut
$desktopPath = [Environment]::GetFolderPath("Desktop")
$s1 = $wsh.CreateShortcut("$desktopPath\LSAT U Agent Browser.lnk")
$s1.TargetPath = $chromeExe
$s1.Arguments = $chromeArgs
$s1.Description = "Dedicated Chrome instance for LSAT U visual verification on port 9223"
$s1.IconLocation = "$chromeExe,0"
$s1.Save()
Write-Output "Updated: $desktopPath\LSAT U Agent Browser.lnk (Port 9223)"

# Start Menu Programs shortcut
$startMenuPrograms = [Environment]::GetFolderPath("Programs")
$s2 = $wsh.CreateShortcut("$startMenuPrograms\LSAT U Agent Browser.lnk")
$s2.TargetPath = $chromeExe
$s2.Arguments = $chromeArgs
$s2.Description = "Dedicated Chrome instance for LSAT U visual verification on port 9223"
$s2.IconLocation = "$chromeExe,0"
$s2.Save()
Write-Output "Updated: $startMenuPrograms\LSAT U Agent Browser.lnk (Port 9223)"
