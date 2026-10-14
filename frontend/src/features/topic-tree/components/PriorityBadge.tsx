import { PRIORITY_MEANING } from '../labels'
import type { Priority } from '../types'

// The darker the badge, the more tests need the skill.
const COLOURS: Record<Priority, string> = {
  '1': 'bg-ink text-page',
  '2': 'bg-muted text-page',
  '3': 'border border-edge text-muted',
  S: 'border border-dashed border-edge text-faint',
}

/** A skill's priority as a small badge ("1", "2", "3", "S"); its rule on hover. */
export function PriorityBadge({ priority }: { priority: Priority }) {
  return (
    <span
      className={`grid h-5 min-w-5 flex-none place-items-center rounded-md px-1 text-tiny font-semibold ${COLOURS[priority]}`}
      title={`Priorita ${priority}: ${PRIORITY_MEANING[priority]}`}
    >
      {priority}
    </span>
  )
}
