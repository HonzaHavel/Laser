from ISO import *			#might not be needed - just for test
							#inherit movement through canvas
class Execute:				#will be executed by button in canvas - executin dictionary from process return
	def __init__(self,movement, Z, F):		#execute will be checking for variable changed by stop button 
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
		pass