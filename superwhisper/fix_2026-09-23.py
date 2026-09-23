"""2026-09-23: remove replacement rules that fire INSIDE other words, and add what the
1,369-recording scan turned up.

Superwhisper replacements are plain substring matches with no word boundaries, so the bare
acronym pins added on 2026-09-12 were mangling ordinary words: "click" -> "CLIck" (48 times),
"you install" -> "yoUInstall", "per capita" -> "per cAPIta". `firecraw` -> Firecrawl was also
matching inside "firecrawl" itself and producing "Firecrawll". Sonnet 5 handles casing through
the mode glossary, so these rows are deleted rather than reworked.
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
D = "2026-09-23"

# heard sides to delete: substrings that appear inside ordinary English words
KILL = {
    # bare acronyms and two/three-letter pins
    "cli", "c l i", "api", "a p i", "mcp", "m c p", "u i", "ui", "url", "u r l", "ai", "a i",
    "pr", "prs", "ci", "ux", "pdf", "html", "css", "sql", "s q l", "json", "rls", "rpc",
    "llm", "llms", "jwt", "oauth", "rrc", "r r c", "pt", "lr", "rc",
    # self-matching Firecrawl / Superwhisper chains
    "firecraw", "superwhispere", "superwhispero",
    # fragments of longer words
    "fernand", "codec", "vercel", "react", "stripe", "gemini", "kling", "obsidian",
    "markdown", "readme", "postgres", "tailwind", "anthropic", "github", "gmail",
    "chatgpt", "openai", "open ai", "typescript", "lsat", "lsat demon", "grill with doc",
    "aspiring attorney", "aspiring attorneys", "md file", "sage", "seven",
}

kept, dropped = [], []
for line in open("replacements.md", encoding="utf-8").read().splitlines():
    if line.startswith("| ") and not line.startswith("| Heard") and not line.startswith("|---"):
        heard = line.split("|")[1].strip().lower()
        if heard in KILL:
            dropped.append(heard)
            continue
    kept.append(line)

# additions the scan justified: real mis-hearings, none of them ordinary English
ADD = [
    # Firecrawl tails the old `firecraw` rule created, plus fresh ones
    ("firecrawlls", "Firecrawl"), ("firecrawlli", "Firecrawl"), ("firecowl", "Firecrawl"),
    ("firecowls", "Firecrawl"), ("firecroll", "Firecrawl"), ("firecrull", "Firecrawl"),
    ("firecaw", "Firecrawl"), ("firecrawln", "Firecrawl"), ("firecrawlll", "Firecrawl"),
    # Claude Code tails
    ("claudecode", "Claude Code"), ("claudeco", "Claude Code"), ("claude coyce", "Claude Code"),
    ("chatclaude code", "Claude Code"), ("cloud codes", "Claude Code"),
    # Superwhisper
    ("superwhishper", "Superwhisper"), ("superwhusperer", "Superwhisper"),
    ("superwhiskersco", "Superwhisper"), ("superwhispers", "Superwhisper"),
    # Codex / models
    ("coex", "Codex"), ("codex6", "Codex"), ("gbt-6", "GPT-6"), ("gbt 6", "GPT-6"),
    ("gpt-6 astra", "GPT-6 Astra"), ("gpt-6 luna", "GPT-6 Luna"), ("gpt-6 sol", "GPT-6 Sol"),
    ("gbt-6astra", "GPT-6 Astra"), ("claude sonic", "Claude Sonnet"), ("claud opus", "Claude Opus"),
    # tools he started using since the last scan
    ("anti-gravity", "Antigravity"), ("anti gravity", "Antigravity"), ("antigravity", "Antigravity"),
    ("ai os", "AI OS"), ("aios", "AI OS"), ("a i o s", "AI OS"),
    ("microsoft edge", "Microsoft Edge"), ("figma", "Figma"), ("lovable cloud", "Lovable Cloud"),
    # people the scan surfaced
    ("kelsey regis", "Kelsey Regis"), ("regis", "Regis"), ("althea", "Althea"),
    ("cameron", "Cameron"), ("cameron's", "Cameron's"),
    # LSAT U / vault
    ("lsat-u", "LSAT U"), ("lsat u is", "LSAT U is"), ("lsat uis", "LSAT U is"),
    ("lsatprep.studys", "lsatprep.study"), ("post recap skill", "/session-recap"),
    ("postrecap skill", "/session-recap"), ("session recap skill", "/session-recap"),
    ("seven sager", "7Sager"), ("7sager", "7Sager"),
    # email tails the scan found
    ("joshua.fissiah01@jameel.com", "joshua.fisseha01@gmail.com"),
    ("joshua.fissiah01@jimail.com", "joshua.fisseha01@gmail.com"),
    ("joshua.fissier01@jml.com", "joshua.fisseha01@gmail.com"),
    ("joshua fissier", "Joshua Fisseha"), ("fissier", "Fisseha"),
    ("yohunatan", "Yahunatan"), ("suprabase", "Supabase"), ("lovible", "Lovable"),
]

existing = {l.split("|")[1].strip().lower() for l in kept if l.startswith("| ")}
new = [f"| {h} | {w} | {D} | scan 2026-09-23 |" for h, w in ADD
       if h.lower() not in existing and h.lower() not in KILL]

open("replacements.md", "w", encoding="utf-8").write("\n".join(kept + new) + "\n")
print(f"dropped {len(dropped)} unsafe rules, added {len(new)}")
print("dropped:", ", ".join(sorted(set(dropped))))
