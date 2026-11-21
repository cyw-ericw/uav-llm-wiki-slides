# 飛行系統的角色分工

## 核心概念
**Pixhawk（飛行控制器硬體）**與 **ArduPilot（飛控韌體）**不是同一個東西。Pixhawk 提供運算與感測器介面，飛控韌體負責飛行控制邏輯。Holybro 表示 Pixhawk 6C 出廠預裝 PX4；是否改用 ArduPilot，需要看使用者安裝的韌體與硬體支援。

規格表將內建感測器和周邊介面分列。遙測、GPS（全球定位系統）、遙控輸入都是介面例子。[[S02]] 飛行模式的行為請接著查 Copter 說明。[[S03]]

## 初學者例子
就像電腦硬體與作業系統是不同層次；不能只看到 Pixhawk 名稱就推斷韌體必然是 PX4 或 ArduPilot。

## 常見誤解
「Pixhawk 就是 ArduPilot」是不正確的等號。

## 來源與連結
- [[S01]]｜[Holybro Overview](https://docs.holybro.com/autopilot/pixhawk-6c/overview)
- [[S02]]｜[Holybro Technical Specification](https://docs.holybro.com/autopilot/pixhawk-6c/technical-specification)
- [[S03]]｜[Copter Flight Modes](https://ardupilot.org/copter/docs/flight-modes.html)
- 相關：[[sensors-and-ekf]]
