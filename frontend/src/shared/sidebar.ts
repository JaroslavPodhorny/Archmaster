import { createContext } from 'react'

/** Whether the app's sidebar is hidden, and how to bring it back. The shell (src/Sidebar.tsx) provides
 *  it; a page's bar reads it through SidebarButton. */
export type SidebarControl = { hidden: boolean; show: () => void }

export const SidebarContext = createContext<SidebarControl>({ hidden: false, show: () => {} })
