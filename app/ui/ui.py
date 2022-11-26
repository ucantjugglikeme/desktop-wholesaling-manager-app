import time
import ctypes
from sys import platform
from typing import TYPE_CHECKING

from PyQt5.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QDialog,
)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QMouseEvent, QIcon

from generated_uis.mainwnindow_v2 import UiMainWindow
from generated_uis.table_1_1 import UiForm as T1Form
from generated_uis.customer_menu import UiForm as T2Form
from generated_uis.manager_menu import UiForm as T3Form
from generated_uis.product_menu import UiForm as T5Form
from generated_uis.vendor_menu import UiForm as T6Form
from generated_uis.warehouse_menu import UiForm as T7Form
from generated_uis.login_dialog import UiDialog as LogInDialog
from generated_uis.signup_dialog import UiDialog as SignUpDialog
from generated_uis.info_dialog import UiDialog as InfoDialog
from generated_uis.get_vendors_table import UiFrame as TableGetVendors

from app.ui.table_masters import TableMaster
from app.back.utils import (
    in_rect, set_up_info_dialog
)
from app.entities.manager.views import (
    ManagerSignUpView, ManagerLogInView
)

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

        self.t2_form = T2Form()
        self.t3_form = T3Form()
        self.t5_form = T5Form()
        self.t6_form = T6Form()
        self.t7_form = T7Form()

        # Setting up application
        self.set_properties()
        self.set_signals()

        self.manager: "ManagerAuth" | None = None

        self.err_img = f"{self.app_dir}/resources/error.png"
        self.err_icon = f"{self.app_dir}/resources/error-icon.png"
        self.warn_img = f"{self.app_dir}/resources/warning-v2.png"
        self.warn_icon = f"{self.app_dir}/resources/warning-icon.png"
        self.ok_img = f"{self.app_dir}/resources/ok-mark-v2.png"
        self.ok_icon = f"{self.app_dir}/resources/ok-mark-icon.png"

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
                    set_up_info_dialog(
                        self.info_dialog, self.info_form,
                        text="Вы уже аворизовались",
                        icon_path=self.err_icon, img_path=self.err_img
                    )
                else:
                    self.login_dialog.exec()
            case "label_15":
                self.signup_dialog.exec()
            case "label_17":
                if not self.manager:
                    set_up_info_dialog(
                        self.info_dialog, self.info_form,
                        text="Вы ещё не вошли, чтобы выходить",
                        icon_path=self.err_icon, img_path=self.err_img
                    )
                else:
                    set_up_info_dialog(
                        self.info_dialog, self.info_form,
                        text="Вы вышли из учетной записи",
                        icon_path=self.ok_icon, img_path=self.ok_img
                    )
                    self.manager = None
            case "label_go_back":
                self.go_back(self.spawner.cur_table_widget_name)
            case _:
                self.define_clicked_label_actions(label)

    def go_back(self, widget_name):
        match widget_name:
            case "customers_table":
                self.t2_form.setupUi(self)
                self.setCentralWidget(self.t2_form.horizontalLayoutWidgetT2)
                self.spawner.cur_table_widget_name = ""
            case "managers_table":
                self.t3_form.setupUi(self)
                self.setCentralWidget(self.t3_form.horizontalLayoutWidgetT3)
                self.spawner.cur_table_widget_name = ""
            case "products_table":
                self.t5_form.setupUi(self)
                self.setCentralWidget(self.t5_form.horizontalLayoutWidgetT5)
                self.spawner.cur_table_widget_name = ""
            case "vendors_table":
                self.t6_form.setupUi(self)
                self.setCentralWidget(self.t6_form.horizontalLayoutWidgetT6)
                self.spawner.cur_table_widget_name = ""
            case "warehouses_table":
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
            case "label_2":
                self.t2_form.setupUi(self)
                self.setCentralWidget(self.t2_form.horizontalLayoutWidgetT2)
            case "label_T2_2":
                self.t1_form.setupUi(self)
                self.setCentralWidget(self.t1_form.horizontalLayoutWidgetT)
                self.spawner.spawn_get_customers_table()
            case "label_T2_3":
                self.t1_form.setupUi(self)
                self.setCentralWidget(self.t1_form.horizontalLayoutWidgetT)
                self.spawner.spawn_add_customers_table()
            case "label_T2_4":
                self.t1_form.setupUi(self)
                self.setCentralWidget(self.t1_form.horizontalLayoutWidgetT)
                self.spawner.spawn_mod_customers_table()
            case "label_T2_5":
                self.t1_form.setupUi(self)
                self.setCentralWidget(self.t1_form.horizontalLayoutWidgetT)
                self.spawner.spawn_delete_customers_table()
            case "label_3":
                self.t3_form.setupUi(self)
                self.setCentralWidget(self.t3_form.horizontalLayoutWidgetT3)
            case "label_T3_2":
                self.t1_form.setupUi(self)
                self.setCentralWidget(self.t1_form.horizontalLayoutWidgetT)
                self.spawner.spawn_get_managers_table()
            case "label_T3_4":
                self.t1_form.setupUi(self)
                self.setCentralWidget(self.t1_form.horizontalLayoutWidgetT)
                self.spawner.spawn_mod_managers_table()
            case "label_5":
                self.t5_form.setupUi(self)
                self.setCentralWidget(self.t5_form.horizontalLayoutWidgetT5)
            case "label_T5_2":
                self.t1_form.setupUi(self)
                self.setCentralWidget(self.t1_form.horizontalLayoutWidgetT)
                self.spawner.spawn_get_product_table()
            case "label_T5_3":
                self.t1_form.setupUi(self)
                self.setCentralWidget(self.t1_form.horizontalLayoutWidgetT)
                self.spawner.spawn_add_products_table()
            case "label_T5_4":
                self.t1_form.setupUi(self)
                self.setCentralWidget(self.t1_form.horizontalLayoutWidgetT)
                self.spawner.spawn_mod_products_table()
            case "label_T5_5":
                self.t1_form.setupUi(self)
                self.setCentralWidget(self.t1_form.horizontalLayoutWidgetT)
                self.spawner.spawn_del_product_table()
            case "label_6":
                self.t6_form.setupUi(self)
                self.setCentralWidget(self.t6_form.horizontalLayoutWidgetT6)
            case "label_T6_2":
                self.t1_form.setupUi(self)
                self.setCentralWidget(self.t1_form.horizontalLayoutWidgetT)
                self.spawner.spawn_get_vendors_table()
            case "label_T6_3":
                self.t1_form.setupUi(self)
                self.setCentralWidget(self.t1_form.horizontalLayoutWidgetT)
                self.spawner.spawn_add_vendors_table()
            case "label_T6_4":
                self.t1_form.setupUi(self)
                self.setCentralWidget(self.t1_form.horizontalLayoutWidgetT)
                self.spawner.spawn_mod_vendors_table()
            case "label_T6_5":
                self.t1_form.setupUi(self)
                self.setCentralWidget(self.t1_form.horizontalLayoutWidgetT)
                self.spawner.spawn_delete_vendors_table()
            case "label_7":
                self.t7_form.setupUi(self)
                self.setCentralWidget(self.t7_form.horizontalLayoutWidgetT7)
            case "label_T7_2":
                self.t1_form.setupUi(self)
                self.setCentralWidget(self.t1_form.horizontalLayoutWidgetT)
                self.spawner.spawn_get_warehouse_table()
            case "label_T7_3":
                self.t1_form.setupUi(self)
                self.setCentralWidget(self.t1_form.horizontalLayoutWidgetT)
                self.spawner.spawn_add_warehouses_table()
            case "label_T7_4":
                self.t1_form.setupUi(self)
                self.setCentralWidget(self.t1_form.horizontalLayoutWidgetT)
                self.spawner.spawn_mod_warehouses_table()
            case "label_T7_5":
                self.t1_form.setupUi(self)
                self.setCentralWidget(self.t1_form.horizontalLayoutWidgetT)
                self.spawner.spawn_del_warehouse_table()

    def get_table_labels(self, widget_name) -> list[QLabel]:
        match widget_name:
            case "horizontalLayoutWidgetT2":
                return [
                    self.t2_form.label_T2_2, self.t2_form.label_T2_3,
                    self.t2_form.label_T2_4, self.t2_form.label_T2_5,
                    self.t2_form.label_go_back
                ]
            case "horizontalLayoutWidgetT3":
                return [
                    self.t3_form.label_T3_2, self.t3_form.label_T3_4,
                    self.t3_form.label_go_back
                ]
            case "horizontalLayoutWidgetT5":
                return [
                    self.t5_form.label_T5_2, self.t5_form.label_T5_3,
                    self.t5_form.label_T5_4, self.t5_form.label_T5_5,
                    self.t5_form.label_go_back
                ]
            case "horizontalLayoutWidgetT6":
                return [
                    self.t6_form.label_T6_2, self.t6_form.label_T6_3,
                    self.t6_form.label_T6_4, self.t6_form.label_T6_5,
                    self.t6_form.label_go_back
                ]
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
            self.ui.label_13, self.ui.label_15, self.ui.label_17
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
            set_up_info_dialog(self.info_dialog, self.info_form, "Вы уже авторизовались", self.err_icon, self.err_img)
            return

        data = (
            self.login_form.lineEdit.text(),
            self.login_form.lineEdit_2.text(),
        )

        manager_login = ManagerLogInView(self.app)
        response_data = manager_login.login(data)
        self.manager = response_data[3]

        set_up_info_dialog(
            self.info_dialog, self.info_form,
            text=response_data[0], icon_path=response_data[1], img_path=response_data[2]
        )

    def signupClickedEvent(self):
        data = (
            self.signup_form.lineEdit.text(),
            self.signup_form.lineEdit_2.text(),
            self.signup_form.lineEdit_3.text(),
        )

        manager_signup = ManagerSignUpView(self.app)
        response_data = manager_signup.signup(data)

        set_up_info_dialog(
            self.info_dialog, self.info_form,
            text=response_data[0], icon_path=response_data[1], img_path=response_data[2]
        )

    def okInfoDialogClickedEvent(self):
        self.info_dialog.close()

# Needed platforms and imageformats in dir with python.exe
