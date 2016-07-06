import csv
import subprocess
import os

Class WirelessList:
	def __init__(self):
		print "hi!"
		airodump = subprocess.Popen(['sudo airodump-ng wlan1 -w pkeMeterLog --output-format csv > /dev/null 2>&1'],shell=True)

	def shutdown():
		os.system('sudo pkill -9 airodump-ng')

	def getNearestDeviceName():
		print "hi!"

	def getNearestDeviceStrength():
		print "HI!"

