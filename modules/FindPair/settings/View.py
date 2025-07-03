from typing import Any

from PySide6.QtWidgets import QDialog

from ..resources.FindPairSettingsUI import Ui_Dialog


class FindPairSettingsView(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self._connect_ui()

    def _connect_ui(self):
        self.ui.save.clicked.connect(self.accept)
        self.ui.cancel.clicked.connect(self.reject)
        self.ui.restore.clicked.connect(self._restore)

    def _restore(self):
        self.ui.preview_time.setValue(1000)
        self.ui.pair_count.setValue(2)
        self.ui.Endless.setChecked(False)

    def set_settings(self, data: dict[str, Any]):
        self.ui.preview_time.setValue(data['preview_time'])
        self.ui.pair_count.setValue(data['pair_count'])
        self.ui.Endless.setChecked(data['Endless'])

    def get_settings(self):
        return {"preview_time": self.ui.preview_time.value(), "pair_count": self.ui.pair_count.value(),
                "Endless": self.ui.Endless.isChecked()}
