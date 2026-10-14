"""Read-only source audit and proposal export. Never rebuilds the application DB.

Run from any directory with the project's Python. Only writes sibling evidence.json
and example-exam-graph.json. The export is an illustration, not a production release.
"""
from __future__ import annotations

import hashlib
import json
import sqlite3
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "analysis"))
from audit_graph_review import audit


def main():
    data = ROOT / "analysis/data"
    evidence = audit(data)
    solutions = json.loads((data / "m9_item_solutions.json").read_text())
    older = json.loads((data / "m9_item_solutions_older.json").read_text())
    tree = json.loads((data / "rebuilt/m9_topic_tree.json").read_text())
    principles = {p["id"]: p for a in tree["areas"] for t in a["children"] for p in t["children"]}
    db_path = ROOT / "backend/data/problems.sqlite"
    db = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    db.row_factory = sqlite3.Row
    exams = [dict(r) for r in db.execute("SELECT year, term, COUNT(*) tasks, SUM(points) points FROM problems GROUP BY year, term")]
    evidence.update({
        "audited_on": "2026-10-04",
        "database_sha256": hashlib.sha256(db_path.read_bytes()).hexdigest(),
        "database_tasks": db.execute("SELECT COUNT(*) FROM problems").fetchone()[0],
        "database_items": db.execute("SELECT COUNT(*) FROM (SELECT DISTINCT problem_id,item FROM problem_skills)").fetchone()[0],
        "database_empty_text_tasks": db.execute("SELECT COUNT(*) FROM problems WHERE TRIM(text) = ''").fetchone()[0],
        "older_annotations": sum(len(g) for g in older.values()),
        "exams": exams,
        "interpretation": "Counts measure stored annotations and structure, not correctness, mastery, or learning impact.",
    })
    assert len(exams) == 20 and all(x["tasks"] == 16 and x["points"] == 50 for x in exams)
    nodes, edges = {}, []

    def node(id, kind, **attrs):
        assert id not in nodes, id
        nodes[id] = {"id": id, "type": kind, **attrs}
        return id

    def edge(src, relation, dst, **attrs):
        edges.append({"source": src, "type": relation, "target": dst, **attrs})

    exam = node("M9-2025-B", "Exam", year=2025, term="B", maximum_points=50)
    group = solutions["2025 B"]
    used = sorted({p for x in group.values() for p in x["principy"]})
    for p in used:
        node(p, "Principle", label=principles[p]["name"], identity_status="legacy_id; stable ID migration proposed")
    tasks = [dict(r) for r in db.execute("SELECT * FROM problems WHERE year=2025 AND term='B' ORDER BY task")]
    task_summary = []
    for task in tasks:
        tid = node(task["id"], "Task", number=task["task"], label=task["description"], maximum_points=task["points"], format=task["format"], source_pdf=task["source_pdf"], pages=task["pages"], screenshot=task["screenshot"], key_screenshot=task["solution"])
        edge(exam, "HAS_TASK", tid)
        rubric = node(f"{tid}:rubric", "ScoringRule", maximum_points=task["points"], source=task["solution"], encoding="reference_only")
        if task["task"] == 11:
            nodes[rubric].update(encoding="correct_count_lookup", points_by_correct_count={"0":0,"1":0,"2":2,"3":4}, verification="key image inspected 2026-10-04")
        if task["task"] == 15:
            nodes[rubric].update(encoding="correct_count_lookup", points_by_correct_count={"0":0,"1":2,"2":4,"3":6}, verification="key image inspected 2026-10-04")
        edge(tid, "SCORED_BY", rubric)
        selected = {item: v for item, v in group.items() if int(item.split('.')[0]) == task["task"]}
        for item, value in selected.items():
            iid = node(f"{exam}:item:{item}", "Item", label=item, solution_text=value["reseni"], reasoning_status="expanded_proposal" if item == "15.2" else "legacy_text_only")
            edge(tid, "HAS_ITEM", iid)
            edge(rubric, "READS_RESPONSE_FOR", iid)
            for position, principle in enumerate(value["principy"]):
                edge(iid, "ANNOTATED_USES", principle, main=position == 0, provenance="existing single-route annotation; not a universal requirement")
        task_summary.append({"task": task["task"], "description": task["description"], "format": task["format"], "points": task["points"], "items": len(selected), "principles": len({p for v in selected.values() for p in v["principy"]})})
    ctx = node(f"{exam}:context:15", "Context", label="Camp: 80 children, 5 leaders, 4 instructors")
    edge("M9-2025-B-15", "HAS_CONTEXT", ctx)
    for item in ["15.1", "15.2", "15.3"]:
        edge(f"{exam}:item:{item}", "SHARES_CONTEXT", ctx)
    item = f"{exam}:item:15.2"
    given = node(f"{item}:given", "Fact", statement="There are one third fewer younger children than older children", role="given_relation", meaning="Y and O are younger and older child counts", scope=item, derivation="source wording; text inspected")
    goal = node(f"{item}:goal", "Goal", statement="100 (O-Y) / Y", unit="percent", base_population="younger", scope=item)
    answer = node(f"{item}:answer", "Fact", statement="50%", exact_ratio="1/2", option="F", scope=item, answer_check="official key image matched")
    edge(item, "HAS_GIVEN", given)
    edge(item, "ASKS", goal)
    edge(answer, "SATISFIES", goal)

    def route(suffix, label):
        rid = node(f"{item}:route:{suffix}", "Route", label=label, review="proposal authored in this study; principle assignments need independent review")
        edge(item, "HAS_ROUTE", rid)
        return rid

    def step(rid, suffix, label, inputs, output, skills):
        sid = node(f"{rid}:{suffix}", "Step", label=label, input_logic="ALL")
        edge(rid, "HAS_STEP", sid)
        for role, fid in inputs:
            edge(fid, "INPUT_TO", sid, role=role)
        edge(sid, "PRODUCES", output)
        for p in skills:
            edge(sid, "APPLIES", p)

    r1 = route("ratio", "Invert the comparison")
    relation = node(f"{r1}:relation", "Fact", statement="Y = (2/3) O", scope=r1)
    step(r1, "interpret", "Interpret one third fewer using the older group as the base", [("wording", given)], relation, ["VZT.NEZ.o-zlomek"])
    f1 = node(f"{r1}:ratio", "Fact", statement="O / Y = 3/2", scope=r1)
    step(r1, "invert", "Invert the ratio", [("relation", relation)], f1, ["VZT.NEZ.obraceni"])
    step(r1, "percent", "(3/2 - 1) × 100% = 50%", [("ratio", f1), ("requested_base", goal)], answer, ["VZT.PROC.o-kolik-procent"])
    r2 = route("parts", "Use proportional parts")
    f2 = node(f"{r2}:parts", "Fact", statement="O = 3u, Y = 2u, u > 0", scope=r2, note="Proportional units, not literal counts of children")
    step(r2, "represent", "Represent the groups by three and two equal parts", [("relation", given)], f2, ["VZT.NEZ.o-zlomek"])
    step(r2, "percent", "(3u - 2u) / (2u) × 100% = 50%", [("parts", f2), ("requested_base", goal)], answer, ["VZT.PROC.o-kolik-procent"])
    assert Fraction(3,2)-1 == (Fraction(3)-2)/2 == Fraction(1,2)
    assert 180 - 60 - (180 - 132) == 72
    assert Fraction(180 - 72,4) == 27
    assert all(e["source"] in nodes and e["target"] in nodes for e in edges)
    for rid in [r1, r2]:
        route_steps = {e["target"] for e in edges if e["source"] == rid and e["type"] == "HAS_STEP"}
        pending = set(route_steps)
        available = {given, goal}
        while pending:
            ready = {s for s in pending if {e["source"] for e in edges if e["target"] == s and e["type"] == "INPUT_TO"} <= available}
            assert ready, "Cyclic or unsatisfied route dependency"
            available |= {e["target"] for e in edges if e["source"] in ready and e["type"] == "PRODUCES"}
            pending -= ready
        assert answer in available
    evidence["example_exam"] = {"id":exam, "tasks":len(tasks), "items":len(group), "principles":len(used), "annotation_links":sum(len(v["principy"]) for v in group.values()), "task_summary":task_summary}
    evidence["example_validation"] = {"node_count":len(nodes), "edge_count":len(edges), "all_references_resolve":True, "routes_reach_goal_with_all_inputs":True, "percent_and_angle_arithmetic_checked":True, "whole_exam_points":sum(t["points"] for t in tasks)}
    result = {
        "schema": "proposal-0.1",
        "scope": "Complete 2025 B structural/annotation projection; two proposed reasoning routes for 15.2 only. Other reasoning and most rubrics are not formalized.",
        "source_note": "Task records from current read-only SQLite snapshot; annotations from rebuilt solutions; this is not the application's active graph.",
        "semantics": {"INPUT_TO":"All inputs to a step are jointly necessary for this recorded application.","HAS_ROUTE":"Alternative accepted method; routes are OR choices, not simultaneous requirements.","ANNOTATED_USES":"Projection of the existing chosen solution annotation, not evidence of student mastery.","SHARES_CONTEXT":"Shared source context, not answer dependency."},
        "nodes": list(nodes.values()), "edges":edges,
    }
    (HERE / "evidence.json").write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+"\n")
    (HERE / "example-exam-graph.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"evidence":str(HERE/'evidence.json'),"example":str(HERE/'example-exam-graph.json'),"checks":evidence['example_validation']},indent=2))


if __name__ == "__main__":
    main()
