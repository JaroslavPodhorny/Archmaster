import { useState, type ReactNode } from 'react'
import { Link } from 'react-router'
import { ArrowIcon } from '../../../shared/icons'
import { button, focusRing, hint, linkPlain, linkQuiet } from '../../../shared/controls'
import { problemsUrl } from '../../../shared/routes'
import { Section } from '../../../shared/Section'
import {
  KIND_MEANING,
  KIND_NAMES,
  LEAVES_COUNTED,
  LEAVES_TITLE,
  ONE_DEPENDENT,
  PRIORITIES,
  PRIORITY_LABELS,
  PRIORITY_NAMES,
  RECENT_YEARS,
  STANDARD_TESTS_NOTE,
  TERM_NAMES,
  capitalized,
  percentLabel,
  pointsLabel,
  problemsToShowLabel,
} from '../labels'
import { ancestors, depth, skillsUnder } from '../tree'
import type { TreeIndex } from '../tree'
import type { TreeNode, TreeVersion } from '../types'
import { PrerequisiteGraph } from './PrerequisiteGraph'
import { PriorityBadge } from './PriorityBadge'

type Props = {
  index: TreeIndex
  node: TreeNode
  /** For a skill: what it needs and what builds on it, with distances. */
  before: Map<string, number>
  after: Map<string, number>
  /** How a skill's prerequisite links are shown: as the small graph, or, beside the graph of all
   *  links, as two lists. */
  links: 'graph' | 'list'
  /** Which tree the node belongs to: its leaves are skills (dovednosti) or principles (principy). */
  version: TreeVersion
  /** The problem database can list the tasks of this tree's nodes. It stores the skills of the old
   *  tree only; for the new one an item opens its task without a filter. */
  inDatabase: boolean
  /** Selects another node of the tree. */
  onGo: (nodeId: string) => void
}

/** One number of the "in the tests" row: the value, what it counts, and on hover what that means. */
type Stat = { value: string; label: string; title?: string }

const TASKS_SHOWN = 8
// The columns of the task table: the item, its test, its success rate with a bar; in a narrow pane the
// bar goes, so that the test's name keeps its room.
const taskColumns =
  'grid grid-cols-[3rem_minmax(0,1fr)_5rem] items-center gap-x-3 @md:grid-cols-[4.5rem_minmax(0,1fr)_7.5rem]'
// A label and its value, side by side, or the label above when the pane is narrow.
const factRow = 'grid grid-cols-[7.5rem_minmax(0,1fr)] gap-x-4 @max-md:grid-cols-1'

// Four numbers stand in one row divided by thin lines; in a narrow pane two by two.
function statPlace(i: number): string {
  if (i === 0) return ''
  if (i === 2) return 'mt-4 @[30rem]:mt-0 @[30rem]:border-l @[30rem]:pl-4'
  return `border-l pl-4 ${i === 3 ? 'mt-4 @[30rem]:mt-0' : ''}`
}

/** The node's numbers in the tests, each value large with what it counts under it. */
function Stats({ stats }: { stats: Stat[] }) {
  return (
    <div className="@container">
      <dl className="grid grid-cols-2 @[30rem]:grid-cols-4">
        {stats.map(({ value, label, title }, i) => (
          <div key={label} className={`flex flex-col-reverse justify-end border-line ${statPlace(i)}`}>
            <dt className={`mt-0.5 ${hint}`} title={title}>
              {label}
            </dt>
            <dd className="text-title font-semibold whitespace-nowrap tabular-nums">{value}</dd>
          </div>
        ))}
      </dl>
    </div>
  )
}

/** The tasks that need the skill as a table, hardest first: the item, its test, and how many students
 *  solved it. A row opens the task in the problem database, among the skill's other tasks when the
 *  database knows the skill (`filterBy` is then given). The first few show; the rest open on request. */
function Tasks({ node, filterBy }: { node: TreeNode; filterBy: TreeNode | null }) {
  const [all, setAll] = useState(false)
  const sorted = [...node.uses].sort((a, b) => (a.success_pct ?? 101) - (b.success_pct ?? 101))
  const shown = all ? sorted : sorted.slice(0, TASKS_SHOWN)
  const secondary = node.uses.some((use) => !use.main)

  return (
    <>
      {sorted.length > 0 && (
        <>
          <div className={`${taskColumns} border-b border-line pb-1.5 ${hint}`}>
            <span>Úloha</span>
            <span>Test</span>
            <span>Úspěšnost</span>
          </div>
          <ul>
            {shown.map((use) => {
              const [year, term, item] = use.ref.split(' ')
              return (
                <li key={use.ref}>
                  <Link
                    className={`${taskColumns} border-b border-line py-1.5 hover:bg-tint ${focusRing} ${use.main ? '' : 'text-muted'}`}
                    to={problemsUrl({ skills: filterBy ? [filterBy.id] : [], problem: use.problem_id })}
                    title="Otevřít úlohu v databázi úloh"
                  >
                    <span className={use.main ? 'text-accent' : ''}>{item}</span>
                    <span className="truncate">
                      {year}, {TERM_NAMES[term]}
                    </span>
                    <span className="flex items-center gap-2.5 tabular-nums">
                      <span className="w-10 text-right">
                        {use.success_pct === null ? '–' : percentLabel(use.success_pct)}
                      </span>
                      {use.success_pct !== null && (
                        <span className="h-1.5 w-14 overflow-hidden rounded-full bg-selected @max-md:hidden">
                          <span className="block h-full bg-faint" style={{ width: `${use.success_pct}%` }} />
                        </span>
                      )}
                    </span>
                  </Link>
                </li>
              )
            })}
          </ul>
          {sorted.length > TASKS_SHOWN && (
            <button type="button" className={`${linkPlain} mt-2.5`} onClick={() => setAll(!all)}>
              {all ? 'Zobrazit méně' : `Zobrazit všech ${sorted.length}`}
            </button>
          )}
        </>
      )}
      {(secondary || node.older.length > 0) && (
        <div className={`mt-3 space-y-1 ${hint}`}>
          {secondary && <p>Šedě úlohy, ve kterých dovednost není hlavní.</p>}
          {node.older.length > 0 && <p>Starší testy, které se do čísel nepočítají: {node.older.join(', ')}</p>}
        </div>
      )}
    </>
  )
}

/** Skills as links, one to a line, and how many there are counting the ones reached through them. */
function SkillLinks({ index, ids, all, onGo }: { index: TreeIndex; ids: string[]; all: number; onGo: (id: string) => void }) {
  if (ids.length === 0) return <p className="text-muted">nic</p>
  return (
    <ul className="space-y-1">
      {ids.map((id) => (
        <li key={id}>
          <button type="button" className={linkPlain} onClick={() => onGo(id)}>
            {index.byId.get(id)!.name}
          </button>
        </li>
      ))}
      {all > ids.length && <li className={hint}>i nepřímo celkem {all}</li>}
    </ul>
  )
}

/** Where a skill's priority comes from when others build on it: it counts their tasks too. */
function reachSentence(node: TreeNode, version: TreeVersion): string {
  const counting = node.dependents === 1 ? ONE_DEPENDENT[version] : `${node.dependents} navazujících ${LEAVES_COUNTED[version]}`
  return `Včetně ${counting} je potřeba v ${node.reach_tests} ze 16 standardních testů a v ${node.reach_recent} z 8 testů ${RECENT_YEARS}.`
}

/** The selected area, topic or skill. On top where it sits, its name, for a skill its priority, and
 *  the way to its tasks in the problem database; then sections under thin lines: for an area or topic
 *  its skills by priority, its numbers in the tests and the skills most built on; for a skill its
 *  numbers in the tests, its tasks and its links to other skills; last what else is known about it. */
export function NodeDetail({ index, node, before, after, links, version, inDatabase, onGo }: Props) {
  const isSkill = depth(node) === 2
  const groups = ancestors(index, node)
  const skills = isSkill ? [] : skillsUnder(index, node)
  const direct = index.neededBy.get(node.id) ?? []

  const stats: Stat[] = node.items
    ? [
        { value: `${node.tests} ze 16`, label: 'standardních testů', title: STANDARD_TESTS_NOTE },
        { value: `${node.recent} z 8`, label: `testů ${RECENT_YEARS}` },
        {
          value: pointsLabel(node.points),
          label: 'bodu na test',
          title: isSkill
            ? 'Kolik bodů standardního testu v průměru závisí na této dovednosti.'
            : 'Kolik bodů standardního testu v průměru připadá na úlohy těchto dovedností.',
        },
        {
          value: node.success_pct === null ? '–' : percentLabel(node.success_pct),
          label: 'úspěšnost',
          title: 'Úspěšnost úloh v řádných termínech.',
        },
      ]
    : []

  const byPriority = PRIORITIES.map((p) => ({ priority: p, count: skills.filter((s) => s.priority === p).length })).filter(
    ({ count }) => count > 0,
  )
  const foundations = skills
    .filter((s) => s.dependents > 0)
    .sort((a, b) => b.dependents - a.dependents)
    .slice(0, 10)

  const about = isSkill ? 'O dovednosti' : depth(node) === 0 ? 'O oblasti' : 'O tématu'
  const facts: { label: string; value: ReactNode }[] = []
  if (isSkill) {
    facts.push({
      label: 'Druh',
      value: (
        <>
          {capitalized(KIND_NAMES[node.kind!])} <span className="text-muted">– {KIND_MEANING[node.kind!]}</span>
        </>
      ),
    })
  }
  if (node.spec.length) facts.push({ label: 'Ve specifikaci', value: `oblast ${node.spec.join(', ')}` })
  if (node.note) facts.push({ label: 'Poznámka', value: node.note })

  return (
    <article className="@container overflow-y-auto">
      <div className="max-w-170 px-4 pt-5.5 pb-10 @md:px-8">
        {groups.length > 0 && (
          <p className={hint}>
            {groups.map((group, i) => (
              <span key={group.id}>
                {i > 0 && ' › '}
                <button type="button" className={linkQuiet} onClick={() => onGo(group.id)}>
                  {group.name}
                </button>
              </span>
            ))}
          </p>
        )}
        <h2 className="mt-1 text-title font-semibold" title={node.id}>
          {node.name}
        </h2>

        {isSkill && (
          <div className="mt-2.5">
            <p className="flex items-center gap-2">
              <PriorityBadge priority={node.priority!} />
              <span>Priorita {PRIORITY_NAMES[node.priority!]}</span>
            </p>
            {node.dependents > 0 && <p className={`mt-1 ${hint}`}>{reachSentence(node, version)}</p>}
          </div>
        )}

        {node.problems > 0 && inDatabase && (
          <p className="mt-4">
            <Link className={`${button} max-w-full gap-2`} to={problemsUrl({ skills: [node.id] })}>
              <span className="truncate">Zobrazit {problemsToShowLabel(node.problems)} v databázi úloh</span>
              <ArrowIcon />
            </Link>
          </p>
        )}
        {node.problems > 0 && !inDatabase && (
          <p className={`mt-4 ${hint}`}>
            Databáze úloh zatím filtruje jen podle původního stromu
            {isSkill ? '; úlohy níže se v ní otevřou bez filtru.' : '.'}
          </p>
        )}

        {byPriority.length > 0 && (
          <Section title={LEAVES_TITLE[version]} aside={skills.length}>
            <ul className="grid max-w-80 grid-cols-[auto_minmax(0,1fr)_auto] items-center gap-x-2.5 gap-y-1.5">
              {byPriority.map(({ priority, count }) => (
                <li key={priority} className="contents">
                  <PriorityBadge priority={priority} />
                  <span>{PRIORITY_LABELS[priority]}</span>
                  <span className="text-right text-muted tabular-nums">{count}</span>
                </li>
              ))}
            </ul>
          </Section>
        )}

        {stats.length > 0 && (
          <Section title={isSkill ? 'Přímo v testech' : 'V testech'}>
            <Stats stats={stats} />
          </Section>
        )}

        {foundations.length > 0 && (
          <Section title="Na čem se nejvíc staví" aside={`číslo: kolik dalších ${LEAVES_COUNTED[version]} na tom staví`}>
            <ul className="space-y-1">
              {foundations.map((s) => (
                <li key={s.id} className="flex items-baseline gap-4">
                  <button type="button" className={`${linkPlain} min-w-0`} onClick={() => onGo(s.id)}>
                    {s.name}
                  </button>
                  <span className="ml-auto text-muted tabular-nums">{s.dependents}</span>
                </li>
              ))}
            </ul>
          </Section>
        )}

        {isSkill && (node.uses.length > 0 || node.older.length > 0) && (
          <Section title="Úlohy" aside={node.uses.length > 0 ? `${node.uses.length} · od nejtěžší` : undefined}>
            <Tasks node={node} filterBy={inDatabase ? node : null} />
          </Section>
        )}

        {isSkill && links === 'graph' && before.size + after.size > 0 && (
          <Section
            title="Vazby"
            aside={`potřebuje ${before.size} · přímo navazuje ${direct.length}${
              after.size > direct.length ? `, celkem ${after.size}` : ''
            }`}
          >
            <PrerequisiteGraph index={index} skill={node} before={before} onGo={onGo} />
            <p className={`mt-2 ${hint}`}>Vlevo, co je potřeba umět dřív; vpravo, co přímo navazuje.</p>
          </Section>
        )}

        {isSkill && links === 'list' && (
          <Section title="Vazby">
            <h4 className={`mb-1 ${hint}`}>Potřebuje ({node.requires.length})</h4>
            <SkillLinks index={index} ids={node.requires} all={before.size} onGo={onGo} />
            <h4 className={`mt-4 mb-1 ${hint}`}>Navazuje ({direct.length})</h4>
            <SkillLinks index={index} ids={direct} all={after.size} onGo={onGo} />
          </Section>
        )}

        {facts.length > 0 && (
          <Section title={about}>
            <dl className="space-y-2">
              {facts.map(({ label, value }) => (
                <div key={label} className={factRow}>
                  <dt className="text-muted">{label}</dt>
                  <dd>{value}</dd>
                </div>
              ))}
            </dl>
          </Section>
        )}
      </div>
    </article>
  )
}
