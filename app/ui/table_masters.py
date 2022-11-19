from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.ui.ui import Ui
from PyQt5.QtWidgets import QDialog, QLineEdit
from app.ui.ui import T1Form

from generated_uis.get_vendors_table import UiFrame as TableGetVendors
from generated_uis.add_vendors_table import UiFrame as TableAddVendors
from generated_uis.modify_vendors_table import UiFrame as TableModVendors
from generated_uis.del_vendors_table import UiFrame as TableDelVendors

from generated_uis.get_warehouses_table import UiFrame as TableGetWarehouses
from generated_uis.add_warehouses_table import UiFrame as TableAddWarehouses
from generated_uis.modify_warehouses_table import UiFrame as TableModWarehouses
from generated_uis.del_warehouses_table import UiFrame as TableDelWarehouses

from generated_uis.get_products_table import UiFrame as TableGetProducts

from generated_uis.update_vendors_dialog import UiDialog as DialogModVendors
from generated_uis.update_warehouses_dialog import UiDialog as DialogModWarehouses

from app.entities.vendor.views import *
from app.entities.warehouse.views import *
from app.entities.product.views import *
from app.back.utils import *


VENDOR_HANDLERS = [
    "ID поставщика", "Наименование организации / ФИО", "Адрес поставщика",
    "Контактный телефон", "Электронная почта E-mail"
]
WAREHOUSE_HANDLERS = ["ID склада", "Адрес склада"]
PRODUCT_HANDLERS = [
    "ID товара", "Наименование товара", "Стоимость товара", "Кол-во товара",
    "ID категории товара", "ID склада", "ID поставщика"
]
PR_CATEGORY_HANDLERS = ["ID категории товара", "Категория товара"]


class TableMaster:
    def __init__(self, parent_ui: "Ui", related_form: T1Form):
        self.parent = parent_ui
        self.base_form = related_form
        self.cur_table_widget_name = ""

        self.table_get_vendor = TableGetVendors()
        self.table_add_vendor = TableAddVendors()
        self.table_mod_vendor = TableModVendors()
        self.table_del_vendor = TableDelVendors()

        self.table_get_warehouses = TableGetWarehouses()
        self.table_add_warehouses = TableAddWarehouses()
        self.table_mod_warehouses = TableModWarehouses()
        self.table_del_warehouses = TableDelWarehouses()

        self.table_get_product = TableGetProducts()

        self.dialog_mod_vendor = QDialog(self.parent)
        self.dialog_mod_vendor_form = DialogModVendors()
        self.dialog_mod_vendor_form.setupUi(self.dialog_mod_vendor)

        self.dialog_mod_warehouse = QDialog(self.parent)
        self.dialog_mod_warehouse_form = DialogModWarehouses()
        self.dialog_mod_warehouse_form.setupUi(self.dialog_mod_warehouse)

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

    def setup_extra_table(self, tableWidget, headers: list[str]):
        tableWidget.setColumnCount(len(headers))
        tableWidget.setHorizontalHeaderLabels(headers)
        tableWidget.resizeColumnsToContents()

    def spawn_get_vendors_table(self):
        headers = VENDOR_HANDLERS
        self.spawn_table(self.table_get_vendor, "vendors_table", headers)

        lines = (
            self.table_get_vendor.lineEdit_3, self.table_get_vendor.lineEdit_4,
            self.table_get_vendor.lineEdit_5, self.table_get_vendor.lineEdit_6,
            self.table_get_vendor.lineEdit_7,
        )
        self.table_get_vendor.pushButton.clicked.connect(
            lambda: self.listSmthClickedEvent(self.table_get_vendor, VendorGetView, lines)
        )

    def spawn_add_vendors_table(self):
        headers = VENDOR_HANDLERS
        self.spawn_table(self.table_add_vendor, "vendors_table", headers)

        filter_lines = [
            self.table_add_vendor.lineEdit_4, self.table_add_vendor.lineEdit_5,
            self.table_add_vendor.lineEdit_6, self.table_add_vendor.lineEdit_7,
        ]

        self.table_add_vendor.pushButton.clicked.connect(
            lambda: self.addSmthClickEvent(self.table_add_vendor, VendorAddView, filter_lines)
        )

    def spawn_mod_vendors_table(self):
        headers = VENDOR_HANDLERS
        self.spawn_table(self.table_mod_vendor, "vendors_table", headers)

        lines = (
            None, self.table_mod_vendor.lineEdit_4, self.table_mod_vendor.lineEdit_5,
            self.table_mod_vendor.lineEdit_6, self.table_mod_vendor.lineEdit_7,
        )
        self.table_mod_vendor.comboBox.addItem("---")
        self.table_mod_vendor.pushButton.clicked.connect(
            lambda: self.listSmthClickedEvent(
                self.table_mod_vendor, VendorGetView, lines, lambda: add_combo_items(self.table_mod_vendor)
            )
        )

        filter_values = [None, None, None, None, None]
        self.dialog_mod_vendor_form.pushButton.clicked.connect(
            lambda: self.modifySmthClickDialogEvent(
                self.table_mod_vendor, self.dialog_mod_vendor_form, get_vendors_update_values,
                get_vendors_filter_values, modify_vendors, VendorUpdateView
            )
        )
        self.table_mod_vendor.pushButton_2.clicked.connect(
            lambda: self.modifySmthClickEvent(
                self.table_mod_vendor, self.dialog_mod_vendor, get_vendors_update_values, filter_values,
                modify_vendors, VendorUpdateView
            )
        )

    def spawn_delete_vendors_table(self):
        headers = VENDOR_HANDLERS
        self.spawn_table(self.table_del_vendor, "vendors_table", headers)

        lines = (
            self.table_del_vendor.lineEdit_3, self.table_del_vendor.lineEdit_4,
            self.table_del_vendor.lineEdit_5, self.table_del_vendor.lineEdit_6,
            self.table_del_vendor.lineEdit_7,
        )
        self.listSmthClickedEvent(self.table_del_vendor, VendorGetView, lines)
        self.table_del_vendor.pushButton.clicked.connect(
            lambda: self.deleteSmthClickEvent(self.table_del_vendor, lines, VendorDeleteView, VendorGetView)
        )

    def spawn_get_warehouse_table(self):
        headers = WAREHOUSE_HANDLERS
        self.spawn_table(self.table_get_warehouses, "warehouses_table", headers)

        lines = (self.table_get_warehouses.lineEdit_3, self.table_get_warehouses.lineEdit_4)
        self.table_get_warehouses.pushButton.clicked.connect(
            lambda: self.listSmthClickedEvent(self.table_get_warehouses, WarehouseGetView, lines)
        )

    def spawn_add_warehouses_table(self):
        headers = WAREHOUSE_HANDLERS
        self.spawn_table(self.table_add_warehouses, "warehouses_table", headers)

        filter_lines = [self.table_add_warehouses.lineEdit_4]

        self.table_add_warehouses.pushButton.clicked.connect(
            lambda: self.addSmthClickEvent(self.table_add_warehouses, WarehouseAddView, filter_lines)
        )

    def spawn_mod_warehouses_table(self):
        headers = WAREHOUSE_HANDLERS
        self.spawn_table(self.table_mod_warehouses, "warehouses_table", headers)

        lines = (None, self.table_mod_warehouses.lineEdit_4,)
        self.table_mod_warehouses.comboBox.addItem("---")
        self.table_mod_warehouses.pushButton.clicked.connect(
            lambda: self.listSmthClickedEvent(
                self.table_mod_warehouses, WarehouseGetView, lines, lambda: add_combo_items(self.table_mod_warehouses)
            )
        )

        filter_values = [None, None]
        self.dialog_mod_warehouse_form.pushButton.clicked.connect(
            lambda: self.modifySmthClickDialogEvent(
                self.table_mod_warehouses, self.dialog_mod_warehouse_form, get_warehouses_update_values,
                get_warehouses_filter_values, modify_warehouses, WarehouseUpdateView
            )
        )
        self.table_mod_warehouses.pushButton_2.clicked.connect(
            lambda: self.modifySmthClickEvent(
                self.table_mod_warehouses, self.dialog_mod_warehouse, get_warehouses_update_values, filter_values,
                modify_warehouses, WarehouseUpdateView
            )
        )

    def spawn_del_warehouse_table(self):
        headers = WAREHOUSE_HANDLERS
        self.spawn_table(self.table_del_warehouses, "warehouses_table", headers)

        lines = (self.table_del_warehouses.lineEdit_3, self.table_del_warehouses.lineEdit_4)
        self.listSmthClickedEvent(self.table_del_warehouses, WarehouseGetView, lines)
        self.table_del_warehouses.pushButton.clicked.connect(
            lambda: self.deleteSmthClickEvent(self.table_del_warehouses, lines, WarehouseDeleteView, WarehouseGetView)
        )

    def spawn_get_product_table(self):
        headers = PRODUCT_HANDLERS
        self.spawn_table(self.table_get_product, "products_table", headers)
        headers = PR_CATEGORY_HANDLERS
        self.setup_extra_table(self.table_get_product.tableWidget_2, headers)

        lines = (
            self.table_get_product.lineEdit_3, self.table_get_product.lineEdit_4,
            self.table_get_product.lineEdit_5, self.table_get_product.lineEdit_6,
            self.table_get_product.lineEdit_7, self.table_get_product.lineEdit_8,
            self.table_get_product.lineEdit_9
        )
        self.table_get_product.pushButton.clicked.connect(
            lambda: self.listSmthClickedEvent(self.table_get_product, ProductGetView, lines)
        )

    # EVENTS ------------------------------------------------------------------------------------------------

    def listSmthClickedEvent(self, table, SmthGetView, lines: tuple, func=None):
        if table.tableWidget.rowCount() > 0:
            clear_table_widget(table.tableWidget)

        filter_params = [line.text() if (line is not None and line.text() != "") else None for line in lines]

        smth_get = SmthGetView(self.parent.app)
        response_data = smth_get.get(filter_params)

        fill_table_with_data(response_data, table.tableWidget)

        if func:
            func()

    def addSmthClickEvent(self, table, SmthAddView, filter_lines):
        if table.tableWidget.rowCount() > 0:
            clear_table_widget(table.tableWidget)

        filter_params = [f_line.text() if (f_line.text() != "") else None for f_line in filter_lines]

        smth_add = SmthAddView(self.parent.app)
        response_data = smth_add.add(filter_params)
        fill_table_with_data([response_data], table.tableWidget)

    def modifySmthClickEvent(self, table, dialog_mod, get_smth_func, filter_values, modify_smth, SmthUpdateView):
        smth_id = int(table.comboBox.currentText()) if table.comboBox.currentText() != "---" else None

        if not smth_id:
            dialog_mod.exec()
            return

        update_values = get_smth_func(table)
        filter_values[0] = str(smth_id)

        modify_smth(SmthUpdateView, filter_values, update_values, self.parent)

    def modifySmthClickDialogEvent(
            self, table, dialog_form, get_smth_func, get_smth_filters, modify_smth, SmthUpdateView
    ):
        smth_id = int(table.comboBox.currentText()) if table.comboBox.currentText() != "---" else None

        update_values = get_smth_func(table)
        filter_values = get_smth_filters(dialog_form)
        filter_values[0] = str(smth_id) if smth_id is not None else None

        modify_smth(SmthUpdateView, filter_values, update_values, self.parent)

    def deleteSmthClickEvent(self, table, lines: tuple, SmthDeleteView, SmthGetView):
        delete_params = [line.text() if (line.text() != "") else None for line in lines]

        smth_get = SmthDeleteView(self.parent.app)
        response_data = smth_get.delete(delete_params)

        self.listSmthClickedEvent(
            table, SmthGetView, tuple(QLineEdit() for _ in lines)
        )

        set_up_info_dialog(
            self.parent.info_dialog, self.parent.info_form,
            response_data[0], response_data[1], response_data[2]
        )
