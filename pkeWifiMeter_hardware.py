import Adafruit_PCA9685

class Hardware:
	def __init__(self):
		self.pwm = Adafruit_PCA9685.PCA9685(address=0x40, busnum=2)
		self.pwm.set_pwm_freq(60)
		print "HARDWaRE INIT!"

	def shutdown(self):
		self.pwm.set_pwm(0, 0, 0)
		print "HARDWARE SHUTDOWN"

	def set_servo_pulse(self, channel, pulse):
		pulse_length = 1000000    # 1,000,000 us per second
    		pulse_length //= 60       # 60 Hz
		pulse_length //= 4096     # 12 bits of resolution
		pulse *= 1000
		pulse //= pulse_length
		self.pwm.set_pwm(channel, 0, pulse)

	def updateServo(self,signal):
		self.pwm.set_pwm(0, 0, 10-(signal*100))

	def update(self,signal):
		self.updateServo(((signal + 20)*-10)/-40)
