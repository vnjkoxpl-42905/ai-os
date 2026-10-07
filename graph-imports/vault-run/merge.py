"""Merge extraction chunks, collapse duplicate-label nodes, drop dangling edges.

The fragmentation fix from the docs run. Parallel extraction agents only see their
own chunk, so they only write intra-chunk edges. Naive merge shatters the graph.
Node/edge totals look identical whether a graph is whole or in pieces, so the only
honest health signal is nx.connected_components.
"""
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import networkx as nx

OUT = Path("graphify-out")


def norm_label(label):
    """Normalize a label so the same concept from two files collapses to one node."""
    s = label.lower().strip()
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def main():
    chunk_files = sorted(OUT.glob(".graphify_chunk_*.json"))
    if not chunk_files:
        sys.exit("No chunk files found.")

    nodes, edges, hyperedges = [], [], []
    missing, bad = [], []
    for i in range(1, 15):
        p = OUT / f".graphify_chunk_{i:02d}.json"
        if not p.exists():
            missing.append(i)
            continue
        try:
            d = json.loads(p.read_text())
        except json.JSONDecodeError as e:
            bad.append((i, str(e)[:60]))
            continue
        nodes.extend(d.get("nodes", []))
        edges.extend(d.get("edges", []))
        hyperedges.extend(d.get("hyperedges", []))

    print(f"chunks: {len(chunk_files)}/14 present")
    if missing:
        print(f"  MISSING chunks (re-run these): {missing}")
    if bad:
        print(f"  INVALID JSON: {bad}")
    print(f"raw: {len(nodes)} nodes, {len(edges)} edges, {len(hyperedges)} hyperedges")

    # --- collapse duplicate labels -------------------------------------------
    # IDs are {stem}_{entity}, so the same concept in two files gets two IDs.
    # Pick one canonical ID per normalized label; remap everything onto it.
    by_label = defaultdict(list)
    for n in nodes:
        by_label[norm_label(n.get("label", n["id"]))].append(n)

    canonical, remap = {}, {}
    for label, group in by_label.items():
        # prefer the shortest id — usually the least file-name-polluted
        keep = min(group, key=lambda n: (len(n["id"]), n["id"]))
        canonical[keep["id"]] = keep
        for n in group:
            remap[n["id"]] = keep["id"]
            # preserve every source file this concept appeared in
            keep.setdefault("source_files", [])
            sf = n.get("source_file")
            if sf and sf not in keep["source_files"]:
                keep["source_files"].append(sf)

    collapsed = len(nodes) - len(canonical)
    print(f"collapsed {collapsed} duplicate-label nodes -> {len(canonical)} unique")

    # --- remap + validate edges ----------------------------------------------
    valid_ids = set(canonical)
    seen_pairs = set()
    clean_edges, dangling, self_loops = [], 0, 0
    for e in edges:
        s, t = remap.get(e["source"]), remap.get(e["target"])
        if s is None or t is None:
            dangling += 1
            continue
        if s == t:
            self_loops += 1
            continue
        key = (min(s, t), max(s, t))
        if key in seen_pairs:
            continue
        seen_pairs.add(key)
        e = dict(e, source=s, target=t)
        clean_edges.append(e)

    print(f"edges: {len(clean_edges)} kept, {dangling} dangling dropped, "
          f"{self_loops} self-loops dropped")

    clean_hyper = []
    for h in hyperedges:
        mapped = [remap[n] for n in h.get("nodes", []) if n in remap]
        if len(mapped) >= 3:
            clean_hyper.append(dict(h, nodes=sorted(set(mapped))))

    extraction = {
        "nodes": list(canonical.values()),
        "edges": clean_edges,
        "hyperedges": clean_hyper,
        "input_tokens": 0,
        "output_tokens": 0,
    }
    (OUT / ".graphify_extract.json").write_text(json.dumps(extraction, indent=2))

    # --- the ship gate --------------------------------------------------------
    G = nx.Graph()
    G.add_nodes_from(valid_ids)
    G.add_edges_from((e["source"], e["target"]) for e in clean_edges)

    comps = sorted(nx.connected_components(G), key=len, reverse=True)
    largest = len(comps[0]) if comps else 0
    print()
    print(f"GRAPH: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")
    print(f"components: {len(comps)}  |  largest: {largest} "
          f"({largest / max(G.number_of_nodes(), 1):.1%})")
    if len(comps) > 1:
        print(f"  NOT SHIPPABLE — needs a stitching pass.")
        orphans = {}
        for c in comps[1:]:
            orphans[len(c)] = orphans.get(len(c), 0) + 1
        print(f"  orphan component sizes: {dict(sorted(orphans.items(), reverse=True))}")
        # write orphans out for the stitching agent
        payload = []
        for c in comps[1:]:
            payload.append([
                {"id": nid, "label": canonical[nid].get("label", nid),
                 "source_file": canonical[nid].get("source_file")}
                for nid in sorted(c)
            ])
        (OUT / ".orphans.json").write_text(json.dumps(payload, indent=2))
        hubs = sorted(comps[0], key=lambda n: G.degree(n), reverse=True)[:60]
        (OUT / ".hubs.json").write_text(json.dumps(
            [{"id": h, "label": canonical[h].get("label", h),
              "degree": G.degree(h)} for h in hubs], indent=2))
        print(f"  wrote .orphans.json ({len(comps) - 1} components) and .hubs.json")
    else:
        print("  CONNECTED — shippable.")

    # --- coverage -------------------------------------------------------------
    chunks = json.loads((OUT / ".chunks.json").read_text())
    all_src = {f for c in chunks for f in c}
    covered = set()
    for n in canonical.values():
        for sf in n.get("source_files", []) or [n.get("source_file")]:
            if sf:
                covered.add(sf)
    uncovered = all_src - covered
    print()
    print(f"coverage: {len(all_src) - len(uncovered)}/{len(all_src)} source files "
          f"produced at least one node")
    if uncovered:
        print(f"  {len(uncovered)} uncovered:")
        for f in sorted(uncovered)[:15]:
            print(f"    {f}")


if __name__ == "__main__":
    main()
