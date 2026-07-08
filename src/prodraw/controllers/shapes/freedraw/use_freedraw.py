from tkinter import Canvas, StringVar

from .freedraw_controller import FreeDrawController


def freedraw_bind(canvas: Canvas, figures: dict, bg: StringVar) -> FreeDrawController:
    controller = FreeDrawController(canvas, figures, get_bg=bg.get)
    controller.bind()
    return controller


def freedraw_delete(canvas: Canvas, controller: FreeDrawController):
    controller.unbind()
