#from ISO import *							#might not be needed - just for test
							#inherit movement through canvas
class Execute:				#will be executed by button in canvas - executin dictionary from process return
	def __init__(self, circle, canvasName, visual, ISO, movement):		#execute will be checking for variable changed by stop button 
		self.visual = visual
		self.canvasName = canvasName
		self.Laser = False
		self.ISO = ISO
		self.movement = movement
		self.circle = circle

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
		return (self.movement.change_feedrate(feedrate))

	def Z(self, state):
		state = int(state)
		if state == 10: #laser off
			self.Laser = False

		if state == 0: #laser on
			self.Laser = True

	def move_to_pos(self, x, y):
		#well move damn it
		#z tabule to bude funkcni jen pro simulaci
		#motory musi krokovat u sikmo, takze treba 2x na 1y
		#kontrolovat co je mensi - udelat for r in range mensi a v nem dalsi for loop 
		#kde bude krokovat motor s vetsim poctem kroku
		#X:Y = 3:1
		#pocet kroku Y = 200
		#for r in range 200:
		#	for x in range 3:
		#		krok.X()
		#	krok.Y()
		SPM = self.movement.get_SPM()
		ABS = self.movement.get_absolute_position()
		Ax = ABS['X']
		Ay = ABS['Y']		#position now
		Mx = x - Ax
		My = y - Ay			#mm to go in axis
		SNx = round(Mx * SPM)
		SNy = round(My * SPM) 		#used for motor steps - check +/-	potreba zaokrouhlit
		DPSx = Mx / abs(SNx) if SNx is not 0 else 0
		DPSy = My / abs(SNy) if SNy is not 0 else 0		#distance per step for simulation
		StepsX = abs(SNx)
		StepsY = abs(SNy)
		range_prev = 0
		if SNx == SNy:
			for r in range (SNx):
				self.burn()
				self.movement.reposition(DPSx, DPSy)

		else:
			sideways_error = 0
			sideways_variable = abs(SNx) / abs(SNy) if abs(SNy) > abs(SNx) else abs(SNy) / abs(SNx)
			if StepsX > StepsY:
				for r in range (StepsX):
					self.movement.reposition(DPSx, 0)
					sideways_error += sideways_variable
					if r - range_prev == 10:
						self.burn()
						range_prev = r
					if sideways_error >= 1:
						self.movement.reposition(0, DPSy)
						#self.burn()
						sideways_error -= 1

			elif StepsY > StepsX:
				for r in range (StepsY):
					self.movement.reposition(0, DPSy)
					sideways_error += sideways_variable
					if r - range_prev == 10:
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