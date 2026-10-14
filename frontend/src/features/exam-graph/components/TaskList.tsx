import { useEffect, useRef, type KeyboardEvent } from 'react'
import { focusRing, hint, link, message, rowHover, selectedRow } from '../../../shared/controls'
import { pointsLabel, successLabel, taskCountLabel, testName } from '../labels'
import type { TaskEntry } from '../types'
import type { ExamGraph } from '../useExamGraph'

const row = `grid w-full cursor-pointer gap-y-0.5 rounded-xl px-3 py-2.5 text-left ${focusRing}`

/** The tasks of the 20 tests, newest test first, under a heading per test; the meta line says which have
 *  steps and which have open questions. Arrow keys walk the list. */
export function TaskList({ graph, onPick }: { graph: ExamGraph; onPick: () => void }) {
  const { taskRows, task, reviewByTask } = graph
  const selectedRef = useRef<HTMLButtonElement>(null)
  const byKeyboard = useRef(false)
  const total = graph.index?.tasks.length ?? 0
  const stepped = graph.index?.tasks.filter((t) => t.stepped).length ?? 0
  const filtering = graph.filters.q.trim() !== '' || graph.filters.steppedOnly || graph.filters.reviewOnly

  // A row reached by a link or the address comes to the middle of the list; one reached by the keys just into view.
  useEffect(() => {
    const el = selectedRef.current
    const pane = el?.closest('[data-list]')
    if (!el || !pane) return
    const at = el.getBoundingClientRect()
    const view = pane.getBoundingClientRect()
    if (at.top < view.top || at.bottom > view.bottom) el.scrollIntoView({ block: byKeyboard.current ? 'nearest' : 'center' })
    byKeyboard.current = false
  }, [task?.id])

  function onKeyDown(e: KeyboardEvent) {
    if (e.metaKey || e.ctrlKey || e.altKey || (e.key !== 'ArrowDown' && e.key !== 'ArrowUp')) return
    const i = taskRows.findIndex((t) => t.id === task?.id)
    const next = taskRows[e.key === 'ArrowDown' ? i + 1 : i - 1]
    if (!next) return
    e.preventDefault()
    byKeyboard.current = true
    graph.go({ view: 'uloha', task: next.id }, false)
    document.querySelector<HTMLButtonElement>(`[data-task="${next.id}"]`)?.focus()
  }

  const groups: { test: string; tasks: TaskEntry[] }[] = []
  for (const t of taskRows) {
    if (groups.at(-1)?.test !== t.test) groups.push({ test: t.test, tasks: [] })
    groups.at(-1)!.tasks.push(t)
  }

  return (
    <div className="flex min-h-0 flex-col">
      <p className={`flex flex-none flex-wrap justify-between gap-x-4 px-5 pt-2.5 pb-1 ${hint}`}>
        <span>{taskCountLabel(stepped)} s kroky</span>
        <span className="tabular-nums">{filtering ? `${taskRows.length} z ${taskCountLabel(total)}` : taskCountLabel(total)}</span>
      </p>
      {taskRows.length === 0 ? (
        <p className={message}>
          Těmto filtrům žádná úloha neodpovídá.{' '}
          <button type="button" className={link} onClick={graph.clearFilters}>
            Zrušit filtry
          </button>
        </p>
      ) : (
        <div className="min-h-0 flex-1 overflow-y-auto px-2 pb-4" data-list onKeyDown={onKeyDown}>
          {groups.map(({ test, tasks }) => (
            <section key={test} aria-label={testName(test)}>
              <h3 className="px-3 pt-4 pb-1 text-small font-semibold">{testName(test)}</h3>
              <ul>
                {tasks.map((t) => {
                  const selected = t.id === task?.id
                  const notes = [t.stepped && 's\u00a0kroky', reviewByTask.has(t.id) && 'k\u00a0revizi'].filter(Boolean).join(' · ')
                  return (
                    <li key={t.id}>
                      <button
                        type="button"
                        ref={selected ? selectedRef : undefined}
                        data-task={t.id}
                        className={`${row} ${selected ? selectedRow : rowHover}`}
                        aria-current={selected}
                        onClick={() => {
                          graph.go({ view: 'uloha', task: t.id })
                          onPick()
                        }}
                      >
                        <span className="text-small text-muted tabular-nums">
                          Úloha {t.task} · {pointsLabel(t.points)} · {successLabel(t.success_pct)}
                          {notes && ` · ${notes}`}
                        </span>
                        <span className="line-clamp-2">{t.description}</span>
                      </button>
                    </li>
                  )
                })}
              </ul>
            </section>
          ))}
        </div>
      )}
    </div>
  )
}
