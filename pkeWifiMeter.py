import pygame
import time
import os
import sys
from pygame.locals import *
from random import randint
from pkeWifiMeter_wirelessList import WirelessList
from pkeWifiMeter_hardware import Hardware

kPath = os.path.dirname(os.path.realpath(sys.argv[0]))

# initialize game engine
pygame.init()
pygame.mouse.set_visible(False)
pygame.screen = pygame.display.set_mode([480,272])
pygame.display.set_caption('PKE Wifi Meter')
# initialize clock. used later in the loop.
clock = pygame.time.Clock()

wifi = WirelessList()
hardware = Hardware()

pygame.bgImage = pygame.image.load(kPath+"/pke_background.gif").convert_alpha()
pygame.staticImage = pygame.image.load(kPath+"/pke_static.gif").convert()

pygame.font.init()

font = pygame.font.Font("256 bytes.ttf", 26)

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
		clock.tick(30)
		wifi.update()

		wifiName = wifi.getNearestDeviceName()
		if not wifiName:
			wifiName = "DEMO PIRATE LECHUCK"
			signal = "-69"
		else:
			hardware.update(wifi.getNearestDeviceStrength())
			signal = wifi.getNearestDeviceStrength()
	
		wifiText = font.render(wifiName, True, (0, 255, 0), (0, 0, 0))
		wifiTextrect = wifiText.get_rect()
		wifiTextrect.centerx = pygame.screen.get_rect().centerx
		wifiTextrect.centery = 215
		
		signalText = font.render(signal, True, (0, 255, 0), (0, 0, 0))
                signalTextrect = signalText.get_rect()
                signalTextrect.centerx = pygame.screen.get_rect().centerx
                signalTextrect.centery = 255

		pygame.screen.fill((0, 0, 0))
	        pygame.screen.blit(pygame.bgImage, (0,0))

		pygame.screen.blit(wifiText,wifiTextrect)
		pygame.screen.blit(signalText,signalTextrect)

		xflip = False

		if randint(0,1) == 1:
			xflip = True

		yflip = False

		if randint(0,1) == 1:
			yflip = True

		angle = 0
		if randint(0,1) == 1:
			angle = 180

       		static = pygame.transform.flip(pygame.staticImage, xflip, yflip)
		static = pygame.transform.rotate(static, angle)
		static.set_alpha(14)
		pygame.screen.blit(static, (0,0))

		pygame.display.flip()
	except:
		print "Unexpected error:", sys.exc_info()[0]
		done = True
 
wifi.shutdown()
hardware.shutdown()
# close the window and quit
pygame.quit()
