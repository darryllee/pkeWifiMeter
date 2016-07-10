import csv
import subprocess
import os
import sys
import glob
import time
import distutils.spawn

class WirelessList:
	def __init__(self):
		installed = distutils.spawn.find_executable('aircrack-ng')
		if not installed:
			subprocess.call(['sudo','apt-get','update'])
			subprocess.call(['sudo','apt-get','install','aircrack-ng','-y'])

		self.nearestWifi = None
		self.nearestSignal = -100
		self.updateTime = time.time()
		subprocess.call(['sudo','ifconfig','wlan0','down'])
		subprocess.call(['sudo','iwconfig','wlan1','mode','monitor'])
		subprocess.call(['sudo rm pkeMeterLog*.csv > /dev/null 2>&1'],shell=True)
		airodump = subprocess.Popen(['sudo airodump-ng wlan1 --write pkeMeterLog --write-interval 1 --output-format csv > /dev/null 2>&1'],shell=True)

	def shutdown(self):
		os.system('sudo pkill -9 airodump-ng')
		subprocess.call(['sudo rm pkeMeterLog*.csv > /dev/null 2>&1'],shell=True)

	def update(self):
		if( time.time() - self.updateTime > 0.5 ):
			self.updateTime = time.time()
			filepath = "pkeMeterLog*.csv"
			files = glob.glob(filepath)
			for file in files:
				f = open(file, 'r')
				try:
    					reader = csv.reader(f)
					nearestSignal = -100
    					for row in reader:
						if len(row) == 15 and row[0] != "BSSID":
        						signal = int(row[8][1:])
							if signal > nearestSignal:
								nearestSignal = signal
								self.nearestSignal = signal
								self.nearestWifi = row[13][1:]
				finally:
    					f.close()

	def getNearestDeviceName(self):
		return self.nearestWifi

	def getNearestDeviceStrength(self):
		return self.nearestSignal

