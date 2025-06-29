from .main_window import BaseMainWindowController
from ..core import register_module


@register_module('Base')
class BaseModule:
    def __init__(self, context):
        self.context = context
        self.main_controller = BaseMainWindowController(context)
        self.settings_controller = None
        self.result_controller = None

    def start(self): ...

    def finish(self): ...

    def close(self): ...

    def _connect_controllers(self): ...
