#from ISO import *							#might not be needed - just for test
import time							#inherit movement through canvas
class Execute:				#will be executed by button in canvas - executin dictionary from process return
	def __init__(self, circle, canvasName, visual, ISO, movement, DB):		#execute will be checking for variable changed by stop button 
		self.visual = visual
		self.canvasName = canvasName
		self.Laser = False
		self.ISO = ISO
		self.movement = movement
		self.circle = circle
		self.state = 0
		self.DB = DB
		self.Traveled_range = 0

	def Exe_ISO(self, command):
		if 'G' in command:
			value = command['G']
			self.G(value)
			self.ISO.Add_count()

		if 'F' in command:
			value = command['F']
			self.F(value)
			self.ISO.Add_count()

		if 'Z' in command:
			value = command['Z']
			print(value)
			self.Z(value)
			self.ISO.Add_count()

		if 'X' in command or 'Y' in command:
			self.move_to_pos(float(command['X']), float(command['Y']))
			self.ISO.Add_count()

	def G(self, value):
		if value == 1:
			print("what now? :D")

	def F(self, feedrate):
		return (self.DB.change_feedrate(feedrate))

	def Z(self, state):
		self.state = int(state)
		if self.state == 10: #laser off
			self.Laser = False

		if self.state == 0: #laser on
			self.Laser = True

	def move_to_pos(self, x, y):
		SPM = self.DB.get_SPMM()
		ABS = self.movement.get_absolute_position()
		Ax = ABS['X']
		Ay = ABS['Y']		#position now
		Mx = x - Ax
		My = y - Ay			#mm to go in axis
		SNx = round(Mx * float(SPM))
		SNy = round(My * float(SPM)) 		#used for motor steps - check +/-	potreba zaokrouhlit
		DPSx = Mx / abs(SNx) if SNx is not 0 else 0
		DPSy = My / abs(SNy) if SNy is not 0 else 0		#distance per step for simulation
		StepsX = abs(SNx)
		StepsY = abs(SNy)
		range_prev = 0
		delay = self.movement.get_step_delay()
		timing = 0
		prevTime = 0
		ra = 0
		print (float(delay))
		
		if SNx == SNy:
			for r in range (SNx):
				#self.movement.reposition(DPSx, DPSy)
				if r - range_prev == 45:
					self.burn()
					range_prev = r
				timeNow = time.time()
				timing = timeNow - prevTime
				if timing >= delay:
					#run = False
					self.burn()
					self.movement.reposition(DPSx, DPSy)
					prevTime = timeNow
				else:
					r = r - 1

		if SNx == SNy:
			if self.Traveled_range < SNx:
				if self.Traveled_range - range_prev == 45:
					self.burn()
					range_prev = self.Traveled_range
				timeNow = time.time()
				timing = timeNow - prevTime
				if timing >= delay:
					self.movement.reposition(DPSx, DPSy)
					prevTime = timeNow
					self.Traveled_range += 1
					





		# else:
		# 	sideways_error = 0
		# 	sideways_variable = abs(SNx) / abs(SNy) if abs(SNy) > abs(SNx) else abs(SNy) / abs(SNx)
		# 	if StepsX > StepsY:
		# 		for r in range (StepsX):
		# 			timeNow = time.time()
		# 			timing = timeNow - prevTime
		# 			if timing >= delay:
		# 				self.movement.reposition(DPSx, 0)
		# 				sideways_error += sideways_variable
		# 				prevTime = timeNow
		# 				if r - range_prev == 45:
		# 					self.burn()
		# 					range_prev = r
		# 				if sideways_error >= 1:
		# 					self.movement.reposition(0, DPSy)
		# 					#self.burn()
		# 					sideways_error -= 1
		# 			else:
		# 				#r = r - 1
		# 				pass


		else:
			sideways_error = 0
			sideways_variable = abs(SNx) / abs(SNy) if abs(SNy) > abs(SNx) else abs(SNy) / abs(SNx)
			if StepsX > StepsY:
				while ra < StepsX:
					timeNow = time.time()
					timing = timeNow - prevTime
					print (delay)
					#print (timeNow)
					if timing >= delay:
						ra += 1
						self.movement.reposition(DPSx, 0)
						sideways_error += sideways_variable
						prevTime = timeNow
						if ra - range_prev == 45:
							self.burn()
							range_prev = ra
						if sideways_error >= 1:
							self.movement.reposition(0, DPSy)
							#self.burn()
							sideways_error -= 1


			elif StepsY > StepsX:
				for r in range (StepsY):
					self.movement.reposition(0, DPSy)
					sideways_error += sideways_variable
					if r - range_prev == 45:
						self.burn()
						range_prev = r
					if sideways_error >= 1:
						self.movement.reposition(DPSx, 0)
						#self.burn()
						sideways_error -= 1
			

	def count_steps(self, x, y):
		pos = self.movement.get_absolute_position()
		steps_x = x - pos['X']
		steps_y = y - pos['Y']

	def burn(self):				#will turn on laser
		if self.Laser == True:
			self.visual.draw(self.circle, self.canvasName, "red2")
		else:
			pass

	def get_Z(self):
		return(self.state)

	def idk(self):
		pass