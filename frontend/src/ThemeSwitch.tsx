import { useState } from 'react'
import { switchOption, switchOptionOff, switchOptionOn, switchTrack } from './shared/controls'

type Theme = 'light' | 'dark' | 'system'

const THEMES: Theme[] = ['light', 'dark', 'system']
const NAMES: Record<Theme, string> = { light: 'Světlý', dark: 'Tmavý', system: 'Systém' }
const HINTS: Record<Theme, string> = {
  light: 'Vždy světlý vzhled',
  dark: 'Vždy tmavý vzhled',
  system: 'Světlý nebo tmavý podle nastavení systému',
}

// index.html reads the same key to set the theme before the page is drawn.
const STORAGE_KEY = 'archmaster.theme'

function readTheme(): Theme {
  try {
    const saved = localStorage.getItem(STORAGE_KEY)
    if (saved === 'light' || saved === 'dark') return saved
  } catch {
    // Storage may be blocked (private window); the system's theme applies.
  }
  return 'system'
}

/** Sets the theme on <html> the way index.html does. */
function apply(theme: Theme) {
  const dark = theme === 'dark' || (theme === 'system' && window.matchMedia('(prefers-color-scheme: dark)').matches)
  document.documentElement.dataset.theme = dark ? 'dark' : 'light'
}

/** Light, dark, or whatever the system uses; remembered in this browser. */
export function ThemeSwitch() {
  const [theme, setTheme] = useState(readTheme)

  function choose(next: Theme) {
    try {
      if (next === 'system') localStorage.removeItem(STORAGE_KEY)
      else localStorage.setItem(STORAGE_KEY, next)
    } catch {
      // Without storage the choice lasts until the page is reloaded.
    }
    apply(next)
    setTheme(next)
  }

  return (
    <div className={switchTrack} role="group" aria-label="Vzhled">
      {THEMES.map((option) => (
        <button
          key={option}
          type="button"
          className={`${switchOption} flex-1 px-1.5 text-small ${theme === option ? switchOptionOn : switchOptionOff}`}
          aria-pressed={theme === option}
          title={HINTS[option]}
          onClick={() => choose(option)}
        >
          {NAMES[option]}
        </button>
      ))}
    </div>
  )
}
