"""Read-only measurements for 06_graph_review.md; run with Python 3.11+.

    python analysis/audit_graph_review.py

Measures annotations in the rebuilt M9 graph, not mathematical correctness or
student mastery. Writes JSON to stdout; never changes graph or solution files.
"""
from __future__ import annotations

import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean


def audit(data: Path) -> dict:
    paths = {
        "tree": data / "rebuilt/m9_topic_tree.json",
        "solutions": data / "m9_item_solutions.json",
        "assignment": data / "rebuilt/m9_item_skills.json",
    }
    documents = {key: json.loads(path.read_text()) for key, path in paths.items()}
    nodes = {}
    counts = Counter()

    def visit(node: dict, level: int) -> None:
        counts[level] += 1
        if level == 2:
            if node["id"] in nodes:
                raise ValueError(f"Duplicate principle: {node['id']}")
            nodes[node["id"]] = node
        for child in node.get("children", []):
            visit(child, level + 1)

    for area in documents["tree"]["areas"]:
        visit(area, 0)

    items = {
        f"{test} {item}": value["principy"]
        for test, group in documents["solutions"].items()
        for item, value in group.items()
    }
    derived = {
        test: {item: value["principy"] for item, value in group.items()}
        for test, group in documents["solutions"].items()
    }
    if derived != documents["assignment"]:
        raise ValueError("Solutions and generated assignment disagree")
    for ref, ids in items.items():
        if not ids or len(ids) != len(set(ids)) or set(ids) - nodes.keys():
            raise ValueError(f"Invalid principle list: {ref}")

    ancestors = {}
    active = set()

    def closure(node_id: str) -> set[str]:
        if node_id not in nodes:
            raise ValueError(f"Unknown prerequisite: {node_id}")
        if node_id in active:
            raise ValueError(f"Prerequisite cycle involving: {node_id}")
        if node_id not in ancestors:
            active.add(node_id)
            result = {node_id}
            for prerequisite in nodes[node_id]["requires"]:
                result.update(closure(prerequisite))
            active.remove(node_id)
            ancestors[node_id] = result
        return ancestors[node_id]

    for node_id in nodes:
        closure(node_id)

    uses = {node_id: set() for node_id in nodes}
    for ref, ids in items.items():
        for node_id in ids:
            uses[node_id].add(ref)
    used = [node_id for node_id, refs in uses.items() if refs]
    edges = [(p, n) for n, node in nodes.items() for p in node["requires"]]
    redundant = [
        [p, n] for p, n in edges
        if any(p in closure(q) for q in nodes[n]["requires"] if q != p)
    ]
    single = Counter(ids[0] for ids in items.values() if len(ids) == 1)
    main = Counter(ids[0] for ids in items.values())
    expanded = [len(set().union(*(closure(n) for n in ids))) for ids in items.values()]
    signatures = defaultdict(list)
    for node_id in used:
        signatures[tuple(sorted(uses[node_id]))].append(node_id)

    adjacency = {node_id: set() for node_id in nodes}
    for p, n in edges:
        adjacency[p].add(n)
        adjacency[n].add(p)
    unseen = set(nodes)
    components = []
    while unseen:
        component, pending = set(), [min(unseen)]
        while pending:
            n = pending.pop()
            if n not in component:
                component.add(n)
                pending.extend(adjacency[n] - component)
        components.append(len(component))
        unseen.difference_update(component)

    return {
        "scope": "Rebuilt M9 graph; 2022–2026 solution annotations; excludes older items",
        "source_sha256": {key: hashlib.sha256(path.read_bytes()).hexdigest() for key, path in paths.items()},
        "areas": counts[0], "topics": counts[1], "skills": len(nodes),
        "used_skills": len(used), "unused_skills": len(nodes) - len(used),
        "edges": len(edges), "redundant_edges": redundant,
        "items": len(items), "tests": len(documents["solutions"]),
        "principle_count_distribution": dict(sorted(Counter(map(len, items.values())).items())),
        "average_direct": mean(map(len, items.values())),
        "average_closure": mean(expanded), "max_closure": max(expanded),
        "used_without_single_principle_item": sum(not single[n] for n in used),
        "used_never_main": sum(not main[n] for n in used),
        "used_one_or_two_items": sum(len(uses[n]) <= 2 for n in used),
        "used_less_than_five_items": sum(len(uses[n]) < 5 for n in used),
        "multi_principle_items": sum(len(ids) > 1 for ids in items.values()),
        "multi_principle_items_without_edges": sum(
            len(ids) > 1 and not any(p in ids and n in ids for p, n in edges)
            for ids in items.values()
        ),
        "component_sizes": sorted(components, reverse=True),
        "isolated_used": [n for n in used if not adjacency[n]],
        "identical_nonempty_assignment_columns": [group for group in signatures.values() if len(group) > 1],
    }


if __name__ == "__main__":
    print(json.dumps(audit(Path(__file__).resolve().parent / "data"), ensure_ascii=False, indent=2))
