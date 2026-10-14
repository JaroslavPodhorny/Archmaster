# Parked: trial of a knowledge graph built from solutions

**This is not the curriculum tree the project works on.** The tree being developed is
`analysis/data/m9_topic_tree.json` with `m9_item_skills.json`, edited through
`analysis/topic_tree.py` and shown at `/strom`.

On 2 October 2026 a second, deeper graph was tried on 38 items: each solution written as
steps, each step naming one node, nodes in three layers (typ, nástroj, základ). The owner
then decided to keep developing the original tree. Nothing here is used by the backend,
the frontend or the tree, and none of its node names or ids exist in the tree.

Do not build on these files, extend them, or cross-reference them unless the owner asks
to resume the experiment.

- `m9_graph_trial.json`: the 93 nodes and 38 decomposed items
- `graph_trial.py`: validates the file and writes `report.md`
- `report.md`: numbers and every item's steps
