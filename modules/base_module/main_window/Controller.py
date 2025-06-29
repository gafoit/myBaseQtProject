from PySide6 import QtWidgets, QtCore


class BaseMainWindowController(QtCore.QObject):
    settingsSignal = QtCore.Signal()
    menuSignal = QtCore.Signal()
    resultSignal = QtCore.Signal()

    def __init__(self, context, /):
        super().__init__()
        self.context = context

    def show(self): ...

    def open_settings(self):
        self.settingsSignal.emit()

    def open_menu(self):
        self.menuSignal.emit()

    def open_results(self):
        self.resultSignal.emit()

    def hide(self): ...

    def _connect_view(self): ...
