<#
    02-remove-bloatware.ps1
    Run elevated, AFTER reading the list below. This script REMOVES software.

    Measured on this machine 2026-09-07, these were the resident memory costs
    of the OEM/trial software with nothing else running:

        Dell.TechHub.Instrumentation.SubAgent   303 MB
        SupportAssistAgent                      260 MB
        WavesSysSvc64                           235 MB   (audio - see note)
        mc-fw-host (McAfee firewall host)       230 MB

    At the time of audit the machine had only 2.7 GB of 16 GB free. Reclaiming
    ~800 MB-1 GB of that is the difference between comfortable and swapping.

    WHAT EACH ONE IS
    ----------------
    McAfee + WebAdvisor  - Preinstalled trial AV. Windows Defender is already
                           running and is sufficient. Two real-time scanners on
                           one box is strictly worse than one. SAFE TO REMOVE.

    Dell SupportAssist   - Driver-update nag + telemetry agent. Drivers can be
    + Dell Core Services   updated through Windows Update or dell.com/support.
    + Dell Optimizer       SAFE TO REMOVE. (Dell Optimizer also manages some
                           thermal/battery profiles - if you care about Dell's
                           battery-longevity mode, keep Optimizer and drop the
                           rest.)

    Waves MaxxAudio      - NOT INCLUDED BELOW. This one is tied to the Realtek
                           audio driver on Dell machines; removing it can leave
                           you with no speaker EQ or, in some cases, degraded
                           audio. 235 MB is real but the risk is real too.
                           Left in place deliberately. Remove manually only if
                           you don't care about audio tuning.

    Xbox / Solitaire /   - Consumer apps, zero cost when not running, but they
    Bing News / Weather    clutter Start and update in the background.
                           Uncomment the OPTIONAL block to remove.

    NOTHING IN THIS SCRIPT TOUCHES YOUR FILES, YOUR VAULT, OR YOUR DEV TOOLS.
#>

#Requires -RunAsAdministrator

$ErrorActionPreference = 'Continue'

function Remove-WingetPkg {
    param([string]$Id, [string]$Label)
    Write-Host "`n--- $Label ($Id)" -ForegroundColor Cyan
    $found = winget list --id $Id -e --disable-interactivity 2>$null | Select-String $Id
    if (-not $found) { Write-Host "  not installed, skipping" -ForegroundColor DarkGray; return }
    winget uninstall --id $Id -e --disable-interactivity --accept-source-agreements 2>&1 |
        Select-Object -Last 2 | ForEach-Object { "  $_" }
}

Write-Host "=== Removing McAfee (Defender is already active) ===" -ForegroundColor Yellow
Remove-WingetPkg -Id 'McAfee.wps'      -Label 'McAfee WPS'
Remove-WingetPkg -Id 'McAfee.WebAdvisor' -Label 'McAfee WebAdvisor'

Write-Host "`n=== Removing Dell telemetry / support agents ===" -ForegroundColor Yellow
Remove-WingetPkg -Id 'Dell.SupportAssist'  -Label 'Dell SupportAssist'
Remove-WingetPkg -Id 'Dell.Optimizer'      -Label 'Dell Optimizer'

# ---------------------------------------------------------------------------
# OPTIONAL: consumer Store apps. Uncomment to remove.
# ---------------------------------------------------------------------------
# $storeApps = @(
#     'Microsoft.MicrosoftSolitaireCollection'
#     'Microsoft.BingNews'
#     'Microsoft.BingWeather'
#     'Microsoft.GamingApp'
#     'Microsoft.XboxGamingOverlay'
#     'Clipchamp.Clipchamp'
# )
# foreach ($a in $storeApps) {
#     Write-Host "Removing $a" -ForegroundColor Cyan
#     Get-AppxPackage -Name $a -AllUsers | Remove-AppxPackage -AllUsers -ErrorAction SilentlyContinue
# }

Write-Host "`n=== Remaining memory picture ===" -ForegroundColor Yellow
Get-Process | Sort-Object WS -Descending | Select-Object -First 12 Name,
    @{n='MB';e={[int]($_.WS/1MB)}} | Format-Table -AutoSize

Write-Host "`nReboot to reclaim everything. Done." -ForegroundColor Green
