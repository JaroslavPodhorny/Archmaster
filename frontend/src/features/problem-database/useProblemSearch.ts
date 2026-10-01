import { useEffect, useState } from 'react'
import { fetchFilterOptions, searchProblems } from './api'
import type {
  FilterName,
  FilterOptions,
  FilterValue,
  OrderBy,
  Problem,
  SelectedFilters,
  SuccessRange,
} from './types'

const PAGE_SIZE = 50

const NOTHING_SELECTED: SelectedFilters = { years: [], terms: [], tags: [], formats: [], points: [] }
const NO_RANGE: SuccessRange = { min: null, max: null }

/** All state of the search: what the user chose and what the backend returned. */
export function useProblemSearch() {
  const [options, setOptions] = useState<FilterOptions | null>(null)
  const [input, setInput] = useState('')
  const [q, setQ] = useState('')
  const [selected, setSelected] = useState<SelectedFilters>(NOTHING_SELECTED)
  const [success, setSuccess] = useState<SuccessRange>(NO_RANGE)
  const [orderBy, setOrderBy] = useState<OrderBy>('newest')
  const [problems, setProblems] = useState<Problem[] | null>(null)
  const [total, setTotal] = useState(0)
  const [loadingMore, setLoadingMore] = useState(false)
  const [error, setError] = useState<string | null>(null)

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
    searchProblems({ ...params, offset: 0 }, controller.signal)
      .then((r) => {
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
    if (!problems || loadingMore) return
    setLoadingMore(true)
    searchProblems({ ...params, offset: problems.length })
      .then((r) => setProblems((current) => [...(current ?? []), ...r.problems]))
      .catch((e) => setError(e.message))
      .finally(() => setLoadingMore(false))
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
