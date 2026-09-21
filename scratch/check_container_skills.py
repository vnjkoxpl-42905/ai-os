import os

p = r"C:\Users\Joshu\dev\ai-os\.gemini\skills"
for container in ["_inactive", "_project-forks"]:
    cp = os.path.join(p, container)
    print(f"=== {container} ===")
    for root, dirs, files in os.walk(cp):
        if "SKILL.md" in files:
            print(f"- {os.path.relpath(root, cp)}")
