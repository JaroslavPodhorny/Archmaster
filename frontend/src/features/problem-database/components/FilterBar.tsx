import { FILTER_ORDER, FILTER_TITLES, ORDERINGS, WIDE_FILTERS } from '../labels'
import type { OrderBy } from '../types'
import type { ProblemSearch } from '../useProblemSearch'
import { Dropdown } from './Dropdown'
import { SuccessRangeFields } from './SuccessRangeFields'

/** Search field, one menu per filter, and the sort order: everything that narrows the list. */
export function FilterBar({ search }: { search: ProblemSearch }) {
  const { options, selected, success } = search
  const successActive = success.min !== null || success.max !== null

  return (
    <div className="pd-filterbar">
      <input
        type="search"
        className="pd-search"
        value={search.input}
        onChange={(e) => search.setInput(e.target.value)}
        placeholder="Hledat v zadání"
        aria-label="Hledat v zadání"
      />
      {options &&
        FILTER_ORDER.map((name) => {
          const count = selected[name].length
          return (
            <Dropdown
              key={name}
              label={count ? `${FILTER_TITLES[name]} · ${count}` : FILTER_TITLES[name]}
              active={count > 0}
              wide={WIDE_FILTERS.includes(name)}
            >
              {options[name].map((option) => (
                <label key={option.value} className="pd-option">
                  <input
                    type="checkbox"
                    checked={selected[name].includes(option.value)}
                    onChange={() => search.toggleFilter(name, option.value)}
                  />
                  <span>{option.label}</span>
                  <span className="pd-option-count">{option.count}</span>
                </label>
              ))}
            </Dropdown>
          )
        })}
      <Dropdown label="Úspěšnost" active={successActive}>
        <SuccessRangeFields value={success} onChange={search.setSuccess} />
      </Dropdown>
      <select
        className="pd-button pd-sort"
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
