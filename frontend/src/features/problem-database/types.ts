// Shapes returned by the problem database endpoints (backend/api/problems.py).

/** A skill of the curriculum tree that one scored item of a problem needs. */
export type ItemSkill = {
  /** "15.2", or the task number when the task has no sub-items. */
  item: string
  skill_id: string
  name: string
  /** The first skill listed for the item. */
  main: boolean
}

/** A skill in the graph of what a problem rests on. */
export type GraphSkill = {
  skill_id: string
  name: string
  /** The name of the topic it belongs to. */
  topic: string
  /** Direct prerequisites; all of them are in the same graph. */
  requires: string[]
  /** An item of the problem needs it itself, not only as a prerequisite of another skill. */
  needed: boolean
}

export type Problem = {
  id: string
  year: number
  term: string
  task: number
  format: string
  points: number
  tags: string[]
  skills: ItemSkill[]
  /** Those skills and everything they rest on, in learning order. */
  skill_graph: GraphSkill[]
  description: string
  text: string
  answer_key: string
  success_pct: number | null
  skipped_pct: number | null
  screenshot_url: string
  solution_url: string
}

export type SearchResult = { total: number; problems: Problem[] }

export type FilterValue = string | number
/** depth is set for skills only: 0 area, 1 topic, 2 skill of the curriculum tree. */
export type FilterOption = { value: FilterValue; label: string; count: number; depth?: number }
export type FilterName = 'years' | 'terms' | 'skills' | 'formats' | 'points'
export type FilterOptions = Record<FilterName, FilterOption[]>
export type SelectedFilters = Record<FilterName, FilterValue[]>

export type OrderBy = 'newest' | 'oldest' | 'hardest' | 'easiest'

export type SearchParams = {
  q: string
  selected: SelectedFilters
  minSuccess: number | null
  maxSuccess: number | null
  orderBy: OrderBy
  limit: number
  offset: number
}

/** Success-rate bounds in percent; null means no bound. */
export type SuccessRange = { min: number | null; max: number | null }
