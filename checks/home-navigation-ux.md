# 網站導覽補強：左上角品牌返回首頁

日期：2026-11-22。使用者在 GitHub Pages 發布後，反映進入 HTML 簡報與 Wiki 子頁後，左上角「UAV LAB / Wiki」品牌文字缺乏返回首頁的直覺互動。

## 修改範圍

- 首頁、Wiki 索引／Log、Wiki 概念與來源頁、Graph、需求、來源對照、驗證報告：讓左上角 `UAV LAB / Wiki` 成為返回網站首頁的連結，保留原本的「首頁」選單。
- 11 頁 HTML 簡報：桌面側欄標題「無人機實驗室」可返回網站首頁；手機窄螢幕上於左上角顯示 `UAV LAB / Wiki` 返回首頁入口。單獨下載 HTML 時，首頁入口指向公開 GitHub Pages 網站。
- 同步修改 `scripts/deck-template.html`，避免日後執行 `scripts/render.py` 時覆蓋這項功能。
- 未修改 `raw/`、Wiki Markdown、Evidence Cards、逐頁稿、既有的 Graph/Loop 歷史紀錄，也未改寫課文、官方引文或原有換頁邏輯。

## 實際驗證

- 解析 20 個公開網站 HTML 頁面，檢查其品牌連結的相對 URL 經正規化後都精確指向網站根目錄的 `index.html`：20/20 PASS。
- 檢查簡報桌面與手機兩組品牌連結存在、目標都是既有 GitHub Pages 首頁：PASS。
- 重新執行 `validate.py`、`check_slides.py --draft`、`source_map.py`、`render.py`、`check_render.py`：全部 PASS；11 頁、34 個正文主張、11 組問答、66 處官方引用及 178 個來源對照連結保留。
- 在 Chromium 以 `set_content` 載入本地 HTML，分別測試 1440、768、390、320 CSS px：桌面／手機品牌連結可點擊、跳轉意圖指向首頁；「下一頁」仍可將頁碼切換為 02 / 11；四種寬度無水平溢出。全部 PASS。
- 執行環境限制直接瀏覽 file URL 或測試網站導覽；部署到 GitHub Pages 後的正式點擊，仍需使用者在瀏覽器人工確認。未宣稱已測到遠端網站的真實 200 狀態。

## 回退／重測

屬於 Graph／Loop 中「使用者驗收 → 導覽互動問題 → HTML 模板及網站標頭局部修正 → 重新檢查」的迭代，無需重建 Wiki。若 GitHub 上傳後沒有更新，先清除快取或強制重新整理，再檢查是否所有修改過的 HTML、`site.css` 與模板都已提交。
