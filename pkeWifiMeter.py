import time
from pkeWifiMeter_wirelessList import WirelessList

wifi = WirelessList()
time.sleep(5)
wifi.update()
time.sleep(3)
wifi.update()
time.sleep(3)
wifi.update()
time.sleep(5)
wifi.update()
time.sleep(3)
wifi.shutdown()
