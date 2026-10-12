"""Model of Claude Code's skill listing budget, reconstructed from the installed binary (2026-10-12).

  budget = SLASH_COMMAND_TOOL_CHAR_BUDGET or floor(context_tokens * 4 * skillListingBudgetFraction[0.01])
  entry  = "- name: description" (description capped at skillListingMaxDescChars[1536]); name-only = "- name"
  If the full listing fits the budget, every description is shown. Otherwise bundled skills keep their
  descriptions, everything else is ranked by usageCount * max(0.5**(days/7), 0.1) and gets its
  description greedily while budget remains. disable-model-invocation and user-invocable-only skills
  are not listed at all.

usage: python budget.py [overrides.json]
"""
import json
import sys
import time
from pathlib import Path

import yaml

HOME = Path.home()
V = HOME / "dev" / "ai-os"
CAP = 1536


def load_root(root, prefix=""):
    out = {}
    for skf in sorted(root.glob("*/SKILL.md")):
        text = skf.read_text(encoding="utf-8", errors="replace").lstrip("﻿")
        if not text.startswith("---"):
            continue
        fm = yaml.safe_load(text.split("---", 2)[1]) or {}
        if fm.get("disable-model-invocation") is True or fm.get("user-invocable") is False and False:
            continue
        desc = str(fm.get("description") or "")
        if fm.get("when_to_use"):
            desc += " - " + str(fm["when_to_use"])
        out[prefix + skf.parent.name] = desc
    return out


user = load_root(HOME / ".claude/skills")
project = {k: v for k, v in load_root(V / ".claude/skills").items() if k not in user}
synced_dirs = list((HOME / ".claude/skills/synced").glob("*"))
synced = load_root(synced_dirs[0], "anthropic-skills:") if synced_dirs else {}
entries = list(user.items()) + list(project.items()) + list(synced.items())

usage = json.load(open(HOME / ".claude.json", encoding="utf-8"))["skillUsage"]
now = time.time() * 1000


def score(name):
    u = usage.get(name)
    if not u:
        return 0.0
    days = (now - u["lastUsedAt"]) / 86400000
    return u["usageCount"] * max(0.5 ** (days / 7), 0.1)


def simulate(entries, overrides, budget, fixed):
    """fixed = chars always consumed by bundled/plugin entries outside this model."""
    listed = [(n, d) for n, d in entries if overrides.get(n) not in ("user-invocable-only", "off")]
    full = sum(len(n) + 4 + min(len(d), CAP) for n, d in listed) + len(listed) + fixed
    if full <= budget:
        return {"mode": "fits", "listed": len(listed), "described": [n for n, _ in listed], "full": full}
    names_cost = sum(len(n) + 2 for n, _ in listed) + len(listed) + fixed
    remaining = budget - names_cost
    ranked = sorted(((n, d) for n, d in listed if overrides.get(n) != "name-only"),
                    key=lambda nd: -score(nd[0]))  # stable: ties keep listing order
    described = []
    for n, d in ranked:
        cost = min(len(d), CAP) + 2
        if cost <= remaining:
            remaining -= cost
            described.append(n)
    return {"mode": "priority", "listed": len(listed), "described": described, "full": full, "left": remaining}


if __name__ == "__main__":
    overrides = json.load(open(sys.argv[1])) if len(sys.argv) > 1 else {}
    budget = int(sys.argv[2]) if len(sys.argv) > 2 else 40000
    fixed = int(sys.argv[3]) if len(sys.argv) > 3 else 9000
    r = simulate(entries, overrides, budget, fixed)
    print(f"entries {len(entries)} (user {len(user)}, project-only {len(project)}, synced {len(synced)})")
    print(f"mode {r['mode']}  listed {r['listed']}  described {len(r['described'])}  full-listing chars {r['full']}")
    core = ("pickup wrapup session-handoff audit level-up consultation-inquiry-drafts consultation-followup-drafts "
            "inbound-tutoring-replies transcript-intake post-session-recap guided-drill-assignment "
            "lsat-u-platform-actions tutorocean-profile-fill prompt-architect-refiner accommodations-email "
            "assign-lsatu-work booking-link send-booking-link superwhisper bootcamp-builder lsat-u-voice "
            "lsat-lab-sync morning-brief pull-submissions ingest second-brain-query second-brain-lint").split()
    missing = [c for c in core if c not in r["described"]]
    print(f"core skills described {len(core) - len(missing)}/{len(core)}; missing: {' '.join(missing)}")
    json.dump(r, open("budget_out.json", "w"), indent=1)
