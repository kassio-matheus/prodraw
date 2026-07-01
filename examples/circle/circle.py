from tkinter import *

from src.shapes.colors import SHAPE_COLORS


def Circle(canvas: Canvas, bg: StringVar, figures: list):
    # start the circle when button is pressed
    def start_line(event):
        nonlocal start_x, start_y
        start_x = event.x
        start_y = event.y

    # draw the circle when the mouse is moved with the button pressed
    def update_line(event):
        nonlocal end_x, end_y, raio
        end_x = event.x
        end_y = event.y
        raio = ((start_x - end_x)**2 + (start_y - end_y)**2) ** 0.5
        draw()
        canvas.create_oval(start_x-raio, start_y-raio, start_x +
                           raio, start_y+raio, outline=bg.get(), fill=SHAPE_COLORS.get(bg.get()), tags="circle")
        

    # add the circle in the figures
    def add_line(event):
        if isinstance(raio, float):
            figures.append(("circle",bg.get(),(start_x, start_y, raio)))

    
    # draw all circles
    def draw():
        canvas.delete("circle")
        for circle in figures:
            if circle[0] == 'circle':
                x,y,r = circle[2]
                canvas.create_oval(x-r, y-r, x+r, y+r,
                                outline=circle[1], fill=SHAPE_COLORS.get(circle[1]), tags="circle")

    start_x = None
    start_y = None
    end_x = None
    end_y = None
    canvas.bind('<ButtonPress-1>', start_line)
    canvas.bind('<B1-Motion>', update_line)
    canvas.bind('<ButtonRelease-1>', add_line)
    raio = None
