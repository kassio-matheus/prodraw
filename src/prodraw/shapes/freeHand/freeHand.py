from tkinter import *
from dataclasses import *

from prodraw.shapes import Shape
from prodraw.config import SHAPE_COLORS


@dataclass
class FreeHand(Shape):
    """Represents a freehand drawing shape."""

    # Binds mouse press and motion events to enable continuous drawing
    def bind(self, start, update):
        self.canvas.bind('<ButtonPress-1>', start)
        self.canvas.bind('<B1-Motion>', update)
