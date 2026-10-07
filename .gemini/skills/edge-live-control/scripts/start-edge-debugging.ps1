# start-edge-debugging.ps1
# Ensures Microsoft Edge is running with Chrome DevTools Protocol enabled on specified port.

param(
    [int]$Port = 9223,
    [string]$Url = "",
    [switch]$ForceRestart
)

$ErrorActionPreference = "Stop"

function Test-PortResponding {
    param([int]$CheckPort)
    try {
        $response = Invoke-RestMethod -Uri "http://localhost:$CheckPort/json/version" -TimeoutSec 2 -ErrorAction SilentlyContinue
        if ($response -and $response.webSocketDebuggerUrl) {
            return $true
        }
    } catch {
        return $false
    }
    return $false
}

Write-Host "Checking if Edge remote debugging is active on port $Port..."
if (Test-PortResponding -CheckPort $Port) {
    Write-Host "Edge remote debugging is already active on port $Port."
    if ($Url) {
        Start-Process "msedge.exe" -ArgumentList $Url
    }
    exit 0
}

$edgeProcesses = Get-Process -Name "msedge" -ErrorAction SilentlyContinue
if ($edgeProcesses) {
    Write-Host "Edge is currently running without remote debugging enabled."
    Write-Host "Terminating background Edge processes to allow remote debugging attachment..."
    Stop-Process -Name "msedge" -Force -ErrorAction SilentlyContinue
    Start-Sleep -Seconds 1
}

$edgePaths = @(
    "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    "$env:LOCALAPPDATA\Microsoft\Edge\Application\msedge.exe"
)

$edgeExe = $edgePaths | Where-Object { Test-Path $_ } | Select-Object -First 1

if (-not $edgeExe) {
    Write-Error "Microsoft Edge executable not found in standard paths."
    exit 1
}

$launchArgs = @(
    "--remote-debugging-port=$Port",
    "--restore-last-session"
)

if ($Url) {
    $launchArgs += $Url
}

Write-Host "Launching Microsoft Edge with remote debugging on port $Port..."
Start-Process -FilePath $edgeExe -ArgumentList $launchArgs

$maxRetries = 15
$connected = $false
for ($i = 0; $i -lt $maxRetries; $i++) {
    Start-Sleep -Milliseconds 800
    if (Test-PortResponding -CheckPort $Port) {
        $connected = $true
        break
    }
}

if ($connected) {
    Write-Host "Successfully connected to Edge on port $Port."
    exit 0
} else {
    Write-Warning "Edge launched, but port $Port did not respond within timeout."
    exit 1
}
