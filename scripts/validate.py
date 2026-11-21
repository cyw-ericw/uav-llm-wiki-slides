#!/usr/bin/env python3
"""可執行的結構驗證；不冒稱已執行獨立技術審查或 HTML 檢查。"""
from pathlib import Path
import json, re
from datetime import datetime
from zoneinfo import ZoneInfo
ROOT=Path(__file__).resolve().parents[1]
raw=json.loads((ROOT/'raw/source_cards.json').read_text(encoding='utf-8'))
sources=raw.get('sources',[])
checks={}
checks['at_least_five_sources']=len(sources)>=5
ids=[s.get('id') for s in sources]
checks['unique_source_ids']=len(ids)==len(set(ids))
checks['official_source_urls']=all(s.get('url','').startswith('https://') and any(x in s.get('url','') for x in ['docs.holybro.com/','ardupilot.org/']) for s in sources)
checks['source_facts_and_sections']=all(len(s.get('facts',[]))>=2 and all(len(f)==2 and f[0] and f[1] for f in s['facts']) for s in sources)
checks['generated_source_files']=all((ROOT/f'wiki/sources/{i}.md').is_file() for i in ids)
checks['wiki_index']= (ROOT/'wiki/index.md').is_file() and all(f'[[{i}]]' in (ROOT/'wiki/index.md').read_text(encoding='utf-8') for i in ids)
concept_files=list((ROOT/'wiki/concepts').glob('*.md'))
missing=[]
for p in concept_files:
 for link in re.findall(r'\[\[([^]#|]+)',p.read_text(encoding='utf-8')):
  if not ((ROOT/'wiki/concepts'/f'{link}.md').exists() or (ROOT/'wiki/sources'/f'{link}.md').exists() or link=='log'):
   missing.append([p.name,link])
checks['concept_wiki_links_resolve']=not missing
checks['concept_pages_at_least_five']=len(concept_files)>=5
outline=ROOT/'slides/outline.md'
outline_text=outline.read_text(encoding='utf-8')
checks['approved_eleven_page_outline']=('已人工核准' in outline_text and
    re.findall(r'^\| (\d{2}) \|', outline_text, re.M)==[f'{i:02}' for i in range(1,12)])
now=datetime.now(ZoneInfo('Asia/Taipei')).isoformat(timespec='seconds')
result={'checked_at_taipei':now,'status':'PASS' if all(checks.values()) else 'FAIL','source_count':len(sources),'concept_count':len(concept_files),'checks':checks,'unresolved_concept_links':missing,'limitations':['只檢查來源卡生成與 Wiki 結構','獨立忠實度與 HTML 測試結果另見 slides/report.md']}
(ROOT/'checks/validation_report.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for k,v in checks.items(): print(('PASS' if v else 'FAIL')+' '+k)
print('RESULT:',result['status'])
raise SystemExit(0 if result['status']=='PASS' else 1)
