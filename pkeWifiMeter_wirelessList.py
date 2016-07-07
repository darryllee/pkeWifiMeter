import csv
import subprocess
import os
import sys
import glob

class WirelessList:
	def __init__(self):
		print "hi!"
		self.nearestWifi = None
		self.nearestSignal = -100
		subprocess.call(['sudo rm pkeMeterLog*.csv > /dev/null 2>&1'],shell=True)
		airodump = subprocess.Popen(['sudo airodump-ng wlan1 -w pkeMeterLog --output-format csv > /dev/null 2>&1'],shell=True)

	def shutdown(self):
		os.system('sudo pkill -9 airodump-ng')
		subprocess.call(['sudo rm pkeMeterLog*.csv > /dev/null 2>&1'],shell=True)

	def update(self):
		filepath = "pkeMeterLog*.csv"
		files = glob.glob(filepath)
		for file in files:
			f = open(file, 'r')
			try:
    				reader = csv.reader(f)
    				for row in reader:
					if len(row) == 15 and row[0] != "BSSID":
        					signal = int(row[8][1:])
						if signal > self.nearestSignal:
							self.nearestSignal = signal
							self.nearestWifi = row[13][1:]
							print self.nearestWifi
							print self.nearestSignal
			finally:
    				f.close()

	def getNearestDeviceName(self):
		return self.nearestWifi

	def getNearestDeviceStrength(self):
		return self.nearestSignal

