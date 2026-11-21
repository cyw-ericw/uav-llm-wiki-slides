# UAV LLM Wiki｜AI 開發與工作流程規範

## 1. 專案目標
建立給新進 UAV 實驗室成員使用的繁體中文 LLM Wiki，先從至少五篇官方文件實際 ingest，再依 Wiki 建置 10–12 頁 HTML 教學簡報。重點是可追溯、可驗證的資料與 Loop / Graph，不是單純把網站做好看。

## 2. 唯一真實來源與限制
- 只使用 `raw/source_cards.json` 中已登錄的 Holybro、ArduPilot 資料卡及其官方來源網址寫入知識敘述；如需新增資料，先以新來源 ID 登錄並留下紀錄。
- `raw/source_cards.json` 是**由官方頁面人工整理／查核後的中文來源摘錄**，不是整頁官方原文，也不能當成原文逐字引用。
- 不可虛構文獻、頁碼、數據、查核結果、實驗或工作流程錯誤；沒有根據就寫「待確認」。
- 對「Loiter 無 GPS」、「EKF sensor fusion」等條件性議題，需保留位置估測條件與韌體設定脈絡。
- 教學並非飛行安全驗證；不建議繞過 Pre-Arm、不能自稱能保證安全飛行。
- 勿加入 API Key、密碼、私人紀錄、原始專有文件或未授權圖片。

## 3. 專案結構
```
AGENTS.md              AI 工作規範
requirements.md        已確認需求
raw/source_cards.json  官方來源的整理摘錄與來源連結
wiki/index.md          概念與來源索引
wiki/log.md            真實 ingest 紀錄
wiki/sources/Sxx.md    每一篇來源卡（由 ingest.py 生成）
wiki/concepts/*.md     以來源 ID 對應的概念筆記
slides/outline.md      待人工確認的簡報大綱
slides/cards/          每頁的來源證據卡
slides/drafts/         逐頁內容（確認大綱後才建立）
slides/deck.html       最終 HTML 簡報（尚未產生）
slides/report.md       執行、檢查、反思（未測不可先宣稱通過）
checks/                可執行驗證及結果檔案
scripts/ingest.py      以來源摘錄產生 wiki/sources / index / log
```

## 4. Ingest 程序
1. 檢查至少 5 份不同官方文件；每份必須有 `id`、標題、網址、出版者、實際查核的關鍵敘述與章節線索。
2. 來源摘錄放於 `raw/source_cards.json`；不假裝已儲存完整官方網頁。
3. 執行 `python3 scripts/ingest.py`，生成 `wiki/sources/`、來源索引與 ingest log。
4. 執行 `python3 scripts/validate.py` 驗證來源卡數、唯一 ID、URL、生成檔案、概念來源 ID 與基本連結。
5. 來源爭議要顯式標註，必要時回來源階段補查；禁止用 AI 記憶硬補。
6. 每次資料更新後需重跑 ingest 與 validate；更新 log 並保存 Git commit。

## 5. Wiki 編輯規則
- 概念頁第一行為 H1，含「概念／用語、簡短定義、初學者例子、常見誤解、來源」等資訊。
- 專業術語第一次出現加中文括註，文章用繁體中文，避免未解釋的艱深縮寫。
- 使用 Obsidian Wiki 連結 `[[S01]]`、`[[flight-modes]]` 等做關聯；重要事實需有來源 ID 與官方網址。
- 跨資料有衝突時，保留版本／使用條件的差異，不宣稱其中任一方必然正確。
- 優先局部修改，不刪除其他已驗收知識頁；維持 `wiki/index.md` 一致。

## 6. 簡報 Graph 與節點邊界
1. **Retrieval：** 只讀已建立的 Wiki 和來源卡，輸出 `slides/sources.md`。
2. **Coverage Gate：** 主題至少有 5 個已 ingest 來源及每個核心教學節點的支持來源，缺資料回 Ingest。
3. **Evidence Cards：** 每張投影片先填 source IDs、可支持之敘述、限制；不要混入 Wiki 外部事實。
4. **Outline：** 做 10–12 頁初學者教學結構，輸出 `slides/outline.md`；必須人工確認後才進入下一步。
5. **Draft：** 只讀 outline 與 evidence cards，逐頁生成內容，不能編造參數與數據。
6. **Faithfulness Gate：** 獨立審查來源對應、條件、過度簡化，錯在單頁就只退回該頁或證據卡。
7. **Render：** 僅把通過內容轉成 HTML/CSS，**不得自行修改已審核技術論點**。
8. **HTML Gate：** 用程式檢查連結、檔案、頁數、導覽；另以實際瀏覽器檢查溢出及可讀性。
9. **Publish / Report：** 成功後發布 GitHub Pages，並保存真實測試與修正紀錄。

## 7. Loop 與停止條件
- 每處錯誤最多 3 輪「產生 → 檢查 → 局部修訂 → 重新測試」。
- 通過門檻：技術敘述有相應 source ID、無明顯無根據數字、預計 10–12 頁且導覽有效、桌面／窄螢幕無明顯溢出。
- 來源不足、內容衝突未釐清、或達修正上限：**停止、自動記錄 blocker、交回人工決定**，不可謊稱通過。
- 程式檢查判斷結構；獨立 AI 審查判斷內容。不能用「我檢查過了」取代檢查報告。

## 8. 追溯與反思
- `slides/report.md` 必須記錄日期、使用哪一版 Wiki、每個檢查節點的 PASS/FAIL、實際修改前後與重測結果。
- 反思中的「最常出錯節點」只根據真實失敗次數計算；沒有失敗要如實寫「本次未觀察到失敗」，不得捏造。
- 若錯誤直到 HTML 才發現，檢討是否應把檢查提前到 evidence、outline、draft；保留 Graph 變更說明。
- 每個交付階段都要能打開、重跑、另存版本；逐段 Git commit。

## 9. 目前狀態（V3，全 11 頁；2026-11-22）
- 需求與 11 頁大綱：經使用者確認。
- 官方資料：8 份經查閱整理的來源摘要，不是官方網頁全文。
- Wiki：8 份來源卡、5 篇概念、索引與 ingest log 已建立。
- HTML：11 頁 V3 已產生，含自我檢核、每頁證據與可離線使用的圖解。
- 驗證：依 `slides/report.md` 和 `checks/` 已有執行紀錄，V3 圖解修正與重測有保留。不要把尚未執行的 Mac Safari、實體投影或手機觸控宣稱通過。
- 公開部署：**仍待使用者自行建立新 GitHub Repository 並啟用 GitHub Pages**。
- V1、V2 與 V3 第一批的舊狀態和變更歷程已保留於 `slides/report.md`、`checks/`，不再作為目前完成狀態。

## 10. 發布版限制
- `index.html`、`wiki/*.html`、`workflow-view.html`、`verification-view.html` 等為公開導覽用呈現副本；原本可追溯的 Markdown Wiki 與證據仍是內容來源。
- 發布準備可修改導覽首頁和文件狀態，但不可在未審核來源的情況下改動 11 頁的既有技術主張與證據。
