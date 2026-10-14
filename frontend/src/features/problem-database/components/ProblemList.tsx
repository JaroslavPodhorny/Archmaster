import { useEffect, useRef } from 'react'
import { button, focusRing, hint, rowHover, selectedRow } from '../../../shared/controls'
import { successLabel } from '../labels'
import type { Problem } from '../types'

type Props = {
  problems: Problem[]
  total: number
  selectedId: string | null
  onSelect: (id: string) => void
  onLoadMore: () => void
  loadingMore: boolean
}

const row = `grid w-full cursor-pointer grid-cols-[minmax(0,1fr)_auto] gap-x-3 gap-y-0.5 rounded-xl px-3 py-2.5 text-left ${focusRing}`
const rowNumbers = 'text-small text-muted tabular-nums'

/** One line per problem; the selected one is shown in the detail pane. The next page loads by itself
 *  when the end of the list comes near (scrolling, or the arrow keys walking down); the button is there
 *  for when it does not. */
export function ProblemList({ problems, total, selectedId, onSelect, onLoadMore, loadingMore }: Props) {
  const end = useRef<HTMLLIElement>(null)
  const more = problems.length < total

  useEffect(() => {
    const el = end.current
    if (!el || !more) return
    const observer = new IntersectionObserver((entries) => entries[0].isIntersecting && onLoadMore(), {
      rootMargin: '300px',
    })
    observer.observe(el)
    return () => observer.disconnect()
  }, [more, onLoadMore, problems.length])

  return (
    <ul className="overflow-y-auto border-r border-line p-2 max-sm:border-r-0 max-sm:group-data-[detail=true]/pd:hidden">
      {problems.map((problem) => (
        <li key={problem.id}>
          <button
            type="button"
            className={`${row} ${problem.id === selectedId ? selectedRow : rowHover}`}
            data-problem-id={problem.id}
            aria-current={problem.id === selectedId}
            onClick={() => onSelect(problem.id)}
          >
            <span className={rowNumbers}>
              {problem.year} {problem.term} · {problem.task}
            </span>
            <span className="col-span-full line-clamp-2">{problem.description}</span>
            <span className={`${rowNumbers} col-start-2 row-start-1`} title="Úspěšnost">
              {successLabel(problem.success_pct)}
            </span>
          </button>
        </li>
      ))}
      {more && (
        <li className="px-3 py-3" ref={end}>
          {loadingMore ? (
            <span className={hint}>Načítám další…</span>
          ) : (
            <button type="button" className={button} onClick={onLoadMore}>
              Zobrazit další ({total - problems.length})
            </button>
          )}
        </li>
      )}
    </ul>
  )
}
