# C:\Users\Joshu\Tools\LSATU-Agent\start-dev-session.ps1
# One-click workflow script to launch LSAT U Agent Browser and verify environment

$chromeExe = "C:\Program Files\Google\Chrome\Application\chrome.exe"
$profileDir = "$env:LOCALAPPDATA\LSATU-Agent-Chrome"
$port = 9223

Write-Host "=== LSAT U Agent Environment Check ===" -ForegroundColor Cyan

# 1. Check Chrome on Port 9223
$conn = Get-NetTCPConnection -LocalPort $port -ErrorAction SilentlyContinue
if ($conn) {
    Write-Host "[OK] LSAT U Agent Browser is already running on port $port." -ForegroundColor Green
} else {
    Write-Host "[..] Launching LSAT U Agent Browser on port $port..." -ForegroundColor Yellow
    & pwsh -File "C:\Users\Joshu\Tools\LSATU-Agent\launch-agent-browser.ps1"
}

# 2. Check local dev server on localhost:8080
$viteConn = Get-NetTCPConnection -LocalPort 8080 -ErrorAction SilentlyContinue
if ($viteConn) {
    Write-Host "[OK] Local Vite dev server is active on port 8080." -ForegroundColor Green
} else {
    Write-Host "[INFO] Local dev server is not currently running. Start it anytime with: npm run dev" -ForegroundColor Gray
}

# 3. Verify CDP status
try {
    $ver = Invoke-RestMethod -Uri "http://127.0.0.1:$port/json/version" -TimeoutSec 3
    Write-Host "[OK] Chrome DevTools Protocol responsive: $($ver.Browser)" -ForegroundColor Green
    Write-Host "Environment is ready for Antigravity visual verification!" -ForegroundColor Green
} catch {
    Write-Host "[ERROR] Could not connect to Chrome CDP endpoint: $_" -ForegroundColor Red
}
