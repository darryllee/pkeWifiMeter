import pygame
import time
import os
import sys
from pkeWifiMeter_wirelessList import WirelessList
from pkeWifiMeter_hardware import Hardware

kPath = os.path.dirname(os.path.realpath(sys.argv[0]))

# initialize game engine
pygame.init()
# set screen width/height and caption
size = [480, 272]
pygame.screen = pygame.display.set_mode(size)
pygame.display.set_caption('PKE Wifi Meter')
pygame.mouse.set_visible(False)
# initialize clock. used later in the loop.
clock = pygame.time.Clock()

wifi = WirelessList()
hardware = Hardware()

pygame.bgImage = pygame.image.load(kPath+"/pke_background.gif").convert_alpha()
pygame.staticImage = pygame.image.load(kPath+"/pke_static.gif").convert_alpha()

# Loop until the user clicks close button
done = False
while done == False:
	# Event handlers here
	try:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			#elif event.type == KEYDOWN:
               	#		if event.key == K_ESCAPE:
                #   			done = True
	except:
		done = True

	try: 
		# clear the screen before drawing
		
		# fps
		clock.tick(60)
		wifi.update()
		
		pygame.screen.fill((0, 0, 0))
	        pygame.screen.blit(pygame.bgImage, (0,0))

		#pygame.staticImage.set_alpha(10)

		#pygame.screen.blit(pygame.staticImage, (0,0))
		pygame.display.flip()

		if wifi.getNearestDeviceName():
			#print wifi.getNearestDeviceName()
			#print wifi.getNearestDeviceStrength()
			hardware.update(wifi.getNearestDeviceStrength())
	except:
		done = True
 
wifi.shutdown()
hardware.shutdown()
# close the window and quit
pygame.quit()
