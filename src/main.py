# from prodraw.window import FullScreen, Version
from prodraw.controllers import create_window, destroy_window
from prodraw.models import Version
from prodraw.workspace import Workspace


def main():
    window = create_window(title="ProDraw", is_fullscreen=True)
    version = Version("1.0.0")

    Workspace(root=window.view.root, version=version).start()

    window.run()


main()
