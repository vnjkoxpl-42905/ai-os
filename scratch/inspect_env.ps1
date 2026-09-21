Write-Output "=== Windows Version ==="
[System.Environment]::OSVersion.VersionString
(Get-CimInstance Win32_OperatingSystem).Caption

Write-Output "=== Chrome Executable & Version ==="
$chromePaths = @(
    "${env:ProgramFiles}\Google\Chrome\Application\chrome.exe",
    "${env:ProgramFiles(x86)}\Google\Chrome\Application\chrome.exe",
    "$env:LOCALAPPDATA\Google\Chrome\Application\chrome.exe"
)
foreach ($p in $chromePaths) {
    if (Test-Path $p) {
        Write-Output "Found Chrome: $p"
        (Get-Item $p).VersionInfo.ProductVersion
    }
}

Write-Output "=== Port 9222 Status ==="
$conn = Get-NetTCPConnection -LocalPort 9222 -ErrorAction SilentlyContinue
if ($conn) {
    $conn | Format-Table -AutoSize
} else {
    Write-Output "Port 9222 is FREE (not occupied)"
}

Write-Output "=== Node, NPM, NPX ==="
Get-Command node, npm, npx -ErrorAction SilentlyContinue | Select-Object Name, Source
Write-Output "Node version: $(node -v)"
Write-Output "NPM version: $(npm -v)"

Write-Output "=== Antigravity Processes & Version ==="
$agProcs = Get-Process -Name "*antigravity*" -ErrorAction SilentlyContinue
if ($agProcs) {
    $agProcs | Select-Object ProcessName, Path, Id | Format-Table -AutoSize
    $mainPath = ($agProcs | Where-Object { $_.Path } | Select-Object -First 1).Path
    if ($mainPath) {
        (Get-Item $mainPath).VersionInfo | Format-List
    }
} else {
    Write-Output "No running antigravity process detected by name."
}
