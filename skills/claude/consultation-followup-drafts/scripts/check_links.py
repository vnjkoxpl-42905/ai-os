"""Price-to-link check for consultation follow-up drafts. Read-only; never sends or writes.

Reads the price/link pairs from wiki/CONSULTATION-FOLLOW-UP-TEMPLATE.md (one tier per fenced block),
checks every link in the chosen tier is well formed and not a placeholder, and, when --draft is given,
checks the draft carries exactly that tier's prices with exactly those links.

usage: python check_links.py [--tier standard|higher] [--draft draft.txt] [--live] [--template PATH]
exit 0 = pass (warnings allowed), 1 = fail. --live also requests each Cal.com link and fails on 404/410 or no response;
Stripe Payment Links answer 200 for any id, so their liveness and amounts need the Stripe dashboard or API.
"""
import argparse
import re
import sys
import urllib.request
from collections import Counter
from pathlib import Path

DEFAULT_TEMPLATE = Path("C:/Users/Joshu/dev/ai-os/wiki/CONSULTATION-FOLLOW-UP-TEMPLATE.md")
TIERS = {"standard": {45, 40, 35}, "higher": {60, 55, 50}}
PRICE = re.compile(r"\$(\d{2,3})\b")
URL = re.compile(r"https?://\S+")
PLACEHOLDER = re.compile(r"[{}<>\[\]]|xxx|todo|tbd|placeholder|example|\.\.\.", re.I)
STRIPE = re.compile(r"^https://buy\.stripe\.com/([A-Za-z0-9]{14,40})$")
CAL = re.compile(r"^https://cal\.com/joshua-jtx5ud/[a-z0-9-]+$")


def pairs(text):
    """Pair each price with the first payment/booking URL after it, before the next price."""
    out, pending = [], None
    for line in text.splitlines():
        p = PRICE.search(line)
        if p:
            pending = int(p.group(1))
        for u in URL.findall(line):
            u = u.rstrip(".,;)")
            if pending is not None and ("stripe.com" in u or "cal.com" in u or PLACEHOLDER.search(u)):
                out.append((pending, u))
                pending = None
    return out


def tier_blocks(md):
    blocks = re.findall(r"```[a-z]*\n(.*?)```", md, re.S)
    found = {}
    for b in blocks:
        ps = pairs(b)
        prices = {p for p, _ in ps}
        for name, want in TIERS.items():
            if want <= prices:
                found[name] = [(p, u) for p, u in ps if p in want]
    return found


def check_link(u, errors, warnings):
    if PLACEHOLDER.search(u):
        errors.append(f"placeholder link: {u}")
    elif not (STRIPE.match(u) or CAL.match(u)):
        errors.append(f"malformed or unexpected link: {u}")


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--tier", default="standard", choices=sorted(TIERS))
    ap.add_argument("--draft")
    ap.add_argument("--live", action="store_true")
    ap.add_argument("--template", default=str(DEFAULT_TEMPLATE))
    a = ap.parse_args(argv)
    tier, template = a.tier, Path(a.template)
    errors, warnings = [], []
    blocks = tier_blocks(template.read_text(encoding="utf-8"))
    if tier not in blocks:
        print(f"FAIL: tier '{tier}' not found in {template}")
        return 1
    tpl = blocks[tier]
    prices = [p for p, _ in tpl]
    if sorted(prices) != sorted(TIERS[tier]):
        errors.append(f"template tier {tier}: expected one link per price {sorted(TIERS[tier])}, got {prices}")
    links = [u for _, u in tpl]
    if len(set(links)) != len(links):
        errors.append(f"template tier {tier}: the same link is used for two prices")
    for _, u in tpl:
        check_link(u, errors, warnings)
    # Stripe ids in this account share a length; an odd one out may be truncated.
    all_ids = [m.group(1) for b in blocks.values() for _, u in b if (m := STRIPE.match(u))]
    common = Counter(len(i) for i in all_ids).most_common(1)
    for p, u in tpl:
        m = STRIPE.match(u)
        if m and common and len(m.group(1)) != common[0][0]:
            warnings.append(f"${p}: Stripe id is {len(m.group(1))} chars, others are {common[0][0]}; "
                            f"confirm in Stripe that {u} is live and charges ${p}")
    if a.draft:
        draft = pairs(Path(a.draft).read_text(encoding="utf-8"))
        for _, u in draft:
            check_link(u, errors, warnings)
        if sorted(draft) != sorted(tpl):
            errors.append(f"draft pairs {sorted(draft)} do not match template tier {tier} {sorted(tpl)}")
    if a.live:
        for p, u in tpl:
            if CAL.match(u):
                try:
                    code = urllib.request.urlopen(urllib.request.Request(u, method="GET", headers={"User-Agent": "Mozilla/5.0"}), timeout=20).status
                except urllib.error.HTTPError as e:
                    code = e.code
                except Exception as e:  # network failure is a failed check, not a pass
                    code = f"unreachable ({e.__class__.__name__})"
                if code in (404, 410) or isinstance(code, str):
                    errors.append(f"${p}: {u} returned {code}")
                elif code != 200:
                    warnings.append(f"${p}: {u} returned {code}; open it in a browser to confirm")
    for p, u in tpl:
        print(f"  ${p:<4} {u}")
    for w in warnings:
        print(f"WARN: {w}")
    for e in errors:
        print(f"FAIL: {e}")
    print(f"{'FAIL' if errors else 'PASS'}: tier {tier}, {len(tpl)} price/link pairs"
          + (", draft matched" if a.draft and not errors else ""))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
