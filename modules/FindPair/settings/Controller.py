from typing import Any

from PySide6 import QtCore

from .Model import FindPairSettingsModel
from .View import FindPairSettingsView


class FindPairSettingsController(QtCore.QObject):
    def __init__(self, context):
        super().__init__()
        self.context = context
        self.view = FindPairSettingsView()
        self.model = FindPairSettingsModel(context)
        self._connect_view()

    def show(self):
        self.view.set_settings(self.context.settingsManager.load(
            ['pair_count', 'preview_time', 'Endless'], [int, int, bool], 'FindPair'))
        self.view.show()

    def _connect_view(self):
        self.view.accepted.connect(lambda: self.model.settings.save(self.view.get_settings(), self.model.prefix))
