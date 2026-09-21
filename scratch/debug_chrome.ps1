$chromeExe = "C:\Program Files\Google\Chrome\Application\chrome.exe"
$profileDir = "$env:LOCALAPPDATA\LSATU-Agent-Chrome"
& $chromeExe --remote-debugging-port=9222 --remote-debugging-address=127.0.0.1 --user-data-dir="$profileDir" --no-first-run --no-default-browser-check --enable-logging=stderr --v=1 "https://lsatprep.study" 2>&1 | Select-Object -First 30
