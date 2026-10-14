import { useMemo } from 'react'
import { Link } from 'react-router'
import { focusRing } from '../../../shared/controls'
import { graphLayout } from '../../../shared/graphLayout'
import { treeUrl } from '../../../shared/routes'
import type { GraphSkill } from '../types'

const box = `absolute line-clamp-2 h-9 w-37.5 rounded-md border px-1.75 py-0.5 text-tiny ${focusRing}`

/** The skills a problem needs (in the accent colour) with everything they rest on, what is needed
 *  first to the left, joined by the prerequisite links, in a frame. A box goes to the skill in the
 *  curriculum tree. The heading above it is the detail pane's. */
export function ProblemSkillGraph({ skills }: { skills: GraphSkill[] }) {
  const nodes = useMemo(() => skills.map((skill) => ({ id: skill.skill_id, requires: skill.requires })), [skills])
  const layout = graphLayout(nodes, true)
  const needed = new Set(skills.filter((skill) => skill.needed).map((skill) => skill.skill_id))

  return (
    <div className="w-fit max-w-full overflow-x-auto rounded-xl border border-line p-3" role="group" aria-label="Graf dovedností potřebných k úloze">
      <div className="relative" style={{ width: layout.width, height: layout.height }}>
        <svg className="absolute top-0 left-0 fill-none" width={layout.width} height={layout.height} aria-hidden="true">
          {layout.links.map((link) => (
            <path
              key={`${link.from} ${link.to}`}
              className={needed.has(link.to) ? 'stroke-accent' : 'stroke-edge'}
              d={link.path}
            />
          ))}
        </svg>
        {skills.map((skill) => {
          const at = layout.spots.get(skill.skill_id)!
          return (
            <Link
              key={skill.skill_id}
              to={treeUrl(skill.skill_id)}
              className={`${box} ${
                skill.needed ? 'border-accent bg-accent-soft font-semibold text-accent' : 'border-edge bg-page hover:bg-tint'
              }`}
              style={{ left: at.x, top: at.y }}
              title={`${skill.name} – ${skill.topic}`}
            >
              {skill.name}
            </Link>
          )
        })}
      </div>
    </div>
  )
}
