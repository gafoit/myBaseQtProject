from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Slot

from ..resources.MainWindowUI import Ui_Dialog


class MainMenuView(QtWidgets.QDialog):
    open_module_sig = QtCore.Signal(str)

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self._connect_ui()

    def _connect_ui(self):
        self.ui.Formula.clicked.connect(lambda: self.open_module('Formula'))
        self.ui.FindPair.clicked.connect(lambda: self.open_module('FindPair'))
        self.ui.Counting.clicked.connect(lambda: self.open_module('Counting'))
        self.ui.Concentration.clicked.connect(lambda: self.open_module('Concentration'))
        self.ui.Desc.clicked.connect(lambda: self.open_module('Desc'))
        self.ui.CloseButton.clicked.connect(self.reject)

    @Slot(str)
    def open_module(self, module: str):
        self.open_module_sig.emit(module)
