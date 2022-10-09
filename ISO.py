 
class ISO:
	def __init__(self):		#file has to be already imported
		self.file = None
		self.Lines = None
		self.count = 0				#ocunts lines send
		self.ISO_done = False
		self.CreateDrawing = False

	def Input_Line(self):
		x = self.count
		return (self.Lines[x])

	def Process(self, line):		#line is return from function Input_Line()
		toReturn = {}
		#line = line.split('\n\r')
		line = line.split()
		for command in line:
			if command[0] == 'G':
				toReturn['G'] = command[1:]
			elif command[0] == 'F':
				toReturn['F'] = command[1:]
			elif command[0] == 'X':
				toReturn['X'] = command[1:]
			elif command[0] == 'Y':
				toReturn['Y'] = command[1:]
			elif command[0] == 'Z':
				toReturn['Z'] = command[1:]
		return toReturn

	def Add_count(self):
		if self.count < (len(self.Lines)-1):
			self.count += 1
		else:
			self.ISO_done = True
			self.CreateDrawing = False

	def reset_count(self):
		self.count = 0

	def Actual_count(self):
		return(self.count)

	def Check(self):
		return(self.ISO_done)

	def Drawing_status(self):
		return(self.CreateDrawing)


	def Input_folder_path (self, file):
		self.file = file
		file = file.split("/")
		file = open(file[-1])
		self.Lines = file.readlines()
		self.CreateDrawing = True
		# while self.drawing == True:
		# 	self.Draw_out(self.Process(self.Input_Line()))

'''
IS = ISO(file_name)
while True:
	x = IS.Check()
	if x == True:
		break
	IS.Process(IS.Input_Line())
	IS.Add_count()
'''