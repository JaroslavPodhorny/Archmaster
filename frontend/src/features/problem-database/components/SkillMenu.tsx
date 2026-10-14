import { useState } from 'react'
import type { FilterOption, FilterValue } from '../types'
import { CheckOption } from '../../../shared/CheckOption'

type Props = {
  /** The curriculum tree in learning order; depth 0 area, 1 topic, 2 skill. */
  options: FilterOption[]
  selected: FilterValue[]
  onToggle: (value: FilterValue) => void
}

// Areas stand out; skills are indented under their topic.
const DEPTH_CLASSES = ['font-semibold', '', 'pl-11']

function topicOf(value: FilterValue): string {
  return String(value).split('.').slice(0, 2).join('.')
}

/** The curriculum tree as a menu. A topic opens to show its skills; ticking an area or a topic
 *  selects everything under it. */
export function SkillMenu({ options, selected, onToggle }: Props) {
  // Topics holding a selected skill start open.
  const [open, setOpen] = useState(
    () => new Set(selected.filter((v) => String(v).split('.').length === 3).map(topicOf)),
  )

  function toggleOpen(topic: string) {
    const next = new Set(open)
    if (!next.delete(topic)) next.add(topic)
    setOpen(next)
  }

  return options
    .filter((option) => option.depth !== 2 || open.has(topicOf(option.value)))
    .map((option) => {
      const id = String(option.value)
      return (
        <div key={id} className={`flex items-baseline ${DEPTH_CLASSES[option.depth ?? 1]}`}>
          {option.depth === 1 && (
            <button
              type="button"
              className="w-5.5 cursor-pointer text-muted"
              aria-expanded={open.has(id)}
              aria-label={`Dovednosti tématu ${option.label}`}
              onClick={() => toggleOpen(id)}
            >
              {open.has(id) ? '▾' : '▸'}
            </button>
          )}
          <CheckOption
            label={option.label}
            count={option.count}
            checked={selected.includes(option.value)}
            onChange={() => onToggle(option.value)}
            className="min-w-0 flex-1"
          />
        </div>
      )
    })
}
