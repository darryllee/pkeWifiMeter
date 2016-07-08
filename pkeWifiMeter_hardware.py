import Adafruit_PCA9685


class Hardware:
	def __init__(self):
		#pwm = Adafruit_PCA9685.PCA9685()
		print "HARDWaRE INIT!"

	def shutdown(self):
		print "HARDWARE SHUTDOWN"

	def updateServo(self,signal):
		print signal

	def update(self,signal):
		self.updateServo(((signal + 20)*10)/-40)
