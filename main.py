import sys

from PySide6.QtWidgets import QApplication

from modules.FindPair import FindPair
from modules.core import AppContext


def import_modules():
    # from modules.base_module import BaseModule
    # from modules.mainMenu import MainMenu
    from modules.FindPair import FindPair


def start_app():
    app = QApplication(sys.argv)

    context = AppContext()
    # from modules.base_module import BaseModule
    # context.create_module('Base', context)
    import_modules()

    fp = context.create_module('FindPair',context)
    fp.main_window_controller.view.show()

    # mm = context.create_module('MainMenu', context)
    # mm.main_window_controller.show()
    # mm.main_window_controller.view.rejected.connect(app.quit)
    # mm.main_window_controller.view.module_open_sig.connect(lambda _: context.create_module(_,context))
    sys.exit(app.exec())


if __name__ == '__main__':
    start_app()
