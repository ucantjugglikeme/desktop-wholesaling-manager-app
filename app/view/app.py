import sys
from PyQt5 import QtWidgets
from generated_uis.mainwindow import UiMainWindow


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()

        self.ui = UiMainWindow()
        self.ui.setupUi(self)
        self.setCentralWidget(self.ui.layoutWidget)

        self.set_properties()

    def set_properties(self):
        self.setWindowTitle("DWMA")
        self.setMinimumSize(800, 600)

        self.ui.menubar.setStyleSheet("background-color: rgb(252, 239, 229);")
        self.ui.statusbar.setStyleSheet("background-color: rgb(203, 191, 182);")
        self.ui.label.setStyleSheet("border-color: rgb(170, 170, 127);")


def setup_app():
    app = QtWidgets.QApplication([])

    m_window = Ui()
    m_window.show()
    sys.exit(app.exec())
