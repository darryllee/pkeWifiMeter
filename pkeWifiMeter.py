import time
from pkeWifiMeter_wirelessList import WirelessList

wifi = WirelessList()
time.sleep(1)
wifi.update()
time.sleep(1)
wifi.shutdown()
