import pygame
import time
import os
import sys
from pygame.locals import *
from random import randint
from pkeWifiMeter_wirelessList import WirelessList
from pkeWifiMeter_hardware import Hardware

kPath = os.path.dirname(os.path.realpath(sys.argv[0]))

# Initialize PyGame display
pygame.init()
pygame.mouse.set_visible(False)
pygame.screen = pygame.display.set_mode([480,272])
pygame.display.set_caption('PKE Wifi Meter')

clock = pygame.time.Clock()
wifi = WirelessList()
hardware = Hardware()

# Load images
pygame.bgImage = pygame.image.load(kPath+"/pke_background.gif").convert_alpha()
pygame.staticImage = pygame.image.load(kPath+"/pke_static.gif").convert()

# Load fonts
pygame.font.init()
font = pygame.font.Font(kPath+"/256 bytes.ttf", 25)

pygame.manualControl = False
pygame.manualDirection = 0
pygame.manualValue = -50

def manualControl(dir):
	pygame.manualDirection = dir
	pygame.manualControl = True


def updateDisplay(wifiName,signal):
	# Add wifi name text
        wifiText = font.render(wifiName, True, (0, 255, 0), (0, 0, 0))
        wifiTextrect = wifiText.get_rect()
        wifiTextrect.centerx = pygame.screen.get_rect().centerx
        wifiTextrect.centery = 215

        # Add wifi signal strength test
        signalText = font.render(str(signal), True, (0, 255, 0), (0, 0, 0))
        signalTextrect = signalText.get_rect()
        signalTextrect.centerx = pygame.screen.get_rect().centerx
        signalTextrect.centery = 255

        pygame.screen.fill((0, 0, 0))
          
        # Animate static
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

        # Set opacity of static based on signal strength
        try:
                static.set_alpha((signal+25)*-4.25)
        except:
                static.set_alpha(50) # Not a valid number. Default value set

        # Draw images
        pygame.screen.blit(pygame.bgImage, (0,0))
        pygame.screen.blit(wifiText,wifiTextrect)
        pygame.screen.blit(signalText,signalTextrect)
        pygame.screen.blit(static, (0,0))

	# Update display
        pygame.display.flip()

# Loop until user quits
done = False
while done == False:
	try:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			elif event.type == KEYDOWN:
               			if event.key == K_ESCAPE:
					if pygame.manualControl == True:
						pygame.manualControl = False
					else:
	                   			done = True
				elif event.key == K_UP or event.key == K_RIGHT:
					manualControl(1)
				elif event.key == K_DOWN or event.key == K_LEFT:
					manualControl(-1)
			elif event.type == KEYUP:
				if event.key == K_UP or event.key == K_RIGHT or event.key == K_DOWN or event.key == K_LEFT:
					manualControl(0)
	except:
		done = True
	try:
		clock.tick(30) #update at 60 fps
		
		wifi.update()
		wifiName = wifi.getNearestDeviceName()
		
		# Adjust manual control, if currently active.
		if pygame.manualControl == True:
			if pygame.manualDirection == 1:
				pygame.manualValue = pygame.manualValue + 1.5
				if pygame.manualValue > -20:
					pygame.manualValue = -20
			elif pygame.manualDirection == -1:
				pygame.manualValue = pygame.manualValue - 1.5
				if pygame.manualValue < -50:
					pygame.manualValue = -50

			wifiName = "MANUAL CONTROL - PRESS ESC TO STOP"
			signal = int(pygame.manualValue)
			hardware.update(signal)
		elif not wifiName:
			wifiName = "AIN'T NO WIFI DETECTED"
			signal = "(wifi makes me feel good)"
		else:
			hardware.update(wifi.getNearestDeviceStrength())
			signal = wifi.getNearestDeviceStrength()

		updateDisplay(wifiName,signal)

	except:
		print "Unexpected error:", sys.exc_info()[0]
		done = True
 
# Quit application
wifi.shutdown()
hardware.shutdown()
pygame.quit()
