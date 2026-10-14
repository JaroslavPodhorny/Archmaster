import { focusRing, linkQuiet } from '../../../shared/controls'
import { FILTER_ORDER, ORDERINGS, optionLabel, problemCountLabel } from '../labels'
import type { OrderBy } from '../types'
import type { ProblemSearch } from '../useProblemSearch'

const chip = `inline-flex cursor-pointer items-center gap-1.5 rounded-full bg-tint py-0.5 pr-2.5 pl-3 hover:bg-selected ${focusRing}`
const cross = <span className="text-muted" aria-hidden="true">×</span>

// The sort order as quiet text with a menu arrow: it belongs to the results, not to the filters.
const sortSelect = `ml-auto cursor-pointer rounded-lg py-1 pr-1 pl-2 text-small text-muted hover:bg-tint hover:text-ink ${focusRing}`

/** The result count, every filter in use (each removable with one click) and, at the right end, the
 *  sort order of the results. */
export function ActiveFilters({ search }: { search: ProblemSearch }) {
  const { options, selected, success } = search
  const rangeText =
    success.min !== null || success.max !== null
      ? `úspěšnost ${success.min ?? 0}–${success.max ?? 100} %`
      : null

  return (
    <div className="flex flex-wrap items-center gap-x-1.5 gap-y-1 border-b border-line px-6 pb-3 max-sm:px-4 max-sm:group-data-[detail=true]/pd:hidden">
      <span className="mr-2 font-semibold">{problemCountLabel(search.total)}</span>
      {FILTER_ORDER.flatMap((name) =>
        selected[name].map((value) => (
          <button
            key={`${name}-${value}`}
            type="button"
            className={chip}
            onClick={() => search.toggleFilter(name, value)}
            aria-label={`Zrušit filtr ${optionLabel(options, name, value)}`}
          >
            {optionLabel(options, name, value)}
            {cross}
          </button>
        )),
      )}
      {rangeText && (
        <button
          type="button"
          className={chip}
          onClick={() => search.setSuccess({ min: null, max: null })}
          aria-label="Zrušit filtr úspěšnosti"
        >
          {rangeText}
          {cross}
        </button>
      )}
      {search.anyFilter && (
        <button type="button" className={`${linkQuiet} ml-1.5 text-small`} onClick={search.clearFilters}>
          Zrušit vše
        </button>
      )}
      <select
        className={sortSelect}
        value={search.orderBy}
        onChange={(e) => search.setOrderBy(e.target.value as OrderBy)}
        aria-label="Řazení"
      >
        {Object.entries(ORDERINGS).map(([value, label]) => (
          <option key={value} value={value}>
            {label}
          </option>
        ))}
      </select>
    </div>
  )
}
