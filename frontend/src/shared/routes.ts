// Where each page lives and how to link to it. A feature never imports another
// feature; when one page links to another, it builds the address here.

export const TREE_PATH = '/strom'
export const PROBLEMS_PATH = '/ulohy'

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

