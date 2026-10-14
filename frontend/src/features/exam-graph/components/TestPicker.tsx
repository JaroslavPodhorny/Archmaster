import { button } from '../../../shared/controls'
import { testName } from '../labels'
import type { ExamGraph } from '../useExamGraph'

/** Which of the 20 tests the Zkouška view shows: a pill like the other filters, opening the browser's own
 *  list of the tests by year (a single choice, so no checkboxes). */
export function TestPicker({ graph }: { graph: ExamGraph }) {
  const tests = graph.index?.tests ?? []
  const years = [...new Set(tests.map((t) => t.slice(0, 4)))].reverse()
  return (
    <div className="relative">
      <select
        className={`${button} appearance-none pr-8`}
        aria-label="Test"
        value={graph.test ?? ''}
        onChange={(e) => graph.go({ view: 'zkouska', test: e.target.value })}
      >
        {years.map((year) => (
          <optgroup key={year} label={year}>
            {tests
              .filter((t) => t.startsWith(year))
              .map((t) => (
                <option key={t} value={t}>
                  Test {testName(t)}
                </option>
              ))}
          </optgroup>
        ))}
      </select>
      <span
        className="pointer-events-none absolute top-1/2 right-3.5 -translate-y-1/4 border-4 border-b-0 border-transparent border-t-current opacity-70"
        aria-hidden="true"
      />
    </div>
  )
}
