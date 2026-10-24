# ArchMaster design guide

How the interface looks and behaves, so every page and every new tool feels like the same product.
Read it before any UI work; follow it unless the owner decides otherwise, and update it when they do.
The values here live in code: the tokens in `src/index.css`, the shared class names in
`src/shared/controls.ts`, the shared components in `src/shared/`. When this guide and the code disagree,
the code is what users see: fix whichever is wrong, and keep the two in step.

## 1. What the owner wants

- **Modern, plain, calm.** The model is Modern ai platform web interface (chosen 4 October 2026): white page,
  near-black text, soft greys, a light-grey sidebar, pill-shaped buttons and fields, rounded rows,
  generous spacing.
- **Not "AI slop."** No gradients, no purple or indigo, no letter-spaced or uppercase labels, no
  decorative cards, no icons for decoration, no animations or transitions.
- **No hunting for controls.** Filters and navigation are always visible: a fixed bar on top, panes below
  that scroll on their own. The window itself never scrolls.
- **Readable at a glance.** Every number has its label right beside it, related things are grouped under
  a heading, nothing is "placed everywhere". When in doubt, fewer kinds of visual treatment.
- **Nothing moves or spills.** A control stays where it is when toggled, text and controls stay inside
  their containers, a bar wraps into at most two tidy rows.

The owner rejected, at one time or another: long scrolling pages, a sidebar that leaves a grey strip
when hidden, bold used for two meanings (level and importance), grey tags plus dotted underlines plus
inline hints all at once ("cluttered"), label–value fact lists with mixed content, and a theme switch
that overflowed its track. Avoid all of these.

For a new page or a real redesign, show a mockup first (a static HTML page served temporarily from
`frontend/public/`, deleted afterwards). When the right answer is unclear, offer two or three variants
on real data side by side and let the owner choose.

## 2. Tokens (`src/index.css`)

Use only these; Tailwind's default palette, radii and shadows are switched off. Never write a fixed
colour in a component, or the dark theme breaks.

### Colours

| Token | Light | Dark | Use |
|---|---|---|---|
| `page` | #fff | #212121 | page background; buttons, fields, graph boxes; `text-page` on `bg-ink` |
| `ink` | #0d0d0d | #ececec | text; what is switched on (active filter, pressed toggle, priority 1 badge) |
| `muted` | #5f5f5f | #a8a8a8 | secondary text, labels, hints; priority 2 badge |
| `faint` | #9a9a9a | #747474 | placeholders, disabled text, counts in the tree, bar fills |
| `line` | #ebebeb | #303030 | hairlines: pane borders, section rules, table rows |
| `edge` | #dedede | #444 | borders of controls and graph boxes |
| `surface` | #f9f9f9 | #181818 | the sidebar |
| `tint` | #f2f2f2 | #2b2b2b | hover on rows and buttons, chips, the track of a switch |
| `selected` | #e8e8e8 | #393939 | the selected row, the active sidebar link, hover inside menus, bar tracks |
| `raised` | #fff | #333 | menus, the pressed option of a switch |
| `accent` | #1b5fc1 | #7ba8f5 | links and graph highlights only |
| `accent-soft` | #e9f0fb | #1e2b40 | fill of highlighted graph boxes |
| `paper` | #fff | #fff | behind scanned test pages, white in both themes |
| `shade` | 20 % black | 50 % black | over the page behind the sidebar overlay |
| `error` | #a11 | #ff7b7b | error messages |

Black (`ink`) means "switched on", never decoration. The accent never marks state; it marks links and
the parts of a graph that belong to the selection.

### Type

- System font stack (`ui-sans-serif, -apple-system, system-ui, …`), root size 15 px, line height 1.45,
  antialiased.
- **Four sizes only:** `text-title` (1.4rem, a pane's heading, also big numbers and the app name), body
  (the default), `text-small` (counts, hints, secondary text, table headers), `text-tiny` (graph boxes,
  badges). No `text-[…]`.
- Weights: `font-semibold` for headings, areas in the tree and big numbers; `font-medium` for buttons,
  switches and the active sidebar link; everything else regular. Weight shows level, never importance.
- `tabular-nums` wherever numbers stand in columns or change in place.

### Spacing, corners, shadows, layers

- One spacing step is 4 px (`p-4` = 16 px). Gaps of 1, 2, 3, 4 and 6 steps: tight within a row, wider
  between rows, widest between sections.
- Corners: `rounded-full` for buttons, fields, chips and switches; `rounded-md` (8) graph boxes, badges,
  small fields; `rounded-lg` (10) menu lines, tree rows, nav links, icon buttons; `rounded-xl` (14) list
  rows and frames around pictures and graphs; `rounded-2xl` (16) menus.
- Shadows: `shadow-panel` (menus, the sidebar overlay), `shadow-control` (the search field),
  `shadow-raised` (pressed switch option). They point at CSS variables so the dark theme can change them.
- Layers: sticky headings inside a pane `z-10`, menus `z-20`, the sidebar overlay `z-30` (shade) and
  `z-40` (panel).

## 3. Page anatomy

```
┌ sidebar (240 px, surface) ┬ bar: [sidebar button] [search] [filters…]      [view switches] ┐
│ [⊟] ArchMaster            ├──────────────────────────────────────────────────────────────────┤
│ Strom učiva               │ list / tree / graph pane   │ detail pane                         │
│ Databáze úloh             │ (scrolls on its own)       │ (scrolls on its own)                │
│ …                         │                            │                                     │
│ Matematika M9             │                            │                                     │
│ [Světlý|Tmavý|Systém]     │                            │                                     │
└───────────────────────────┴────────────────────────────┴─────────────────────────────────────┘
```

- **Shell** (`src/Sidebar.tsx`, `WithSidebar`): sidebar beside the page from 1024 px; hidden, it is gone
  completely and its button is the first thing in the page's bar (`shared/SidebarButton.tsx`, which every
  page's bar must render). Between 640 and 1024 px the button opens it over the page (shade behind, page
  `inert`, closes on Escape, a click outside or choosing a page). Below 640 px the navigation is a row
  above the page. Whether it is hidden is remembered in `localStorage`, not in the address.
- **The sidebar button never moves**: open or hidden it stands 10 px from the left, centred on the bar's
  first row (y 15–53). Hence every page's bar is `px-6` with `pt-3.5` and a 40 px first row (the search
  field's height), `SidebarButton` reaches into that padding (`-ml-3.5`), and the sidebar's top row
  matches (`pt-3.5`, `h-10`, no padding of its own). Keyboard focus moves to the button's counterpart
  when it is pressed.
- **The sidebar has one left edge.** The button's box lines up with the links' rows (10 px), and its icon
  with the links' text and the bottom part's text (22 px: `px-3` inside the sidebar's `px-2.5`); the app
  name follows the icon (`gap-1`). Anything added to the sidebar keeps to these two lines.
- **The bar** is `border-b border-line`, filters in one group on the left, view switches in one group
  on the right (`justify-between`). When both do not fit, the switch group moves to a second line as a
  whole. Nothing else lives in the bar: counts and sort order go with the results (the row above the
  list, a pane's tool row).
- **Panes** form a grid under the bar (`min-h-0 flex-1`), divided by `border-line`, each with its own
  `overflow-y-auto`. Below 640 px they stack or take turns (list ↔ detail with "Zpět na seznam").
- **A detail pane** is `@container`, padding `px-8 pt-5.5 pb-10` (`px-4` when narrow), text limited to
  `max-w-170` (680 px, about 75 characters a line).

## 4. Components and patterns

Use the shared piece when one exists; if two features need something new, it goes to `src/shared/`.

### Controls (`shared/controls.ts`)

- `button`: outline pill (`h-9`, `border-edge`, hover `tint`). `buttonActive`: black pill (`bg-ink
  text-page`) for a filter or toggle that is on. Disabled: faint text and border.
- `input`: the search field at the start of a bar, a 40 px pill with `shadow-control`; 240 px wide, it
  narrows to 160 px before the bar wraps; full width on a phone.
- `iconButton`: 38 px square, `rounded-lg`, muted icon, `tint` on hover; for the sidebar toggle and
  previous/next.
- `switchTrack` + `switchOption` (+ `switchOptionOn` / `switchOptionOff`): a grey track with the chosen
  option raised. The option has no side padding of its own; a switch in a bar adds `px-3.5`, a narrow
  one less (the theme switch: `flex-1 px-1.5 text-small`). Make sure it fits its container.
- Links: `link` (underlined: in running text or alone), `linkPlain` (accent, underline on hover: lists
  of skills or items), `linkQuiet` (grey: secondary actions such as "Rozbalit", breadcrumbs).
- `selectedRow` (`bg-selected`) and `rowHover` (`hover:bg-tint`): selection is a grey rounded row, no
  accent bar.
- `hint` for secondary text, `message` / `errorMessage` for pane-level states, `focusRing` on every
  interactive element.

### Filters (`shared/Dropdown.tsx`, `shared/CheckOption.tsx`)

- Every filter is a pill that opens a menu of checkboxes; nothing ticked means no filter. In use, the
  pill turns black and its label gets the count: "Rok · 1".
- Menu: `rounded-2xl bg-raised p-1.5 shadow-panel`, kept inside the window; lines `rounded-lg px-2.5
  py-1.5`, hover `bg-selected`, the count right-aligned in `hint`. Checkboxes take the ink colour.
- Closes on a click outside or Escape (focus back to its pill). Stays open while ticking.
- Filters in use repeat as chips in the results row (`rounded-full bg-tint`, a grey ×, hover
  `bg-selected`), each removable with one click, then "Zrušit vše" in `linkQuiet`.
- A filter that cannot apply in the current state is disabled, with a tooltip saying why ("Jen
  související" while an area or topic is selected).

### Lists and trees

- A list is a column with `p-2` of rounded rows (`rounded-xl px-3 py-2.5`), no dividing lines; meta in
  `text-small text-muted` on top, the main text under it (two lines at most).
- Tree rows: `rounded-lg px-2.5 py-1.25`, indent by level (`pl-7`, `pl-10`), a faint ▸/▾ for groups, a
  faint count after a group's name. Only areas are bold.
- Long lists load the next page by themselves as the end comes near (the "Zobrazit další" button stays
  as a fallback). Arrow keys walk the list or tree; a row reached by a link or the address comes to the
  middle of the pane, a row reached by the keys just into view.
- A pane's tool row (`px-5 pt-2.5 pb-1 text-small`) holds actions on that pane in `linkQuiet` and, at its
  right end, how many items the filters leave ("41 z 157 dovedností").

### Detail panes

- **Header:** breadcrumb in `hint` with `linkQuiet` parts → title (`text-title font-semibold`) → the one
  fact that identifies the thing (a skill's priority badge and name, with one grey sentence on where the
  priority comes from) → the link onward as a button with an arrow.
- **Sections** (`shared/Section.tsx`): a hairline above, a semibold heading, a grey count or ordering
  after it ("Úlohy 31 · od nejtěžší"). One job per section. Order by importance, top to bottom.
- **Numbers** stand in a row: the value large (`text-title font-semibold`), what it counts under it in
  `hint`, written to read as one phrase ("16 ze 16" / "standardních testů"). Columns are divided by
  hairlines; four in a row from a 30rem container, two by two below.
- **Tables** for lists of things with properties: a header row in `hint` with `border-b`, rows with
  `border-b py-1.5`, the whole row a link with `hover:bg-tint`. Spell out codes ("2025, 1. řádný", not
  "2025 A"). A thin bar (`h-1.5 rounded-full`, track `bg-selected`, fill `bg-faint`) may sit beside a
  percentage; in a narrow pane the bar goes and the text keeps its room. Show the first 8, the rest on
  "Zobrazit všech N".
- **Loose facts** (kind, specification, note) come last as label–value rows: label `text-muted` in a
  7.5rem column, above the value when the pane is narrow.
- Each thing appears once: a skill needed by several items is one row listing the items ("1.1, 1.2,
  1.3"), not three rows.
- Previous / next are two `iconButton`s with chevrons (∧ ∨), with the arrow keys named in their titles.

### Badges, icons, graphs, pictures

- Priority badge (`topic-tree/components/PriorityBadge.tsx`): 20 px, `rounded-md`, `text-tiny
  font-semibold`, darker the more tests need the skill: 1 `bg-ink`, 2 `bg-muted`, 3 outlined, S dashed
  outline. The same badge in the tree, the detail and anywhere priority shows.
- Icons (`shared/icons.tsx`, all of them in one file): line icons, 1.5 stroke, round caps and joins,
  `currentColor`, 16–20 px. Only on controls with their usual meaning: the sidebar toggle, chevrons for
  previous/next, an arrow (`ArrowIcon`) after any link or button that leads to another page.
- Graph boxes: 150 × 36 px, `rounded-md border border-edge bg-page text-tiny`, two lines at most; the
  selection `border-accent bg-accent-soft text-accent font-semibold`; links `stroke-edge`, the selected
  chain `stroke-accent`. A graph sits in a `rounded-xl border-line p-3` frame with one grey line under it
  saying how to read it.
- Scans of test pages sit on `bg-paper` in a `rounded-xl border-line p-2` frame, so they read as one
  white sheet in both themes.

### States

- Empty: a `message` saying nothing matches, with a "Zrušit filtry" link.
- Loading: `shared/Loading.tsx`, which shows "Načítám…" only after 0.4 s so fast loads never flash it.
- Error: `errorMessage` "Nepodařilo se načíst data: …".
- Page titles name what is shown: "Procenta – Strom učiva", "Úloha 2025 B 15 – Databáze úloh".

## 5. Responsive rules

- Window breakpoints: 640 px (`sm`: phone layout below) and 1024 px (sidebar beside the page from here).
- Panes use container queries (the pane is `@container`): labels above values below `@md` (28rem,
  420 px at our root size); four numbers in a row from `@[30rem]`.
- Check every change at 375, 820, 1100, 1280 and 1440 px. At each: no horizontal scroll of the page,
  no text cut off except where truncation is meant (tree names, two-line list descriptions), bars in at
  most two rows, nothing hidden behind something else.
- Keep labels from breaking badly: a non-breaking space before `%` (`percentLabel`), a word joiner in year
  ranges (`RECENT_YEARS`), `whitespace-nowrap` on short controls and values.

## 6. Dark theme

- Every colour is a token; `:root[data-theme='dark']` redefines them. A script in `index.html` sets
  `data-theme` before the first paint from the sidebar's choice (`localStorage` key `archmaster.theme`)
  or the system's setting, and follows the system while "Systém" is chosen. `color-scheme` follows, so
  native controls and scrollbars match.
- `text-page` on `bg-ink` inverts correctly (an active filter is a light pill in the dark theme).
- Check every change in both themes: menus raised above the page, hairlines visible, badges readable,
  scans on white paper.

## 7. Interaction and accessibility

- Everything interactive has `focusRing` and works from the keyboard. Escape closes what is open (menus,
  the sidebar overlay) and returns focus to the control that opened it.
- A control that is toggled keeps its place; if the pressed control disappears, focus moves to its
  counterpart.
- What another page or a reload must restore (selected node, search, shown problem, view) lives in the
  address; per-browser preferences (sidebar, theme) in `localStorage`, read and written in `try/catch`.
- `aria-label` on icon-only buttons, `aria-pressed` on toggles, `aria-expanded` on menus, real
  `title`s on badges and truncated names.

## 8. Words

- Czech, in students' words; internal ids (`VZT.PROC.obracene`) never in visible text, at most in a
  tooltip.
- Explain by wording first: a label says what its value counts so it needs no tooltip. A tooltip only
  adds detail; where a label still needs one, `explained` (dotted underline) marks it. State the page
  must announce stays visible as `hint`.
- Correct Czech forms: plural helpers for counts (`problemCountLabel`, `skillCountLabel`,
  `problemsToShowLabel`), agreement with the number ("před ní" / "před nimi"). Text shared by both
  trees is worded so it fits both "dovednost" (feminine) and "princip" (masculine), or takes the word
  from `LEAVES_COUNTED` / `LEAVES_TITLE`.
- En dash for ranges and asides (2025–2026, "Priorita 1 – nejčastěji potřeba"), Czech quotes „…“.

## 9. Before calling UI work done

1. Build and lint: `npm --prefix frontend run build && npm --prefix frontend run lint`.
2. Look at it in the browser at the five widths of section 5, in both themes, on real data, including
   the awkward cases: the longest names, a skill with 30 tasks, one with none (priority S), an area, the
   new tree, an empty search, a task without published success rate.
3. Try the keyboard: Tab through the bar, open and close a menu with Escape, arrow keys in lists, the
   sidebar toggle.
4. Run the overflow check below in the browser console on each page; it should print nothing.

```js
// Elements whose text is cut off (outside intentional truncation) and whether the page scrolls sideways.
;[...document.querySelectorAll('body *')].filter((el) => {
  if (el.closest('[role=tree], svg') || String(el.className).includes('line-clamp')) return false
  const cs = getComputedStyle(el)
  return el.children.length === 0 && el.textContent.trim() && el.clientWidth > 0 &&
    el.scrollWidth > el.clientWidth + 1 && (cs.overflow === 'hidden' || cs.textOverflow === 'ellipsis')
}).forEach((el) => console.log('cut off:', el.textContent.trim()))
if (document.documentElement.scrollWidth > innerWidth + 1) console.log('page scrolls sideways')
```
