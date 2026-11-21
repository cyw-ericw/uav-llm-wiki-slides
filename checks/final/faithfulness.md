# 最終版圖解與教學內容獨立審查

## 查核方式

由未撰寫圖解的審查者讀取 `scripts/course_graphics.py`、`scripts/batch_one.py` 和兩個 SVG 圖檔，按 11 個頁碼分別執行實際圖解函式，比對其標籤、圖說、來源和傳入的正文。使用原專案作基準逐位元組比較 11 張證據卡、11 份逐頁稿、5 篇 Wiki 概念、8 張 Wiki 來源卡及 raw 事實庫，全部相同。已通過的正文、提問與解答可沿用先前獨立審查。這一輪額外查核圖解新增的關係。

## 首輪結果

**FAIL，10 頁通過，第 09 頁退回圖解文字。** 正文與證據卡均無需退修。下表列出每頁圖解的實際對應。

| 頁 | 圖解、原稿和官方來源 | 首輪判定 |
|---|---|---|
| 01 | 課程地圖對應 01a–c（S01、S03、S07）。三個入口分別落在飛控與感測、模式、安全檢查，四旋翼只用於辨識課程主題。 | PASS |
| 02 | 02a–c（S01.1–3、S02.1、S02.3、S03.1）。硬體欄列元件和介面，韌體欄要求先辨認實際安裝內容；Copter 文件入口有「使用 Copter 時」的限制。 | PASS |
| 03 | 03a–c（S01.2、S02.1–3）。板載元件、外接介面分開，邏輯圖有示意標籤；規格有 GPS 埠的例子沒有延伸成實機有定位。 | PASS |
| 04 | 04a–c（S02.1–2、S08.4）。磁力計、氣壓計指向相應的估測用途，正文註明 EKF3 的一般或預設來源，保留配置條件。 | PASS |
| 05 | 05a–c（S08.1、.3、.4）。逐列比對量測與用途。氣壓資料供垂直位置，羅盤供航向參考；圖中分列「預設來源」「通常預設」。光流的水平速度是官方特定配置的輸入，圖下明載水平位置是相對估值。 | PASS |
| 06 | 06a–c 與 07–09 頁對應證據。S03 模式表用於三種模式總覽；S04.1–2 支持回平與飛手分工；S05.1、.3 支持中立區定高；S06.1–2 支持水平桿調整位置與嘗試保持。圖下注明有效水平位置估測前提。 | PASS |
| 07 | 07a–c（S04.1–2）。同一四旋翼先傾斜再回平；圖例寫明亮色僅為「可能的位置」。條件為橫滾、俯仰桿回中，正文保留飛手顧油門與風漂修正。 | PASS |
| 08 | 08a–c（S05.1–3、S03.2）。兩個相同高度的機體輪廓代表同一架機的不同位置；油門中立區與「嘗試維持」齊備。圖上無刻度及精度承諾，正文保留氣壓影響和水平需飛手修正。 | PASS |
| 09 | 09a–c（S03.2–3、S06.1–3、S08.3）。地面十字為本次定點，正文保留替代來源正常、配置相符、EKF 原點等條件。首輪場景將「位置估測有效、水平桿回中」連到「減速後嘗試維持位置與高度」；S06 Controls 將水平桿與油門的控制量分開，因此單憑水平桿回中不能判定高度指令。 | FAIL · Render |
| 10 | 10a–c（S07.1–4）。原始字串與錯誤表所列成因相符，圖上標作官方例子，正文仍要求飛前排除檢查失敗原因。 | PASS |
| 11 | 11a–d（S03–S07）。回看連結對應三種保持行為，正文及問答補足桿位、定位及讀取 Pre-Arm 訊息的條件。 | PASS |

`quad-body.svg` 的元件解析得到四個旋翼，三種模式使用同一原圖與視角。場景的平移、姿態旋轉和地面基準是概念示意，未新增實機尺寸、位移、速度或高度的量測值。

## 原頁對讀

[Holybro Overview](https://docs.holybro.com/autopilot/pixhawk-6c/overview) 與 [Technical Specification](https://docs.holybro.com/autopilot/pixhawk-6c/technical-specification) 提供硬體及版本根據。模式分工對讀 [Flight Modes](https://ardupilot.org/copter/docs/flight-modes.html)、[Stabilize Overview](https://ardupilot.org/copter/docs/stabilize-mode.html)、[Altitude Hold Controls](https://ardupilot.org/copter/docs/altholdmode.html)、[Loiter Controls](https://ardupilot.org/copter/docs/loiter-mode.html)。錯誤訊息對照 [Pre-Arm Failure Messages](https://ardupilot.org/copter/docs/common-prearm-safety-checks.html)。估測來源對照 [EKF3 的來源欄位與 ExternalNAV/Optical Flow Transitions](https://ardupilot.org/copter/docs/common-ekf-sources.html)。

## 第 09 頁局部修正與重測

**PASS，累計 11/11 頁通過。** 場景改為「減速後嘗試維持水平位置。圖中十字標示這次的定點。」重新呼叫 `mode_scene('09')`，並解析重建後 `slides/deck.html` 的 `section#p09`。逐項斷言確認新文案同時出現在可見圖說與 SVG 的無障礙標籤，兩者均無舊文案；有效定位、水平桿回中、替代來源正常、設定 EKF 原點、光流可提供水平速度等文字均保留。正文仍列 Loiter 一般可維持位置、航向與高度，再另句說明水平桿回中後的行為。退回一次圖解節點即解決本輪發現的唯一問題。
