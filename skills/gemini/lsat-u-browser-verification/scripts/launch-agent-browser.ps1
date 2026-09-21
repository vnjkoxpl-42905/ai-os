# Permanent machine infrastructure launcher for LSAT U Agent Browser
# Target: Port 9223, persistent user-data-dir: %LOCALAPPDATA%\LSATU-Agent-Chrome

$chromeExe = "C:\Program Files\Google\Chrome\Application\chrome.exe"
$profileDir = "$env:LOCALAPPDATA\LSATU-Agent-Chrome"
$targetUrl = "https://lsatprep.study"

# Check if already running on 9223
$conn = Get-NetTCPConnection -LocalPort 9223 -ErrorAction SilentlyContinue
if ($conn) {
    Write-Output "LSAT U Agent Browser is already running on 127.0.0.1:9223 (PID $($conn.OwningProcess))."
    exit 0
}

# Ensure directory exists
if (-not (Test-Path $profileDir)) {
    New-Item -ItemType Directory -Path $profileDir -Force | Out-Null
}

$cmd = "`"$chromeExe`" --remote-debugging-port=9223 --remote-debugging-address=127.0.0.1 --remote-allow-origins=* --user-data-dir=`"$profileDir`" --no-first-run --no-default-browser-check $targetUrl"

$res = Invoke-CimMethod -ClassName Win32_Process -MethodName Create -Arguments @{CommandLine = $cmd}
if ($res.ReturnValue -eq 0) {
    Write-Output "Spawned LSAT U Agent Browser via WMI (PID $($res.ProcessId))."
} else {
    Write-Output "Failed to launch Chrome via WMI. ReturnValue: $($res.ReturnValue)"
    exit 1
}

# Wait up to 5 seconds for port 9223
for ($i = 0; $i -lt 10; $i++) {
    Start-Sleep -Milliseconds 500
    $conn = Get-NetTCPConnection -LocalPort 9223 -ErrorAction SilentlyContinue
    if ($conn) {
        Write-Output "SUCCESS: LSAT U Agent Browser is listening on 127.0.0.1:9223."
        exit 0
    }
}

Write-Output "WARNING: Port 9223 did not open within 5 seconds."
exit 1
