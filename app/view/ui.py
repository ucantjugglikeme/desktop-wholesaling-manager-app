import time
from PyQt5 import QtWidgets, QtGui, QtCore
from generated_uis.mainwindow2 import UiMainWindow
from generated_uis.table_1 import UiForm as T1Form
from app.view.signals import LabelSignal
from app.back.utils import in_rect


class Ui(QtWidgets.QMainWindow):
    def __init__(self, app_dir: str):
        super(Ui, self).__init__()

        self.app_dir = app_dir

        self.ui = UiMainWindow()
        self.ui.setupUi(self)
        self.setCentralWidget(self.ui.layoutWidget)
        self.centralWidget().setMouseTracking(True)

        self.t1_form = T1Form()

        self.set_properties()
        self.set_signals()

    def set_properties(self):
        self.setWindowTitle("DWMA")
        self.setMinimumSize(800, 600)

        self.ui.menubar.setStyleSheet("background-color: rgb(252, 239, 229);")
        self.ui.statusbar.setStyleSheet("background-color: rgb(203, 191, 182);")

    def set_signals(self):
        # defining signals

        self.label1_signal = LabelSignal()
        self.label1_signal.clicked.connect(self.open_table)

    def open_table(self):
        # defining actions when signal emitted

        self.t1_form.setupUi(self)
        self.setCentralWidget(self.t1_form.horizontalLayoutWidgetT1)

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        # {a0.globalPos().x()}, {a0.globalPos().y()}
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
                QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.PointingHandCursor)
                self.label1_signal.click()

        time.sleep(0.2)
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.ArrowCursor)
