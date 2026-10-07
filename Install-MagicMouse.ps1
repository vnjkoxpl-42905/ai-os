$tempDir = Join-Path $env:TEMP "MagicMouseDriver"
Write-Host "Installing Apple Magic Mouse Driver..."
pnputil.exe /add-driver "$tempDir\AppleWirelessMouse.inf" /install
Write-Host "Installation complete. Please toggle your mouse off and back on."
Pause
