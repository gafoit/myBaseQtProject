import sys

from PySide6.QtWidgets import QApplication

from modules.core import AppContext
from modules.FindPair.settings import Controller

if __name__ == '__main__':
    app = QApplication(sys.argv)

    context = AppContext()
    test_window = MainMenu(context)
    test_window.main_window_controller.show()
    sys.exit(app.exec())
