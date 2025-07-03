from typing import Any

from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Slot

from .Model import FindPairModel
from .View import FindPairMainWindow


class FindPairController(QtCore.QObject):
    def __init__(self, context):
        super().__init__()
        self.context = context
        self.view = FindPairMainWindow()
        self.model = FindPairModel(context)
        self.connect_view_to_model()
        self.start()

    @Slot()
    def start(self):
        self.model.create_cards()
        self.view.add_cards(self.model.get_cards())

    def connect_view_to_model(self):
        self.view.start_game_signal.connect(self.start)

