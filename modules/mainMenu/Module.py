from PySide6 import QtCore
from PySide6.QtCore import Slot

from ..core import register_module
from .main_window import MainWindowController


@register_module('MainMenu')
class MainMenu(QtCore.QObject):
    closing = QtCore.Signal()

    def __init__(self, context):
        super().__init__()
        self.main_window_controller = MainWindowController(context)
        self.main_window_controller.closing.connect(self.close)

    @Slot()
    def save(self):
        self.closing.emit()

    @Slot()
    def close(self):
        self.closing.emit()
