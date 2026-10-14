import { useId, useMemo } from 'react'
import { focusRing } from '../../../shared/controls'
import { BOX_W, flowLayout } from '../flowLayout'
import { keptTogether, percentLabel } from '../labels'
import type { Route, TaskDetail } from '../types'

type Props = {
  task: TaskDetail
  route: Route
  /** The selected step, whose inputs are marked. */
  selected: string | null
  onSelect: (stepId: string | null) => void
}

const box = 'absolute flex flex-col gap-0.5 overflow-hidden rounded-md border px-2 py-1.25 text-left text-tiny'

/** The solution flow of a route: the given facts in the first row, then one column per item with its steps
 *  from top to bottom, each result with the principle its step applies. Arrows run from a result to the
 *  steps that compute from it; in the accent colour where an item takes a result found for an earlier
 *  one, and into the selected step. Answers are grey with CERMAT's success rate; a step whose principle
 *  is missing from its item's stored list has a dashed border. A click selects a step, which marks
 *  everything it computes from, the given facts included. */
export function SolutionFlow({ task, route, selected, onSelect }: Props) {
  const layout = useMemo(() => flowLayout(task, route), [task, route])
  const marker = useId()
  const success = new Map(task.items.map((item) => [item.item, item.success_pct]))
  const missing = new Map(route.items.map((item) => [item.item, new Set(item.missing)]))
  const chosen = route.steps.find((step) => step.id === selected)
  const feeds = new Set(chosen?.inputs ?? [])
  const lit = (link: { to: string; reused: boolean }) => link.to === selected || link.reused
  // Highlighted links are drawn last, so no grey line crosses them.
  const links = [...layout.links].sort((a, b) => Number(lit(a)) - Number(lit(b)))

  return (
    <div className="w-fit max-w-full overflow-x-auto rounded-xl border border-line p-3" role="group" aria-label="Postup řešení po krocích">
      <div className="relative" style={{ width: layout.width, height: layout.height }}>
        <svg className="absolute top-0 left-0 overflow-visible fill-none" width={layout.width} height={layout.height} aria-hidden="true">
          <defs>
            {(['edge', 'accent'] as const).map((tone) => (
              <marker
                key={tone}
                id={`${marker}-${tone}`}
                viewBox="0 0 10 10"
                refX="9"
                refY="5"
                markerWidth="6"
                markerHeight="6"
                orient="auto-start-reverse"
              >
                <path className={tone === 'edge' ? 'fill-edge' : 'fill-accent'} d="M0,0 L10,5 L0,10 z" />
              </marker>
            ))}
          </defs>
          {links.map((link) => (
            <path
              key={`${link.from} ${link.to}`}
              className={lit(link) ? 'stroke-accent' : 'stroke-edge'}
              strokeWidth={lit(link) ? 1.5 : 1.25}
              d={link.path}
              markerEnd={`url(#${marker}-${lit(link) ? 'accent' : 'edge'})`}
            />
          ))}
        </svg>

        {layout.titles.map((title) => (
          <span key={title.item} className="absolute text-small text-muted" style={{ left: title.x, top: title.y }}>
            Položka {title.item}
          </span>
        ))}

        {task.given.map((given, n) => {
          const at = layout.spots.get(given.id)!
          return (
            <div
              key={given.id}
              className={`${box} bg-surface ${feeds.has(given.id) ? 'border-accent' : 'border-edge'}`}
              style={{ left: at.x, top: at.y, width: BOX_W, height: at.height }}
              title={given.text}
            >
              <span className="text-muted">Zadání {n + 1}</span>
              <span className="line-clamp-3">{keptTogether(given.text)}</span>
            </div>
          )
        })}

        {route.steps.map((step) => {
          const at = layout.spots.get(step.id)!
          const isSelected = step.id === selected
          const border = isSelected || feeds.has(step.id) || step.reused_by.length ? 'border-accent' : 'border-edge'
          const fill = isSelected ? 'bg-accent-soft' : step.answer ? 'bg-tint' : 'bg-page'
          const dashed = missing.get(step.item)?.has(step.principle.id) ? 'border-dashed' : ''
          const solved = step.answer ? success.get(step.answer) : null
          return (
            <button
              key={step.id}
              type="button"
              className={`${box} cursor-pointer ${border} ${fill} ${dashed} ${isSelected ? '' : 'hover:border-muted'} ${focusRing}`}
              style={{ left: at.x, top: at.y, width: BOX_W, height: at.height }}
              aria-pressed={isSelected}
              title={`${step.result} – ${step.principle.name}`}
              onClick={() => onSelect(isSelected ? null : step.id)}
            >
              {step.answer && (
                <span className="font-semibold tabular-nums">
                  Odpověď {step.answer}
                  {solved != null && ` · ${percentLabel(solved)}`}
                </span>
              )}
              <span className="line-clamp-3">{keptTogether(step.result)}</span>
              <span className="mt-auto line-clamp-1 text-muted">{step.principle.name}</span>
            </button>
          )
        })}
      </div>
    </div>
  )
}
