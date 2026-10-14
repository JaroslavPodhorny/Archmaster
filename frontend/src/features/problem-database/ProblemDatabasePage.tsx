import { useEffect, useState } from 'react'
import { useSearchParams } from 'react-router'
import { errorMessage, link, message } from '../../shared/controls'
import { Loading } from '../../shared/Loading'
import { readAddress, writeAddress } from './address'
import { ActiveFilters } from './components/ActiveFilters'
import { FilterBar } from './components/FilterBar'
import { ProblemDetail } from './components/ProblemDetail'
import { ProblemList } from './components/ProblemList'
import { useProblemSearch } from './useProblemSearch'

function isTyping(target: EventTarget | null): boolean {
  return target instanceof HTMLElement && ['INPUT', 'SELECT', 'TEXTAREA'].includes(target.tagName)
}

export function ProblemDatabasePage() {
  // A link can name the search and the problem to show: ?skills=VZT.PROC.obracene&problem=M9-2025-B-15
  const [address, setAddress] = useSearchParams()
  const [initial] = useState(() => readAddress(address))
  const search = useProblemSearch(initial)
  const { problems, options, error } = search
  const [selectedId, setSelectedId] = useState(initial.problem)
  // On narrow screens the list and the detail take turns; this says which one shows.
  const [detailOpen, setDetailOpen] = useState(selectedId !== null)

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

  // The problem named in the address may be far down the list: it comes to the middle.
  const loaded = problems !== null
  useEffect(() => {
    if (selectedId) document.querySelector(`[data-problem-id="${selectedId}"]`)?.scrollIntoView({ block: 'center' })
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [loaded])

  // The address follows the search, so a reload or the browser's Back comes to the same list and problem.
  // It names a problem only when one was picked, not when the first of the list is shown by default.
  const current = writeAddress({
    q: search.input,
    selected: search.selected,
    success: search.success,
    orderBy: search.orderBy,
    problem: !problems || problem?.id === selectedId ? selectedId : null,
  }).toString()
  useEffect(() => {
    if (current !== address.toString()) setAddress(new URLSearchParams(current), { replace: true })
  }, [current, address, setAddress])

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

  // The page fills the space under the navigation and never scrolls as a whole: the filters stay
  // on top, and the list and the detail scroll separately below them. data-detail lets the parts
  // hide themselves on narrow screens (the group-data-[detail=…]/pd classes).
  return (
    <div className="group/pd flex h-full flex-col" data-detail={detailOpen}>
      <title>{problem ? `Úloha ${problem.year} ${problem.term} ${problem.task} – Databáze úloh` : 'Databáze úloh – ArchMaster'}</title>
      <FilterBar search={search} />
      <ActiveFilters search={search} />

      {error && <p className={errorMessage}>Nepodařilo se načíst data: {error}</p>}
      {!problems && !error && <Loading />}

      {problems && problems.length === 0 && (
        <p className={message}>
          Žádná úloha těmto filtrům neodpovídá.{' '}
          <button type="button" className={link} onClick={search.clearFilters}>
            Zrušit filtry
          </button>
        </p>
      )}

      {problems && problem && (
        <div className="grid min-h-0 flex-1 grid-cols-[clamp(250px,34%,400px)_minmax(0,1fr)] max-sm:grid-cols-1">
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
            onSkill={(id) => {
              if (!search.selected.skills.includes(id)) search.toggleFilter('skills', id)
            }}
          />
        </div>
      )}
    </div>
  )
}
