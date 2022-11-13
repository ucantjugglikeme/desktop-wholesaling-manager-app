from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.ui.ui import Ui
from PyQt5.QtWidgets import QDialog, QLineEdit
from app.ui.ui import T1Form

from generated_uis.get_vendors_table import UiFrame as TableGetVendors
from generated_uis.add_vendors_table import UiFrame as TableAddVendors
from generated_uis.modify_vendors_table import UiFrame as TableModVendors
from generated_uis.del_vendors_table import UiFrame as TableDelVendors

from generated_uis.update_vendors_dialog import UiDialog as DialogModVendors

from app.entities.vendor.views import *
from app.back.utils import *


VENDOR_HANDLERS = [
    "ID поставщика", "Наименование организации / ФИО", "Адрес поставщика",
    "Контактный телефон", "Электронная почта E-mail"
]


class TableMaster:
    def __init__(self, parent_ui: "Ui", related_form: T1Form):
        self.parent = parent_ui
        self.base_form = related_form
        self.cur_table_widget_name = ""

        self.table_get_vendor = TableGetVendors()
        self.table_add_vendor = TableAddVendors()
        self.table_mod_vendor = TableModVendors()
        self.table_del_vendor = TableDelVendors()

        self.dialog_mod_vendor = QDialog(self.parent)
        self.dialog_mod_vendor_form = DialogModVendors()
        self.dialog_mod_vendor_form.setupUi(self.dialog_mod_vendor)

        self.set_signals()

    def set_signals(self):
        self.dialog_mod_vendor_form.pushButton.clicked.connect(self.modifyVendorClickDialogEvent)

    # TABLES SPAWN POINT ------------------------------------------------------------------------

    def spawn_table(self, table, table_name, headers: list[str]):
        # setting up widgets
        table.setupUi(self.parent)
        self.base_form.verticalLayoutT1.addWidget(table.horizontalLayoutWidget)
        self.base_form.verticalLayoutT1.removeWidget(self.base_form.label)
        self.cur_table_widget_name = table_name

        # setting up table
        table.tableWidget.setColumnCount(len(headers))
        table.tableWidget.setHorizontalHeaderLabels(headers)
        table.tableWidget.resizeColumnsToContents()

    def spawn_get_vendors_table(self):
        headers = VENDOR_HANDLERS
        self.spawn_table(self.table_get_vendor, "vendors_table", headers)

        lines = (
            self.table_get_vendor.lineEdit_3, self.table_get_vendor.lineEdit_4,
            self.table_get_vendor.lineEdit_5, self.table_get_vendor.lineEdit_6,
            self.table_get_vendor.lineEdit_7,
        )
        self.table_get_vendor.pushButton.clicked.connect(
            lambda: self.listVendorsClickedEvent(self.table_get_vendor, lines)
        )

    def spawn_add_vendors_table(self):
        headers = VENDOR_HANDLERS
        self.spawn_table(self.table_add_vendor, "vendors_table", headers)

        self.table_add_vendor.pushButton.clicked.connect(self.addVendorClickEvent)

    def spawn_mod_vendors_table(self):
        headers = VENDOR_HANDLERS
        self.spawn_table(self.table_mod_vendor, "vendors_table", headers)

        lines = (
            None, self.table_mod_vendor.lineEdit_4, self.table_mod_vendor.lineEdit_5,
            self.table_mod_vendor.lineEdit_6, self.table_mod_vendor.lineEdit_7,
        )
        self.table_mod_vendor.comboBox.addItem("---")
        self.table_mod_vendor.pushButton.clicked.connect(
            lambda: self.listVendorsClickedEvent(
                self.table_mod_vendor, lines, lambda: add_combo_items(self.table_mod_vendor)
            )
        )
        self.table_mod_vendor.pushButton_2.clicked.connect(self.modifyVendorClickEvent)

    def spawn_delete_vendors_table(self):
        headers = VENDOR_HANDLERS
        self.spawn_table(self.table_del_vendor, "vendors_table", headers)

        lines = (
            self.table_del_vendor.lineEdit_3, self.table_del_vendor.lineEdit_4,
            self.table_del_vendor.lineEdit_5, self.table_del_vendor.lineEdit_6,
            self.table_del_vendor.lineEdit_7,
        )
        self.listVendorsClickedEvent(self.table_del_vendor, lines)
        self.table_del_vendor.pushButton.clicked.connect(self.deleteVendorClickEvent)

    # EVENTS ------------------------------------------------------------------------------------------------

    def listVendorsClickedEvent(self, table, lines: tuple, func=None):
        if table.tableWidget.rowCount() > 0:
            clear_table_widget(table.tableWidget)

        filter_params = [line.text() if (line is not None and line.text() != "") else None for line in lines]

        vendor_get = VendorGetView(self.parent.app)
        response_data = vendor_get.get(filter_params)

        fill_table_with_data(response_data, table.tableWidget)

        if func:
            func()

    def addVendorClickEvent(self):
        if self.table_add_vendor.tableWidget.rowCount() > 0:
            clear_table_widget(self.table_add_vendor.tableWidget)

        filter_params = [
            line.text() if (line.text() != "") else None for line in (
                self.table_add_vendor.lineEdit_4, self.table_add_vendor.lineEdit_5,
                self.table_add_vendor.lineEdit_6, self.table_add_vendor.lineEdit_7,
            )
        ]

        vendor_add = VendorAddView(self.parent.app)
        response_data = vendor_add.add(filter_params)
        fill_table_with_data([response_data], self.table_add_vendor.tableWidget)

    def modifyVendorClickEvent(self):
        vendor_id = int(self.table_mod_vendor.comboBox.currentText()) \
            if self.table_mod_vendor.comboBox.currentText() != "---" else None

        if not vendor_id:
            self.dialog_mod_vendor.exec()
            return

        update_values = get_vendors_update_values(self.table_mod_vendor)
        filter_values = [str(vendor_id), None, None, None, None]

        modify_vendors(VendorUpdateView, filter_values, update_values, self.parent)

    def modifyVendorClickDialogEvent(self):
        vendor_id = int(self.table_mod_vendor.comboBox.currentText()) \
            if self.table_mod_vendor.comboBox.currentText() != "---" else None

        update_values = get_vendors_update_values(self.table_mod_vendor)
        filter_values = [
            str(vendor_id) if vendor_id is not None else None,
            self.dialog_mod_vendor_form.lineEdit.text()
            if self.dialog_mod_vendor_form.lineEdit.text() != "" else None,
            self.dialog_mod_vendor_form.lineEdit_2.text()
            if self.dialog_mod_vendor_form.lineEdit_2.text() != "" else None,
            self.dialog_mod_vendor_form.lineEdit_3.text()
            if self.dialog_mod_vendor_form.lineEdit_3.text() != "" else None,
            self.dialog_mod_vendor_form.lineEdit_4.text()
            if self.dialog_mod_vendor_form.lineEdit_4.text() != "" else None,
        ]

        modify_vendors(VendorUpdateView, filter_values, update_values, self.parent)

    def deleteVendorClickEvent(self):
        lines = (
            self.table_del_vendor.lineEdit_3, self.table_del_vendor.lineEdit_4,
            self.table_del_vendor.lineEdit_5, self.table_del_vendor.lineEdit_6,
            self.table_del_vendor.lineEdit_7,
        )

        delete_params = [line.text() if (line.text() != "") else None for line in lines]

        vendor_get = VendorDeleteView(self.parent.app)
        response_data = vendor_get.delete(delete_params)

        self.listVendorsClickedEvent(
            self.table_del_vendor, (QLineEdit(), QLineEdit(), QLineEdit(), QLineEdit(), QLineEdit())
        )

        set_up_info_dialog(
            self.parent.info_dialog, self.parent.info_form,
            response_data[0], response_data[1], response_data[2]
        )
