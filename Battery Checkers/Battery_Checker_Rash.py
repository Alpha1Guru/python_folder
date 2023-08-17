import psutil
import time
import subprocess

def check_battery_level():
    battery = psutil.sensors_battery()
    if battery.percent <= 37:
        subprocess.call("shutdown /h")  # Hibernate the computer

while True:
    check_battery_level()
    time.sleep(5)  # Check battery level every 1 minute