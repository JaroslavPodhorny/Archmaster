import { useEffect, useId, useMemo, useRef, useState, type KeyboardEvent } from 'react'
import { focusRing } from '../../../shared/controls'
import { fold } from '../labels'
import type { ExamGraph } from '../useExamGraph'

const MATCHES_SHOWN = 12
// The bar's search field (shared/controls.ts `input`) sized by its wrapper, which carries the flex sizing.
const field = `h-10 w-full rounded-full border border-edge bg-page px-4 shadow-control placeholder:text-faint ${focusRing}`

/** A search that lists the principles whose name or topic matches and goes to the one chosen (a click,
 *  or the arrow keys and Enter). Escape or a click elsewhere closes the list. */
export function PrincipleSearch({ graph }: { graph: ExamGraph }) {
  const [q, setQ] = useState('')
  const [open, setOpen] = useState(false)
  const [active, setActive] = useState(0)
  const root = useRef<HTMLDivElement>(null)
  const list = useId()

  const matches = useMemo(() => {
    const needle = fold(q.trim())
    if (!needle || !graph.index) return []
    return graph.index.principles
      .filter((p) => fold(`${p.name} ${graph.groups.get(p.topic)?.name ?? ''}`).includes(needle))
      .slice(0, MATCHES_SHOWN)
  }, [q, graph.index, graph.groups])

  useEffect(() => {
    if (!open) return
    function onPointerDown(e: PointerEvent) {
      if (!root.current?.contains(e.target as Node)) setOpen(false)
    }
    document.addEventListener('pointerdown', onPointerDown)
    return () => document.removeEventListener('pointerdown', onPointerDown)
  }, [open])

  function choose(id: string) {
    graph.go({ view: 'princip', node: id })
    setOpen(false)
    setQ('')
  }

  function onKeyDown(e: KeyboardEvent) {
    if (e.key === 'Escape') setOpen(false)
    else if (e.key === 'ArrowDown') setActive(Math.min(active + 1, matches.length - 1))
    else if (e.key === 'ArrowUp') setActive(Math.max(active - 1, 0))
    else if (e.key === 'Enter' && matches[active]) choose(matches[active].id)
    else return
    e.preventDefault()
  }

  const shown = open && q.trim() !== ''
  return (
    <div className="relative max-w-60 min-w-40 flex-[1_1_10rem] max-sm:max-w-none max-sm:basis-full" ref={root}>
      <input
        type="search"
        className={field}
        value={q}
        placeholder="Hledat princip"
        aria-label="Hledat princip"
        role="combobox"
        aria-expanded={shown}
        aria-controls={list}
        aria-activedescendant={shown && matches[active] ? `${list}-${matches[active].id}` : undefined}
        onChange={(e) => {
          setQ(e.target.value)
          setActive(0)
          setOpen(true)
        }}
        onFocus={() => setOpen(true)}
        onKeyDown={onKeyDown}
      />
      {shown && (
        <ul
          id={list}
          role="listbox"
          className="absolute top-[calc(100%+6px)] left-0 z-20 max-h-[70dvh] w-120 max-w-[calc(100vw-16px)] overflow-y-auto rounded-2xl bg-raised p-1.5 shadow-panel"
        >
          {matches.length === 0 && <li className="px-2.5 py-1.5 text-muted">Žádný princip neodpovídá.</li>}
          {matches.map((p, i) => (
            <li
              key={p.id}
              id={`${list}-${p.id}`}
              role="option"
              aria-selected={i === active}
              className={`flex cursor-pointer items-baseline gap-3 rounded-lg px-2.5 py-1.5 ${i === active ? 'bg-selected' : 'hover:bg-selected'}`}
              onPointerEnter={() => setActive(i)}
              onClick={() => choose(p.id)}
            >
              <span className="min-w-0">{p.name}</span>
              <span className="ml-auto flex-none pl-2 text-small text-muted">{graph.groups.get(p.topic)?.name}</span>
            </li>
          ))}
        </ul>
      )}
    </div>
  )
}
