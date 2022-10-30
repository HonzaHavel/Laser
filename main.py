from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import visual
from movement import movement
from Execute import *
from ISO import *
from DB import *

class Main:
	def __init__(self):
		self.entry_widget = 0
		self.control_type = 0 #control type 1 = movement, control type 2 = relocation of ISO

		self.Z = False
		self.start = False

		self.root = Tk()
		self.root.configure(background = "gray16")
		self.root.resizable(width=False, height=False)
		self.root.geometry("800x480")
		self.width = 480
		self.height = 480

		circle_pos = [240, 240]

		self.visual = visual

		self.canvas = Canvas(self.root, width = self.width, height = self.height, background = "gray18")
		self.canvas.place(x=0, y=0)

		self.DB = Database()

		self.line_x = visual.create_line_x(circle_pos, self.canvas, "gray30")
		self.line_y = visual.create_line_y(circle_pos, self.canvas, "gray30")
		self.circle = visual.create_circle(circle_pos, 5, self.canvas, "cyan2")
		self.m = movement(self.canvas, self.circle, self.line_x, self.line_y, self.DB)#, self.LaserQuery)

		self.control_frame()
		self.main_frame()
		self.numeric_frame()
		self.f_main.tkraise()
		#self.pos_labels()

		

		self.IS = ISO()
		self.EXE = Execute(self.circle, self.canvas, self.visual, self.IS, self.m, self.DB)
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
		self.simulate()
		self.root.after(1, self.loop)
		self.update_pos_labels()

	def simulate(self):
		# pos = self.m.get_absolute_position()
		if self.start == True:
			self.EXE.Exe_ISO(self.IS.Process(self.IS.Input_Line()))

	def get_pos(self):
		idk = m.get_coords()
		pos = m.get_absolute_position()
		root.after(20, get_pos)

	def control_frame(self):
		self.f_control = Frame(self.root, height = 480, width = 320, borderwidth = 1, background = "gray16")
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

		Button_back = Button(self.f_control, text = "BACK", command = lambda:self.f_main.tkraise())
		Button_home = Button(self.f_control, text = "HOME")
		Button_laser = Button(self.f_control, text = "LASER", command = lambda:self.EXE.Z(20)) #state 20 = reverse value of laser

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
		self.f_main = Frame(self.root, height = 480, width = 320, borderwidth = 1, background = "gray16")
		self.f_main.place(x=480, y=0)

		Button_upload = Button(self.f_main, text = "UPLOAD G-CODE",bg = "gray20", command = lambda: self.file_directory())
		Button_upload.place(x = 10, y = 10, height = 60, width = 300)

		Button_start = Button(self.f_main, text = "S", command = lambda: self.start_laser())
		Button_pause = Button(self.f_main, text = "P", command = lambda: self.pause_laser())
		Button_unpause = Button(self.f_main, text = "U")
		Button_stop = Button(self.f_main, text = "ST", command = lambda: self.stop_laser())

		Button_start.place(x = 10, y = 70, height = 48, width = 75)
		Button_pause.place(x = 85, y = 70, height = 48, width = 75)
		Button_unpause.place(x = 160, y = 70, height = 48, width = 75)
		Button_stop.place(x = 235, y = 70, height = 48, width = 75)

		Label_F = Label(self.f_main, text = "FEEDRATE", relief = "groove")
		Label_MM = Label(self.f_main, text = "STEP/MM", relief = "groove")
		self.eF = Entry(self.f_main, relief = "groove")
		self.eMM = Entry(self.f_main, relief = "groove")
		Button_save = Button(self.f_main, text = "SAVE", relief = "groove", command = lambda:self.save())

		Label_F.place(x = 10, y = 128, height = 40, width = 60)
		Label_MM.place(x = 10, y = 166, height = 40, width = 60)
		self.eF.place(x = 70, y = 128, height = 40, width = 70)
		self.eMM.place(x = 70, y = 166, height = 40, width = 70)
		Button_save.place(x = 10, y = 206, height = 60, width = 130)

		open = lambda x: open_numeric_keyboard(x)

		self.eF.bind("<1>", lambda x:self.open_numeric_keyboard(0))	#open numeric for feedrate
		self.eMM.bind("<1>", lambda x:self.open_numeric_keyboard(1))	#open numeric for MM

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

		self.Button_Control = Button(self.f_main, text = "Control", relief = "groove", command = lambda:self.open_control(1))
		self.Button_Move = Button(self.f_main, text = "Move", relief = "groove", command = lambda:self.open_control(2))

		self.Button_Control.place(x = 160, y = 128, height = 60, width = 150)
		self.Button_Move.place(x = 160, y = 188, height = 60, width = 150)


	def numeric_frame(self):
		self.f_numeric = Frame(self.root, height = 240, width = 180, borderwidth = 1,highlightthickness=1)
		self.f_numeric.place(x=560, y=250)

		Button_OK = Button(self.f_numeric, text = "OK", command = lambda:self.Enter(11))
		Button_0 = Button(self.f_numeric, text = "0", command = lambda:self.Enter(0))
		Button_1 = Button(self.f_numeric, text = "1", command = lambda:self.Enter(1))
		Button_2 = Button(self.f_numeric, text = "2", command = lambda:self.Enter(2))
		Button_3 = Button(self.f_numeric, text = "3", command = lambda:self.Enter(3))
		Button_4 = Button(self.f_numeric, text = "4", command = lambda:self.Enter(4))
		Button_5 = Button(self.f_numeric, text = "5", command = lambda:self.Enter(5))
		Button_6 = Button(self.f_numeric, text = "6", command = lambda:self.Enter(6))
		Button_7 = Button(self.f_numeric, text = "7", command = lambda:self.Enter(7))
		Button_8 = Button(self.f_numeric, text = "8", command = lambda:self.Enter(8))
		Button_9 = Button(self.f_numeric, text = "9", command = lambda:self.Enter(9))

		Button_OK.place(x = 0, y = 180, height = 60, width = 60)
		Button_0.place(x = 60, y = 180, height = 60, width = 60)
		Button_1.place(x = 0, y = 0, height = 60, width = 60)
		Button_2.place(x = 60, y = 0, height = 60, width = 60)
		Button_3.place(x = 120, y = 0, height = 60, width = 60)
		Button_4.place(x = 0, y = 60, height = 60, width = 60)
		Button_5.place(x = 60, y = 60, height = 60, width = 60)
		Button_6.place(x = 120, y = 60, height = 60, width = 60)
		Button_7.place(x = 0, y = 120, height = 60, width = 60)
		Button_8.place(x = 60, y = 120, height = 60, width = 60)
		Button_9.place(x = 120, y = 120, height = 60, width = 60)


	def update_pos_labels(self):
		pos = self.m.get_absolute_position()
		pos['X'] = round(pos['X'],3)
		pos['Y'] = round(pos['Y'],3)
		Z = self.EXE.get_Z()
		self.Label_X.configure(text = "{}".format(pos['X']))
		self.Label_Y.configure(text = "{}".format(pos['Y']))
		self.Label_Z.configure(text = "{}".format(Z))


	def open_numeric_keyboard(self, entry):
		#entry = chceck what entry is opened to write to the right one
		if entry == 0:		#F
			self.entry_widget = 0

		elif entry == 1:	#MM
			self.entry_widget = 1
		self.f_numeric.tkraise()


	def close_numeric_keyboard(self):
		pass

	def Enter(self, number):
		#enter into entery
		if number == 11:
			self.f_main.tkraise()

		elif self.entry_widget == 0:
			self.eF.insert(END, number)

		elif self.entry_widget == 1:
			self.eMM.insert(END, number)

	def save(self):
		feedrate = self.eF.get()
		stepPerMM = self.eMM.get()
		#self.writeDB(feedrate, stepPerMM)
		self.DB.change_feedrate(feedrate)
		self.DB.change_SPMM(stepPerMM)

	def file_directory(self):
		path = filedialog.askopenfilename()
		self.IS.Input_folder_path(path)
		status = self.IS.Drawing_status()
		while status == True:
			self.EXE.Draw_out(self.IS.Process(self.IS.Input_Line()))
			status = self.IS.Drawing_status()
		self.IS.reset_count()

	def start_laser(self):
		self.start = True

	def pause_laser(self):
		self.start = False

	def stop_laser(self):
		self.start = False
		self.IS.reset_count()
		circle_pos = self.m.get_coords()
		self.canvas.delete("line")

	def open_control(self, type): #control type 1 = movement, control type 2 = relocation of ISO
		self.control_type = type
		self.f_control.tkraise()

	def control_move(self, direction): #determin if we are moving laser or iso and send out executive command
		if self.control_type == 1: #move laser
			match direction:
				case 1:
					self.m.Move_lUp()
				case 2:
					self.m.move_left()
				case 3:
					self.m.Move_lDown()
				case 4:
					self.m.move_up()
				case 5:
					self.m.Move_up()
				case 6:
					self.m.move_down()
				case 7:
					self.m.Move_rUp()
				case 8:
					self.m.move_right()
				case 9:
					self.m.Move_rDown()

		elif self.control_type == 2:
			pass
			# match direction:
			# 	case 1:
			# 		self.m.Move_lUp()
			# 	case 2:
			# 		self.m.move_left()
			# 	case 3:
			# 		self.m.Move_lDown()
			# 	case 4:
			# 		self.m.move_up()
			# 	case 5:
			# 		self.m.Move_up()
			# 	case 6:
			# 		self.m.move_down()
			# 	case 7:
			# 		self.m.Move_rUp()
			# 	case 8:
			# 		self.m.move_right()
			# 	case 9:
			# 		self.m.Move_rDown()


app = Main()