# 忠實度獨立審查 · 首輪

2026-11-21（臺北）。由未撰寫本批逐頁稿的獨立 AI 審查。對讀 11 個 draft（標題、導語、34 個內容段落、11 組提問與解答）、對應 evidence cards、5 篇 Wiki 概念及 raw 事實欄。重新開啟八份官方文件的相關段落。下列審查保留首輪當時的事實編號，後來的改動請見重測紀錄。

**結果為 FAIL**。八頁通過，三頁的技術敘述與原頁相符，但證據卡指向摘要中過於籠統的條目。程式能證實 ID 存在，這一關另要求標出的條目可以解釋那一句話。三頁退回 Evidence，無須重寫大綱或重做 Wiki。

| 頁 | 逐段對讀與教學問答 | 首輪 |
|---|---|---|
| 01 | a 的飛控硬體由 S01.1 支持。b 的模式控制量對照 S03.1。c 的異常與飛行前檢查由 S07.1、.3 支持，但正文另有「讀懂訊息，找到對應的官方說明」，證據未指向說明讀取地面站訊息的 S07.2。解答將範圍限於文件練習與實機仍需檢查。 | FAIL · 01c 補 S07.2 |
| 02 | a 的 S01.1 指向平台與開放標準、S02.3 指向介面；「提供運算」可在 S01.2 或 S02.1 所記處理器找到。b 的 PX4 出廠預裝與條件句「若使用 ArduPilot」成立。c 和解答把當前韌體列為須現場確認的資訊。 | FAIL · 02a 補處理器條目 |
| 03 | a 的處理器、四種板載感測元件與 S01.2、S02.1 相符。b 的三類連接介面見 S02.3。c 的版本差異見 S02.2；題目用「有連接埠」推論不出「有定位」，未宣稱實機接有周邊。 | PASS |
| 04 | a 根據 S02 的 Accel/Gyro 分組辨認 IMU。b 與 c 分別用 S02.1 確認硬體、用 S08.4 確認通常預設的航向與垂直位置來源；題解引導讀者查設定，未保證所用實機採預設值。 | PASS |
| 05 | 導語的量測更新見 S08 起始段。a 涵蓋可分別設定的四類量。b 準確轉述 S08.4 的兩個預設值。c 及題解的依據是 S08.3 的光流來源組範例，區分水平速度輸入與相對位置，保留「這個配置」限定。 | PASS |
| 06 | a 的回平與油門分工、b 的定高、c 的水平定點都能由官方模式表及專頁證實。現有 S03.1 僅概述不同模式、S03.2 只列定位需求、S03.3 描述替代定位來源。若只按原卡讀摘要，會少掉三種模式分別維持什麼的具體文字。題解「高度資訊不等於水平位置資訊」正確。 | FAIL · 06a/b/c 分別增列 S04.1、S05.1、S06.1 |
| 07 | a 的兩個軸回中回平、b 的高度仍由飛手以油門管理、c 的風漂需修正，逐項對到 S04 Overview。標題及問答以姿態和水平位置兩種觀察量說明「回平仍可漂移」，沒有擴大到所有飛行模式。 | PASS |
| 08 | a 由 S05 Controls 支撐，區分升降速度與中立區。b 由 Overview 及其 Note 支撐，保留「主要」「可能」等條件。c 與題解符合 S03 模式表及 S05 的水平操控說明。 | PASS |
| 09 | a 的回中減速與三項保持對到 S06 開頭及 Controls。b 同時保留 S03 有效位置和 S06 替代來源可用、由地面站設定原點的例子。c 與題解區分 S08.3 的水平速度與系統水平位置估測；沒有對室內實機作成功保證。 | PASS |
| 10 | a 取自 S07 開頭。b 逐字核對警示名稱「3D Accel calibration needed」及其官方成因。c 保留 Warning 的飛行前排除問題。題解不根據籠統的無法解鎖訊息推定特定故障。 | PASS |
| 11 | a、b、c 分別核對 S04 回平、S05 油門中立區及 S06 水平桿回中；S03 提供有效位置條件。d 及題解把安全訊息交由 S07 錯誤表查核。標題與導語以「相應」中立位置限定比較，不會將不同模式的操控軸混為一談。 | PASS |

數字複核包括標題、導語、正文及解答。Pixhawk 6C、PX4、EKF3 是名稱，3D 是官方訊息中的字串；未見教學稿自行加入精度、門檻、時限或飛行速度。

## 本輪讀取的原頁

| ID | 對讀位置 | 原頁 |
|---|---|---|
| S01 | Overview 首段的板型、預裝韌體與處理器 | [Holybro Overview](https://docs.holybro.com/autopilot/pixhawk-6c/overview) |
| S02 | Processors & Sensors、兩個版本與 Interfaces | [Holybro Technical Specification](https://docs.holybro.com/autopilot/pixhawk-6c/technical-specification) |
| S03 | Overview 的模式表、圖例與 GPS Dependency 清單 | [Copter Flight Modes](https://ardupilot.org/copter/docs/flight-modes.html) |
| S04 | Overview 橫滾、俯仰、風漂與油門段落 | [Stabilize](https://ardupilot.org/copter/docs/stabilize-mode.html) |
| S05 | Overview、氣壓 Note、Controls 中立區 | [Altitude Hold](https://ardupilot.org/copter/docs/altholdmode.html) |
| S06 | 開頭及 Controls 的回中、非 GPS 與原點段落 | [Loiter](https://ardupilot.org/copter/docs/loiter-mode.html) |
| S07 | 開頭、Warning、地面站辨識段落、Failure Messages | [Pre-Arm Safety Checks](https://ardupilot.org/copter/docs/common-prearm-safety-checks.html) |
| S08 | 垂直位置及航向預設值、ExternalNAV/Optical Flow Transitions | [EKF Source Selection and Switching](https://ardupilot.org/copter/docs/common-ekf-sources.html) |
