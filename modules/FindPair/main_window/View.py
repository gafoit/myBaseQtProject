from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QPushButton

from ..resources.FindPairMainWindowUI import Ui_MainWindow


class FindPairMainWindow(QtWidgets.QMainWindow):
    start_game_signal = QtCore.Signal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._connect_ui()

    def _connect_ui(self):
        self.ui.StartButton.clicked.connect(lambda: self.start_game_signal.emit())

    def update_labels(self, found: str, left: str):
        self.ui.PairsLeft.setText(left)
        self.ui.PairsFound.setText(found)

    def add_cards(self, cards_list: list[list[int]]):
        for i in self.ui.gridLayout_2.children():
            if isinstance(i, QtWidgets.QWidget):
                i.deleteLater()
        for i in range(len(cards_list)):
            for j in range(len(cards_list[i])):
                self.ui.gridLayout_2.addWidget(QPushButton(str(cards_list[i][j])), i, j)
