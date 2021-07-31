from tkinter import *
import visual
from movement import movement


root = Tk()
root.resizable(width=False, height=False)

width = 300
height = 300

circle_pos = [150, 150]


canvas = Canvas(root, width = width, height = height)
canvas.grid(row=0, rowspan=3, column=0, columnspan=3)

line_x = visual.create_line_x(circle_pos, canvas, "gray30")
line_y = visual.create_line_y(circle_pos, canvas, "gray30")
circle = visual.create_circle(circle_pos, 5, canvas, "red2")
m = movement(canvas, circle, line_x, line_y)
"""
Button_lUp = Button (root, text = "*", padx = 40, pady = 40, command=lambda: m.Move_lUp())
Button_left = Button (root, text = "L", padx = 40, pady = 40, command=lambda: m.move_left())
Button_lDown = Button (root, text = "*", padx = 40, pady = 40, command=lambda: m.Move_lDown())
Button_Up = Button (root, text = "U", padx = 40, pady = 40, command=lambda: m.move_up())
Button_ = Button (root, text = "*", padx = 40, pady = 40, command=lambda: m.move_up())
Button_Down = Button (root, text = "D", padx = 40, pady = 40, command=lambda: m.move_down())
Button_rUp = Button (root, text = "*", padx = 40, pady = 40, command=lambda: m.Move_rUp())
Button_right = Button (root, text = "R", padx = 40, pady = 40, command=lambda: m.move_right())
Button_rDown = Button (root, text = "*", padx = 40, pady = 40, command=lambda: m.Move_rDown())

Button_lUp.grid(row = 0, column = 4)
Button_left.grid(row = 1,column = 4)
Button_lDown.grid(row = 2, column = 4)
Button_Up.grid(row = 0, column = 5)
Button_.grid(row = 1, column = 5)
Button_Down.grid(row = 2, column = 5)
Button_rUp.grid(row = 0, column = 6)
Button_right.grid(row = 1, column = 6)
Button_rDown.grid(row = 2, column = 6)
"""
root.bind("<KeyPress-Left>",lambda e: m.move_left())
root.bind("<KeyPress-Right>",lambda e: m.move_right())
root.bind("<KeyPress-Up>",lambda e: m.move_up())
root.bind("<KeyPress-Down>",lambda e: m.move_down())
root.bind("<KeyRelease>", lambda e: m.Stop())

def get_pos():
	visual.draw(circle, canvas, "red2")
	idk = m.get_coords()
	print(idk)
	print(type(idk))
	root.after(20, get_pos)

root.after(20, get_pos)
root.mainloop()