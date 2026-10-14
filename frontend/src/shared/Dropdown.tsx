import { useEffect, useLayoutEffect, useRef, useState, type ReactNode } from 'react'
import { button, buttonActive } from './controls'

type Props = {
  label: string
  /** Marks the button when the filter behind it is in use. */
  active?: boolean
  wide?: boolean
  children: ReactNode
}

/** A button that opens a small panel below itself. Closes on outside click or Escape (which gives the
 *  keyboard focus back to the button). */
export function Dropdown({ label, active = false, wide = false, children }: Props) {
  const [open, setOpen] = useState(false)
  const root = useRef<HTMLDivElement>(null)
  const panel = useRef<HTMLDivElement>(null)
  const toggle = useRef<HTMLButtonElement>(null)

  useEffect(() => {
    if (!open) return
    function onPointerDown(e: PointerEvent) {
      if (!root.current?.contains(e.target as Node)) setOpen(false)
    }
    function onKeyDown(e: KeyboardEvent) {
      if (e.key !== 'Escape') return
      setOpen(false)
      if (root.current?.contains(document.activeElement)) toggle.current?.focus()
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
    <div className="relative" ref={root}>
      <button
        type="button"
        ref={toggle}
        className={active ? buttonActive : button}
        aria-expanded={open}
        onClick={() => setOpen(!open)}
      >
        {label}
        <span className="ml-2 border-4 border-b-0 border-transparent border-t-current opacity-70" aria-hidden="true" />
      </button>
      {/* Layers: sticky headings inside a pane are z-10, menus z-20, the sidebar over the page z-30 and z-40. */}
      {open && (
        <div
          className={`absolute top-[calc(100%+6px)] left-0 z-20 max-h-[70dvh] max-w-[calc(100vw-16px)] min-w-60 overflow-y-auto rounded-2xl bg-raised p-1.5 shadow-panel ${
            wide ? 'w-120 max-sm:w-[calc(100vw-16px)]' : ''
          }`}
          ref={panel}
        >
          {children}
        </div>
      )}
    </div>
  )
}
