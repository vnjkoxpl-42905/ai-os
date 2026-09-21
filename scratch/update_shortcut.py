import os
import subprocess

profile_dir = os.path.expandvars(r"%LOCALAPPDATA%\LSATU-Agent-Chrome")
chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
shortcut_args = f'--remote-debugging-port=9222 --remote-debugging-address=127.0.0.1 --remote-allow-origins=* --user-data-dir="{profile_dir}" --no-first-run --no-default-browser-check'

ps_cmd = f"""
$wsh = New-Object -ComObject WScript.Shell
$desktop = [Environment]::GetFolderPath("Desktop")
$s1 = $wsh.CreateShortcut("$desktop\\LSAT U Agent Browser.lnk")
$s1.TargetPath = "{chrome_exe}"
$s1.Arguments = '{shortcut_args}'
$s1.Description = "Dedicated Chrome instance for LSAT U visual verification in Antigravity"
$s1.IconLocation = "{chrome_exe},0"
$s1.Save()

$startMenu = [Environment]::GetFolderPath("Programs")
$s2 = $wsh.CreateShortcut("$startMenu\\LSAT U Agent Browser.lnk")
$s2.TargetPath = "{chrome_exe}"
$s2.Arguments = '{shortcut_args}'
$s2.Description = "Dedicated Chrome instance for LSAT U visual verification in Antigravity"
$s2.IconLocation = "{chrome_exe},0"
$s2.Save()

Write-Output "Shortcuts updated successfully with --remote-allow-origins=*"
"""

subprocess.run(["pwsh", "-Command", ps_cmd], check=True)
