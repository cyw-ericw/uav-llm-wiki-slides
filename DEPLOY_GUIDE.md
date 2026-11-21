# GitHub Pages 部署教學（尚未實際發布）

1. 前往 GitHub，建立新的 **Public** repository，名稱建議 `uav-llm-wiki-slides`，不要覆蓋第九週的 `uav-lab-wiki`。
2. 解壓本專案 ZIP。**將內層 `uav-llm-wiki-slides/` 資料夾「裡面的檔案與子資料夾」上傳到 repository 根目錄**，不要多包一層資料夾。根目錄應直接看到 `index.html`、`README.md`、`slides/`、`wiki/`。
3. GitHub 網頁上傳限制**每次最多 100 個檔案**；若超過，請分批上傳或使用 GitHub Desktop／Git。若使用「GitHub 網頁上傳精簡版 ZIP」，其檔案總數已控制於 100 以下。
4. 到 repo `Settings` → `Pages` → `Build and deployment` → `Source: Deploy from a branch` → `main` + `/(root)` → `Save`。
5. 等 GitHub 出現公開網站網址，使用無痕視窗檢查首頁、slides/deck.html、wiki/index.html、workflow-view.html、verification-view.html 皆能讀取。
6. 確認後，才在 COOL 繳交公開網站 URL 與 GitHub repo URL，加上簡短 Graph／Loop 反思。不要把本機 `/Users/...` 路徑作為公開連結。

**注意**：原始 wiki Markdown 應保留以證明實際建置；`.html` 僅為讓老師更方便閱讀的網頁副本。`raw/source_cards.json` 是官方文件的查核摘錄，不是全文。
