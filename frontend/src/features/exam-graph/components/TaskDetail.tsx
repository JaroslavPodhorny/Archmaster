import { useState } from 'react'
import { Link } from 'react-router'
import { button, focusRing, hint, linkPlain, linkQuiet } from '../../../shared/controls'
import { ArrowIcon } from '../../../shared/icons'
import { problemsUrl } from '../../../shared/routes'
import { Section } from '../../../shared/Section'
import {
  ANSWER_STATES,
  FORMAT_NAMES,
  REVIEW_STATES,
  keptTogether,
  percentLabel,
  pointsLabel,
  stepCountLabel,
  successLabel,
  testName,
} from '../labels'
import type { PrincipleRef, ReviewEntry, Route, TaskDetail as Task } from '../types'
import type { ExamGraph } from '../useExamGraph'
import { Misconceptions } from './Misconceptions'
import { OptionShares } from './OptionShares'
import { ReviewNotes } from './ReviewNotes'
import { SolutionFlow } from './SolutionFlow'
import { Switch } from './Switch'

// The task and its key on a sheet of white with rounded corners, in the dark theme too.
const shot = 'block h-auto max-w-[min(100%,720px)] rounded-xl border border-line bg-paper p-2'
const chip = `inline-block rounded-full px-2.5 py-px text-left text-small ${focusRing}`
const factRow = 'grid grid-cols-[7.5rem_minmax(0,1fr)] gap-x-4 @max-md:grid-cols-1'

type Props = {
  graph: ExamGraph
  task: Task
  route: Route | null
  review: ReviewEntry[]
  onBack: () => void
}

/** A principle as a pill that opens it in the Princip view; dashed where a step applies it and the item's
 *  stored list lacks it. */
function PrincipleChip({ graph, principle, missing = false }: { graph: ExamGraph; principle: PrincipleRef; missing?: boolean }) {
  return (
    <button
      type="button"
      className={`${chip} ${missing ? 'border border-dashed border-muted hover:bg-tint' : 'bg-tint hover:bg-selected'}`}
      title={missing ? `${principle.topic} – krok ho používá, v uloženém seznamu položky chybí` : principle.topic}
      onClick={() => graph.go({ view: 'princip', node: principle.id })}
    >
      {principle.name}
    </button>
  )
}

/** Principles as links into the Princip view, separated by commas. */
function principleLinks(graph: ExamGraph, ids: string[]) {
  return ids.map((id, i) => (
    <span key={id}>
      {i > 0 && ', '}
      <button type="button" className={linkPlain} onClick={() => graph.go({ view: 'princip', node: id })}>
        {graph.principles.get(id)?.name ?? id}
      </button>
    </span>
  ))
}

/** What the selected step computes, from what, and which principle it applies. */
function SelectedStep({ graph, task, route, stepId }: { graph: ExamGraph; task: Task; route: Route; stepId: string | null }) {
  const step = route.steps.find((s) => s.id === stepId)
  if (!step) {
    return <p className={`mt-2 ${hint}`}>Klikněte na krok: ukáže se, z čeho počítá a který princip použil.</p>
  }
  const steps = new Map(route.steps.map((s) => [s.id, s]))
  const given = new Map(task.given.map((g, n) => [g.id, n + 1]))
  const inputs = step.inputs.map((id) => {
    const from = steps.get(id)
    if (!from) return `zadání ${given.get(id)}`
    return `„${keptTogether(from.result)}“${from.item !== step.item ? ` (položka ${from.item})` : ''}`
  })
  return (
    <div className="mt-3 max-w-170 rounded-xl border border-line px-3.5 py-2.5">
      <p className={hint}>Vybraný krok · položka {step.item}</p>
      <p className="font-medium">{keptTogether(step.result)}</p>
      <p className="mt-0.5 text-small">
        <span className="text-muted">Princip </span>
        <button type="button" className={linkPlain} onClick={() => graph.go({ view: 'princip', node: step.principle.id })}>
          {step.principle.name}
        </button>
        <span className="text-muted"> · počítá z: {inputs.join(', ')}</span>
      </p>
    </div>
  )
}

/** Per item: the answer, what it takes from earlier items, partial points, and the principles of its own
 *  steps with how they differ from the stored list. */
function ItemSteps({ graph, task, route }: { graph: ExamGraph; task: Task; route: Route }) {
  const steps = new Map(route.steps.map((s) => [s.id, s]))
  const byCount = task.scoring?.kind === 'pocet-spravnych'
  return (
    <ul>
      {route.items.map((derived) => {
        const item = task.items.find((i) => i.item === derived.item)!
        const answer = route.steps.find((s) => s.answer === derived.item)!
        const partial = (task.scoring?.partial ?? []).filter((p) => p.item === derived.item)
        return (
          <li key={derived.item} className="border-b border-line py-2.5 first:pt-0 last:border-b-0">
            <p>
              <span className="font-semibold">{derived.item}</span>
              <span className={`${hint} tabular-nums`}>
                {' '}
                · úspěšnost {successLabel(item.success_pct)}
                {!byCount && ` · ${pointsLabel(item.points)}`}
                {item.key && ` · klíč ${item.key}`}
              </span>
            </p>
            <p className="mt-0.5 text-small">{keptTogether(answer.result)}</p>
            {derived.reused.map((r) => (
              <p key={r.step} className={`mt-0.5 ${hint}`}>
                Přebírá výsledek položky {r.item}: „{keptTogether(steps.get(r.step)!.result)}“
              </p>
            ))}
            {partial.map((p) => (
              <p key={p.step} className={`mt-0.5 ${hint}`}>
                Klíč dává {pointsLabel(p.points)} už za mezivýsledek „{keptTogether(steps.get(p.step)!.result)}“
              </p>
            ))}
            <p className="mt-1.5 flex flex-wrap gap-1.5">
              {derived.principles.map((p) => (
                <PrincipleChip key={p.id} graph={graph} principle={p} missing={derived.missing.includes(p.id)} />
              ))}
            </p>
            {derived.extra_reused.length > 0 && (
              <p className={`mt-1 ${hint}`}>
                Uložený seznam má i {principleLinks(graph, derived.extra_reused)}: ty používá jen převzatý výsledek.
              </p>
            )}
            {derived.extra.length > 0 && (
              <p className={`mt-1 ${hint}`}>Uložený seznam má navíc {principleLinks(graph, derived.extra)}: žádný krok je nepoužívá.</p>
            )}
          </li>
        )
      })}
    </ul>
  )
}

/** A task without steps yet: its stored solution line and principle list, item by item. */
function SolutionLines({ graph, task }: { graph: ExamGraph; task: Task }) {
  const byCount = task.format === 'AN'
  return (
    <ul>
      {task.items.map((item) => (
        <li key={item.item} className="border-b border-line py-2.5 first:pt-0 last:border-b-0">
          <p>
            <span className="font-semibold">{item.item}</span>
            <span className={`${hint} tabular-nums`}>
              {' '}
              · úspěšnost {successLabel(item.success_pct)}
              {!byCount && ` · ${pointsLabel(item.points)}`}
              {item.key && ` · klíč ${item.key}`}
            </span>
          </p>
          <p className="mt-0.5 text-small">{keptTogether(item.solution)}</p>
          <p className="mt-1.5 flex flex-wrap gap-1.5">
            {item.stored.map((p) => (
              <PrincipleChip key={p.id} graph={graph} principle={p} />
            ))}
          </p>
        </li>
      ))}
    </ul>
  )
}

function scoringText(task: Task): string {
  const s = task.scoring!
  if (s.kind === 'soucet') return Object.entries(s.points).map(([item, p]) => `${item}: ${pointsLabel(p)}`).join(' · ')
  const counts = Object.entries(s.points)
    .filter(([, p]) => p > 0)
    .sort((a, b) => Number(b[0]) - Number(a[0]))
  return [...counts.map(([count, p]) => `${count} správně: ${pointsLabel(p)}`), 'méně: 0 bodů'].join(' · ')
}

/** The selected task: where it comes from, its booklet page (and the key on request), then its solution
 *  flow with what each item derives from it, or the stored solution where it has no steps yet; the shares
 *  of its options and the misconceptions they reveal; scoring; open questions; review state. */
export function TaskDetail({ graph, task, route, review, onBack }: Props) {
  const [keyOpen, setKeyOpen] = useState(false)
  const [step, setStep] = useState<string | null>(null)
  const notes = review.filter((entry) => entry.kind !== 'kroky')
  const steps = task.stepped && route

  function showMisconception(id: string) {
    document.getElementById(`mc-${id}`)?.scrollIntoView({ block: 'start', behavior: 'auto' })
  }

  return (
    <article className="@container min-h-0 overflow-y-auto px-8 pt-5.5 pb-10 max-sm:px-4">
      <button type="button" className={`${button} mb-3 sm:hidden`} onClick={onBack}>
        Zpět na seznam
      </button>
      <div className="max-w-170">
        <p className={hint}>
          <button type="button" className={linkQuiet} onClick={() => graph.go({ view: 'zkouska', test: task.test })}>
            {testName(task.test)}
          </button>{' '}
          › úloha {task.task}
        </p>
        <h2 className="mt-1 text-title font-semibold">{task.description}</h2>
        <p className={`mt-1 ${hint} tabular-nums`}>
          {pointsLabel(task.points)} · {FORMAT_NAMES[task.format] ?? task.format} · úspěšnost {successLabel(task.success_pct)}
          {task.skipped_pct !== null && ` · vynechalo ${percentLabel(task.skipped_pct)}`}
        </p>
        <p className="mt-4">
          <Link className={`${button} gap-2`} to={problemsUrl({ problem: task.id })}>
            Otevřít v databázi úloh
            <ArrowIcon />
          </Link>
        </p>
      </div>

      <img className={`${shot} mt-5`} src={`/api/screenshots/${task.screenshot}`} alt={`Úloha ${task.task}: ${task.description}`} />
      <div className="mt-3">
        <button type="button" className={button} aria-expanded={keyOpen} onClick={() => setKeyOpen(!keyOpen)}>
          {keyOpen ? 'Skrýt klíč' : 'Zobrazit klíč'}
        </button>
        {keyOpen && (
          <img className={`${shot} mt-3`} src={`/api/screenshots/${task.key_screenshot}`} alt={`Klíč k úloze ${task.task}`} />
        )}
      </div>

      {steps ? (
        <>
          <Section title="Postup řešení" aside={`${stepCountLabel(route.steps.length)} · ${route.name}`}>
            {task.routes.length > 1 && (
              <div className="mb-3 flex">
                <Switch
                  label="Postup"
                  options={task.routes.map((r) => r.id)}
                  names={Object.fromEntries(task.routes.map((r) => [r.id, r.name]))}
                  value={route.id}
                  small
                  onChange={(id) => {
                    setStep(null)
                    graph.go({ route: id }, false)
                  }}
                />
              </div>
            )}
            <SolutionFlow task={task} route={route} selected={step} onSelect={setStep} />
            <p className={`mt-2 max-w-170 ${hint}`}>
              Šipka vede od výsledku ke kroku, který z něj počítá; kroky bez šipky vycházejí jen ze zadání. Pod
              výsledkem je princip, který krok použil. Šedě odpovědi s úspěšností z CERMATu, modrá šipka výsledek
              převzatý jinou položkou, čárkovaně krok, jehož princip v uloženém seznamu položky chybí.
            </p>
            <SelectedStep graph={graph} task={task} route={route} stepId={step} />
          </Section>
          <div className="max-w-170">
            <Section title="Položky" aside="principy odvozené z kroků">
              <ItemSteps graph={graph} task={task} route={route} />
            </Section>
          </div>
        </>
      ) : (
        <div className="max-w-170">
          <Section title="Řešení" aside="zatím bez kroků">
            <p className={`mb-3 ${hint}`}>Úloha ještě nemá rozepsaný postup po krocích; níže je uložené řešení a seznam principů.</p>
            <SolutionLines graph={graph} task={task} />
          </Section>
        </div>
      )}

      <div className="max-w-170">
        {task.options.length > 0 && (
          <Section title="Volby žáků" aside="podíl žáků, kteří zvolili každou možnost">
            <OptionShares options={task.options} misconceptions={task.misconceptions} onMisconception={showMisconception} />
          </Section>
        )}

        {task.misconceptions.length > 0 && (
          <Section title="Typické chyby" aside={task.misconceptions.length}>
            {task.misconceptions.map((m) => (
              <div key={m.id} id={`mc-${m.id}`}>
                <Misconceptions graph={graph} list={[m]} here={task.id} />
              </div>
            ))}
          </Section>
        )}

        {task.scoring && (
          <Section title="Bodování" aside="podle klíče">
            <p className="tabular-nums">{scoringText(task)}</p>
            {task.scoring.note && <p className={`mt-1 ${hint}`}>{task.scoring.note}</p>}
          </Section>
        )}

        {notes.length > 0 && (
          <Section title="K revizi" aside={notes.length}>
            <ReviewNotes graph={graph} entries={notes} />
          </Section>
        )}

        {task.review && (
          <Section title="Stav">
            <dl className="space-y-1.5">
              <div className={factRow}>
                <dt className="text-muted">Odpovědi</dt>
                <dd>{ANSWER_STATES[task.review.answers]}</dd>
              </div>
              <div className={factRow}>
                <dt className="text-muted">Kroky</dt>
                <dd>{REVIEW_STATES[task.review.steps]}</dd>
              </div>
              <div className={factRow}>
                <dt className="text-muted">Principy kroků</dt>
                <dd>{REVIEW_STATES[task.review.principles]}</dd>
              </div>
            </dl>
          </Section>
        )}
      </div>
    </article>
  )
}
