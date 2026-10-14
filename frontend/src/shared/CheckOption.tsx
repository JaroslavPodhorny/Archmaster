import type { ReactNode } from 'react'

type Props = {
  label: ReactNode
  /** How many things have this value, shown at the right. */
  count?: number
  checked: boolean
  onChange: () => void
  /** What the value means, on hover. */
  title?: string
  className?: string
}

/** One line of a filter menu: a checkbox, the value's name and how many things have it. */
export function CheckOption({ label, count, checked, onChange, title, className = '' }: Props) {
  return (
    <label className={`flex cursor-pointer items-baseline gap-2.5 rounded-lg px-2.5 py-1.5 hover:bg-selected ${className}`} title={title}>
      <input type="checkbox" checked={checked} onChange={onChange} />
      <span>{label}</span>
      {count !== undefined && <span className="ml-auto pl-2 text-small text-muted tabular-nums">{count}</span>}
    </label>
  )
}
