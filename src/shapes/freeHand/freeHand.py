from tkinter import *

from src.shapes.shape import Shape
from src.shapes.colors import SHAPE_COLORS
from dataclasses import *


@dataclass
class FreeHand(Shape):
    

    def bind(self, start, update):
        self.canvas.bind('<ButtonPress-1>', start)
        self.canvas.bind('<B1-Motion>', update)


