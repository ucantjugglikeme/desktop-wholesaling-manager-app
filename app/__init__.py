import sys
from PyQt5 import QtWidgets
from app.view.ui import Ui


class App:
    def __init__(self, q_app: QtWidgets.QApplication, m_win: Ui):
        self.q_app = q_app
        self.m_win = m_win

    def exec(self):
        self.m_win.show()
        return self.q_app.exec()


def setup_app(app_dir: str):
    q_app = QtWidgets.QApplication([])
    m_window = Ui(app_dir)
    app = App(q_app, m_window)

    sys.exit(app.exec())
