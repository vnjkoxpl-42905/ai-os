"""Write the skill-listing settings for AI OS sessions into .claude/settings.json.

Why (measured 2026-10-12): Claude Code gives skill descriptions 1% of the context window
(30,000 chars here) and fills it by recent usage, then listing order. 403 skills wanted
126,322 chars, so most of Joshua's own operational skills were listed by name only and could
not trigger on their own.

Rules (reversible; every skill stays installed and stays invocable as /name):
  hide       -> "user-invocable-only": generic vendor packs never used in 669 sessions
                (Workspace recipes and personas, team/enterprise Workspace admin, Anthropic
                brand and Slack GIF tools).
  name-only  -> listed without description: skills never used and not in Joshua's working set.
  everything else (core operations + anything ever used) keeps its description, and the
  budget fraction rises to 0.015 so all of them fit.

Edit CORE or KEEP below, then rerun:  python audits/skills-2026-10-12-karpathy/listing_overrides.py
"""
import json
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
SETTINGS = VAULT / ".claude" / "settings.json"
FRACTION = 0.015

VENDOR_PERSONAS = ["persona-content-creator", "persona-customer-support", "persona-event-coordinator",
                   "persona-exec-assistant", "persona-hr-coordinator", "persona-it-admin",
                   "persona-project-manager", "persona-researcher", "persona-sales-ops", "persona-team-lead"]
ENTERPRISE_GWS = ["gws-admin-reports", "gws-chat", "gws-chat-send", "gws-classroom", "gws-events",
                  "gws-events-renew", "gws-events-subscribe", "gws-keep", "gws-modelarmor",
                  "gws-modelarmor-create-template", "gws-modelarmor-sanitize-prompt",
                  "gws-modelarmor-sanitize-response", "gws-script", "gws-script-push",
                  "gws-workflow-file-announce", "gws-workflow-standup-report"]
OTHER_HIDDEN = ["brand-guidelines", "slack-gif-creator"]
# Never used, outside the working set: listed by name only (still invocable by name).
NAME_ONLY = json.loads((HERE / "name-only.json").read_text(encoding="utf-8"))
# Sub-skills reached through a router that stays described, per the vendor's own design:
# expo-overview says to load it first for every Expo/EAS task and route from there.
ROUTERS = {"expo-overview": ("expo-", "eas-")}


def main():
    installed = {p.parent.name for root in (Path.home() / ".claude/skills", VAULT / ".claude/skills")
                 for p in root.glob("*/SKILL.md")}
    recipes = sorted(n for n in installed if n.startswith("recipe-"))
    hidden = sorted(set(recipes + VENDOR_PERSONAS + ENTERPRISE_GWS + OTHER_HIDDEN))
    overrides = {n: "user-invocable-only" for n in hidden}
    overrides.update({n: "name-only" for n in NAME_ONLY if n not in overrides})
    for router, prefixes in ROUTERS.items():
        if router in installed:
            overrides.update({n: "name-only" for n in installed
                              if n.startswith(prefixes) and n != router and n not in overrides})
    missing = sorted(n for n in overrides if n not in installed)
    raw = SETTINGS.read_bytes().decode("utf-8")
    newline = "\r\n" if "\r\n" in raw else "\n"
    data = json.loads(raw)
    data["skillListingBudgetFraction"] = FRACTION
    data["skillOverrides"] = dict(sorted(overrides.items()))
    text = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
    SETTINGS.write_bytes(text.replace("\n", newline).encode("utf-8"))
    print(f"wrote {SETTINGS}: fraction {FRACTION}, {len(hidden)} hidden, "
          f"{sum(v == 'name-only' for v in overrides.values())} name-only; not installed here: {missing or 'none'}")


if __name__ == "__main__":
    main()
