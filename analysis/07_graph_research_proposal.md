# Representing CERMAT problems and exams as graphs

Research and design proposal · 4 October 2026 · M9 corpus in the current ArchMaster working tree

**My recommendation is a typed graph whose core is a network of facts and reasoning steps. Each step links to the reusable mathematical principles it applies. An exam joins these problem graphs through its tasks, shared contexts, scoring rules and common principles. Keep student observations and knowledge estimates as a separate layer.**

In ordinary language: store **what is given → what can be done with it → what follows → what answers the question**, including alternative methods. The existing curriculum graph remains the map of principles. It cannot, by itself, represent the reasoning inside every problem.

This is a research proposal, not a change to the application. “Best” means best for ArchMaster's stated purpose: explaining mistakes, finding useful practice, and improving exam results per unit of preparation time. If the only objective were search and filtering, a much simpler graph would win. This review covers the major relevant families, not every graph algorithm ever published. Recommendations and applications to CERMAT below are design judgments; cited publications establish the precedents, not that the proposed system will improve learning.

## What the existing data actually supports

I queried `backend/data/problems.sqlite` read-only, inspected the current schema, both graph designs and solution records, and reran the existing graph audit. The resulting [evidence snapshot](/Users/jarda/Projects/ArchMaster/analysis/graph_research/evidence.json) includes source hashes.

- **20 exams, 320 tasks, 610 annotated items/subitems**, covering 2022–2026. Every stored exam has 16 tasks and 50 maximum points.
- The rebuilt vocabulary has **157 principles**, of which 131 occur in these annotations; 26 are specification-only. There are 131 prerequisite edges, across 7 areas and 23 topics.
- **519 items use several principles; 224 of those have no direct prerequisite edge between their listed principles.** That is 43.2% of the multi-principle items. They can still have perfectly coherent solutions: combining two principles in one problem does not make either a prerequisite of the other.
- The average explicit annotation lists **2.62 principles**. Expanding all prerequisites produces **5.45**. Treating that expansion as observed evidence would more than double the apparent skill coverage.
- **95 of the 131 used principles have no single-principle item** in these annotations; 42 appear in fewer than five items. Absence of isolated items is a warning for diagnosis, not by itself a general impossibility theorem.
- **32 tasks have empty extracted text.** The stored images are necessary input, especially for diagrams and image-only booklets.
- There are another **97 older annotations**, outside the 320-task database. The repository explicitly records that their official keys are unavailable. They should retain that status.

The active problem database still uses the original skill vocabulary, while rebuilt solution annotations use the new one. A proposal must identify the graph release it uses. I did not silently migrate either version. The earlier [graph review](/Users/jarda/Projects/ArchMaster/analysis/06_graph_review.md) identified several of these problems; the counts above were checked again against current files.

I visually inspected the official stored task and key images for **2025 B 15**, **2022 A 12**, and **2026 A 9**, plus the scoring key for **2025 B 11**. The worked designs below are grounded in those checks. This study does not independently re-solve all 610 items or validate their annotations as a diagnostic instrument.

## What successful graph systems teach us

**Euler's bridge problem: preserve the relations that decide the answer.** Abstracting land areas and bridges makes the question depend on connectivity, rather than the appearance of the map. For CERMAT, the useful abstraction is the mathematical relation, such as equal lengths or a percentage base, rather than the location of a label in the picture. Source: [Euler's original bridge paper, archived by the University of the Pacific](https://scholarlycommons.pacific.edu/euler-works/53/). Its historical dating varies between the journal volume and publication date; that distinction is immaterial to the design lesson.

**Google Maps: the right graph depends on the state and objective.** Google's published electric-vehicle routing design uses charging stations and feasible trips, then expands states to represent battery charge. Travel time alone misses charging time. The CERMAT analogue is that the cheapest route depends on the student's available skills and the objective—solve now, learn a method, or prepare efficiently. A skill name alone is not enough to describe the state. Source: [Google Research, EV routing, 2021](https://research.google/blog/addressing-range-anxiety-with-smart-electric-vehicle-routing/).

**Google Maps also separates prediction from route choice.** Its published traffic model represents road segments as nodes and their connections as edges, using graph neural networks to predict travel times. That is a different representation from a conventional intersection/road routing graph. For ArchMaster, keep estimates of difficulty, time and success separate from the mathematical rules. Source: [Google DeepMind, traffic prediction, 2020](https://deepmind.google/blog/traffic-prediction-with-advanced-graph-neural-networks/). These publications describe particular systems, not every part of present-day Maps.

**Facebook: typed relationships make a graph useful.** TAO represents objects and associations in a directed, labelled multigraph; its durable storage uses MySQL. The transferable idea is explicit relationship meanings and predictable local queries. `APPLIES`, `REQUIRES` and `SHARES_CONTEXT` must not collapse into one generic “connected to” relation. Nor does choosing a graph model require choosing a graph database. Sources: [Facebook's TAO engineering account](https://engineering.fb.com/2013/06/25/core-infra/tao-the-power-of-the-graph/) and [the USENIX paper](https://www.usenix.org/conference/atc13/technical-sessions/presentation/bronson).

**Google Search: link structure helps rank candidates.** PageRank used the web's hyperlink structure as a ranking signal. A principle graph can similarly expose influential or widely reused principles. However, centrality measures the authored graph, not a student's likely improvement. Use it to prioritize review or suggest candidates, then evaluate benefit using actual responses. Source: [Brin and Page, the original Google search-engine paper, 1998](https://research.google/pubs/the-anatomy-of-a-large-scale-hypertextual-web-search-engine/).

**Pinterest: relationships plus content improve retrieval.** PinSage combines graph structure, random walks and learned representations to recommend related content. ArchMaster can retrieve structurally similar problems, including different stories using the same method. Similarity is useful for choosing practice; similarity does not establish a prerequisite or guarantee educational benefit. Source: [Ying et al., PinSage, 2018](https://arxiv.org/abs/1806.01973).

**Computation graphs: results have explicit inputs.** TensorFlow graphs represent operations and the values flowing between them. For a worked solution, this gives the right distinction between a reusable operation and its application to particular values. A step needing two inputs must wait for both. Source: [TensorFlow's graph documentation](https://www.tensorflow.org/guide/intro_to_graphs).

**AI planning: distinguish AND from OR.** Some subproblems must all be solved; other branches are alternative ways to reach the same goal. AND/OR search makes this distinction explicit. It maps naturally to “base AND height are needed” versus “use a formula OR decompose the shape.” Source: [Otten and Dechter on AND/OR decomposition and search](https://ojs.aaai.org/index.php/SOCS/article/view/18185).

**Intelligent tutors: observe work, then infer knowledge.** Knowledge tracing models a student's changing knowledge from successive opportunities to apply skills. Learning-space theory represents feasible knowledge states and supports adaptive assessment, including ALEKS. These are closer precedents for ArchMaster than social networks. Sources: [Corbett and Anderson, knowledge tracing](https://link.springer.com/article/10.1007/BF01099821), [Doignon and Falmagne, knowledge and learning spaces](https://arxiv.org/abs/1511.06757). Neither makes an expert-written prerequisite graph a validated student model automatically.

## The modeling approaches worth comparing

These choices sit at different levels. A property graph is a general container; an expression tree, dependency graph or factor graph specifies what some of its contents mean. They can be combined.

**1. A taxonomy tree: area → topic → principle.** Cheapest to author and easiest to browse. Useful for organizing the curriculum and filters. It cannot describe cross-topic prerequisites, alternative methods or intermediate results. Keep it as a navigation view, with topic membership independent of a principle's identity.

**2. A principle prerequisite DAG.** Nodes are principles; edges express reviewed dependencies within a stated scope. Useful for background explanations and candidate learning order. This is close to the existing graph. Its weakness is overgeneralization: a learning preference or a requirement of one variant can become an allegedly universal prerequisite. For example, the current fraction-power/root node requires square roots, although most annotated applications only square fractions. Separate `REQUIRES_IN_SCOPE` from `RECOMMENDED_BEFORE`; validate cycles independently of topic order.

**3. An item–principle bipartite graph, also called a Q-matrix representation.** One node set is items, the other is principles; links record which principles a specified route applies. This is the best inexpensive first layer for coverage, search and exam comparison. It loses the order of reasoning and alternative methods. A single row containing the union of all methods falsely says every method is necessary. A route-specific Q-matrix, or an item–route–principle structure, preserves that distinction. Statistical diagnosis requires appropriate observations and model-specific identifiability checks; see [Gu and Xu on DINA identifiability](https://arxiv.org/abs/1711.03174).

**4. An expression tree or expression DAG.** Leaves are quantities/variables; internal nodes are operators. A DAG can share repeated expressions. Excellent for arithmetic, equation structure and symbolic checking. Store operand roles or order: `a−b` differs from `b−a`. It does not explain where the equation came from, why a geometric theorem applies, or how a drawing is constructed. Graph2Tree is a relevant precedent: quantity-relation graphs encode a word problem and a tree decoder generates a solution expression. Source: [Zhang et al., Graph2Tree, ACL 2020](https://aclanthology.org/2020.acl-main.362/).

**5. A quantity/entity relation graph.** Nodes represent quantities and entities with units, referents and roles; relationships encode comparisons, parts, totals, rates and conditions. This distinguishes “one third fewer than older children” from “one third of all children.” It is particularly useful for diagnosing translation from language to mathematics. A number-only graph loses the base population. Research on typed entities, units, rates and numbers supports this direction: [Hu and Jiang, heterogeneous line graphs for math problems](https://arxiv.org/abs/2208.05645).

**6. A constraint graph or factor graph.** Variables connect to relation nodes such as `x+y=80` or `2y−x=16`. One relation can involve several variables. Deterministic constraints express validity; probabilistic factors express uncertainty. This is strong for systems, geometry and consistency checking, but satisfaction of constraints is not a teaching explanation. The same mathematical problem may support several proofs. Source for the representation and inference framework: [Kschischang, Frey and Loeliger, factor graphs, 2001](https://web.stanford.edu/~montanar/TEACHING/Stat375/papers/sumprod.pdf).

**7. A geometry relation graph.** Points, lines, circles, segments and angles connect through incidence, perpendicularity, parallelism, equality and other predicates. Relation nodes retain all participants: `Perpendicular(lineAB,lineB)` and `On(B,lineB)`. This captures constructions and diagram facts that an equation tree misses. Keep original diagram evidence and distinguish given, derived and visually conjectured relations; do not infer a right angle merely because it looks right. Source: [Lu et al., Inter-GPS, 2021](https://arxiv.org/abs/2105.04165), which combines formalized text/diagram information with theorem-based reasoning.

**8. A solution dependency DAG.** Facts/results feed step instances; steps produce new facts/results. Every step links to its principle applications. This is the highest-value addition for explanations and hints. Its limitation is that one DAG ordinarily records one route. Routine arithmetic may remain inside a meaningful step; there is no need for a universal skill node for every subtraction.

**9. An AND/OR proof hypergraph.** This extends the dependency model: a rule application consumes a set of premises jointly; alternative applications can establish the same result. It naturally represents several solution methods and shared intermediates. It is my recommended semantics for problem reasoning. Implement it with ordinary nodes by making each rule application a `Step` node; a specialized hypergraph database is unnecessary. Human-reviewed, finite routes keep annotation manageable. Do not enumerate every algebraically equivalent rearrangement.

**10. An equality graph, or e-graph.** Groups equivalent expressions and explores transformations efficiently. Useful later for accepting different correct algebraic forms and proposing alternative derivations. It needs domain-aware rules—cancelling `x` requires `x≠0`, for example—and is poor as the primary student-facing model. Source: [the egg project's equality-saturation documentation](https://egraphs-good.github.io/egg/egg/tutorials/index.html).

**11. A probabilistic and temporal student graph.** Latent skill states connect to observed answers, steps, hints and times, with state changing after practice. Bayesian knowledge tracing, diagnostic models, learning spaces and graph-based knowledge tracing are alternatives here. They solve an inference problem rather than a content-representation problem. The historical corpus does not contain the individual response sequences needed to fit and validate a rich model. [DAGKT](https://arxiv.org/abs/2210.15470) also shows why question difficulty and attempts are relevant beyond shared skill tags.

**12. Similarity graphs and learned graph representations.** Items connect by shared principles, quantities, proof structure, text or diagram features. Useful for finding practice, duplicate/template detection and research on transfer. Start with explicit features and a transparent similarity calculation; learn embeddings only when a benchmark justifies them. Nearest neighbors, co-occurrence edges and learned attention are not mathematical implications or causal learning effects.

**13. A state-transition graph or Petri-net-style process model.** Nodes/states encode what is currently available; transitions apply operations. Useful for an interactive tutor with repeated attempts, hints and branching actions. A search state may be a set of established facts rather than one fact. This is more expensive than storing reviewed solutions; unrolling an observed attempt can usually produce a simpler trace. Reserve it for a product that actually needs interactive action planning.

**14. A typed property graph or RDF knowledge graph.** Both can carry the above domain relationships. Property graphs are convenient for application-owned nodes/edges with attributes. RDF triples and named graphs help interchange, shared vocabularies and provenance, at the cost of extra modeling machinery for rich relation instances. Source: [W3C RDF concepts](https://www.w3.org/TR/rdf-concepts/). For this project, choose the meaning of entities and edges first; RDF can be an export if interoperability becomes a concrete requirement.

## The design I would choose

Use **one logical typed graph, exposed through separate views**, with five connected layers. They need not be five databases.

**Exam structure.** `Exam → Task → Item`. A task groups the booklet content; an item is a response target. A `Context` contains a shared passage, table or diagram. A `ScoringRule` maps one or several responses to points. Do not assume every subitem has an independent, additive maximum.

**Problem meaning.** Local entities, quantities, givens and goals. Quantities carry exact values where possible, units, referents and roles. Mathematical expressions can be small ASTs attached to facts instead of exposing every token as a visible node. Geometry uses typed relation records. The original wording and image remain attached as evidence.

**Reasoning.** `Item → Route → Step`. A step consumes facts and produces facts, and links to the principles it applies. A route can contain independent branches that later join. Alternative routes reach the same goal. In the stored proof graph, all input edges of a step mean AND; alternative routes mean OR. A step must explicitly state which formula/rule and bindings justify the result.

**Reusable knowledge.** A stable `Principle` identity, its Czech name, scope, typical misconceptions and reviewed prerequisite relations. A step is an occurrence of using a principle, not the principle itself. “Supplementary angles” exists once; its use to compute 48° and later to write an equation are two applications. The existing 157-node vocabulary is a strong starting point, subject to refinement.

**Learner evidence.** `Attempt`, `ObservedStep`, answer, hint use, elapsed time and review events; separately, versioned knowledge estimates with uncertainty. An observation can support several competing explanations. Student records do not alter the reference proof graph. A misconception label is a hypothesis until supported, not something to assert from one wrong number.

The essential edge vocabulary is small: `HAS_TASK`, `HAS_ITEM`, `SHARES_CONTEXT`, `HAS_ROUTE`, `HAS_STEP`, `INPUT_TO`, `PRODUCES`, `APPLIES`, `SATISFIES`, `SCORED_BY`, `REQUIRES_IN_SCOPE`, and `RECOMMENDED_BEFORE`. Observed evidence and similarity add distinct edge types when used. Avoid a generic relation carrying several incompatible meanings.

Each authored record needs identity, release, source and review status. Use separate answer, reasoning and annotation review fields. Keep stable IDs independent of the current topic path, with aliases for today's IDs. Store split/merge lineage before student histories depend on them. Keep source-backed prerequisite assertions even when a transitive reduction hides them in a display.

The **full graph need not be acyclic**: inverse relations and other typed links can form cycles. A particular proof route's fact dependencies should be acyclic; the scoped prerequisite projection should also pass its own cycle check. Validate each projection under its own rules.

## Three worked examples from your database

### Percentages: 2025 B, item 15.2

The task says there are one third fewer younger children than older children, then asks how many percent more older children there are than younger children. [Problem image](/Users/jarda/Projects/ArchMaster/backend/data/screenshots/M9-2025-B-15.png) · [official key](/Users/jarda/Projects/ArchMaster/backend/data/screenshots/M9-2025-B-15-reseni.png).

Let `Y` be younger and `O` older. The requested base is **Y**, a crucial part of the goal.

Route A has three meaningful applications: interpret the comparison as `Y=(2/3)O`; invert it to `O/Y=3/2`; calculate `(3/2−1)×100%=50%`. It connects directly to the existing principles for fractional comparison, reversing a relation, and percentage difference.

Route B uses proportional parts: represent the older group as `3u` and the younger group as `2u`, then compute the excess `u/(2u)=1/2=50%`. These are proportional units, not an assertion that the camp contains only five children. This route need not explicitly perform an algebraic inversion. Its principle applications should be reviewed on their own merits.

Both reach option **F**, matching the key. The shared context's 80 children is unnecessary for either route. The graph should preserve that context without making every contextual number a required input. Also, the context has 4 instructors, while item 15.3 separately mentions a difference of 4 children. Equal numerals are different quantities and must not be merged.

A 33⅓% response could reflect keeping the older group as the base. It could also be a guess or another error. A useful follow-up asks the student to identify the comparison base or work with the 3:2 representation. The graph localizes a diagnostic question without pretending the answer alone proves a misconception.

### Angles: 2022 A, task 12

The [diagram](/Users/jarda/Projects/ArchMaster/backend/data/screenshots/M9-2022-A-12.png) contains intersecting lines and angles of 60°, 132°, α and 3α. The existing three principle tags have no direct prerequisite edges between them, yet the reasoning is connected:

1. A vertical-angle application establishes the triangle's 60° angle.
2. A supplementary-angle application establishes `180°−132°=48°`.
3. **Both** 60° and 48°, together with the triangle relation, feed the angle-sum application, producing 72°.
4. The straight-angle relation at A produces `3α+α+72°=180°`.
5. Solving gives `α=27°`, option **B**, confirmed by the [key](/Users/jarda/Projects/ArchMaster/backend/data/screenshots/M9-2022-A-12-reseni.png).

The first two calculations can happen independently. Step 3 requires both. Pairwise links from each input directly to “72°” do not encode that conjunction. The step node does. Reusing supplementary angles later does not imply that supplementary angles are a curriculum prerequisite for every triangle-angle problem.

For annotation review, explicitly decide whether the final equation-solving step deserves the existing `ALG.ROV.upravy` application. A trace makes this possible omission visible; the earlier list is not automatically the gold standard.

### Construction: 2026 A, task 9

The [task](/Users/jarda/Projects/ArchMaster/backend/data/screenshots/M9-2026-A-09.png) requires `B∈b`, `AB⊥b`, `C∈c`, and `|BC|=|AB|+2 cm`.

Construct the perpendicular from A to b; its intersection gives B. Construct the circle centered at B with radius `|AB|+2 cm`. Intersect that circle with c, giving C₁ and C₂ in the supplied configuration. Draw and label **both** triangles. The [official key](/Users/jarda/Projects/ArchMaster/backend/data/screenshots/M9-2026-A-09-reseni.png) confirms those two constructions and gives a rubric that also considers precision, labels and extraneous figures.

Here the output is a **set of required geometric solutions**, not one number. C₁ and C₂ are not OR routes from which the student may freely select one: the instruction requires all solutions. The graph must distinguish “alternative methods to complete the task” from “multiple outputs required by the task.” Constraint geometry plus a derivation graph handles this; a simple expression tree does not. I checked the logical construction and the key image, not a newly drawn construction at physical scale.

## How a whole exam becomes a graph

Form the exam from the union of its local problem graphs, identifying only deliberately shared entities. Join them through the exam/task/item hierarchy, common principles, shared contexts and scoring rules. **Do not identify quantities or step instances just because they have the same name or value.** Item IDs must include exam and occurrence scope.

There are three useful projections:

- **Coverage:** items ↔ principles. What does this exam exercise, through the recorded routes? An incidence matrix is often clearer than a force-directed diagram.
- **Reasoning:** item → routes → facts/steps → principles. What exactly connects the givens to the answer? Expand one item at a time.
- **Assessment:** responses → scoring rules → exam total, with separate links to evidence for knowledge estimation. What was earned, and what can reasonably be inferred?

Shared context is not answer dependency. Sibling items may reuse the same passage without using each other's answers. Add a data-dependency edge only when the recorded solution consumes another item's result. Keep any carry-forward scoring policy separate.

The score is `Σ fᵤ(responses used by scoring unit u)`, summing **each scoring unit once**. In **2025 B task 11**, three correct A/N answers earn 4 points; two earn 2; one or none earn 0. Three independent equal-weight item scores cannot reproduce that rule. Task 15 happens to be additive: 2 points for each correct match. Both patterns require a rubric entity. Checked against [task 11's key](/Users/jarda/Projects/ArchMaster/backend/data/screenshots/M9-2025-B-11-reseni.png) and task 15's key.

For a probabilistic prediction, use `E[score]=Σ E[fᵤ(Rᵤ)]`. The expectation of the total is additive, but each joint rubric needs the relevant response distribution; do not assume sibling independence or add the same points once for every associated skill. A skill's “points touched” can be a useful overlapping coverage measure, clearly labelled as non-additive. It is not recoverable points.

The concrete [2025 B example export](/Users/jarda/Projects/ArchMaster/analysis/graph_research/example-exam-graph.json) includes **all 16 tasks, 32 annotated items, 53 used principles and 88 item–principle annotation links**, with two proposed reasoning routes expanded for 15.2. Other items retain their existing textual solutions; most rubrics are source references rather than executable rules. This is a complete structural projection of one exam, not a claim to have formalized every proof. Its maximum points reconcile to 50 and all graph references resolve.

Across exams, shared principles provide stable links; task families/templates can later provide another level. Keep repeated or near-identical problems detectable so evaluation does not accidentally test on a reworded training problem. Preserve exam/year/term metadata and the documented 2024 structure difference instead of hard-coding “task 15 always means percentages.”

## Algorithms this would unlock—and their limits

**Explain and hint:** backward-slice from a goal through a selected route to the next unestablished fact. Reveal a relevant input or rule before the full result. A topological traversal is enough for a reviewed route; a general theorem prover is not required.

**Choose among methods:** compare the available routes using measured time, error likelihood and teaching purpose. Dijkstra or A* only applies after a state/cost model is defined correctly. A shortest path through isolated principles loses AND requirements. Search over fact sets or use AND/OR planning; if subproofs share work, count that work once rather than naïvely summing duplicated branches.

**Find practice:** rank candidates by route-level principle overlap, unfamiliar surface context, suitable difficulty, and freshness. A weighted Jaccard measure can be a transparent baseline. Add text/diagram similarity to identify near duplicates. Common arithmetic should not dominate every recommendation.

**Diagnose:** treat errors as observations with several possible causes. Ask discriminating questions or inspect steps when an answer is ambiguous. Guessing, slips, reading errors and alternate methods matter. Passing a problem does not certify its full prerequisite closure; failing it does not mark all its principles as missing.

**Choose what to study:** optimize for expected future exam improvement under a time budget and uncertainty, using the graph to supply candidates and constraints. A possible experimental objective is expected gain in properly scored held-out exams per minute, with some exploration for diagnosis. That gain must be estimated from intervention data; population success percentages and graph centrality do not provide it.

**Plan learning:** a student's knowledge state contains many skills and degrees of confidence. Even a binary representation over 157 skills has `2^157` possible states before restrictions. Do not materialize that full graph. Begin with a small, calibrated model and local candidate selection. Full learning-space or sequential decision models become worthwhile only if simpler baselines fail demonstrably.

## Three feasible proposals

**A — Minimal coverage graph.** Keep the rebuilt vocabulary, clarify prerequisite semantics, add explicit item identities and scoring rules, and derive item–principle links. Best for searchable practice, exam comparison and low annotation cost. It offers limited reasoning-level diagnosis. Choose this if the immediate product is a question bank.

**B — Typed solution graph, recommended.** Add meaningful fact/step dependencies, route-specific principle applications, alternatives where they change evidence, and provenance. Use quantity and geometry relations when needed. It provides explainable links from a particular problem to a particular gap, while avoiding the cost of a universal solver. Choose this for the stated preparation product.

**C — Formal mathematical and learner model.** Formalize all givens/constraints, generate and verify proofs, add symbolic equivalence tooling, then fit a probabilistic student model and policy. Highest potential for automatic checking and tutoring, but highest authoring, validation and research burden. Choose it for selected domains after B proves useful; making it a prerequisite for launching practice would delay learning from users.

These are incremental options. B retains A; selected parts of C can be introduced without rewriting the whole model. The recommendation is based on fit and implementation burden, not an invented numerical score claiming that one approach is empirically best.

## Storage and a practical next experiment

Keep the current relational storage for the pilot. SQLite supports recursive graph queries, and Python can load typed graph projections for analysis. NetworkX provides directed multigraphs when needed. Sources: [SQLite recursive queries](https://www.sqlite.org/lang_with.html), [NetworkX graph types](https://networkx.org/documentation/stable/reference/introduction.html). This is a prototype recommendation, not a permanent hosting choice or a performance benchmark.

Use typed tables/records for exams, tasks, items, contexts, routes, facts, steps, input/output bindings, principle applications and rubrics. Simple join tables preserve the graph while enforcing references. Avoid one unchecked universal edge table as the only schema. A native graph database can be reconsidered if real multi-hop query needs, scale or operations justify it; the present corpus size alone is not a reason to migrate.

Run a **30-item authoring pilot** covering arithmetic, algebra, word problems, graph/table reading, plane/solid geometry, constructions and patterns. Include shared contexts, partial-credit rules, alternatives and known annotation exceptions. Thirty is a practical review batch, not a statistically justified efficacy-study size. Pick an entire exam as a structural/scoring integration check too.

For each pilot item, produce the source, goal, one reviewed route, material alternatives, step principles and rubric identity. Review whether two annotators agree on meaningful steps and principle applications; adjudicate disagreements before automating expansion. LLM extraction can draft these records but must retain uncertainty. Source images are required wherever text is insufficient.

Use proposed acceptance gates: all references resolve; all retained route inputs are available and routes reach the stated goal; exact arithmetic/units are checked where possible; answer, reasoning and annotation review are separate; alternatives and required output sets are distinguished; exam totals match official rubrics. These are engineering and content gates, not proof of learning impact.

Then collect real student work with route/step evidence. Compare topic-only selection, Q-matrix selection and the solution-graph approach. Evaluate useful mistake localization, calibrated predictions, annotation/maintenance effort and learning improvement on unseen problems. Split by student and by related task family, and use a time-based exam holdout; avoid leakage through shared contexts and near duplicates. For claims about learning improvement, a prospective comparison with equal preparation time is needed. Prediction accuracy alone is insufficient.

The first experiment should answer one concrete question: **does recording the inputs and outputs of meaningful solution steps help us choose a better explanation or next problem than the existing principle list?** If it does, expand. If it does not, simplify the model before investing in graph infrastructure or graph neural networks.

## Deliverables and verification

The [interactive comparison](/Users/jarda/.cursor/projects/Users-jarda-ArchMaster/canvases/cermat-graph-design.canvas.tsx) presents the recommendation, representation options, worked route diagrams, historical lessons and the 2025 B exam projection. The [machine-readable example](/Users/jarda/Projects/ArchMaster/analysis/graph_research/example-exam-graph.json) makes the proposed relationship semantics inspectable. [Evidence and source hashes](/Users/jarda/Projects/ArchMaster/analysis/graph_research/evidence.json) record the corpus audit.

Verification for this study covers the current corpus counts, exam-point reconciliation, example references and route reachability, arithmetic for the percentage/angle examples, and the inspected official images. The example's annotations are proposals requiring independent review. No application files, existing graph data, student data or database contents were changed.

The interactive artifact passes the canvas TypeScript check. Live visual inspection was unavailable because the computer-use tool does not permit inspecting the Codex app; its rendered appearance is therefore not independently verified here.
