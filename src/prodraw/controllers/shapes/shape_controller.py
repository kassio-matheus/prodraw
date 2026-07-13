from dataclasses import dataclass
from tkinter import *
from typing import Any

from prodraw.controllers.shapes.tools import Tools


@dataclass
class ShapeController:
    tools: Tools
    view: Any

    def __post_init__(self):
        canvas = self.view.canvas

        if canvas is not None:
            canvas.bind('<ButtonPress-1>', self.on_press)
            canvas.bind('<B1-Motion>', self.on_drag)
            canvas.bind('<ButtonRelease-1>', self.on_release)

    def on_drag(self, event):
        self.tools._on_drag(event)

    def on_press(self, event):
        self.tools._on_press(event)

    def on_release(self, event):
        self.tools._on_release(event)
