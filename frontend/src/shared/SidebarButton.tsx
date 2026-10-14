import { useContext } from 'react'
import { iconButton } from './controls'
import { PanelIcon } from './icons'
import { SidebarContext } from './sidebar'

/** The button that brings the hidden sidebar back. Every page puts it first in its bar; it shows only
 *  while the sidebar is hidden, and never on a phone, where the navigation is a row above the page.
 *  It reaches into the bar's px-6 so that it stands 10 px from the left, where the sidebar's own
 *  button stands. */
export function SidebarButton() {
  const { hidden, show } = useContext(SidebarContext)
  if (!hidden) return null
  return (
    <button
      type="button"
      className={`${iconButton} -ml-3.5 max-sm:hidden`}
      data-sidebar-toggle
      aria-label="Zobrazit postranní panel"
      title="Zobrazit postranní panel"
      onClick={show}
    >
      <PanelIcon />
    </button>
  )
}
