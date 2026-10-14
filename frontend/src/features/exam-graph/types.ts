// Shapes returned by the exam graph endpoints (backend/api/exam_graph.py, backend/core/exam_graph.py).

/** The three views of the page, as the address names them. */
export type View = 'uloha' | 'princip' | 'zkouska'

/** A task of the 20 tests, as the task list shows it. */
export type TaskEntry = {
  /** M9-2025-B-08, as the problem database names it */
  id: string
  /** "2025 B" */
  test: string
  task: number
  format: string
  points: number
  description: string
  success_pct: number | null
  items: number
  /** It has a solution flow (steps). */
  stepped: boolean
  /** The main principle of its first item. */
  main: string | null
}

/** A principle of the rebuilt tree. */
export type PrincipleEntry = {
  id: string
  name: string
  /** POC.ZLOM */
  topic: string
  /** POC */
  area: string
  requires: string[]
  /** Items that need it. */
  items: number
}

/** An area (no parent) or a topic. */
export type Group = { id: string; name: string; parent: string | null }

export type Index = { tests: string[]; tasks: TaskEntry[]; principles: PrincipleEntry[]; groups: Group[] }

export type PrincipleRef = { id: string; name: string; topic: string }

/** One step of a route: it uses given facts and earlier results (all together), applies one principle
 *  and produces a result. */
export type Step = {
  id: string
  inputs: string[]
  result: string
  /** The item this step answers. */
  answer: string | null
  /** The item it belongs to: the first whose answer depends on it. */
  item: string
  /** Later items that use its result. */
  reused_by: string[]
  principle: PrincipleRef
}

/** What a route says about one item, all derived from the steps. */
export type ItemSteps = {
  item: string
  steps: string[]
  reused: { step: string; item: string }[]
  principles: PrincipleRef[]
  /** Applied by a step, missing in the stored list. */
  missing: string[]
  /** In the stored list, applied by no step the item depends on. */
  extra: string[]
  /** In the stored list, applied only by a step the item reuses from an earlier item. */
  extra_reused: string[]
}

export type Route = { id: string; name: string; steps: Step[]; items: ItemSteps[] }

export type TaskItem = {
  item: string
  points: number
  success_pct: number | null
  /** The key option of a closed item. */
  key: string | null
  /** The stored solution line. */
  solution: string
  /** The stored principle list, main first. */
  stored: PrincipleRef[]
}

export type OptionShare = {
  option: string
  share: number
  key: boolean
  /** The misconception this wrong option reveals. */
  misconception: string | null
  /** Why no misconception was named for it. */
  unexplained: string | null
}

export type ItemOptions = { item: string; key: string | null; options: OptionShare[] }

export type Evidence = {
  test: string
  item: string
  option: string
  share: number
  key: string | null
  key_share: number | null
  problem_id: string
}

export type Misconception = {
  id: string
  name: string
  description: string
  state: 'navrh' | 'zkontrolovano'
  /** The principle it corrupts. */
  principle: PrincipleRef
  evidence: Evidence[]
}

export type Scoring = {
  /** soucet: points per item; pocet-spravnych: points by the number of correct items */
  kind: 'soucet' | 'pocet-spravnych'
  points: Record<string, number>
  max_points: number
  /** Points the key gives for an intermediate result. */
  partial: { item: string; step: string; points: number }[]
  /** The key's other rules in words. */
  note: string
}

export type ReviewState = {
  answers: 'shoda-s-klicem' | 'prevzato-z-klice' | 'bez-klice'
  steps: 'navrh' | 'zkontrolovano'
  principles: 'navrh' | 'zkontrolovano'
  notes: string[]
}

export type TaskDetail = {
  id: string
  test: string
  task: number
  format: string
  points: number
  description: string
  success_pct: number | null
  skipped_pct: number | null
  screenshot: string
  key_screenshot: string
  items: TaskItem[]
  stepped: boolean
  given: { id: string; text: string }[]
  routes: Route[]
  scoring: Scoring | null
  review: ReviewState | null
  options: ItemOptions[]
  misconceptions: Misconception[]
}

export type PrincipleStep = {
  problem_id: string
  test: string
  task: number
  route: string
  route_name: string
  /** The step belongs to the task's first route, not to an alternative. */
  main_route: boolean
  step: string
  result: string
  item: string
}

export type PrincipleItem = {
  test: string
  item: string
  problem_id: string
  success_pct: number | null
  points: number
  /** It is the first of the item's stored list. */
  main: boolean
  /** Where the item's list comes from: its task's steps, or the stored list. */
  source: 'kroky' | 'seznam'
  in_steps: boolean
  in_list: boolean
}

export type PrincipleDetail = {
  id: string
  name: string
  note: string
  kind: string
  topic: { id: string; name: string }
  area: { id: string; name: string }
  requires: PrincipleRef[]
  required_by: PrincipleRef[]
  misconceptions: Misconception[]
  steps: PrincipleStep[]
  items: PrincipleItem[]
  tests: number
  points: number
}

export type Slot = {
  task: number
  tests: number
  /** One topic fills it in at least 60 % of the tests. */
  fixed: boolean
  topics: { id: string; name: string; count: number }[]
  areas: { id: string; name: string; count: number }[]
}

export type Coverage = { id: string; tests: number; items: number; points: number }

export type ExamRow = {
  task: number
  item: string
  problem_id: string
  points: number
  success_pct: number | null
  source: 'kroky' | 'seznam'
  principles: string[]
  main: string | null
}

export type ExamDetail = {
  test: string
  tasks: {
    task: number
    id: string
    format: string
    points: number
    description: string
    success_pct: number | null
    topic: string | null
    stepped: boolean
  }[]
  points: number
  scored_tasks: number
  rows: ExamRow[]
  /** The principles the test needs, in learning order. */
  principles: string[]
  template: Slot[]
  coverage: Coverage[]
}

/** One open question for the owner. */
export type ReviewEntry =
  | {
      kind: 'rozdil-principu'
      problem_id: string
      ref: string
      missing: string[]
      extra: string[]
      extra_reused: string[]
      reused: { step: string; item: string }[]
    }
  | { kind: 'odpoved'; problem_id: string; ref: string; state: string }
  | { kind: 'poznamka'; problem_id: string; ref: string; text: string }
  | { kind: 'chyba'; id: string; name: string; refs: string[] }
  | { kind: 'nevysvetleno'; problem_id: string; ref: string; text: string }
  | { kind: 'neprozkoumano'; problem_id: string; ref: string; share: number; key_share: number }
  | { kind: 'kroky'; problem_id: string; ref: string }
