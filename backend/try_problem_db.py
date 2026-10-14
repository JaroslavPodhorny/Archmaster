"""Throwaway try-out of backend/core/problem_db.py on the real booklets.

    uv run --project backend python backend/try_problem_db.py build
    uv run --project backend python backend/try_problem_db.py search "obdelnik" --skills GEO.ROV --years 2025 2026
    uv run --project backend python backend/try_problem_db.py filters

search opens the screenshots of the listed problems in Preview (macOS);
add --no-open to only print them.
"""
import argparse
import os
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from backend.core import problem_db  # noqa: E402

DB = os.path.join(ROOT, 'backend/data/problems.sqlite')
SHOTS = os.path.join(ROOT, 'backend/data/screenshots')

parser = argparse.ArgumentParser()
sub = parser.add_subparsers(dest='command', required=True)
sub.add_parser('build')
sub.add_parser('filters')
s = sub.add_parser('search')
s.add_argument('query', nargs='?', default='')
s.add_argument('--years', nargs='*', type=int)
s.add_argument('--terms', nargs='*')
s.add_argument('--formats', nargs='*')
s.add_argument('--tags', nargs='*')
s.add_argument('--skills', nargs='*', help='ids from the tree: a skill, a topic or an area')
s.add_argument('--points', nargs='*', type=int)
s.add_argument('--min-success', type=float)
s.add_argument('--max-success', type=float)
s.add_argument('--order', default='newest')
s.add_argument('--limit', type=int, default=10)
s.add_argument('--no-open', action='store_true', help='only print, do not open the screenshots')
args = parser.parse_args()

if args.command == 'build':
    started = time.time()
    n = problem_db.build_database(DB, SHOTS, os.path.join(ROOT, 'References/Matematika'),
                                  os.path.join(ROOT, 'analysis/data'))
    print(f'{n} problems -> {DB} ({time.time() - started:.0f} s)')
elif args.command == 'filters':
    for name, options in problem_db.filter_options(DB).items():
        print(name)
        for o in options:
            print(f"  {o['value']!s:8} {o['count']:4d}  {'  ' * o.get('depth', 0)}{o['label']}")
else:
    result = problem_db.search_problems(
        DB, args.query, args.years, args.terms, args.formats, args.tags, args.skills, args.points,
        args.min_success, args.max_success, args.order, args.limit)
    print(f'{result.total} found, showing {len(result.problems)}')
    for p in result.problems:
        success = f'{p.success_pct:.0f} %' if p.success_pct is not None else '–'
        print(f"{p.id}  {p.points} b  {p.format:6} {success:>5}  {','.join(p.tags):16}  {p.description}")
        print(f'    {os.path.join(SHOTS, p.screenshot)}')
    if result.problems and not args.no_open:
        subprocess.run(['open'] + [os.path.join(SHOTS, p.screenshot) for p in result.problems])
