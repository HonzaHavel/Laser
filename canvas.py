from tkinter import *
from tkinter import ttk
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
		self.root.geometry("800x480")
		self.width = 480
		self.height = 480

		self.circle_pos = [240, 240]

		self.visual = visual

		self.canvas = Canvas(self.root, width = self.width, height = self.height)
		self.canvas.place(x=0, y=0)
		#self.canvas.pack()#grid(row=0, rowspan=3, column=1, columnspan=3)

		self.line_x = visual.create_line_x(self.circle_pos, self.canvas, "gray30")
		self.line_y = visual.create_line_y(self.circle_pos, self.canvas, "gray30")
		self.circle = visual.create_circle(self.circle_pos, 5, self.canvas, "red2")
		self.m = movement(self.canvas, self.circle, self.line_x, self.line_y)

		self.control_frame()
		self.main_frame()
		self.f_main.tkraise()
		#self.pos_labels()

		self.IS = ISO(self.file_name)
		self.EXE = Execute(self.circle, self.canvas, self.visual, self.IS, self.m)

		self.root.bind("<KeyPress-Left>",lambda e: self.m.move_left())
		self.root.bind("<KeyPress-Right>",lambda e: self.m.move_right())
		self.root.bind("<KeyPress-Up>",lambda e: self.m.move_up())
		self.root.bind("<KeyPress-Down>",lambda e: self.m.move_down())
		self.root.bind("<KeyRelease>", lambda e: self.m.Stop())

		self.root.after(1, self.loop)
		#root.after(20, get_pos)
		self.root.mainloop()
		'''
		def laser_toggle():
			visual.draw(circle, canvas, "red2")
			root.after(20, laser_toggle)

		if Z == True:
			root.after(20, laser_toggle)
		'''

	def loop(self):
		self.update_pos_labels()
		self.simulate()
		self.root.after(1, self.loop)

	def simulate(self):
		pos = self.m.get_absolute_position()
		print(pos)
		self.EXE.Exe_ISO(self.IS.Process(self.IS.Input_Line()))

	def get_pos(self):
		idk = m.get_coords()
		pos = m.get_absolute_position()
		print(pos)
		#print(type(idk))
		root.after(20, get_pos)

	def control_frame(self):
		self.f_control = Frame(self.root, height = 480, width = 320, borderwidth = 1, highlightbackground="red",highlightthickness=1)
		self.f_control.place(x=480, y=0)

		Label_X = Label(self.f_control, text = "X:", relief = "groove")
		Label_Y = Label(self.f_control, text = "Y:", relief = "groove")
		Label_Z = Label(self.f_control, text = "Z:", relief = "groove")

		self.Label_X = Label(self.f_control, text = " ", relief = "groove")
		self.Label_Y = Label(self.f_control, text = " ", relief = "groove")
		self.Label_Z = Label(self.f_control, text = " ", relief = "groove")

		Label_X.place(x = 10, y = 10, height = 48, width = 30)
		Label_Y.place(x = 10, y = 58, height = 48, width = 30)
		Label_Z.place(x = 10, y = 106, height = 48, width = 30)

		self.Label_X.place(x = 40, y = 10, height = 48, width = 100)
		self.Label_Y.place(x = 40, y = 58, height = 48, width = 100)
		self.Label_Z.place(x = 40, y = 106, height = 48, width = 100)

		Button_back = Button(self.f_control, text = "BACK")
		Button_home = Button(self.f_control, text = "HOME")
		Button_laser = Button(self.f_control, text = "LASER")

		Button_back.place(x = 158, y = 10, height = 40, width = 150)
		Button_home.place(x = 158, y = 62, height = 40, width = 150)
		Button_laser.place(x = 158, y = 114, height = 40, width = 150)
		
		Button_lUp = Button (self.f_control, text = "*", command=lambda: self.m.Move_lUp())
		Button_left = Button (self.f_control, text = "L", command=lambda: self.m.move_left())
		Button_lDown = Button (self.f_control, text = "*", command=lambda: self.m.Move_lDown())
		Button_Up = Button (self.f_control, text = "U", command=lambda: self.m.move_up())
		Button_0 = Button (self.f_control, text = "0,0", command=lambda: self.m.move_up())
		Button_Down = Button (self.f_control, text = "D", command=lambda: self.m.move_down())
		Button_rUp = Button (self.f_control, text = "*", command=lambda: self.m.Move_rUp())
		Button_right = Button (self.f_control, text = "R", command=lambda: self.m.move_right())
		Button_rDown = Button (self.f_control, text = "*", command=lambda: self.m.Move_rDown())

		Button_lUp.place(x = 8, y = 170, height = 100, width = 100)
		Button_left.place(x = 8, y = 270, height = 100, width = 100)
		Button_lDown.place(x = 8, y = 370, height = 100, width = 100)
		Button_Up.place(x = 108, y = 170, height = 100, width = 100)
		Button_0.place(x = 108, y = 270, height = 100, width = 100)
		Button_Down.place(x = 108, y = 370, height = 100, width = 100)
		Button_rUp.place(x = 208, y = 170, height = 100, width = 100)
		Button_right.place(x = 208, y = 270, height = 100, width = 100)
		Button_rDown.place(x = 208, y = 370, height = 100, width = 100)
		
	def main_frame(self):
		self.f_main = Frame(self.root, height = 480, width = 320, borderwidth = 1, highlightbackground="red",highlightthickness=1)
		self.f_main.place(x=480, y=0)

		Button_upload = Button(self.f_main, text = "UPLOAD G-CODE")
		Button_upload.place(x = 10, y = 10, height = 60, width = 300)

		Button_start = Button(self.f_main, text = "S")
		Button_pause = Button(self.f_main, text = "P")
		Button_unpause = Button(self.f_main, text = "U")
		Button_stop = Button(self.f_main, text = "ST")

		Button_start.place(x = 10, y = 70, height = 48, width = 75)
		Button_pause.place(x = 85, y = 70, height = 48, width = 75)
		Button_unpause.place(x = 160, y = 70, height = 48, width = 75)
		Button_stop.place(x = 235, y = 70, height = 48, width = 75)

		Label_F = Label(self.f_main, text = "FEEDRATE", relief = "groove")
		Label_MM = Label(self.f_main, text = "STEP/MM", relief = "groove")
		eF = Entry(self.f_main, relief = "groove")
		eMM = Entry(self.f_main, relief = "groove")
		Button_save = Button(self.f_main, text = "SAVE", relief = "groove")

		Label_F.place(x = 10, y = 128, height = 40, width = 60)
		Label_MM.place(x = 10, y = 166, height = 40, width = 60)
		eF.place(x = 70, y = 127, height = 40, width = 60)
		eMM.place(x = 70, y = 166, height = 40, width = 60)
		Button_save.place(x = 10, y = 276, height = 60, width = 130)

		Label_X = Label(self.f_main, text = "X:", relief = "groove")
		Label_Y = Label(self.f_main, text = "Y:", relief = "groove")
		Label_Z = Label(self.f_main, text = "Z:", relief = "groove")

		Label_X.place(x = 10, y = 326, height = 48, width = 30)
		Label_Y.place(x = 10, y = 374, height = 48, width = 30)
		Label_Z.place(x = 10, y = 422, height = 48, width = 30)

		self.Label_X = Label(self.f_main, text = " ", relief = "groove")
		self.Label_Y = Label(self.f_main, text = " ", relief = "groove")
		self.Label_Z = Label(self.f_main, text = " ", relief = "groove")

		self.Label_X.place(x = 40, y = 326, height = 48, width = 100)
		self.Label_Y.place(x = 40, y = 374, height = 48, width = 100)
		self.Label_Z.place(x = 40, y = 422, height = 48, width = 100)


	def update_pos_labels(self):
		pos = self.m.get_absolute_position()
		pos['X'] = round(pos['X'],3)
		pos['Y'] = round(pos['Y'],3)
		Z = self.EXE.get_Z()
		self.Label_X.configure(text = "{}".format(pos['X']))
		self.Label_Y.configure(text = "{}".format(pos['Y']))
		self.Label_Z.configure(text = "{}".format(Z))

app = Main()