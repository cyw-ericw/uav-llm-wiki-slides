# 無 GPS 時的 Loiter 與位置資訊

## 核心概念
Loiter 嘗試保持位置、航向及高度。ArduPilot 的說明以 GPS 取得定位為常見情況，也明確提及 Optical Flow 與其他 Non-GPS Navigation 來源，在有效位置資訊、EKF 原點及適當配置下可能支援室內定點。

## 初學者例子
室內配置若使用光流提供水平速度，仍須有可用的位置估測；官方例子另要求經地面站設定估測原點。[[S03]] [[S06]] [[S08]]

## 常見誤解
- 「無 GPS 就一定不能用 Loiter」：過度絕對化。
- 「沒有 GPS 就能直接切 Loiter」：也不對；仍需可靠位置估測、正確參數及驗證。

## 來源與連結
- [[S06]]｜[Loiter Mode](https://ardupilot.org/copter/docs/loiter-mode.html)
- [[S08]]｜[EKF Source Selection](https://ardupilot.org/copter/docs/common-ekf-sources.html)
- [[S03]]｜[Flight Modes](https://ardupilot.org/copter/docs/flight-modes.html)
- 相關：[[flight-modes]]、[[sensors-and-ekf]]
