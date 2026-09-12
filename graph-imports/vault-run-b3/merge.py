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
    for i in range(1, 11):
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

    print(f"chunks: {len(chunk_files)}/10 present")
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

    def absorb(keep, n):
        """Fold n's provenance into keep.

        Batch 2's extraction emitted a single `source_file`; batch 3's emits a
        `sources` list. Unioning only the singular field silently drops every
        source on a merged batch-3 node, which then reads as unsourced to
        wire_sources.py. Handle both shapes.
        """
        keep.setdefault("source_files", [])
        incoming = list(n.get("sources") or [])
        if n.get("source_file"):
            incoming.append(n["source_file"])
        for sf in incoming:
            if sf and sf not in keep["source_files"]:
                keep["source_files"].append(sf)

    canonical, remap = {}, {}
    for label, group in by_label.items():
        # prefer the shortest id — usually the least file-name-polluted
        keep = min(group, key=lambda n: (len(n["id"]), n["id"]))
        canonical[keep["id"]] = keep
        for n in group:
            remap[n["id"]] = keep["id"]
            absorb(keep, n)

    collapsed = len(nodes) - len(canonical)
    print(f"collapsed {collapsed} duplicate-label nodes -> {len(canonical)} unique")

    # --- second pass: word-order-insensitive collapse --------------------------
    # norm_label only folds case and punctuation, so "Adversarial cross-model
    # plan review" and "Cross-model adversarial plan review" survive as two
    # hubs of the same concept. Sorting the token set catches those.
    #
    # Deliberately kept as a separate, logged pass rather than folded into
    # norm_label: token-sorting is lossy (it would also equate "A depends on B"
    # with "B depends on A"), so every group it forms is printed for eyeball
    # review instead of being merged silently.
    STOP = {"a", "an", "the", "of", "to", "for", "and", "or", "in", "on",
            "before", "after", "not", "is", "by", "with", "as", "at"}

    def token_key(label):
        words = [w for w in re.sub(r"[^a-z0-9 ]", " ", label.lower()).split()
                 if w and w not in STOP]
        return " ".join(sorted(words))

    fuzzy = defaultdict(list)
    for nid, n in canonical.items():
        fuzzy[token_key(n.get("label", nid))].append(nid)

    fuzzy_merged = 0
    for _, ids in fuzzy.items():
        if len(ids) < 2:
            continue
        keep_id = min(ids, key=lambda i: (len(i), i))
        for nid in ids:
            if nid == keep_id:
                continue
            print(f"  fuzzy-collapse: {canonical[nid].get('label')!r} "
                  f"-> {canonical[keep_id].get('label')!r}")
            absorb(canonical[keep_id], canonical[nid])
            remap[nid] = keep_id
            for src, dst in list(remap.items()):
                if dst == nid:
                    remap[src] = keep_id
            del canonical[nid]
            fuzzy_merged += 1

    if fuzzy_merged:
        print(f"fuzzy-collapsed {fuzzy_merged} word-order duplicates "
              f"-> {len(canonical)} unique")

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
    # Batch 3 differs from batch 2 in two ways the old pass could not read:
    # the chunk manifest is a list of {chunk, files:[{path}]} rather than a list
    # of path lists, and the agents were told to emit `sources` (plural) rather
    # than `source_files`. Paths also arrive absolute from the agents but are
    # stored "./claude/..." in the manifest, so both sides are normalized to a
    # skills-relative tail before comparing — otherwise every file reads as
    # uncovered and the coverage number is a silent lie.
    def norm_src(s):
        s = str(s).strip()
        for pre in ("/Users/joshuaf/ai-os/skills/", "skills/", "./"):
            if s.startswith(pre):
                s = s[len(pre):]
                break
        return s

    chunks = json.loads((OUT / ".b3_chunks.json").read_text())
    all_src = {norm_src(f["path"]) for c in chunks for f in c["files"]}
    covered = set()
    for n in canonical.values():
        srcs = n.get("sources") or n.get("source_files") or []
        if not srcs and n.get("source_file"):
            srcs = [n["source_file"]]
        for sf in srcs:
            if sf:
                covered.add(norm_src(sf))
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
