// Where each page lives and how to link to it. A feature never imports another
// feature; when one page links to another, it builds the address here.

export const TREE_PATH = '/strom'
export const PROBLEMS_PATH = '/ulohy'
export const GRAPH_PATH = '/graf'

/** The curriculum tree, with an area, topic or skill selected. */
export function treeUrl(nodeId?: string): string {
  return nodeId ? `${TREE_PATH}?${new URLSearchParams({ node: nodeId })}` : TREE_PATH
}

/** The problem database narrowed to tree ids (skills, topics or areas), with one problem shown. */
export function problemsUrl(link: { skills?: string[]; problem?: string } = {}): string {
  const query = new URLSearchParams()
  for (const skill of link.skills ?? []) query.append('skills', skill)
  if (link.problem) query.set('problem', link.problem)
  return query.size ? `${PROBLEMS_PATH}?${query}` : PROBLEMS_PATH
}

/** The tree rebuilt from the solutions of all items (/strom?tree=novy), with a principle selected. */
export function newTreeUrl(nodeId: string): string {
  return `${TREE_PATH}?${new URLSearchParams({ tree: 'novy', node: nodeId })}`
}

/** The exam graph: a task with its solution flow (view uloha), a principle (princip) or a test (zkouska,
 *  test as 2025-B). Whatever the other views had selected may stay in the address beside the view's own. */
export function graphUrl(link: { view?: 'uloha' | 'princip' | 'zkouska'; task?: string; route?: string; node?: string; test?: string } = {}): string {
  const query = new URLSearchParams()
  for (const name of ['view', 'task', 'route', 'node', 'test'] as const) {
    const value = link[name]
    if (value) query.set(name, value)
  }
  return query.size ? `${GRAPH_PATH}?${query}` : GRAPH_PATH
}
