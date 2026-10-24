import { useEffect, useRef, useState, useSyncExternalStore, type ReactNode } from 'react'
import { NavLink } from 'react-router'
import { focusRing, iconButton } from './shared/controls'
import { PROBLEMS_PATH, TREE_PATH } from './shared/routes'
import { SidebarContext } from './shared/sidebar'
import { PanelIcon } from './shared/icons'
import { ThemeSwitch } from './ThemeSwitch'

// From this width the sidebar sits beside the page; below it, it would leave the panes too little room,
// so it opens over the page instead.
const WIDE = '(min-width: 1024px)'

function subscribeToWidth(onChange: () => void) {
  const query = window.matchMedia(WIDE)
  query.addEventListener('change', onChange)
  return () => query.removeEventListener('change', onChange)
}

function isWide(): boolean {
  return window.matchMedia(WIDE).matches
}

// Whether the sidebar beside the page is shown is a preference of this browser, not state of a page,
// so it is remembered here and not in the address.
const STORAGE_KEY = 'archmaster.sidebar'

function readDocked(): boolean {
  try {
    return localStorage.getItem(STORAGE_KEY) !== 'closed'
  } catch {
    return true
  }
}

function saveDocked(open: boolean) {
  try {
    localStorage.setItem(STORAGE_KEY, open ? 'open' : 'closed')
  } catch {
    // Storage may be blocked (private window); the choice then lasts until the page is reloaded.
  }
}

const navLink = ({ isActive }: { isActive: boolean }) =>
  `block rounded-lg px-3 py-2 whitespace-nowrap ${focusRing} ${isActive ? 'bg-selected font-medium' : 'hover:bg-tint'}`

type PanelProps = {
  onHide: () => void
  /** Called when a page is chosen. */
  onNavigate?: () => void
}

/** What the sidebar holds: the app's name with the button that hides the sidebar, a link to every page,
 *  and at the bottom the subject and the colour theme. */
function Panel({ onHide, onNavigate }: PanelProps) {
  return (
    <>
      {/* The button stands exactly where SidebarButton stands in a page's bar while the sidebar is
          hidden (10 px from the left, centred on the bar's first row), so it never moves when toggled.
          Its box lines up with the links' rows and its icon with their text, which the bottom part
          shares (px-3). */}
      <div className="flex h-10 items-center gap-1 max-sm:h-auto max-sm:pl-1.5 b">
        <button
          type="button"
          className={`${iconButton} max-sm:hidden`}
          data-sidebar-toggle
          aria-label="Skrýt postranní panel"
          title="Skrýt postranní panel"
          onClick={onHide}
        >
          <PanelIcon />
        </button>
       
      </div>

      <nav className="mt-4 flex flex-col gap-0.5 max-sm:mt-0 max-sm:min-w-0 max-sm:flex-row max-sm:overflow-x-auto">
        <NavLink to={TREE_PATH} className={navLink} onClick={onNavigate}>
          Strom učiva
        </NavLink>
        <NavLink to={PROBLEMS_PATH} className={navLink} onClick={onNavigate}>
          Databáze úloh
        </NavLink>
      </nav>

      <div className="mt-auto border-t border-line px-3 pt-3 pb-1 max-sm:hidden">
        <p className="font-medium">Matematika M9</p>
        <p className="text-small text-muted">Přijímací zkouška z 9. ročníku</p>
        <div className="mt-3">
          <ThemeSwitch />
        </div>
      </div>
    </>
  )
}

/** The app's frame: the sidebar with the navigation on the left and the page beside it. On a wide window
 *  the sidebar sits beside the page until the user hides it (remembered); then it is gone, and the button
 *  that brings it back sits at the start of the page's bar (SidebarButton). On a narrower window that
 *  button opens it over the page until a page is chosen, the page is clicked or Escape is pressed. On a
 *  phone the navigation is a row above the page instead. */
export function WithSidebar({ children }: { children: ReactNode }) {
  const wide = useSyncExternalStore(subscribeToWidth, isWide)
  const [docked, setDocked] = useState(readDocked)
  const [overlay, setOverlay] = useState(false)
  // An overlay open on a narrow window ends when the window becomes wide, so it does not come back by itself.
  if (wide && overlay) setOverlay(false)
  const column = wide && docked
  const overlayOpen = overlay && !wide
  const toggled = useRef(false)

  // The pressed button disappears with what it showed or hid; its counterpart stands in the same place,
  // so the keyboard focus moves there. Of the buttons shown, the last in the page is the one on top:
  // the overlay's comes after the page's.
  useEffect(() => {
    if (!toggled.current) return
    toggled.current = false
    const buttons = [...document.querySelectorAll<HTMLElement>('[data-sidebar-toggle]')]
    buttons.findLast((el) => el.getClientRects().length > 0)?.focus()
  }, [column, overlayOpen])

  function setColumn(open: boolean) {
    toggled.current = true
    saveDocked(open)
    setDocked(open)
  }

  function closeOverlay() {
    toggled.current = true
    setOverlay(false)
  }

  function show() {
    if (wide) setColumn(true)
    else {
      toggled.current = true
      setOverlay(true)
    }
  }

  useEffect(() => {
    if (!overlayOpen) return
    function onKeyDown(e: KeyboardEvent) {
      if (e.key === 'Escape') closeOverlay()
    }
    document.addEventListener('keydown', onKeyDown)
    return () => document.removeEventListener('keydown', onKeyDown)
  }, [overlayOpen])

  return (
    <SidebarContext value={{ hidden: !column, show }}>
      <div className="flex h-dvh max-sm:flex-col">
        <aside
          className={`flex w-60 flex-none flex-col border-r border-line bg-surface px-2.5 pt-3.5 pb-2.5 max-sm:w-full max-sm:flex-row max-sm:items-center max-sm:gap-3 max-sm:border-r-0 max-sm:border-b max-sm:py-2 ${
            column ? '' : 'sm:hidden'
          }`}
        >
          <Panel onHide={() => setColumn(false)} />
        </aside>
        {/* While the sidebar is open over it, the page cannot be reached with Tab or clicked. */}
        <main className="min-h-0 min-w-0 flex-1" inert={overlayOpen}>
          {children}
        </main>
      </div>

      {overlayOpen && (
        <div className="max-sm:hidden">
          <div className="fixed inset-0 z-30 bg-shade" aria-hidden="true" onClick={closeOverlay} />
          <aside className="fixed inset-y-0 left-0 z-40 flex w-60 flex-col bg-surface px-2.5 pt-3.5 pb-2.5 shadow-panel">
            <Panel onHide={closeOverlay} onNavigate={() => setOverlay(false)} />
          </aside>
        </div>
      )}
    </SidebarContext>
  )
}
