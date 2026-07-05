from tkinter import *

from .draw import Draw

from prodraw.config import SHAPE_COLORS


class Update:
    """Handles updating oval properties dynamically during mouse drag."""

    @staticmethod
    # Returns an event handler that updates the oval's endpoint and redraws it
    def update(obj, figures: list):

        # Updates the end coordinates and dynamically draws the oval on the canvas
        def update_points(event):
            obj["obj"].end_x = event.x
            obj["obj"].end_y = event.y
            Draw.draw(obj["obj"].canvas, figures)
            if abs(obj["obj"].end_y-obj["obj"].start_y)>5 and abs(obj["obj"].end_x-obj["obj"].start_x)>5:
                obj["obj"].canvas.create_oval(obj["obj"].start_x, obj["obj"].start_y, obj["obj"].end_x, obj["obj"].end_y,
                                          fill=SHAPE_COLORS.get(obj["obj"].bg), outline=obj['obj'].bg, tags=("oval", "shape"))

        return update_points
