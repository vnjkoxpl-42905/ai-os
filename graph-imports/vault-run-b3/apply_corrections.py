"""Apply reviewed edge corrections and re-check the ship gate.

Extraction agents write confident-sounding edges that are sometimes category
errors. Two survived batch 3's merge: one pairing an identity-model trainer with
a frozen plan spec, one hanging an LSAT drill workflow off the TDD cycle. Both
were found by reading the low-confidence tail, and in both cases the agent's own
evidence field already conceded the problem — the signal was there, nobody had
looked.

Guard rails:
  * A `drop` whose source or target would fall to degree 0 is refused. Removing
    a node's only edge orphans it and silently breaks the one-component gate,
    which is the whole health signal.
  * Every target id is validated before use, so a typo in corrections.json
    fails loudly instead of silently doing nothing.
  * Idempotent: re-running finds the edges already corrected and reports zero.
"""
import json
import sys
from pathlib import Path

import networkx as nx

RUN = Path(__file__).resolve().parent
OUT = RUN / "graphify-out"
EXTRACT = OUT / ".graphify_extract.json"
CORRECTIONS = RUN / "corrections.json"


def main():
    data = json.loads(EXTRACT.read_text())
    corr = json.loads(CORRECTIONS.read_text())
    edges = data["edges"]
    valid = {n["id"] for n in data["nodes"]}

    def degree_map():
        G = nx.Graph()
        G.add_nodes_from(valid)
        G.add_edges_from((e["source"], e["target"]) for e in edges)
        return G

    def find(src, tgt):
        for i, e in enumerate(edges):
            if {e["source"], e["target"]} == {src, tgt}:
                return i
        return None

    # Validate every id up front. Without this, a typo'd id makes find() return
    # None and the edge reports as "already applied" — a silent no-op that reads
    # like success. This bit during authoring: the TDD node is `tdd_cycle`, not
    # `tdd_red_green_refactor`, and the run would have claimed the fix landed.
    unknown = []
    for entry in corr.get("replace", []) + corr.get("drop", []):
        for key in ("source", "target", "new_target"):
            v = entry.get(key)
            if v and v not in valid:
                unknown.append(f"{key}={v}")
    if unknown:
        print("  ERROR unknown node ids in corrections.json:")
        for u in unknown:
            print(f"    {u}")
        return 1

    replaced = dropped = skipped = 0

    for r in corr.get("replace", []):
        if r["new_target"] not in valid:
            print(f"  ERROR unknown new_target: {r['new_target']}")
            return 1
        i = find(r["source"], r["target"])
        if i is None:
            print(f"  already applied: {r['source']} -> {r['target']}")
            skipped += 1
            continue
        edges[i] = {
            "source": r["source"],
            "target": r["new_target"],
            "type": r["new_type"],
            "confidence": r["new_confidence"],
            "evidence": r["new_evidence"],
        }
        print(f"  replaced: {r['source']} -> {r['target']}  ==>  {r['new_target']}")
        replaced += 1

    for d in corr.get("drop", []):
        i = find(d["source"], d["target"])
        if i is None:
            print(f"  already applied: {d['source']} -> {d['target']}")
            skipped += 1
            continue
        G = degree_map()
        endangered = [n for n in (d["source"], d["target"]) if G.degree(n) <= 1]
        if endangered:
            print(f"  REFUSED drop {d['source']} -> {d['target']}: "
                  f"would orphan {endangered}. Use a replace instead.")
            return 1
        edges.pop(i)
        print(f"  dropped: {d['source']} -> {d['target']}")
        dropped += 1

    data["edges"] = edges
    EXTRACT.write_text(json.dumps(data, indent=2))

    G = degree_map()
    ncomp = nx.number_connected_components(G)
    print(f"\ncorrections: {replaced} replaced, {dropped} dropped, "
          f"{skipped} already applied")
    print(f"GRAPH: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")
    print(f"components: {ncomp}  |  largest: "
          f"{max(len(c) for c in nx.connected_components(G))}")
    if ncomp != 1:
        print("  NOT SHIPPABLE — corrections fragmented the graph.")
        return 1
    print("  CONNECTED — shippable.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
