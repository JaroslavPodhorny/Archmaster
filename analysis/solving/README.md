# Solving notes (audit trail)

Raw material from solving every task of the M9 tests, kept so the skill tree can be traced back to the
work it came from. Nothing in the app reads these files; the finished results are in `analysis/data/`.

The tasks were solved with an AI assistant (Claude Code) from images of the booklet pages and checked
against CERMAT's official keys. How the principles were chosen, and why, is in
[../graph_design_spec.md](../graph_design_spec.md).

| File | What it is |
|---|---|
| `raw/YYYY_T.json` | One file per test: for every item, the solution in Czech and the principles it uses, under the working ids used while solving. |
| `raw/vocab.tsv` | The working vocabulary of principles (id and name) as it grew during solving. |
| `consolidate.py` | Mapped the working ids to the final ones and wrote `analysis/data/m9_item_solutions.json` (run once, 2 October 2026). Running it again would overwrite later corrections made with `analysis/topic_tree.py`. |
| `info.py` | Prints a test's catalog rows and its official key as text, to check a solution against. |
| `zoom.py` | Enlarges part of a task's figure when it is too small to read. |

Run from the repository root, e.g.

```sh
uv run --project backend python analysis/solving/info.py 2025 B
```

Corrections to a solution are now made with `analysis/topic_tree.py assign … --solution`, not here.
