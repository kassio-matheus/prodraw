from tkinter import *

from .button import Button
from prodraw.models.workspace.toolbar_model import TOOLBAR_BG


class Cursor(Button):
    """Represents a rectangle tool button in the toolbar."""

    # Initializes the rectangle button properties and state watchers
    def __init__(self, toolsbar: Frame, width: int = 50, height: int = 50,
                 command=None, padding: int = 8, background: str = "#303035",
                 shape_colors: dict = None, selected_color_var: StringVar = None,
                 selected_option: StringVar = None, selected_key: str = "cursor"):
        super().__init__(
            toolsbar=toolsbar, width=width, height=height, command=command,
            watch_vars=(selected_option, selected_color_var)
        )
        self.padding = padding
        self.background = background
        self.shape_colors = shape_colors or {}
        self.selected_color_var = selected_color_var
        self.selected_option = selected_option
        self.selected_key = selected_key

    @property
    # Returns True if the rectangle tool is currently active
    def is_selected(self) -> bool:
        return self.selected_option is not None and self.selected_option.get() == self.selected_key

    # Draws the cursor icon and updates colors based on selection state
    def draw(self):
        if self.icon_id is not None:
            self.canvas.delete(self.icon_id)

        fill_color = self.selected_color_var.get(
        ) if self.selected_color_var and self.is_selected else TOOLBAR_BG
        border_color = self.shape_colors.get(
            fill_color, "#FFFFFF") if self.is_selected else self.background

        self.canvas.configure(
            bg=border_color,
            highlightthickness=1,
            highlightbackground=fill_color,
            highlightcolor=fill_color,
        )

        self.icon_id = self.canvas.create_rectangle(
            self.padding, self.padding,
            self.width - self.padding, self.height - self.padding,
            fill=border_color,
            outline=border_color
        )

        cursor_icon = PhotoImage(file="public/icons/cursor.png")

        self.image_id = self.canvas.create_image(
            self.width // 2, self.height // 2,
            image=cursor_icon
        )

        self.canvas.image = cursor_icon
