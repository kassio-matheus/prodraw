from dataclasses import dataclass
from tkinter import Canvas
from prodraw.config import SHAPE_COLORS


@dataclass
class FreeDrawView:
    canvas: Canvas = None

    def draw_preview(self, start_x: float, start_y: float, end_x: float, end_y: float, bg: str):
        self.canvas.create_line(
            start_x, start_y, end_x, end_y,
            fill=bg,
            smooth=True,
            width=5,
            capstyle="round",
            joinstyle="round",
            tags=("freedraw_preview", "shape")
        )

    def draw(self, start_x: float, start_y: float, end_x: float, end_y: float, bg: str):
        self.canvas.create_line(
            start_x, start_y, end_x, end_y,
            fill=bg,
            smooth=True,
            width=5,
            capstyle="round",
            joinstyle="round",
            tags=("freedraw", "shape")
        )

    def draw_path(self, positions: list, bg: str):
        if len(positions) < 2:
            return

        self.canvas.create_line(
            positions,
            fill=bg,
            smooth=True,
            width=4,
            capstyle="round",
            joinstyle="round",
            tags=("freedraw", "shape")
        )

    def clear_preview(self):
        self.canvas.delete("freedraw_preview")

    def delete(self):
        self.canvas.delete("freedraw")
        self.canvas.delete("freedraw_preview")
