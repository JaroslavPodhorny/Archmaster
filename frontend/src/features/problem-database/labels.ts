// Czech wording used by the problem database page.

import type { FilterName, FilterOptions, FilterValue, OrderBy } from './types'

export const FILTER_TITLES: Record<FilterName, string> = {
  years: 'Rok',
  terms: 'Termín',
  skills: 'Téma',
  formats: 'Typ úlohy',
  points: 'Body',
}

/** The order the filters are shown in. */
export const FILTER_ORDER: FilterName[] = ['years', 'terms', 'skills', 'formats', 'points']

export const ORDERINGS: Record<OrderBy, string> = {
  newest: 'Nejnovější',
  oldest: 'Nejstarší',
  hardest: 'Nejtěžší',
  easiest: 'Nejlehčí',
}

/** The backend's Czech label for a filter value, e.g. "A" -> "1. řádný termín". */
export function optionLabel(options: FilterOptions | null, name: FilterName, value: FilterValue): string {
  return options?.[name].find((o) => o.value === value)?.label ?? String(value)
}

export function pointsLabel(points: number): string {
  if (points === 1) return '1 bod'
  return points < 5 ? `${points} body` : `${points} bodů`
}

export function percentLabel(value: number): string {
  return `${value.toFixed(0)}\u00a0%`
}

export function successLabel(value: number | null): string {
  return value === null ? '–' : percentLabel(value)
}

/** "úloha" in the right grammatical form for a count. */
export function problemCountLabel(count: number): string {
  if (count === 1) return '1 úloha'
  return count >= 2 && count <= 4 ? `${count} úlohy` : `${count} úloh`
}

/** "dovednost" in the right grammatical form for a count. */
export function skillCountLabel(count: number): string {
  if (count === 1) return '1 dovednost'
  return count >= 2 && count <= 4 ? `${count} dovednosti` : `${count} dovedností`
}
