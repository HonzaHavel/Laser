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
		self.sideways_error = 0
		self.range_prev = 0
		self.loops = 0
		self.prevLoop = 0
		self.StepsX = 0
		self.StepsY = 0
		self.DPSx = 0
		self.DPSy = 0
		self.total_range = 0
		self.line_points = []
		self.StoreValue = False
		self.old_state = 0
		self.correction_x = 0
		self.correction_y = 0

	def Exe_ISO(self, command):
		if 'G' in command:
			value = command['G']
			self.G(value)
			self.ready_for_next_CMD()

		if 'F' in command:
			value = command['F']
			self.F(value)
			self.ready_for_next_CMD()

		if 'Z' in command:
			value = command['Z']
			self.Z(value)
			self.ready_for_next_CMD()

		if 'X' in command or 'Y' in command:
			x = float(float(command['X']) + self.correction_x)
			y = float(float(command['Y']) + self.correction_y)
			self.move_to_pos(x, y)
			# self.move_to_pos(float(command['X']), float(command['Y']))
			#self.ISO.Add_count()

	def G(self, value):
		if value == 1:
			print("what now? :D")

	def F(self, feedrate):
		return (self.DB.change_feedrate(feedrate))

	def Z(self, state): #send output for laser start here
		self.old_state = self.state
		self.state = int(state)
		self.Laser = True if int(state) == 10 else False

		if self.state == 20: #reverse value
			if self.old_state == 10:
				self.state = 0
			elif self.old_state == 0:
				self.state = 10

		if self.state == 0:
			pos = self.movement.get_absolute_position()
			self.visual.set_start(pos["X"], pos["Y"])

		elif self.state == 10:
			self.visual.end_line()
		print(self.state)

	def move_to_pos(self, x, y):
		SPM = self.DB.get_SPMM()
		if self.Traveled_range == 0:
			ABS = self.movement.get_absolute_position()
			Ax = ABS['X']
			Ay = ABS['Y']		#position now
			Mx = x - Ax
			My = y - Ay			#mm to go in axis
			SNx = round(Mx * float(SPM))
			SNy = round(My * float(SPM)) 		#used for motor steps - check +/-	potreba zaokrouhlit
			self.DPSx = Mx / abs(SNx) if SNx is not 0 else 0
			self.DPSy = My / abs(SNy) if SNy is not 0 else 0		#distance per step for simulation
			self.StepsX = abs(SNx)
			self.StepsY = abs(SNy)
		delay = self.movement.get_step_delay()
		#print(delay)
		timing = 0
		prevTime = 0
		if self.StepsY != 0 and self.StepsX != 0:
			sideways_variable = self.StepsX / self.StepsY if self.StepsY > self.StepsX else self.StepsY / self.StepsX
		else:
			sideways_variable = 0

		timeNow = time.time()
		timing = timeNow - prevTime
		if timing >= delay:
			prevTime == timeNow
			if self.StepsX == self.StepsY:
				if self.Traveled_range < self.StepsX:
					self.movement.reposition(self.DPSx, self.DPSy)
					self.Traveled_range += 1
					self.total_range += 1
				else:
					self.ready_for_next_CMD()

			elif self.StepsX > self.StepsY:
				if self.Traveled_range < self.StepsX:
					self.movement.reposition(self.DPSx, 0)
					self.Traveled_range += 1
					self.total_range += 1
					self.sideways_error += sideways_variable
					if self.sideways_error >= 1:
						self.movement.reposition(0, self.DPSy)
						self.sideways_error -= 1
				else:
					self.ready_for_next_CMD()

			elif self.StepsX < self.StepsY:
				if self.Traveled_range < self.StepsY:
					self.movement.reposition(0, self.DPSy)
					self.Traveled_range += 1
					self.total_range += 1
					self.sideways_error += sideways_variable
					if self.sideways_error >= 1:
						self.movement.reposition(self.DPSx, 0)
						self.sideways_error -= 1
				else:
					self.ready_for_next_CMD()

			else:
				print("MOVEMENT ERROR")


		# print ("total", self.total_range)
		# print ("prev", self.range_prev)
		# if self.Traveled_range - self.range_prev == 10:
		# 			print("range")
		# 			self.burn()
		# 			self.range_prev = self.Traveled_range

		self.loops += 1
		if self.loops - self.prevLoop == 4:
			self.prevLoop = self.loops
			self.burn()
		#print(self.Traveled_range)
		#print(self.range_prev)

	def count_steps(self, x, y):
		pos = self.movement.get_absolute_position()
		steps_x = x - pos['X']
		steps_y = y - pos['Y']

	def burn(self):				#will turn on laser
		# self.visual.draw(self.circle, self.canvasName, "red2")
		if self.state == 0:
			#print("draw")
			pos = self.movement.get_absolute_position()
			self.visual.draw_line(self.canvasName, pos["X"], pos["Y"])
		else:
			pass


	def get_Z(self):
		return(self.state)

	def idk(self):
		pass

	def ready_for_next_CMD(self):
		self.ISO.Add_count()
		self.sideways_error = 0
		self.Traveled_range = 0
		self.range_prev = 0

#----------This portion will only be executed after inputing folder path---------

	def Draw_out(self, command):
		if 'Z' in command:
			if int(command['Z']) == 10:
				if self.StoreValue == True:
					line_id = self.canvasName.create_line(self.line_points, fill="blue", width=1, tag="upload_line")
				self.StoreValue = False
			elif int(command['Z']) == 0:
				if self.StoreValue != True:
					self.line_points.clear()
					self.StoreValue = True
		elif 'X' in command or 'Y' in command:
			if self.StoreValue == True:
				self.line_points.extend((command['X'], command['Y']))
			else:
				pass
		self.ISO.Add_count() #add then one line is finished

	def return_line_points(self):
		return (self.line_points)

#----------Accept correction value from move function in main---------
	def correction(self, x, y):
		self.correction_x = self.correction_x + x
		self.correction_y = self.correction_y + y