# Pre-Arm 安全檢查入門

## 核心概念
Pre-Arm（解鎖前檢查）用於發現校正、配置或感測器狀態異常，在問題解決前阻止解鎖。可使用地面站讀取完整錯誤訊息，再依據官方文件查核原因。

## 初學者例子
若地面站出現 Pre-Arm 問題，應先保留完整原始訊息並確認對應硬體／韌體設定，不直接猜想是哪顆感測器故障。

例如 `3D Accel calibration needed` 對應加速度計尚未校正。用完整訊息在錯誤表對照原因與處理欄。[[S07]]

## 常見誤解
「停用安全檢查就代表問題解決」是錯誤的；教學不提供將其用於實際飛行的繞過建議。

## 來源與連結
- [[S07]]｜[Pre-Arm Safety Checks](https://ardupilot.org/copter/docs/common-prearm-safety-checks.html)
- 相關：[[sensors-and-ekf]]、[[flight-modes]]
