from typing import Any

from PySide6 import QtCore
from PySide6.QtCore import QSettings


class SettingsManager(QtCore.QObject):
    def __init__(self):
        super().__init__()
        self._settings = QSettings(".config\\app.gft", QSettings.IniFormat)

    @property
    def settings(self):
        return self._settings

    def save(self, data: dict, prefix=''):
        for key, value in data.items():
            self.settings.setValue('/'.join([prefix, key]), value)

    def load(self, keys: list[str] | str, types: dict[str, Any] | list[Any], prefix: str) -> dict[str, Any]:
        res = {}
        try:
            if type(types) == dict:
                for key in keys:
                    res[key] = self.settings.value('/'.join([prefix, key]), defaultValue=None, type=types[key])
            elif type(types) == list:
                for key in keys:
                    res[key] = self.settings.value('/'.join([prefix, key]), defaultValue=None,
                                                   type=types[keys.index(key)])
        except Exception as e:
            print(e)
        return res
