from tkinter import *

from .rounded import create_round_rectangle
from src.shapes.colors import SHAPE_COLORS

# function for draw rectangles

def Rectangle(canvas: Canvas, bg: StringVar, figures: list):

    # When the mouse is pressed

    def start_rectangle(event):
        nonlocal ini_x, ini_y
        ini_x = event.x
        ini_y = event.y

    # When the mouse is moved with the button pressed

    def update_rectangle(event):
        nonlocal end_x, end_y
        end_x = event.x
        end_y = event.y
        draw()
        canvas.create_rectangle(
            ini_x, ini_y, end_x, end_y, fill=SHAPE_COLORS.get(bg.get()), outline=bg.get(), tags="rectangle")
        # create_round_rectangle(canvas,
        #                        ini_x, ini_y, end_x, end_y, radius=40, fill="white", outline="black", tags="rectangle")

    # When the mouse is released

    def include_rectangle(event):
        nonlocal end_x, end_y
        if end_x is not None and end_y is not None:
            if ini_x != end_x or ini_y != end_y:
                figures.append(("rectangle", bg.get(), (ini_x, ini_y, end_x, end_y)))

    # draw all figures
    def draw():
        canvas.delete("rectangle")
        for rectagle in figures:
            if rectagle[0] == "rectangle":
                canvas.create_rectangle(
                    *rectagle[2], fill=SHAPE_COLORS.get(rectagle[1]), outline=rectagle[1], tags="rectangle")

        # for rectagle in rectangles:
        #     create_round_rectangle(
        #         canvas, rectagle[0], rectagle[1], rectagle[2], rectagle[3], radius=40, fill="white", outline="black", tags="rectangle")

    ini_x = None
    ini_y = None
    end_x = None
    end_y = None

    canvas.bind('<ButtonPress-1>', start_rectangle)
    canvas.bind('<B1-Motion>', update_rectangle)
    canvas.bind('<ButtonRelease-1>', include_rectangle)
