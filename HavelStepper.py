import RPi.GPIO as GPIO
import datetime
import time

from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class TypeNotSupportedException(Exception):
	def __init__(self, msg):
		super().__init__(msg)

class NumberNotSupportedException(Exception):
	def __init__(self, msg):
		super().__init__(msg)

class Driver:
	def __init__(self, EN, STEP, DIR, MotorSteps):
		self.MStep = 1			#microsteps
		self.MinP = 0			#min position
		self.MaxP = 0			#max position
		self.Pstate = False
		self.steps = 0
		self.STEP = STEP
		self.EN = EN
		self.DIR = DIR
		self.MotorSteps = MotorSteps
		self.prevTime = 0
		self.runs = 0
		try:
			GPIO.setup(self.EN, GPIO.OUT)
		except:
			print("EN pin doesn't exist")
		try:
			GPIO.setup(self.STEP, GPIO.OUT)
		except:
			print("self.MStep pin doesn't exist")
		try:
			GPIO.setup(self.DIR, GPIO.OUT)
		except:
			print("DIR pin doesn't exist")
		GPIO.output(EN, GPIO.HIGH)

	def set_microsteps (self, MS1, MS2, MS3, MStep):	#set MS pins and MS value => 1; 2; 4; 8; 16
		if self.MStep is not 1 or 2 or 4 or 8 or 16:
			raise Exception ("self.MStep only takes values of 1; 2; 4; 8; 16. self.MStep:" + str(self.MStep))

		try:
			GPIO.setup(MS1, GPIO.OUT)
			GPIO.setup(MS2, GPIO.OUT)
			GPIO.setup(MS3, GPIO.OUT)
		except:
			print ("MS pin doesn't exist")

			if self.MStep == 1:
				GPIO.output(MS1, GPIO.LOW)
				GPIO.output(MS2, GPIO.LOW)
				GPIO.output(MS3, GPIO.LOW)
				self.self.MStep = 1

			elif self.MStep == 2:
				GPIO.output(MS1, GPIO.HIGH)
				GPIO.output(MS2, GPIO.LOW)
				GPIO.output(MS3, GPIO.LOW)
				self.self.MStep = 2

			elif self.MStep == 4:
				GPIO.output(MS1, GPIO.LOW)
				GPIO.output(MS2, GPIO.HIGH)
				GPIO.output(MS3, GPIO.LOW)
				self.self.MStep = 4

			elif self.MStep == 8:
				GPIO.output(MS1, GPIO.HIGH)
				GPIO.output(MS2, GPIO.HIGH)
				GPIO.output(MS3, GPIO.LOW)
				self.self.MStep = 8

			elif self.MStep == 16:
				GPIO.output(MS1, GPIO.HIGH)
				GPIO.output(MS2, GPIO.HIGH)
				GPIO.output(MS3, GPIO.HIGH)
				self.MStep = 16

	def get_MS(self):
		return (int(self.MStep))

	def set_minimum_position(self):
		print("minimum position set to" + str(self.steps))
		self.Pstate = True
		self.MinP = 0
		self.steps = 0

	def set_maximum_position(self):
		print("maximum position set to" + str(self.steps))
		self.MaxP = self.steps
		#self.Pstate = False
		print(self.MaxP)

	def count_steps(self, x):		#x +/-
		if self.Pstate == True:
			if x == True:
				self.steps += 1
			elif x == False:
				self.steps -= 1

	def get_steps(self):
		return (int(self.steps))

	def check_position_active(self):
		if self.MaxP is not 0:
			return (True)
		else:
			return (False)

	def check_position(self, x):
		if self.check_position_active():
			if (x == True) and (self.MinP <= self.steps <= self.MaxP):
				if self.steps == self.MaxP:
					print(str(self.steps) + "  " + str(self.MaxP))
					print("1")
					return(False)
				else:
					print("2")
					return(True)
			elif (x == False) and (self.MinP <= self.steps <= self.MaxP):
				if self.steps == self.MinP:
					print("3")
					return(False)
				else:
					print("4")
					return(True)
			else:
				print("something went wrong!")
		else:
			return(True)

	#def check_position(self):
	#	if self.check_position_active():
	#		if (self.steps > self.MinP) and (self.steps < self.MaxP):
	#			print ("cajk")
	#			return(True)
	#		else:
	#			print("necajk")
	#			return(False)
	#	else:
	#		return(True)
	
	#SPIN - INTERUPTION

	def turn_clockwise_interupt (self, Turns, speed):		#stops flow of program until makes certain nubmer of turns
		if speed <= 0:
			raise NumberNotSupportedException("Speed not defined as positive number. Speed:" + str(speed))
		elif type (speed) is not int:
			raise TypeNotSupportedException("Speed not defined as type int. Speed type:" + type(speed))
		if Turns <= 0:
			raise NumberNotSupportedException("Turns not defined as positive number. Turns:" + str(Turns))
		elif type (Turns) is not int and type (Turns) is not float:
			raise TypeNotSupportedException("Turns not defined as type int or float. Turns type:")
		if self.check_position(True):
			print("check CW")
			V = speed * 0.001
			T = Turns * self.MotorSteps * self.get_MS()
			T = int(T)
			GPIO.output(self.DIR, GPIO.LOW)
			for x in range(T):
				if self.check_position(True):
					self.count_steps(True)
					GPIO.output(self.STEP, GPIO.HIGH)
					time.sleep(V)
					GPIO.output(self.STEP, GPIO.LOW)
					time.sleep(V)
					print(self.steps)
				else:
					print("out of range")
					break
		else:
			pass

	def turn_counterclockwise_interupt (self, Turns, speed):		#stops flow of program until makes certain nubmer of turns
		if speed <= 0:
			raise NumberNotSupportedException("Speed not defined as positive number. Speed:" + str(speed))
		elif type (speed) is not int:
			raise TypeNotSupportedException("Speed not defined as type int. Speed type:" + type(speed))
		if Turns <= 0:
			raise NumberNotSupportedException("Turns not defined as positive number. Turns:" + str(Turns))
		elif type (Turns) is not int and type (Turns) is not float:
			raise TypeNotSupportedException("Turns not defined as type int or float. Turns type:")
		if self.check_position(False):
			V = speed * 0.001
			T = Turns * self.MotorSteps * self.get_MS()
			T = int(T)
			GPIO.output(self.DIR, GPIO.HIGH)
			for x in range(T):
				if self.check_position(False):
					self.count_steps(False)
					GPIO.output(self.STEP, GPIO.HIGH)
					time.sleep(V)
					GPIO.output(self.STEP, GPIO.LOW)
					time.sleep(V)
					print(self.steps)
				else:
					print("out of range")
					break
		else:
			pass

	#RUN UNTIL..

	def step_by_step (self, speed, DIR):
		if speed <= 0:
			raise NumberNotSupportedException("Speed can only be defined as positive number. Speed:" + str(speed))
		elif type (speed) is not int:
			raise TypeNotSupportedException("Speed not defined as type int. Speed type:" + type(speed))
		#if (DIR is not 0 or DIR is not 1) and (DIR is not True or DIR is not False):
		#	raise NumberNotSupportedException("Direction can only be defined as 0 or 1 (True/False). DIR:" + str(DIR))
		#elif type (DIR) is not int and type (DIR) is not bool:
		#	raise TypeNotSupportedException("Direction not defined as type int or bool. DIR type:" + type(DIR))
		checkDIR = False
		if DIR == 0:
			checkDIR = True
		elif DIR == 1:
			checkDIR = False
		if self.check_position(checkDIR):
			V = speed
			x = time.time()
			timeNow = x * 1000
			timing = timeNow - self.prevTime
			#print(timing)
			if timing >= V:
				if DIR == 0:
					GPIO.output(self.DIR, GPIO.LOW)
					self.count_steps(True)
				elif DIR == 1:
					GPIO.output(self.DIR, GPIO.HIGH)
					self.count_steps(False)
				GPIO.output(self.STEP, GPIO.HIGH)
				self.prevTime = timeNow
			if timing >= V:
				GPIO.output(self.STEP, GPIO.LOW)
				self.prevTime = timeNow
				print(self.steps)
		else:
			pass

	#SPIN - NO INTERUPTION
	#!!!!problem s opakovanim!!!!

	def turn_stop_clockwise (self, Turns, speed, Pause):
		if Pause <= 0:
			raise NumberNotSupportedException("Pause not defined as positive number. Pause:" + str(Pause))
		elif type (Pause) is not int and type (Pause) is not float:
			raise TypeNotSupportedException("Pause not defined as type int or float. Pause type:" + type(Pause))
		if speed <= 0:
			raise NumberNotSupportedException("Speed not defined as positive number. Speed:" + str(speed))
		elif type (speed) is not int:
			raise TypeNotSupportedException("Speed not defined as type int. Speed type:" + type(speed))
		if Turns <= 0:
			raise NumberNotSupportedException("Turns not defined as positive number. Turns:" + str(Turns))
		elif type (Turns) is not int and type (Turns) is not float:
			raise TypeNotSupportedException("Turns not defined as type int or float. Turns type:" + type(Turns))
		if self.check_position(True):	
			V = speed
			T = Turns * self.MotorSteps * self.get_MS()
			T = int(T)
			GPIO.output(self.DIR, GPIO.LOW)
			x = time.time()
			timeNow = x * 1000
			timing = timeNow - self.prevTime
			P = Pause
			P = int(P)
			if self.runs < T:
				self.count_steps(True)
				if timing >= V:
					GPIO.output(self.STEP, GPIO.HIGH)
					self.prevTime = timeNow
				if timing >= V:
					GPIO.output(self.STEP, GPIO.LOW)
					self.prevTime = timeNow
					self.runs += 1
			elif self.runs == T and timing >= P:
				self.runs = 0
		else:
			pass

	def turn_stop_counterclockwise (self, Turns, speed, Pause):
		if Pause <= 0:
			raise NumberNotSupportedException("Pause not defined as positive number. Pause:" + str(Pause))
		elif type (Pause) is not int and type (Pause) is not float:
			raise TypeNotSupportedException("Pause not defined as type int or float. Pause type:" + type(Pause))
		if speed <= 0:
			raise NumberNotSupportedException("Speed not defined as positive number. Speed:" + str(speed))
		elif type (speed) is not int:
			raise TypeNotSupportedException("Speed not defined as type int. Speed type:" + type(speed))
		if Turns <= 0:
			raise NumberNotSupportedException("Turns not defined as positive number. Turns:" + str(Turns))
		elif type (Turns) is not int and type (Turns) is not float:
			raise TypeNotSupportedException("Turns not defined as type int or float. Turns type:" + type(Turns))
		if self.check_position(False):	
			V = speed
			T = Turns * self.MotorSteps * self.get_MS()
			T = int(T)
			GPIO.output(self.DIR, GPIO.HIGH)
			x = time.time()
			timeNow = x * 1000
			timing = timeNow - self.prevTime
			P = Pause
			P = int(P)
			if self.runs < T:
				self.count_steps(False)
				if timing >= V:
					GPIO.output(self.STEP, GPIO.HIGH)
					self.prevTime = timeNow
				if timing >= V:
					GPIO.output(self.STEP, GPIO.LOW)
					self.prevTime = timeNow
					self.runs += 1
			elif self.runs == T and timing >= P:
				self.runs = 0
		else:
			pass