from .window_controller import WindowController


def create_window(title: str, is_fullscreen: bool, icon: str) -> WindowController:
    """Create window screen based on atributes."""
    controller = WindowController()
    controller.load(title=title, is_fullscreen=is_fullscreen, icon=icon)

    controller.bind("<F11>", controller.toggle)
    controller.bind("<Escape>", controller.exit)

    controller.create_menubar()

    return controller


def destroy_window(controller: WindowController):
    controller.destroy()
