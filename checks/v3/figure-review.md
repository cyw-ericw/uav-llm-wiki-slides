# V3 第一批圖解獨立審查

**技術忠實度 PASS，3/3 圖。** 第 06 頁矩陣整合第 07 至 09 頁已查核細節，完整逐格對應如下。圖首列出文件編號；只查第 06 頁證據卡，無法直接找到每一格的細節。

審查者獨立讀取 `scripts/batch_one.py`、`scripts/figures/pixhawk-logic.svg`、三頁的稿件與證據卡，並重新開啟 S01 至 S07 的官方段落。實際呼叫三個頁碼的 `teaching_body`，讀取圖中文字與表格排列，確認三次傳入的正文區皆原樣返回。三頁稿件和三張證據卡分別與原專案逐位元組比較，六檔相同。本審查涵蓋教學內容；瀏覽器與畫面尺寸另見 HTML 關卡。

| 頁 | 審查結果與界線 |
|---|---|
| 03 | PASS。處理器、加速度計、陀螺儀、磁力計與氣壓計屬板載功能，GPS 埠、遙測埠及遙控輸入屬介面，對應 03a、03b。SVG 標籤和圖說把層次、位置識別為教學示意。晶片方塊及電路板層數沒有充當實體規格；正文保留版本辨識與定位是否可用兩個問題。見 Holybro 的 Overview、Technical Specification 的 Processors & Sensors 與 Interfaces。 |
| 06 | PASS。官方模式表與三份專頁支持下表的九格含義。「中立區」在 AltHold 的高度欄指油門桿；兩個模式的「回平」指橫滾、俯仰桿回中。定位條件附在 Loiter 格下方。教學時可依這些軸別讀表。 |
| 10 | PASS。原文錯誤字串與大小寫相同；查訊息的箭頭指向官方表格中的成因，旁邊標明為官方文件範例。圖解對應 10b 的 S07.2、S07.4。原稿 10c 的飛行前排除問題保留。 |

## 第 06 頁逐格追溯

| 模式 | 姿態與水平桿 | 高度 | 水平位置 |
|---|---|---|---|
| Stabilize | 06a、S04.1 的橫滾／俯仰回平 | 06a、S04.1 的飛手油門 | 07c、S04.2 的風漂需飛手修正 |
| AltHold | S03 Overview 的 Alt Hold 列直接指明橫滾／俯仰回平，S05 Overview 說明操控與 Stabilize 相同 | 08a、S05.3 的油門中立區定高 | 08c、S05.1 配合 S03 模式表，水平位置由飛手照顧 |
| Loiter | 09a、S06.2 的水平桿調整位置 | 09a、S06.1 的高度保持 | 06c、S06.1 與 S03.2 的嘗試保持水平位置與有效定位前提 |

## 官方來源

- [Holybro Overview](https://docs.holybro.com/autopilot/pixhawk-6c/overview) · [Holybro Technical Specification](https://docs.holybro.com/autopilot/pixhawk-6c/technical-specification)
- [Copter 模式表與圖例](https://ardupilot.org/copter/docs/flight-modes.html) · [Stabilize](https://ardupilot.org/copter/docs/stabilize-mode.html) · [Altitude Hold](https://ardupilot.org/copter/docs/altholdmode.html) · [Loiter](https://ardupilot.org/copter/docs/loiter-mode.html)
- [Pre-Arm Safety Checks 的地面站說明與 Failure Messages 錯誤表](https://ardupilot.org/copter/docs/common-prearm-safety-checks.html)
