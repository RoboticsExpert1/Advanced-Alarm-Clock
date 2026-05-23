import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
import winsound

# -------------------------------------------------
# Global Variables
# -------------------------------------------------
alarm_time = None
alarm_active = False
alarm_ringing = False

# -------------------------------------------------
# Update Clock
# -------------------------------------------------
def update_clock():

    global alarm_ringing

    now = datetime.now()

    # Display current time
    clock_label.config(
        text=now.strftime("%H:%M:%S")
    )

    # Alarm active status
    if alarm_active and alarm_time:

        remaining_seconds = int(
            (alarm_time - now).total_seconds()
        )

        # Display remaining time
        if remaining_seconds > 0:

            hours = remaining_seconds // 3600
            minutes = (remaining_seconds % 3600) // 60
            seconds = remaining_seconds % 60

            remain_label.config(
                text=f"Time Left⏱️ {hours:02}:{minutes:02}:{seconds:02}"
            )

        else:

            remain_label.config(
                text="⏰ Alarm Time!"
            )

            if not alarm_ringing:
                alarm_ringing = True
                ring_alarm()

                # Unlock input fields
                unlock_inputs()

    root.after(200, update_clock)

# -------------------------------------------------
# Repeat Alarm Sound
# -------------------------------------------------
def ring_alarm():

    if alarm_ringing:
        winsound.Beep(1200, 700)
        root.after(900, ring_alarm)

# -------------------------------------------------
# Lock Inputs
# -------------------------------------------------
def lock_inputs():

    hour_entry.config(state="disabled")
    minute_entry.config(state="disabled")
    start_button.config(state="disabled")

    timer_entry.config(state="disabled")
    timer_button.config(state="disabled")

# -------------------------------------------------
# Unlock Inputs
# -------------------------------------------------
def unlock_inputs():

    hour_entry.config(state="normal")
    minute_entry.config(state="normal")
    start_button.config(state="normal")

    timer_entry.config(state="normal")
    timer_button.config(state="normal")

# -------------------------------------------------
# Common Alarm Activation Function
# -------------------------------------------------
def activate_alarm(target):

    global alarm_time
    global alarm_active
    global alarm_ringing

    alarm_time = target
    alarm_active = True
    alarm_ringing = False

    status_label.config(
        text=f"Target Time : {target.strftime('%H:%M:%S')}"
    )

    lock_inputs()

# -------------------------------------------------
# Set Alarm Time Manually
# -------------------------------------------------
def start_alarm():

    try:

        hour = int(hour_entry.get())
        minute = int(minute_entry.get())

        if not (0 <= hour <= 23):
            raise ValueError

        if not (0 <= minute <= 59):
            raise ValueError

        now = datetime.now()

        target = now.replace(
            hour=hour,
            minute=minute,
            second=0,
            microsecond=0
        )

        # If the time has already passed, set for the next day
        if target <= now:
            target += timedelta(days=1)

        activate_alarm(target)

    except:
        messagebox.showerror(
            "Error",
            "Please check the time input."
        )

# -------------------------------------------------
# Timer (N Minutes Later)
# -------------------------------------------------
def start_timer():

    try:

        minutes = int(timer_entry.get())

        if minutes <= 0:
            raise ValueError

        target = datetime.now() + timedelta(minutes=minutes)

        activate_alarm(target)

    except:
        messagebox.showerror(
            "Error",
            "Please enter a valid number of minutes."
        )

# -------------------------------------------------
# Stop Alarm
# -------------------------------------------------
def stop_alarm():

    global alarm_active
    global alarm_ringing
    global alarm_time

    alarm_active = False
    alarm_ringing = False
    alarm_time = None

    remain_label.config(text="")
    status_label.config(text="No Alarm")

    unlock_inputs()

# -------------------------------------------------
# GUI Setup
# -------------------------------------------------
root = tk.Tk()

root.title("Alarm Clock")
root.geometry("1280x720")
root.configure(bg="#111111")

# -------------------------------------------------
# Laboratory Name
# -------------------------------------------------
title_label = tk.Label(
    root,
    text="LEE SUCHEOL Robotics Lab",
    font=("Arial", 24, "bold"),
    fg="white",
    bg="#111111"
)
title_label.pack(pady=10)

# -------------------------------------------------
# Current Time
# -------------------------------------------------
clock_label = tk.Label(
    root,
    text="00:00:00",
    font=("Arial", 80, "bold"),
    fg="cyan",
    bg="#111111"
)
clock_label.pack(pady=20)

# -------------------------------------------------
# Manual Alarm Setting Area
# -------------------------------------------------
manual_frame = tk.Frame(root, bg="#111111")
manual_frame.pack(pady=15)

hour_entry = tk.Entry(
    manual_frame,
    font=("Arial", 36),
    width=3,
    justify="center"
)
hour_entry.pack(side="left", padx=5)
hour_entry.insert(0, "12")

colon = tk.Label(
    manual_frame,
    text=":",
    font=("Arial", 40, "bold"),
    fg="white",
    bg="#111111"
)
colon.pack(side="left")

minute_entry = tk.Entry(
    manual_frame,
    font=("Arial", 36),
    width=3,
    justify="center"
)
minute_entry.pack(side="left", padx=5)
minute_entry.insert(0, "00")

start_button = tk.Button(
    manual_frame,
    text="Start Alarm",
    font=("Arial", 24, "bold"),
    bg="#008800",
    fg="white",
    command=start_alarm
)
start_button.pack(side="left", padx=25)

# -------------------------------------------------
# Timer Area
# -------------------------------------------------
timer_frame = tk.Frame(root, bg="#111111")
timer_frame.pack(pady=20)

timer_entry = tk.Entry(
    timer_frame,
    font=("Arial", 32),
    width=5,
    justify="center"
)
timer_entry.pack(side="left", padx=10)
timer_entry.insert(0, "30")

timer_text = tk.Label(
    timer_frame,
    text="Min Later",
    font=("Arial", 28, "bold"),
    fg="white",
    bg="#111111"
)
timer_text.pack(side="left")

timer_button = tk.Button(
    timer_frame,
    text="Start Timer",
    font=("Arial", 24, "bold"),
    bg="#0055aa",
    fg="white",
    command=start_timer
)
timer_button.pack(side="left", padx=25)

# -------------------------------------------------
# Stop Button
# -------------------------------------------------
stop_button = tk.Button(
    root,
    text="Stop Alarm",
    font=("Arial", 23, "bold"),
    bg="#aa0000",
    fg="white",
    width=15,
    height=1,
    command=stop_alarm
)
stop_button.pack(pady=17)

# -------------------------------------------------
# Status Display
# -------------------------------------------------
status_label = tk.Label(
    root,
    text="No Alarm",
    font=("Arial", 23),
    fg="white",
    bg="#111111"
)
status_label.pack(pady=8)

# -------------------------------------------------
# Remaining Time
# -------------------------------------------------
remain_label = tk.Label(
    root,
    text="",
    font=("Arial", 60, "bold"),
    fg="yellow",
    bg="#111111"
)
remain_label.pack(pady=30)

# -------------------------------------------------
# Execution
# -------------------------------------------------
update_clock()

root.mainloop()