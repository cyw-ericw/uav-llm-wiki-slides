# 感測器與狀態估測

## 核心概念
IMU（慣性量測單元）可包含加速度計和陀螺儀；磁力計與氣壓計提供其他量測資訊。Pixhawk 6C 規格列有不同型式的內建感測器。EKF（擴展卡爾曼濾波器）用於融合感測器資訊進行狀態估測；ArduPilot 的 EKF3 可選擇位置、速度、高度及航向來源。

Holybro 把標準版與新版的加速度計／陀螺儀分列，應依版本讀規格。[[S02]] 在 EKF3 中，氣壓計是預設垂直位置來源，羅盤通常是預設航向來源。光流可提供水平速度，這個配置的水平位置是相對的。[[S08]]

## 初學者例子
陀螺儀量測角速度，氣壓計可協助推估高度；並不能直接由單一 IMU 量測保證精確的全球位置。

## 常見誤解
「有 IMU 就能穩定知道無人機在哪裡」不成立；估測方法仍受感測器配置與誤差影響。

## 來源與連結
- [[S02]]｜[Holybro Sensors](https://docs.holybro.com/autopilot/pixhawk-6c/technical-specification)
- [[S08]]｜[EKF Source Selection](https://ardupilot.org/copter/docs/common-ekf-sources.html)
- 相關：[[loiter-and-position]]
