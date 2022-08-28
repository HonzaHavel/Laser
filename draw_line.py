import tkinter as tk

line_id = None
line_points = []
line_options = {}


def draw_line(event):
    global line_id
    line_points.extend((event.x, event.y))
    # if line_id is not None:
    #     canvas.delete(line_id)
    line_id = canvas.create_line(line_points, **line_options) 


def set_start(event):
    line_points.extend((event.x, event.y))


def end_line(event=None):
    global line_id
    line_points.clear()
    line_id = None


root = tk.Tk()

canvas = tk.Canvas()
canvas.pack()

canvas.bind('<Button-1>', set_start)
canvas.bind('<B1-Motion>', draw_line)
canvas.bind('<ButtonRelease-1>', end_line)

root.mainloop()