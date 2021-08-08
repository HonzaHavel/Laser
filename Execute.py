from ISO import *			#might not be needed - just for test
							#inherit movement through canvas
class Execute:				#will be executed by button in canvas - executin dictionary from process return
	def __init__(self,movement, Z):		#execute will be checking for variable changed by stop button 
		self.Z = Z

	def Exe_ISO(self, command):
		if 'G' in command:
			value = command['G']
			G(value)

		if 'F' in command:
			value = command['F']
			F(value)

		if 'Z' in command:
			value = command['Z']
			Z(value)

		if 'X' in command or 'Y' in command:
			move_to_pos(float(command['X']), float(command['Y']))

	def G(self, value):
		if value == 1:
			print("what now? :D")

	def F(self, feedrate):
		return (movement.change_feedrate(feedrate))

	def Z(self, state):
		if state == 10: #laser off
			return (self.Z = False)

		elif state == 0: #laser on
			return (self.Z = True)

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
		SPM = movement.get_SPM()
		ABS = movement.get_absolute_position()
		Ax = ABS['X']
		Ay = ABS['Y']		#position now
		Mx = x - Ax
		My = y - Ay			#mm to go in axis
		SNx = Mx * SPM
		SNy = My * SPM 		#used for motor steps - check +/-	potreba zaokrouhlit
		DPSx = Mx / SNx
		DPSy = My/ SNy		#distance per step for simulation
		if SNx > SNy:
			pomer = SNx / SNy #nebude fungovat.. je treba najit nejvetiho spolecneho delitele 
		pass

	def count_steps(self, x, y):
		pos = movement.get_absolute_position()
		steps_x = x - pos['X']
		steps_y = y - pos['Y']
