import psutil
import time
import os
from tkinter import messagebox

def warn_battery_percentage(warning_percent, shutting_percent, no_of_warning, waiting_time_in_sec):
    battery = psutil.sensors_battery()
    percent = battery.percent

    counter = 0
    if percent <= warning_percent and counter < no_of_warning:
        messagebox.showwarning("Battery Warning", "Battery is low! Please connect the charger.")

    if percent <= shutting_percent:
        time_in_seconds = waiting_time_in_sec
        messagebox.showinfo("Battery Warning", f"Computer will hibernate in {time_in_seconds//60} minutes.")
        hibernate_on_low_battery(time_in_seconds)

def hibernate_on_low_battery(time_in_seconds):
    time.sleep(time_in_seconds)  # Wait for 2 minutes
    os.system("shutdown /h")  # Hibernate the computer

def main():
    while True:
        warn_battery_percentage(40, 38, 2, 120)
        time.sleep(60)
        
if __name__ == "__main__":
    main()