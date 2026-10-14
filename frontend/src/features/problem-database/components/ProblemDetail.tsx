import { useState } from 'react'
import { Link } from 'react-router'
import { button, hint, iconButton, linkPlain, linkQuiet } from '../../../shared/controls'
import { ArrowIcon, ChevronIcon } from '../../../shared/icons'
import { treeUrl } from '../../../shared/routes'
import { Section } from '../../../shared/Section'
import { optionLabel, percentLabel, pointsLabel, skillCountLabel } from '../labels'
import type { FilterOptions, ItemSkill, Problem } from '../types'
import { ProblemSkillGraph } from './ProblemSkillGraph'

type Props = {
  problem: Problem
  options: FilterOptions | null
  onPrevious: (() => void) | null
  onNext: (() => void) | null
  onBack: () => void
  /** Narrows the list to problems needing the skill. */
  onSkill: (skillId: string) => void
}

// The task and its solution on a sheet of white with rounded corners, in the dark theme too: the scans are
// white, so their own square edges disappear into it.
const shot = 'block h-auto max-w-[min(100%,720px)] rounded-xl border border-line bg-paper p-2'

/** A skill the problem needs and the items that need it; `main` is false where it is not the item's
 *  main skill. */
type SkillUse = { id: string; name: string; items: { item: string; main: boolean }[] }

/** Each skill once, in the order it first appears, with the items that need it. */
function skillUses(skills: ItemSkill[]): SkillUse[] {
  const uses = new Map<string, SkillUse>()
  for (const skill of skills) {
    const use = uses.get(skill.skill_id) ?? { id: skill.skill_id, name: skill.name, items: [] }
    use.items.push({ item: skill.item, main: skill.main })
    uses.set(skill.skill_id, use)
  }
  return [...uses.values()]
}

/** The selected problem, in the order a student works through it: where it comes from with its numbers,
 *  the skills it needs (a click narrows the list to them; "ve stromu" goes to the curriculum tree), its
 *  screenshot, its official solution, and last the graph of what those skills rest on. */
export function ProblemDetail({ problem, options, onPrevious, onNext, onBack, onSkill }: Props) {
  const [solutionOpen, setSolutionOpen] = useState(false)
  const uses = skillUses(problem.skills)
  // Item numbers only help when the task has several items.
  const severalItems = new Set(problem.skills.map((skill) => skill.item)).size > 1
  const needed = problem.skill_graph.filter((skill) => skill.needed).length
  const before = problem.skill_graph.length - needed

  return (
    <article className="overflow-y-auto px-8 pt-5.5 pb-10 max-sm:px-4 max-sm:group-data-[detail=false]/pd:hidden">
      {/* On a phone the back button and the arrows take the first line and the title goes under them. */}
      <header className="mb-4 flex items-start gap-3 max-sm:flex-wrap">
        <button type="button" className={`${button} sm:hidden`} onClick={onBack}>
          Zpět na seznam
        </button>
        <div className="min-w-0 flex-1 max-sm:order-3 max-sm:basis-full">
          <h2 className="text-title font-semibold">
            {problem.year} · {optionLabel(options, 'terms', problem.term)} · úloha {problem.task}
          </h2>
          <p className="mt-1 text-muted">
            {pointsLabel(problem.points)} · {optionLabel(options, 'formats', problem.format)} · úspěšnost{' '}
            {problem.success_pct === null ? 'nezveřejněna' : percentLabel(problem.success_pct)}
            {problem.skipped_pct !== null && ` · vynechalo ${percentLabel(problem.skipped_pct)}`}
          </p>
        </div>
        <div className="flex gap-1 max-sm:ml-auto">
          <button
            type="button"
            className={iconButton}
            onClick={onPrevious ?? undefined}
            disabled={!onPrevious}
            aria-label="Předchozí úloha"
            title="Předchozí úloha (šipka nahoru)"
          >
            <ChevronIcon direction="up" />
          </button>
          <button
            type="button"
            className={iconButton}
            onClick={onNext ?? undefined}
            disabled={!onNext}
            aria-label="Další úloha"
            title="Další úloha (šipka dolů)"
          >
            <ChevronIcon direction="down" />
          </button>
        </div>
      </header>

      {/* Each skill once: its name narrows the list to problems needing it, the items that need it
          follow (lighter where it is not the item's main skill), and the link to the tree ends the line. */}
      <ul className="mb-5 space-y-1.5" aria-label="Dovednosti potřebné k úloze">
        {uses.map((use) => (
          <li key={use.id} className="grid grid-cols-[minmax(0,1fr)_auto_auto] items-baseline gap-x-4">
            <button
              type="button"
              className={linkPlain}
              title="Zobrazit úlohy s touto dovedností"
              onClick={() => onSkill(use.id)}
            >
              {use.name}
            </button>
            <span
              className="text-small text-muted tabular-nums"
              title={severalItems ? 'Položky úlohy, které dovednost potřebují; světleji ty, kde není hlavní' : undefined}
            >
              {severalItems &&
                use.items.map(({ item, main }, i) => (
                  <span key={item}>
                    {i > 0 && ', '}
                    <span className={main ? '' : 'text-faint'}>{item}</span>
                  </span>
                ))}
            </span>
            <Link
              className={`${linkQuiet} inline-flex items-center gap-1 text-small whitespace-nowrap`}
              to={treeUrl(use.id)}
              title="Zobrazit dovednost ve stromu učiva"
            >
              ve stromu
              <ArrowIcon size={12} />
            </Link>
          </li>
        ))}
      </ul>

      <img className={shot} src={problem.screenshot_url} alt={problem.description} />

      <div className="mt-4">
        <button type="button" className={button} onClick={() => setSolutionOpen(!solutionOpen)}>
          {solutionOpen ? 'Skrýt řešení' : 'Zobrazit řešení'}
        </button>
        {solutionOpen && (
          <img
            className={`${shot} mt-3`}
            src={problem.solution_url}
            alt={`Řešení úlohy ${problem.task} z klíče správných řešení`}
          />
        )}
      </div>

      <Section
        title="Na čem úloha staví"
        aside={
          before > 0
            ? `${skillCountLabel(needed)} úlohy, ${before} před ${needed === 1 ? 'ní' : 'nimi'}`
            : 'žádná dovednost úlohy nestaví na jiné'
        }
      >
        <ProblemSkillGraph skills={problem.skill_graph} />
        <p className={`mt-2 ${hint}`}>
          Zvýrazněné dovednosti úloha potřebuje; vlevo od nich, co je potřeba umět dřív.
        </p>
      </Section>
    </article>
  )
}
