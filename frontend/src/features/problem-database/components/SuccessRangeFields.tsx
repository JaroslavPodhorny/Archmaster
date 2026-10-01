import type { SuccessRange } from '../types'

type Props = { value: SuccessRange; onChange: (value: SuccessRange) => void }

function parse(text: string): number | null {
  if (text.trim() === '') return null
  const n = Number(text)
  return Number.isFinite(n) ? Math.min(100, Math.max(0, n)) : null
}

/** "From – to" percent fields for the share of students who solved a problem. */
export function SuccessRangeFields({ value, onChange }: Props) {
  return (
    <div className="pd-range">
      <p>Kolik procent uchazečů úlohu vyřešilo</p>
      <div className="pd-range-fields">
        <label>
          od
          <input
            type="number"
            min={0}
            max={100}
            value={value.min ?? ''}
            placeholder="0"
            onChange={(e) => onChange({ ...value, min: parse(e.target.value) })}
          />
        </label>
        <label>
          do
          <input
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
      <p className="pd-hint">Úlohy bez zveřejněné úspěšnosti se při použití tohoto filtru nezobrazí.</p>
    </div>
  )
}
