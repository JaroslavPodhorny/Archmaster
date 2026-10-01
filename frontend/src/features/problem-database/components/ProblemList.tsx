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

/** One line per problem; the selected one is shown in the detail pane. */
export function ProblemList({ problems, total, selectedId, onSelect, onLoadMore, loadingMore }: Props) {
  return (
    <ul className="pd-list">
      {problems.map((problem) => (
        <li key={problem.id}>
          <button
            type="button"
            className={problem.id === selectedId ? 'pd-row pd-row-selected' : 'pd-row'}
            data-problem-id={problem.id}
            aria-current={problem.id === selectedId}
            onClick={() => onSelect(problem.id)}
          >
            <span className="pd-row-source">
              {problem.year} {problem.term} · {problem.task}
            </span>
            <span className="pd-row-description">{problem.description}</span>
            <span className="pd-row-success">{successLabel(problem.success_pct)}</span>
          </button>
        </li>
      ))}
      {problems.length < total && (
        <li className="pd-more">
          <button type="button" className="pd-button" onClick={onLoadMore} disabled={loadingMore}>
            {loadingMore ? 'Načítám…' : `Zobrazit další (${total - problems.length})`}
          </button>
        </li>
      )}
    </ul>
  )
}
