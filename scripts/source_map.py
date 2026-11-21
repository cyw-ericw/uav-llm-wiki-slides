"""Build the reader-facing forward and reverse index from the evidence cards."""
from pathlib import Path
from check_slides import ROOT, read
sources={s['id']:s for s in read(ROOT/'raw/source_cards.json')['sources']}
cards=[read(p) for p in sorted((ROOT/'slides/cards').glob('*.json'))]
lines=['# Wiki 與投影片來源對照','',
       '從頁碼查主張，或從文件反查用途。S02.3 表示 S02 來源卡的第 3 條中文摘錄。原頁段落以標題定位，便於查核會更新的線上文件。','',
       '## 由官方文件找投影片','','| 來源卡／官方原文 | 本次逐項讀取位置 | 涵蓋頁 | 對讀筆記 |','|---|---|---|---|']
for sid,s in sources.items():
    pages=[c['page'] for c in cards if any(f.startswith(sid+'.') for cl in c['claims'] for f in cl['facts'])]
    links='、'.join(f'[{p}](#p{p})' for p in pages)
    v=s['verification']
    lines.append(f"| [{sid}](../wiki/sources/{sid}.md) · [{s['title']}]({s['url']}) | {v['location']} | {links} | {v['decision']} |")
lines+=['','## 由投影片查證據','',
        '每頁下表依畫面段落排序。「適用範圍」也是 HTML 本頁證據面板的內容。自我檢核的引用依據另列在表後。']
for c in cards:
    n=c['page']
    d=read(ROOT/f'slides/drafts/{n}.json')
    lines += ['',f'<a id="p{n}"></a>',f"### {n}　{d['title']}",'',
              f'[投影片](deck.html#p{n}) · [證據卡](cards/{n}.json) · [逐頁稿](drafts/{n}.json)','',
              '| 段落 | 投影片主張 | Wiki 概念 | 來源卡條目 |','|---|---|---|---|']
    for row,cl in zip(d['rows'],c['claims']):
        w=cl['wiki']
        facts='、'.join(f'[{f}](../wiki/sources/{f.split(".")[0]}.md)' for f in cl['facts'])
        lines.append(f"| {cl['id']} | {row['text']} | [{w}](../wiki/concepts/{w}.md) | {facts} |")
    lines+=['','自我檢核依據為 '+ '、'.join(d['answer_evidence'])+'。','',f"適用範圍：{c['limit']}"]
lines.extend(['', '## V3 代表頁的讀圖依據', '', '第 03 頁將 03a／03b 的 S01、S02 區分為板載與外接介面。版本條件由 03c 保留。', '第 06 頁的矩陣合併 06a–06c 與既有 07c、08a、08c、09a；見[九個比較格的逐格對應](../checks/v3/figure-review.md)。', '第 10 頁完整訊息及其原因對應 10b／S07.4，同頁的安全處理順序對應 10a–10c。'])
lines.extend(['','## V3 全套圖解','',
              '逐頁圖解、條件與對應條目見[完整技術審查](../checks/final/faithfulness.md)。',
              '第 05 頁的垂直位置與航向見 S08.4，光流的水平速度與相對位置見 S08.3。',
              '第 07–09 頁依序對應 S04.1–2、S05.1 與 S05.3、S03.2 與 S06.1–3。第 09 頁的光流限制另見 S08.3。'])
(ROOT/'slides/sources.md').write_text('\n'.join(lines)+'\n')
