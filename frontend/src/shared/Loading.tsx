import { useEffect, useState } from 'react'
import { message } from './controls'

/** "Načítám…" for data that is slow to come. It shows only after a moment, so a fast load never
 *  flashes it. */
export function Loading() {
  const [shown, setShown] = useState(false)
  useEffect(() => {
    const timer = setTimeout(() => setShown(true), 400)
    return () => clearTimeout(timer)
  }, [])
  return shown ? <p className={message}>Načítám…</p> : null
}
