import csv
import subprocess
import os
import time

airodump = subprocess.Popen(['sudo airodump-ng wlan1 -w pkeMeterLog --output-format csv > /dev/null 2>&1'],shell=True)
time.sleep(5)
os.system('sudo pkill -9 airodump-ng')
airodump=None
