import { useEffect, useRef, type KeyboardEvent } from 'react'
import { link, linkQuiet, message, rowHover, selectedRow } from '../../../shared/controls'
import type { TopicTree } from '../useTopicTree'
import { MatchCount } from './MatchCount'
import { PriorityBadge } from './PriorityBadge'

const RELATIONS = { prerequisite: 'předpoklad', dependent: 'navazuje' }

const pane = 'flex min-h-0 flex-col border-r border-line max-sm:border-r-0 max-sm:border-b'
const mark = 'w-3 flex-none text-center font-normal text-faint'
// Areas, topics, skills: each level further in. Only areas are bold: weight shows the level in the tree,
// never the priority.
const DEPTH_CLASSES = ['mt-4 font-semibold first:mt-0', 'pl-7', 'pl-10']

/** The tree pane: a line to open or close every group (and how many skills the filters leave), then
 *  areas, topics that open to their skills, each skill with its priority. Arrow keys move through it;
 *  left and right close and open a group. */
export function TreeRows({ tree }: { tree: TopicTree }) {
  const { rows, selected } = tree
  const selectedRef = useRef<HTMLDivElement>(null)
  const byKeyboard = useRef(false)

  // A row out of view comes into it: by the arrow keys just far enough, from anywhere else (a link,
  // the address, the detail pane) to the middle. A row already in view stays where it is.
  useEffect(() => {
    const row = selectedRef.current
    const pane = row?.closest('[role=tree]')
    if (!row || !pane) return
    const at = row.getBoundingClientRect()
    const view = pane.getBoundingClientRect()
    if (at.top < view.top || at.bottom > view.bottom) row.scrollIntoView({ block: byKeyboard.current ? 'nearest' : 'center' })
    byKeyboard.current = false
  }, [selected?.id])

  function onKeyDown(e: KeyboardEvent) {
    if (!selected || e.metaKey || e.ctrlKey || e.altKey) return
    const i = rows.findIndex((row) => row.node.id === selected.id)
    const group = i >= 0 && rows[i].depth < 2
    if (e.key === 'ArrowDown' && i < rows.length - 1) tree.select(rows[i + 1].node.id)
    else if (e.key === 'ArrowUp' && i > 0) tree.select(rows[i - 1].node.id)
    else if (e.key === 'ArrowLeft' && group && rows[i].open) tree.setOpen(selected, false)
    else if (e.key === 'ArrowLeft' && selected.parent) tree.select(selected.parent)
    else if (e.key === 'ArrowRight' && group) tree.setOpen(selected, true)
    else return
    byKeyboard.current = true
    e.preventDefault()
  }

  return (
    <div className={pane}>
      <div className="flex flex-none flex-wrap items-baseline gap-x-4 px-5 pt-2.5 pb-1 text-small whitespace-nowrap">
        <button type="button" className={linkQuiet} title="Rozbalit všechny skupiny" onClick={() => tree.setAllOpen(true)}>
          Rozbalit
        </button>
        <button type="button" className={linkQuiet} title="Sbalit všechny skupiny" onClick={() => tree.setAllOpen(false)}>
          Sbalit
        </button>
        <MatchCount tree={tree} />
      </div>

      {rows.length === 0 ? (
        <p className={message}>
          Těmto filtrům nic neodpovídá.{' '}
          <button type="button" className={link} onClick={tree.clearFilters}>
            Zrušit filtry
          </button>
        </p>
      ) : (
        <div
          className="min-h-0 flex-1 overflow-y-auto px-2 pt-1 pb-4 focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-accent"
          role="tree"
          tabIndex={0}
          aria-label="Strom učiva"
          aria-activedescendant={selected ? `tt-${selected.id}` : undefined}
          onKeyDown={onKeyDown}
        >
          {rows.map(({ node, depth, open, matching, relation }) => {
            const isSelected = node.id === selected?.id
            const group = depth < 2
            return (
              <div
                key={node.id}
                id={`tt-${node.id}`}
                ref={isSelected ? selectedRef : undefined}
                role="treeitem"
                aria-level={depth + 1}
                aria-selected={isSelected}
                aria-expanded={group ? open : undefined}
                className={`flex cursor-default items-center gap-2 rounded-lg px-2.5 py-1.25 whitespace-nowrap ${DEPTH_CLASSES[depth]} ${
                  isSelected ? selectedRow : rowHover
                }`}
                onClick={() => {
                  if (group) tree.setOpen(node, !tree.isOpen(node))
                  tree.select(node.id)
                }}
              >
                {group ? (
                  <span className={mark} aria-hidden="true">
                    {open ? '▾' : '▸'}
                  </span>
                ) : (
                  <PriorityBadge priority={node.priority!} />
                )}
                <span className="truncate">{node.name}</span>
                {group && <span className="text-small font-normal text-faint tabular-nums">{matching}</span>}
                {relation && <span className="ml-auto pl-3 text-small font-normal text-accent">{RELATIONS[relation]}</span>}
              </div>
            )
          })}
        </div>
      )}
    </div>
  )
}
