import { useLayoutEffect, useRef } from 'react'
import { BOX_H as H, BOX_W as W } from '../../../shared/graphLayout'
import type { TreeIndex } from '../tree'
import type { TreeNode } from '../types'
import { SkillBox } from './SkillBox'

type Props = {
  index: TreeIndex
  skill: TreeNode
  /** Everything the skill needs, with its distance from the skill. */
  before: Map<string, number>
  onGo: (skillId: string) => void
}

// The gaps between columns and rows, in pixels.
const GAP_X = 34
const GAP_Y = 8

/** The skill between what it rests on (to the left, the furthest first) and what directly builds on
 *  it (to the right), joined by the prerequisite links, in a frame. A box goes to that skill. The
 *  heading above it is the detail pane's. */
export function PrerequisiteGraph({ index, skill, before, onGo }: Props) {
  const wrap = useRef<HTMLDivElement>(null)

  const furthest = Math.max(0, ...before.values())
  const direct = index.neededBy.get(skill.id) ?? []
  const columns: string[][] = Array.from({ length: furthest + 1 }, () => [])
  for (const [id, distance] of before) columns[furthest - distance].push(id)
  columns[furthest].push(skill.id)
  if (direct.length) columns.push([...direct])

  const tallest = Math.max(...columns.map((column) => column.length))
  const place = new Map<string, { x: number; y: number }>()
  columns.forEach((column, c) => {
    column.sort((a, b) => index.position.get(a)! - index.position.get(b)!)
    column.forEach((id, r) => {
      place.set(id, { x: c * (W + GAP_X), y: ((tallest - column.length) * (H + GAP_Y)) / 2 + r * (H + GAP_Y) })
    })
  })
  const width = columns.length * (W + GAP_X) - GAP_X
  const height = tallest * (H + GAP_Y) - GAP_Y
  const boxes = [...place].map(([id, at]) => ({ node: index.byId.get(id)!, at }))
  const center = place.get(skill.id)!.x + W / 2

  // Start with the skill itself in the middle of what is visible.
  useLayoutEffect(() => {
    if (wrap.current) wrap.current.scrollLeft = center - wrap.current.clientWidth / 2
  }, [center])

  return (
    <>
      <div className="overflow-x-auto rounded-xl border border-line p-3" ref={wrap}>
        <div className="relative" style={{ width, height }}>
          <svg className="absolute top-0 left-0 fill-none" width={width} height={height} aria-hidden="true">
            {boxes.flatMap(({ node, at }) =>
              node.requires
                .filter((id) => place.has(id))
                .map((id) => {
                  const from = place.get(id)!
                  const x1 = from.x + W
                  const y1 = from.y + H / 2
                  const y2 = at.y + H / 2
                  const mid = (x1 + at.x) / 2
                  return (
                    <path
                      key={`${id} ${node.id}`}
                      className={node.id === skill.id || id === skill.id ? 'stroke-accent' : 'stroke-edge'}
                      d={`M${x1} ${y1} C${mid} ${y1} ${mid} ${y2} ${at.x} ${y2}`}
                    />
                  )
                }),
            )}
          </svg>
          {boxes.map(({ node, at }) => (
            <SkillBox
              key={node.id}
              index={index}
              skill={node}
              at={at}
              className={
                node.id === skill.id
                  ? 'border-accent bg-accent-soft font-semibold text-accent'
                  : `border-edge bg-page hover:bg-tint ${(before.get(node.id) ?? 1) > 1 ? 'text-muted' : ''}`
              }
              onGo={onGo}
            />
          ))}
        </div>
      </div>
    </>
  )
}
