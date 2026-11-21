# Wiki 與投影片來源對照

從頁碼查主張，或從文件反查用途。S02.3 表示 S02 來源卡的第 3 條中文摘錄。原頁段落以標題定位，便於查核會更新的線上文件。

## 由官方文件找投影片

| 來源卡／官方原文 | 本次逐項讀取位置 | 涵蓋頁 | 對讀筆記 |
|---|---|---|---|
| [S01](../wiki/sources/S01.md) · [Pixhawk 6C — Overview](https://docs.holybro.com/autopilot/pixhawk-6c/overview) | Overview：首段、處理器、隔振 | [01](#p01)、[02](#p02)、[03](#p03) | 板型與出廠韌體分開記錄；未查特定實驗室機器。 |
| [S02](../wiki/sources/S02.md) · [Pixhawk 6C — Technical Specification](https://docs.holybro.com/autopilot/pixhawk-6c/technical-specification) | Processors & Sensors → On-board sensors；Interfaces | [02](#p02)、[03](#p03)、[04](#p04) | 原卡未列新版組合。已分列兩版；簡報只教感測器種類。 |
| [S03](../wiki/sources/S03.md) · [Copter — Flight Modes](https://ardupilot.org/copter/docs/flight-modes.html) | Overview 模式表與圖例；GPS Dependency 的兩份清單 | [01](#p01)、[02](#p02)、[06](#p06)、[08](#p08)、[09](#p09)、[11](#p11) | 讀取 Pos Sensor 欄與圖例；將「不要求」限定在水平定位。 |
| [S04](../wiki/sources/S04.md) · [Copter — Stabilize Mode](https://ardupilot.org/copter/docs/stabilize-mode.html) | Warning；Overview 的 roll/pitch、風及 throttle 條目 | [06](#p06)、[07](#p07)、[11](#p11) | 用回平、需修正風漂和油門高度分工解釋。 |
| [S05](../wiki/sources/S05.md) · [Copter — Altitude Hold Mode](https://ardupilot.org/copter/docs/altholdmode.html) | Overview 與 Note；Controls 的中立區說明 | [06](#p06)、[08](#p08)、[11](#p11) | 保留油門中立區與環境氣壓兩個條件。 |
| [S06](../wiki/sources/S06.md) · [Copter — Loiter Mode](https://ardupilot.org/copter/docs/loiter-mode.html) | Loiter Mode 開頭；Controls 的非 GPS 與原點段落 | [06](#p06)、[09](#p09)、[11](#p11) | 保留替代來源有效與 EKF 原點兩個條件；未將光流寫成絕對位置。 |
| [S07](../wiki/sources/S07.md) · [Copter — Pre-Arm Safety Checks](https://ardupilot.org/copter/docs/common-prearm-safety-checks.html) | Warning；Recognising which Pre-Arm Check has failed using the GCS；Pre-Arm Failure Messages | [01](#p01)、[10](#p10)、[11](#p11) | 增加表中真實錯誤作為讀表練習。未引用停用設定。 |
| [S08](../wiki/sources/S08.md) · [Copter — EKF Source Selection and Switching](https://ardupilot.org/copter/docs/common-ekf-sources.html) | 開頭的 EKF3 水平／垂直與航向欄位；Source Switching；ExternalNAV/Optical Flow Transitions | [04](#p04)、[05](#p05)、[09](#p09) | 區分水平位置與水平速度；增加氣壓計及羅盤預設來源的段落依據。 |

## 由投影片查證據

每頁下表依畫面段落排序。「適用範圍」也是 HTML 本頁證據面板的內容。自我檢核的引用依據另列在表後。

<a id="p01"></a>
### 01　歡迎來到 UAV 實驗室

[投影片](deck.html#p01) · [證據卡](cards/01.json) · [逐頁稿](drafts/01.json)

| 段落 | 投影片主張 | Wiki 概念 | 來源卡條目 |
|---|---|---|---|
| 01a | 從 Pixhawk 6C 開始，辨認 UAV（無人機）的飛行控制器硬體。 | [flight-stack](../wiki/concepts/flight-stack.md) | [S01.1](../wiki/sources/S01.md) |
| 01b | 比較飛行模式，看機身傾斜、高度與水平位置各由誰控制。 | [flight-modes](../wiki/concepts/flight-modes.md) | [S03.1](../wiki/sources/S03.md) |
| 01c | 讀懂 Pre-Arm（解鎖前檢查）訊息，找到對應的官方說明。 | [prearm](../wiki/concepts/prearm.md) | [S07.1](../wiki/sources/S07.md)、[S07.3](../wiki/sources/S07.md)、[S07.2](../wiki/sources/S07.md) |

自我檢核依據為 01c。

適用範圍：學習目標與讀表練習不代表實機已通過飛行驗證。

<a id="p02"></a>
### 02　無人機系統分工

[投影片](deck.html#p02) · [證據卡](cards/02.json) · [逐頁稿](drafts/02.json)

| 段落 | 投影片主張 | Wiki 概念 | 來源卡條目 |
|---|---|---|---|
| 02a | 飛控板提供運算與周邊介面。查板上有哪些元件，從 Holybro 的硬體文件開始。 | [flight-stack](../wiki/concepts/flight-stack.md) | [S01.1](../wiki/sources/S01.md)、[S02.3](../wiki/sources/S02.md)、[S01.2](../wiki/sources/S01.md) |
| 02b | Holybro 說明出廠預裝 PX4。若使用 ArduPilot 的 Copter（多旋翼飛控韌體），飛行模式的行為要查 Copter 文件。 | [flight-stack](../wiki/concepts/flight-stack.md) | [S01.3](../wiki/sources/S01.md)、[S03.1](../wiki/sources/S03.md) |
| 02c | 板子上的型號能識別硬體。要判斷手上的機器會怎麼執行飛行模式，還要確認目前安裝的韌體。 | [flight-stack](../wiki/concepts/flight-stack.md) | [S01.3](../wiki/sources/S01.md) |

自我檢核依據為 02b、02c。

適用範圍：硬體型號與韌體識別要分開。以兩份文件共同說明軟硬體分工。

<a id="p03"></a>
### 03　Pixhawk 6C 是什麼？

[投影片](deck.html#p03) · [證據卡](cards/03.json) · [逐頁稿](drafts/03.json)

| 段落 | 投影片主張 | Wiki 概念 | 來源卡條目 |
|---|---|---|---|
| 03a | 處理器負責運算；規格也列出板載加速度計、陀螺儀、磁力計與氣壓計。 | [flight-stack](../wiki/concepts/flight-stack.md) | [S01.2](../wiki/sources/S01.md)、[S02.1](../wiki/sources/S02.md) |
| 03b | 遙測埠、GPS（全球定位系統）埠與遙控輸入，都是連接周邊的介面。 | [flight-stack](../wiki/concepts/flight-stack.md) | [S02.3](../wiki/sources/S02.md) |
| 03c | Holybro 分列標準版與新版的慣性元件。查加速度計或陀螺儀型號時，要先讀對版本。 | [sensors-and-ekf](../wiki/concepts/sensors-and-ekf.md) | [S02.2](../wiki/sources/S02.md) |

自我檢核依據為 03b。

適用範圍：列有 GPS 介面不代表已接上接收器，也不保證定位可用。

<a id="p04"></a>
### 04　認識常見感測器

[投影片](deck.html#p04) · [證據卡](cards/04.json) · [逐頁稿](drafts/04.json)

| 段落 | 投影片主張 | Wiki 概念 | 來源卡條目 |
|---|---|---|---|
| 04a | 在 Pixhawk 6C 的規格裡，找加速度計與陀螺儀這一組。 | [sensors-and-ekf](../wiki/concepts/sensors-and-ekf.md) | [S02.1](../wiki/sources/S02.md)、[S02.2](../wiki/sources/S02.md) |
| 04b | 板上感測器包含磁力計。估算航向，也就是機頭朝向時，飛控的 EKF3（擴展卡爾曼濾波器）通常預設使用羅盤。 | [sensors-and-ekf](../wiki/concepts/sensors-and-ekf.md) | [S02.1](../wiki/sources/S02.md)、[S08.4](../wiki/sources/S08.md) |
| 04c | 板上的氣壓計提供氣壓資訊。EKF3 預設用氣壓計估算垂直位置，也就是高度。 | [sensors-and-ekf](../wiki/concepts/sensors-and-ekf.md) | [S02.1](../wiki/sources/S02.md)、[S08.4](../wiki/sources/S08.md) |

自我檢核依據為 04b、04c。

適用範圍：感測器存在、提供量測與估測器實際選用是不同層次。

<a id="p05"></a>
### 05　EKF 在做什麼？

[投影片](deck.html#p05) · [證據卡](cards/05.json) · [逐頁稿](drafts/05.json)

| 段落 | 投影片主張 | Wiki 概念 | 來源卡條目 |
|---|---|---|---|
| 05a | 在 ArduPilot 的 EKF3 中，水平位置、水平速度、垂直位置與航向各有對應的來源設定。 | [sensors-and-ekf](../wiki/concepts/sensors-and-ekf.md) | [S08.1](../wiki/sources/S08.md)、[S08.4](../wiki/sources/S08.md) |
| 05b | 以預設配置為例，垂直位置用氣壓計，航向通常用羅盤。同一台飛機可以依估測項目使用不同來源。 | [sensors-and-ekf](../wiki/concepts/sensors-and-ekf.md) | [S08.4](../wiki/sources/S08.md) |
| 05c | Optical Flow（光流）在官方範例中提供水平速度。這個配置估出的水平位置是相對位置。 | [sensors-and-ekf](../wiki/concepts/sensors-and-ekf.md) | [S08.3](../wiki/sources/S08.md) |

自我檢核依據為 05a、05c。

適用範圍：保留來源配置語境，不宣稱任何感測器可保證絕對位置或精度。

<a id="p06"></a>
### 06　為什麼有不同飛行模式？

[投影片](deck.html#p06) · [證據卡](cards/06.json) · [逐頁稿](drafts/06.json)

| 段落 | 投影片主張 | Wiki 概念 | 來源卡條目 |
|---|---|---|---|
| 06a | 橫滾與俯仰可回平，高度由飛手控制。 | [flight-modes](../wiki/concepts/flight-modes.md) | [S03.1](../wiki/sources/S03.md)、[S03.2](../wiki/sources/S03.md)、[S04.1](../wiki/sources/S04.md) |
| 06b | 飛控增加高度保持功能，這個模式不要求水平定位。 | [flight-modes](../wiki/concepts/flight-modes.md) | [S03.1](../wiki/sources/S03.md)、[S03.2](../wiki/sources/S03.md)、[S05.1](../wiki/sources/S05.md) |
| 06c | 飛控還會嘗試維持水平位置，因此需要有效的位置資訊。 | [flight-modes](../wiki/concepts/flight-modes.md) | [S03.1](../wiki/sources/S03.md)、[S03.2](../wiki/sources/S03.md)、[S03.3](../wiki/sources/S03.md)、[S06.1](../wiki/sources/S06.md) |

自我檢核依據為 06b、06c。

適用範圍：表內「不需要」僅指水平位置資訊。

<a id="p07"></a>
### 07　Stabilize：姿態回正

[投影片](deck.html#p07) · [證據卡](cards/07.json) · [逐頁稿](drafts/07.json)

| 段落 | 投影片主張 | Wiki 概念 | 來源卡條目 |
|---|---|---|---|
| 07a | Roll（橫滾）與 Pitch（俯仰）搖桿回中後，飛控使機身回到水平姿態。 | [flight-modes](../wiki/concepts/flight-modes.md) | [S04.1](../wiki/sources/S04.md)、[S04.2](../wiki/sources/S04.md) |
| 07b | 飛手仍須調整油門來維持高度。回平這個動作本身沒有接管定高。 | [flight-modes](../wiki/concepts/flight-modes.md) | [S04.1](../wiki/sources/S04.md) |
| 07c | 風吹時，已回平的機身仍可能水平移動，飛手須修正位置。 | [flight-modes](../wiki/concepts/flight-modes.md) | [S04.2](../wiki/sources/S04.md) |

自我檢核依據為 07a、07c。

適用範圍：姿態、高度、水平位置要分別解讀。

<a id="p08"></a>
### 08　AltHold：高度保持

[投影片](deck.html#p08) · [證據卡](cards/08.json) · [逐頁稿](drafts/08.json)

| 段落 | 投影片主張 | Wiki 概念 | 來源卡條目 |
|---|---|---|---|
| 08a | 油門桿指定升降速度，回到中立區時，飛控嘗試維持目前高度。 | [flight-modes](../wiki/concepts/flight-modes.md) | [S05.1](../wiki/sources/S05.md)、[S05.3](../wiki/sources/S05.md) |
| 08b | 飛控自動調節油門。它主要依氣壓估計高度，環境氣壓改變時，定高也可能受影響。 | [flight-modes](../wiki/concepts/flight-modes.md) | [S05.1](../wiki/sources/S05.md)、[S05.2](../wiki/sources/S05.md) |
| 08c | 橫滾、俯仰與偏航仍由飛手操控。AltHold 沒有自動維持水平位置的功能。 | [flight-modes](../wiki/concepts/flight-modes.md) | [S05.1](../wiki/sources/S05.md)、[S03.2](../wiki/sources/S03.md) |

自我檢核依據為 08a、08c。

適用範圍：勿將氣壓高度當作精確離地高度，不承諾高度誤差範圍。

<a id="p09"></a>
### 09　Loiter：位置保持

[投影片](deck.html#p09) · [證據卡](cards/09.json) · [逐頁稿](drafts/09.json)

| 段落 | 投影片主張 | Wiki 概念 | 來源卡條目 |
|---|---|---|---|
| 09a | Loiter 嘗試維持位置、航向與高度。水平操控桿回中後，飛機會減速並嘗試定點。 | [loiter-and-position](../wiki/concepts/loiter-and-position.md) | [S06.1](../wiki/sources/S06.md)、[S06.2](../wiki/sources/S06.md) |
| 09b | GPS 是常見定位來源。官方的非 GPS 例子要求替代定位來源運作正常，並由地面站設定 EKF 原點（估測座標的基準）。 | [loiter-and-position](../wiki/concepts/loiter-and-position.md) | [S03.2](../wiki/sources/S03.md)、[S03.3](../wiki/sources/S03.md)、[S06.3](../wiki/sources/S06.md) |
| 09c | 光流可以提供水平速度。估測器的來源配置必須對應實際輸入，系統仍要能估出可用的水平位置。 | [loiter-and-position](../wiki/concepts/loiter-and-position.md) | [S08.3](../wiki/sources/S08.md)、[S06.3](../wiki/sources/S06.md) |

自我檢核依據為 09b、09c。

適用範圍：未驗證任何實機；裝上光流或僅設好原點都不足以推論能定點。

<a id="p10"></a>
### 10　Pre-Arm：解鎖前先檢查

[投影片](deck.html#p10) · [證據卡](cards/10.json) · [逐頁稿](drafts/10.json)

| 段落 | 投影片主張 | Wiki 概念 | 來源卡條目 |
|---|---|---|---|
| 10a | Pre-Arm 會在發現校正、配置或感測器資料異常時阻止解鎖。 | [prearm](../wiki/concepts/prearm.md) | [S07.1](../wiki/sources/S07.md) |
| 10b | 例如「3D Accel calibration needed」。在官方錯誤表找到相同訊息，原因欄指出加速度計尚未完成校正。 | [prearm](../wiki/concepts/prearm.md) | [S07.2](../wiki/sources/S07.md)、[S07.4](../wiki/sources/S07.md) |
| 10c | 依對應條目處理，保留安全檢查並在飛行前排除問題。 | [prearm](../wiki/concepts/prearm.md) | [S07.3](../wiki/sources/S07.md) |

自我檢核依據為 10b。

適用範圍：範例是官方訊息，不是本專案實機日誌。

<a id="p11"></a>
### 11　三種模式回顧與下一步

[投影片](deck.html#p11) · [證據卡](cards/11.json) · [逐頁稿](drafts/11.json)

| 段落 | 投影片主張 | Wiki 概念 | 來源卡條目 |
|---|---|---|---|
| 11a | 橫滾、俯仰回平。高度與水平位置由飛手維持。 | [flight-modes](../wiki/concepts/flight-modes.md) | [S03.2](../wiki/sources/S03.md)、[S04.1](../wiki/sources/S04.md)、[S04.2](../wiki/sources/S04.md) |
| 11b | 油門桿在中立區時定高。水平位置仍由飛手維持。 | [flight-modes](../wiki/concepts/flight-modes.md) | [S03.2](../wiki/sources/S03.md)、[S05.1](../wiki/sources/S05.md)、[S05.3](../wiki/sources/S05.md) |
| 11c | 在定位有效時，水平桿回中後會減速並嘗試保持位置。 | [flight-modes](../wiki/concepts/flight-modes.md) | [S03.2](../wiki/sources/S03.md)、[S06.1](../wiki/sources/S06.md) |
| 11d | 抄下地面站完整訊息，對照 Pre-Arm 官方錯誤表，先排除原因。 | [prearm](../wiki/concepts/prearm.md) | [S07.2](../wiki/sources/S07.md)、[S07.3](../wiki/sources/S07.md) |

自我檢核依據為 11a、11b、11c、11d。

適用範圍：只比較指定三種模式的保持行為；安全檢查獨立判讀。

## V3 代表頁的讀圖依據

第 03 頁將 03a／03b 的 S01、S02 區分為板載與外接介面。版本條件由 03c 保留。
第 06 頁的矩陣合併 06a–06c 與既有 07c、08a、08c、09a；見[九個比較格的逐格對應](../checks/v3/figure-review.md)。
第 10 頁完整訊息及其原因對應 10b／S07.4，同頁的安全處理順序對應 10a–10c。

## V3 全套圖解

逐頁圖解、條件與對應條目見[完整技術審查](../checks/final/faithfulness.md)。
第 05 頁的垂直位置與航向見 S08.4，光流的水平速度與相對位置見 S08.3。
第 07–09 頁依序對應 S04.1–2、S05.1 與 S05.3、S03.2 與 S06.1–3。第 09 頁的光流限制另見 S08.3。
