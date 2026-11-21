"""Compare rendered content and links with the approved draft and evidence."""
import hashlib
import json
import re
from collections import Counter
from urllib.parse import urlsplit
from lxml import html
from check_slides import ROOT,read
from render import revision

path=ROOT/'slides/deck.html'
doc=html.fromstring(path.read_bytes().decode('utf-8'))
sources={s['id']:s for s in read(ROOT/'raw/source_cards.json')['sources']}
errors=[]
def verify(actual,expected,where):
    if actual!=expected:
        errors.append(where)
frames=doc.xpath('//section[@data-chapter]')
verify(len(frames),11,'page count')
verify(revision(),read(ROOT/'checks/render-approval.json')['reviewed_sha256'],'content revision')
verify(len(set(e.get('id') for e in doc.xpath('//*[@id]'))),len(doc.xpath('//*[@id]')),'unique IDs')
verify([a.get('href') for a in doc.xpath('//nav[@class="contents"]/a')],['#'+s.get('id') for s in frames],'index links')
external=Counter()
for frame in frames:
    n=frame.get('id')[1:]
    d=read(ROOT/f'slides/drafts/{n}.json')
    c=read(ROOT/f'slides/cards/{n}.json')
    for selector,expected in [('./h1',d['title']),('./p[@class="lead"]',d['lead']),('.//details[@class="practice"]/p',d['answer']),
                              ('.//details[@class="practice"]/summary','自我檢核'+d['question']),('.//details[@class="refs"]/p','適用範圍｜'+c['limit'])]:
        verify(frame.xpath(selector)[0].text_content(),expected,n+' '+selector)
    for selector,key in [('.//div[@class="row"]/h2','label'),('.//div[@class="row"]/p','text')]:
        verify([e.text_content() for e in frame.xpath(selector)],[r[key] for r in d['rows']],n+' '+key)
    refs=frame.xpath('.//details[@class="refs"]//li')
    verify(len(refs),len(c['claims']),n+' claims')
    for li,claim in zip(refs,c['claims']):
        verify(li.text_content().startswith(claim['claim']),True,claim['id'])
        expected=[(sources[f.split('.')[0]]['url'],f) for f in claim['facts']]
        actual=[(a.get('href'),a.text_content().split(' · ')[0]) for a in li.xpath('.//a')]
        verify(actual,expected,claim['id']+' links')
        external.update(u for u,f in actual)
view=ROOT/'slides/sources.md'
md=view.read_text()
markdown_links=re.findall(r'\[[^\]]+\]\(([^)]+)\)',md)
for link in markdown_links:
    url=urlsplit(link)
    if url.scheme:
        verify(link in external,True,'unregistered '+link)
        continue
    dest=(view.parent/url.path) if url.path else view
    verify(dest.is_file(),True,'missing '+link)
    if url.fragment:
        target=doc.xpath('//*[@id=$id]',id=url.fragment) if dest.suffix=='.html' else f'id="{url.fragment}"' in dest.read_text()
        verify(bool(target),True,'fragment '+link)
verify(set(external),{s['url'] for s in sources.values()},'all original documents')
verify(len(doc.xpath('//script[@src or @type="module"] | //link[@rel="stylesheet"] | //img[@src] | //iframe')),0,'offline asset dependencies')
result=dict(status='FAIL' if errors else 'PASS',sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
            slides=len(frames),bodies=len(doc.xpath('//div[@class="row"]/p')),questions=len(doc.xpath('//details[@class="practice"]')),
            official_link_occurrences=sum(external.values()),unique_official_urls=len(external),source_map_links=len(markdown_links),
            external_verification='Canonical URL compared to the documents actually opened during source review; no live HTTP status probe in this script.',errors=errors)
(ROOT/'checks/render.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(result)
raise SystemExit(bool(errors))
