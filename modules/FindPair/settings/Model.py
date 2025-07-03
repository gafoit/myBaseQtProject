import os
from typing import Any

from PySide6 import QtCore


class FindPairSettingsModel(QtCore.QObject):
    def __init__(self, context):
        super().__init__()
        self.prefix = 'FindPair'
        self.settings = context.settingsManager
