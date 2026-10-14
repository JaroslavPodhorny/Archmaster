// Czech wording used by the exam graph page.

import type { View } from './types'

export const VIEWS: View[] = ['uloha', 'princip', 'zkouska']
export const VIEW_NAMES: Record<View, string> = { uloha: 'Úloha', princip: 'Princip', zkouska: 'Zkouška' }
export const VIEW_HINTS: Record<View, string> = {
  uloha: 'Postup řešení úlohy po krocích',
  princip: 'Princip s tím, na čem stojí a co na něm stojí',
  zkouska: 'Test proti všem dvaceti: sloty, principy, pokrytí',
}

export const TERM_NAMES: Record<string, string> = { A: '1. řádný', B: '2. řádný', C: '1. náhradní', D: '2. náhradní' }

/** "2025 B" -> "2025, 2. řádný". */
export function testName(test: string): string {
  const [year, term] = test.split(' ')
  return `${year}, ${TERM_NAMES[term]}`
}

/** "2025 B" <-> "2025-B", as the address has it. */
export const testToAddress = (test: string) => test.replace(' ', '-')
export const testFromAddress = (test: string) => test.replace('-', ' ')

export const FORMAT_NAMES: Record<string, string> = {
  OV: 'otevřená, jen výsledek',
  OP: 'otevřená s postupem',
  'OV+OP': 'otevřená, část s postupem',
  K: 'konstrukční',
  AN: 'svazek ano/ne',
  MC: 'výběr z pěti možností',
  PR: 'přiřazovací',
}

/** A whole percentage, or one decimal where small differences matter (shares of options). */
export function percentLabel(value: number, decimals = 0): string {
  return `${value.toFixed(decimals).replace('.', ',')} %`
}

export function successLabel(value: number | null): string {
  return value === null ? '–' : percentLabel(value)
}

function number(value: number): string {
  return Number.isInteger(value) ? String(value) : value.toFixed(1).replace('.', ',')
}

/** "bod" in the right form: 1 bod, 2 body, 5 bodů, 1,3 bodu. */
export function pointsLabel(points: number): string {
  if (!Number.isInteger(points)) return `${number(points)} bodu`
  if (points === 1) return '1 bod'
  return points >= 2 && points <= 4 ? `${points} body` : `${points} bodů`
}

function counted(count: number, one: string, few: string, many: string): string {
  if (count === 1) return `1 ${one}`
  return count >= 2 && count <= 4 ? `${count} ${few}` : `${count} ${many}`
}

export const stepCountLabel = (n: number) => counted(n, 'krok', 'kroky', 'kroků')
export const itemCountLabel = (n: number) => counted(n, 'položka', 'položky', 'položek')
export const taskCountLabel = (n: number) => counted(n, 'úloha', 'úlohy', 'úloh')
export const principleCountLabel = (n: number) => counted(n, 'princip', 'principy', 'principů')

/** "z 20 testů" after a count: "1 z 20 testů", "2 z 20 testů". */
export function ofTestsLabel(count: number, total: number): string {
  return `${count} z ${total} testů`
}

/** Keeps digit groups ("3 600") and a number with its unit together on one line. */
export function keptTogether(text: string): string {
  return text.replace(/(\d) (?=\d{3}\b)/g, '$1 ').replace(/(\d) (cm|mm|dm|m|km|Kč|%|°)/g, '$1 $2')
}

/** Lower case without diacritics, for searching. */
export function fold(text: string): string {
  return text.normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase()
}

export const ANSWER_STATES: Record<string, string> = {
  'shoda-s-klicem': 'shodné s klíčem',
  'prevzato-z-klice': 'převzaté z klíče, nepočítané nezávisle',
  'bez-klice': 'bez klíče, nic je neověřilo',
}

export const REVIEW_STATES: Record<string, string> = {
  navrh: 'návrh, čeká na kontrolu',
  zkontrolovano: 'zkontrolováno',
}
