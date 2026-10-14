import { useEffect, useRef, type KeyboardEvent } from 'react'
import { BOX_W, columnX, graphLayout, neighbour } from '../../../shared/graphLayout'
import { STEPS_NOTE, stepsLabel } from '../labels'
import { depth, skillsUnder } from '../tree'
import type { TreeNode } from '../types'
import type { TopicTree } from '../useTopicTree'
import { MatchCount } from './MatchCount'
import { SkillBox } from './SkillBox'

const pane = 'flex min-h-0 flex-col border-r border-line max-sm:border-r-0 max-sm:border-b'
// Skills needed in most tests stand out; rare and specification-only ones step back.
const PRIORITY_CLASSES: Record<string, string> = { 1: 'font-semibold', 3: 'text-muted', S: 'text-muted' }

/** The graph pane: every skill at once, what it needs to its left, joined by the prerequisite links.
 *  The selected skill's chain (all it needs, all that builds on it) is drawn in the accent colour;
 *  for a selected area or topic its skills are tinted. Skills the filters leave out turn grey and
 *  stay in place, "Jen související" hides everything outside the chain. Arrow keys move between boxes. */
export function SkillGraph({ tree }: { tree: TopicTree }) {
  const { selected, before, after, passes, isRelated } = tree
  const index = tree.index!
  const layout = graphLayout(index.nodes)
  const scrolled = useRef(false)

  const skills = index.nodes.filter((node) => depth(node) === 2 && isRelated(node))
  const shown = new Set(skills.map((skill) => skill.id))
  const chosen = selected && depth(selected) === 2 ? selected.id : null
  const tinted = new Set(selected && !chosen ? skillsUnder(index, selected).map((skill) => skill.id) : [])
  const inView = chosen ?? [...tinted][0]

  // The selected box (for an area or topic its first skill) comes into view: in the middle when the
  // graph opens, then only as far as needed.
  useEffect(() => {
    document.getElementById(`sg-${inView}`)?.scrollIntoView(
      scrolled.current ? { block: 'nearest', inline: 'nearest' } : { block: 'center', inline: 'center' },
    )
    scrolled.current = true
  }, [inView])

  const inChain = (id: string) => id === chosen || before.has(id) || after.has(id)
  // A link belongs to the chain when it lies on a way to the selected skill or on a way from it.
  const onWay = (side: Map<string, number>, id: string) => id === chosen || side.has(id)
  const links = layout.links
    .map((link) => ({
      ...link,
      chain: (onWay(before, link.from) && onWay(before, link.to)) || (onWay(after, link.from) && onWay(after, link.to)),
    }))
    .filter((link) => shown.has(link.from) && shown.has(link.to))
    .sort((a, b) => Number(a.chain) - Number(b.chain))

  function look(skill: TreeNode): string {
    if (skill.id === chosen) return 'border-accent bg-accent-soft font-semibold text-accent'
    const border = inChain(skill.id) ? 'border-accent' : 'border-edge'
    const fill = tinted.has(skill.id) ? 'bg-accent-soft' : 'bg-page hover:bg-tint'
    return `${border} ${fill} ${passes(skill) ? (PRIORITY_CLASSES[skill.priority!] ?? '') : 'text-faint'}`
  }

  function onKeyDown(e: KeyboardEvent) {
    if (!chosen || e.metaKey || e.ctrlKey || e.altKey || !e.key.startsWith('Arrow')) return
    const next = neighbour(layout, chosen, e.key, (id) => shown.has(id))
    if (next) tree.select(next)
    e.preventDefault()
  }

  return (
    <div className={pane}>
      <div className="flex flex-none px-5 pt-2.5 pb-1 text-small">
        <MatchCount tree={tree} />
      </div>
      <div
        className="min-h-0 flex-1 overflow-auto focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-accent"
        role="group"
        tabIndex={0}
        aria-label="Graf závislostí dovedností"
        aria-activedescendant={chosen ? `sg-${chosen}` : undefined}
        onKeyDown={onKeyDown}
      >
        <div className="sticky top-0 z-10 w-max min-w-full border-b border-line bg-page px-6 text-small text-muted" title={STEPS_NOTE}>
          <div className="relative h-6.5" style={{ width: layout.width }}>
            {Array.from({ length: layout.columns }, (_, column) => (
              <span key={column} className="absolute top-0.75 whitespace-nowrap" style={{ left: columnX(column) }}>
                {stepsLabel(column)}
              </span>
            ))}
          </div>
        </div>

        <div className="w-max px-6 pt-4 pb-8">
          <div className="relative" style={{ width: layout.width, height: layout.height }}>
            <svg className="absolute top-0 left-0 fill-none" width={layout.width} height={layout.height} aria-hidden="true">
              {links.map((link) => (
                <path
                  key={`${link.from} ${link.to}`}
                  className={link.chain ? 'stroke-accent stroke-[1.5]' : 'stroke-edge'}
                  d={link.path}
                />
              ))}
            </svg>

            {skills.length === layout.spots.size && layout.alone.count > 0 && (
              <p className="absolute left-0 border-t border-line pt-2.5 text-muted" style={{ top: layout.alone.top, width: layout.width }}>
                Bez vazeb ({layout.alone.count}): nic nepotřebují a nic na ně nenavazuje
              </p>
            )}
            {skills.length === layout.spots.size && layout.alone.areas.map((area) => (
              <span
                key={area.id}
                className="absolute left-0 pt-0.5 text-small leading-[17px] text-muted"
                style={{ top: area.y, width: BOX_W }}
              >
                {index.byId.get(area.id)!.name}
              </span>
            ))}

            {skills.map((skill) => (
              <SkillBox
                key={skill.id}
                id={`sg-${skill.id}`}
                tabIndex={-1}
                index={index}
                skill={skill}
                at={layout.spots.get(skill.id)!}
                className={`scroll-m-10 ${look(skill)}`}
                onGo={tree.select}
              />
            ))}
          </div>
        </div>
      </div>
    </div>
  )
}
