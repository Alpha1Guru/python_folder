import psutil
import time
import subprocess

def check_battery_level():
    battery = psutil.sensors_battery()
    if battery.percent <= 37:
        print("Warning: Battery level critical. Computer will hibernate in 5 minutes.")
        time.sleep(300)  # Wait for 5 minutes before hibernating
        subprocess.call("shutdown /h")  # Hibernate the computer

while True:
    check_battery_level()
    time.sleep(60)  # Check battery level every 1 minute