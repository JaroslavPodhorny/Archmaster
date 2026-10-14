import { CheckOption } from '../../../shared/CheckOption'
import { input } from '../../../shared/controls'
import { Dropdown } from '../../../shared/Dropdown'
import { SidebarButton } from '../../../shared/SidebarButton'
import { FILTER_ORDER, FILTER_TITLES } from '../labels'
import type { ProblemSearch } from '../useProblemSearch'
import { SkillMenu } from './SkillMenu'
import { SuccessRangeFields } from './SuccessRangeFields'

/** Search field and one menu per filter: everything that narrows the list. The sort order sits with
 *  the results, in ActiveFilters. */
export function FilterBar({ search }: { search: ProblemSearch }) {
  const { options, selected, success } = search
  const successActive = success.min !== null || success.max !== null

  return (
    <div className="flex flex-wrap items-center gap-2 px-6 pt-3.5 pb-2.5 max-sm:px-4 max-sm:group-data-[detail=true]/pd:hidden">
      <SidebarButton />
      <input
        type="search"
        className={`${input} max-sm:max-w-none max-sm:basis-full`}
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
              wide={name === 'skills'}
            >
              {name === 'skills' ? (
                <SkillMenu
                  options={options.skills}
                  selected={selected.skills}
                  onToggle={(value) => search.toggleFilter('skills', value)}
                />
              ) : (
                options[name].map((option) => (
                  <CheckOption
                    key={option.value}
                    label={option.label}
                    count={option.count}
                    checked={selected[name].includes(option.value)}
                    onChange={() => search.toggleFilter(name, option.value)}
                  />
                ))
              )}
            </Dropdown>
          )
        })}
      <Dropdown label="Úspěšnost" active={successActive}>
        <SuccessRangeFields value={success} onChange={search.setSuccess} />
      </Dropdown>
    </div>
  )
}
