# LLM Wiki Ingest Log

- 執行日期：2026-11-21T14:45:08+08:00
- 指令：`python3 scripts/ingest.py`
- 來源：`raw/source_cards.json`，由官網已查閱資訊整理的中文摘錄（非網頁全文）
- 本次完成：8 篇不同的官方資料 → `wiki/sources/Sxx.md`
- 來源 ID：S01, S02, S03, S04, S05, S06, S07, S08
- 概念筆記：5 篇已備妥，見 `wiki/concepts/`
- 結果：來源卡已成功建立。HTML 教學簡報尚未完成。
- 內容忠實度：**仍需後續獨立審查**。即使 Python 驗證通過，也不代表來源無誤。
- 驗證檔案：`checks/ingest_report.json`、`checks/validation_report.json`

## 重現方式
```bash
python3 scripts/ingest.py
python3 scripts/validate.py
```

## 2026-11-21T15:01:58+08:00｜第二階段重新匯入

讀取已對照原頁的 raw/source_cards.json，產生 8 張來源卡與索引。本指令只處理本機資料；原頁閱讀日期與查閱段落見每張來源卡的「原頁對讀」。 結構檢查與內容審查另見 checks/ 與 slides/report.md。

### 本次八份原始文件的核對範圍

第一階段留存的 log 能證實 8 張摘要已匯入；初版沒有提供獨立逐頁回讀的輸出。本階段實際開啟原頁並對照相關段落，再重跑 ingest。原頁查閱證據見每張卡末的「原頁對讀」及 [獨立審查紀錄](../checks/faithfulness-round1.md)。本次保存中文摘錄與段落線索，官網仍是可更新的文件。

| 原頁 | 查閱位置／本次決定 |
|---|---|
| [[S01]] | Overview 首段與設計說明；分開記錄板型和出廠預裝韌體。 |
| [[S02]] | On-board sensors 和 Interfaces；把標準版與新版的兩組型號分開。 |
| [[S03]] | Overview 模式表及 GPS Dependency；定位需求指有效水平位置。 |
| [[S04]] | Warning 與 Overview；核對回平、油門和有風時的漂移。 |
| [[S05]] | Overview、氣壓 Note 與 Controls；保留中立區及氣壓變動的條件。 |
| [[S06]] | 首段與 Controls；保留替代來源有效及估測原點的條件。 |
| [[S07]] | Warning、地面站辨識段落及錯誤表；新增真實校正訊息作讀表練習。 |
| [[S08]] | 垂直位置／航向來源、Source Switching 與光流範例；區分水平速度及相對位置。 |
