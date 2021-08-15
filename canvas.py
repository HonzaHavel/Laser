from tkinter import *
import visual
from movement import movement
from Execute import *
from ISO import *

class Main:
	def __init__(self):
		self.file_name = ('G-code_test.tap')

		self.Z = False

		self.root = Tk()
		self.root.resizable(width=False, height=False)

		self.width = 300
		self.height = 300

		self.circle_pos = [150, 150]

		self.visual = visual

		self.canvas = Canvas(self.root, width = self.width, height = self.height)
		self.canvas.grid(row=0, rowspan=3, column=1, columnspan=3)

		self.line_x = visual.create_line_x(self.circle_pos, self.canvas, "gray30")
		self.line_y = visual.create_line_y(self.circle_pos, self.canvas, "gray30")
		self.circle = visual.create_circle(self.circle_pos, 5, self.canvas, "red2")
		self.m = movement(self.canvas, self.circle, self.line_x, self.line_y)

		self.pos_buttons()
		self.pos_labels()

		self.IS = ISO(self.file_name)
		self.EXE = Execute(self.circle, self.canvas, self.visual, self.IS, self.m)

		self.root.bind("<KeyPress-Left>",lambda e: self.m.move_left())
		self.root.bind("<KeyPress-Right>",lambda e: self.m.move_right())
		self.root.bind("<KeyPress-Up>",lambda e: self.m.move_up())
		self.root.bind("<KeyPress-Down>",lambda e: self.m.move_down())
		self.root.bind("<KeyRelease>", lambda e: self.m.Stop())

		#self.root.after(1, self.simulate)
		#root.after(20, get_pos)
		self.root.mainloop()
		'''
		def laser_toggle():
			visual.draw(circle, canvas, "red2")
			root.after(20, laser_toggle)

		if Z == True:
			root.after(20, laser_toggle)
		'''
	def simulate(self):
		pos = self.m.get_absolute_position()
		print(pos)
		self.EXE.Exe_ISO(self.IS.Process(self.IS.Input_Line()))
		self.root.after(1, self.simulate)

	def get_pos(self):
		idk = m.get_coords()
		pos = m.get_absolute_position()
		print(pos)
		#print(type(idk))
		root.after(20, get_pos)

	def pos_buttons(self):
		Button_lUp = Button (self.root, text = "*", padx = 40, pady = 40, command=lambda: self.m.Move_lUp())
		Button_left = Button (self.root, text = "L", padx = 40, pady = 40, command=lambda: self.m.move_left())
		Button_lDown = Button (self.root, text = "*", padx = 40, pady = 40, command=lambda: self.m.Move_lDown())
		Button_Up = Button (self.root, text = "U", padx = 40, pady = 40, command=lambda: self.m.move_up())
		Button_ = Button (self.root, text = "*", padx = 40, pady = 40, command=lambda: self.m.move_up())
		Button_Down = Button (self.root, text = "D", padx = 40, pady = 40, command=lambda: self.m.move_down())
		Button_rUp = Button (self.root, text = "*", padx = 40, pady = 40, command=lambda: self.m.Move_rUp())
		Button_right = Button (self.root, text = "R", padx = 40, pady = 40, command=lambda: self.m.move_right())
		Button_rDown = Button (self.root, text = "*", padx = 40, pady = 40, command=lambda: self.m.Move_rDown())

		Button_lUp.grid(row = 0, column = 5)
		Button_left.grid(row = 1,column = 5)
		Button_lDown.grid(row = 2, column = 5)
		Button_Up.grid(row = 0, column = 6)
		Button_.grid(row = 1, column = 6)
		Button_Down.grid(row = 2, column = 6)
		Button_rUp.grid(row = 0, column = 7)
		Button_right.grid(row = 1, column = 7)
		Button_rDown.grid(row = 2, column = 7)

	def pos_labels(self):
		Label_X = Label(self.root, text = "X:", padx = 40, pady = 40)
		Label_Y = Label(self.root, text = "Y:", padx = 40, pady = 40)
		Label_Z = Label(self.root, text = "Z:", padx = 40, pady = 40)

		Label_X.grid(row = 0, column = 0)
		Label_Y.grid(row = 1, column = 0)
		Label_Z.grid(row = 2, column = 0)

app = Main()