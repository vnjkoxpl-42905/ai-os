<#
    01-defender-exclusions.ps1
    Run ONCE, elevated (right-click > Run with PowerShell, or from an admin terminal).

    Why: Defender real-time scanning inspects every file a build touches. On a
    node_modules tree that is tens of thousands of small files per install.
    Excluding dev trees and dev processes is the single largest speed win on
    this machine — typically 2-4x on npm/pnpm install and vite builds.

    Scope: This ONLY narrows scanning for your own dev folders and toolchain
    binaries. Downloads, email, browsers, and the rest of the system stay fully
    protected. Nothing here disables Defender.

    To undo: swap Add-MpPreference for Remove-MpPreference and re-run.
#>

#Requires -RunAsAdministrator

$paths = @(
    'C:\Users\Joshu\dev'
    'C:\Users\Joshu\AppData\Roaming\npm'
    'C:\Users\Joshu\AppData\Local\pnpm'
    'C:\Users\Joshu\.cargo'
    'C:\Users\Joshu\go'
    'C:\Users\Joshu\AppData\Local\Programs\Microsoft VS Code'
)

$processes = @(
    'node.exe', 'npm.exe', 'pnpm.exe', 'bun.exe', 'deno.exe'
    'git.exe', 'rg.exe', 'fd.exe'
    'Code.exe', 'cargo.exe', 'rustc.exe', 'go.exe', 'python.exe'
)

Write-Host "Adding Defender path exclusions..." -ForegroundColor Cyan
foreach ($p in $paths) {
    if (Test-Path $p) {
        Add-MpPreference -ExclusionPath $p
        Write-Host "  + $p" -ForegroundColor Green
    } else {
        Write-Host "  ! skipped (not found): $p" -ForegroundColor Yellow
    }
}

Write-Host "`nAdding Defender process exclusions..." -ForegroundColor Cyan
foreach ($e in $processes) {
    Add-MpPreference -ExclusionProcess $e
    Write-Host "  + $e" -ForegroundColor Green
}

Write-Host "`n--- Current exclusions ---" -ForegroundColor Cyan
$pref = Get-MpPreference
Write-Host "Paths:"     -ForegroundColor White; $pref.ExclusionPath     | ForEach-Object { "  $_" }
Write-Host "Processes:" -ForegroundColor White; $pref.ExclusionProcess  | ForEach-Object { "  $_" }

Write-Host "`nDone." -ForegroundColor Green
