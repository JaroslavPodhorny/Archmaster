import { focusRing, hint, linkPlain } from '../../../shared/controls'
import { REVIEW_STATES, percentLabel, testName } from '../labels'
import type { Misconception } from '../types'
import type { ExamGraph } from '../useExamGraph'

const columns = 'grid grid-cols-[minmax(0,1fr)_7.5rem_6.5rem] items-baseline gap-x-3'

/** Typical errors, each with what it is, the principle it corrupts and the wrong options that show it:
 *  how many students chose the wrong option, and how many the right one. */
export function Misconceptions({ graph, list, here }: { graph: ExamGraph; list: Misconception[]; here?: string }) {
  return (
    <ul>
      {list.map((m) => (
        <li key={m.id} className="border-b border-line py-2.5 first:pt-0 last:border-b-0">
          <p className="font-semibold">{m.name}</p>
          <p className="mt-0.5">{m.description}</p>
          <p className={`mt-1 ${hint}`}>
            Kazí princip{' '}
            <button type="button" className={linkPlain} onClick={() => graph.go({ view: 'princip', node: m.principle.id })}>
              {m.principle.name}
            </button>{' '}
            · {REVIEW_STATES[m.state]}
          </p>
          <div className={`${columns} mt-2 border-b border-line pb-1.5 ${hint}`}>
            <span>Položka</span>
            <span>Chybná možnost</span>
            <span>Správná</span>
          </div>
          <ul>
            {m.evidence.map((e) => (
              <li key={`${e.test} ${e.item}`}>
                <button
                  type="button"
                  className={`${columns} w-full cursor-pointer border-b border-line py-1.5 text-left hover:bg-tint ${focusRing}`}
                  disabled={e.problem_id === here}
                  title={e.problem_id === here ? undefined : 'Otevřít úlohu'}
                  onClick={() => graph.go({ view: 'uloha', task: e.problem_id })}
                >
                  <span className={e.problem_id === here ? '' : 'text-accent'}>
                    {testName(e.test)} · {e.item}
                  </span>
                  <span className="tabular-nums">
                    {e.option} · {percentLabel(e.share, 1)}
                  </span>
                  <span className="text-muted tabular-nums">
                    {e.key} · {e.key_share === null ? '–' : percentLabel(e.key_share, 1)}
                  </span>
                </button>
              </li>
            ))}
          </ul>
        </li>
      ))}
    </ul>
  )
}
