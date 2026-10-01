import { useEffect, useState } from 'react'
import { ActiveFilters } from './components/ActiveFilters'
import { FilterBar } from './components/FilterBar'
import { ProblemDetail } from './components/ProblemDetail'
import { ProblemList } from './components/ProblemList'
import { useProblemSearch } from './useProblemSearch'
import './problem-database.css'

function isTyping(target: EventTarget | null): boolean {
  return target instanceof HTMLElement && ['INPUT', 'SELECT', 'TEXTAREA'].includes(target.tagName)
}

export function ProblemDatabasePage() {
  const search = useProblemSearch()
  const { problems, options, error } = search
  const [selectedId, setSelectedId] = useState<string | null>(null)
  // On narrow screens the list and the detail take turns; this says which one shows.
  const [detailOpen, setDetailOpen] = useState(false)

  // The selection follows the results: keep it while it is still listed, otherwise take the first.
  const index = problems ? Math.max(0, problems.findIndex((p) => p.id === selectedId)) : 0
  const problem = problems?.[index] ?? null

  function select(id: string, openDetail = true) {
    setSelectedId(id)
    if (openDetail) setDetailOpen(true)
    document.querySelector(`[data-problem-id="${id}"]`)?.scrollIntoView({ block: 'nearest' })
  }

  const previous = problems && index > 0 ? () => select(problems[index - 1].id) : null
  const next = problems && index < problems.length - 1 ? () => select(problems[index + 1].id) : null

  // Arrow keys walk through the list unless the user is typing in a field.
  useEffect(() => {
    function onKeyDown(e: KeyboardEvent) {
      if (isTyping(e.target) || e.metaKey || e.ctrlKey || e.altKey) return
      const step = e.key === 'ArrowDown' ? next : e.key === 'ArrowUp' ? previous : null
      if (!step) return
      e.preventDefault()
      step()
    }
    document.addEventListener('keydown', onKeyDown)
    return () => document.removeEventListener('keydown', onKeyDown)
  })

  return (
    <div className={detailOpen ? 'pd-page pd-page-detail' : 'pd-page'}>
      <header className="pd-top">
        <h1>Databáze úloh</h1>
        <p>Matematika, přijímací zkouška z 9. ročníku (M9), 2022–2026</p>
      </header>
      <FilterBar search={search} />
      <ActiveFilters search={search} />

      {error && <p className="pd-message pd-error">Nepodařilo se načíst data: {error}</p>}

      {problems && problems.length === 0 && (
        <p className="pd-message">
          Žádná úloha těmto filtrům neodpovídá.{' '}
          <button type="button" className="pd-link" onClick={search.clearFilters}>
            Zrušit filtry
          </button>
        </p>
      )}

      {problems && problem && (
        <div className="pd-panes">
          <ProblemList
            problems={problems}
            total={search.total}
            selectedId={problem.id}
            onSelect={select}
            onLoadMore={search.loadMore}
            loadingMore={search.loadingMore}
          />
          <ProblemDetail
            key={problem.id}
            problem={problem}
            options={options}
            onPrevious={previous}
            onNext={next}
            onBack={() => setDetailOpen(false)}
          />
        </div>
      )}
    </div>
  )
}
