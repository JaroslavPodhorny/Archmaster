import { CheckOption } from '../../../shared/CheckOption'
import { button, buttonActive, input, switchOption, switchOptionOff, switchOptionOn, switchTrack } from '../../../shared/controls'
import { SidebarButton } from '../../../shared/SidebarButton'
import { Dropdown } from '../../../shared/Dropdown'
import {
  KIND_MEANING,
  KIND_NAMES,
  PRIORITIES,
  PRIORITY_MEANING,
  PRIORITY_NAMES,
  SEARCH_PLACEHOLDER,
  VERSION_MEANING,
  VERSION_NAMES,
  capitalized,
} from '../labels'
import { depth } from '../tree'
import type { Kind, TreeVersion } from '../types'
import type { TopicTree, View } from '../useTopicTree'

const VERSIONS: TreeVersion[] = ['old', 'new']
const VIEWS: View[] = ['tree', 'graph']
const VIEW_NAMES: Record<View, string> = { tree: 'Strom', graph: 'Graf' }
const KINDS = Object.keys(KIND_NAMES) as Kind[]


type SwitchProps<T extends string> = {
  label: string
  options: T[]
  names: Record<T, string>
  hints?: Record<T, string>
  value: T
  onChange: (value: T) => void
}

/** Options of which one is pressed. */
function Switch<T extends string>({ label, options, names, hints, value, onChange }: SwitchProps<T>) {
  return (
    <div className={switchTrack} role="group" aria-label={label}>
      {options.map((option) => (
        <button
          key={option}
          type="button"
          className={`${switchOption} px-3.5 ${value === option ? switchOptionOn : switchOptionOff}`}
          aria-pressed={value === option}
          title={hints?.[option]}
          onClick={() => onChange(option)}
        >
          {names[option]}
        </button>
      ))}
    </div>
  )
}

/** Adds the value to the list, or takes it out. */
function toggled<T>(list: T[], value: T): T[] {
  return list.includes(value) ? list.filter((v) => v !== value) : [...list, value]
}

/** Everything that narrows the tree on the left (search, priority, kind of skill, "only what relates
 *  to the selection"), laid out like the problem database's bar; on the right what is shown: the old
 *  or the new tree, as a tree or as the graph of all prerequisite links. When the window is too narrow
 *  for both groups on one line, the switches move to a second line together. */
export function TreeBar({ tree }: { tree: TopicTree }) {
  const { filters, setFilters } = tree
  const skills = tree.index?.nodes.filter((node) => depth(node) === 2) ?? []
  const label = (title: string, count: number) => (count ? `${title} · ${count}` : title)
  // "Only related" works from a skill; while an area or topic is selected it stays set but does nothing.
  const canRelate = tree.selected !== null && depth(tree.selected) === 2
  const related = filters.relatedOnly && canRelate

  return (
    <div className="flex flex-wrap items-center justify-between gap-x-6 gap-y-2 border-b border-line px-6 py-3.5 max-sm:px-4">
      <div className="flex flex-wrap items-center gap-2 max-sm:w-full">
        <SidebarButton />
        <input
          type="search"
          className={`${input} max-sm:max-w-none max-sm:basis-full`}
          value={filters.q}
          onChange={(e) => setFilters({ ...filters, q: e.target.value })}
          placeholder={SEARCH_PLACEHOLDER[tree.version]}
          aria-label={SEARCH_PLACEHOLDER[tree.version]}
        />
        <Dropdown label={label('Priorita', filters.priorities.length)} active={filters.priorities.length > 0}>
          {PRIORITIES.map((priority) => (
            <CheckOption
              key={priority}
              label={PRIORITY_NAMES[priority]}
              count={skills.filter((s) => s.priority === priority).length}
              title={PRIORITY_MEANING[priority]}
              checked={filters.priorities.includes(priority)}
              onChange={() => setFilters({ ...filters, priorities: toggled(filters.priorities, priority) })}
            />
          ))}
        </Dropdown>
        <Dropdown label={label('Druh', filters.kinds.length)} active={filters.kinds.length > 0}>
          {KINDS.map((kind) => (
            <CheckOption
              key={kind}
              label={capitalized(KIND_NAMES[kind])}
              count={skills.filter((s) => s.kind === kind).length}
              title={capitalized(KIND_MEANING[kind])}
              checked={filters.kinds.includes(kind)}
              onChange={() => setFilters({ ...filters, kinds: toggled(filters.kinds, kind) })}
            />
          ))}
        </Dropdown>
        <button
          type="button"
          className={related ? buttonActive : button}
          aria-pressed={related}
          disabled={!canRelate}
          title={
            canRelate
              ? 'Zobrazí jen vybranou dovednost, vše, co potřebuje, a vše, co na ni navazuje'
              : 'Vyberte dovednost: oblast ani téma nic nepotřebují'
          }
          onClick={() => setFilters({ ...filters, relatedOnly: !filters.relatedOnly })}
        >
          Jen související
        </button>
      </div>
      <div className="flex flex-wrap gap-2">
        <Switch
          label="Verze stromu"
          options={VERSIONS}
          names={VERSION_NAMES}
          hints={VERSION_MEANING}
          value={tree.version}
          onChange={tree.setVersion}
        />
        <Switch label="Zobrazení" options={VIEWS} names={VIEW_NAMES} value={tree.view} onChange={tree.setView} />
      </div>
    </div>
  )
}
