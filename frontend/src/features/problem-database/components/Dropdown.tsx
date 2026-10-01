import { useEffect, useLayoutEffect, useRef, useState, type ReactNode } from 'react'

type Props = {
  label: string
  /** Marks the button when the filter behind it is in use. */
  active?: boolean
  wide?: boolean
  children: ReactNode
}

/** A button that opens a small panel below itself. Closes on outside click or Escape. */
export function Dropdown({ label, active = false, wide = false, children }: Props) {
  const [open, setOpen] = useState(false)
  const root = useRef<HTMLDivElement>(null)
  const panel = useRef<HTMLDivElement>(null)

  useEffect(() => {
    if (!open) return
    function onPointerDown(e: PointerEvent) {
      if (!root.current?.contains(e.target as Node)) setOpen(false)
    }
    function onKeyDown(e: KeyboardEvent) {
      if (e.key === 'Escape') setOpen(false)
    }
    document.addEventListener('pointerdown', onPointerDown)
    document.addEventListener('keydown', onKeyDown)
    return () => {
      document.removeEventListener('pointerdown', onPointerDown)
      document.removeEventListener('keydown', onKeyDown)
    }
  }, [open])

  // Keep the panel inside the window when the button sits near the right edge.
  useLayoutEffect(() => {
    const el = panel.current
    if (!open || !el) return
    el.style.transform = ''
    const overflow = el.getBoundingClientRect().right - (window.innerWidth - 8)
    if (overflow > 0) el.style.transform = `translateX(${-overflow}px)`
  }, [open])

  return (
    <div className="pd-dropdown" ref={root}>
      <button
        type="button"
        className={active ? 'pd-button pd-button-active' : 'pd-button'}
        aria-expanded={open}
        onClick={() => setOpen(!open)}
      >
        {label}
        <span className="pd-caret" aria-hidden="true" />
      </button>
      {open && (
        <div className={wide ? 'pd-panel pd-panel-wide' : 'pd-panel'} ref={panel}>
          {children}
        </div>
      )}
    </div>
  )
}
