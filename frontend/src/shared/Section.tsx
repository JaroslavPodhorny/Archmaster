import type { ReactNode } from 'react'
import { hint } from './controls'

type Props = {
  title: string
  /** In grey after the heading: a count, or how the list below is ordered. */
  aside?: ReactNode
  children: ReactNode
}

/** A part of a detail pane: a thin line above it and its heading, so it is clear what belongs together. */
export function Section({ title, aside, children }: Props) {
  return (
    <section className="mt-6 border-t border-line pt-5">
      <h3 className="mb-3 flex flex-wrap items-baseline gap-x-2">
        <span className="font-semibold">{title}</span>
        {aside !== undefined && <span className={hint}>{aside}</span>}
      </h3>
      {children}
    </section>
  )
}
