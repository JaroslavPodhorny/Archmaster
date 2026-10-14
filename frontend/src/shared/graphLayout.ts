// Where every skill stands in a graph of prerequisite links: the whole curriculum tree, or the
// skills one problem needs.

/** A node of the curriculum tree. Only skills ("POC.VYR.poradi") are placed; areas and topics are skipped. */
export type GraphNode = { id: string; requires: string[] }

// Box size (the same as w-37.5 h-9 in the boxes drawn on it) and the gaps between columns and rows, in pixels.
export const BOX_W = 150
export const BOX_H = 36
const GAP_X = 56
const GAP_Y = 8
/** Between groups of skills that no link joins. */
const GROUP_GAP = 28
/** Height a link takes in a column it only passes. */
const THREAD = 6
// How hard the ordering is searched: starting orders tried, and sweeps over the columns from each.
const STARTS = 100
const SWEEPS = 24

export type Spot = {
  x: number
  y: number
  column: number
  /** False for a skill that needs nothing and that nothing builds on; those are listed under the graph. */
  linked: boolean
}

export type GraphLink = { from: string; to: string; path: string }

export type GraphLayout = {
  spots: Map<string, Spot>
  links: GraphLink[]
  /** Columns of the linked part; a skill's column is the longest chain of prerequisites before it. */
  columns: number
  width: number
  height: number
  /** The list of unlinked skills: where it starts, and the area each of its rows belongs to. */
  alone: { top: number; count: number; areas: { id: string; y: number }[] }
}

/** A box, or the place a longer link takes in a column it passes. */
type Item = {
  column: number
  height: number
  group: number
  /** What it is joined to in the column before and in the column after. */
  up: Item[]
  down: Item[]
  /** Place in learning order, of the skill or of the skill the link leads to. */
  start: number
  order: number
  y: number
}

export function columnX(column: number): number {
  return column * (BOX_W + GAP_X)
}

function sortBy(list: Item[], key: Map<Item, number>) {
  list.sort((a, b) => a.group - b.group || key.get(a)! - key.get(b)!)
  list.forEach((item, i) => (item.order = i))
}

function crossings(byColumn: Item[][]): number {
  let n = 0
  for (const list of byColumn.slice(1)) {
    const pairs = list.flatMap((item) => item.up.map((above) => [above.order, item.order]))
    for (let i = 0; i < pairs.length; i++)
      for (let j = i + 1; j < pairs.length; j++)
        if ((pairs[i][0] - pairs[j][0]) * (pairs[i][1] - pairs[j][1]) < 0) n++
  }
  return n
}

/** Crossings between the links of two items of a column when `a` stands above `b`. */
function crossingsBetween(a: Item, b: Item): number {
  let n = 0
  for (const side of ['up', 'down'] as const)
    for (const x of a[side]) for (const y of b[side]) if (x.order > y.order) n++
  return n
}

/** Orders every column so that few links cross. From each starting order the columns are swept
 *  back and forth, every item going to the mean place of its neighbours, and then neighbours swap
 *  while that removes crossings. The first start is the learning order, the rest are shuffles of it
 *  (always the same ones, so the graph looks the same on every load). The best order stays. */
function orderColumns(items: Item[], byColumn: Item[][]) {
  const orders = () => new Map(items.map((item) => [item, item.order]))
  let seed = 1
  const random = () => (seed = (seed * 48271) % 2147483647) / 2147483647
  let best: { n: number; orders: Map<Item, number> } | null = null

  for (let start = 0; start < STARTS; start++) {
    const first = new Map(items.map((item) => [item, start === 0 ? item.start : random()]))
    byColumn.forEach((list) => sortBy(list, first))

    let swept = { n: crossings(byColumn), orders: orders() }
    for (let sweep = 0; sweep < SWEEPS; sweep++) {
      const side = sweep % 2 === 0 ? 'up' : 'down'
      for (const list of sweep % 2 === 0 ? byColumn : [...byColumn].reverse()) {
        const mean = new Map(
          list.map((item) => [
            item,
            item[side].length ? item[side].reduce((sum, near) => sum + near.order, 0) / item[side].length : item.order,
          ]),
        )
        sortBy(list, mean)
      }
      const n = crossings(byColumn)
      if (n < swept.n) swept = { n, orders: orders() }
    }
    byColumn.forEach((list) => sortBy(list, swept.orders))

    for (let swapped = true, turn = 0; swapped && turn < 40; turn++) {
      swapped = false
      for (const list of byColumn) {
        for (let i = 0; i + 1 < list.length; i++) {
          const [a, b] = [list[i], list[i + 1]]
          if (a.group !== b.group || crossingsBetween(b, a) >= crossingsBetween(a, b)) continue
          list[i] = b
          list[i + 1] = a
          b.order = i
          a.order = i + 1
          swapped = true
        }
      }
    }
    const n = crossings(byColumn)
    if (!best || n < best.n) best = { n, orders: orders() }
  }
  if (best) byColumn.forEach((list) => sortBy(list, best.orders))
}

/** Gives every item its y. A group is as tall as its fullest column; inside it the items of a column
 *  keep their order and drift towards the middle of what they are joined to. Returns the height. */
function placeRows(byColumn: Item[][], groupCount: number): number {
  const groups = Array.from({ length: groupCount }, () => ({ top: 0, height: 0 }))
  const stacks = byColumn.flatMap((list) =>
    groups.map((group, g) => ({ group, list: list.filter((item) => item.group === g) })).filter((s) => s.list.length),
  )
  for (const { group, list } of stacks) {
    group.height = Math.max(group.height, list.reduce((sum, item) => sum + item.height + GAP_Y, -GAP_Y))
  }
  let top = 0
  for (const group of groups) {
    group.top = top
    top += group.height + GROUP_GAP
  }
  for (const { group, list } of stacks) {
    let y = group.top
    for (const item of list) {
      item.y = y
      y += item.height + GAP_Y
    }
  }

  const middle = (item: Item) => item.y + item.height / 2
  for (let round = 0; round < 40; round++) {
    for (const { group, list } of round % 2 === 0 ? stacks : [...stacks].reverse()) {
      // As close to the wanted places as the order, the gaps and the group's edges allow.
      let y = group.top
      const pushedDown = list.map((item) => {
        const near = round >= 30 ? [...item.up, ...item.down] : round % 2 === 0 ? item.up : item.down
        const wanted = near.length ? near.reduce((sum, n) => sum + middle(n), 0) / near.length - item.height / 2 : item.y
        y = Math.max(y, wanted)
        const at = y
        y += item.height + GAP_Y
        return at
      })
      let limit = group.top + group.height
      for (let i = list.length - 1; i >= 0; i--) {
        list[i].y = Math.min(pushedDown[i], limit - list[i].height)
        limit = list[i].y - GAP_Y
      }
    }
  }
  return Math.max(0, top - GROUP_GAP)
}

const layouts = new WeakMap<GraphNode[], GraphLayout>()

/** The whole graph: prerequisites to the left of what needs them, one column for every step of the
 *  longest chain before a skill. Skills that no link joins to each other are kept in separate groups,
 *  one under another, and the skills without any link are listed below, area by area; with
 *  `aloneInGraph` they stand in the first column as groups of their own instead (for a small graph).
 *  Working out the whole tree takes about 0.1 s, so it is done once for a list of nodes (always asked
 *  for the same way), not every time the graph opens. */
export function graphLayout(nodes: GraphNode[], aloneInGraph = false): GraphLayout {
  if (!layouts.has(nodes)) layouts.set(nodes, layoutGraph(nodes, aloneInGraph))
  return layouts.get(nodes)!
}

function layoutGraph(nodes: GraphNode[], aloneInGraph: boolean): GraphLayout {
  const skills = nodes.filter((node) => node.id.split('.').length === 3)
  const byId = new Map(skills.map((skill) => [skill.id, skill]))
  const position = new Map(skills.map((skill, i) => [skill.id, i]))
  const needed = new Set(skills.flatMap((skill) => skill.requires))
  const linked = skills.filter((skill) => aloneInGraph || skill.requires.length > 0 || needed.has(skill.id))

  const column = new Map<string, number>()
  function columnOf(id: string): number {
    if (!column.has(id)) column.set(id, Math.max(-1, ...byId.get(id)!.requires.map(columnOf)) + 1)
    return column.get(id)!
  }
  const columns = Math.max(0, ...linked.map((skill) => columnOf(skill.id))) + 1

  // Groups: skills joined by links, whatever their direction. Each is named by its first skill.
  const head = new Map(linked.map((skill) => [skill.id, skill.id]))
  function headOf(id: string): string {
    while (head.get(id) !== id) id = head.get(id)!
    return id
  }
  for (const skill of linked) {
    for (const id of skill.requires) {
      const [a, b] = [headOf(skill.id), headOf(id)].sort((x, y) => position.get(x)! - position.get(y)!)
      head.set(b, a)
    }
  }
  const groupIds = [...new Set(linked.map((skill) => headOf(skill.id)))]

  const items: Item[] = []
  function add(of: GraphNode, at: number, height: number): Item {
    const item = { column: at, height, group: groupIds.indexOf(headOf(of.id)), up: [], down: [], start: position.get(of.id)!, order: 0, y: 0 }
    items.push(item)
    return item
  }
  const boxes = new Map(linked.map((skill) => [skill.id, add(skill, column.get(skill.id)!, BOX_H)]))
  const chains: { from: string; to: string; chain: Item[] }[] = []
  for (const skill of linked) {
    for (const id of skill.requires) {
      const chain = [boxes.get(id)!]
      for (let c = column.get(id)! + 1; c < column.get(skill.id)!; c++) chain.push(add(skill, c, THREAD))
      chain.push(boxes.get(skill.id)!)
      for (let i = 1; i < chain.length; i++) {
        chain[i].up.push(chain[i - 1])
        chain[i - 1].down.push(chain[i])
      }
      chains.push({ from: id, to: skill.id, chain })
    }
  }
  const byColumn = Array.from({ length: columns }, (_, c) => items.filter((item) => item.column === c))
  orderColumns(items, byColumn)
  const graphHeight = placeRows(byColumn, groupIds.length)
  const width = columnX(columns) - GAP_X

  const spots = new Map<string, Spot>()
  for (const [id, item] of boxes) spots.set(id, { x: columnX(item.column), y: Math.round(item.y), column: item.column, linked: true })
  const links = chains.map(({ from, to, chain }) => {
    let path = ''
    for (let i = 1; i < chain.length; i++) {
      const [a, b] = [chain[i - 1], chain[i]]
      const x1 = columnX(a.column) + BOX_W
      const x2 = columnX(b.column)
      const y1 = Math.round(a.y + a.height / 2)
      const y2 = Math.round(b.y + b.height / 2)
      const mid = (x1 + x2) / 2
      path += `${i === 1 ? 'M' : ' L'}${x1} ${y1} C${mid} ${y1} ${mid} ${y2} ${x2} ${y2}`
    }
    return { from, to, path }
  })

  // The unlinked skills: a heading, then for each area its name and its boxes in rows beside it.
  const alone = skills.filter((skill) => !boxes.has(skill.id))
  const top = graphHeight + GROUP_GAP
  const left = BOX_W + GAP_X
  const perRow = Math.max(1, Math.floor((width - left + GAP_Y) / (BOX_W + GAP_Y)))
  const areas: { id: string; y: number }[] = []
  let y = top + 44
  for (const area of new Set(alone.map((skill) => skill.id.split('.')[0]))) {
    const list = alone.filter((skill) => skill.id.startsWith(`${area}.`))
    areas.push({ id: area, y })
    list.forEach((skill, i) => {
      const [row, at] = [Math.floor(i / perRow), i % perRow]
      spots.set(skill.id, { x: left + at * (BOX_W + GAP_Y), y: y + row * (BOX_H + GAP_Y), column: at, linked: false })
    })
    y += Math.ceil(list.length / perRow) * (BOX_H + GAP_Y) + 6
  }

  return { spots, links, columns, width, height: alone.length ? y - GAP_Y - 6 : graphHeight, alone: { top, count: alone.length, areas } }
}

/** The skill an arrow key leads to from another: up and down along the column, left and right to
 *  the nearest box of the next column. `shown` says which skills are on the screen. */
export function neighbour(layout: GraphLayout, id: string, key: string, shown: (id: string) => boolean): string | null {
  const here = layout.spots.get(id)
  if (!here) return null
  const others = [...layout.spots].filter(([other]) => other !== id && shown(other))
  const sign = key === 'ArrowDown' || key === 'ArrowRight' ? 1 : -1
  const nearest = (found: [string, Spot][]) =>
    found.reduce<[string, Spot] | null>((best, one) => {
      const far = (spot: Spot) => Math.abs(spot.x - here.x) + Math.abs(spot.y - here.y)
      return best && far(best[1]) <= far(one[1]) ? best : one
    }, null)?.[0] ?? null

  if (key === 'ArrowLeft' || key === 'ArrowRight') {
    return nearest(others.filter(([, spot]) => spot.linked === here.linked && spot.column === here.column + sign))
  }
  const further = others.filter(([, spot]) => (spot.y - here.y) * sign > 0)
  return (
    nearest(further.filter(([, spot]) => spot.linked === here.linked && spot.x === here.x)) ??
    nearest(further.filter(([, spot]) => spot.linked !== here.linked))
  )
}
