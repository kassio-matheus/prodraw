from prodraw.controllers.circleController import CircleController
from tkinter import *
from prodraw.views.circleView import circleView

def circle_bind(canvas: Canvas, figures, bg):

    view = circleView(canvas)
    canvas.bind('<ButtonPress-1>', CircleController.start(bg))
    canvas.bind('<B1-Motion>', CircleController.update(view))
    canvas.bind('<ButtonRelease-1>', CircleController.add(view, figures))


def circle_delete(canvas):
     view = circleView(canvas)
     view.delete()