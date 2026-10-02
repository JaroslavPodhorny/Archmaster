# Graph design specification (M9)

Written 2 October 2026 as a handoff. It records the review of the old topic tree, the goal, the rules decided while solving all 20 tests, the node set that came out of it, and what is left to do. A new session should be able to finish the work from this file and the data it points to, without the earlier conversation.

## 1. Goal (the owner's words)

> What the graph is supposed to be is if you solved every problem in all the 20 tests and written down all the solutions the graph elements would be all of the principles that you would use and those principles would be connected together if one is dependent on the other and grouped. The detail of all the principles should be one that is practical and detailed enough for classifying student gaps without being overly detailed (like for example you don't need to be super detailed like saying subtracting equation deserves a node when it should just be equivalent transformation of equation node) and the database should be cross-referenced with the graph in a way that each task has a subgraph of principles it needs to be solved (this really tests if the graph is good because you can solve the problem and see how good of an insight the graph gives you). Also the graph view is currently really messy so try to fix it so it is nicer to search through, make the UX better.

Longer-term purpose: the graph is the core of the application. A CERMAT problem is a subgraph; a student's knowledge is a state of the full graph.

## 2. Where things are

| What | Path | State |
|---|---|---|
| Solutions of all 610 items, with the principles each uses (final ids) | `analysis/data/m9_item_solutions.json` | **done** |
| Raw solving notes per test (working ids) and the working vocabulary | `analysis/solving/raw/` | done, audit trail |
| Script that turns raw notes into the file above (holds the id mapping) | `analysis/solving/consolidate.py` | done |
| Helpers: catalog rows + trimmed key of a test; enlarge part of a task figure | `analysis/solving/info.py`, `zoom.py` | done |
| Old tree and old assignment, untouched copies | `analysis/data/before_rebuild/` | backup |
| Tree still in use by the app | `analysis/data/m9_topic_tree.json`, `m9_item_skills.json`, `m9_item_skills_older.json` | **old, not yet replaced** |

Format of `m9_item_solutions.json`:

```json
{"2023 A": {"6.1": {"reseni": "základna AB = 6 cm, výška k ní je BC = 8 cm (leží vně trojúhelníku): S = 6 · 8 : 2 = 24 cm²",
                    "principy": ["GEO.ROV.trojuhelnik", "KON.VLAST.vyska"]}}}
```

Item names are those of the task catalog. `principy` has the main principle first.

## 3. Review of the old tree (why it is being rebuilt)

Old tree: 7 areas, 24 topics, 162 skills (32 specification-only), 133 prerequisite links.

1. What a task needs was stored twice and inconsistently: the item's list and the `requires` closure. 149 of 295 multi-skill items listed a skill with its own prerequisite; others left it implicit. The list averaged 1.7 skills, the closure 4.9 (up to 14).
2. `requires` mixed meanings and was too strong in places (n-tý člen ended up requiring fractions and reversed comparisons; krychle a kvádr required strana z obsahu). 47 skills had no link; there was no link between GEO and KON although twin nodes existed.
3. Nodes were uneven: bundles (four fraction operations in one node; six area formulas in one "fact"), bins defined by what they are not (úsudek bez rovnice, netradiční úlohy), slivers (29 skills with one or two items).
4. No notion of "how well": success of items with the same main skill ranged e.g. 9–57 %.
5. A whole item's success was credited to every listed skill; 55 of 130 used skills never appeared alone.
6. Ids encode position; moving a skill changes its id.
7. Notes mixed tips, traps, specification quotes and hand-typed counts, in English; 60 were empty.
8. The assignment was made from task wording, figures mostly not seen.

Points 1–3 and 8 are addressed by this rebuild. Points 4–6 are **not** part of it (section 10).

## 4. What a node is (granularity rules)

- A node is one **principle**: a rule, fact or method that a solution applies as a step, and that a student either has or lacks.
- Fine enough to name a gap, no finer. "Ekvivalentní úpravy rovnice" is one node; adding to both sides is not. "Odstranění zlomků z rovnice" is a separate node, because it is a distinct step with its own typical error.
- No bundles: the old "čtyři operace se zlomky" is now krácení, sčítání (společný jmenovatel), násobení a dělení.
- No bins. The only general node kept is `VZT.SLOV.usudek`, defined positively: reading a text into a chain of simple calculations, used only when nothing else applies.
- No node for a task type that is only a combination: "rovnice se závorkami" is úpravy + roznásobení.
- One principle, one node, wherever it is used: Thaletova věta, rovnoramenný trojúhelník, osa úhlu, výška exist once and serve both angle calculation and constructions.
- A principle used once stays if it is a real, nameable rule (smíšené číslo, stupně a minuty, poměr obsahů v měřítku).
- Specification-only nodes (no item of the 20 tests needs them) are kept, marked by having no items, and carry no links.

## 5. What a link is

`B requires A` means B cannot be carried out or understood without A. Direct links only (no link that another path already implies). A prerequisite must come earlier in the tree's learning order (the editor validates this), which is why basic constructions (KON) now precede calculations (GEO).

`requires` is for learning order and inference. It does **not** define what a task needs; the item's list does (section 6).

## 6. Assignment rules (item → principles)

1. Solve the item from the booklet image; check the result against the official key.
2. List **every principle the natural solution applies as a step**, the main one first (the one the item is chiefly about, usually where it is lost).
3. Do not list a principle only because a listed one requires it; list it if it is actually applied.
4. A formula that is only a shortcut is not listed (a² − b² when plain multiplication does it). `ALG.VYR.rozdil` is listed only for factoring.
5. `ALG.ROV.upravy` is listed for any equation of more than one step; a one-step equation (ax = b) does not list it. Combining like terms inside an equation is part of úpravy; `ALG.VYR.scitani` is listed in expression tasks and where a minus before a bracket matters.
6. `POC.VYR.poradi` only where the order of operations is a real decision. Whole-number arithmetic is never listed.
7. When two solution paths exist, take the one a 9th-grader would most naturally use.
8. A task's subgraph = its listed principles + the links among them. Their unlisted prerequisites may be shown greyed.

Distribution reached: 610 items; 1 principle 89 items, 2: 226, 3: 167, 4: 89, 5: 28, 6: 11.

## 7. The node set

131 principles are used by the items. Ids are `AREA.TOPIC.slug`. Number = items using it. `←` = requires.

Area order: POC, ALG, VZT, DAT, KON, GEO, ZAK.

### POC Počítání s čísly
**POC.VYR Čísla a číselné výrazy**
- `poradi` Pořadí operací a závorky (23)
- `zaporna` Počítání se zápornými čísly (51)
- `desetinna` Počítání s desetinnými čísly (24)
- `mocnina` Druhá mocnina čísla (13)
- `odmocnina` Druhá odmocnina (21) ← mocnina
- `zaokrouhleni` Zaokrouhlení na daný řád (5) ← desetinna
- `osa` Číselná osa se stejnými dílky (4)
- `slovy` Výraz zadaný slovy (5) ← poradi
- S: `absolutni`, `periodicke`, `odhady`

**POC.DEL Dělitelnost** (before ZLOM, because fractions need it)
- `delitele` Dělitelé a násobky čísla (4)
- `prvocisla` Prvočísla a rozklad na prvočísla (4) ← delitele
- `zbytek` Dělení se zbytkem (9)
- `nasobek` Společný násobek a dělitel (2) ← delitele
- S: `znaky`

**POC.ZLOM Zlomky**
- `kraceni` Krácení, rozšiřování, základní tvar (39) ← POC.DEL.delitele
- `scitani` Sčítání a odčítání: společný jmenovatel (50) ← kraceni, POC.DEL.nasobek
- `nasobeni` Násobení a dělení zlomků (55) ← kraceni
- `slozeny` Složený zlomek (19) ← nasobeni, POC.VYR.poradi
- `desetinna` Převod desetinného čísla na zlomek a zpět (4) ← kraceni, POC.VYR.desetinna
- `mocnina` Mocnina a odmocnina zlomku (9) ← nasobeni, POC.VYR.odmocnina
- `smisene` Smíšené číslo (1) ← scitani
- S: `porovnani`

**POC.JED Jednotky**
- `delka` (17) ← POC.VYR.desetinna · `obsah` (2) ← delka · `objem` Objem a litry (4) ← delka · `hmotnost` (3) ← POC.VYR.desetinna · `cas` (8) · `uhel` Stupně a minuty (1)

### ALG Výrazy a rovnice
**ALG.VYR Výrazy**
- `hodnota` Dosazení čísla do výrazu (1) ← POC.VYR.poradi, POC.VYR.mocnina
- `scitani` Sloučení členů, minus před závorkou (44) ← POC.VYR.zaporna
- `nasobeni` Násobení jednočlenů a mnohočlenů (roznásobení závorek) (71) ← scitani
- `umocneni` Vzorec (a ± b)² (19) ← nasobeni
- `vytykani` Vytýkání (10) ← nasobeni
- `rozdil` Rozklad a² − b² na součin (10) ← nasobeni, POC.VYR.mocnina
- `rozklad` Rozklad trojčlenu podle (a ± b)², doplnění (2) ← umocneni

**ALG.ROV Rovnice**
- `upravy` Ekvivalentní úpravy rovnice (57) ← ALG.VYR.scitani
- `zlomky` Odstranění zlomků z rovnice (30) ← upravy, POC.DEL.nasobek, ALG.VYR.nasobeni
- `pocet-reseni` Rovnice bez řešení a s nekonečně mnoha řešeními (2) ← upravy
- `soustava` Soustava dvou rovnic (6) ← upravy

### VZT Vztahy mezi veličinami
**VZT.CAST Zlomek jako část celku**
- `cast` Zlomek z čísla (14) ← POC.ZLOM.nasobeni
- `podil` Jakou částí celku je (3) ← POC.ZLOM.kraceni
- `zbytek` Zbytek celku a část ze zbytku (26) ← cast, POC.ZLOM.scitani
- `zlomek-ze-zlomku` (4) ← cast
- `celek` Celek z části (15) ← cast

**VZT.NEZ Srovnání**
- `okolik-kolikrat` „o kolik" je rozdíl, „kolikrát" je podíl (22)
- `o-zlomek` „o třetinu více / méně než" jako násobení (30) ← VZT.CAST.cast
- `obraceni` Obrácení vztahu: neznámá je za „než" (11) ← okolik-kolikrat, o-zlomek

**VZT.PROC Procenta**
- `cast` Procentová část (12) ← POC.VYR.desetinna
- `pocet` Počet procent (11) ← cast
- `zaklad` Základ z procentové části (15) ← cast
- `prevody` Procento, zlomek a poměr: převody (10) ← cast, POC.ZLOM.kraceni
- `nasobitel` „o x % více / méně" jako násobitel (21) ← cast
- `zaklad-po-zmene` Základ po změně (9) ← nasobitel, zaklad
- `o-kolik-procent` O kolik procent se liší dvě veličiny (17) ← pocet, VZT.NEZ.okolik-kolikrat
- `postupne` Dvě změny po sobě (4) ← nasobitel
- `urok` Úrok a daň z úroku (2) ← cast
- S: `promile`, `finance-pojmy`

**VZT.POM Poměr a úměrnost**
- `pomer` Poměr: zápis, krácení (6) ← POC.ZLOM.kraceni
- `deleni` Díly poměru: z celku, části nebo rozdílu (11) ← pomer
- `meritko` Měřítko mapy a plánu (6) ← pomer, POC.JED.delka
- `obsah-meritko` Měřítko a obsah: druhá mocnina (1) ← meritko, POC.JED.obsah
- `prima` Přímá úměrnost (16) ← VZT.NEZ.okolik-kolikrat
- `neprima` Nepřímá úměrnost (10) ← prima
- `prace` Společná práce: sčítají se výkony (3) ← prima, POC.ZLOM.scitani
- `pohyb` Pohyb: s = v · t (3) ← prima, POC.JED.cas
- `smesi` Směsi a průměrná cena (2) ← prima
- S: `postupny`, `graf`

**VZT.SLOV Slovní úlohy**
- `usudek` Rozbor textu: řetěz jednoduchých výpočtů (9)
- `vyraz` Vyjádření veličiny výrazem s proměnnou (31)
- `rovnice` Sestavení rovnice ze zadání (47) ← vyraz, ALG.ROV.upravy
- `dve-nezname` Dvě neznámé: dvě podmínky, součet a rozdíl (12) ← rovnice
- `cela-cisla` Podmínka celého čísla (5) ← POC.DEL.delitele

### DAT Grafy, tabulky, průměr
**DAT.GRAF**
- `cteni` Čtení hodnot z grafu nebo diagramu (32)
- `tabulka` Třídění údajů do tabulky (2)
- `kruhovy` Kruhový diagram: části jako procenta a úhly (12) ← cteni, VZT.PROC.cast
- `dilek` Graf bez stupnice: hodnota dílku z podmínky (2) ← cteni, VZT.POM.prima
- `chybejici` Dopočet chybějícího údaje ze vztahu mezi údaji (12) ← cteni
- S: `statistika`, `volba`, `souradnice` (moved here from VZT.POM)

**DAT.PRUM**
- `vypocet` Aritmetický průměr (4) · `cetnosti` Průměr z četností (4) ← vypocet · `zpetne` Součet z průměru, chybějící hodnota (5) ← vypocet

### KON Geometrie: útvary a konstrukce
**KON.ZAKL Základní pojmy a konstrukce**
- `kolmice` Kolmice daným bodem (18)
- `rovnobezka` Rovnoběžka daným bodem (7)
- `osa-usecky` Střed a osa úsečky (13) ← kolmice
- `kruznice` Kružnice: body v dané vzdálenosti, přenesení délky (22)
- `uhel` Úhel dané velikosti (3)
- `stredova` Středová souměrnost (16) ← kruznice
- `osova` Osová souměrnost, samodružný bod (8) ← kolmice
- S: `prenos-uhlu`, `opsana`, `tecna`, `obraz-utvaru`

**KON.VLAST Vlastnosti útvarů**
- `rovnoramenny` Rovnoramenný a rovnostranný trojúhelník: shodná ramena, úhly při základně, osa (19)
- `thales` Thaletova věta a kružnice (7) ← KON.ZAKL.kruznice
- `vyska` Výška: kolmice z vrcholu na protější stranu, i vně (5) ← KON.ZAKL.kolmice
- `teznice` Těžnice (2) ← KON.ZAKL.osa-usecky
- `nerovnost` Trojúhelníková nerovnost (2)
- `rovnobeznik` Rovnoběžník: úhlopříčky se půlí (4) ← KON.ZAKL.stredova
- `kosoctverec` (2) ← rovnobeznik
- `obdelnik` Obdélník: shodné úhlopříčky, vrcholy na kružnici (8) ← rovnobeznik
- `ctverec` (2) ← obdelnik, kosoctverec
- `lichobeznik` Rovnoramenný a pravoúhlý lichoběžník (5) ← KON.ZAKL.rovnobezka
- `mnohouhelnik` Pravidelný mnohoúhelník (pěti-, šesti-, osmiúhelník) (2) ← rovnoramenny
- `osy` Osy souměrnosti útvaru (5) ← KON.ZAKL.osova
- S: `shodnost`, `podobnost`

**KON.ROZBOR Rozbor konstrukční úlohy**
- `mnoziny` Podmínka jako množina bodů, bod jako průsečík dvou čar (31) ← KON.ZAKL.kruznice, KON.ZAKL.osa-usecky
- `dve-reseni` Všechna řešení (18) ← mnoziny
- S: `sss`

### GEO Geometrie: výpočty
**GEO.UHLY Úhly**
- `vedlejsi` Vedlejší a vrcholové úhly (19)
- `rovnobezky` Souhlasné a střídavé úhly (10) ← vedlejsi
- `trojuhelnik` Součet úhlů v trojúhelníku (21)
- `osa` Osa úhlu (4)

**GEO.PYT Pythagorova věta**
- `veta` (17) ← POC.VYR.odmocnina · `najit` Nalezení pravoúhlého trojúhelníku v útvaru nebo tělese (9) ← veta

**GEO.ROV Obvod a obsah**
- `obvod` Obvod mnohoúhelníku (18)
- `obdelnik` Obsah čtverce a obdélníku (4)
- `trojuhelnik` Obsah trojúhelníku (13) ← obdelnik, KON.VLAST.vyska
- `rovnobeznik` Obsah rovnoběžníku a kosočtverce (1) ← obdelnik, KON.VLAST.vyska
- `lichobeznik` Obsah lichoběžníku (6) ← trojuhelnik
- `zpetne` Rozměr z obsahu nebo obvodu (vzorec obráceně, i u kruhu) (17) ← obdelnik, obvod
- `slozene` Skládání a rozklad útvarů (13) ← obdelnik, obvod
- `rozestupy` Rozestupy po obvodu (2) ← obvod
- S: `sit`

**GEO.KRUH Kruh**
- `obvod` (5) ← POC.VYR.desetinna · `obsah` (5) ← POC.VYR.desetinna, POC.VYR.mocnina · `casti` Půlkruh, čtvrtkruh, výseč (7) ← obvod, obsah
- S: `tecna`, `dve-kruznice`

**GEO.TEL Tělesa**
- `hrany` Hrany a stěny hranolu (3)
- `kvadr-objem` (7) ← GEO.ROV.obdelnik · `kvadr-povrch` (9) ← GEO.ROV.obdelnik
- `hranol-objem` (6) ← kvadr-objem · `hranol-povrch` (4) ← kvadr-povrch
- `valec-objem` (6) ← hranol-objem, GEO.KRUH.obsah · `valec-povrch` Plášť a povrch válce (3) ← hranol-povrch, GEO.KRUH.obvod
- `zpetne` Hrana nebo výška z objemu či povrchu (6) ← kvadr-objem, kvadr-povrch
- `sit` Síť tělesa (3) ← kvadr-povrch
- `slepena` Slepená a rozříznutá tělesa, řez (14) ← kvadr-povrch, kvadr-objem
- `krychlicky` Tělesa z krychliček (4)
- S: `pohledy`, `nacrt`, `jehlan`, `koule`

### ZAK Zákonitosti a úsudek
**ZAK.RADA**
- `tabulka` Pokračování pravidla po krocích (11)
- `nty-clen` Obecné pravidlo, n-tý člen (25) ← tabulka, VZT.SLOV.vyraz
- `obraceni` Obrácení pravidla (13) ← nty-clen
- `nasobenim` Růst násobením (4) ← tabulka
- `cisla` Číselná řada daná pravidlem (6) ← tabulka

**ZAK.USUDEK**
- `periody` Periodické děje (8) ← POC.DEL.zbytek
- `vsechna` Systematické vypsání možností (6)

### Changes against the old tree
- Split: zlomky `operace` → kraceni, scitani, nasobeni; `poradi` → poradi, zaporna; `mocniny` → mocnina, odmocnina; procenta `tri-vypocty` → cast, pocet, zaklad; `vzorce` → obvod, obdelnik, trojuhelnik, rovnobeznik, lichobeznik; `krychle-kvadr`, `hranol`, `valec` → objem and povrch each; `pomer` → pomer, deleni; `roznasobeni` → scitani, nasobeni; `dvojice` → vedlejsi, rovnobezky.
- New: ALG.ROV.upravy, VZT.CAST.podil, VZT.POM.obsah-meritko, DAT.GRAF.dilek, GEO.TEL.hrany, GEO.TEL.zpetne, KON.ZAKL.rovnobezka, KON.VLAST.teznice.
- Merged: twin GEO/KON nodes (rovnoramenný, Thales, osa úhlu, mnohoúhelník, výška); rovnostranný into rovnoramenný; bez-reseni + nekonecne; nasobek + nsn-nsd; cas + sekunda-tyden; krat-mene into okolik-kolikrat; PYT.telesa into najit; KRUH.zpetne into ROV.zpetne.
- Dissolved (expressed by other principles): ALG.ROV.zavorky, ALG.ROV.mocniny, VZT.PROC.obracene, ze-zbytku, se-souctem, body, VZT.POM.usecka, GEO.UHLY.s-promennou, GEO.ROV.s-promennou, dvojim, GEO.ROV.lichobeznik (strategy), GEO.KRUH.oblouky, GEO.TEL.vztah, litry, KON.VLAST.pravouhly, ZAK.USUDEK.strategie, POC.ZLOM.prevraceny.
- KON.SOUM topic removed (`osy` → KON.VLAST, `obraz-utvaru` → KON.ZAKL, `samodruzny` → note of osova).

The links above are a first proposal made while solving; review them once against the solutions before fixing them (does any item use B without A?).

## 8. How the solving was done, and its limits

- Each task was read from its image in `backend/data/screenshots/`, solved, and the result compared with the text of the official key (`info.py`). All 610 results agree with the keys.
- Two key results lost their minus sign in text extraction; computed values are used: 2024 C 3.2 = −16/5, 2024 D 3.2 = −1/30. Confirm against the key image.
- Not worked out independently, answer taken from the key: 2022 D 11.1–11.3 and 2023 D 8.1 (symmetry in a grid; 8.2 was checked), 2025 B 13 (which diagonals), 2026 B 13 (corner cut-outs), 2025 A 11.3.
- Construction tasks: the construction was derived from the wording and figure and compared with the points named in the key, not drawn.
- The assignment is still one solver's judgement.
- The three older tests (2019 A, 2021 A, 2021 B in `References/Matematika_starsi/`) were **not** re-solved. `m9_item_skills_older.json` uses old ids.

## 9. Remaining work, in order

1. **Tree file.** Write the new `analysis/data/m9_topic_tree.json` from section 7 (fields per node as the editor demands: id, name, kind, requires, tags, spec, note). Notes in Czech: one or two sentences stating the principle and its typical error; no counts or success rates. Specification-only nodes: take name, spec and the specification quote from `before_rebuild/m9_topic_tree.json`.
2. **Assignment file.** `m9_item_skills.json` = the `principy` lists of `m9_item_solutions.json`. Keep the solutions file as the source; extend `analysis/topic_tree.py` so `assign` keeps both in step and `check` validates the solutions file too. All writes go through the editor's validation (`problems()`), then `build`.
3. **Older tests.** Re-solve the three older tests the same way (render pages from the PDFs; no keys are in the repository) and rewrite `m9_item_skills_older.json`.
4. **Review the links** (end of section 7), then run `topic_tree.py check` and `build`.
5. **Backend.** Rebuild the database (`try_problem_db.py build`), run the tests; fix tests that name old ids. The API must give, per problem and item, the principles, the links among them and the solution line.
6. **Problem database page.** Each task shows its subgraph: principles as boxes with the links among them, main one marked, per item; the solution line under each item; every box links to the tree. A graph component used by both pages belongs in `frontend/src/shared/`.
7. **Graph view** (section 11).
8. **Docs.** Update `CLAUDE.md` (analysis and tree paragraphs), regenerate `04_strom_M9.md/.html`; delete `analysis/data/before_rebuild/` once the owner agrees.

## 10. Deliberately left out

- Levels within a principle ("how well").
- Roles or weights on the item–principle link beyond "main first".
- Stable ids independent of position. Do this before any student data is stored.
- Diagnostic items that test one principle alone.

## 11. Graph view

Current state (seen 2 October): the graph of 162 skills is drawn on a canvas of about 1 400 × 2 600 px inside a pane about 420 px wide, so only a few boxes are visible at once; long curved links cross many columns; names are cut; the selected skill may be off-screen; the search only greys boxes out.

Requirements for the redesign (show the owner a mockup first, as `CLAUDE.md` demands):
- Searching must take you to the node: typing a name lists matches, choosing one centres and selects it.
- A focused mode as the default reading: the selected principle with everything it requires on the left and everything built on it on the right, nothing else.
- An overview that fits the screen: grouped by area and topic, groups collapsible, specification-only nodes hidden unless asked for.
- A task can be shown in the graph: its subgraph highlighted (`/strom?view=graf&problem=M9-2025-B-15`).
- Full names readable (wrap or tooltip), fewer and shorter links (direct links only), zoom and pan.
- Keep the house style: plain, dense, one accent colour, no animation.
