"""Turns the raw solving notes (raw/YYYY_T.json, working ids) into analysis/data/m9_item_solutions.json (final ids).

    uv run --project backend python analysis/solving/consolidate.py

raw/YYYY_T.json:  {"item": ["solution in Czech", ["principle id", ...main first]]}
output:           {"2022 A": {"4.1": {"reseni": "...", "principy": ["ALG.VYR.vytykani", ...]}}}

The mapping below is the consolidation decided on 2 October 2026 (see analysis/graph_design_spec.md, section 7).
"""
import glob, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, ROOT)
from backend.core.catalog import load_catalog  # noqa: E402
from backend.core.topic_tree import catalog_items  # noqa: E402

DROP = None
MAPPING = {
    'DAT.GRAF.sloupcovy': 'DAT.GRAF.cteni',
    'GEO.UHLY.rovnoramenny': 'KON.VLAST.rovnoramenny',
    'GEO.UHLY.kruznice': 'KON.VLAST.rovnoramenny',
    'KON.VLAST.rovnostranny': 'KON.VLAST.rovnoramenny',
    'GEO.UHLY.thales': 'KON.VLAST.thales',
    'KON.ZAKL.thales': 'KON.VLAST.thales',
    'KON.VLAST.pravouhly': DROP,
    'KON.ZAKL.osa-uhlu': 'GEO.UHLY.osa',
    'GEO.UHLY.mnohouhelnik': 'KON.VLAST.mnohouhelnik',
    'KON.VLAST.sestiuhelnik': 'KON.VLAST.mnohouhelnik',
    'GEO.ROV.vyska': 'KON.VLAST.vyska',
    'GEO.PYT.telesa': 'GEO.PYT.najit',
    'GEO.ROV.dvojim': DROP,
    'VZT.PROC.body': DROP,
    'GEO.UHLY.rovnice': 'VZT.SLOV.rovnice',
    'GEO.KRUH.zpetne': 'GEO.ROV.zpetne',
    'GEO.TEL.kvadr-hrany': 'GEO.TEL.hrany',
    'GEO.ROV.nerovnost': 'KON.VLAST.nerovnost',
    'KON.SOUM.osy': 'KON.VLAST.osy',
}


def final_ids(ids):
    out = []
    for i in ids:
        i = MAPPING.get(i, i)
        if i is not DROP and i not in out:
            out.append(i)
    return out


def main():
    expected = catalog_items(load_catalog(os.path.join(ROOT, 'analysis', 'data')))
    result, used = {}, {}
    for path in sorted(glob.glob(os.path.join(HERE, 'raw', '20*_*.json'))):
        test = os.path.basename(path)[:-5].replace('_', ' ')
        with open(path, encoding='utf-8') as f:
            raw = json.load(f)
        result[test] = {}
        for item, (solution, ids) in raw.items():
            assert (test, item) in expected, f'{test} {item}: not an item of the catalog'
            ids = final_ids(ids)
            assert ids, f'{test} {item}: no principle left'
            result[test][item] = {'reseni': solution, 'principy': ids}
            for i in ids:
                used[i] = used.get(i, 0) + 1
    missing = [k for k in expected if k[1] not in result.get(k[0], {})]
    assert not missing, f'items without a solution: {missing[:5]}'
    out = os.path.join(ROOT, 'analysis', 'data', 'm9_item_solutions.json')
    with open(out, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=1)
        f.write('\n')
    print(f'{sum(len(v) for v in result.values())} items of {len(result)} tests, {len(used)} principles -> {out}')
    for i, n in sorted(used.items(), key=lambda kv: (-kv[1], kv[0])):
        print(f'{n:4d}  {i}')


if __name__ == '__main__':
    main()
