import os
import sys
import json
import glob
import subprocess

def inspect_subagents():
    print("=== Subagents in .gemini/agents ===")
    agents_dir = r"C:\Users\Joshu\dev\ai-os\.gemini\agents"
    if os.path.exists(agents_dir):
        files = glob.glob(os.path.join(agents_dir, "*.toml"))
        print(f"Total TOML files: {len(files)}")
        for f in sorted(files):
            size = os.path.getsize(f)
            with open(f, 'r', encoding='utf-8', errors='ignore') as fh:
                lines = [line.strip() for line in fh if line.strip() and not line.startswith('#')]
            print(f"- {os.path.basename(f)} ({size} bytes): {lines[:3]}")
    else:
        print("Directory does not exist:", agents_dir)

def inspect_processes():
    print("\n=== Active Relevant Processes via PowerShell ===")
    ps_script = """
    Get-CimInstance Win32_Process | Where-Object { 
        $_.Name -match 'chrome|node|python|antigravity' -or $_.CommandLine -match '9223|8080|vite|devtools' 
    } | Select-Object ProcessId, Name, @{Name='WS_MB';Expression={[math]::Round($_.WorkingSetSize/1MB,1)}}, CommandLine | Format-Table -AutoSize
    """
    res = subprocess.run(["powershell", "-NoProfile", "-Command", ps_script], capture_output=True, text=True)
    print(res.stdout)

def inspect_disk_usage():
    print("\n=== Disk Usage of Key Directories ===")
    dirs_to_check = [
        r"C:\Users\Joshu\.gemini",
        r"C:\Users\Joshu\dev\ai-os\.gemini",
        r"C:\Users\Joshu\dev\ai-os\projects\lsatu",
        r"C:\Users\Joshu\dev\ai-os\.agents",
        r"C:\Users\Joshu\dev\ai-os\.claude",
    ]
    for d in dirs_to_check:
        if os.path.exists(d):
            total_size = 0
            file_count = 0
            for root, _, files in os.walk(d):
                for f in files:
                    fp = os.path.join(root, f)
                    try:
                        total_size += os.path.getsize(fp)
                        file_count += 1
                    except OSError:
                        pass
            print(f"{d}: {file_count} files, {total_size / (1024*1024):.2f} MB")
        else:
            print(f"{d}: NOT FOUND")

if __name__ == "__main__":
    inspect_subagents()
    inspect_processes()
    inspect_disk_usage()
