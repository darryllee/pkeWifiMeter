import pygame
import time
from pkeWifiMeter_wirelessList import WirelessList
from pkeWifiMeter_hardware import Hardware

# initialize game engine
pygame.init()
# set screen width/height and caption
size = [480, 272]
#screen = pygame.display.set_mode(size)
#pygame.display.set_caption('PKE Wifi Meter')
# initialize clock. used later in the loop.
clock = pygame.time.Clock()

wifi = WirelessList()
hardware = Hardware()

# Loop until the user clicks close button
done = False
while done == False:
	# write event handlers here
	try:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
	except:
		done = True

	try: 
		# clear the screen before drawing
		#screen.fill((255, 255, 255)) 

		# pygame.display.update()
    
		# fps
		clock.tick(60)
		wifi.update()	
		if wifi.getNearestDeviceName():
			print wifi.getNearestDeviceName()
			hardware.update(wifi.getNearestDeviceStrength())
	except:
		done = True
 
wifi.shutdown()
hardware.shutdown()
# close the window and quit
pygame.quit()
