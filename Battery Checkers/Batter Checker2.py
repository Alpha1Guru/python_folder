import psutil
import time
import os

def warn_battery_percentage():
    battery = psutil.sensors_battery()
    percent = battery.percent
    if percent >= 40:
        print("Warning: Battery percentage is at or above 40%")

def hibernate_on_low_battery():
    battery = psutil.sensors_battery()
    percent = battery.percent
    if percent <= 38:
        print("Warning: Battery percentage is low. The computer will hibernate in 2 minutes.")
        time.sleep(120 )  # Wait for 2 minutes
        os.system("shutdown /h")  # Hibernate the computer

def main():
    while True:
        warn_battery_percentage()
        hibernate_on_low_battery()
        time.sleep(60)  # Check battery percentage every minute

if __name__ == "__main__":
    main()