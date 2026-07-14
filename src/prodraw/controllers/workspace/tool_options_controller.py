from tkinter import Canvas
from prodraw.models.workspace.tool_options_model import ToolOptionsModel
from prodraw.views.workspace.tool_options_view import ToolOptionsView


class ToolOptionsController:
    """
    Connects the Tool Options model and view. 
    Handles user selections for fills, borders, and sizes.
    """

    def __init__(self, canvas: Canvas, cursor=None):
        self.model = ToolOptionsModel()
        self.view = ToolOptionsView(canvas, self.model)
        self.cursor = cursor

    def setup(self) -> None:
        """Builds the UI and initializes default highlighted states."""
        self.view.build(
            on_fill_click=self._on_fill_select,
            on_border_click=self._on_border_select,
            on_size_click=self._on_size_select
        )

        # Trigger initial selection to highlight default values
        self._on_fill_select(self.model.get_fill())
        self._on_border_select(self.model.get_border())

        # --- TEMPORARILY REMOVED: Size Options ---
        # self._on_size_select(self.model.get_size())
        # -----------------------------------------

    def _on_fill_select(self, option_id: str) -> None:
        """Updates the selected fill model and refreshes the UI highlight."""
        previous = self.model.get_fill()
        self.view.unhighlight(previous)
        self.model.set_fill(option_id)
        self.view.highlight(option_id)

        # Design Rule: Disable border type selection if "No Border" is selected
        if option_id == "solid_no_border":
            self.view.set_border_buttons_state("disabled")
        else:
            self.view.set_border_buttons_state("normal")

        if self.cursor:
            self.cursor.update_shape_style(option_id, "fill")

    def _on_border_select(self, option_id: str) -> None:
        """Updates the selected border model and refreshes the UI highlight."""
        previous = self.model.get_border()
        self.view.unhighlight(previous)
        self.model.set_border(option_id)
        self.view.highlight(option_id)

        if self.cursor:
            self.cursor.update_shape_style(option_id, "border")

    def _on_size_select(self, option_id: str) -> None:
        """Updates the selected size model and refreshes the UI highlight."""
        previous = self.model.get_size()
        self.view.unhighlight(previous)
        self.model.set_size(option_id)
        self.view.highlight(option_id)

        # TODO: Broadcast change to cursor/shapes if necessary

    def sync_ui_from_shape(self, fill_option_id: str, border_option_id: str) -> None:
        """
        Synchronizes the Tool Options UI highlighting with the properties 
        of the currently selected shape.
        """
        # 1. Update Fill highlight in Model and View
        old_fill = self.model.get_fill()
        self.view.unhighlight(old_fill)
        self.model.set_fill(fill_option_id)
        self.view.highlight(fill_option_id)

        # 2. Update Border highlight in Model and View
        old_border = self.model.get_border()
        self.view.unhighlight(old_border)
        self.model.set_border(border_option_id)
        self.view.highlight(border_option_id)

        # 3. Handle disabling/enabling of border buttons based on fill type
        if fill_option_id == "solid_no_border":
            self.view.set_border_buttons_state("disabled")
        else:
            self.view.set_border_buttons_state("normal")
