import { useState } from 'react'
import { optionLabel, percentLabel, pointsLabel } from '../labels'
import type { FilterOptions, Problem } from '../types'

type Props = {
  problem: Problem
  options: FilterOptions | null
  onPrevious: (() => void) | null
  onNext: (() => void) | null
  onBack: () => void
}

/** The selected problem: where it comes from, its screenshot and its official solution. */
export function ProblemDetail({ problem, options, onPrevious, onNext, onBack }: Props) {
  const [solutionOpen, setSolutionOpen] = useState(false)

  return (
    <article className="pd-detail">
      <header className="pd-detail-header">
        <button type="button" className="pd-button pd-back" onClick={onBack}>
          Zpět na seznam
        </button>
        <div className="pd-detail-title">
          <h2>
            {problem.year} · {optionLabel(options, 'terms', problem.term)} · úloha {problem.task}
          </h2>
          <p>
            {pointsLabel(problem.points)} · {optionLabel(options, 'formats', problem.format)} · úspěšnost{' '}
            {problem.success_pct === null ? 'nezveřejněna' : percentLabel(problem.success_pct)}
            {problem.skipped_pct !== null && ` · vynechalo ${percentLabel(problem.skipped_pct)}`}
          </p>
          <p>{problem.tags.map((tag) => optionLabel(options, 'tags', tag)).join(' · ')}</p>
        </div>
        <div className="pd-detail-nav">
          <button type="button" className="pd-button" onClick={onPrevious ?? undefined} disabled={!onPrevious}>
            Předchozí
          </button>
          <button type="button" className="pd-button" onClick={onNext ?? undefined} disabled={!onNext}>
            Další
          </button>
        </div>
      </header>

      <img className="pd-shot" src={problem.screenshot_url} alt={problem.description} />

      <button type="button" className="pd-button" onClick={() => setSolutionOpen(!solutionOpen)}>
        {solutionOpen ? 'Skrýt řešení' : 'Zobrazit řešení'}
      </button>
      {solutionOpen && (
        <img
          className="pd-shot"
          src={problem.solution_url}
          alt={`Řešení úlohy ${problem.task} z klíče správných řešení`}
        />
      )}
    </article>
  )
}
