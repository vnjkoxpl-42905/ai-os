"""Summarize per-skill SkillSpector JSON reports into SUMMARY.md (run with python -I)."""
import json, sys, collections
from pathlib import Path
here = Path(__file__).resolve().parent
rows, errors = [], []
for label in ("home-claude", "vault-claude"):
    for f in sorted((here / label).glob("*.json")):
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
        except Exception as e:
            errors.append(f"{label}/{f.stem}: unreadable ({e})"); continue
        ra = d.get("risk_assessment", {}); iss = d.get("issues") or []
        ac = d.get("analysis_completeness") or {}
        rows.append(dict(label=label, skill=f.stem, score=ra.get("score"), sev=ra.get("severity"),
                         rec=ra.get("recommendation"), n=len(iss), status=ac.get("status"), issues=iss))
    have = {r["skill"] for r in rows if r["label"] == label}
    codes = here / label / "_exit-codes.txt"
    if codes.exists():
        for line in codes.read_text().splitlines():
            name = line.split(" rc=")[0]
            if name not in have:
                errors.append(f"{label}/{name}: no JSON report ({line}); see {label}/{name}.log")
order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}
out = ["# SkillSpector scan, 2026-10-14", "",
       "Static mode only (`skillspector scan --no-llm`, SkillSpector 2.12.0). Each skill scanned on its own; "
       "the recursive mode stops after 32 skills (partial first attempt kept in `first-attempt-recursive/`). "
       "Pattern and YARA matches, not verdicts: every HIGH or CRITICAL finding needs a human read before any action. "
       "No skill was removed or deactivated.", ""]
cnt = collections.Counter((r["label"], r["sev"]) for r in rows)
out += ["| Root | Scanned | CRITICAL | HIGH | MEDIUM | LOW |", "|---|---|---|---|---|---|"]
for label in ("home-claude", "vault-claude"):
    n = sum(1 for r in rows if r["label"] == label)
    out.append(f"| {label} | {n} | " + " | ".join(str(cnt[(label, s)]) for s in ("CRITICAL", "HIGH", "MEDIUM", "LOW")) + " |")
out += ["", "## Skills rated HIGH or CRITICAL (DO_NOT_INSTALL)", ""]
flagged = sorted((r for r in rows if r["sev"] in ("HIGH", "CRITICAL")), key=lambda r: (order[r["sev"]], -(r["score"] or 0), r["skill"], r["label"]))
for r in flagged:
    out.append(f"### {r['skill']} ({r['label']}): {r['sev']} {r['score']}/100, {r['n']} findings")
    top = sorted(r["issues"], key=lambda i: order.get(i.get("severity"), 9))
    hc = [i for i in top if i.get("severity") in ("CRITICAL", "HIGH")]
    for i in hc[:6]:
        loc = i.get("location") or {}
        out.append(f"- {i.get('severity')} {i.get('id')} {i.get('category')}: {i.get('pattern','')[:140]} "
                   f"(`{loc.get('file')}:{loc.get('start_line')}`)")
    if len(hc) > 6: out.append(f"- ... {len(hc) - 6} more HIGH/CRITICAL findings in the JSON")
    out.append("")
out += ["## All scores", "", "| Skill | Root | Severity | Score | Findings | Coverage |", "|---|---|---|---|---|---|"]
for r in sorted(rows, key=lambda r: (order.get(r["sev"], 9), -(r["score"] or 0), r["skill"])):
    out.append(f"| {r['skill']} | {r['label']} | {r['sev']} | {r['score']} | {r['n']} | {r['status']} |")
if errors:
    out += ["", "## Scan errors", ""] + [f"- {e}" for e in errors]
(here / "SUMMARY.md").write_text("\n".join(out) + "\n", encoding="utf-8")
print(f"rows={len(rows)} flagged={len(flagged)} errors={len(errors)}")
