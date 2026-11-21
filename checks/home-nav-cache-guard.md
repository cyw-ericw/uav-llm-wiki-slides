# 首頁 ↔ 簡報導覽版本連結修正

本次使用者實測發現：帶 `?v=home-nav-3` 的簡報可以返回首頁，但從首頁透過無參數 `slides/deck.html` 再進入時，左側標題又可能讀到先前的舊版。

## 修正

- 版本代號：`20261122-home-v4`。
- 公開網站內所有「開啟簡報」入口，改用 `slides/deck.html?v=20261122-home-v4`（若原有 `#p09` 錨點，將 `?v=` 放在錨點之前）。
- 簡報的桌面／手機左上角首頁入口，改用 `https://cyw-ericw.github.io/uav-llm-wiki-slides/?v=20261122-home-v4`，讓回首頁與重新進入簡報都使用明確的版本網址。
- 原本的 11 頁正文、Wiki、來源卡、自我檢核與 Graph／Loop 記錄不更動；簡報修改的來源是 `scripts/deck-template.html`，不是只手改成品。

## 驗收範圍

建置和資料完整性以 `scripts/render.py`、`scripts/check_render.py` 及 `scripts/source_map.py` 再驗。其他頁的站內連結由程式解析；GitHub Pages 部署、瀏覽器快取與 Mac 實際連點行為仍須發布後人工確認。
