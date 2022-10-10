import sys
from PyQt5 import QtWidgets
from app.view.ui import Ui


def setup_app(app_dir: str):
    app = QtWidgets.QApplication([])

    m_window = Ui(app_dir)
    m_window.show()
    sys.exit(app.exec())
