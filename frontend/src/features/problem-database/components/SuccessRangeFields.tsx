import { focusRing } from '../../../shared/controls'
import type { SuccessRange } from '../types'

type Props = { value: SuccessRange; onChange: (value: SuccessRange) => void }

const field = `h-9 w-18 rounded-lg border border-edge px-2.5 ${focusRing}`

function parse(text: string): number | null {
  if (text.trim() === '') return null
  const n = Number(text)
  return Number.isFinite(n) ? Math.min(100, Math.max(0, n)) : null
}

/** "From – to" percent fields for the share of students who solved a problem. */
export function SuccessRangeFields({ value, onChange }: Props) {
  return (
    <div className="w-65 px-2 py-2">
      <p className="mb-2">Kolik procent uchazečů úlohu vyřešilo</p>
      <div className="mb-2 flex items-center gap-2">
        <label className="flex items-center gap-1.5">
          od
          <input
            className={field}
            type="number"
            min={0}
            max={100}
            value={value.min ?? ''}
            placeholder="0"
            onChange={(e) => onChange({ ...value, min: parse(e.target.value) })}
          />
        </label>
        <label className="flex items-center gap-1.5">
          do
          <input
            className={field}
            type="number"
            min={0}
            max={100}
            value={value.max ?? ''}
            placeholder="100"
            onChange={(e) => onChange({ ...value, max: parse(e.target.value) })}
          />
        </label>
        <span>%</span>
      </div>
      <p className="text-small text-muted">Úlohy bez zveřejněné úspěšnosti se při použití tohoto filtru nezobrazí.</p>
    </div>
  )
}
