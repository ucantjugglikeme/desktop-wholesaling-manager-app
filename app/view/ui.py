import time
from typing import TYPE_CHECKING
import ctypes
from sys import platform

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMouseEvent, QIcon

from generated_uis.mainwindow2 import UiMainWindow
from generated_uis.table_1 import UiForm as T1Form

from app.view.signals import LabelSignal
from app.back.utils import in_rect

if TYPE_CHECKING:
    from app import App


class Ui(QMainWindow):
    def __init__(self, app: "App", app_dir: str):
        super(Ui, self).__init__()

        self.app = app
        self.app_dir = app_dir

        self.ui = UiMainWindow()
        self.ui.setupUi(self)
        self.setCentralWidget(self.ui.layoutWidget)

        self.t1_form = T1Form()

        self.set_properties()
        self.set_signals()

    def set_properties(self):
        self.setWindowTitle("DWMA")
        self.setMinimumSize(800, 600)

        self.ui.menubar.setStyleSheet("background-color: rgb(252, 239, 229);")
        self.ui.statusbar.setStyleSheet("background-color: rgb(203, 191, 182);")

        self.setWindowIcon(QIcon(f"{self.app_dir}/resources/IIT-small.jpg"))
        if platform == 'win32':
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
                'rtumirea.dwma.ui.version1'
            )

    def set_signals(self):
        # defining signals

        self.label1_signal = LabelSignal()
        self.label1_signal.clicked.connect(self.open_table)

    def open_table(self):
        # defining actions when signal emitted

        self.t1_form.setupUi(self)
        self.setCentralWidget(self.t1_form.horizontalLayoutWidgetT1)

    def mousePressEvent(self, a0: QMouseEvent) -> None:
        if self.centralWidget().objectName() != 'layoutWidget':
            return

        labels = [
            self.ui.label_4, self.ui.label_3, self.ui.label_2,
            self.ui.label_8, self.ui.label_6, self.ui.label_7,
            self.ui.label_10, self.ui.label_9
        ]

        for label in labels:
            if in_rect(
                a0.x(), a0.y(), label.x(), label.y(),
                label.size().width(), label.size().height()
            ):
                QApplication.setOverrideCursor(Qt.PointingHandCursor)
                self.label1_signal.click()

        time.sleep(0.2)
        QApplication.restoreOverrideCursor()

# Needed platforms and imageformats in dir with python.exe
