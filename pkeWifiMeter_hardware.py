import Adafruit_PCA9685
import array
import time

class Hardware:
	def __init__(self):
		try:
			self.pwm = Adafruit_PCA9685.PCA9685(address=0x40, busnum=2)
			self.pwm.set_pwm_freq(60)
		except:
			self.pwm = None

		self.updateTime = time
		self.ledCurSpeed = 1
		self.ledNewSpeed = 1
		self.activeLED = 0
		self.totalLEDs = 7
		self.ledPWMvalues = []

		for i in range(self.totalLEDs):
			self.ledPWMvalues.append(0)

		self.updateTime = time.time()
		#self.pwm.set_pwm(8, 0, 2624)

	def shutdown(self):
		if self.pwm:
			self.pwm.set_pwm(0, 0, 0)

	def updateLEDs(self,signal):
		for i in range(0,self.totalLEDs):
			if i == self.activeLED-1:
				self.ledPWMvalues[i] = self.ledPWMvalues[i]+600
				if self.ledPWMvalues[i] > 4000:
					self.ledPWMvalues[i] = 4000
			else:
				self.ledPWMvalues[i] = self.ledPWMvalues[i]-600
			 	if self.ledPWMvalues[i] < 0:
                                        self.ledPWMvalues[i] = 0
			if self.pwm:
				self.pwm.set_pwm(i+1, 0, self.ledPWMvalues[i])
		
		self.ledNewSpeed = (signal*.007)*-1

		if( self.ledCurSpeed < self.ledNewSpeed ):
			self.ledCurSpeed = self.ledCurSpeed + 0.01
		elif( self.ledCurSpeed > self.ledNewSpeed ):
			self.ledCurSpeed = self.ledCurSpeed - 0.01

		if time.time() - self.updateTime > self.ledCurSpeed:
			self.updateTime = time.time()
			self.activeLED = self.activeLED + 1
			if self.activeLED > self.totalLEDs:
				self.activeLED = 1

	def updateServo(self,signal):
		if self.pwm:
			self.pwm.set_pwm(0, 0, 10-(signal*100))
			#self.set_servo_pulse(0,700)

	def update(self,signal):
		signal = -50
		self.updateServo(((signal + 20)*-10)/-40)
		self.updateLEDs(signal)
