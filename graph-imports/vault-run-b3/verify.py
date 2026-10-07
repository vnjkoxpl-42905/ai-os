"""Independent post-build verification of a graphify vault.

Written because batch 3 shipped a defect that every in-band check missed: an
extraction agent reported "48 of 48 files read, every file contributed a node"
while an entire skill had produced nothing. The merge coverage pass caught it
only because it recomputed coverage from the artifacts instead of believing the
report.

The rule this file encodes: never verify a graph using a number that the thing
being verified supplied. Everything below is recomputed from files on disk.

Exit code is non-zero if any FAIL fires, so this can gate a rebuild.
"""
import json
import os
import re
import sys
from collections import Counter
from pathlib import Path

import networkx as nx

RUN = Path(__file__).resolve().parent
OUT = RUN / "graphify-out"
VAULT = RUN.parent / "vault-b3"
SKILLS_ROOT = Path("/Users/joshuaf/ai-os")

results = []


def check(name, ok, detail="", fatal=True):
    results.append((name, ok, detail, fatal))
    flag = "PASS" if ok else ("FAIL" if fatal else "WARN")
    print(f"[{flag}] {name}" + (f" — {detail}" if detail else ""))
    return ok


def main():
    extraction = json.loads((OUT / ".graphify_extract.json").read_text())
    corpus = json.loads((OUT / ".b3_corpus.json").read_text())
    nodes = extraction["nodes"]
    edges = extraction["edges"]

    # --- graph structure ------------------------------------------------------
    G = nx.Graph()
    G.add_nodes_from(n["id"] for n in nodes)
    G.add_edges_from((e["source"], e["target"]) for e in edges)
    ncomp = nx.number_connected_components(G)
    check("graph is one connected component", ncomp == 1, f"{ncomp} component(s)")

    ids = [n["id"] for n in nodes]
    dupe_ids = [i for i, c in Counter(ids).items() if c > 1]
    check("no duplicate node ids", not dupe_ids, f"{len(dupe_ids)} dupes")

    valid = set(ids)
    dangling = [(e["source"], e["target"]) for e in edges
                if e["source"] not in valid or e["target"] not in valid]
    check("no dangling edges", not dangling, f"{len(dangling)} dangling")

    self_loops = [e for e in edges if e["source"] == e["target"]]
    check("no self-loops", not self_loops, f"{len(self_loops)}")

    # --- label hygiene --------------------------------------------------------
    labels = [n.get("label", n["id"]) for n in nodes]
    dupe_labels = [l for l, c in Counter(labels).items() if c > 1]
    check("no exact duplicate labels", not dupe_labels,
          f"{len(dupe_labels)}: {dupe_labels[:5]}")

    STOP = {"a", "an", "the", "of", "to", "for", "and", "or", "in", "on",
            "before", "after", "not", "is", "by", "with", "as", "at"}

    def tok(l):
        return " ".join(sorted(w for w in re.sub(r"[^a-z0-9 ]", " ", l.lower()).split()
                               if w and w not in STOP))

    fuzzy = Counter(tok(l) for l in labels)
    fuzzy_dupes = [k for k, c in fuzzy.items() if c > 1 and k]
    check("no word-order duplicate labels", not fuzzy_dupes,
          f"{len(fuzzy_dupes)}: {fuzzy_dupes[:3]}")

    # A label that sanitizes to a leading dot becomes a hidden file that Obsidian
    # will not display. Batch 3 shipped one of these.
    def safe_name(label):
        c = re.sub(r'[\\/*?:"<>|#^\[\]]', "", label.replace("\n", " ")).strip()
        return re.sub(r"\.(md|mdx|markdown)$", "", c, flags=re.I) or "unnamed"

    # Non-fatal: the dotted label is correct — it names a real file — so the fix
    # belongs in fix_vault_names.py after export, not in the label. The fatal
    # guard is "no hidden note files in vault" below, which checks the outcome
    # rather than the cause.
    hidden = [l for l in labels if safe_name(l).startswith(".")]
    check("no label sanitizes to a hidden dotfile", not hidden,
          f"{len(hidden)} (handled by fix_vault_names.py): {hidden}", fatal=False)

    # --- source coverage ------------------------------------------------------
    def norm(s):
        s = str(s).strip()
        for pre in ("/Users/joshuaf/ai-os/skills/", "skills/", "./"):
            if s.startswith(pre):
                return s[len(pre):]
        return s

    covered = set()
    unsourced_nodes = []
    for n in nodes:
        srcs = n.get("sources") or n.get("source_files") or []
        if not srcs and n.get("source_file"):
            srcs = [n["source_file"]]
        if not srcs:
            unsourced_nodes.append(n.get("label", n["id"]))
        for s in srcs:
            covered.add(norm(s))

    expected = {norm(p) for p in corpus}
    uncovered = expected - covered
    check("every corpus file produced a node",
          not uncovered, f"{len(uncovered)} uncovered: {sorted(uncovered)[:5]}")
    check("every node carries at least one source",
          not unsourced_nodes, f"{len(unsourced_nodes)}: {unsourced_nodes[:5]}")

    # Sources must point at files that actually exist — a hallucinated path is
    # worse than a missing one because it reads as provenance.
    ghost = sorted({s for s in covered if not (SKILLS_ROOT / "skills" / s).exists()})
    check("no source path points at a missing file", not ghost,
          f"{len(ghost)}: {ghost[:5]}")

    # --- vault files ----------------------------------------------------------
    if VAULT.exists():
        md = [f for f in os.listdir(VAULT) if f.endswith(".md")]
        comm = [f for f in md if f.startswith("_COMMUNITY_")]
        concept = [f for f in md if not f.startswith("_COMMUNITY_") and f != "INDEX.md"]
        check("vault concept-note count matches node count",
              len(concept) == len(nodes), f"{len(concept)} notes vs {len(nodes)} nodes")

        hidden_files = [f for f in os.listdir(VAULT)
                        if f.startswith(".") and f.endswith(".md")]
        check("no hidden note files in vault", not hidden_files, f"{hidden_files}")

        sourced = sum(1 for f in concept
                      if "## Source" in (VAULT / f).read_text(errors="replace"))
        check("every concept note has a Source section",
              sourced == len(concept), f"{sourced}/{len(concept)}")

        # Dangling wikilinks: a [[target]] with no matching note is a dead click.
        stems = {f[:-3] for f in md}
        dead = Counter()
        for f in md:
            for m in re.findall(r"\[\[([^\]|#]+)", (VAULT / f).read_text(errors="replace")):
                t = m.strip()
                # source links point outside the vault by design; only check
                # intra-vault concept links (those without a path separator)
                if "/" not in t and t not in stems:
                    dead[t] += 1
        check("no dangling intra-vault wikilinks", not dead,
              f"{len(dead)} targets, e.g. {list(dead)[:5]}", fatal=False)
        print(f"       vault: {len(md)} .md ({len(concept)} concept, "
              f"{len(comm)} community)")

    # --- evidence quality -----------------------------------------------------
    inferred = [e for e in edges if "INFERRED" in str(e.get("evidence", ""))]
    lowconf = [e for e in edges
               if isinstance(e.get("confidence"), (int, float)) and e["confidence"] < 0.65]
    noev = [e for e in edges if not str(e.get("evidence", "")).strip()]
    check("every edge carries evidence", not noev, f"{len(noev)} without", fatal=False)
    print(f"       {len(inferred)} INFERRED edges, {len(lowconf)} below 0.65 confidence")

    print()
    fails = [r for r in results if not r[1] and r[3]]
    warns = [r for r in results if not r[1] and not r[3]]
    print(f"{len(results) - len(fails) - len(warns)} passed, "
          f"{len(warns)} warnings, {len(fails)} failures")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
