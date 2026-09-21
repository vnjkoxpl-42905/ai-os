$chromeExe = "C:\Program Files\Google\Chrome\Application\chrome.exe"
$profileDir = "$env:LOCALAPPDATA\LSATU-Agent-Chrome"

$proc = Start-Process $chromeExe -ArgumentList @(
    '--remote-debugging-port=9222',
    '--remote-debugging-address=127.0.0.1',
    "--user-data-dir=$profileDir",
    '--no-first-run',
    '--no-default-browser-check',
    'https://lsatprep.study'
) -PassThru

Start-Sleep -Seconds 3

$conn = Get-NetTCPConnection -LocalPort 9222 -ErrorAction SilentlyContinue
if ($conn) {
    Write-Output "SUCCESS: Chrome started (PID $($conn.OwningProcess)) and listening on 127.0.0.1:9222."
} else {
    Write-Output "WARNING: Chrome process started (PID $($proc.Id)) but port 9222 is not yet listening."
}
