"""Render the independently reviewed JSON drafts as one offline HTML file."""
import hashlib
import json
from html import escape as esc
from pathlib import Path
from check_slides import ROOT, read, check
from course_graphics import course_body
from batch_one import LAYOUTS, teaching_body

def revision():
    h=hashlib.sha256()
    files=[ROOT/'raw/source_cards.json',ROOT/'slides/outline.md']
    for folder in ('wiki/concepts','wiki/sources','slides/cards','slides/drafts'):
        files.extend(sorted(p for p in (ROOT/folder).iterdir() if not p.name.startswith('.')))
    for p in files:
        h.update(p.relative_to(ROOT).as_posix().encode()+b'\0'+p.read_bytes()+b'\0')
    return h.hexdigest()

def render():
    if not check(True):
        raise SystemExit('Draft coverage failed')
    gate=read(ROOT/'checks/render-approval.json')
    if gate.get('status')!='PASS' or gate.get('reviewed_sha256')!=revision():
        raise SystemExit('Review current Wiki, cards and drafts before rendering')
    sources={s['id']:s for s in read(ROOT/'raw/source_cards.json')['sources']}
    frames, links, options=[],[],[]
    for path in sorted((ROOT/'slides/drafts').glob('*.json')):
        d=read(path)
        n=d['page']
        c=read(ROOT/f'slides/cards/{n}.json')
        title=esc(d['title'])
        chapter=('課程導讀' if n=='01' else '飛控與感測' if n<='05' else '飛行模式' if n<='09' else '安全與回顧')
        rows=''.join('<div class="row"><h2>'+esc(r['label'])+'</h2><p>'+esc(r['text'])+'</p></div>' for r in d['rows'])
        refs=[]
        for claim in c['claims']:
            citations=[]
            for ref in claim['facts']:
                sid,idx=ref.split('.')
                s=sources[sid]
                section=s['facts'][int(idx)-1][0]
                citations.append(f'<a rel="noopener" target="_blank" href="{esc(s["url"])}">{ref} · {esc(section)}</a>')
            refs.append('<li>'+esc(claim['claim'])+'　'+'、'.join(citations)+'</li>')
        src_ids=sorted({f.split('.')[0] for cl in c['claims'] for f in cl['facts']})
        refs_html=''.join(refs)
        diagram_refs=''
        if n=='06':
            diagram_refs=('<p class="diagram-refs">讀圖依據｜姿態與水平桿見 S03 模式表、S04.1、S06.2。'
                          '高度見 S04.1、S05.3、S06.1。水平位置見 S04.2、S05.1、S03.2、S06.1。'
                          '可對讀第 07–09 頁的本頁證據。</p>')
        kind=' v3'
        body=teaching_body(n,rows) if n in LAYOUTS else course_body(n,rows)
        hidden='' if n=='01' else ' hidden'
        frames.append(f'''<section class="frame{kind}" id="p{n}" data-chapter="{chapter}" aria-labelledby="t{n}"{hidden}>
<h1 id="t{n}" tabindex="-1">{title}</h1><p class="lead">{esc(d['lead'])}</p>{body}
<details class="practice"><summary><span class="hint">自我檢核</span>{esc(d['question'])}</summary><p>{esc(d['answer'])}</p></details>
<details class="refs"><summary>本頁證據　{' · '.join(src_ids)}</summary><ul>{refs_html}</ul><p>適用範圍｜{esc(c['limit'])}</p>{diagram_refs}</details></section>''')
        links.append(f'<a href="#p{n}"><span class="num">{n}</span><span>{title}</span></a>')
        options.append(f'<option value="p{n}">{n}　{title}</option>')
    html=(ROOT/'scripts/deck-template.html').read_text()
    html=html.replace('@@V3CSS@@','\n'.join((ROOT/'scripts'/name).read_text() for name in ('batch-one.css','course.css')))
    for slot,items in [('SLIDES',frames),('INDEX',links),('OPTIONS',options)]:
        html=html.replace(f'@@{slot}@@','\n'.join(items))
    (ROOT/'slides/deck.html').write_text(html)
    print('Rendered',len(frames),'slides')
if __name__=='__main__':
    render()
