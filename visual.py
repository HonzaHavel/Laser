

def create_circle(circle_pos, r, canvasName, color): #center coordinates, radius
    x = int(circle_pos[0])
    y = int(circle_pos[1])
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1, fill = color)

def create_line_x(circle_pos, canvasName, color):
    width = canvasName["width"]
    x = int(circle_pos[0])
    y = int(circle_pos[1])

    x0 = (-abs(int(width)))
    y0 = y
    x1 = 2*width
    y1 = y

    return(canvasName.create_line(x0, y0, x1, y1, fill = color))

def create_line_y(circle_pos, canvasName, color):
    height = canvasName["height"]
    x = int(circle_pos[0])
    y = int(circle_pos[1])

    x2 = x
    y2 = 2*height
    x3 = x
    y3 = (-abs(int(height)))

    return(canvasName.create_line(x2, y2, x3, y3, fill = color))