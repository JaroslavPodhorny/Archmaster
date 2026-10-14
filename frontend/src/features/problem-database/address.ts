// The search as it is written in the page address: /ulohy?skills=VZT.PROC&years=2025&problem=M9-2025-B-15.
// A link from another page can name a search this way, and the page keeps its address up to date,
// so a reload or the browser's Back shows the same list and problem. Parameter names are the API's.

import { FILTER_ORDER } from './labels'
import type { FilterName, OrderBy, SelectedFilters, SuccessRange } from './types'

export type AddressState = {
  q: string
  selected: SelectedFilters
  success: SuccessRange
  orderBy: OrderBy
  /** The problem shown in the detail pane. */
  problem: string | null
}

/** Filters whose values are numbers in the backend's options. */
const NUMERIC: FilterName[] = ['years', 'points']
const ORDERINGS: OrderBy[] = ['newest', 'oldest', 'hardest', 'easiest']

function percent(text: string | null): number | null {
  const n = text === null || text.trim() === '' ? NaN : Number(text)
  return Number.isFinite(n) ? Math.min(100, Math.max(0, n)) : null
}

export function readAddress(query: URLSearchParams): AddressState {
  const selected = {} as SelectedFilters
  for (const name of FILTER_ORDER) {
    const values = query.getAll(name)
    selected[name] = NUMERIC.includes(name) ? values.map(Number).filter(Number.isFinite) : values
  }
  const orderBy = query.get('order_by') as OrderBy
  return {
    q: query.get('q') ?? '',
    selected,
    success: { min: percent(query.get('min_success')), max: percent(query.get('max_success')) },
    orderBy: ORDERINGS.includes(orderBy) ? orderBy : 'newest',
    problem: query.get('problem'),
  }
}

export function writeAddress(state: AddressState): URLSearchParams {
  const query = new URLSearchParams()
  if (state.q.trim()) query.set('q', state.q.trim())
  for (const name of FILTER_ORDER) {
    for (const value of state.selected[name]) query.append(name, String(value))
  }
  if (state.success.min !== null) query.set('min_success', String(state.success.min))
  if (state.success.max !== null) query.set('max_success', String(state.success.max))
  if (state.orderBy !== 'newest') query.set('order_by', state.orderBy)
  if (state.problem) query.set('problem', state.problem)
  return query
}
