// Class names of the controls every page uses. Anything only one feature needs
// stays in that feature's components.

export const focusRing = 'focus-visible:outline-2 focus-visible:outline-offset-1 focus-visible:outline-accent'

// Buttons and fields are pills; a link may look like a button too, hence inline-flex.
const buttonBase = `inline-flex h-9 cursor-pointer items-center rounded-full border px-3.5 font-medium whitespace-nowrap disabled:cursor-default disabled:border-line disabled:text-faint ${focusRing}`

export const button = `${buttonBase} border-edge bg-page not-disabled:hover:bg-tint`

/** A button whose filter or state is in use: black. */
export const buttonActive = `${buttonBase} border-ink bg-ink text-page`

/** The search field at the start of a bar: up to 240 px wide, it narrows to 160 px before the bar wraps. */
export const input = `h-10 max-w-60 min-w-40 flex-[1_1_10rem] rounded-full border border-edge bg-page px-4 shadow-control placeholder:text-faint ${focusRing}`

/** A link in running text, or a lone link that must read as one: underlined. */
export const link = `cursor-pointer text-left text-accent underline ${focusRing}`

/** A link among many (a list of skills or items): the accent colour alone marks it, the underline
 *  comes on hover. */
export const linkPlain = `cursor-pointer text-left text-accent hover:underline ${focusRing}`

/** A secondary link: grey until hovered. */
export const linkQuiet = `cursor-pointer text-left text-muted hover:text-ink hover:underline ${focusRing}`

/** A switch between views or settings: options on a grey track, the pressed one raised from it.
 *  An option has no side padding of its own; a switch in a bar gives it px-3.5, a narrower one less. */
export const switchTrack = 'flex rounded-full bg-tint p-0.75'
export const switchOption = `h-7.5 min-w-0 cursor-pointer rounded-full font-medium whitespace-nowrap ${focusRing}`
export const switchOptionOn = 'bg-raised shadow-raised'
export const switchOptionOff = 'text-muted hover:text-ink'

/** A square button holding only an icon, such as the one that shows or hides the sidebar. */
export const iconButton = `grid size-9.5 flex-none cursor-pointer place-items-center rounded-lg text-muted enabled:hover:bg-tint enabled:hover:text-ink disabled:cursor-default disabled:opacity-35 ${focusRing}`

/** The selected row of a list or tree: a grey, rounded row (the row gives the rounding). Hover stays fainter. */
export const selectedRow = 'bg-selected'

export const rowHover = 'hover:bg-tint'

/** The heading of a section inside a pane. */
export const sectionHeading = 'font-semibold'

/** Secondary text: counts, notes, the state of something. Explanations go in a tooltip instead. */
export const hint = 'text-small text-muted'

/** A label that explains itself on hover (its `title`): a dotted underline says there is more. */
export const explained = 'cursor-help underline decoration-faint decoration-dotted underline-offset-3'

export const message = 'px-4 py-6 text-muted'

export const errorMessage = 'px-4 py-6 text-error'
