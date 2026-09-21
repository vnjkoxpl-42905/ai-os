import os
import difflib

p_agents = r"C:\Users\Joshu\dev\ai-os\AGENTS.md"
p_gemini = r"C:\Users\Joshu\dev\ai-os\GEMINI.md"
p_claude = r"C:\Users\Joshu\dev\ai-os\CLAUDE.md"

with open(p_agents, "r", encoding="utf-8", errors="ignore") as f:
    lines_agents = f.readlines()
with open(p_gemini, "r", encoding="utf-8", errors="ignore") as f:
    lines_gemini = f.readlines()
with open(p_claude, "r", encoding="utf-8", errors="ignore") as f:
    lines_claude = f.readlines()

print(f"Total lines: AGENTS.md={len(lines_agents)}, GEMINI.md={len(lines_gemini)}, CLAUDE.md={len(lines_claude)}")

# AGENTS vs CLAUDE
sm_ac = difflib.SequenceMatcher(None, lines_agents, lines_claude)
ratio_ac = sm_ac.ratio()
print(f"Similarity ratio (AGENTS vs CLAUDE): {ratio_ac:.3f} (Nearly 100% identical!)")

# AGENTS vs GEMINI
sm_ag = difflib.SequenceMatcher(None, lines_agents, lines_gemini)
ratio_ag = sm_ag.ratio()
print(f"Similarity ratio (AGENTS vs GEMINI): {ratio_ag:.3f}")

# GEMINI vs CLAUDE
sm_gc = difflib.SequenceMatcher(None, lines_gemini, lines_claude)
ratio_gc = sm_gc.ratio()
print(f"Similarity ratio (GEMINI vs CLAUDE): {ratio_gc:.3f}")

# Token estimation (chars / 4)
tok_agents = len("".join(lines_agents)) / 4
tok_gemini = len("".join(lines_gemini)) / 4
tok_claude = len("".join(lines_claude)) / 4

print(f"Estimated Tokens: AGENTS.md=~{tok_agents:.0f}, GEMINI.md=~{tok_gemini:.0f}, CLAUDE.md=~{tok_claude:.0f}")
print(f"Total tokens across all three files: ~{tok_agents + tok_gemini + tok_claude:.0f}")
print(f"Total tokens injected into Antigravity (AGENTS + GEMINI): ~{tok_agents + tok_gemini:.0f}")
