from tkinter import Event
from dataclasses import dataclass

from prodraw.models.workspace.cursor_model import CursorModel
from prodraw.views.workspace.cursor_view import CursorView

from prodraw.controllers.shapes.tools import Tools


@dataclass
class CursorController(Tools):
    """Bridges raw Tkinter mouse events and the Cursor model/view.
    This is the only layer allowed to know about both Tkinter events
    and business rules (model state)."""

    current: CursorModel = None

    def _on_press(self, event: Event):
        """Step 1: mouse down starts a new, uncommitted cursor.
        A fresh Rectangle instance is created per press — no shared
        class-level state between draws."""

        self.current = CursorModel()
        self.current.start(event.x, event.y)

    def _on_drag(self, event: Event):
        """Step 2: mouse movement updates the in-progress cursor
        and renders a preview only"""

        self.current.update(event.x, event.y)

        self.view.draw(
            self.current.start_x, self.current.start_y, self.current.end_x, self.current.end_y, outline=self.current.outline_color)

    def _on_release(self, event: Event):
        """Step 3: mouse up commits the cursor."""

        self.view.clear_view_selection()
        self.current = None
