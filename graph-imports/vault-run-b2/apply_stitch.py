"""Apply the stitching agent's bridge edges and re-check connectivity.

Validates every proposed edge against the real ID set before merging — the
stitching agent works from label lists and can hallucinate an ID. Dangling
edges are dropped and reported, never silently accepted.
"""
import json
from pathlib import Path

import networkx as nx

OUT = Path("graphify-out")


def main():
    extraction = json.loads((OUT / ".graphify_extract.json").read_text())
    stitch = json.loads((OUT / ".stitch.json").read_text())

    valid = {n["id"] for n in extraction["nodes"]}
    existing = {(min(e["source"], e["target"]), max(e["source"], e["target"]))
                for e in extraction["edges"]}

    added, dangling, dupes = [], [], 0
    for e in stitch.get("edges", []):
        s, t = e.get("source"), e.get("target")
        if s not in valid or t not in valid:
            dangling.append((s, t))
            continue
        key = (min(s, t), max(s, t))
        if key in existing:
            dupes += 1
            continue
        existing.add(key)
        e.pop("note", None)  # justification is for review, not the graph
        added.append(e)

    print(f"stitch: {len(added)} edges added, {len(dangling)} dangling dropped, "
          f"{dupes} already present")
    for s, t in dangling[:10]:
        print(f"  dropped (unknown id): {s} -> {t}")

    extraction["edges"].extend(added)
    (OUT / ".graphify_extract.json").write_text(json.dumps(extraction, indent=2))

    G = nx.Graph()
    G.add_nodes_from(valid)
    G.add_edges_from((e["source"], e["target"]) for e in extraction["edges"])
    comps = sorted(nx.connected_components(G), key=len, reverse=True)
    largest = len(comps[0]) if comps else 0

    print()
    print(f"GRAPH: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")
    print(f"components: {len(comps)}  |  largest: {largest} "
          f"({largest / max(G.number_of_nodes(), 1):.1%})")
    if len(comps) == 1:
        print("  CONNECTED — shippable.")
    else:
        print("  still fragmented:")
        for c in comps[1:]:
            labels = [n for n in sorted(c)][:5]
            print(f"    {len(c)} nodes: {labels}")


if __name__ == "__main__":
    main()
