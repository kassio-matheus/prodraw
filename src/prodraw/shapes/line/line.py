from tkinter import *
from dataclasses import *

from prodraw.shapes import Shape
from prodraw.config import SHAPE_COLORS


@dataclass
class Line(Shape):
    """Represents a straight line shape."""

    # Binds start, update, and add events to the shape
    def bind(self, start, update, add):
        super().bind(start, update, add)
