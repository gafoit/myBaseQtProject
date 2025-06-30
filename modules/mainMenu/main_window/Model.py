from PySide6 import QtCore
from PySide6.QtCore import Slot, QObject


class MainMenuModel(QObject):
    def __init__(self, context, /):
        super().__init__()
        self.context = context

    @Slot(str)
    def open(self, module_name):
        self.context.create(module_name, self.context)
