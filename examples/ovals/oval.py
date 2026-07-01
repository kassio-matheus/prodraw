from tkinter import *
from src.shapes.colors import SHAPE_COLORS


def Oval(canvas: Canvas, bg: StringVar, figures: list):

    # start oval whe the button is pressed
    def start_line(event):
        nonlocal start_x, start_y
        start_x = event.x
        start_y = event.y

    # When the mouse is moved with the button pressed, draw the preview
    def update_line(event):
        nonlocal end_x, end_y

        end_x = event.x
        end_y = event.y

        draw()

        # Preview
        canvas.create_oval(start_x, start_y, end_x, end_y,
                           fill=SHAPE_COLORS.get(bg.get()), outline=bg.get(), tags="oval")

    # add oval in figures list when de mouse is released
    def add_line(event):
        nonlocal end_x, end_y
        if end_x is not None and end_y is not None:
            figures.append(("oval",bg.get(),(start_x, start_y, end_x, end_y)))
    
    # draw all ovals
    def draw():
        canvas.delete("oval")

        for oval in figures:
            if oval[0] == 'oval':
                canvas.create_oval(oval[2], fill=SHAPE_COLORS.get(oval[1]),
                                outline=oval[1], tags="oval")


    start_x = None
    start_y = None
    end_x = None
    end_y = None

    canvas.bind('<ButtonPress-1>', start_line)
    canvas.bind('<B1-Motion>', update_line)
    canvas.bind('<ButtonRelease-1>', add_line)