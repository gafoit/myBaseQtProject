from PySide6 import QtCore

from .main_window import FindPairController
from .settings import FindPairSettingsController
from ..core import register_module


@register_module('FindPair')
class FindPair(QtCore.QObject):
    def __init__(self, context):
        super().__init__()
        self.main_window_controller = FindPairController(context)
        self.settings_window_controller = FindPairSettingsController(context)
        self._connect_parts()

    def open_settings(self):
        self.settings_window_controller.show()

    def _connect_parts(self):
        self.main_window_controller.view.ui.ModeOptions_2.triggered.connect(self.open_settings)
        self.settings_window_controller.view.accepted.connect(self.main_window_controller.start)
