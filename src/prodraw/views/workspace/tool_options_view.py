from tkinter import Canvas, Frame
from prodraw.models.workspace.tool_options_model import ToolOptionsModel, PANEL_BG, SELECTED_BG, BUTTON_SIZE


class ToolOptionsView:
    """
    Renders the tool options panel containing fill, border, and size selectors.
    Uses Canvas shapes to draw the icons dynamically.
    """

    def __init__(self, canvas: Canvas, model: ToolOptionsModel):
        self.canvas = canvas
        self.model = model
        # Creates the main panel container with padding
        self.panel = Frame(canvas, bg=PANEL_BG, padx=31, pady=12)
        
        # Dictionary to store border canvas references and their commands
        self.border_buttons = {}

    def build(self, on_fill_click, on_border_click, on_size_click) -> None:
        """
        Builds the grid of options and positions the panel on the screen.
        It calculates the position right below the Color Picker.
        """
        # Row 0: Fill Options
        for col, fill_type in enumerate(self.model.fills):
            self._create_button(0, col, fill_type, "fill", on_fill_click)

        # Row 1: Border Options
        for col, border_type in enumerate(self.model.borders):
            self._create_button(1, col, border_type, "border", on_border_click)

        # Places the panel below the Color Picker (y=170 accommodates the Color Picker height)
        self.panel.place(relx=1.0, x=-16, y=170, anchor="ne")

    def _create_button(self, row: int, col: int, option_id: str, category: str, command) -> None:
        """
        Creates a single square button and draws the corresponding icon inside it.
        """
        btn_canvas = Canvas(self.panel, width=BUTTON_SIZE, height=BUTTON_SIZE,
                            bg=PANEL_BG, highlightthickness=0, cursor="hand2")
        btn_canvas.grid(row=row, column=col, padx=4, pady=4)

        # Draw the respective icon based on category and option_id
        self._draw_icon(btn_canvas, option_id, category)

        # Bind the click event
        btn_canvas.bind("<Button-1>", lambda event, opt=option_id, cmd=command: cmd(opt))

        # Store the canvas reference in the model for highlighting
        self.model.canvas_by_option[option_id] = btn_canvas

        # --- FIX: Store border buttons to easily disable them later ---
        if category == "border":
            self.border_buttons[option_id] = {
                "canvas": btn_canvas,
                "command": command
            }

    def _draw_icon(self, canvas: Canvas, option_id: str, category: str) -> None:
        """Draws the geometric representation of the tool inside the button."""
        # center = BUTTON_SIZE / 2
        padding = 6
        shape_size = BUTTON_SIZE - padding * 2

        stroke_color = "#ffffff"
        fill_color = "#5c5c66"  # Neutral gray for solid fills
        line_weight = 1.5

        # NOTE: Added tags=("icon",) to all drawings so we can target them later to change colors
        if category == "fill":
            if option_id == "solid_border":
                canvas.create_rectangle(padding, padding, padding + shape_size, padding + shape_size,
                                        fill=fill_color, outline=stroke_color, width=line_weight, tags=("icon",))
            elif option_id == "solid_no_border":
                canvas.create_rectangle(padding, padding, padding + shape_size, padding + shape_size,
                                        fill=fill_color, outline="", tags=("icon",))
            elif option_id == "no_solid_border":
                canvas.create_rectangle(padding, padding, padding + shape_size, padding + shape_size,
                                        fill="", outline=stroke_color, width=line_weight, tags=("icon",))

        elif category == "border":
            if option_id == "solid":
                canvas.create_oval(padding, padding, padding + shape_size, padding + shape_size,
                                   outline=stroke_color, width=line_weight, tags=("icon",))
            elif option_id == "dotted":
                canvas.create_oval(padding, padding, padding + shape_size, padding + shape_size,
                                   outline=stroke_color, width=line_weight, dash=(2, 3), tags=("icon",))

    def highlight(self, option_id: str) -> None:
        """Applies the selection highlight to the specific option button."""
        if option_id in self.model.canvas_by_option:
            self.model.canvas_by_option[option_id].config(bg=SELECTED_BG)

    def unhighlight(self, option_id: str) -> None:
        """Removes the selection highlight from the specific option button."""
        if option_id in self.model.canvas_by_option:
            self.model.canvas_by_option[option_id].config(bg=PANEL_BG)

    def set_border_buttons_state(self, state: str):
        """Enables or disables the border style buttons visually and behaviorally."""
        if not hasattr(self, 'border_buttons') or not self.border_buttons:
            return

        # Dim the icon color to dark gray when disabled, white when normal
        color = "#3a3a40" if state == "disabled" else "#ffffff"
        cursor = "arrow" if state == "disabled" else "hand2"

        for option_id, btn_data in self.border_buttons.items():
            btn = btn_data["canvas"]
            cmd = btn_data["command"]

            try:
                # 1. Update visual feedback (dim the icon and change cursor)
                btn.config(cursor=cursor)
                btn.itemconfig("icon", outline=color)

                # 2. Update behavior (prevent or allow clicks)
                if state == "disabled":
                    btn.unbind("<Button-1>")
                    # Automatically remove highlight if it was previously selected
                    self.unhighlight(option_id) 
                else:
                    # Rebind the click event
                    btn.bind("<Button-1>", lambda event, opt=option_id, c=cmd: c(opt))
            except Exception as e:
                print(f"Error setting state on border button '{option_id}': {e}")