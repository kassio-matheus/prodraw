from tkinter import Event
from dataclasses import dataclass

from prodraw.models import Circle
from prodraw.views import CircleView
from prodraw.controllers.shapes.tools import Tools
from prodraw.models.workspace.color_picker_model import SHAPE_COLORS


@dataclass
class CircleController(Tools):
    """
    Bridges raw Tkinter mouse events and the Circle model/view.
    This is the only layer allowed to know about both Tkinter events
    and business rules (model state).
    """

    current: Circle = None

    def get_current_shape_style(self) -> dict:
        """Translates the active Tool Options and Colors into Tkinter canvas kwargs."""
        base_color = self.get_bg() if callable(self.get_bg) else "#FFFFFF"
        fill_color = SHAPE_COLORS.get(base_color, "#2C3036")

        fill_opt = "solid_border"
        border_opt = "solid"

        # Safely fetch configurations from the injected Tool Options Model
        if hasattr(self, 'tool_options_model') and self.tool_options_model:
            fill_opt = self.tool_options_model.get_fill()
            border_opt = self.tool_options_model.get_border()

        # Default style setup
        style = {"fill": fill_color, "outline": base_color,
                 "width": 1.5, "dash": ""}

        # 1. Apply Fill Configuration logic
        if fill_opt == "solid_no_border":
            style["fill"] = base_color
            style["outline"] = ""
        elif fill_opt == "no_solid_border":
            style["fill"] = ""
            style["width"] = 3.5

        # 2. Apply Border Configuration logic
        if border_opt == "dotted":
            style["dash"] = (6, 6)

        return style

    def _on_press(self, event: Event):
        """Step 1: mouse down starts a new, uncommitted circle."""
        self.current = Circle(bg=self.get_bg())
        self.current.start(event.x, event.y)

    def _on_drag(self, event: Event):
        """Step 2: mouse movement updates the in-progress circle's
        radius and renders a preview only, never touching the
        confirmed figures list."""
        self.current.update(event.x, event.y)
        
        if self.current.has_min_size():
            self.view.clear_preview()

            # Let the View draw the standard base preview (using 'circle_preview' tag)
            self.view.draw_preview(
                self.current.start_x, self.current.start_y,
                self.current.radius, self.current.bg
            )

            # Apply the active Tool Options style to the preview tag
            style = self.get_current_shape_style()
            self.canvas.itemconfig("circle_preview", **style)

    def _on_release(self, event: Event):
        """Step 3: mouse up commits the circle if it meets the minimum size."""
        if self.current is not None and self.current.has_min_size():
            circle_data = self.current.to_tuple()
            
            # Append data to the model
            self.figures['Circle'].append(circle_data)
            
            # Let the View draw the confirmed base shape
            self.view.draw(*circle_data)

            # Instantly apply the active Tool Options style to the final shape on the Canvas
            shape_id = circle_data[0]
            style = self.get_current_shape_style()
            self.canvas.itemconfig(f"id_{shape_id}", **style)

        self.view.clear_preview()
        self.current = None