from PySide6 import QtCore

from ...base_module.main_window import BaseMainWindowController
from .View import MainMenuView
from .Model import MainMenuModel


class MainWindowController(BaseMainWindowController):
    save = QtCore.Signal()
    closing = QtCore.Signal()

    def __init__(self, context):
        super().__init__(context)
        self.view = MainMenuView()
        self.model = MainMenuModel(context)
        self._connect_view()

    def show(self):
        self.view.show()

    def hide(self):
        self.view.hide()

    def close(self):
        self.view.close()

    def _connect_view(self):
        self.model.save.connect(lambda: self.save.emit())
        self.view.closing.connect(lambda: self.closing.emit())
        self.view.open_module_sig.connect(lambda _: print(_))
