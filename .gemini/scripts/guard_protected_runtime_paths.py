#!/usr/bin/env python3
"""
Codex / Claude Protected Runtime Path Guard for Antigravity (Jay 2).

Mechanically blocks Antigravity from mutating Codex-owned and Claude-owned
configuration files and directories, while preserving full read-only access.
Allows Antigravity full write access to Gemini-owned configurations and ordinary
application/workspace files.
"""

import os
import sys
import json
import re

# Canonical protected files (lower-case, normalized absolute paths)
PROTECTED_FILES = {
    r"c:\users\joshu\dev\ai-os\agents.md",
    r"c:\users\joshu\dev\ai-os\claude.md",
    r"c:\users\joshu\dev\ai-os\projects\lsatu\agents.md",
    r"c:\users\joshu\dev\ai-os\projects\lsatu\claude.md",
}

# Canonical protected directories (lower-case, normalized absolute paths without trailing slash)
PROTECTED_DIRS = [
    r"c:\users\joshu\dev\ai-os\.agents",
    r"c:\users\joshu\dev\ai-os\.codex",
    r"c:\users\joshu\dev\ai-os\.claude",
    r"c:\users\joshu\dev\ai-os\skills\codex",
    r"c:\users\joshu\dev\ai-os\skills\claude",
    r"c:\users\joshu\dev\ai-os\projects\lsatu\.agents",
    r"c:\users\joshu\dev\ai-os\projects\lsatu\.codex",
    r"c:\users\joshu\dev\ai-os\projects\lsatu\.claude",
]

# Sensitive tokens that indicate possible targeting in command lines
SENSITIVE_TOKENS = [
    "agents.md",
    "claude.md",
    ".agents",
    ".codex",
    ".claude",
    "skills/codex",
    "skills\\codex",
    "skills/claude",
    "skills\\claude",
]

# Mutating commands or operators in shell
MUTATING_COMMAND_PATTERNS = [
    # Redirections
    r">",
    r">>",
    # PowerShell file writing
    r"\bset-content\b",
    r"\bsc\b",
    r"\badd-content\b",
    r"\bac\b",
    r"\bout-file\b",
    r"\bnew-item\b",
    r"\bni\b",
    r"\bclear-content\b",
    r"\bexport-csv\b",
    r"\bexport-clixml\b",
    # Deletions / Removals
    r"\bremove-item\b",
    r"\bri\b",
    r"\bdel\b",
    r"\berase\b",
    r"\brmdir\b",
    r"\brd\b",
    r"\brm\b",
    # Moves / Renames
    r"\bmove-item\b",
    r"\bmi\b",
    r"\bmv\b",
    r"\bmove\b",
    r"\brename-item\b",
    r"\bren\b",
    r"\brename\b",
    # Copies overwriting
    r"\bcopy-item\b",
    r"\bcp\b",
    r"\bcopy\b",
    # Git mutating commands
    r"\bgit\s+checkout\b",
    r"\bgit\s+restore\b",
    r"\bgit\s+clean\b",
    r"\bgit\s+reset\b",
    r"\bgit\s+rm\b",
    r"\bgit\s+mv\b",
    # Other mutators
    r"\btruncate\b",
    r"\btee\b",
    r"\bsed\s+-i\b",
]

COMPILED_MUTATING_PATTERNS = [
    re.compile(pat, re.IGNORECASE) for pat in MUTATING_COMMAND_PATTERNS
]

def normalize_target_path(path_str, cwd=""):
    if not path_str:
        return ""
    p = str(path_str).strip().strip('\'"')
    if p.startswith("\\\\?\\"):
        p = p[4:]
    p = os.path.expanduser(p)
    p = os.path.expandvars(p)
    if not os.path.isabs(p):
        if cwd:
            p = os.path.join(cwd, p)
        else:
            p = os.path.abspath(p)
    p = os.path.normpath(p)
    return p.lower()

def is_path_protected(norm_path):
    if not norm_path:
        return False, None
    
    # Check exact files
    if norm_path in PROTECTED_FILES:
        return True, norm_path
        
    # Check protected directories and their descendants
    for pdir in PROTECTED_DIRS:
        if norm_path == pdir or norm_path.startswith(pdir + os.sep):
            return True, pdir
            
    return False, None

def evaluate_decision(payload):
    """
    Evaluates the hook payload and returns (decision, reason).
    """
    tool_call = payload.get("toolCall") or {}
    tool_name = tool_call.get("name", "")
    args = tool_call.get("args") or {}
    
    # 1. Direct file modification tools
    if tool_name in ("write_to_file", "replace_file_content", "edit_file", "create_file"):
        target_file = args.get("TargetFile") or args.get("path") or ""
        norm = normalize_target_path(target_file)
        protected, matched = is_path_protected(norm)
        if protected:
            return (
                "deny",
                f"BLOCKED by Codex/Claude Protection Guard: Attempted file mutation on protected path '{target_file}' (matches protected rule '{matched}'). Antigravity has read-only access to Codex/Claude runtime configurations. Explicit Joshua authorization is required for cross-runtime modifications."
            )
        return "allow", None
        
    # 2. Command execution tool: run_command, bash, shell
    if tool_name in ("run_command", "bash", "terminal", "execute_command"):
        cmd = args.get("CommandLine") or args.get("command") or ""
        cwd = args.get("Cwd") or args.get("cwd") or ""
        cmd_lower = cmd.lower()
        
        # Quick exit: if command does not mention any sensitive token or protected path, allow
        has_sensitive_token = any(tok in cmd_lower for tok in SENSITIVE_TOKENS)
        if not has_sensitive_token:
            return "allow", None
            
        # Check if command has mutating operators or keywords
        has_mutator = any(pat.search(cmd) for pat in COMPILED_MUTATING_PATTERNS)
        
        # In-place Python write check
        if "open(" in cmd_lower and any(m in cmd_lower for m in ["'w'", '"w"', "'a'", '"a"', "wb", "write"]):
            has_mutator = True
            
        if has_mutator:
            return (
                "deny",
                f"BLOCKED by Codex/Claude Protection Guard: Attempted shell mutation targeting protected runtime configuration: '{cmd}'. Antigravity has read-only access to Codex/Claude configuration. Explicit Joshua authorization is required for cross-runtime modifications."
            )
            
        # If it's a read-only command (e.g. Get-Content, git diff, Get-FileHash, grep), allow
        return "allow", None
        
    # Default: allow
    return "allow", None

def main():
    try:
        input_data = sys.stdin.read()
        if not input_data.strip():
            print(json.dumps({"decision": "allow"}))
            return
        payload = json.loads(input_data)
    except Exception:
        print(json.dumps({"decision": "allow"}))
        return

    decision, reason = evaluate_decision(payload)
    if decision == "deny":
        response = {
            "decision": "deny",
            "reason": reason
        }
    else:
        response = {
            "decision": "allow"
        }

    try:
        from datetime import datetime
        with open(r"C:\Users\Joshu\.gemini\config\scripts\guard_audit.log", "a", encoding="utf-8") as af:
            af.write(f"{datetime.now().isoformat()} [{__file__}] tool={payload.get('toolCall', {}).get('name')} decision={decision} args={str(payload.get('toolCall', {}).get('args'))[:100]}\n")
    except Exception:
        pass
        
    print(json.dumps(response))

if __name__ == "__main__":
    main()
