import { useEffect, useMemo, useState } from 'react'
import { useSearchParams } from 'react-router'
import { fetchTree } from './api'
import { ancestors, dependents, depth, fold, indexTree, nearest, prerequisites, skillsUnder } from './tree'
import type { Kind, Priority, TreeNode, TreeVersion } from './types'

/** The tree with its groups, or the graph of all prerequisite links. */
export type View = 'tree' | 'graph'

export type Filters = {
  q: string
  /** Empty means no filter, as in the problem database's menus. */
  priorities: Priority[]
  kinds: Kind[]
  /** Show only the selected skill, what it needs and what builds on it. */
  relatedOnly: boolean
}

/** A line of the tree pane. */
export type Row = {
  node: TreeNode
  depth: number
  /** Areas and topics only. */
  open: boolean
  /** How many skills under it (or the skill itself) pass the filters. */
  matching: number
  /** How the selected skill relates to it. */
  relation: 'prerequisite' | 'dependent' | null
}

const NO_FILTERS: Filters = { q: '', priorities: [], kinds: [], relatedOnly: false }
const NOTHING = new Map<string, number>()

/** Areas start open and topics closed; `toggled` holds the ones that are the other way round. */
function isOpen(node: TreeNode, toggled: ReadonlySet<string>): boolean {
  return (depth(node) === 0) !== toggled.has(node.id)
}

/** All state of the page: the tree from the backend (the old or the new one), the selected node and
 *  the view (all three kept in the address as ?node=VZT.PROC.obracene&view=graf&tree=novy, so other
 *  pages can link to it), what is open and the filters. */
export function useTopicTree() {
  // Each tree is fetched when first shown and kept, so switching back and forth is immediate.
  const [trees, setTrees] = useState<Partial<Record<TreeVersion, TreeNode[]>>>({})
  const [failed, setFailed] = useState<{ version: TreeVersion; message: string } | null>(null)
  const [address, setAddress] = useSearchParams()
  const [filters, setFilters] = useState(NO_FILTERS)
  const [toggled, setToggled] = useState<ReadonlySet<string>>(new Set())
  const [revealedId, setRevealedId] = useState<string | null>(null)

  const version: TreeVersion = address.get('tree') === 'novy' ? 'new' : 'old'
  const nodes = trees[version] ?? null
  const error = failed?.version === version ? failed.message : null
  const loaded = nodes !== null

  useEffect(() => {
    if (loaded) return
    const controller = new AbortController()
    fetchTree(version, controller.signal)
      .then((fetched) => setTrees((known) => ({ ...known, [version]: fetched })))
      .catch((e) => {
        if (e.name !== 'AbortError') setFailed({ version, message: e.message })
      })
    return () => controller.abort()
  }, [version, loaded])

  const index = useMemo(() => (nodes ? indexTree(nodes) : null), [nodes])
  // A node of one tree may be missing in the other; then the group it would belong to is shown.
  const selected = index ? nearest(index, address.get('node') ?? '') : null
  const view: View = address.get('view') === 'graf' ? 'graph' : 'tree'
  const skill = selected && depth(selected) === 2 ? selected : null
  const before = useMemo(() => (index && skill ? prerequisites(index, skill.id) : NOTHING), [index, skill])
  const after = useMemo(() => (index && skill ? dependents(index, skill.id) : NOTHING), [index, skill])

  // Whatever selects a node (a click, a link from another page, the browser's Back), the groups above it open.
  if (index && selected && revealedId !== selected.id) {
    setRevealedId(selected.id)
    const next = new Set(toggled)
    for (const group of ancestors(index, selected)) {
      if (depth(group) === 0) next.delete(group.id)
      else next.add(group.id)
    }
    setToggled(next)
  }

  const shown = useMemo(() => {
    if (!index) return { rows: [] as Row[], matching: 0, total: 0, passes: () => true, isRelated: () => true }
    const needle = fold(filters.q.trim())
    const related = filters.relatedOnly && skill !== null
    const filtering = related || needle !== '' || filters.kinds.length > 0 || filters.priorities.length > 0

    /** The search, the priorities and the kind let the skill through. */
    function passes(n: TreeNode): boolean {
      return (
        (filters.priorities.length === 0 || filters.priorities.includes(n.priority!)) &&
        (filters.kinds.length === 0 || filters.kinds.includes(n.kind!)) &&
        (needle === '' || fold(`${n.name} ${n.note} ${n.id}`).includes(needle))
      )
    }
    /** "Jen související" lets the skill through. */
    function isRelated(n: TreeNode): boolean {
      return !related || n.id === skill?.id || before.has(n.id) || after.has(n.id)
    }
    const matches = (n: TreeNode) => isRelated(n) && passes(n)

    // While a filter is on, every group with a matching skill is shown open.
    const rows: Row[] = []
    function walk(node: TreeNode) {
      const matching = skillsUnder(index!, node).filter(matches).length
      if (matching === 0) return
      const d = depth(node)
      const open = d < 2 && (filtering || isOpen(node, toggled))
      const relation = before.has(node.id) ? 'prerequisite' : after.has(node.id) ? 'dependent' : null
      rows.push({ node, depth: d, open, matching, relation })
      if (open) (index!.children.get(node.id) ?? []).forEach(walk)
    }
    const areas = index.children.get(null) ?? []
    areas.forEach(walk)
    const skills = index.nodes.filter((n) => depth(n) === 2)
    return { rows, matching: skills.filter(matches).length, total: skills.length, passes, isRelated }
  }, [index, filters, toggled, skill, before, after])

  function show(id: string | null, inView: View, inVersion: TreeVersion, push: boolean) {
    const next: Record<string, string> = {}
    if (id) next.node = id
    if (inView === 'graph') next.view = 'graf'
    if (inVersion === 'new') next.tree = 'novy'
    setAddress(next, { replace: !push })
  }

  /** `push` adds a step to the browser's history, so Back returns to the node shown before. */
  function select(id: string, push = false) {
    show(id, view, version, push)
  }

  function setView(next: View) {
    if (selected && next !== view) show(selected.id, next, version, true)
  }

  /** The node named in the address is kept, so switching there and back returns to the same node
   *  even when the other tree does not have it. */
  function setVersion(next: TreeVersion) {
    if (next !== version) show(address.get('node'), view, next, true)
  }

  function setOpen(node: TreeNode, open: boolean) {
    if (isOpen(node, toggled) === open) return
    const next = new Set(toggled)
    if (!next.delete(node.id)) next.add(node.id)
    setToggled(next)
  }

  function setAllOpen(open: boolean) {
    const groups = index?.nodes.filter((n) => depth(n) === (open ? 1 : 0)) ?? []
    setToggled(new Set(groups.map((n) => n.id)))
  }

  return {
    index, error, version, setVersion, selected, view, setView, before, after, filters, setFilters,
    clearFilters: () => setFilters(NO_FILTERS), ...shown,
    select, isOpen: (node: TreeNode) => isOpen(node, toggled), setOpen, setAllOpen,
  }
}

export type TopicTree = ReturnType<typeof useTopicTree>
