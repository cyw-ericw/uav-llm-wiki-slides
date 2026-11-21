"""Offline visual regression smoke checks for design v2 (Playwright + Chromium)."""
import json
from pathlib import Path
from collections import Counter
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]
html=(ROOT/'slides/deck.html').read_text()
widths=[(1440,900),(1024,768),(768,1024),(390,844),(320,568)]
failures=[];nav_y={}; page_checks=0;accordion_checks=0;button_checks=0
with sync_playwright() as pw:
  browser=pw.chromium.launch(executable_path='/usr/bin/chromium', args=['--no-sandbox','--disable-dev-shm-usage','--disable-gpu'])
  for w,h in widths:
    page=browser.new_page(viewport={'width':w,'height':h})
    for i in range(11):
      page.goto('about:blank')
      page.set_content(html,wait_until='load')
      page.evaluate('(i)=>document.querySelectorAll(".contents a")[i].click()',i)
      page.wait_for_function('(id)=>document.querySelector(".frame:not([hidden])")?.id===id',arg=f'p{i+1:02d}')
      data=page.evaluate('''() => ({visible:Array.from(document.querySelectorAll('.frame')).filter(f=>!f.hidden).length,overflow:document.documentElement.scrollWidth-innerWidth,navY:document.querySelector('.nav').getBoundingClientRect().y, navX:document.querySelector('.nav').getBoundingClientRect().x, prevDisabled:document.querySelector('#prev').disabled,nextDisabled:document.querySelector('#next').disabled,active:document.querySelector('.frame:not([hidden])').id})''')
      page_checks+=1
      if data['visible']!=1 or data['overflow']>0 or data['prevDisabled']!=(i==0) or data['nextDisabled']!=(i==10):failures.append({'size':w,'page':i+1,'layout':data})
      nav_y.setdefault(w,[]).append(data['navY'])
      if i in (0,8,10):
        for dsel in ('.practice','.refs'):
          el=page.locator('.frame:not([hidden]) '+dsel)
          el.locator('summary').click();page.wait_for_timeout(30)
          a=el.evaluate('(e)=>e.open'); y=page.locator('.nav').bounding_box()['y']
          accordion_checks+=1
          if not a or abs(y-data['navY'])>.1:failures.append({'size':w,'page':i+1,'accordion':dsel,'open':a,'navShift':y-data['navY']})
          el.locator('summary').click()
      if i<10 and i in (0,8):
        page.locator('#next').click();page.wait_for_function('(id)=>document.querySelector(".frame:not([hidden])")?.id===id',arg=f'p{i+2:02d}')
        button_checks+=1
      if i>0 and i in (9,10):
        page.locator('#prev').click();page.wait_for_function('(id)=>document.querySelector(".frame:not([hidden])")?.id===id',arg=f'p{i:02d}')
        button_checks+=1
    page.close()
  browser.close()
result={'status':'PASS' if not failures else 'FAIL','page_size_tests':page_checks,'sizes':widths,'accordion_open_close_tests':accordion_checks,'paging_button_tests':button_checks,'nav_y_range_by_width':{str(w):round(max(ys)-min(ys),3) for w,ys in nav_y.items()},'failures':failures,'scope':'Chromium in isolated local rendered HTML; Safari and real projector not tested. No HTTP verification of source URLs.'}
(ROOT/'checks/visual-design-v2.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
assert not failures
