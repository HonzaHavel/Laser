from tkinter import *


class Main:
	def __init__(self):
		self.entry_widget = 0

		self.root = Tk()
		self.root.resizable(width=False, height=False)
		self.root.geometry("800x480")
		self.width = 480
		self.height = 480

		self.main_frame()


	def main_frame(self):
		self.f_main = Frame(self.root, height = 480, width = 320, borderwidth = 1, highlightbackground="red",highlightthickness=1)
		self.f_main.place(x=480, y=0)

		eF = Entry(self.f_main, relief = "groove")
		eMM = Entry(self.f_main, relief = "groove")

		eF.place(x = 70, y = 127, height = 40, width = 60)
		eMM.place(x = 70, y = 166, height = 40, width = 60)

		eF.bind("<1>", open_numeric_keyboard(0))	#open numeric for feedrate
		eMM.bind("<1>", open_numeric_keyboard(1))	#open numeric for MM

	def open_numeric_keyboard(self, entry):
		#entry = chceck what entry is opened to write to the right one
		self.numeric_frame.tkraise()
		if entry == 0:		#F
			self.entry_widget = 0

		elif entry == 1:	#MM
			self.entry_widget = 1

app = Main()