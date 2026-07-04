import tkinter as tk

from prodraw.workspace import Workspace

# Initializes the main application window and starts the workspace

#Waiting to apply SOLID principles to the App class and its methods. The current implementation is functional but could be improved for better maintainability and scalability.

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ProDraw") #SOLID
        self.root.attributes("-fullscreen", True) #SOLID

    # Toggles the window fullscreen mode - SOLID
    def toggle_fullscreen(self, event=None):
        is_fullscreen = not self.root.attributes("-fullscreen")
        self.root.attributes("-fullscreen", is_fullscreen)

    # Exits the window fullscreen mode - SOLID
    def exit_fullscreen(self, event=None):
        self.root.attributes("-fullscreen", False)

    def run(self):
        self.root.bind("<F11>", self.toggle_fullscreen) #SOLID
        self.root.bind("<Escape>", self.exit_fullscreen) #SOLID

        VERSION = "1.0.0" #SOLID
        Workspace(self.root, version=VERSION).start() #SOLID

        self.root.mainloop()


# class VersionController:
#     def __init__(self, version):
#         self.version = version

#     def get_version(self):
#         return self.version


# class FullscreenController:
#     def __init__(self, root):
#         self.root = root

#     def toggle(self, event=None):
#         is_fullscreen = not self.root.attributes("-fullscreen")
#         self.root.attributes("-fullscreen", is_fullscreen)

#     def exit(self, event=None):
#         self.root.attributes("-fullscreen", False)
