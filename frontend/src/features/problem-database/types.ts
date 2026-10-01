// Shapes returned by the problem database endpoints (backend/api/problems.py).

export type Problem = {
  id: string
  year: number
  term: string
  task: number
  format: string
  points: number
  tags: string[]
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
export type FilterOption = { value: FilterValue; label: string; count: number }
export type FilterName = 'years' | 'terms' | 'formats' | 'tags' | 'points'
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
