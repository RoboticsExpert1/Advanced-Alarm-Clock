# 🤖 Robotics Experts : Alarm Clock

A clean and intuitive desktop alarm clock and timer application built with Python and Tkinter. It features a sleek dark-themed UI that allows users to set specific target times or custom minute-based countdowns with synchronized audio alerts.

## ✨ Key Features

* **Real-time Digital Clock:** High-precision time tracking synchronized using Tkinter's main event loop.
* **Dual Mode Setup:**
  * *Manual Alarm Mode:* Input a specific hour and minute. Automatically sets for the next day if the target time has already passed.
  * *Quick Timer Mode:* Enter a precise minute duration for immediate countdowns.
* **Dynamic Visual Feedback:** Live calculation showing the exact remaining time until the alarm triggers.
* **System Audio Integration:** Uses the native Windows `winsound` API to generate recurring beep alerts seamlessly without freezing the UI.
* **Smart Input Interlocking:** Automatically disables input fields and start buttons while an alarm is active to prevent configuration overrides.

## 🚀 Getting Started

### Prerequisites
* Windows OS (Required for `winsound` native audio API)
* Python 3.x

### Execution
```bash
run python Timer.py
