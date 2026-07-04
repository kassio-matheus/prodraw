from tkinter import *
from dataclasses import *

from prodraw.shapes import Shape


@dataclass
class Oval(Shape):
    """Represents an oval shape."""

    # Binds start, update, and add events to the shape
    def bind(self, start, update, add):
        super().bind(start, update, add)
