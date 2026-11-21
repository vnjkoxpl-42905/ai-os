param(
    [string]$Root = 'C:\Users\Joshu\laptop-recovery-2026-10-04',
    [string]$FolderId = '16OHDPoLNxCPinaPatuYVZCkYljQNotSO',
    [string[]]$RequiredCategories = @('runtime-final','second-brain','app-data','sqlite-live-raw','personal-files','extra-settings','additional-profile','codex-final-delta'),
    [string[]]$ExcludedArchiveCategories = @('development')
)
$ErrorActionPreference = 'Stop'
$journal = Join-Path $Root 'cloud-verification'
$allRecords = @(Get-ChildItem -LiteralPath $journal -Filter '*.verified.json' | ForEach-Object { Get-Content -LiteralPath $_.FullName -Raw | ConvertFrom-Json })
$excludedRecords = @($allRecords | Where-Object {
    $recordName = $_.name
    @($ExcludedArchiveCategories | Where-Object { $recordName -match ('^' + [regex]::Escape($_) + '\.7z(?:\.\d+)?$') }).Count -gt 0
})
$records = @($allRecords | Where-Object { $_.name -notin $excludedRecords.name })
if (-not $records.Count) { throw 'No verified uploads found.' }
$sourceHashes = @{}
$hashManifests = @()
if (Test-Path -LiteralPath (Join-Path $Root 'SHA256SUMS.txt')) { $hashManifests += Join-Path $Root 'SHA256SUMS.txt' }
$hashManifests += @(Get-ChildItem -LiteralPath (Join-Path $Root 'archives') -Filter '*.SHA256SUMS' | Select-Object -ExpandProperty FullName)
foreach ($hashManifest in $hashManifests) {
    foreach ($line in Get-Content -LiteralPath $hashManifest) {
        if ($line -match '^\s*([a-fA-F0-9]{64})\s+\*?(.+?)\s*$') { $sourceHashes[[IO.Path]::GetFileName($Matches[2])] = $Matches[1].ToLowerInvariant() }
    }
}
$remoteFiles = [Collections.Generic.List[object]]::new()
$pageToken = $null
do {
    $params = @{q="'$FolderId' in parents and trashed = false";fields='nextPageToken,files(id,name,size,md5Checksum)';pageSize=100}
    if ($pageToken) { $params.pageToken = $pageToken }
    $output = & gws drive files list --params ($params | ConvertTo-Json -Compress)
    if ($LASTEXITCODE -ne 0) { throw 'Could not independently verify cloud contents.' }
    $page = $output | Out-String | ConvertFrom-Json
    foreach ($remote in $page.files) { $remoteFiles.Add($remote) }
    $pageToken = $page.nextPageToken
} while ($pageToken)
foreach ($record in $records) {
    if ($sourceHashes.ContainsKey($record.name) -and $sourceHashes[$record.name] -ne $record.sha256) { throw "Final tested archive changed after its upload: $($record.name)" }
    $remote = $remoteFiles | Where-Object id -EQ $record.driveId | Select-Object -First 1
    if (-not $remote -or $remote.md5Checksum -ne $record.md5 -or [long]$remote.size -ne [long]$record.size) { throw "Cloud copy absent or changed: $($record.name)" }
}
$categories = foreach ($category in $RequiredCategories) {
    $parts = @(Get-ChildItem -LiteralPath (Join-Path $Root 'archives') -Filter ($category + '.7z.*') | Where-Object Name -Match '\.\d+$' | Sort-Object Name)
    if (-not $parts.Count) { throw "Missing archive category: $category" }
    if ($category -eq 'development' -and -not $sourceHashes.ContainsKey($parts[0].Name)) { throw 'Development archive has not finished its test/hash manifest.' }
    for ($index=0; $index -lt $parts.Count; $index++) {
        $expectedName = '{0}.7z.{1:000}' -f $category,($index + 1)
        if ($parts[$index].Name -ne $expectedName) { throw "Missing numbered volume: $expectedName" }
        if (-not $sourceHashes.ContainsKey($expectedName)) { throw "Final tested source SHA256 missing: $expectedName" }
        $record = $records | Where-Object name -EQ $expectedName | Select-Object -First 1
        if (-not $record -or [long]$record.size -ne $parts[$index].Length) { throw "Archive volume not verified online: $expectedName" }
    }
    [ordered]@{category=$category;parts=$parts.Count;bytes=($parts | Measure-Object Length -Sum).Sum}
}
$manifestPath = Join-Path $Root 'CLOUD-VERIFIED-SHA256SUMS.txt'
$reportPath = Join-Path $Root 'CLOUD-VERIFICATION.json'
if ((Test-Path -LiteralPath $manifestPath) -or (Test-Path -LiteralPath $reportPath)) { throw 'Final report already exists. Preserve it and use a new output name for a later verification.' }
$records | Sort-Object name | ForEach-Object { "$($_.sha256)  $($_.name)" } | Set-Content -LiteralPath $manifestPath -Encoding utf8
$report = [ordered]@{
    status='All required archive volumes verified in Google Drive by MD5 and byte length'
    verifiedAt=(Get-Date).ToString('o')
    driveFolder="https://drive.google.com/drive/folders/$FolderId"
    categories=@($categories)
    scope='Second brain, Codex/Claude information, Downloads and Superwhisper. Unrelated development projects were removed from the required scope by Joshua.'
    excludedArchives=@($excludedRecords | Sort-Object name | Select-Object name,size,driveId)
    excludedArchiveNote='Partially uploaded development archive volumes are retained in Drive but excluded from the restore manifest. They are not a complete, restorable project backup.'
    files=@($records | Sort-Object name | Select-Object name,size,md5,sha256,driveId,webViewLink,verifiedAt)
    limitations='File/data backup, not a bootable Windows image. See restore guide and known issues for app installation, sign-ins, path repair, Superwhisper database integrity, and OneDrive Personal Vault coverage.'
}
$report | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $reportPath -Encoding utf8
Write-Output "All $($records.Count) saved files independently verified in Google Drive. Final manifest and report generated."
