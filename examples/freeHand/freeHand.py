from tkinter import *
from src.shapes.colors import SHAPE_COLORS


def FreeHand(canva: Canvas, bg:StringVar, figures: list = []):

    init_x = None
    init_y = None

    # start the free hand when button is pressed
    def startFigure(event):
        global init_x, init_y

        init_x = event.x
        init_y = event.y

    # draw the freehand when the mouse is moved with the button pressed
    def updateFigure(event):
        global init_x, init_y
        canva.create_line(init_x, init_y, event.x, event.y, fill=bg.get(), tags='freehand')

        init_x = event.x
        init_y = event.y
        



    

    canva.bind('<ButtonPress-1>', startFigure)
    canva.bind('<B1-Motion>', updateFigure)
