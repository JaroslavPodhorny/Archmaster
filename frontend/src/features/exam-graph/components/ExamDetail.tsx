import { Fragment, useState } from 'react'
import { focusRing, hint } from '../../../shared/controls'
import { Section } from '../../../shared/Section'
import { itemCountLabel, ofTestsLabel, pointsLabel, principleCountLabel, taskCountLabel, testName } from '../labels'
import type { ExamDetail as Exam, ExamRow } from '../types'
import type { ExamGraph } from '../useExamGraph'
import { Switch } from './Switch'

type Paint = 'tests' | 'points'
const PAINTS: Paint[] = ['tests', 'points']
const PAINT_NAMES: Record<Paint, string> = { tests: 'Počet testů', points: 'Body' }

// Four shades of the ink colour over the page, lightest first, so the text stays readable in both themes.
const SHADES = ['bg-ink/5', 'bg-ink/10', 'bg-ink/15', 'bg-ink/22']

/** The 16 slots: this test's topic for every task number, against how often that topic fills the slot in
 *  the 20 tests. A slot that one topic fills in at least 60 % of the tests is grey. A slot opens its task. */
function SlotStrip({ graph, exam }: { graph: ExamGraph; exam: Exam }) {
  return (
    <div className="grid grid-cols-4 gap-2 @[64rem]:grid-cols-8">
      {exam.template.map((slot) => {
        const task = exam.tasks.find((t) => t.task === slot.task)
        const top = slot.topics[0]
        const mine = task?.topic ? graph.groups.get(task.topic)?.name : null
        const same = task?.topic === top.id
        return (
          <button
            key={slot.task}
            type="button"
            className={`flex min-h-23 cursor-pointer flex-col gap-0.5 rounded-md border border-edge px-2 py-1.5 text-left text-tiny hover:border-muted ${
              slot.fixed ? 'bg-tint' : 'bg-page'
            } ${focusRing}`}
            title={`Úloha ${slot.task}: ${task?.description ?? ''}\nV 20 testech: ${slot.topics
              .slice(0, 4)
              .map((t) => `${t.name} ${t.count}×`)
              .join(', ')}`}
            onClick={() => task && graph.go({ view: 'uloha', task: task.id })}
          >
            <span className="text-small font-semibold">{slot.task}</span>
            <span className="line-clamp-2">{mine ?? '–'}</span>
            <span className="mt-auto text-muted">
              {same ? `jako v ${top.count} z ${slot.tests}` : `obvykle ${top.name} (${top.count} z ${slot.tests})`}
            </span>
          </button>
        )
      })}
    </div>
  )
}

/** Items as columns (grouped by task), the test's principles as rows (grouped by topic); a dot where the
 *  item needs the principle, larger for its main one. A row opens the principle, a task number the task. */
function IncidenceMatrix({ graph, exam }: { graph: ExamGraph; exam: Exam }) {
  const byTask: { task: number; id: string; rows: ExamRow[] }[] = []
  for (const row of exam.rows) {
    if (byTask.at(-1)?.task !== row.task) byTask.push({ task: row.task, id: row.problem_id, rows: [] })
    byTask.at(-1)!.rows.push(row)
  }
  const columns = byTask.flatMap((t) => t.rows.map((row, i) => ({ row, first: i === 0 })))
  const cell = (first: boolean) => `h-4.5 w-5.5 p-0 text-center ${first ? 'border-l border-line' : ''}`
  // A topic's name stands above its first principle.
  const lines = exam.principles.map((pid, i) => {
    const p = graph.principles.get(pid)!
    return { pid, p, heading: i === 0 || graph.principles.get(exam.principles[i - 1])!.topic !== p.topic }
  })

  return (
    <div className="w-fit max-w-full overflow-x-auto rounded-xl border border-line p-3">
      <table className="border-collapse text-tiny">
        <thead>
          <tr>
            <th />
            {byTask.map((t) => (
              <th key={t.task} colSpan={t.rows.length} className="border-b border-l border-line p-0 font-normal">
                <button
                  type="button"
                  className={`w-full cursor-pointer px-0.5 pb-0.5 text-muted hover:text-ink ${focusRing}`}
                  title={`Otevřít úlohu ${t.task}`}
                  onClick={() => graph.go({ view: 'uloha', task: t.id })}
                >
                  {t.task}
                </button>
              </th>
            ))}
          </tr>
          <tr>
            <th />
            {columns.map(({ row, first }) => (
              <th key={row.item} className={`${cell(first)} pb-1 font-normal text-faint`}>
                {row.item.includes('.') ? row.item.split('.')[1] : ''}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {lines.map(({ pid, p, heading }) => {
            return (
              <Fragment key={pid}>
                {heading && (
                  <tr>
                    <th colSpan={columns.length + 1} className="pt-2.5 pb-0.5 text-left font-normal text-muted">
                      {graph.groups.get(p.topic)?.name}
                    </th>
                  </tr>
                )}
                <tr className="hover:bg-tint">
                  <th className="w-56 min-w-44 p-0 pr-2.5 text-right font-normal">
                    <button
                      type="button"
                      className={`line-clamp-1 cursor-pointer text-right hover:text-accent ${focusRing}`}
                      title={p.name}
                      onClick={() => graph.go({ view: 'princip', node: pid })}
                    >
                      {p.name}
                    </button>
                  </th>
                  {columns.map(({ row, first }) => {
                    const used = row.principles.includes(pid)
                    const main = row.main === pid && used
                    return (
                      <td key={row.item} className={cell(first)} title={used ? `${row.item} · ${p.name}${main ? ' (hlavní)' : ''}` : undefined}>
                        {used && <span className={`inline-block rounded-full align-middle ${main ? 'size-2.5 bg-ink' : 'size-2 bg-faint'}`} />}
                      </td>
                    )
                  })}
                </tr>
              </Fragment>
            )
          })}
        </tbody>
      </table>
    </div>
  )
}

/** Every principle of the rebuilt tree under its area and topic, shaded by how many of the 20 tests need
 *  it or how many points of them depend on it; this test's principles have an accent border, principles
 *  no item needs a dashed one. A principle opens in the Princip view. */
function CoverageMap({ graph, exam, paint }: { graph: ExamGraph; exam: Exam; paint: Paint }) {
  const cover = new Map(exam.coverage.map((c) => [c.id, c]))
  const inTest = new Set(exam.principles)
  const most = Math.max(...exam.coverage.map((c) => c.points))
  function shade(id: string): string {
    const c = cover.get(id)!
    if (c.items === 0) return 'border-dashed border-edge text-faint'
    const level =
      paint === 'tests'
        ? c.tests >= 15 ? 3 : c.tests >= 10 ? 2 : c.tests >= 5 ? 1 : 0
        : c.points >= most / 2 ? 3 : c.points >= most / 4 ? 2 : c.points >= most / 10 ? 1 : 0
    return `${SHADES[level]} ${inTest.has(id) ? 'border-accent' : 'border-transparent'}`
  }
  const areas = graph.index!.groups.filter((g) => g.parent === null)
  return (
    <div className="space-y-4">
      {areas.map((area) => (
        <div key={area.id}>
          <h4 className="font-semibold">{area.name}</h4>
          {graph.index!.groups
            .filter((g) => g.parent === area.id)
            .map((topic) => (
              <div key={topic.id} className="mt-1.5 grid grid-cols-[10rem_minmax(0,1fr)] gap-x-3 @max-md:grid-cols-1">
                <span className={`pt-0.5 ${hint}`}>{topic.name}</span>
                <div className="flex flex-wrap gap-1">
                  {graph.index!.principles
                    .filter((p) => p.topic === topic.id)
                    .map((p) => {
                      const c = cover.get(p.id)!
                      return (
                        <button
                          key={p.id}
                          type="button"
                          className={`max-w-full cursor-pointer rounded-md border px-2 py-0.5 text-left text-tiny hover:border-muted ${shade(p.id)} ${focusRing}`}
                          title={`${p.name} – ${ofTestsLabel(c.tests, 20)}, ${itemCountLabel(c.items)}, ${pointsLabel(c.points)}${inTest.has(p.id) ? '; v tomto testu' : ''}`}
                          onClick={() => graph.go({ view: 'princip', node: p.id })}
                        >
                          {p.name}
                        </button>
                      )
                    })}
                </div>
              </div>
            ))}
        </div>
      ))}
    </div>
  )
}

/** One test against all 20: its numbers, the slot template, its items × principles, and the coverage map. */
export function ExamDetail({ graph, exam }: { graph: ExamGraph; exam: Exam }) {
  const [paint, setPaint] = useState<Paint>('tests')
  const stepped = exam.tasks.filter((t) => t.stepped).length
  return (
    <article className="@container min-h-0 overflow-y-auto px-8 pt-5.5 pb-10 max-sm:px-4">
      <div className="max-w-170">
        <p className={hint}>Test</p>
        <h2 className="mt-1 text-title font-semibold">{testName(exam.test)} termín</h2>
        <p className={`mt-1 ${hint} tabular-nums`}>
          {taskCountLabel(exam.tasks.length)} · {itemCountLabel(exam.rows.length)} · {pointsLabel(exam.points)} ·{' '}
          {principleCountLabel(exam.principles.length)} · s kroky {stepped} z {exam.tasks.length}
        </p>
      </div>

      <Section title="Šablona testu" aside="téma hlavního principu každé úlohy, srovnané se 20 testy">
        <SlotStrip graph={graph} exam={exam} />
        <p className={`mt-2 max-w-170 ${hint}`}>Šedě sloty, které jedno téma plní aspoň v 60 % testů. Slot otevře svou úlohu.</p>
      </Section>

      <Section title="Položky a principy" aside={`${itemCountLabel(exam.rows.length)} × ${principleCountLabel(exam.principles.length)}`}>
        <IncidenceMatrix graph={graph} exam={exam} />
        <p className={`mt-2 max-w-170 ${hint}`}>
          Sloupce jsou položky po úlohách, řádky principy po tématech; větší tečka je hlavní princip položky. U úloh s kroky
          jsou principy odvozené z kroků.
        </p>
      </Section>

      <Section title="Pokrytí principů" aside="ve 20 testech">
        <div className="mb-3 flex flex-wrap items-center justify-between gap-x-4 gap-y-2">
          <p className={`max-w-170 ${hint}`}>
            {paint === 'tests'
              ? 'Čím tmavší, tím ve více testech princip je (do 4, 5–9, 10–14, 15–20).'
              : 'Čím tmavší, tím více bodů 20 testů na principu závisí; body položky se počítají u každého jejího principu.'}{' '}
            Modře principy tohoto testu, čárkovaně principy, které žádná položka nepotřebuje.
          </p>
          <Switch label="Barva podle" options={PAINTS} names={PAINT_NAMES} value={paint} onChange={setPaint} small />
        </div>
        <CoverageMap graph={graph} exam={exam} paint={paint} />
      </Section>
    </article>
  )
}
