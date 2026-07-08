import tkinter as tk
from dataclasses import dataclass


@dataclass
class WindowView:
    _root = tk.Tk()

    @property
    def root(self):
        return self._root

    def set_title(self, title: str):
        self._root.title(title)

    def set_size(self, width: int, height: int):
        self._root.geometry(f"{width}x{height}")

    def set_fullscreen(self, enabled: bool):
        self._root.attributes("-fullscreen", enabled)

    def start(self):
        self._root.mainloop()

    def destroy(self):
        self._root.destroy()
        self._root = None
