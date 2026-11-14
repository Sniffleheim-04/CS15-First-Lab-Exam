import sys

from PySide6.QtWidgets import QApplication

from model.main_model import MainModel
from view.main_view import MainView
from controller.main_controller import MainController


if __name__ == "__main__":
    app = QApplication(sys.argv)

    model = MainModel()
    view = MainView()
    controller = MainController(model, view)

    view.show()

    sys.exit(app.exec())