"""Compare ways of representing CERMAT M9 items and tests as graphs, on real data.

Read-only. Reads the rebuilt tree (data/rebuilt/), the solutions of the 20 tests and CERMAT's
item statistics, and prints the numbers quoted in 07_graph_representation.md.

    uv run --no-project --with numpy --with networkx --with scikit-learn \
        python analysis/graph_representation_audit.py
"""
import random
import csv
import json
import re
import collections
import itertools
from pathlib import Path

import numpy as np
import networkx as nx
from sklearn.linear_model import RidgeCV
from sklearn.model_selection import LeaveOneGroupOut

ROOT = Path(__file__).resolve().parent / "data"
tree = json.loads((ROOT / "rebuilt/m9_topic_tree.json").read_text())
sol = json.loads((ROOT / "m9_item_solutions.json").read_text())
stats = {(r["year"] + " " + r["term"], r["item"]): r
         for r in csv.DictReader(open(ROOT / "m9_item_stats_2022_2026.csv"))}
catalog = {(r["year"] + " " + r["term"], r["task"]): r
           for r in csv.DictReader(open(ROOT / "m9_task_catalog.tsv"), delimiter="\t")}

# ---------- tree ----------
nodes, area_of, topic_of, requires, name = [], {}, {}, {}, {}
for a in tree["areas"]:
    for t in a["children"]:
        for s in t["children"]:
            nodes.append(s["id"])
            area_of[s["id"]] = a["id"]
            topic_of[s["id"]] = t["id"]
            requires[s["id"]] = s.get("requires", [])
            name[s["id"]] = s["name"]
G = nx.DiGraph()  # edge A -> B means B requires A
G.add_nodes_from(nodes)
for b, reqs in requires.items():
    for a in reqs:
        G.add_edge(a, b)
assert nx.is_directed_acyclic_graph(G)

depth = {}
for n in nx.topological_sort(G):
    preds = list(G.predecessors(n))
    depth[n] = 1 + max((depth[p] for p in preds), default=0)

def closure(ps):
    out = set(ps)
    for p in ps:
        out |= nx.ancestors(G, p)
    return out

# ---------- items ----------
ALIAS = {("2023 B", "9"): "9.3"}

def sub_ids(task, sp):
    if sp.startswith("b"):
        return [f"{task}.{i}" for i in (1, 2, 3)]
    if ":" not in sp:
        return [task]
    return [x.split(":")[0] for x in sp.split(",")]

def pct_correct(row, key):
    d = dict(x.split(":") for x in row["distribution_pct"].split() if ":" in x)
    key = {"Ano": "A", "Ne": "N"}.get(key, key)
    if key in d:
        return float(d[key])
    if key == "N" and "B" in d:
        return float(d["B"])
    return None

def success_of(test, it, cat):
    st = stats.get((test, ALIAS.get((test, it), it)))
    if not st:
        return None, None
    n = int(st["n_test_takers"]) if st["n_test_takers"] else None
    if st["mean_pct_score"]:
        return float(st["mean_pct_score"]), n
    keys = cat["keys"].split(",") if cat.get("keys") else []
    ids = sub_ids(cat["task"], cat["subpoints"])
    if it in ids and keys and ids.index(it) < len(keys):
        return pct_correct(st, keys[ids.index(it)]), n
    return None, n

items = []
for test, its in sol.items():
    for it, rec in its.items():
        task = it.split(".")[0]
        cat = catalog.get((test, task), {})
        succ, n = success_of(test, it, cat)
        items.append(dict(
            test=test, item=it, task=task, principles=rec["principy"], reseni=rec["reseni"],
            fmt=cat.get("fmt", "?"), tags=(cat.get("tags") or "").split(";"),
            success=succ, n=n,
        ))
print(f"items {len(items)}, with success rate {sum(i['success'] is not None for i in items)}")
used = sorted({p for i in items for p in i["principles"]})
print(f"principles used {len(used)} of {len(nodes)}; links {G.number_of_edges()}")

# ---------- 1. exam as a graph: coverage per test ----------
print("\n## 1. Coverage per test")
tests = sorted(sol)
per_test = {t: set(p for i in items if i["test"] == t for p in i["principles"]) for t in tests}
sizes = [len(per_test[t]) for t in tests]
print(f"principles per test: mean {np.mean(sizes):.1f}, min {min(sizes)}, max {max(sizes)}")
appear = collections.Counter(p for t in tests for p in per_test[t])
for k in (20, 15, 10, 5, 1):
    print(f"  principles in >= {k:2d} of 20 tests: {sum(v >= k for v in appear.values())}")
core = sorted([p for p, v in appear.items() if v >= 15], key=lambda p: -appear[p])
print("  core (>=15 tests):", ", ".join(f"{p}({appear[p]})" for p in core))
jac = [len(per_test[a] & per_test[b]) / len(per_test[a] | per_test[b])
       for a, b in itertools.combinations(tests, 2)]
print(f"Jaccard overlap of two tests' principle sets: mean {np.mean(jac):.2f}, min {min(jac):.2f}, max {max(jac):.2f}")
# same year pairs A/B vs others
same = [len(per_test[a] & per_test[b]) / len(per_test[a] | per_test[b])
        for a, b in itertools.combinations(tests, 2) if a[:4] == b[:4]]
print(f"  same-year pairs: mean {np.mean(same):.2f}")
# closure coverage per test
csz = [len(closure(per_test[t])) for t in tests]
print(f"principles per test incl. prerequisites: mean {np.mean(csz):.1f}")
# area points blueprint
pts_area = collections.defaultdict(lambda: collections.Counter())
for i in items:
    pts_area[i["test"]][area_of[i["principles"][0]]] += 1
areas = [a["id"] for a in tree["areas"]]
print("items per area (by main principle), mean over tests:",
      {a: round(np.mean([pts_area[t][a] for t in tests]), 1) for a in areas})
print("  sd over tests:", {a: round(np.std([pts_area[t][a] for t in tests]), 1) for a in areas})

# ---------- 2. Q-matrix diagnosability ----------
print("\n## 2. Q-matrix: can the item bank localize a gap?")
Qsets = [frozenset(i["principles"]) for i in items]
single = collections.Counter(next(iter(q)) for q in Qsets if len(q) == 1)
print(f"principles that appear alone in some item: {len(single)} of {len(used)}")
# contrast pairs: items i, j with Q_i = Q_j + {k}
by_set = collections.defaultdict(list)
for q in Qsets:
    by_set[q].append(q)
contrast = collections.defaultdict(int)
setlist = set(Qsets)
for q in setlist:
    for k in q:
        rest = q - {k}
        if (not rest) or rest in setlist:
            contrast[k] += 1
print(f"principles isolable by a contrast pair (an item that needs exactly one principle more than another item, or the principle alone): {len(contrast)} of {len(used)}")
# with prerequisite closure as the "needs" set (old-style)
Csets = set(frozenset(closure(q)) for q in Qsets)
contrast_c = set()
for q in Csets:
    for k in q:
        rest = q - {k}
        if (not rest) or rest in Csets:
            contrast_c.add(k)
print(f"  same test when an item's set is its prerequisite closure: {len(contrast_c)}")
# identical columns
cols = collections.defaultdict(list)
for p in used:
    cols[frozenset(idx for idx, q in enumerate(Qsets) if p in q)].append(p)
print(f"principles sharing an identical item column with another: {sum(len(v) for v in cols.values() if len(v) > 1)}")

# ---------- 3. prerequisite links vs. observed difficulty (surmise check) ----------
print("\n## 3. Do prerequisites look easier than what rests on them?")
def mean_success(p, main_only):
    vals = [i["success"] for i in items if i["success"] is not None and
            ((i["principles"][0] == p) if main_only else (p in i["principles"]))]
    return (np.mean(vals), len(vals)) if vals else (None, 0)
for main_only in (False, True):
    ok = bad = 0
    diffs = []
    for a, b in G.edges():
        ma, na = mean_success(a, main_only)
        mb, nb = mean_success(b, main_only)
        if ma is None or mb is None or na < 3 or nb < 3:
            continue
        diffs.append(ma - mb)
        ok += ma > mb
        bad += ma <= mb
    print(f"  {'main principle' if main_only else 'any position'}: links testable {ok+bad}, prerequisite easier in {ok} ({ok/(ok+bad):.0%}), mean gap {np.mean(diffs):+.1f} pp")

# ---------- 4. which representation explains item difficulty? ----------
print("\n## 4. Predicting CERMAT item success (leave-one-test-out ridge regression)")
D = [i for i in items if i["success"] is not None]
y = np.array([i["success"] for i in D])
groups = np.array([i["test"] for i in D])
fmts = sorted({i["fmt"] for i in D})
tags = sorted({t for i in D for t in i["tags"] if t})
topics = sorted({topic_of[p] for p in used})

def n_steps(text):
    # rough proxy: number of computation segments in the solution line
    return len([s for s in re.split(r"[;:]\s|, ", text) if re.search(r"[=·+−:/]|\d", s)])

def feats(kind, i):
    P = i["principles"]
    C = closure(P)
    f = {}
    if "fmt" in kind:
        for x in fmts: f["fmt=" + x] = float(i["fmt"] == x)
    if "tags" in kind:
        for x in tags: f["tag=" + x] = float(x in i["tags"])
    if "topic_main" in kind:
        for x in topics: f["topic=" + x] = float(topic_of[P[0]] == x)
    if "main" in kind:
        for x in used: f["main=" + x] = float(P[0] == x)
    if "flat" in kind:
        for x in used: f["p=" + x] = float(x in P)
    if "closure" in kind:
        for x in nodes: f["c=" + x] = float(x in C)
    if "counts" in kind:
        f["n_principles"] = len(P)
        f["n_closure"] = len(C)
        f["max_depth"] = max(depth[p] for p in P)
        f["n_areas"] = len({area_of[p] for p in P})
        f["n_steps"] = n_steps(i["reseni"])
    if "steps" in kind:
        f["n_steps"] = n_steps(i["reseni"])
    if "nprin" in kind:
        f["n_principles"] = len(P)
    if "hier" in kind:  # principle + its topic + its area: rare principles borrow from their group
        for x in used:
            if x in P:
                f["p=" + x] = 1.0
                f["t=" + topic_of[x]] = f.get("t=" + topic_of[x], 0) + 1.0
                f["a=" + area_of[x]] = f.get("a=" + area_of[x], 0) + 1.0
    if "weighted" in kind:  # main principle counts more than the helpers
        for k, x in enumerate(P):
            f["p=" + x] = 1.0 if k == 0 else 0.5
    return f

def evaluate(kind, subset=None, return_pred=False):
    D_ = D if subset is None else [i for i in D if subset(i)]
    y_ = np.array([i["success"] for i in D_])
    g_ = np.array([i["test"] for i in D_])
    r2, mae, k, pred = _evaluate(kind, D_, y_, g_)
    return (r2, mae, k, pred) if return_pred else (r2, mae, k)

def _evaluate(kind, D, y, groups):
    F = [feats(kind, i) for i in D]
    keys = sorted({k for f in F for k in f})
    X = np.array([[f.get(k, 0.0) for k in keys] for f in F]) if keys else np.zeros((len(D), 0))
    pred = np.zeros_like(y)
    for tr, te in LeaveOneGroupOut().split(X, y, groups):
        if X.shape[1] == 0:
            pred[te] = y[tr].mean()
            continue
        mu, sd = X[tr].mean(0), X[tr].std(0) + 1e-9
        m = RidgeCV(alphas=np.logspace(-2, 4, 25)).fit((X[tr] - mu) / sd, y[tr])
        pred[te] = m.predict((X[te] - mu) / sd)
    ss = ((y - pred) ** 2).sum()
    r2 = 1 - ss / ((y - y.mean()) ** 2).sum()
    mae = np.abs(y - pred).mean()
    return r2, mae, X.shape[1], pred

MODELS = [
    ("baseline: mean only", ()),
    ("format of the item only", ("fmt",)),
    ("catalog tags (19 topics as labels)", ("tags",)),
    ("topic of main principle (23)", ("topic_main",)),
    ("main principle only (131)", ("main",)),
    ("flat principle set = Q-matrix (131)", ("flat",)),
    ("principle set + prerequisite closure", ("closure",)),
    ("counts: n principles, closure, depth, areas, steps", ("counts",)),
    ("n principles only", ("nprin",)),
    ("solution-step count only", ("steps",)),
    ("format + Q-matrix", ("fmt", "flat")),
    ("format + Q-matrix + counts", ("fmt", "flat", "counts")),
    ("format + closure + counts", ("fmt", "closure", "counts")),
    ("format + tags + counts", ("fmt", "tags", "counts")),
    ("hierarchical: principle + topic + area", ("hier",)),
    ("main weighted 1, helpers 0.5", ("weighted",)),
    ("format + hierarchical + counts", ("fmt", "hier", "counts")),
    ("format + tags", ("fmt", "tags")),
]
for label, kind in MODELS:
    r2, mae, k = evaluate(kind)
    r2b, maeb, _ = evaluate(kind, subset=lambda i: i["test"][-1] in "AB")
    print(f"  {label:45s} feat {k:4d}  R² {r2:+.3f}  MAE {mae:5.1f}  | A/B only R² {r2b:+.3f}")

# residuals of the best principle model: what does the graph miss?
_, _, _, pred = evaluate(("fmt", "hier", "counts"), return_pred=True)
res = sorted(zip(y - pred, D), key=lambda x: x[0])
print("\n  Harder than the model predicts (success − prediction):")
for r, i in res[:14]:
    print(f"   {r:+6.1f}  {i['test']} {i['item']:5s} {i['fmt']:5s} {i['success']:5.1f}%  {', '.join(i['principles'])}  | {i['reseni'][:110]}")
print("  Easier than predicted:")
for r, i in res[-8:]:
    print(f"   {r:+6.1f}  {i['test']} {i['item']:5s} {i['fmt']:5s} {i['success']:5.1f}%  {', '.join(i['principles'])}  | {i['reseni'][:110]}")
# variance decomposition by format
for f_ in fmts:
    v = y[np.array([i["fmt"] == f_ for i in D])]
    print(f"  format {f_:6s} items {len(v):3d}  mean success {v.mean():5.1f} %")

# simple correlations
ns = np.array([len(i["principles"]) for i in D])
cs = np.array([len(closure(i["principles"])) for i in D])
st = np.array([n_steps(i["reseni"]) for i in D])
print(f"  corr(success, n principles) {np.corrcoef(y, ns)[0,1]:+.2f}; corr(success, closure size) {np.corrcoef(y, cs)[0,1]:+.2f}; corr(success, step proxy) {np.corrcoef(y, st)[0,1]:+.2f}")
for k in range(1, 7):
    v = y[ns == k]
    if len(v): print(f"    items with {k} principles: {len(v):3d}, mean success {v.mean():.1f} %")

# ---------- 5. co-occurrence network (bipartite projection) ----------
print("\n## 5. Principle co-occurrence network (two principles linked when one item uses both)")
C = nx.Graph()
C.add_nodes_from(used)
for i in items:
    for a, b in itertools.combinations(sorted(set(i["principles"])), 2):
        w = C[a][b]["weight"] + 1 if C.has_edge(a, b) else 1
        C.add_edge(a, b, weight=w)
print(f"edges {C.number_of_edges()}, density {nx.density(C):.3f}, components {nx.number_connected_components(C)}")
comms = nx.community.louvain_communities(C, weight="weight", seed=1)
print(f"Louvain communities: {len(comms)}")
from sklearn.metrics import adjusted_mutual_info_score
lab_c = {p: k for k, c in enumerate(comms) for p in c}
print(f"agreement with the 7 areas (AMI): {adjusted_mutual_info_score([area_of[p] for p in used], [lab_c[p] for p in used]):.2f}; with the 23 topics: {adjusted_mutual_info_score([topic_of[p] for p in used], [lab_c[p] for p in used]):.2f}")
for k, c in enumerate(sorted(comms, key=len, reverse=True)):
    ar = collections.Counter(area_of[p] for p in c)
    print(f"  community {k+1}: {len(c)} principles, areas {dict(ar.most_common())}")
bt = nx.betweenness_centrality(C, weight=None)
print("bridges (highest betweenness):", ", ".join(f"{p} {bt[p]:.2f}" for p in sorted(bt, key=bt.get, reverse=True)[:10]))
# overlap of co-occurrence with prerequisite links
pre_und = {frozenset(e) for e in G.edges()}
co = {frozenset(e) for e in C.edges()}
print(f"prerequisite links that also co-occur in an item: {len(pre_und & co)} of {len(pre_und)}; co-occurrence pairs that are prerequisite links: {len(pre_und & co)} of {len(co)}")
cross_area = sum(1 for a, b in C.edges() if area_of[a] != area_of[b])
print(f"co-occurrence edges across areas: {cross_area} of {C.number_of_edges()} ({cross_area / C.number_of_edges():.0%}); prerequisite links across areas: {sum(1 for a, b in G.edges() if area_of[a] != area_of[b])} of {G.number_of_edges()}")

# ---------- 6. PageRank on prerequisites (what everything rests on) ----------
print("\n## 6. Centrality in the prerequisite graph")
# weight each principle by the items using it, then let credit flow to prerequisites
use_count = collections.Counter(p for i in items for p in i["principles"])
pers = {n: use_count.get(n, 0) + 0.01 for n in nodes}
pr = nx.pagerank(G.reverse(), personalization=pers, alpha=0.85)
print("PageRank (items' demand flowing down to prerequisites):",
      ", ".join(f"{p} {pr[p]:.3f}" for p in sorted(pr, key=pr.get, reverse=True)[:12]))
desc = {n: len(nx.descendants(G, n)) for n in nodes}
print("most principles resting on it:", ", ".join(f"{p} {desc[p]}" for p in sorted(desc, key=desc.get, reverse=True)[:10]))
print(f"longest prerequisite chain: {max(depth.values())} principles: ", " → ".join(nx.dag_longest_path(G)))

# ---------- 7. tasks as hyperedges (shared stems) ----------
print("\n## 7. Tasks with several items (shared stem)")
by_task = collections.defaultdict(list)
for i in items:
    by_task[(i["test"], i["task"])].append(i)
multi = [v for v in by_task.values() if len(v) > 1]
print(f"tasks {len(by_task)}, with >1 item {len(multi)} covering {sum(len(v) for v in multi)} items")
shared = [len(set.intersection(*[set(x['principles']) for x in v])) for v in multi]
print(f"  items of one task sharing at least one principle: {sum(s > 0 for s in shared)} of {len(multi)} tasks")
# within-task success spread
spreads = [max(x['success'] for x in v) - min(x['success'] for x in v)
           for v in multi if all(x['success'] is not None for x in v)]
print(f"  success spread inside a task: mean {np.mean(spreads):.1f} pp, max {max(spreads):.1f} pp")

# ---------- 8. coverage by k past tests ----------
print('\n## 8. Coverage of the graph by k random past tests')

tests = sorted(sol)
per_test = {t: set(p for i in items if i["test"] == t for p in i["principles"]) for t in tests}
w = collections.Counter(p for i in items for p in i["principles"])  # item uses
tot = sum(w.values())
random.seed(1)
for k in (1, 2, 3, 5, 10, 15):
    cov, wcov = [], []
    for _ in range(2000):
        s = set().union(*[per_test[t] for t in random.sample(tests, k)])
        cov.append(len(s) / len(used)); wcov.append(sum(w[p] for p in s) / tot)
    print(f"{k:2d} past tests: cover {np.mean(cov):.0%} of the 131 principles, {np.mean(wcov):.0%} of all principle uses")

# ---------- 9. position and slots ----------
print('\n## 9. Position in the test and slot stability')

D = [i for i in items if i["success"] is not None]
pos = np.array([int(i["task"]) for i in D]); y = np.array([i["success"] for i in D])
print("corr(success, task number)", round(np.corrcoef(pos, y)[0,1], 2))
for t in range(1, 17):
    v = y[pos == t]
    print(f"task {t:2d}: items {len(v):3d} mean success {v.mean():5.1f}")
print("\n## Slot stability: per task number, which topic is the main principle's topic (20 tests)")
tasks = collections.defaultdict(dict)
for i in items:
    tasks[(i["test"], int(i["task"]))].setdefault("p", []).extend(i["principles"])
    tasks[(i["test"], int(i["task"]))].setdefault("main", i["principles"][0])
for t in range(1, 18):
    tops = collections.Counter(topic_of[v["main"]] for (te, tn), v in tasks.items() if tn == t)
    ars = collections.Counter(area_of[v["main"]] for (te, tn), v in tasks.items() if tn == t)
    n = sum(tops.values())
    if not n: continue
    top, c = tops.most_common(1)[0]; ar, ca = ars.most_common(1)[0]
    print(f"task {t:2d} ({n:2d} tests): top topic {top:10s} {c/n:4.0%} | top area {ar} {ca/n:4.0%} | {dict(tops.most_common(4))}")

# ---------- 10. distractors ----------
print('\n## 10. Closed items with a dominant wrong answer')

rows = []
for i in items:
    cat = catalog.get((i["test"], i["task"]), {})
    if cat.get("fmt") not in ("MC", "PR"):
        continue
    st = stats.get((i["test"], ALIAS.get((i["test"], i["item"]), i["item"])))
    if not st or not st["distribution_pct"]:
        continue
    keys = cat["keys"].split(",") if cat.get("keys") else []
    ids = sub_ids(cat["task"], cat["subpoints"])
    if i["item"] not in ids or not keys:
        continue
    key = keys[ids.index(i["item"])]
    d = {k: float(v) for k, v in (x.split(":") for x in st["distribution_pct"].split() if ":" in x)}
    wrong = {k: v for k, v in d.items() if k != key}
    if not wrong or key not in d:
        continue
    k2, v2 = max(wrong.items(), key=lambda kv: kv[1])
    rows.append((i, key, d[key], k2, v2))
print("closed MC/PR items with distributions:", len(rows))
print("a wrong option chosen by >= 25 %:", sum(r[4] >= 25 for r in rows))
print("a wrong option chosen more often than the key:", sum(r[4] > r[2] for r in rows))
for i, key, kv, k2, v2 in sorted(rows, key=lambda r: r[2] - r[4])[:12]:
    print(f"  {i['test']} {i['item']:5s} key {key} {kv:4.1f}% | top wrong {k2} {v2:4.1f}% | {', '.join(i['principles'])}")
