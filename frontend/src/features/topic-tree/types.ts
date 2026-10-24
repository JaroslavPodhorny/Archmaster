// Shapes returned by the curriculum tree endpoint (backend/api/topic_tree.py).

/** 1–3 by how often a skill is needed; S = in CERMAT's specification only. */
export type Priority = '1' | '2' | '3' | 'S'
export type Kind = 'procedure' | 'translation' | 'fact' | 'strategy'

/** One scored item of a test that needs a skill. */
export type ItemUse = {
  /** "2025 B 15.2" */
  ref: string
  /** The task the item belongs to, as the problem database names it. */
  problem_id: string
  success_pct: number | null
  /** The skill is the item's main one. */
  main: boolean
}

/** An area ("POC"), a topic ("POC.VYR") or a skill ("POC.VYR.poradi"). The backend sends them
 *  as one list in learning order, parents before their children. */
export type TreeNode = {
  id: string
  parent: string | null
  name: string
  /** Areas 1–4 of CERMAT's specification. */
  spec: number[]
  note: string
  /** Scored items of the 20 tests needing it (for an area or topic: anything under it). */
  items: number
  /** The tasks those items belong to: what the problem database lists for this id. */
  problems: number
  /** Of the 16 standard tests, and of the 8 tests of 2025–2026. */
  tests: number
  recent: number
  /** Per standard test. */
  points: number
  success_pct: number | null

  // Skills only; null, 0 or empty for areas and topics.
  kind: Kind | null
  priority: Priority | null
  /** Direct prerequisites. */
  requires: string[]
  /** Skills resting on it, directly or not. */
  dependents: number
  /** tests, recent and points again, counting the items of the dependents too. */
  reach_tests: number
  reach_recent: number
  reach_points: number
  /** Refs of its three least solved items. */
  hardest: string[]
  /** Items of the tests before 2022 needing it; they count in no number above. */
  older: string[]
  uses: ItemUse[]
}
