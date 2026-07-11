from tkinter import Menu


class MenubarView:
    def __init__(self, root):
        self.root = root

    def create(self):
        self.menubar = Menu(self.root)
        return self.menubar

    def render(self, menubar: Menu):
        self.root.config(menu=menubar)
