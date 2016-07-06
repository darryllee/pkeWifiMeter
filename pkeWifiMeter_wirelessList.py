import csv
import subprocess
import os
import sys
import glob

class WirelessList:
	def __init__(self):
		print "hi!"
		subprocess.call(['sudo rm pkeMeterLog*.csv > /dev/null 2>&1'],shell=True)
		airodump = subprocess.Popen(['sudo airodump-ng wlan1 -w pkeMeterLog --output-format csv > /dev/null 2>&1'],shell=True)

	def shutdown(self):
		os.system('sudo pkill -9 airodump-ng')
		#subprocess.call(['sudo rm pkeMeterLog*.csv > /dev/null 2>&1'],shell=True)

	def update(self):
		filepath = "pkeMeterLog*.csv"
		files = glob.glob(filepath)
		for file in files:
			print file
			f = open(file, 'r')
			print f
			try:
    				reader = csv.reader(f)
    				for row in reader:
        				print row
			finally:
    				f.close()

	def getNearestDeviceName(self):
		print "hi!"

	def getNearestDeviceStrength(self):
		print "HI!"

