import { switchOption, switchOptionOff, switchOptionOn, switchTrack } from '../../../shared/controls'

type Props<T extends string> = {
  label: string
  options: T[]
  names: Record<T, string>
  hints?: Record<T, string>
  value: T
  onChange: (value: T) => void
  /** A small switch inside a pane rather than in the bar. */
  small?: boolean
}

/** Options of which one is pressed, on a grey track (the same look as the switches of /strom). */
export function Switch<T extends string>({ label, options, names, hints, value, onChange, small = false }: Props<T>) {
  return (
    <div className={switchTrack} role="group" aria-label={label}>
      {options.map((option) => (
        <button
          key={option}
          type="button"
          className={`${switchOption} ${small ? 'h-6.5 px-2.5 text-small' : 'px-3.5'} ${value === option ? switchOptionOn : switchOptionOff}`}
          aria-pressed={value === option}
          title={hints?.[option]}
          onClick={() => onChange(option)}
        >
          {names[option]}
        </button>
      ))}
    </div>
  )
}
