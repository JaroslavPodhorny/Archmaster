import { useEffect, useRef, useState } from 'react'
import type { AddressState } from './address'
import { fetchFilterOptions, searchProblems } from './api'
import type {
  FilterName,
  FilterOptions,
  FilterValue,
  OrderBy,
  Problem,
  SearchParams,
  SearchResult,
  SelectedFilters,
  SuccessRange,
} from './types'

const PAGE_SIZE = 50

const NOTHING_SELECTED: SelectedFilters = { years: [], terms: [], skills: [], formats: [], points: [] }
const NO_RANGE: SuccessRange = { min: null, max: null }

/** The first page of a search, and further pages for as long as a problem that should be listed is not. */
async function searchFromStart(
  params: Omit<SearchParams, 'offset'>,
  mustList: string | null,
  signal: AbortSignal,
): Promise<SearchResult> {
  const result = await searchProblems({ ...params, offset: 0 }, signal)
  while (
    mustList &&
    result.problems.length < result.total &&
    !result.problems.some((p) => p.id === mustList)
  ) {
    const more = await searchProblems({ ...params, offset: result.problems.length }, signal)
    if (more.problems.length === 0) break
    result.problems.push(...more.problems)
  }
  return result
}

/** All state of the search: what the user chose and what the backend returned.
 *  It starts from what the page address says (see address.ts). */
export function useProblemSearch(initial: AddressState) {
  const [options, setOptions] = useState<FilterOptions | null>(null)
  const [input, setInput] = useState(initial.q)
  const [q, setQ] = useState(initial.q)
  const [selected, setSelected] = useState<SelectedFilters>(initial.selected)
  const [success, setSuccess] = useState<SuccessRange>(initial.success)
  const [orderBy, setOrderBy] = useState<OrderBy>(initial.orderBy)
  const [problems, setProblems] = useState<Problem[] | null>(null)
  const [total, setTotal] = useState(0)
  const [loadingMore, setLoadingMore] = useState(false)
  const [error, setError] = useState<string | null>(null)
  // The problem named in the address has to be listed by the first search, however far down it is.
  const mustList = useRef(initial.problem)
  // Set while the next page is on its way, so that two requests for it never overlap.
  const fetchingMore = useRef(false)

  useEffect(() => {
    const controller = new AbortController()
    fetchFilterOptions(controller.signal)
      .then(setOptions)
      .catch((e) => {
        if (e.name !== 'AbortError') setError(e.message)
      })
    return () => controller.abort()
  }, [])

  // Search only after the user pauses typing.
  useEffect(() => {
    const timer = setTimeout(() => setQ(input), 250)
    return () => clearTimeout(timer)
  }, [input])

  const params = { q, selected, minSuccess: success.min, maxSuccess: success.max, orderBy, limit: PAGE_SIZE }

  // Any change of the search starts again from the first page.
  useEffect(() => {
    const controller = new AbortController()
    searchFromStart(params, mustList.current, controller.signal)
      .then((r) => {
        mustList.current = null
        setProblems(r.problems)
        setTotal(r.total)
        setError(null)
      })
      .catch((e) => {
        if (e.name !== 'AbortError') setError(e.message)
      })
    return () => controller.abort()
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [q, selected, success, orderBy])

  function loadMore() {
    if (!problems || fetchingMore.current || problems.length >= total) return
    fetchingMore.current = true
    setLoadingMore(true)
    searchProblems({ ...params, offset: problems.length })
      .then((r) => setProblems((current) => [...(current ?? []), ...r.problems]))
      .catch((e) => setError(e.message))
      .finally(() => {
        fetchingMore.current = false
        setLoadingMore(false)
      })
  }

  function toggleFilter(name: FilterName, value: FilterValue) {
    setSelected((current) => {
      const values = current[name]
      const next = values.includes(value) ? values.filter((v) => v !== value) : [...values, value]
      return { ...current, [name]: next }
    })
  }

  function clearFilters() {
    setInput('')
    setSelected(NOTHING_SELECTED)
    setSuccess(NO_RANGE)
  }

  const anyFilter =
    input !== '' ||
    success.min !== null ||
    success.max !== null ||
    Object.values(selected).some((values) => values.length > 0)

  return {
    options, input, setInput, selected, toggleFilter, success, setSuccess, orderBy, setOrderBy,
    problems, total, loadMore, loadingMore, error, anyFilter, clearFilters,
  }
}

export type ProblemSearch = ReturnType<typeof useProblemSearch>
