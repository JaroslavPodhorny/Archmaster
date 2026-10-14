"""Throwaway try-out of backend/core/exam_graph.py on the real data in analysis/data.

    uv run --project backend python backend/try_exam_graph.py check
    uv run --project backend python backend/try_exam_graph.py task M9-2025-B-08
    uv run --project backend python backend/try_exam_graph.py principle KON.VLAST.rovnobeznik
    uv run --project backend python backend/try_exam_graph.py exam "2025 B"
    uv run --project backend python backend/try_exam_graph.py review
    uv run --project backend python backend/try_exam_graph.py candidates
"""
import argparse
import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from backend.core import exam_graph  # noqa: E402

DATA = os.path.join(ROOT, 'analysis/data')

parser = argparse.ArgumentParser()
sub = parser.add_subparsers(dest='command', required=True)
sub.add_parser('check')
sub.add_parser('review')
sub.add_parser('candidates')
sub.add_parser('task').add_argument('id')
sub.add_parser('principle').add_argument('id')
sub.add_parser('exam').add_argument('test')
args = parser.parse_args()

start = time.perf_counter()
try:
    release = exam_graph.load_release(DATA)
except exam_graph.InvalidRelease as e:
    sys.exit(str(e))
took = time.perf_counter() - start


def pct(v):
    return '–' if v is None else f'{v:.1f} %'


if args.command == 'check':
    steps = sum(len(r.steps) for f in release.flows.values() for r in f.routes)
    print(f'valid in {took * 1000:.0f} ms: {len(release.tasks)} tasks, {len(release.principles)} principles, '
          f'{len(release.flows)} tasks with steps ({steps} steps), {len(release.misconceptions)} misconceptions, '
          f'{len(release.unexplained)} unexplained options')
    for test in dict.fromkeys(exam_graph.test_of(t) for t in release.tasks.values()):
        flows = [f for f in release.flows.values() if f.test == test]
        if flows:
            scored = [f.scoring.max_points for f in flows if f.scoring]
            print(f'  {test}: {len(flows)} tasks with steps, {len(scored)} scored, {sum(scored):g} points')

elif args.command == 'task':
    v = exam_graph.task_view(release, args.id)
    print(f"{v['test']} {v['task']} ({v['format']}, {v['points']} b.): {v['description']}")
    for item in v['items']:
        print(f"  {item['item']}: {pct(item['success_pct'])}  key {item['key'] or '–'}  | {item['solution']}")
    for g in v['given']:
        print(f"  {g['id']}: {g['text']}")
    for route in v['routes']:
        print(f"  route {route['id']} ({route['name']})")
        for s in route['steps']:
            answer = f"  → {s['answer']}" if s['answer'] else ''
            reused = f"  (reused by {', '.join(s['reused_by'])})" if s['reused_by'] else ''
            print(f"    {s['id']:4s} [{s['item']:4s}] {', '.join(s['inputs']):12s} {s['principle']['id']:24s} {s['result']}{answer}{reused}")
        for d in route['items']:
            reused = ', '.join(f"{r['step']} from {r['item']}" for r in d['reused'])
            print(f"    {d['item']}: {[p['id'] for p in d['principles']]}"
                  f"{'  reuses ' + reused if reused else ''}"
                  f"{'  missing in list: ' + str(d['missing']) if d['missing'] else ''}"
                  f"{'  only in list: ' + str(d['extra']) if d['extra'] else ''}")
    if v['scoring']:
        print(f"  scoring {v['scoring']}")
    for o in v['options']:
        print(f"  options {o['item']}: " + ', '.join(
            f"{x['option']}{'*' if x['key'] else ''} {x['share']}" + (f" [{x['misconception']}]" if x['misconception'] else '')
            for x in o['options']))

elif args.command == 'principle':
    v = exam_graph.principle_view(release, args.id)
    print(f"{v['name']} ({v['topic']['name']}): {v['tests']} tests, {v['points']:g} points")
    print('  requires:', [p['name'] for p in v['requires']])
    print('  required by:', [p['name'] for p in v['required_by']])
    for s in v['steps']:
        print(f"  step {s['test']} {s['task']} {s['route']} {s['step']} ({s['item']}): {s['result']}")
    for m in v['misconceptions']:
        print(f"  misconception {m['name']}: {[(e['test'], e['item'], e['option'], e['share']) for e in m['evidence']]}")
    print(f"  items: {len(v['items'])}, e.g.", [f"{i['test']} {i['item']}" for i in v['items'][:8]])

elif args.command == 'exam':
    v = exam_graph.exam_view(release, args.test)
    print(f"{v['test']}: {v['points']} points, {v['scored_tasks']} tasks scored, {len(v['principles'])} principles")
    for t in v['tasks']:
        print(f"  {t['task']:2d} {t['format']:5s} {t['points']} b. {pct(t['success_pct']):8s} {t['topic']:10s} "
              f"{'steps' if t['stepped'] else '     '} {t['description']}")
    for s in v['template']:
        top = s['topics'][0]
        print(f"  slot {s['task']:2d}: {top['name']} {top['count']}/{s['tests']}"
              f"{' (fixed)' if s['fixed'] else ''}; area {s['areas'][0]['name']} {s['areas'][0]['count']}")
    print('  most covered:', sorted(v['coverage'], key=lambda c: -c['tests'])[:5])

elif args.command == 'review':
    for r in exam_graph.review_list(release):
        print(' ', r)

elif args.command == 'candidates':
    for c in exam_graph.distractor_candidates(release):
        print(f"  {c['test']} {c['item']:5s} key {c['key']} {c['key_share']:4.1f} % | {c['option']} {c['share']:4.1f} %")
