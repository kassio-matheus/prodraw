from tkinter import Canvas, StringVar

from .square_controller import SquareController


def square_bind(canvas: Canvas, figures: dict, bg: StringVar) -> SquareController:
    controller = SquareController(canvas, figures, get_bg=bg.get)
    controller.bind()
    return controller


def square_delete(canvas: Canvas, controller: SquareController):
    controller.unbind()
