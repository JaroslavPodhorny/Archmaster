import { useMemo, useState } from 'react'
import { focusRing } from '../../../shared/controls'
import { BOX_H, BOX_W, graphLayout } from '../../../shared/graphLayout'
import type { ExamGraph } from '../useExamGraph'

/** Room beside the outer boxes for their "+N" buttons. */
const SIDE = 34

/** The selected principle between what it rests on (to the left) and what builds on it (to the right),
 *  one step each way. "+N" on an outer box shows the N principles one step further out on that side; a
 *  box selects its principle. Laid out by shared/graphLayout.ts, like the prerequisite graphs elsewhere. */
export function PrincipleFocus({ graph, id }: { graph: ExamGraph; id: string }) {
  const [opened, setOpened] = useState<ReadonlySet<string>>(new Set())
  const all = graph.index!.principles
  const dependents = useMemo(() => {
    const out = new Map<string, string[]>()
    for (const p of all) for (const q of p.requires) out.set(q, [...(out.get(q) ?? []), p.id])
    return out
  }, [all])

  // What is shown: the principle, one step each way, and one step further from every opened box.
  const { left, right } = useMemo(() => {
    const left = new Set<string>()
    const right = new Set<string>()
    const walk = (from: string, side: Set<string>, next: (id: string) => string[]) => {
      for (const n of next(from)) {
        if (side.has(n)) continue
        side.add(n)
        if (opened.has(n)) walk(n, side, next)
      }
    }
    walk(id, left, (p) => graph.principles.get(p)?.requires ?? [])
    walk(id, right, (p) => dependents.get(p) ?? [])
    return { left, right }
  }, [id, opened, graph.principles, dependents])

  const nodes = useMemo(() => {
    const shown = new Set([id, ...left, ...right])
    return all.filter((p) => shown.has(p.id)).map((p) => ({ id: p.id, requires: p.requires.filter((q) => shown.has(q)) }))
  }, [all, id, left, right])
  const layout = graphLayout(nodes, true)
  const shown = new Set(nodes.map((n) => n.id))

  /** How many principles one step further out a box would show. */
  function hidden(pid: string): number {
    const next = left.has(pid) ? (graph.principles.get(pid)?.requires ?? []) : (dependents.get(pid) ?? [])
    return next.filter((n) => !shown.has(n)).length
  }

  function toggle(pid: string) {
    const next = new Set(opened)
    if (!next.delete(pid)) next.add(pid)
    setOpened(next)
  }

  return (
    <div className="w-fit max-w-full overflow-x-auto rounded-xl border border-line p-3" role="group" aria-label="Předpoklady a navazující principy">
      <div className="relative" style={{ width: layout.width + 2 * SIDE, height: layout.height }}>
        <svg className="absolute top-0 fill-none" style={{ left: SIDE }} width={layout.width} height={layout.height} aria-hidden="true">
          {layout.links.map((link) => (
            <path
              key={`${link.from} ${link.to}`}
              className={link.from === id || link.to === id ? 'stroke-accent' : 'stroke-edge'}
              d={link.path}
            />
          ))}
        </svg>
        {nodes.map((node) => {
          const at = layout.spots.get(node.id)!
          const p = graph.principles.get(node.id)!
          const focus = node.id === id
          const more = focus ? 0 : hidden(node.id)
          const isOpen = opened.has(node.id)
          return (
            <div key={node.id}>
              <button
                type="button"
                className={`absolute line-clamp-2 h-9 w-37.5 cursor-pointer rounded-md border px-1.75 py-0.5 text-left text-tiny ${focusRing} ${
                  focus ? 'border-accent bg-accent-soft font-semibold text-accent' : 'border-edge bg-page hover:bg-tint'
                }`}
                style={{ left: at.x + SIDE, top: at.y }}
                title={`${p.name} – ${graph.groups.get(p.topic)?.name}`}
                onClick={() => graph.go({ view: 'princip', node: node.id })}
              >
                {p.name}
              </button>
              {(more > 0 || isOpen) && (
                <button
                  type="button"
                  className={`absolute h-5 cursor-pointer rounded-full px-1.5 text-tiny text-muted tabular-nums hover:bg-selected hover:text-ink ${isOpen ? 'bg-selected' : 'bg-tint'} ${focusRing}`}
                  style={{ left: left.has(node.id) ? at.x + SIDE - 30 : at.x + SIDE + BOX_W + 4, top: at.y + (BOX_H - 20) / 2 }}
                  aria-expanded={isOpen}
                  title={isOpen ? 'Skrýt principy za ním' : left.has(node.id) ? 'Ukázat, na čem stojí' : 'Ukázat, co na něm stojí'}
                  onClick={() => toggle(node.id)}
                >
                  {isOpen ? '−' : `+${more}`}
                </button>
              )}
            </div>
          )
        })}
      </div>
    </div>
  )
}
