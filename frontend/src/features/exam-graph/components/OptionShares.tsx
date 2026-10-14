import { hint, linkPlain } from '../../../shared/controls'
import { percentLabel } from '../labels'
import type { ItemOptions, Misconception } from '../types'

type Props = {
  options: ItemOptions[]
  misconceptions: Misconception[]
  /** Scrolls to the misconception's description. */
  onMisconception: (id: string) => void
}

/** For every closed item, the share of students who chose each option: the right one marked, a wrong one
 *  with the misconception it reveals or the note on why none was named. */
export function OptionShares({ options, misconceptions, onMisconception }: Props) {
  const names = new Map(misconceptions.map((m) => [m.id, m.name]))
  return (
    <div className="space-y-3">
      {options.map(({ item, options: shares }) => (
        <div key={item} className="grid grid-cols-[3rem_minmax(0,1fr)] gap-x-3">
          <span className="font-semibold">{item}</span>
          <ul>
            {shares.map((o) => (
              <li key={o.option} className="grid grid-cols-[1.25rem_4rem_4rem_minmax(0,1fr)] items-center gap-x-2.5 py-px">
                <span className={o.key ? 'font-semibold' : ''}>{o.option}</span>
                <span className="h-1.5 overflow-hidden rounded-full bg-selected">
                  <span className="block h-full bg-faint" style={{ width: `${o.share}%` }} />
                </span>
                <span className="text-right tabular-nums">{percentLabel(o.share, 1)}</span>
                <span className={`min-w-0 ${hint}`}>
                  {o.key && 'správně'}
                  {o.misconception && (
                    <button type="button" className={`${linkPlain} text-small`} onClick={() => onMisconception(o.misconception!)}>
                      {names.get(o.misconception) ?? o.misconception}
                    </button>
                  )}
                  {o.unexplained && <span title={o.unexplained}>bez pojmenované chyby</span>}
                </span>
              </li>
            ))}
          </ul>
        </div>
      ))}
    </div>
  )
}
