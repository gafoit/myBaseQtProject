import sys

from PySide6.QtWidgets import QApplication

from modules.core import AppContext


def import_modules():
    #from modules.base_module import BaseModule
    from modules.mainMenu import MainMenu


def start_app():
    app = QApplication(sys.argv)

    context = AppContext()
    # from modules.base_module import BaseModule
    # context.create_module('Base', context)
    import_modules()
    mm = context.create_module('MainMenu', context)
    mm.main_window_controller.show()
    mm.closing.connect(app.quit)
    sys.exit(app.exec())


if __name__ == '__main__':
    start_app()
