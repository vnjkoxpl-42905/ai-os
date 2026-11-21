$ErrorActionPreference = 'Stop'
$taskRoot = 'C:\Users\Joshu\laptop-recovery-2026-10-04'
foreach ($name in 'Desktop','Documents','Downloads','OneDrive','Pictures','Videos','Music') {
    $source = Join-Path $env:USERPROFILE $name
    if (-not (Test-Path -LiteralPath $source)) { continue }
    $destination = Join-Path $taskRoot ('staging\personal-files\' + $name)
    New-Item -ItemType Directory -Force -Path $destination | Out-Null
    & robocopy $source $destination /E /XJ /SL /R:0 /W:0 /MT:4 /COPY:DAT /DCOPY:DAT /NP /NFL /NDL (('/LOG:' + (Join-Path $taskRoot ('logs\personal-prestage-' + $name + '.log')))) /XD node_modules .venv venv .vite .turbo .next __pycache__ | Out-Null
    if ($LASTEXITCODE -ge 8) { "$source failed with robocopy $LASTEXITCODE" | Add-Content (Join-Path $taskRoot 'PERSONAL-PRESTAGE-ISSUES.txt') }
}
"DONE $(Get-Date -Format o)" | Set-Content (Join-Path $taskRoot 'PERSONAL-PRESTAGE-PROGRESS.txt')
