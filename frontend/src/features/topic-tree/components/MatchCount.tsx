import { hint } from '../../../shared/controls'
import type { TopicTree } from '../useTopicTree'

/** How many skills there are, at the right end of a pane's tool row: "162 dovedností", or while a
 *  filter is on "41 z 162 dovedností". */
export function MatchCount({ tree }: { tree: TopicTree }) {
  const leaves = 'dovedností'
  return (
    <span className={`ml-auto whitespace-nowrap tabular-nums ${hint}`}>
      {tree.matching === tree.total ? `${tree.total} ${leaves}` : `${tree.matching} z ${tree.total} ${leaves}`}
    </span>
  )
}
