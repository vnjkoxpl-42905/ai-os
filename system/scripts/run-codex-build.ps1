# Run a Codex-built, Claude-inspected build (claudex-loop / codex-build) from a REAL PowerShell.
#
# Why this exists: on this Windows machine the Codex sandbox only works when the Claude runner is
# started from the user's own PowerShell (the Terminal panel in the Claude desktop app, or any
# normal PowerShell), using the Codex CLI installed in %APPDATA%\npm. See
# references/claude-plus-codex.md, section "Running codex-build on this Windows machine".
#
# Usage (from PowerShell):
#   & C:\Users\Joshu\dev\ai-os\system\scripts\run-codex-build.ps1 `
#       -Repo C:\Users\Joshu\dev\ai-os-codex-ore `
#       -Plan C:\path\to\work-order.md `
#       -Proof "python -c ""print('ok')"""
#
# -Repo must be a CLEAN checkout (a worktree is fine) that already contains every file the work order names.
# -Plan should live OUTSIDE the checkout. Add -Approved <result.json> if the plan was reviewed; otherwise
# the run is recorded as an unreviewed work order. Codex's sandbox usually cannot run `python`, so the host
# (Claude) must run the proof itself and inspect every changed file afterwards. Nothing is committed or pushed.

param(
  [Parameter(Mandatory = $true)][string]$Repo,
  [Parameter(Mandatory = $true)][string]$Plan,
  [Parameter(Mandatory = $true)][string]$Proof,
  [string]$Approved = '',
  [string]$Artifacts = ''
)

$ErrorActionPreference = 'Stop'
$runner = Join-Path $PSScriptRoot '..\..\.claude\skills\claudex-loop\scripts\runner.py'
$codex = Join-Path $env:APPDATA 'npm\codex.cmd'
if (-not (Test-Path $codex)) { throw "Codex CLI not found at $codex. Install it from this shell: npm install -g @openai/codex" }
if (-not (Test-Path $runner)) { throw "Runner not found at $runner" }
if (-not $Artifacts) { $Artifacts = Join-Path $env:TEMP ('codex-build-' + (Get-Date -Format 'yyyyMMdd-HHmmss')) }
New-Item -ItemType Directory -Force -Path $Artifacts | Out-Null

Write-Host ('codex:   ' + (& $codex --version))
Write-Host ('login:   ' + (& $codex login status))
Push-Location $Repo
try {
  $dirty = (git status --short | Measure-Object).Count
  if ($dirty -ne 0) { throw "Checkout $Repo has $dirty uncommitted change(s); a delegated build needs a clean checkout." }
  $base = (git rev-parse HEAD).Trim()
  Write-Host ('base:    ' + $base)
  [string[]]$approval = if ($Approved) { @('--approval', $Approved) } else { @('--unreviewed-spec') }
  python $runner build --host claude --builder codex --repo $Repo --plan $Plan @approval --cli $codex --proof $Proof --artifacts $Artifacts --timeout 1800
  Write-Host ('artifacts: ' + $Artifacts)
  Write-Host ('Next: Claude inspects with  python runner.py inspect --host claude --builder codex --repo ' + $Repo + ' --plan ' + $Plan + ' --base ' + $base)
}
finally { Pop-Location }
