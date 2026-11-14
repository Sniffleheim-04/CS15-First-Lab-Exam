from PySide6.QtWidgets import QMainWindow
from ui.main_ui import Ui_MainWindow

class MainView(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
