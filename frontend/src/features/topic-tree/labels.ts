// Czech wording used by the curriculum tree page.

import type { Kind, Priority } from './types'

export const PRIORITIES: Priority[] = ['1', '2', '3', 'S']

/** A priority as a filter menu names it; PRIORITY_MEANING says it exactly. */
export const PRIORITY_NAMES: Record<Priority, string> = {
  '1': '1 – nejčastěji potřeba',
  '2': '2 – občas potřeba',
  '3': '3 – vzácně potřeba',
  S: 'S – jen ve specifikaci',
}

/** A priority in words, beside its badge. */
export const PRIORITY_LABELS: Record<Priority, string> = {
  '1': 'Nejčastěji potřeba',
  '2': 'Občas potřeba',
  '3': 'Vzácně potřeba',
  S: 'Jen ve specifikaci',
}

/** The term of a test by its letter in an item's reference ("2025 A 15.2"). */
export const TERM_NAMES: Record<string, string> = {
  A: '1. řádný',
  B: '2. řádný',
  C: '1. náhradní',
  D: '2. náhradní',
}


/** The years of the last 8 tests, joined so that a line never breaks at the dash. */
export const RECENT_YEARS = '2025–\u20602026'

/** "Standard tests" are the 16 tests of 2022, 2023, 2025 and 2026; the 2024 tests follow a different design. */
export const PRIORITY_MEANING: Record<Priority, string> = {
  '1': 'sama nebo přes dovednost, která na ni navazuje, je potřeba nejméně v 10 ze 16 standardních testů, nebo v 6 z 8 testů 2025–2026',
  '2': 'je potřeba nejméně ve 4 ze 16 standardních testů, nebo ve 3 z 8 posledních',
  '3': 'vzácnější, nebo jen v testech 2024',
  S: 'je ve specifikaci, ale nepotřebuje ji žádná úloha z 20 testů',
}

export const STANDARD_TESTS_NOTE =
  'Standardní testy: 16 testů z let 2022, 2023, 2025 a 2026. Testy 2024 mají jinou stavbu a nepočítají se.'

export const KIND_NAMES: Record<Kind, string> = {
  procedure: 'postup',
  translation: 'překlad',
  fact: 'znalost',
  strategy: 'rozbor',
}

export const KIND_MEANING: Record<Kind, string> = {
  procedure: 'postup, který se procvičuje do rychlosti a bezchybnosti',
  translation: 'převod českého zadání do matematiky',
  fact: 'fakt nebo vlastnost, kterou je třeba znát zpaměti',
  strategy: 'hledání cesty vícekrokovou úlohou',
}

export function capitalized(text: string): string {
  return text.charAt(0).toUpperCase() + text.slice(1)
}

// Ties round to even, as in analysis/04_strom_M9.md, so the page and the document show the same numbers.
const oneDecimal = new Intl.NumberFormat('cs-CZ', {
  minimumFractionDigits: 1,
  maximumFractionDigits: 1,
  roundingMode: 'halfEven',
})
const whole = new Intl.NumberFormat('cs-CZ', { maximumFractionDigits: 0, roundingMode: 'halfEven' })

/** Points per test: "1,4". */
export function pointsLabel(points: number): string {
  return oneDecimal.format(points)
}

export function percentLabel(value: number): string {
  return `${whole.format(value)}\u00a0%`
}

/** "úloha" in the form that follows "Zobrazit": 1 úlohu, 2 úlohy, 5 úloh. */
export function problemsToShowLabel(count: number): string {
  if (count === 1) return '1 úlohu'
  return count >= 2 && count <= 4 ? `${count} úlohy` : `${count} úloh`
}

/** Heading of a column of the graph: how long the longest chain of prerequisites before its skills is. */
export function stepsLabel(steps: number): string {
  if (steps === 0) return 'Nic nepotřebuje'
  if (steps === 1) return '1 krok před ní'
  return steps <= 4 ? `${steps} kroky` : `${steps} kroků`
}

export const STEPS_NOTE =
  'Sloupec říká, kolik kroků má nejdelší řetěz předpokladů před dovedností. Co dovednost potřebuje, je vždy vlevo od ní.'
