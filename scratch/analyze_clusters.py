import os
import json

clusters = {
    "review": ["code-review", "codex-review", "review", "requesting-code-review", "receiving-code-review"],
    "debugging": ["systematic-debugging", "diagnosing-bugs", "a11y-debugging", "memory-leak-debugging", "troubleshooting"],
    "tdd": ["tdd", "test-driven-development"],
    "implement": ["subagent-driven-development", "executing-plans", "writing-plans"],
    "handoff": ["session-handoff", "session-handoff-nate", "session-handoff-nate-active-copy", "lsatu-cc-handoff", "wrapup", "pickup"],
    "skill_creator": ["skill-creator", "skill-development", "writing-skills", "skill-repair", "skill-doctor", "skill-lint"],
    "research": ["research", "research-deep", "research-report", "research-add-items"],
    "frontend_design": ["frontend-design", "design-taste-frontend", "high-end-visual-design", "minimalist-ui", "redesign-existing-projects", "emil-design-eng"],
    "browser": ["auto-auth-browser", "edge-live-control", "lsat-u-browser-verification", "webapp-testing", "chrome-devtools"],
    "grilling": ["grill-me", "grill-me-codex", "grill-with-docs", "grill-with-docs-codex"],
    "bootcamp": ["bootcamp-builder", "bootcamp-parity-audit"],
    "mcp": ["mcp-builder", "build-mcp-app", "build-mcp-server", "build-mcpb", "mcp-integration"]
}

base_dir = r"C:\Users\Joshu\dev\ai-os\.gemini\skills"

print("=== Overlap / Duplicate Skill Cluster Analysis ===")
for cluster_name, skills in clusters.items():
    print(f"\n--- Cluster: {cluster_name} ---")
    for s in skills:
        # check direct or in subfolders
        found_paths = []
        for root, dirs, files in os.walk(base_dir):
            if os.path.basename(root) == s and "SKILL.md" in files:
                found_paths.append(os.path.join(root, "SKILL.md"))
        
        # also check config / builtin
        for extra in [r"C:\Users\Joshu\.gemini\config\skills", r"C:\Users\Joshu\.gemini\antigravity\builtin\skills"]:
            p = os.path.join(extra, s, "SKILL.md")
            if os.path.exists(p):
                found_paths.append(p)
                
        if found_paths:
            sizes = [os.path.getsize(p) for p in found_paths]
            print(f"  * {s}: found at {len(found_paths)} path(s), sizes: {sizes}")
            for p in found_paths:
                rel = os.path.relpath(p, r"C:\Users\Joshu")
                print(f"      -> {rel}")
        else:
            print(f"  * {s}: NOT FOUND in .gemini/skills")
