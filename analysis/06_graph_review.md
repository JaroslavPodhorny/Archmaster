# Review of the M9 knowledge graph

Reviewed 2 October 2026 against the current working tree, including uncommitted work. This is a proposal, not a change to the graph or application.

**Recommendation: keep the rebuilt graph as the starting vocabulary, but treat it as a versioned, reviewable curriculum model. Add a separate representation of item solution steps, and keep student observations and mastery estimates separate from both.** The biggest remaining problem is the meaning and evidence behind the data, rather than the graph database technology or graph layout.

The current implementation is a useful exploration tool. It is not yet a validated model of student knowledge. A model can agree with every official answer and still assign the wrong skills, omit an alternative method, or infer a prerequisite that a student does not actually need.

## What I inspected and verified

I read the design specification, rebuilt and original graph data, solution schema and consolidation code, graph editor, backend statistics and problem database, API tests, and frontend tree/graph components. I computed the following over **all 610 item annotations in the 20 tests from 2022–2026**, using the rebuilt graph:

- 157 principles: 131 used and 26 unused in these annotations; 131 prerequisite edges.
- Both editor checks pass. The rebuilt graph has no redundant transitive prerequisite edges.
- Items list 2.62 principles on average; including prerequisite closure raises that to 5.45, with a maximum of 13.
- 519 items list multiple principles. **224 of those 519 have no direct prerequisite edge between their listed principles.** This measures the induced subgraph defined by the specification, not connections through unlisted nodes.
- **95 of the 131 used principles never appear in a single-principle item.** Sixteen never appear as the first/main principle. Forty-two appear in fewer than five items, including nineteen appearing in only one or two.
- There are no identical nonempty item-incidence columns: no two used principles occur in exactly the same set of these 610 annotations. That is a useful basic check, not proof that a student model will be identifiable or accurate.
- The largest undirected component contains 107 principles; eleven used principles have no edge in either direction. Disconnected principles are not inherently defects.

These are annotation counts, not measurements of students or a certification of mathematical correctness. Reproduce them with [the read-only audit script](/Users/jarda/Projects/ArchMaster/analysis/audit_graph_review.py).

Validation run: **55 backend tests passed; frontend production build and lint passed; old and rebuilt editor checks passed.** Existing tests establish substantial structural and integration consistency. They do not independently validate the mathematical solutions, pedagogical edges, or future mastery inference. Frontend observations below are from code inspection, not a live browser usability test.

I visually checked the stored official booklet/key screenshots for **2022 A task 12** and **2025 B task 15**, and the key screenshots for **2024 C/D item 3.2**. The latter confirm the negative signs recorded in the design notes: −16/5 and −1/30. I did not independently re-solve all 610 items in this review.

## 1. Give each kind of relationship one meaning

The definition in [the specification](/Users/jarda/Projects/ArchMaster/analysis/graph_design_spec.md:76) says that B requires A when B cannot be carried out or understood without A. But [its edge review](/Users/jarda/Projects/ArchMaster/analysis/graph_design_spec.md:303) explicitly retains relationships that are only learning order, or only apply to some variants of a bundled node.

Concrete examples:

- `VZT.POM.neprima → requires VZT.POM.prima` is explicitly described as learning order. It should not automatically imply that every successful inverse-proportion solution demonstrates direct-proportion competence.
- `POC.ZLOM.mocnina` combines powers and roots and requires square roots. The design review says eight of its nine annotated items only square a fraction. The broad node makes the prerequisite too strong for those applications.
- `GEO.ROV.zpetne` covers finding a dimension from area or perimeter, including circles, yet always requires rectangle area and polygon perimeter. Its own note contains several different formulas. Requirements belong to the applicable formula and method.
- `KON.ROZBOR.mnoziny` always requires a circle and a perpendicular bisector, although its definition also covers intersections of other loci. A general construction strategy should not make every listed construction operation compulsory in each application.

**Proposed minimum:** keep `prerequisite` for a reviewed requirement within an explicit scope, and `recommended_before` for a teaching preference. Put method-specific requirements on item solution steps. Keep taxonomy membership separate. Start with these distinctions rather than adding a large vocabulary of edge types.

For every retained prerequisite record its rationale, scope, supporting examples, a counterexample check, review status, and reviewer. Ask: “Can someone perform B, in the stated scope, without A?” A plausible counterexample triggers review; co-occurrence does not establish necessity. Even an expert-approved curriculum prerequisite is not an automatic rule for updating a student's mastery.

Validate cycles in the prerequisite graph itself. The present requirement that prerequisites appear earlier in a nested topic tree conflates topic presentation with dependency order. Compute a topological order for the graph and keep a separate order for browsing topics.

Do not add edges just to connect isolated nodes or make a task diagram look complete. Likewise, “not observed in these tests” should not prohibit valid prerequisite links for specification-covered principles.

## 2. A task needs a solution trace as well as a curriculum subgraph

The current solution record contains only `reseni` and an ordered `principy` list. The list tells us which principles one chosen solution uses. The prerequisite graph tells us how principles are related in the curriculum. Neither tells us which intermediate result feeds which next step.

The 224 edge-free, multi-principle item subgraphs make this distinction visible. Those tasks combine principles without establishing a general prerequisite relationship between them.

**Verified example: 2022 A task 12.** The annotations list `GEO.UHLY.vedlejsi`, `GEO.UHLY.trojuhelnik`, and `VZT.SLOV.rovnice`. None has a direct prerequisite edge to another of those three. Yet the solution has a clear flow:

1. Use vertical/supplementary angles to obtain triangle angles 60° and 48°.
2. Use the triangle angle sum to obtain 72°.
3. Use the straight angle at A to write `3α + α + 72° = 180°`.
4. Obtain `α = 27°`, matching answer B in the official key.

Store those as **step instances** with inputs, output, and principle references. The same principle may occur in multiple steps. An edge between steps means “uses this earlier result”; it must not become a new curriculum prerequisite. Routine arithmetic can remain in the step text without becoming a separate node.

At minimum, an item should have a stable item ID, source references, scoring rubric reference, one or more accepted solution routes, and a review status. A route should have an ID, steps, final answer, and route-specific principle applications. A step should have its ID, statement/result, input step IDs, and principle IDs. Derive the item–principle index from these applications.

The current rule to keep only the “most natural” solution is reasonable for a worked explanation, but insufficient for diagnosis. Preserve materially different routes where they change what is evidenced. For **2025 B 15.2**, both `younger = 2/3 × older` followed by inversion and a representative group of three older/two younger children yield 50%. A reviewer should decide the principle applications for each route; a student's arithmetic route must not be scored as evidence that they solved an equation they never wrote.

Do not enumerate every algebraically equivalent calculation. Add a route when it changes the relevant principles, intermediate evidence, or teaching response. For an answer-only attempt with unknown route, keep route uncertainty rather than crediting the union of all routes. Shared principles across reviewed routes can be useful, but are only shared across the routes recorded so far.

## 3. Make uncertainty and provenance part of the data

[The design notes](/Users/jarda/Projects/ArchMaster/analysis/graph_design_spec.md:317) already disclose important limits:

- Seven item answers were taken from the official key rather than independently worked out: 2022 D 11.1–11.3; 2023 D 8.1; 2025 B 13; 2026 B 13; 2025 A 11.3.
- The 97 older item solutions have no official key available in the repository; their scored-item boundaries are also uncertain in some cases.
- Construction solutions were reasoned about but not drawn.
- Skill assignment comes from one solver's judgment.

Those disclosures are valuable. They are currently absent from the machine-readable solution records, which all have the same two fields. A nonempty solution and agreement between two copies of the skill list are not a record of independent verification.

Record separate states for **answer verification**, **solution reasoning review**, and **principle annotation review**. For example, an answer may be `key_matched` while its reasoning is `key_derived` and its annotation is `unreviewed`. An older answer may be `no_key_available`; a diagram-dependent solution may require visual review. Avoid one vague “confidence: 0.95” supplied by the generating model.

Preserve source PDF identity/hash, page and task/item location, key/rubric location, model/version and prompt version where known, generation time, and actual review events. Historical values that were not recorded should remain unknown. Preserve the current raw notes as immutable generation evidence; they are not another editable authority.

Use a second pass that solves selected tasks without seeing the first solution or key, then compares the result to the key and reviews the annotations separately. Escalate disagreements and geometry/construction cases to a qualified mathematics reviewer. A second model is useful for finding disagreements, not sufficient proof by itself.

Correct final answers validate an outcome. They do not by themselves validate the intermediate reasoning, coverage of legitimate routes, or the psychological meaning of a skill.

## 4. Define principles by what can be taught and assessed

The current size is a reasonable starting point; I would not target a larger or smaller node count. Keep the separation of fraction operations, equation transformations, translation from text, and geometry principles reused across constructions and calculations.

For every principle, add a short observable definition: what the student can do, conditions in which it applies, inclusions/exclusions, a worked example, a near-miss/nonexample, and diagnostic prompts. Preserve the Czech terminology. Separate typical errors from the mathematical definition so an error can point to evidence and a teaching response.

Split a node when its parts can fail independently **and** the distinction changes assessment or instruction. Squaring versus taking a root of a fraction is an immediate candidate because it already causes incorrect scope in prerequisites. Multiplication versus division of fractions is another candidate to test, not an automatic split. Keep “equivalent transformations” together unless real student evidence justifies a finer distinction.

Separate knowing a formula, choosing it in context, and executing the calculation when diagnostic evidence supports that distinction. For example, knowing `S = av/2` does not establish that a student can locate an exterior altitude. Difficulty often belongs to an item/application context—unusual diagram, unfamiliar wording, number types, number of steps—not to a globally “hard” principle.

The “never list whole-number arithmetic” rule is a deliberate boundary, not evidence that every student has it. State the assumed baseline explicitly and allow a small foundation diagnostic if unexplained errors recur. There is no need to expand the entire primary-school curriculum now.

Use the official specification as a separate coverage check. A principle absent from one chosen route is not necessarily absent from all legitimate approaches or from the exam scope. “Specification-only” should be an explicit coverage status supported by a precise specification reference, not merely inferred from zero annotations.

## 5. Keep student evidence separate from mastery estimates

**A failed three-principle task does not establish three missing principles. A correct answer does not establish mastery of every ancestor.** The 95 principles with no single-principle item highlight the need for discriminating evidence, but do not mathematically prove that diagnosis is impossible: combinations across items and observed steps can distinguish skills too.

The frontend currently says [“zvládnout tyto úlohy = dovednost je zvládnutá”](/Users/jarda/Projects/ArchMaster/frontend/src/features/topic-tree/components/NodeDetail.tsx:162) underneath its hardest items. Replace this with a narrower statement such as “Náročné úlohy využívající tuto dovednost.” Selecting three low-success items is not a mastery criterion.

For each attempt, retain the item and graph release, response, awarded score/rubric outcome, observed steps if available, hints, whether the solution was already seen, and timestamp. Record observed evidence first. Derived mastery state can then be recomputed under a specified model version.

Initially show “insufficient evidence,” “observed difficulty,” and “repeated independent success,” with the supporting attempts. Define these labels explicitly; do not present arbitrary percentages as calibrated probabilities. Use short follow-up questions to distinguish plausible causes of an error—for example, angle relationship recognition versus equation setup in task 12.

When there is enough longitudinal student data, compare a simple baseline with an appropriate probabilistic model. Knowledge tracing explicitly accounts for correct guesses and incorrect slips; its parameters require evidence rather than arbitrary confidence propagation. See [Beck and Sison's research discussion of knowledge tracing](https://www.cs.cmu.edu/~listen/pdfs/Beck%20Sison%202006%20jaied%20extended%20version.pdf). The research is from a different learning domain; it supports the distinction between observations and latent knowledge, not a validated CERMAT implementation.

Whether an item–skill design can support particular diagnostic estimates depends on the model and the item design. [Gu and Xu (2021)](https://www3.stat.sinica.edu.tw/statistica/j31n1/j31n118/j31n118.html) formalize that identifiability problem. This is why a plausible skill graph should be evaluated with student responses, rather than treated as psychologically established by expert or AI annotation alone.

## 6. Describe the statistics honestly

[The backend statistics](/Users/jarda/Projects/ArchMaster/backend/core/topic_tree.py:123) are descriptive summaries of annotated items. They are useful, but several distinctions need to be visible:

- `success_pct` is a points-weighted summary of published item outcomes, not “the percentage of students who know this principle.” It mixes item contexts and response/scoring types; report those limits, the item count, cohort/year scope, and missing coverage.
- `points` counts the full annotated item's points for every principle it uses. Values across principles overlap and must not be added. A/N bundle points are allocated equally to statements in the catalog; that is an analytical allocation, not an independently scored value for each statement.
- `reach_points` includes items attached to downstream principles. It measures graph reach under the current edge assumptions, not expected points gained from teaching this node.
- Priority uses hand-set frequency thresholds and downstream reach. This is an exam-coverage heuristic, not an optimal learning plan.
- Frequency/points exclude 2024, while the success-rate calculation includes available regular-term items from that year. The cohorts should be named explicitly and configurable from release metadata. This review did not re-establish the repository's rationale for excluding 2024.

The sensitivity is visible: `POC.DEL.delitele` has about **0.19 directly associated points per standard test**, but **16.04 reach points**. That is not a bug in summation; it shows why downstream reach should not be presented as a causal return from teaching divisors.

Use labels such as “body úloh využívajících princip” and “průměrná úspěšnost přiřazených položek.” Keep direct coverage, prerequisite reach, observed item difficulty, and student evidence separate. Select practice based on the student's observed gaps and the information another attempt would provide; evaluate actual improvement before promising time efficiency.

## 7. Make releases consistent across the editor, API, and database

The plain Python core, thin FastAPI endpoints, JSON authoring, and local SQLite are appropriate for this scale. A dedicated graph database would not solve the current semantic or provenance problems.

Several concrete changes are needed before student history relies on this model:

1. **Immutable principle identity.** IDs currently encode taxonomy; moving a node rewrites its ID in [the editor](/Users/jarda/Projects/ArchMaster/analysis/topic_tree.py:152), and depth is inferred from dots in both backend and frontend. IDs should survive a topic move. Existing strings can be frozen as identities; opaque replacements are optional. Store `node_type`, taxonomy membership, and display slug separately. Record splits, merges and replacements explicitly; never blindly copy mastery to every child of a split.
2. **One authoring direction.** Solutions are declared the source of assignments, but [the editor copies assignments back into solutions](/Users/jarda/Projects/ArchMaster/analysis/topic_tree.py:132), while [consolidation rewrites solutions from raw notes](/Users/jarda/Projects/ArchMaster/analysis/solving/consolidate.py:51). A later rerun can overwrite curated work. Make raw ingestion propose a diff; curate solution applications; generate flat indexes and displays one way.
3. **An explicit release ID and content hash.** Old/new selectors identify two models, not immutable revisions. Pin graph, solutions, annotations, sources and build rules in a release manifest. Carry its ID through API responses, database metadata, frontend cache keys, and future attempts.
4. **The same release across features.** [The tree API](/Users/jarda/Projects/ArchMaster/backend/api/topic_tree.py:14) reads live JSON while [database builds](/Users/jarda/Projects/ArchMaster/backend/core/problem_db.py:124) snapshot only the old graph. The new-tree warning is honest, but an item opened from it currently shows the old task graph. Preserve the old version for comparison, and make every link/filter/problem graph select an explicit matching release.
5. **Per-item and per-route graphs.** [The current problem graph](/Users/jarda/Projects/ArchMaster/backend/core/problem_db.py:257) unions all subitems and adds prerequisite closure. Keep a task overview, but default diagnosis to the selected subitem and route, with actual applications distinct from optional background prerequisites. Serve the solution trace too.
6. **Validated, atomic publication.** Move the graph/schema validator into the reusable core and call it before serving or publishing a release, not only in the editor. Reject missing references and prerequisite cycles; validate solution-step dependencies separately. The editor currently writes several files sequentially, and the database builder deletes the current DB before completing a new build. Stage a complete release, validate it, then switch the active manifest/database atomically. Enable SQLite foreign-key enforcement on write connections and check integrity before promotion. This is a robustness risk, not evidence of current data loss.

Keep authored rationales even if a direct edge becomes transitively redundant. A reduced edge set is a convenient display; an evidence record should not be erased merely because another path now implies the same reachability.

## 8. Make the graph useful for inspection

Build on the existing dense panes and Czech labels. The current code already scrolls a selected node into view; it is inaccurate to treat that feature as entirely missing. However, search primarily fades nonmatching graph nodes, and related-only mode hides nodes without recomputing a compact layout.

The most useful next views are:

- **Principle focus:** the selected principle, one-hop reviewed prerequisites and dependents by default, with explicit expansion. Show edge meaning and evidence on selection. Do not start by exposing the entire 107-node component.
- **Item explanation:** the problem image, subitem selector, solution route, step flow, and linked principles. Selecting a step highlights its principle applications. Background prerequisites are a separately labelled optional expansion.
- **Review queue:** disputed edges, unreviewed solutions, unsupported annotations, rare principles, ambiguous definitions and missing diagnostic evidence, ordered by impact and review status. This directly improves the core data.

Search should list and navigate to matches; URLs should preserve the release, selected item/route and relevant filters. Keep keyboard navigation and full readable labels. Offer taxonomy overview for browsing and graph focus for dependency inspection. Showing more edges should not be the measure of a better interface.

## A small implementation sequence

**First: a trustworthy vertical slice.** Use a proposed pilot of roughly 30 varied items, including 2022 A 12, 2025 B 15.2, a fraction-power/root case, construction cases, and the seven key-derived items. This is a design/review pilot, not a statistically sufficient mastery study.

For that pilot, establish the principle/edge meanings, preserve stable IDs, record review statuses and source references, annotate solution steps and materially different routes, derive the principle index, and serve item details under one release. Show the source, reasoning, annotations and unresolved decisions together for review. Draft the changed UI before implementing it, as the project guidance requests.

**Second: validate and migrate the corpus.** Review all 131 existing edges under the clarified semantics, adjudicate the pilot's annotation disagreements, then extend the schema across the 610 annotations without silently labelling them verified. Keep the old graph as an archived comparison. Prioritize high-reach disputed edges and the acknowledged solution exceptions, then complete mathematical/annotation review before treating a release as fully reviewed.

**Third: test whether it explains students.** Gather a modest formative sample of real student work and think-aloud solutions to discover missing methods and misleading node boundaries. Add short discriminating probes where causes remain ambiguous. Later evaluate prediction and diagnosis on held-out students and task families, and compare preparation outcomes against a simple topic-based baseline. The size of a useful quantitative study depends on the chosen model and observed variability; 20 historical tests are not 20 independent student-learning experiments.

Suggested release gates:

- Every published item has a source and scoring-unit identity; every claimed reviewed answer, reasoning trace and annotation has its own review evidence.
- All graph and step references resolve; prerequisite and step-dependency cycles are rejected; alternatives remain alternatives.
- The annotation index is reproducibly derived; rebuilding the same release preserves its identity and outputs.
- Tree, item API, filters and links agree on release and item-level membership. Integration tests cover the rebuilt release, not only the original tree.
- Moving a principle between topics preserves its identity and historical references. Split/merge migrations retain lineage and require explicit treatment of student estimates.
- Diagnostics represent ambiguous evidence as ambiguous; there is no automatic mastery propagation from an item result or prerequisite closure.

**The next investment should be one inspectable, versioned path from an official item through a reviewed solution to its principle applications.** That gives you something concrete to test for accuracy and usefulness before building student tracking on top of it.
