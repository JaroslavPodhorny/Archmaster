// Where the given facts and the steps of one route stand in the solution flow of a task.
//
// The flow reads from top to bottom: the given facts in the first row, then one column per item, each step
// in its item's column, below everything it uses. The prerequisite graphs of the other pages are laid out
// by shared/graphLayout.ts, which places skills of the tree in columns by their longest chain of
// prerequisites; a flow has items as columns and boxes of two sizes, so it has this small layout of its own.

import type { Route, TaskDetail } from './types'

export const BOX_W = 184
/** A step: its result on up to three lines and its principle on one. */
export const BOX_H = 76
/** An answer has a line more: the item and how many students solved it. */
export const ANSWER_H = 92
const COLUMN_GAP = 40
const ROW_GAP = 30
/** Between two rows of given facts, which no link joins. */
const GIVEN_GAP = 8
/** Room above the first row of steps for the items' names. */
const TITLE_H = 24

export type Spot = { x: number; y: number; height: number; row: number }

export type FlowLink = {
  from: string
  to: string
  path: string
  /** The result comes from another item's steps. */
  reused: boolean
}

export type FlowLayout = {
  spots: Map<string, Spot>
  links: FlowLink[]
  /** The items' names above their columns. */
  titles: { item: string; x: number; y: number }[]
  width: number
  height: number
}

/** A path through the points with its corners rounded. */
function rounded(points: [number, number][], radius = 6): string {
  let d = `M${points[0][0]} ${points[0][1]}`
  for (let i = 1; i < points.length - 1; i++) {
    const [px, py] = points[i - 1]
    const [cx, cy] = points[i]
    const [nx, ny] = points[i + 1]
    const r1 = Math.min(radius, Math.hypot(cx - px, cy - py) / 2)
    const r2 = Math.min(radius, Math.hypot(nx - cx, ny - cy) / 2)
    d += ` L${cx - Math.sign(cx - px) * r1} ${cy - Math.sign(cy - py) * r1}`
    d += ` Q${cx} ${cy} ${cx + Math.sign(nx - cx) * r2} ${cy + Math.sign(ny - cy) * r2}`
  }
  const [lx, ly] = points[points.length - 1]
  return `${d} L${lx} ${ly}`
}

/** Places a route: the given facts first, in as many rows as they need; then each step one row below the
 *  lowest step it uses, in its item's column, and down
 *  again while that place is taken, so two steps of one item never share a row. A link to the next row is
 *  a curve; a longer one leaves the box, runs down the gap beside the columns and comes back, so it
 *  crosses no box. Links from the given facts are not drawn (the page shows them for a selected step). */
export function flowLayout(task: TaskDetail, route: Route): FlowLayout {
  const byId = new Map(route.steps.map((step) => [step.id, step]))
  const column = new Map(task.items.map((item, i) => [item.item, i]))
  const row = new Map<string, number>()
  const taken = new Set<string>()
  for (const step of route.steps) {
    let r = 1 + Math.max(0, ...step.inputs.filter((id) => byId.has(id)).map((id) => row.get(id)!))
    while (taken.has(`${column.get(step.item)} ${r}`)) r++
    taken.add(`${column.get(step.item)} ${r}`)
    row.set(step.id, r)
  }

  // The given facts fill rows as wide as the items' columns (at least three wide), so they never widen the flow much.
  const perRow = Math.max(task.items.length, Math.min(task.given.length, 3))
  const givenRows = Math.ceil(task.given.length / perRow)
  const columns = Math.max(task.items.length, Math.min(task.given.length, perRow))
  const x = (c: number) => c * (BOX_W + COLUMN_GAP)
  const rows = Math.max(0, ...row.values())
  const heights = [givenRows * BOX_H + (givenRows - 1) * GIVEN_GAP]
  for (let r = 1; r <= rows; r++) {
    heights.push(route.steps.some((step) => row.get(step.id) === r && step.answer) ? ANSWER_H : BOX_H)
  }
  const tops = [0]
  for (let r = 1; r <= rows; r++) tops.push(tops[r - 1] + heights[r - 1] + ROW_GAP + (r === 1 ? TITLE_H : 0))

  const spots = new Map<string, Spot>()
  task.given.forEach((given, n) =>
    spots.set(given.id, { x: x(n % perRow), y: Math.floor(n / perRow) * (BOX_H + GIVEN_GAP), height: BOX_H, row: 0 }),
  )
  for (const step of route.steps) {
    const r = row.get(step.id)!
    spots.set(step.id, { x: x(column.get(step.item)!), y: tops[r], height: step.answer ? ANSWER_H : BOX_H, row: r })
  }

  const gaps = Array.from({ length: columns + 1 }, (_, c) => x(c) - COLUMN_GAP / 2)
  const links: FlowLink[] = []
  for (const step of route.steps) {
    for (const input of step.inputs) {
      if (!byId.has(input)) continue
      const a = spots.get(input)!
      const b = spots.get(step.id)!
      const [x1, y1, x2, y2] = [a.x + BOX_W / 2, a.y + a.height, b.x + BOX_W / 2, b.y - 1]
      let path: string
      if (b.row - a.row === 1) {
        const mid = (y1 + y2) / 2
        path = `M${x1} ${y1} C${x1} ${mid} ${x2} ${mid} ${x2} ${y2}`
      } else {
        // The gap nearest to halfway between the two columns; to the left when both are equally near.
        const half = (x1 + x2) / 2 - 1
        const gap = gaps.reduce((best, g) => (Math.abs(g - half) < Math.abs(best - half) ? g : best))
        const below = y1 + ROW_GAP / 2 - 3
        const above = b.y - ROW_GAP / 2 + 3
        path = rounded([[x1, y1], [x1, below], [gap, below], [gap, above], [x2, above], [x2, y2]])
      }
      links.push({ from: input, to: step.id, path, reused: byId.get(input)!.item !== step.item })
    }
  }

  return {
    spots,
    links,
    titles: task.items.map((item, c) => ({ item: item.item, x: x(c), y: tops[1] - TITLE_H - 4 })),
    width: x(columns - 1) + BOX_W,
    height: tops[rows] + heights[rows],
  }
}
