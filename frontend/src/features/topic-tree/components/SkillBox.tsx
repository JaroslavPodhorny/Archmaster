import { focusRing } from '../../../shared/controls'
import type { TreeIndex } from '../tree'
import type { TreeNode } from '../types'

type Props = {
  index: TreeIndex
  skill: TreeNode
  at: { x: number; y: number }
  /** Border, background and text for the state the graph shows it in. */
  className: string
  onGo: (skillId: string) => void
  /** Set by a graph that moves between its boxes with the arrow keys instead of Tab. */
  id?: string
  tabIndex?: number
}

/** A skill as a box of a graph (BOX_W × BOX_H in shared/graphLayout.ts): its name on at most two lines,
 *  the full name and its topic on hover. Clicking goes to the skill. */
export function SkillBox({ index, skill, at, className, onGo, id, tabIndex }: Props) {
  return (
    <button
      type="button"
      id={id}
      tabIndex={tabIndex}
      className={`absolute line-clamp-2 h-9 w-37.5 cursor-pointer rounded-md border px-1.75 py-0.5 text-left text-tiny ${focusRing} ${className}`}
      style={{ left: at.x, top: at.y }}
      title={`${skill.name} – ${index.byId.get(skill.parent!)!.name}`}
      onClick={() => onGo(skill.id)}
    >
      {skill.name}
    </button>
  )
}
