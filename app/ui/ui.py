import time
from typing import TYPE_CHECKING
import ctypes
from sys import platform

from PyQt5.QtWidgets import (
    QMainWindow,
    QApplication,
    QLabel,
    QDialog,
)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QMouseEvent, QIcon, QPixmap

from generated_uis.mainwindow2 import UiMainWindow
from generated_uis.table_1_1 import UiForm as T1Form
from generated_uis.login_dialog import UiDialog as LogInDialog
from generated_uis.signup_dialog import UiDialog as SignUpDialog
from generated_uis.info_dialog import UiDialog as InfoDialog

from app.ui.signals import LabelSignal
from app.ui.spawner import Spawner
from app.back.utils import in_rect
from app.manager.views import ManagerSignUpView, ManagerLogInView
from app.vendor.views import VendorGetView

if TYPE_CHECKING:
    from app import App


class Ui(QMainWindow):
    def __init__(self, app: "App", app_dir: str):
        super(Ui, self).__init__()

        self.app = app
        self.app_dir = app_dir

        # Linking generated windows with application
        self.ui = UiMainWindow()
        self.ui.setupUi(self)
        self.setCentralWidget(self.ui.layoutWidget)

        self.signup_dialog = QDialog(self)
        self.signup_form = SignUpDialog()
        self.signup_form.setupUi(self.signup_dialog)

        self.login_dialog = QDialog(self)
        self.login_form = LogInDialog()
        self.login_form.setupUi(self.login_dialog)

        self.info_dialog = QDialog(self)
        self.info_form = InfoDialog()
        self.info_form.setupUi(self.info_dialog)

        self.t1_form = T1Form()
        self.spawner = Spawner(self, self.t1_form)

        # Setting up application
        self.set_properties()
        self.set_signals()

    def set_properties(self):
        self.setWindowTitle("DWMA")
        self.setMinimumSize(800, 600)

        self.ui.menubar.setStyleSheet("background-color: rgb(252, 239, 229);")
        self.ui.statusbar.setStyleSheet("background-color: rgb(203, 191, 182);")

        self.login_dialog.setWindowIcon(QIcon(f"{self.app_dir}/resources/log-in-v3.png"))
        self.signup_dialog.setWindowIcon(QIcon(f"{self.app_dir}/resources/sign-up-v3.png"))

        self.setWindowIcon(QIcon(f"{self.app_dir}/resources/IIT-small.jpg"))
        if platform == 'win32':
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
                'rtumirea.dwma.ui.version1'
            )

    def refresh_m_window(self, saved_size: QSize):
        self.setWindowTitle("DWMA")
        self.setMinimumSize(800, 600)
        self.resize(saved_size.width(), saved_size.height())

        self.ui.menubar.setStyleSheet("background-color: rgb(252, 239, 229);")
        self.ui.statusbar.setStyleSheet("background-color: rgb(203, 191, 182);")

    def set_signals(self):
        self.login_form.pushButton.clicked.connect(self.loginClickedEvent)
        self.signup_form.pushButton.clicked.connect(self.signupClickedEvent)
        self.info_form.pushButton.clicked.connect(self.okInfoDialogClickedEvent)

    def on_click_label(self, label: QLabel):
        # defining actions when signal emitted

        time.sleep(0.2)
        QApplication.restoreOverrideCursor()

        match label.objectName():
            case "label_13":
                self.login_dialog.exec()
            case "label_15":
                self.signup_dialog.exec()
            case "label_17":
                saved_size = QSize(self.width(), self.height())
                self.ui.setupUi(self)
                self.refresh_m_window(saved_size)
                self.setCentralWidget(self.ui.layoutWidget)
            case _:
                self.t1_form.setupUi(self)
                self.setCentralWidget(self.t1_form.horizontalLayoutWidgetT1)
                self.define_clicked_label_actions(label)

    def define_clicked_label_actions(self, label: QLabel):
        match label.objectName():
            case "label_9":
                self.spawner.spawn_get_vendors_table()
                # self.listVendorsClickedEvent()

    def mousePressEvent(self, a0: QMouseEvent) -> None:
        m_win_labels = [
            self.ui.label_4, self.ui.label_3, self.ui.label_2,
            self.ui.label_8, self.ui.label_6, self.ui.label_7,
            self.ui.label_10, self.ui.label_9, self.ui.label_13,
            self.ui.label_15,
        ]

        try:
            table1_labels = [
                self.t1_form.label_17
            ]
        except AttributeError:
            table1_labels = []

        match self.centralWidget().objectName():
            case 'layoutWidget':
                labels = m_win_labels.copy()
            case _:
                labels = table1_labels.copy()

        for label in labels:
            if in_rect(
                    a0.x(), a0.y(), label.x(), label.y(),
                    label.size().width(), label.size().height()
            ):
                QApplication.setOverrideCursor(Qt.PointingHandCursor)
                self.on_click_label(label)
                break

    def loginClickedEvent(self):
        data = (
            self.login_form.lineEdit.text(),
            self.login_form.lineEdit_2.text(),
        )

        manager_login = ManagerLogInView(self.app)
        response_data = manager_login.login(data)

        self.info_dialog.setWindowIcon(QIcon(response_data[0]))
        self.info_form.label.setPixmap(QPixmap(response_data[1]).scaled(100, 100))
        self.info_form.label_2.setText(response_data[2])
        self.info_dialog.exec()

    def signupClickedEvent(self):
        data = (
            self.signup_form.lineEdit.text(),
            self.signup_form.lineEdit_2.text(),
            self.signup_form.lineEdit_3.text(),
        )

        manager_signup = ManagerSignUpView(self.app)
        response_data = manager_signup.signup(data)

        self.info_dialog.setWindowIcon(QIcon(response_data[0]))
        self.info_form.label.setPixmap(QPixmap(response_data[1]).scaled(100, 100))
        self.info_form.label_2.setText(response_data[2])
        self.info_dialog.exec()

    def okInfoDialogClickedEvent(self):
        self.info_dialog.close()

    def listVendorsClickedEvent(self):
        vendor_get = VendorGetView(self.app)
        response_data = vendor_get.get()
        print(response_data)

# Needed platforms and imageformats in dir with python.exe
