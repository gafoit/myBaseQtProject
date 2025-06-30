import sys

from PySide6.QtWidgets import QApplication

from modules.core import AppContext
from modules.mainMenu.Module import MainMenu

if __name__ == '__main__':
    app = QApplication(sys.argv)

    context = AppContext()
    main_window = MainMenu(context)
    main_window.main_window_controller.show()
    sys.exit(app.exec())
