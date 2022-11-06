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

from generated_uis.mainwnindow_v2 import UiMainWindow
from generated_uis.table_1_1 import UiForm as T1Form
from generated_uis.vendor_menu import UiForm as T7Form
from generated_uis.login_dialog import UiDialog as LogInDialog
from generated_uis.signup_dialog import UiDialog as SignUpDialog
from generated_uis.info_dialog import UiDialog as InfoDialog
from generated_uis.get_vendors_table import UiFrame as TableGetVendors

from app.ui.table_masters import TableMaster
from app.back.utils import in_rect
from app.entities.manager import ManagerSignUpView, ManagerLogInView

if TYPE_CHECKING:
    from app import App
    from app.entities.manager.models import ManagerAuth


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
        self.list_vendors_table = TableGetVendors()
        self.spawner = TableMaster(self, self.t1_form)

        self.t7_form = T7Form()

        # Setting up application
        self.set_properties()
        self.set_signals()

        self.manager: "ManagerAuth" | None = None

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
                if self.manager:
                    self.info_form.label_2.setText("Вы уже авторизовались")
                    self.info_dialog.setWindowIcon(QIcon(f"{self.app.m_win.app_dir}/resources/error-icon.png"))
                    self.info_form.label.setPixmap(QPixmap(f"{self.app.m_win.app_dir}/resources/error.png").
                                                   scaled(100, 100))
                    self.info_dialog.exec()
                else:
                    self.login_dialog.exec()
            case "label_15":
                self.signup_dialog.exec()
            case "label_17":
                if not self.manager:
                    self.info_form.label_2.setText("Вы ещё не вошли, чтобы выходить")
                    self.info_dialog.setWindowIcon(QIcon(f"{self.app.m_win.app_dir}/resources/error-icon.png"))
                    self.info_form.label.setPixmap(QPixmap(f"{self.app.m_win.app_dir}/resources/error.png").
                                                   scaled(100, 100))
                else:
                    self.info_form.label_2.setText("Вы вышли из учетной записи")
                    self.info_dialog.setWindowIcon(QIcon(f"{self.app.m_win.app_dir}/resources/ok-mark-icon.png"))
                    self.info_form.label.setPixmap(QPixmap(f"{self.app.m_win.app_dir}/resources/ok-mark-v2.png").
                                                   scaled(100, 100))
                    self.manager = None
                self.info_dialog.exec()
            case "label_go_back":
                self.go_back(self.spawner.cur_table_widget_name)
            case _:
                self.define_clicked_label_actions(label)

    def go_back(self, widget_name):
        match widget_name:
            case "vendors_table":
                self.t7_form.setupUi(self)
                self.setCentralWidget(self.t7_form.horizontalLayoutWidgetT7)
                self.spawner.cur_table_widget_name = ""
            case _:
                saved_size = QSize(self.width(), self.height())
                self.ui.setupUi(self)
                self.refresh_m_window(saved_size)
                self.setCentralWidget(self.ui.layoutWidget)

    def define_clicked_label_actions(self, label: QLabel):
        match label.objectName():
            case "label_7":
                self.t7_form.setupUi(self)
                self.setCentralWidget(self.t7_form.horizontalLayoutWidgetT7)
            case "label_9":
                self.spawner.spawn_get_vendors_table()
                # self.listVendorsClickedEvent()
            case "label_T7_2":
                self.t1_form.setupUi(self)
                self.setCentralWidget(self.t1_form.horizontalLayoutWidgetT)
                self.spawner.spawn_get_vendors_table()
            case "label_T7_3":
                self.t1_form.setupUi(self)
                self.setCentralWidget(self.t1_form.horizontalLayoutWidgetT)
                self.spawner.spawn_add_vendors_table()
            case "label_T7_4":
                self.t1_form.setupUi(self)
                self.setCentralWidget(self.t1_form.horizontalLayoutWidgetT)
                self.spawner.spawn_mod_vendors_table()
            case "label_T7_5":
                self.t1_form.setupUi(self)
                self.setCentralWidget(self.t1_form.horizontalLayoutWidgetT)
                self.spawner.spawn_delete_vendors_table()

    def get_table_labels(self, widget_name) -> list[QLabel]:
        match widget_name:
            case "horizontalLayoutWidgetT7":
                return [
                    self.t7_form.label_T7_2, self.t7_form.label_T7_3,
                    self.t7_form.label_T7_4, self.t7_form.label_T7_5,
                    self.t7_form.label_go_back
                ]
            case "horizontalLayoutWidgetT":
                return [self.t1_form.label_go_back]
            case _:
                return []

    def mousePressEvent(self, a0: QMouseEvent) -> None:
        labels = [
            self.ui.label_2, self.ui.label_3, self.ui.label_4,
            self.ui.label_5, self.ui.label_6, self.ui.label_7,
            self.ui.label_8, self.ui.label_13, self.ui.label_15,
            self.ui.label_17
        ]  # if self.manager else [self.ui.label_13, self.ui.label_15, self.ui.label_17]

        widget_name = self.centralWidget().objectName()
        match widget_name:
            case "layoutWidget":
                pass
            case _:
                labels = self.get_table_labels(widget_name)

        for label in labels:
            if in_rect(
                    a0.x(), a0.y(), label.x(), label.y(),
                    label.size().width(), label.size().height()
            ):
                QApplication.setOverrideCursor(Qt.PointingHandCursor)
                self.on_click_label(label)
                break

    def loginClickedEvent(self):
        if self.manager:
            self.info_form.label_2.setText("Вы уже авторизовались")
            self.info_dialog.setWindowIcon(QIcon(f"{self.app.m_win.app_dir}/resources/error-icon.png"))
            self.info_form.label.setPixmap(QPixmap(f"{self.app.m_win.app_dir}/resources/error.png").
                                           scaled(100, 100))
            self.info_dialog.exec()
            return

        data = (
            self.login_form.lineEdit.text(),
            self.login_form.lineEdit_2.text(),
        )

        manager_login = ManagerLogInView(self.app)
        response_data = manager_login.login(data)
        self.manager = response_data[3]

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

# Needed platforms and imageformats in dir with python.exe
