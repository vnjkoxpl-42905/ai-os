import os, glob, re

search_roots = [
    r"C:\Users\Joshu\.gemini",
    r"C:\Users\Joshu\AppData\Local\Programs\Antigravity IDE",
    r"C:\Users\Joshu\AppData\Local\Programs\antigravity",
    r"C:\Users\Joshu\.antigravity-ide"
]

print("=== Searching for agent.md references in text/doc/json files ===")
for root_dir in search_roots:
    if os.path.exists(root_dir):
        for root, dirs, files in os.walk(root_dir):
            for f in files:
                if f.endswith(('.md', '.json', '.txt', '.js', '.ts', '.py')):
                    full = os.path.join(root, f)
                    try:
                        with open(full, "r", encoding="utf-8", errors="ignore") as file:
                            content = file.read()
                            if "agent.md" in content or "custom agent" in content.lower() or "agents/" in content:
                                # find matches
                                matches = [line.strip() for line in content.splitlines() if "agent.md" in line or "custom agent" in line.lower()][:5]
                                if matches:
                                    print(f"\nIn {full}:")
                                    for m in matches:
                                        print("  ", m[:120])
                    except:
                        pass

