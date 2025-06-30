from PySide6 import QtCore

from .main_window import MainWindowController
from ..core import register_module


@register_module('MainMenu')
class MainMenu(QtCore.QObject):
    def __init__(self, context):
        super().__init__()
        self.main_window_controller = MainWindowController(context)


