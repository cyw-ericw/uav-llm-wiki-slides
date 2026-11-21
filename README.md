# UAV LLM Wiki｜無人機實驗室新人入門（第十週作業）

> **目前版本：V3 全 11 頁，準備公開部署（2026-11-22）**。教學 HTML 與 Wiki 已完成建置和程式驗證；GitHub Pages 尚待發布，Mac Safari／投影／實體觸控仍需人工確認。請勿將「待驗收」寫成 PASS。

## 立即查看成果

- [網站首頁](index.html)｜[11 頁互動教學簡報](slides/deck.html)
- [LLM Wiki 瀏覽版](wiki/index.html)｜[原始 Wiki Markdown](wiki/index.md)｜[Ingest Log](wiki/log.md)
- [Graph／Loop 工作流程](workflow-view.html)｜[實際檢查與反思](verification-view.html)
- [逐頁 Wiki／證據對照](traceability-view.html)｜[完整原始對照檔](slides/sources.md)

## 作業與設計

本作業先與使用者討論並核准需求，再根據 8 篇 Holybro／ArduPilot 官方文件**經查閱整理的來源摘錄**建立 Markdown Wiki。`raw/source_cards.json` 與 `wiki/sources/` 是來源卡而非官方網頁全文。Wiki 含 5 篇概念筆記、索引及 ingest 日誌。

Graph 流程為：來源查核／Ingest → Wiki → 覆蓋率與證據卡 → 人工核准大綱 → 逐頁稿／忠實度審查 → HTML 渲染 → 瀏覽器測試與局部修正 → 人工驗收／發布。每處錯誤最多 3 輪，來源不足就停止而非猜測。詳見 [`workflow.md`](workflow.md)、[`slides/report.md`](slides/report.md)、`checks/`。

簡報維持 11 頁、34 個正文主張、11 組自我檢核、11 個證據面板與 66 處官方引用，採石墨黑工程展示風格，教學圖解為原創 SVG／HTML。圖解是概念示意，不是實際飛行量測或安全認證。第 07–09 頁使用相同四旋翼與地面參考點比較回平、定高和具有效定位條件下的定點。

## 專案主要位置

| 路徑 | 用途 |
|---|---|
| `AGENTS.md`、`requirements.md` | AI 專案規範與已確認需求 |
| `raw/source_cards.json` | 8 份官方來源的核對摘錄（非全文） |
| `wiki/` | Markdown LLM Wiki、來源卡、概念及 ingest log；`.html` 為公開閱讀副本 |
| `slides/outline.md`、`cards/`、`drafts/` | 人工核准大綱及每頁產製紀錄 |
| `slides/deck.html` | 可離線開啟的 11 頁教學簡報 |
| `slides/sources.md` | 原始資料、Wiki 與投影片的來源對照 |
| `slides/report.md`、`checks/` | Graph／Loop 實際執行、失敗及重測記錄 |
| `NEXT_STEPS.md`、`DEPLOY_GUIDE.md` | 待人工驗收項目與部署教學 |

## 再現檢查

從完整專案根目錄執行：

```bash
python3 scripts/validate.py
python3 scripts/check_slides.py --draft
python3 scripts/source_map.py
python3 scripts/render.py
python3 scripts/check_render.py
```

公開閱讀用 `.html` 頁面由原始 Markdown 整理產生；若更新知識內容，需同步刷新該頁網頁副本。**不需安裝套件即可開啟現有 `index.html`、Wiki 網頁及 `slides/deck.html`。**

先前各版本紀錄保留於 `slides/report.md` 與 `checks/`。GitHub Pages 的正式公開網址應在實際部署並測試後才填入 COOL；本 ZIP 尚不代表已發布。
