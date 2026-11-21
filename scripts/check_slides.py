"""Check traceability before drafting or rendering. Run from any directory."""
import argparse
import json
import re
from pathlib import Path
from urllib.parse import urlsplit
ROOT = Path(__file__).resolve().parents[1]

def read(path):
    return json.loads(path.read_text())

def check(draft=False):
    raw = read(ROOT/'raw/source_cards.json')['sources']
    sources = {s['id']: s for s in raw}
    outline = (ROOT/'slides/outline.md').read_text()
    pages = re.findall(r'^\| (\d{2}) \| ([^|]+?) \| [^|]+ \| ([^|]+?) \|', outline, re.M)
    errors, summary, used, concepts = [], [], set(), set()
    expected = [f'{i:02}' for i in range(1,12)]
    folders = ['cards','drafts'] if draft else ['cards']
    for folder in folders:
        if sorted(p.stem for p in (ROOT/'slides'/folder).glob('*.json')) != expected:
            errors.append(f'{folder}: page inventory')
    if [p[0] for p in pages] != expected or '已人工核准' not in outline:
        errors.append('approved outline')
    for number, title, planned in pages:
        card = read(ROOT/f'slides/cards/{number}.json')
        if not (card['page']==number and card['title']==title and card['limit'] and card['claims']):
            errors.append(f'{number}: card metadata')
        claims = {c['id']:c for c in card['claims']}
        refs = set()
        for c in claims.values():
            w = c['wiki']
            concepts.add(w)
            wiki = (ROOT/f'wiki/concepts/{w}.md').read_text()
            if not c['facts'] or not c['claim']:
                errors.append(c['id']+' empty')
            for ref in c['facts']:
                sid, index = ref.split('.')
                source = sources[sid]
                fact = source['facts'][int(index)-1]
                note = (ROOT/f'wiki/sources/{sid}.md').read_text()
                if not (int(index)>0 and all(x in note for x in fact) and
                        f'[[{sid}]]' in wiki and source['verification']['location'] and
                        urlsplit(source['url']).hostname in {'ardupilot.org','docs.holybro.com'}):
                    errors.append(f'{number}: {ref} via {w}')
                refs.add(sid)
        if not set(planned.split(',')) <= refs:
            errors.append(number+' outline sources')
        used.update(refs)
        if draft:
            d=read(ROOT/f'slides/drafts/{number}.json')
            keys=[k for row in d['rows'] for k in row['evidence']]
            keys+=d['answer_evidence']
            if set(keys)!=set(claims) or d['title']!=title or d['page']!=number:
                errors.append(number+' draft mapping')
            if any(not row['evidence'] or not row['text'] for row in d['rows']):
                errors.append(number+' empty draft row')
        summary.append(dict(page=number,claims=len(claims),sources=sorted(refs)))
    if used!=set(sources) or len(set(s['url'] for s in raw))!=len(sources) or len(used)<5:
        errors.append('source coverage')
    if concepts!={p.stem for p in (ROOT/'wiki/concepts').glob('*.md')}:
        errors.append('wiki concept coverage')
    result=dict(status='FAIL' if errors else 'PASS',checked='draft+cards' if draft else 'cards',
                pages=summary,source_ids=sorted(used),concepts=sorted(concepts),errors=errors)
    output=ROOT/'checks'/('draft-coverage.json' if draft else 'card-coverage.json')
    output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(result['status'],len(summary),'pages;',sum(p['claims'] for p in summary),'evidence claims;',len(used),'sources;',len(concepts),'concepts',errors)
    return not errors
if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--draft',action='store_true')
    raise SystemExit(0 if check(parser.parse_args().draft) else 1)
