from prodraw.models import Window
from prodraw.views import WindowView

from typing import Callable


class WindowController:
    def __init__(self):
        self.view = WindowView()
        self.current: Window = None


    def load(self, title: str = "ProDraw", is_fullscreen: bool = True):
        self.current = Window(title=title, is_fullscreen=is_fullscreen)

        self.view.set_fullscreen(enabled=True)
        self.view.set_title(title)

    def toggle(self, event=None):
        is_fullscreen = not self.view.root.attributes("-fullscreen")
        self.root.attributes("-fullscreen", is_fullscreen)

    def exit(self, event=None):
        self.view.root.attributes("-fullscreen", False)

    def bind(self, keyword: str, command: Callable):
        self.view.root.bind(keyword, command)

        return self

    def run(self):
        self.view.start()
        pass

    def destroy(self):
        self.view.destroy()
        pass
