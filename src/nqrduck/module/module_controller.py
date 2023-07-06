from PyQt5.QtCore import QObject

class ModuleController(QObject):
    def __init__(self, module):
        super().__init__()
        self._module = module

    def on_loading(self):
        pass

    def process_signals(self, key, value):
        pass