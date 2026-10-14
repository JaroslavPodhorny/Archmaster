import { useState } from 'react'
import { errorMessage } from '../../shared/controls'
import { Loading } from '../../shared/Loading'
import { ExamDetail } from './components/ExamDetail'
import { GraphBar } from './components/GraphBar'
import { PrincipleDetail } from './components/PrincipleDetail'
import { TaskDetail } from './components/TaskDetail'
import { TaskList } from './components/TaskList'
import { testName } from './labels'
import { useExamGraph } from './useExamGraph'

/** The M9 exam as a graph in layers (analysis/07_graph_representation.md): a task with its solution flow
 *  step by step (Úloha), a principle with what it rests on, what builds on it and the steps that apply it
 *  (Princip), and a test against all twenty: its slots, its items × principles and the coverage of the
 *  principles (Zkouška). The bar switches between them; the window never scrolls, the panes do. */
export function ExamGraphPage() {
  const graph = useExamGraph()
  // On a phone the task list and the task take turns.
  const [showTask, setShowTask] = useState(false)
  const { view, task, node, test, taskDetail, principleDetail, examDetail } = graph
  const detail = view === 'uloha' ? taskDetail : view === 'princip' ? principleDetail : examDetail
  const error = graph.error ?? detail.error

  const title =
    view === 'uloha' && task
      ? `Úloha ${task.test} ${task.task}`
      : view === 'princip' && node
        ? node.name
        : view === 'zkouska' && test
          ? `Test ${testName(test)}`
          : null

  return (
    <div className="flex h-full flex-col">
      <title>{title ? `${title} – Graf zkoušky` : 'Graf zkoušky – ArchMaster'}</title>
      <GraphBar graph={graph} />

      {error && <p className={errorMessage}>Nepodařilo se načíst data: {error}</p>}
      {!error && !graph.index && <Loading />}

      {graph.index && view === 'uloha' && (
        <div
          className={`grid min-h-0 flex-1 grid-cols-[clamp(260px,26%,340px)_minmax(0,1fr)] max-sm:grid-cols-1 ${
            showTask ? 'max-sm:[&>:first-child]:hidden' : 'max-sm:[&>:last-child]:hidden'
          }`}
        >
          <div className="flex min-h-0 flex-col border-r border-line max-sm:border-r-0">
            <TaskList graph={graph} onPick={() => setShowTask(true)} />
          </div>
          {taskDetail.value && task?.id === taskDetail.value.id ? (
            <TaskDetail
              key={`${taskDetail.value.id} ${graph.route?.id ?? ''}`}
              graph={graph}
              task={taskDetail.value}
              route={graph.route}
              review={graph.reviewByTask.get(taskDetail.value.id) ?? []}
              onBack={() => setShowTask(false)}
            />
          ) : (
            !error && <Loading key={task?.id} />
          )}
        </div>
      )}

      {graph.index && view === 'princip' && (
        <div className="grid min-h-0 flex-1">
          {principleDetail.value ? <PrincipleDetail graph={graph} principle={principleDetail.value} /> : !error && <Loading key={node?.id} />}
        </div>
      )}

      {graph.index && view === 'zkouska' && (
        <div className="grid min-h-0 flex-1">
          {examDetail.value ? <ExamDetail graph={graph} exam={examDetail.value} /> : !error && <Loading key={test ?? ''} />}
        </div>
      )}
    </div>
  )
}
