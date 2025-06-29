from .moduleManager import ModuleManager


class AppContext:
    def __init__(self):
        self.moduleManager = ModuleManager()
        self.sessionManager = None
        self.themeManager = None
        self.settingsManager = None

    def create_module(self, module_name, *args, **kwargs):
        return self.moduleManager.create(module_name, *args, **kwargs)

    def settings(self):
        return self.settingsManager

    def session(self):
        return self.sessionManager

    def themes(self):
        return self.themeManager
