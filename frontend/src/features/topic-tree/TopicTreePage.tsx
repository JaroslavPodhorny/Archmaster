import { errorMessage } from '../../shared/controls'
import { Loading } from '../../shared/Loading'
import { NodeDetail } from './components/NodeDetail'
import { SkillGraph } from './components/SkillGraph'
import { TreeBar } from './components/TreeBar'
import { TreeRows } from './components/TreeRows'
import { useTopicTree } from './useTopicTree'

// The tree takes about a third of the width; the graph takes all the selected node can spare.
const PANES = {
  tree: 'grid-cols-[clamp(280px,36%,460px)_minmax(0,1fr)] max-sm:grid-rows-[42%_minmax(0,1fr)]',
  graph: 'grid-cols-[minmax(0,1fr)_clamp(320px,30%,440px)] max-sm:grid-rows-[55%_minmax(0,1fr)]',
}

/** The curriculum tree of the M9 test: what is examined, in learning order, and how much each skill matters.
 *  There are two of them for now, the old one and the one rebuilt from the solutions of all items; the bar
 *  switches between them. Either is shown as a tree, or as the graph of all prerequisite links between the skills.
 *  The page never scrolls as a whole: the filters stay on top, and the tree or graph and the selected
 *  node scroll separately below them (on narrow windows the tree above, the node below). */
export function TopicTreePage() {
  const tree = useTopicTree()
  const { index, selected } = tree

  return (
    <div className="flex h-full flex-col">
      <title>{selected ? `${selected.name} – Strom učiva` : 'Strom učiva – ArchMaster'}</title>
      <TreeBar tree={tree} />

      {tree.error && <p className={errorMessage}>Nepodařilo se načíst data: {tree.error}</p>}
      {!index && !tree.error && <Loading key={tree.version} />}

      {index && selected && (
        <div className={`grid min-h-0 flex-1 max-sm:grid-cols-1 ${PANES[tree.view]}`}>
          {tree.view === 'graph' ? <SkillGraph tree={tree} /> : <TreeRows tree={tree} />}
          <NodeDetail
            key={selected.id}
            index={index}
            node={selected}
            links={tree.view === 'graph' ? 'list' : 'graph'}
            version={tree.version}
            inDatabase={tree.version === 'old'}
            before={tree.before}
            after={tree.after}
            onGo={(id) => tree.select(id, true)}
          />
        </div>
      )}
    </div>
  )
}
