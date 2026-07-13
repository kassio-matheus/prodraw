from tkinter import Canvas, StringVar

from .freedraw_controller import FreeDrawController
from prodraw.models.shapes import FreeDraw
from prodraw.views.shapes import FreeDrawView


def freedraw_bind(canvas: Canvas, figures: dict, bg: StringVar) -> FreeDrawController:
    controller = FreeDrawController(canvas, figures, get_bg=bg.get)
    controller.bind()
    return controller


def freedraw_sync_data(canvas: Canvas, figures: list, data: dict) -> FreeDrawController:
    view = FreeDrawView(canvas)
    controller = FreeDrawController(
        canvas, figures, get_bg=lambda: "#000000", view=view)

    positions = data.get("positions", [])
    bg_color = data.get("bg", "#000000")

    # for i in range(len(positions) - 1):
    #     start_x = positions[i][0]
    #     start_y = positions[i][1]

    #     end_x = positions[i+1][0]
    #     end_y = positions[i+1][1]

    #     controller.view.draw(start_x, start_y, end_x, end_y, bg=bg_color)

    controller.view.draw_path(positions, bg=bg_color)

    return controller


def freedraw_delete(canvas: Canvas, controller: FreeDrawController):
    controller.unbind()
