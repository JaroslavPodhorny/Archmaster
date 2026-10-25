import { useState } from 'react'
import { switchOption, switchOptionOff, switchOptionOn, switchTrack } from './shared/controls'

type Theme = 'light' | 'dark'

const THEMES: Theme[] = ['light', 'dark']
const NAMES: Record<Theme, string> = { light: 'Světlý', dark: 'Tmavý' }

// index.html reads the same key to set the theme before the page is drawn.
const STORAGE_KEY = 'archmaster.theme'

/** The theme index.html set: the saved one, or the system's until one is chosen. */
function readTheme(): Theme {
  return document.documentElement.dataset.theme === 'dark' ? 'dark' : 'light'
}

/** Sets the theme on <html> the way index.html does. */
function apply(theme: Theme) {
  document.documentElement.dataset.theme = theme
}

/** Light or dark; remembered in this browser. */
export function ThemeSwitch() {
  const [theme, setTheme] = useState(readTheme)

  function choose(next: Theme) {
    try {
      localStorage.setItem(STORAGE_KEY, next)
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
          onClick={() => choose(option)}
        >
          {NAMES[option]}
        </button>
      ))}
    </div>
  )
}
