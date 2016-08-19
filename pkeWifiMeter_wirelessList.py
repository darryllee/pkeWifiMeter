import csv
import subprocess
import os
import signal
import sys
import glob
import time

class WirelessList:
	def __init__(self):
		self.nearestWifi = None
		self.nearestSignal = -100
		self.updateTime = time.time()
		subprocess.call(['sudo','ifconfig','wlan0','down'])
		subprocess.call(['sudo','ifconfig','wlan1','up'])
		subprocess.call(['sudo','iwconfig','wlan1','mode','monitor'])
		subprocess.call(['sudo rm pkeMeterLog*.csv > /dev/null 2>&1'],shell=True)
		self.pID = subprocess.Popen(['tshark -i wlan1 -T fields -e wlan_mgt.ssid -e radiotap.dbm_antsignal -E header=y -E separator="," -E quote=d -E occurrence=f > pkeMeterLog.csv'],shell=True)

	def shutdown(self):
		print( "Restoring wifi..." )
		os.kill(self.pID.pid, signal.SIGTSTP)
		#subprocess.call(['sudo rm pkeMeterLog*.csv > /dev/null 2>&1'],shell=True)
		subprocess.call(['sudo','ifconfig','wlan0','up'])
		subprocess.call(['sudo','ifconfig','wlan1','down'])
		subprocess.call(['sudo','iwconfig','wlan1','mode','managed'])

	def update(self):
		if( time.time() - self.updateTime >= 0.1 ):
			self.updateTime = time.time()
			filepath = "pkeMeterLog*.csv"
			files = glob.glob(filepath)
			for file in files:
				f = open(file, 'r')
				try:
    					reader = csv.reader(f)
					nearestSignal = -100
    					for row in reader:
						if row[1]:
							print row[0]
						
						#if len(row) == 15 and row[0] != "BSSID":
        					#	signal = int(row[8][1:])
						#	if signal > nearestSignal:
						#		nearestSignal = signal
						#		self.nearestSignal = signal
						#		self.nearestWifi = row[13][1:]
				finally:
    					f.close()

	def getNearestDeviceName(self):
		return self.nearestWifi

	def getNearestDeviceStrength(self):
		return self.nearestSignal

