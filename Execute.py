from ISO import *			#might not be needed - just fotr test
							#inherit movement through canvas
class Execute:				#will be executed by button in canvas - executin dictionary from process return
	def __init__(self):		#execute will be checking for variable changed by stop button 
		pass

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

		if 'X' in command or 'Z' in command:
			move_to_pos(float(command['X']), float(command['Y']))

	def G(self, value):
		if value == 1:
			print("what now? :D")

	def F(self, feedrate):
		#change feedrate - maybe by adding value in movement and changing it everytime
		pass

	def Z(self, state):
		if state == 10: #laser off
			pass

		elif state == 0: #laser on
			pass 

	def move_to_pos(self, x, y):
		#well move damn it
		pass