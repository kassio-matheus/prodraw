from typing import Callable

from prodraw.models import Window
from prodraw.views import WindowView

from .menubar_controller import MenubarController
from prodraw.models.window.menubar import MenubarCascade, MenubarCommand


class WindowController:
    def __init__(self):
        self.view = WindowView()
        self.current: Window = None

    def load(self, title: str = "ProDraw", is_fullscreen: bool = True, icon: str = ""):
        self.current = Window(title=title, is_fullscreen=is_fullscreen)

        self.view.set_fullscreen(enabled=True)
        self.view.set_title(title)

        if (len(icon) > 0):
            self.view.set_app_icon(icon)

    def toggle(self, event=None):
        is_fullscreen = not self.view.root.attributes("-fullscreen")
        self.root.attributes("-fullscreen", is_fullscreen)

    def exit(self, event=None):
        self.view.root.attributes("-fullscreen", False)

    def bind(self, keyword: str, command: Callable):
        self.view.root.bind(keyword, command)

        return self

    def create_menubar(self):
        main_menubar = MenubarController(self.view.root)
        main_menubar.create()

        menu = [
            {"Arquivo": {"Sair": lambda: self.destroy()}},
            {"Visualização": {}},
            {"Ajuda": {}},
        ]

        for submenu in menu:
            submenubar = MenubarController(root=main_menubar.menubar)
            submenubar.create()

            cascade = MenubarCascade(
                next(iter(submenu.keys())), menu=submenubar.menubar, underline=0)
            main_menubar.add_cascade(cascade)

            for label, command in submenu[next(iter(submenu.keys()))].items():
                item = MenubarCommand(label, command=command)
                submenubar.add_command(item)

        main_menubar.run()

    def run(self):
        self.view.start()
        pass

    def destroy(self):
        self.view.destroy()
        pass
