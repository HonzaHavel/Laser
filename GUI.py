class GUI:
	def __init__(self,):
		pass

	"""
		for line in self.Lines:
			line = line.strip('\n\r')
			gcode = line.split(' ')
			#print(gcode)
			#print(len(gcode))
			if len(gcode) < 2:
				#print(gcode)
				for command in gcode:
					if command[0] == 'Z':
						print(command)
						toReturn['Z'] = command[1:]
						print(toReturn)
					#return 			#return dictionary toReturn{'X':6.453435}
			else:
				for command in gcode:
					#print(command)
					#print(type(command))
					pass
		print (toReturn)
		##return toReturn
"""

#to canvas maybe

while sumbutton == 1:
	Execute.Exe_ISO(ISO.Process(Input_line()))
	ISO.Add_count()

		Button_lUp = Button (f_move, text = "*", padx = 40, pady = 40, command=lambda: self.m.Move_lUp())
		Button_left = Button (f_move, text = "L", padx = 40, pady = 40, command=lambda: self.m.move_left())
		Button_lDown = Button (f_move, text = "*", padx = 40, pady = 40, command=lambda: self.m.Move_lDown())
		Button_Up = Button (f_move, text = "U", padx = 40, pady = 40, command=lambda: self.m.move_up())
		Button_ = Button (f_move, text = "*", padx = 40, pady = 40, command=lambda: self.m.move_up())
		Button_Down = Button (f_move, text = "D", padx = 40, pady = 40, command=lambda: self.m.move_down())
		Button_rUp = Button (f_move, text = "*", padx = 40, pady = 40, command=lambda: self.m.Move_rUp())
		Button_right = Button (f_move, text = "R", padx = 40, pady = 40, command=lambda: self.m.move_right())
		Button_rDown = Button (f_move, text = "*", padx = 40, pady = 40, command=lambda: self.m.Move_rDown())

		Button_lUp.grid(row = 0, column = 5)
		Button_left.grid(row = 1,column = 5)
		Button_lDown.grid(row = 2, column = 5)
		Button_Up.grid(row = 0, column = 6)
		Button_.grid(row = 1, column = 6)
		Button_Down.grid(row = 2, column = 6)
		Button_rUp.grid(row = 0, column = 7)
		Button_right.grid(row = 1, column = 7)
		Button_rDown.grid(row = 2, column = 7)