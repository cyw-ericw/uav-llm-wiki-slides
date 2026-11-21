# 常見飛行模式的比較

## 核心概念
Stabilize 主要穩定 Roll、Pitch 姿態，但高度須由飛手控制；AltHold 進一步提供自動高度維持；Loiter 再加入位置保持，因而需要可靠的水平位置估測。

## 對照
| 模式 | 主要功能 | 水平位置估測要求 |
|---|---|---|
| Stabilize | 姿態自動回正 | 不要求 |
| AltHold | 姿態穩定及高度維持 | 不要求 |
| Loiter | 高度與水平位置保持 | 需要可靠定位來源 |

## 初學者例子
橫滾與俯仰桿回中後，Stabilize 會回平；風吹仍可能引起水平漂移。[[S04]] AltHold 的油門桿指定升降速度，在中立區維持高度。氣壓變動可能影響定高。[[S05]] Loiter 則在水平桿回中後減速並嘗試定點。[[S06]]

## 常見誤解
「Loiter 必定要求 GPS」過度簡化：某些其他定位系統亦可滿足條件，但必須正確配置。

## 來源與連結
- [[S03]]｜[Flight Modes](https://ardupilot.org/copter/docs/flight-modes.html)
- [[S04]]｜[Stabilize](https://ardupilot.org/copter/docs/stabilize-mode.html)
- [[S05]]｜[AltHold](https://ardupilot.org/copter/docs/altholdmode.html)
- [[S06]]｜[Loiter](https://ardupilot.org/copter/docs/loiter-mode.html)
- 相關：[[loiter-and-position]]
