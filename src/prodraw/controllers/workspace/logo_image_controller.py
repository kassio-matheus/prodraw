from tkinter import Canvas
from prodraw.models.workspace.logo_image_model import LogoImageModel
from prodraw.views.workspace.logo_image_view import LogoImageView


class LogoImageController:
    """Sets up and displays the version watermark."""

    def __init__(self, canvas: Canvas, image: str, bg: str):
        self.model = LogoImageModel(image, bg)
        self.view = LogoImageView(canvas, self.model)

    def setup(self):
        self.view.render()
