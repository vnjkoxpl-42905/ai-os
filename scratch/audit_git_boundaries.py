import os
import subprocess

targets = [
    r"C:\Users\Joshu\dev\ai-os",
    r"C:\Users\Joshu\dev\ai-os\.gemini",
    r"C:\Users\Joshu\dev\ai-os\.agents",
    r"C:\Users\Joshu\dev\ai-os\.claude",
    r"C:\Users\Joshu\dev\ai-os\.codex",
    r"C:\Users\Joshu\dev\ai-os\projects\lsatu",
    r"C:\Users\Joshu\.gemini",
    r"C:\Users\Joshu\Tools\LSATU-Agent"
]

print("=== Git Version Control Boundary Audit ===")
for t in targets:
    print(f"\nTarget: {t}")
    if not os.path.exists(t):
        print("  Status: PATH DOES NOT EXIST")
        continue
    
    # Check if target itself or parent is a git repo
    res_root = subprocess.run(["git", "-C", t, "rev-parse", "--show-toplevel"], capture_output=True, text=True)
    if res_root.returncode == 0:
        repo_root = res_root.stdout.strip()
        res_branch = subprocess.run(["git", "-C", t, "branch", "--show-current"], capture_output=True, text=True)
        branch = res_branch.stdout.strip()
        
        # Check if ignored
        res_ignore = subprocess.run(["git", "-C", repo_root, "check-ignore", t], capture_output=True, text=True)
        is_ignored = res_ignore.returncode == 0
        
        # Check tracking status of files in target relative to repo root
        rel_p = os.path.relpath(t, repo_root).replace("\\", "/")
        if rel_p == ".":
            status_desc = "Repository Root itself"
        elif is_ignored:
            status_desc = "Git IGNORED"
        else:
            # Check if tracked in index
            res_ls = subprocess.run(["git", "-C", repo_root, "ls-files", rel_p], capture_output=True, text=True)
            has_tracked = bool(res_ls.stdout.strip())
            # Check status
            res_st = subprocess.run(["git", "-C", repo_root, "status", "--porcelain", rel_p], capture_output=True, text=True)
            status_desc = f"Tracked files present: {has_tracked}, Status output: {res_st.stdout.strip()[:100]}"
            
        print(f"  Repo Root: {repo_root}")
        print(f"  Branch: {branch}")
        print(f"  Tracking: {status_desc}")
    else:
        print("  Git Status: NOT A GIT REPOSITORY (No .git found)")
