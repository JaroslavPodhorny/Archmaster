import { getJson } from '../../shared/http'
import type { FilterOptions, SearchParams, SearchResult } from './types'

export function fetchFilterOptions(signal?: AbortSignal): Promise<FilterOptions> {
  return getJson('/api/problems/filters', signal)
}

export function searchProblems(params: SearchParams, signal?: AbortSignal): Promise<SearchResult> {
  const query = new URLSearchParams()
  if (params.q.trim()) query.set('q', params.q.trim())
  for (const [name, values] of Object.entries(params.selected)) {
    for (const value of values) query.append(name, String(value))
  }
  if (params.minSuccess !== null) query.set('min_success', String(params.minSuccess))
  if (params.maxSuccess !== null) query.set('max_success', String(params.maxSuccess))
  query.set('order_by', params.orderBy)
  query.set('limit', String(params.limit))
  query.set('offset', String(params.offset))
  return getJson(`/api/problems?${query}`, signal)
}
