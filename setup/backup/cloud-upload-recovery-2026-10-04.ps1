param(
    [Parameter(Mandatory=$true)][string[]]$Paths,
    [string]$FolderId = '16OHDPoLNxCPinaPatuYVZCkYljQNotSO',
    [string]$JournalDirectory = 'C:\Users\Joshu\laptop-recovery-2026-10-04\cloud-verification'
)
$ErrorActionPreference = 'Stop'
New-Item -ItemType Directory -Path $JournalDirectory -Force | Out-Null
foreach ($path in $Paths) {
    $file = Get-Item -LiteralPath $path
    $md5 = (Get-FileHash -LiteralPath $file.FullName -Algorithm MD5).Hash.ToLowerInvariant()
    $sha256 = (Get-FileHash -LiteralPath $file.FullName -Algorithm SHA256).Hash.ToLowerInvariant()
    $queryName = $file.Name.Replace("'", "\'")
    $listParams = @{q="'$FolderId' in parents and name = '$queryName' and trashed = false";fields='files(id,name,size,md5Checksum,webViewLink)';pageSize=100} | ConvertTo-Json -Compress
    $existingOutput = & gws drive files list --params $listParams
    if ($LASTEXITCODE -ne 0) { throw "Could not inspect existing cloud files for $($file.Name)" }
    $existing = ($existingOutput | Out-String | ConvertFrom-Json).files | Where-Object { $_.md5Checksum -eq $md5 -and [long]$_.size -eq $file.Length } | Select-Object -First 1
    if ($existing) {
        $remoteId = $existing.id
        Write-Output "Found matching upload: $($file.Name)"
    } else {
        $metadata = @{name=$file.Name;parents=@($FolderId)} | ConvertTo-Json -Compress
        Write-Output "Uploading $($file.Name): $($file.Length) bytes"
        $uploadOutput = & gws drive files create --json $metadata --upload $file.FullName --upload-content-type application/octet-stream --params '{"fields":"id,name,size,md5Checksum,webViewLink"}'
        if ($LASTEXITCODE -ne 0) { throw "Upload failed: $($file.Name). Rerun to check for a completed matching cloud copy." }
        $remoteId = ($uploadOutput | Out-String | ConvertFrom-Json).id
        if (-not $remoteId) { throw "Upload returned no file id: $($file.Name)" }
    }
    $getParams = @{fileId=$remoteId;fields='id,name,size,md5Checksum,webViewLink'} | ConvertTo-Json -Compress
    $verifyOutput = & gws drive files get --params $getParams
    if ($LASTEXITCODE -ne 0) { throw "Cloud verification failed: $($file.Name)" }
    $remote = $verifyOutput | Out-String | ConvertFrom-Json
    if ($remote.md5Checksum -ne $md5 -or [long]$remote.size -ne $file.Length) { throw "Cloud hash/size mismatch: $($file.Name)" }
    $record = [ordered]@{name=$file.Name;source=$file.FullName;size=$file.Length;md5=$md5;sha256=$sha256;driveId=$remote.id;webViewLink=$remote.webViewLink;verifiedAt=(Get-Date).ToString('o')}
    $record | ConvertTo-Json | Set-Content -LiteralPath (Join-Path $JournalDirectory ($file.Name + '.verified.json')) -Encoding utf8
    Write-Output "VERIFIED $($file.Name) ($($remote.id))"
}
