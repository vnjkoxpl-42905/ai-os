$chromeExe = "C:\Program Files\Google\Chrome\Application\chrome.exe"
$profileDir = "$env:LOCALAPPDATA\LSATU-Agent-Chrome"
$cmd = "`"$chromeExe`" --remote-debugging-port=9222 --remote-debugging-address=127.0.0.1 --remote-allow-origins=* --user-data-dir=`"$profileDir`" --no-first-run --no-default-browser-check https://lsatprep.study"

$res = Invoke-CimMethod -ClassName Win32_Process -MethodName Create -Arguments @{CommandLine = $cmd}
Write-Output "WMI Spawn ReturnValue: $($res.ReturnValue), ProcessId: $($res.ProcessId)"

Start-Sleep -Seconds 3

$conn = Get-NetTCPConnection -LocalPort 9222 -ErrorAction SilentlyContinue
if ($conn) {
    Write-Output "SUCCESS: Port 9222 is listening! OwningProcess: $($conn.OwningProcess)"
} else {
    Write-Output "FAILED: Port 9222 is not listening."
}
