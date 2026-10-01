import { FILTER_ORDER, optionLabel, problemCountLabel } from '../labels'
import type { ProblemSearch } from '../useProblemSearch'

/** The result count and every filter in use, each removable with one click. */
export function ActiveFilters({ search }: { search: ProblemSearch }) {
  const { options, selected, success } = search
  const rangeText =
    success.min !== null || success.max !== null
      ? `úspěšnost ${success.min ?? 0}–${success.max ?? 100} %`
      : null

  return (
    <div className="pd-active">
      <span className="pd-total">{problemCountLabel(search.total)}</span>
      {FILTER_ORDER.flatMap((name) =>
        selected[name].map((value) => (
          <button
            key={`${name}-${value}`}
            type="button"
            className="pd-chip"
            onClick={() => search.toggleFilter(name, value)}
            aria-label={`Zrušit filtr ${optionLabel(options, name, value)}`}
          >
            {optionLabel(options, name, value)}
            <span aria-hidden="true">×</span>
          </button>
        )),
      )}
      {rangeText && (
        <button
          type="button"
          className="pd-chip"
          onClick={() => search.setSuccess({ min: null, max: null })}
          aria-label="Zrušit filtr úspěšnosti"
        >
          {rangeText}
          <span aria-hidden="true">×</span>
        </button>
      )}
      {search.anyFilter && (
        <button type="button" className="pd-link" onClick={search.clearFilters}>
          Zrušit vše
        </button>
      )}
    </div>
  )
}
