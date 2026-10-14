// The few icons the app uses. Each stands on a control with its usual meaning, never for decoration.

const stroke = {
  fill: 'none',
  stroke: 'currentColor',
  strokeWidth: 1.5,
  strokeLinecap: 'round',
  strokeLinejoin: 'round',
  'aria-hidden': true,
} as const

/** An arrow pointing right, after the label of a link that leads to another page. */
export function ArrowIcon({ size = 16 }: { size?: number }) {
  return (
    <svg width={size} height={size} viewBox="0 0 16 16" {...stroke}>
      <path d="M3 8h10M9 4l4 4-4 4" />
    </svg>
  )
}

/** A chevron pointing up or down: the previous or next thing in a list. */
export function ChevronIcon({ direction }: { direction: 'up' | 'down' }) {
  return (
    <svg width="18" height="18" viewBox="0 0 18 18" {...stroke}>
      <path d={direction === 'up' ? 'M4.5 11.25 9 6.75l4.5 4.5' : 'M4.5 6.75 9 11.25l4.5-4.5'} />
    </svg>
  )
}

/** A panel with its left edge marked: the usual sign for showing or hiding a sidebar. */
export function PanelIcon() {
  return (
    <svg width="20" height="20" viewBox="0 0 20 20" {...stroke}>
      <rect x="2.75" y="3.75" width="14.5" height="12.5" rx="2.5" />
      <path d="M7.75 3.75v12.5" />
    </svg>
  )
}
