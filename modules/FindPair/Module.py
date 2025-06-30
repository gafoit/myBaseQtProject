from PySide6 import QtCore

from .main_window import FindPairController
from ..core import register_module


@register_module('FindPair')
class FindPair(QtCore.QObject):
    def __init__(self, context):
        super().__init__()
        self.main_window_controller = FindPairController(context)
