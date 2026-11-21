param(
    [ValidateSet('codex', 'claude', 'antigravity')]
    [string]$Agent = 'codex',
    [switch]$AllAgents,
    [switch]$NewConversation,
    [switch]$CheckOnly,
    [string]$ResumeSession,
    [string]$WorkspacePath = (Split-Path (Split-Path $PSScriptRoot -Parent) -Parent)
)

$ErrorActionPreference = 'Stop'
$orcaCommand = Join-Path $env:LOCALAPPDATA 'Programs\orca\resources\bin\orca.cmd'
$stateName = if ($Agent -eq 'codex') { 'orca-launcher.json' } else { "orca-launcher-$Agent.json" }
$statePath = Join-Path $env:LOCALAPPDATA "AIOS\$stateName"
if (!(Test-Path -LiteralPath $orcaCommand)) { throw "Orca CLI not found: $orcaCommand" }

# Refresh this shell without restarting any running agent.
$env:Path = [Environment]::GetEnvironmentVariable('Path', 'Machine') + ';' + [Environment]::GetEnvironmentVariable('Path', 'User')

function Invoke-Orca {
    param([string[]]$Arguments, [switch]$AllowFailure)
    $output = & $orcaCommand @Arguments --json
    $exitCode = $LASTEXITCODE
    $result = $null
    if ($output) { $result = ($output -join "`n") | ConvertFrom-Json }
    if (!$AllowFailure -and ($exitCode -ne 0 -or !$result -or $result.ok -eq $false)) {
        throw "Orca command failed ($($Arguments -join ' ')): $($result.error.message)"
    }
    return $result
}

$status = Invoke-Orca -Arguments @('status') -AllowFailure
if (!$status -or $status.result.runtime.state -ne 'ready') {
    if ($CheckOnly) { throw 'Orca runtime is not ready. Run this launcher without -CheckOnly to open it.' }
    Write-Host 'Opening Orca and waiting for its runtime...'
    $null = Invoke-Orca -Arguments @('open')
    $status = Invoke-Orca -Arguments @('status')
    if ($status.result.runtime.state -ne 'ready') {
        throw 'Orca opened but its runtime is not ready. Existing projects and chats were preserved; no reset was attempted.'
    }
}

$repos = (Invoke-Orca -Arguments @('repo', 'list')).result.repos
$workspaceRepo = $repos | Where-Object { $_.path.Replace('/', '\').TrimEnd('\') -eq $WorkspacePath.TrimEnd('\') } | Select-Object -First 1
if (!$workspaceRepo) { throw "Saved workspace is missing: $WorkspacePath. No projects were recreated." }
$history = (Invoke-Orca -Arguments @('search', '--index-status')).result
Write-Host "Orca ready. Saved projects: $($repos.Count)."
Write-Host "History enabled: $($history.enabled); state: $($history.phase); failed files: $($history.filesFailed)."
if (!$history.enabled) { Write-Warning 'Enable Agent Session Search in Orca to search your saved chats.' }
if ($CheckOnly) { return }
if ($AllAgents) {
    foreach ($launchAgent in @('claude', 'antigravity', 'codex')) {
        & $PSCommandPath -Agent $launchAgent -WorkspacePath $WorkspacePath
    }
    return
}

$savedState = $null
if (Test-Path -LiteralPath $statePath) { $savedState = Get-Content -LiteralPath $statePath -Raw | ConvertFrom-Json }
if (!$ResumeSession -and $savedState) { $ResumeSession = $savedState.sessionId }
if ($ResumeSession -and $ResumeSession -notmatch '^[0-9a-fA-F-]{36}$') { throw 'Invalid session ID.' }

$terminals = (Invoke-Orca -Arguments @('terminal', 'list')).result.terminals
$existing = $null
if (!$NewConversation -and $savedState -and $savedState.sessionId -eq $ResumeSession) {
    $existing = $terminals | Where-Object { $_.tabId -eq $savedState.tabId -and $_.agentIdentity -eq $Agent -and $_.connected } | Select-Object -First 1
}
if (!$existing) {
    $agentCommand = switch ($Agent) {
        'codex' { 'codex' }
        'claude' { 'claude' }
        'antigravity' { Join-Path $env:LOCALAPPDATA 'agy\bin\agy.exe' }
    }
    if ($NewConversation) {
        $ResumeSession = ''
    } elseif ($ResumeSession) {
        $resumeFlag = switch ($Agent) { 'codex' { 'resume' }; 'claude' { '--resume' }; 'antigravity' { '--conversation' } }
        $agentCommand += " $resumeFlag $ResumeSession"
    } elseif ($savedState) {
        $agentCommand += $(if ($Agent -eq 'codex') { ' resume --last' } else { ' --continue' })
    } else {
        Write-Host "First launch for $Agent. Opening a new conversation; future launches will reuse this tab or continue its latest conversation."
    }
    $worktreeSelector = 'id:' + $workspaceRepo.id + '::' + $workspaceRepo.path
    $existing = (Invoke-Orca -Arguments @('terminal', 'create', '--worktree', $worktreeSelector, '--title', "AI OS - $Agent", '--command', $agentCommand)).result.terminal
    $ready = Invoke-Orca -Arguments @('terminal', 'wait', '--terminal', $existing.handle, '--for', 'tui-idle', '--timeout-ms', '30000') -AllowFailure
    if (!$ready -or !$ready.result.wait.satisfied) {
        Write-Warning 'The resume tab was created but readiness is not yet confirmed. No prompt was sent and no second tab was created.'
    }
}

$null = Invoke-Orca -Arguments @('terminal', 'switch', '--terminal', $existing.handle)
$stateDirectory = Split-Path $statePath -Parent
$null = New-Item -ItemType Directory -Path $stateDirectory -Force
@{ agent = $Agent; sessionId = $ResumeSession; tabId = $existing.tabId; workspacePath = $WorkspacePath } | ConvertTo-Json | Set-Content -LiteralPath $statePath -Encoding UTF8
Write-Host "Selected $Agent in Orca. Session: $ResumeSession"
