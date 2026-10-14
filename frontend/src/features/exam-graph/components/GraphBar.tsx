import { button, buttonActive, input } from '../../../shared/controls'
import { SidebarButton } from '../../../shared/SidebarButton'
import { VIEWS, VIEW_HINTS, VIEW_NAMES } from '../labels'
import type { ExamGraph } from '../useExamGraph'
import { PrincipleSearch } from './PrincipleSearch'
import { Switch } from './Switch'
import { TestPicker } from './TestPicker'

/** On the left what the view is narrowed or moved by: the task search and two filters (Úloha), the
 *  principle search (Princip), the test (Zkouška); on the right the switch between the views. When both
 *  do not fit on one line, the switch moves to a second one. */
export function GraphBar({ graph }: { graph: ExamGraph }) {
  const { view, filters, setFilters } = graph
  return (
    <div className="flex flex-wrap items-center justify-between gap-x-6 gap-y-2 border-b border-line px-6 py-3.5 max-sm:px-4">
      <div className="flex flex-wrap items-center gap-2 max-sm:w-full">
        <SidebarButton />
        {view === 'uloha' && (
          <>
            <input
              type="search"
              className={`${input} max-sm:max-w-none max-sm:basis-full`}
              value={filters.q}
              onChange={(e) => setFilters({ ...filters, q: e.target.value })}
              placeholder="Hledat úlohu"
              aria-label="Hledat úlohu"
            />
            <button
              type="button"
              className={filters.steppedOnly ? buttonActive : button}
              aria-pressed={filters.steppedOnly}
              title="Jen úlohy s rozepsaným postupem po krocích"
              onClick={() => setFilters({ ...filters, steppedOnly: !filters.steppedOnly })}
            >
              Jen s kroky
            </button>
            <button
              type="button"
              className={filters.reviewOnly ? buttonActive : button}
              aria-pressed={filters.reviewOnly}
              title="Jen úlohy s otevřenou otázkou: rozdíl seznamu principů, chybná možnost, kroky ke kontrole"
              onClick={() => setFilters({ ...filters, reviewOnly: !filters.reviewOnly })}
            >
              Jen k revizi
            </button>
          </>
        )}
        {view === 'princip' && <PrincipleSearch graph={graph} />}
        {view === 'zkouska' && <TestPicker graph={graph} />}
      </div>
      <Switch label="Zobrazení" options={VIEWS} names={VIEW_NAMES} hints={VIEW_HINTS} value={view} onChange={graph.setView} />
    </div>
  )
}
