import { hint, linkPlain } from '../../../shared/controls'
import { ANSWER_STATES, percentLabel } from '../labels'
import type { ReviewEntry } from '../types'
import type { ExamGraph } from '../useExamGraph'

/** The open questions about one task, one sentence each. Nothing here changes the stored data: each
 *  difference is a proposal for the owner to accept or reject. */
export function ReviewNotes({ graph, entries }: { graph: ExamGraph; entries: ReviewEntry[] }) {
  const name = (id: string) => graph.principles.get(id)?.name ?? id
  const principle = (id: string) => (
    <button key={id} type="button" className={linkPlain} onClick={() => graph.go({ view: 'princip', node: id })}>
      {name(id)}
    </button>
  )
  const list = (ids: string[]) => ids.map((id, i) => [i > 0 && ', ', principle(id)])
  const item = (ref: string) => ref.split(' ').slice(2).join(' ')

  return (
    <>
      <ul className="space-y-2">
        {entries.map((entry, i) => (
          <li key={i}>
            {entry.kind === 'rozdil-principu' && (
              <>
                <span className="font-semibold">{item(entry.ref)}</span>
                {entry.missing.length > 0 && <> · kroky používají {list(entry.missing)}, uložený seznam to nemá</>}
                {entry.extra.length > 0 && <> · uložený seznam má navíc {list(entry.extra)}, žádný krok to nepoužívá</>}
                {entry.extra_reused.length > 0 && (
                  <> · uložený seznam má i {list(entry.extra_reused)}, to používá jen výsledek převzatý z dřívější položky</>
                )}
              </>
            )}
            {entry.kind === 'odpoved' && <>Odpovědi: {ANSWER_STATES[entry.state]}</>}
            {entry.kind === 'poznamka' && entry.text}
            {entry.kind === 'nevysvetleno' && (
              <>
                <span className="font-semibold">{item(entry.ref)}</span> · chybná možnost bez pojmenované chyby: {entry.text}
              </>
            )}
            {entry.kind === 'neprozkoumano' && (
              <>
                <span className="font-semibold">{item(entry.ref)}</span> · chybnou možnost volilo{' '}
                {percentLabel(entry.share, 1)} žáků, správnou {percentLabel(entry.key_share, 1)}; zatím neprozkoumáno
              </>
            )}
          </li>
        ))}
      </ul>
      <p className={`mt-2.5 ${hint}`}>Jde o návrhy ke kontrole: uložené řešení a seznamy principů se samy nemění.</p>
    </>
  )
}
