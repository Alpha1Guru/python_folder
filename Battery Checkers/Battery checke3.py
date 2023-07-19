import psutil
import time
import tkinter as tk
from tkinter import messagebox


def check_battery():
    battery = psutil.sensors_battery()
    percent = battery.percent

    if percent <= 40:
        messagebox.showwarning("Battery Warning", "Battery is low! Please connect the charger.")

    if percent <= 37:
        messagebox.showinfo("Battery Warning", "Computer will hibernate in 5 minutes.")
        time.sleep(300)  # Wait for 5 minutes before hibernating
        hibernate()


def hibernate():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    root.call('wm', 'attributes', '.', '-topmost', '1')  # Set the window to be always on top
    root.after(1000, lambda: root.destroy())  # Close the window after 1 second
    root.mainloop()
    # Execute hibernation command here


while True:
    check_battery()
    time.sleep(60)
