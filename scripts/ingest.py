#!/usr/bin/env python3
"""從已查核官方頁面整理的 raw/source_cards.json 建立來源 Wiki。
不下載或複製官方網頁全文；來源摘要須由人工查核網站後維護。
"""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import json, re
ROOT=Path(__file__).resolve().parents[1]
source_file=ROOT/'raw/source_cards.json'
raw=json.loads(source_file.read_text(encoding='utf-8'))
sources=raw['sources']
if len(sources)<5:raise SystemExit('FAIL: 少於五篇來源')
ids=[s['id'] for s in sources]
if len(set(ids))!=len(ids):raise SystemExit('FAIL: 來源 ID 重複')
for s in sources:
 for k in ('id','slug','publisher','title','url','facts'):
  if not s.get(k): raise SystemExit(f"FAIL: {s.get('id')} 缺少 {k}")
 if not s['url'].startswith('https://'):raise SystemExit(f"FAIL: {s['id']} URL 不安全")
 if not s['facts']:raise SystemExit(f"FAIL: {s['id']} 無來源摘錄")
 out=ROOT/'wiki/sources'/f"{s['id']}.md"
 lines=[f"# {s['id']}｜{s['title']}","",f"- 出版者：{s['publisher']}",f"- 官方來源：{s['url']}",f"- 原始資料形式：官方文件重點摘錄（非全文）",f"- 查核日期：{raw['access_date']}","", "## 已整理的來源重點"]
 for idx,(section,fact) in enumerate(s['facts'],1):lines.append(f"{idx}. **{section}：** {fact}")
 lines.extend(['','## 原頁對讀',s['verification']['location'],s['verification']['decision'],'','## 相關主題','、'.join(s['focus']),'','## 注意','已保存來源連結及中文摘要；如涉及特定參數、版本或實機行為，應回原始來源逐條核對。'])
 out.write_text('\n'.join(lines)+'\n',encoding='utf-8')
concept_files=sorted((ROOT/'wiki/concepts').glob('*.md'))
idx=['# UAV LLM Wiki｜首頁索引','','## 概念筆記（供 AI 查詢）']
for p in concept_files:
 name=p.read_text(encoding='utf-8').splitlines()[0].lstrip('# ').strip()
 idx.append(f'- [[{p.stem}]]：{name}')
idx+=['','## 官方來源卡（已 ingest 的來源摘錄）']
for s in sources:idx.append(f"- [[{s['id']}]]：{s['publisher']} — {s['title']}（[原始文件]({s['url']})）")
idx+=['','## 說明','來源卡記錄已開啟之官方頁面、段落與中文摘要，而不是原文全文；需要驗證細節請回官方網址。','此 Wiki 的 ingest 紀錄請見 [[log]]。']
(ROOT/'wiki/index.md').write_text('\n'.join(idx)+'\n',encoding='utf-8')
now=datetime.now(ZoneInfo('Asia/Taipei')).isoformat(timespec='seconds')
summary={"status":"PASS","generated_at_taipei":now,"source_count":len(sources),"source_ids":ids,"source_origin":"verified_official_document_summaries_not_full_text","concept_pages_count":len(concept_files),"output_source_cards":[f"wiki/sources/{x}.md" for x in ids],"note":"PASS 僅表示來源卡生成成功；不等於 HTML 簡報已完成或內容經獨立審查。"}
(ROOT/'checks/ingest_report.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
log=ROOT/'wiki/log.md'
entry=(f"\n## {now}｜第二階段重新匯入\n\n"
       f"讀取已對照原頁的 raw/source_cards.json，產生 {len(ids)} 張來源卡與索引。"
       "本指令只處理本機資料；原頁閱讀日期與查閱段落見每張來源卡的「原頁對讀」。"
       " 結構檢查與內容審查另見 checks/ 與 slides/report.md。\n")
with log.open('a',encoding='utf-8') as output:
 output.write(entry)
print(f'INGEST OK: {len(ids)} source cards, {len(concept_files)} concept pages')
