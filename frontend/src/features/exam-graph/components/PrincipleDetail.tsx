import { useState } from 'react'
import { Link } from 'react-router'
import { button, focusRing, hint, linkPlain } from '../../../shared/controls'
import { ArrowIcon } from '../../../shared/icons'
import { newTreeUrl } from '../../../shared/routes'
import { Section } from '../../../shared/Section'
import { itemCountLabel, keptTogether, ofTestsLabel, percentLabel, pointsLabel, testName } from '../labels'
import type { PrincipleDetail as Principle } from '../types'
import type { ExamGraph } from '../useExamGraph'
import { Misconceptions } from './Misconceptions'
import { PrincipleFocus } from './PrincipleFocus'

const ITEMS_SHOWN = 8
const stepColumns = 'grid grid-cols-[minmax(9rem,12rem)_3.5rem_minmax(0,1fr)] items-baseline gap-x-3'
// The item, its test, its success with a bar; in a narrow pane the bar goes so the test keeps its room.
const itemColumns = 'grid grid-cols-[3rem_minmax(0,1fr)_4rem] items-center gap-x-3 @md:grid-cols-[4.5rem_minmax(0,1fr)_7.5rem]'

/** The items that need the principle, hardest first; grey where it is not the item's main principle. */
function Items({ graph, principle }: { graph: ExamGraph; principle: Principle }) {
  const [all, setAll] = useState(false)
  const sorted = [...principle.items].sort((a, b) => (a.success_pct ?? 101) - (b.success_pct ?? 101))
  const shown = all ? sorted : sorted.slice(0, ITEMS_SHOWN)
  const onlySteps = principle.items.filter((i) => i.in_steps && !i.in_list).length
  const onlyList = principle.items.filter((i) => i.in_list && i.source === 'kroky' && !i.in_steps).length
  return (
    <>
      <div className={`${itemColumns} border-b border-line pb-1.5 ${hint}`}>
        <span>Položka</span>
        <span>Test</span>
        <span>Úspěšnost</span>
      </div>
      <ul>
        {shown.map((i) => (
          <li key={`${i.test} ${i.item}`}>
            <button
              type="button"
              className={`${itemColumns} w-full cursor-pointer border-b border-line py-1.5 text-left hover:bg-tint ${focusRing} ${i.main ? '' : 'text-muted'}`}
              title="Otevřít úlohu"
              onClick={() => graph.go({ view: 'uloha', task: i.problem_id })}
            >
              <span className={i.main ? 'text-accent' : ''}>
                {i.item}
                {i.in_steps && !i.in_list && ' *'}
              </span>
              <span className="truncate">{testName(i.test)}</span>
              <span className="flex items-center gap-2.5 tabular-nums">
                <span className="w-10 text-right">{i.success_pct === null ? '–' : percentLabel(i.success_pct)}</span>
                {i.success_pct !== null && (
                  <span className="h-1.5 w-14 overflow-hidden rounded-full bg-selected @max-md:hidden">
                    <span className="block h-full bg-faint" style={{ width: `${i.success_pct}%` }} />
                  </span>
                )}
              </span>
            </button>
          </li>
        ))}
      </ul>
      {sorted.length > ITEMS_SHOWN && (
        <button type="button" className={`${linkPlain} mt-2.5`} onClick={() => setAll(!all)}>
          {all ? 'Zobrazit méně' : `Zobrazit všech ${sorted.length}`}
        </button>
      )}
      <div className={`mt-3 space-y-1 ${hint}`}>
        <p>Šedě položky, kde princip není hlavní.</p>
        {onlySteps > 0 && <p>* Kroky úlohy ho používají, uložený seznam položky ho nemá.</p>}
        {onlyList > 0 && <p>U úloh s kroky se počítá podle kroků; uložený seznam má princip ještě u {itemCountLabel(onlyList)}.</p>}
      </div>
    </>
  )
}

/** The selected principle: where it sits, how often the tests need it, what it rests on and what builds on
 *  it (expandable), the typical errors that corrupt it, the steps and items that apply it, and its note. */
export function PrincipleDetail({ graph, principle }: { graph: ExamGraph; principle: Principle }) {
  const counted = principle.items.filter((i) => i.source === 'seznam' || i.in_steps).length
  return (
    <article className="@container min-h-0 overflow-y-auto px-8 pt-5.5 pb-10 max-sm:px-4">
      <div className="max-w-170">
        <p className={hint}>
          {principle.area.name} › {principle.topic.name}
        </p>
        <h2 className="mt-1 text-title font-semibold">{principle.name}</h2>
        <p className={`mt-1 ${hint} tabular-nums`} title="Body položek, které ho potřebují; položka s více principy se počítá u každého z nich.">
          {counted ? `${ofTestsLabel(principle.tests, 20)} · ${itemCountLabel(counted)} · ${pointsLabel(principle.points)} v nich` : 'Žádná položka 20 testů ho nepotřebuje; je jen ve specifikaci.'}
        </p>
        <p className="mt-4">
          <Link className={`${button} gap-2`} to={newTreeUrl(principle.id)}>
            Otevřít v novém stromu učiva
            <ArrowIcon />
          </Link>
        </p>
      </div>

      <Section title="Na čem stojí a co na něm stojí" aside="vlevo předpoklady, vpravo navazující principy">
        {principle.requires.length + principle.required_by.length > 0 ? (
          <>
            <PrincipleFocus key={principle.id} graph={graph} id={principle.id} />
            <p className={`mt-2 max-w-170 ${hint}`}>Okénko vybere princip; „+N“ ukáže dalších N principů za ním, „−“ je zase skryje.</p>
          </>
        ) : (
          <p className="text-muted">Nestojí na žádném jiném principu a žádný na něm nestojí.</p>
        )}
      </Section>

      <div className="max-w-170">
        <Section title="Typické chyby" aside={principle.misconceptions.length || 'žádná'}>
          {principle.misconceptions.length > 0 ? (
            <Misconceptions graph={graph} list={principle.misconceptions} />
          ) : (
            <p className="text-muted">Zatím není zaznamenaná chyba, kterou by prozradila chybná možnost uzavřené úlohy.</p>
          )}
        </Section>

        <Section title="Kroky, které ho používají" aside={principle.steps.length || undefined}>
          {principle.steps.length > 0 ? (
            <>
              <div className={`${stepColumns} border-b border-line pb-1.5 ${hint}`}>
                <span>Úloha</span>
                <span>Položka</span>
                <span>Výsledek kroku</span>
              </div>
              <ul>
                {principle.steps.map((s) => (
                  <li key={`${s.problem_id} ${s.route} ${s.step}`}>
                    <button
                      type="button"
                      className={`${stepColumns} w-full cursor-pointer border-b border-line py-1.5 text-left hover:bg-tint ${focusRing}`}
                      title="Otevřít postup úlohy"
                      onClick={() => graph.go({ view: 'uloha', task: s.problem_id, route: s.route })}
                    >
                      <span className="text-accent">
                        {testName(s.test)} · {s.task}
                      </span>
                      <span>{s.item}</span>
                      <span className="text-small">
                        {keptTogether(s.result)}
                        {!s.main_route && <span className="text-muted"> ({s.route_name})</span>}
                      </span>
                    </button>
                  </li>
                ))}
              </ul>
            </>
          ) : (
            <p className="text-muted">Žádná úloha s rozepsanými kroky ho zatím nepoužívá.</p>
          )}
        </Section>

        {principle.items.length > 0 && (
          <Section title="Položky" aside={`${principle.items.length} · od nejtěžší`}>
            <Items graph={graph} principle={principle} />
          </Section>
        )}

        {principle.note && (
          <Section title="Popis">
            <p>{principle.note}</p>
          </Section>
        )}
      </div>
    </article>
  )
}
