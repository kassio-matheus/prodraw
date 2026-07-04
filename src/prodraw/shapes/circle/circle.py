from tkinter import *
from dataclasses import *

from prodraw.shapes import Shape

from prodraw.config import SHAPE_COLORS


@dataclass
class Circle(Shape):
    """Represents a circle shape with a specific radius."""

    raio: float = None

    # Binds start, update, and add events to the shape
    def bind(self, start, update, add):
        super().bind(start, update, add)
