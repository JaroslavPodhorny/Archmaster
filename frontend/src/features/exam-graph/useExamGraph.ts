import { useEffect, useMemo, useState } from 'react'
import { useSearchParams } from 'react-router'
import { fetchExam, fetchIndex, fetchPrinciple, fetchReview, fetchTask } from './api'
import { VIEWS, fold, testFromAddress, testToAddress } from './labels'
import type { Index, ReviewEntry, TaskEntry, View } from './types'

/** What narrows the task list. */
export type TaskFilters = {
  q: string
  /** Only tasks that have a solution flow. */
  steppedOnly: boolean
  /** Only tasks with an open question for the owner. */
  reviewOnly: boolean
}

const NO_FILTERS: TaskFilters = { q: '', steppedOnly: false, reviewOnly: false }

/** What the address holds: the view and what each view shows. */
type Place = { view: View; task: string; route: string; node: string; test: string }

/** Details fetched by id and kept, so returning to a task, principle or test is immediate. */
function useDetail<T>(id: string | null, fetcher: (id: string, signal: AbortSignal) => Promise<T>) {
  const [known, setKnown] = useState<ReadonlyMap<string, T>>(new Map())
  const [failed, setFailed] = useState<{ id: string; message: string } | null>(null)
  const missing = id !== null && !known.has(id)

  useEffect(() => {
    if (!missing || id === null) return
    const controller = new AbortController()
    fetcher(id, controller.signal)
      .then((value) => setKnown((map) => new Map(map).set(id, value)))
      .catch((e) => {
        if (e.name !== 'AbortError') setFailed({ id, message: e.message })
      })
    return () => controller.abort()
  }, [id, missing, fetcher])

  return { value: id === null ? null : (known.get(id) ?? null), error: failed && failed.id === id ? failed.message : null }
}

/** Newest tests first; within a year the terms in order, within a test the tasks in order. */
function byRecency(a: TaskEntry, b: TaskEntry): number {
  return b.test.slice(0, 4).localeCompare(a.test.slice(0, 4)) || a.test.localeCompare(b.test) || a.task - b.task
}

/** All state of the page. The address holds the view and what each view shows
 *  (/graf?view=uloha&task=M9-2025-B-08&route=hlavni, view=princip&node=…, view=zkouska&test=2025-B); what one
 *  view selected stays when another is shown, so switching back returns to it. The task list's filters are
 *  state of this page only. */
export function useExamGraph() {
  const [address, setAddress] = useSearchParams()
  const [index, setIndex] = useState<Index | null>(null)
  const [review, setReview] = useState<ReviewEntry[] | null>(null)
  const [error, setError] = useState<string | null>(null)
  const [filters, setFilters] = useState(NO_FILTERS)

  useEffect(() => {
    const controller = new AbortController()
    Promise.all([fetchIndex(controller.signal), fetchReview(controller.signal)])
      .then(([i, r]) => {
        setIndex(i)
        setReview(r)
      })
      .catch((e) => {
        if (e.name !== 'AbortError') setError(e.message)
      })
    return () => controller.abort()
  }, [])

  const tasks = useMemo(() => new Map(index?.tasks.map((t) => [t.id, t])), [index])
  const principles = useMemo(() => new Map(index?.principles.map((p) => [p.id, p])), [index])
  const groups = useMemo(() => new Map(index?.groups.map((g) => [g.id, g])), [index])

  const asked = address.get('view') as View
  const view: View = VIEWS.includes(asked) ? asked : 'uloha'
  // Without a task in the address the first one with steps is shown; without a principle, the main
  // principle of that task; without a test, the task's test.
  const task = tasks.get(address.get('task') ?? '') ?? index?.tasks.find((t) => t.stepped) ?? index?.tasks[0] ?? null
  const node = principles.get(address.get('node') ?? '') ?? principles.get(task?.main ?? '') ?? null
  const askedTest = testFromAddress(address.get('test') ?? '')
  const test = index?.tests.includes(askedTest) ? askedTest : (task?.test ?? null)

  const taskDetail = useDetail(view === 'uloha' ? (task?.id ?? null) : null, fetchTask)
  const principleDetail = useDetail(view === 'princip' ? (node?.id ?? null) : null, fetchPrinciple)
  const examDetail = useDetail(view === 'zkouska' && test ? testToAddress(test) : null, fetchExam)
  const routes = taskDetail.value?.routes ?? []
  const route = routes.find((r) => r.id === address.get('route')) ?? routes[0] ?? null

  /** Shows another place; what is not named stays. `push` adds a step to the browser's history. */
  function go(next: Partial<Place>, push = true) {
    const params = new URLSearchParams(address)
    if (next.task && next.task !== task?.id && next.route === undefined) params.delete('route')
    for (const [name, value] of Object.entries(next)) {
      if (value) params.set(name, value)
      else params.delete(name)
    }
    if (next.test) params.set('test', testToAddress(next.test))
    setAddress(params, { replace: !push })
  }

  const reviewByTask = useMemo(() => {
    const out = new Map<string, ReviewEntry[]>()
    for (const entry of review ?? []) {
      if (!('problem_id' in entry)) continue
      out.set(entry.problem_id, [...(out.get(entry.problem_id) ?? []), entry])
    }
    return out
  }, [review])

  const taskRows = useMemo(() => {
    const needle = fold(filters.q.trim())
    return (index?.tasks ?? [])
      .filter(
        (t) =>
          (!filters.steppedOnly || t.stepped) &&
          (!filters.reviewOnly || reviewByTask.has(t.id)) &&
          (needle === '' || fold(`${t.test} ${t.task} ${t.description}`).includes(needle)),
      )
      .sort(byRecency)
  }, [index, filters, reviewByTask])

  return {
    index, review, error, view, task, node, test, route, tasks, principles, groups,
    taskDetail, principleDetail, examDetail, reviewByTask, filters, setFilters, taskRows,
    clearFilters: () => setFilters(NO_FILTERS),
    go,
    setView: (next: View) => next !== view && go({ view: next }),
  }
}

export type ExamGraph = ReturnType<typeof useExamGraph>
