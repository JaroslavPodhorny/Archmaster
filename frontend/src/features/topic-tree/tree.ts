// Lookups over the tree as the backend sends it: one list in learning order.

import type { TreeNode } from './types'

/** 0 for an area, 1 for a topic, 2 for a skill. */
export function depth(node: TreeNode): number {
  return node.id.split('.').length - 1
}

export type TreeIndex = {
  nodes: TreeNode[]
  byId: Map<string, TreeNode>
  /** Children by parent id; the areas are under null. */
  children: Map<string | null, TreeNode[]>
  /** Skill id -> the skills that require it directly. */
  neededBy: Map<string, string[]>
  /** Place in learning order. */
  position: Map<string, number>
}

export function indexTree(nodes: TreeNode[]): TreeIndex {
  const index: TreeIndex = { nodes, byId: new Map(), children: new Map(), neededBy: new Map(), position: new Map() }
  nodes.forEach((node, i) => {
    index.byId.set(node.id, node)
    index.position.set(node.id, i)
    index.children.set(node.parent, [...(index.children.get(node.parent) ?? []), node])
    for (const id of node.requires) index.neededBy.set(id, [...(index.neededBy.get(id) ?? []), node.id])
  })
  return index
}

/** The node with this id; failing that the nearest group above where it would be (the two trees
 *  share most areas and topics but not all skills); failing that the first area. */
export function nearest(index: TreeIndex, id: string): TreeNode {
  for (let at = id; at; at = at.slice(0, Math.max(0, at.lastIndexOf('.')))) {
    const node = index.byId.get(at)
    if (node) return node
  }
  return index.nodes[0]
}

/** The skills of an area or topic; a skill gives itself. */
export function skillsUnder(index: TreeIndex, node: TreeNode): TreeNode[] {
  if (depth(node) === 2) return [node]
  return (index.children.get(node.id) ?? []).flatMap((child) => skillsUnder(index, child))
}

/** The topic and area above a node, the area first. */
export function ancestors(index: TreeIndex, node: TreeNode): TreeNode[] {
  const parent = node.parent === null ? undefined : index.byId.get(node.parent)
  return parent ? [...ancestors(index, parent), parent] : []
}

/** Every skill reached from one by following `next`, with its longest distance from it. */
function reach(id: string, next: (id: string) => string[]): Map<string, number> {
  const distance = new Map<string, number>()
  function visit(from: string, d: number) {
    for (const to of next(from)) {
      if ((distance.get(to) ?? 0) < d) {
        distance.set(to, d)
        visit(to, d + 1)
      }
    }
  }
  visit(id, 1)
  return distance
}

/** Everything a skill needs, directly (distance 1) or through another skill. */
export function prerequisites(index: TreeIndex, id: string): Map<string, number> {
  return reach(id, (x) => index.byId.get(x)?.requires ?? [])
}

/** Everything that builds on a skill, directly or through another skill. */
export function dependents(index: TreeIndex, id: string): Map<string, number> {
  return reach(id, (x) => index.neededBy.get(x) ?? [])
}

/** Lower case without diacritics, so "uhly" finds "Úhly". */
export function fold(text: string): string {
  return text.normalize('NFD').replace(/\p{M}/gu, '').toLowerCase()
}
