from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.ui.ui import Ui
from PyQt5.QtWidgets import QDialog, QLineEdit
from app.ui.ui import T1Form

from generated_uis.get_customers_table import UiFrame as TableGetCustomers
from generated_uis.add_customers_table import UiFrame as TableAddCustomers
from generated_uis.modify_customers_table import UiFrame as TableModCustomers
from generated_uis.del_customers_table import UiFrame as TableDelCustomers

from generated_uis.get_vendors_table import UiFrame as TableGetVendors
from generated_uis.add_vendors_table import UiFrame as TableAddVendors
from generated_uis.modify_vendors_table import UiFrame as TableModVendors
from generated_uis.del_vendors_table import UiFrame as TableDelVendors

from generated_uis.get_warehouses_table import UiFrame as TableGetWarehouses
from generated_uis.add_warehouses_table import UiFrame as TableAddWarehouses
from generated_uis.modify_warehouses_table import UiFrame as TableModWarehouses
from generated_uis.del_warehouses_table import UiFrame as TableDelWarehouses

from generated_uis.get_products_table import UiFrame as TableGetProducts
from generated_uis.add_products_table import UiFrame as TableAddProducts
from generated_uis.modify_products_table import UiFrame as TableModProducts
from generated_uis.del_products_table import UiFrame as TableDelProducts

from generated_uis.update_customers_dialog import UiDialog as DialogModCustomers
from generated_uis.update_vendors_dialog import UiDialog as DialogModVendors
from generated_uis.update_warehouses_dialog import UiDialog as DialogModWarehouses
from generated_uis.update_products_dialog import UiDialog as DialogModProducts
from generated_uis.update_categories_dialog import UiDialog as DialogModCategories

from app.entities.vendor.views import *
from app.entities.warehouse.views import *
from app.entities.product.views import *
from app.entities.customer.views import *
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
CUSTOMER_HANDLERS = [
    "ID клиента", "Наименование организации / ФИО", "Адрес клиента",
    "Электронная почта E-mail", "Контактный телефон",
]


class TableMaster:
    def __init__(self, parent_ui: "Ui", related_form: T1Form):
        self.parent = parent_ui
        self.base_form = related_form
        self.cur_table_widget_name = ""

        self.table_get_customer = TableGetCustomers()
        self.table_add_customer = TableAddCustomers()
        self.table_mod_customer = TableModCustomers()
        self.table_del_customer = TableDelCustomers()

        self.table_get_vendor = TableGetVendors()
        self.table_add_vendor = TableAddVendors()
        self.table_mod_vendor = TableModVendors()
        self.table_del_vendor = TableDelVendors()

        self.table_get_warehouse = TableGetWarehouses()
        self.table_add_warehouse = TableAddWarehouses()
        self.table_mod_warehouse = TableModWarehouses()
        self.table_del_warehouse = TableDelWarehouses()

        self.table_get_product = TableGetProducts()
        self.table_add_product = TableAddProducts()
        self.table_mod_product = TableModProducts()
        self.table_del_product = TableDelProducts()

        self.dialog_mod_customer = QDialog(self.parent)
        self.dialog_mod_customer_form = DialogModCustomers()
        self.dialog_mod_customer_form.setupUi(self.dialog_mod_customer)

        self.dialog_mod_vendor = QDialog(self.parent)
        self.dialog_mod_vendor_form = DialogModVendors()
        self.dialog_mod_vendor_form.setupUi(self.dialog_mod_vendor)

        self.dialog_mod_warehouse = QDialog(self.parent)
        self.dialog_mod_warehouse_form = DialogModWarehouses()
        self.dialog_mod_warehouse_form.setupUi(self.dialog_mod_warehouse)

        self.dialog_mod_product = QDialog(self.parent)
        self.dialog_mod_product_form = DialogModProducts()
        self.dialog_mod_product_form.setupUi(self.dialog_mod_product)

        self.dialog_mod_category = QDialog(self.parent)
        self.dialog_mod_category_form = DialogModCategories()
        self.dialog_mod_category_form.setupUi(self.dialog_mod_category)

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

    def spawn_get_customers_table(self):
        headers = CUSTOMER_HANDLERS
        self.spawn_table(self.table_get_customer, "customers_table", headers)

        func = lambda: add_combo_ids(self.table_get_customer.comboBox, self.parent.app.store.customers)
        func()
        keys = (self.table_get_customer.comboBox, )
        lines = (
            self.table_get_customer.lineEdit_4, self.table_get_customer.lineEdit_5,
            self.table_get_customer.lineEdit_6, self.table_get_customer.lineEdit_7,
        )
        self.table_get_customer.pushButton.clicked.connect(
            lambda: self.listSmthClickedEvent(self.table_get_customer.tableWidget, CustomerGetView, keys, lines, func)
        )

    def spawn_add_customers_table(self):
        headers = CUSTOMER_HANDLERS
        self.spawn_table(self.table_add_customer, "customers_table", headers)

        filter_lines = [
            self.table_add_customer.lineEdit_4, self.table_add_customer.lineEdit_5,
            self.table_add_customer.lineEdit_6, self.table_add_customer.lineEdit_7,
        ]

        self.table_add_customer.pushButton.clicked.connect(
            lambda: self.addSmthClickEvent(self.table_add_customer.tableWidget, CustomerAddView, filter_lines)
        )

    def spawn_mod_customers_table(self):
        headers = CUSTOMER_HANDLERS
        self.spawn_table(self.table_mod_customer, "customers_table", headers)

        func = lambda: add_combo_ids(self.table_mod_customer.comboBox, self.parent.app.store.customers)
        func()
        keys = (self.table_mod_customer.comboBox, )
        lines = (
            self.table_mod_customer.lineEdit_4, self.table_mod_customer.lineEdit_5,
            self.table_mod_customer.lineEdit_6, self.table_mod_customer.lineEdit_7,
        )
        self.table_mod_customer.pushButton.clicked.connect(
            lambda: self.listSmthClickedEvent(self.table_mod_customer.tableWidget, CustomerGetView, keys, lines, func)
        )

        filter_values = [None, None, None, None, None]
        self.dialog_mod_customer_form.pushButton.clicked.connect(
            lambda: self.modifySmthClickDialogEvent(
                self.table_mod_customer, self.table_mod_customer.comboBox, self.dialog_mod_customer_form,
                get_customers_update_values, get_customers_filter_values, modify_customers, CustomerUpdateView
            )
        )
        self.table_mod_customer.pushButton_2.clicked.connect(
            lambda: self.modifySmthClickEvent(
                self.table_mod_customer, self.table_mod_customer.comboBox, self.dialog_mod_customer,
                get_customers_update_values, filter_values, modify_customers, CustomerUpdateView
            )
        )

    def spawn_delete_customers_table(self):
        headers = CUSTOMER_HANDLERS
        self.spawn_table(self.table_del_customer, "customers_table", headers)

        func = lambda: add_combo_ids(self.table_del_customer.comboBox, self.parent.app.store.customers)
        func()
        keys = (self.table_del_customer.comboBox, )
        lines = (
            self.table_del_customer.lineEdit_4, self.table_del_customer.lineEdit_5,
            self.table_del_customer.lineEdit_6, self.table_del_customer.lineEdit_7,
        )
        self.listSmthClickedEvent(self.table_del_customer.tableWidget, CustomerGetView, keys, lines, func)
        self.table_del_customer.pushButton.clicked.connect(
            lambda: self.deleteSmthClickEvent(
                self.table_del_customer.tableWidget, keys, lines, CustomerDeleteView, CustomerGetView, func
            )
        )

    def spawn_get_vendors_table(self):
        headers = VENDOR_HANDLERS
        self.spawn_table(self.table_get_vendor, "vendors_table", headers)

        func = lambda: add_combo_ids(self.table_get_vendor.comboBox, self.parent.app.store.vendors)
        func()
        keys = (self.table_get_vendor.comboBox, )
        lines = (
            self.table_get_vendor.lineEdit_4, self.table_get_vendor.lineEdit_5,
            self.table_get_vendor.lineEdit_6, self.table_get_vendor.lineEdit_7,
        )
        self.table_get_vendor.pushButton.clicked.connect(
            lambda: self.listSmthClickedEvent(self.table_get_vendor.tableWidget, VendorGetView, keys, lines, func)
        )

    def spawn_add_vendors_table(self):
        headers = VENDOR_HANDLERS
        self.spawn_table(self.table_add_vendor, "vendors_table", headers)

        filter_lines = [
            self.table_add_vendor.lineEdit_4, self.table_add_vendor.lineEdit_5,
            self.table_add_vendor.lineEdit_6, self.table_add_vendor.lineEdit_7,
        ]

        self.table_add_vendor.pushButton.clicked.connect(
            lambda: self.addSmthClickEvent(self.table_add_vendor.tableWidget, VendorAddView, filter_lines)
        )

    def spawn_mod_vendors_table(self):
        headers = VENDOR_HANDLERS
        self.spawn_table(self.table_mod_vendor, "vendors_table", headers)

        func = lambda: add_combo_ids(self.table_mod_vendor.comboBox, self.parent.app.store.vendors)
        func()
        keys = (self.table_mod_vendor.comboBox, )
        lines = (
            self.table_mod_vendor.lineEdit_4, self.table_mod_vendor.lineEdit_5,
            self.table_mod_vendor.lineEdit_6, self.table_mod_vendor.lineEdit_7,
        )
        self.table_mod_vendor.pushButton.clicked.connect(
            lambda: self.listSmthClickedEvent(self.table_mod_vendor.tableWidget, VendorGetView, keys, lines, func)
        )

        filter_values = [None, None, None, None, None]
        self.dialog_mod_vendor_form.pushButton.clicked.connect(
            lambda: self.modifySmthClickDialogEvent(
                self.table_mod_vendor, self.table_mod_vendor.comboBox, self.dialog_mod_vendor_form,
                get_vendors_update_values, get_vendors_filter_values, modify_vendors, VendorUpdateView
            )
        )
        self.table_mod_vendor.pushButton_2.clicked.connect(
            lambda: self.modifySmthClickEvent(
                self.table_mod_vendor, self.table_mod_vendor.comboBox, self.dialog_mod_vendor,
                get_vendors_update_values, filter_values, modify_vendors, VendorUpdateView
            )
        )

    def spawn_delete_vendors_table(self):
        headers = VENDOR_HANDLERS
        self.spawn_table(self.table_del_vendor, "vendors_table", headers)

        func = lambda: add_combo_ids(self.table_del_vendor.comboBox, self.parent.app.store.vendors)
        func()
        keys = (self.table_del_vendor.comboBox, )
        lines = (
            self.table_del_vendor.lineEdit_4, self.table_del_vendor.lineEdit_5,
            self.table_del_vendor.lineEdit_6, self.table_del_vendor.lineEdit_7,
        )
        self.listSmthClickedEvent(self.table_del_vendor.tableWidget, VendorGetView, keys, lines, func)
        self.table_del_vendor.pushButton.clicked.connect(
            lambda: self.deleteSmthClickEvent(
                self.table_del_vendor.tableWidget, keys, lines, VendorDeleteView, VendorGetView, func
            )
        )

    def spawn_get_warehouse_table(self):
        headers = WAREHOUSE_HANDLERS
        self.spawn_table(self.table_get_warehouse, "warehouses_table", headers)

        func = lambda: add_combo_ids(self.table_get_warehouse.comboBox, self.parent.app.store.warehouses)
        func()
        keys = (self.table_get_warehouse.comboBox,)
        lines = (self.table_get_warehouse.lineEdit_4,)

        self.table_get_warehouse.pushButton.clicked.connect(
            lambda: self.listSmthClickedEvent(self.table_get_warehouse.tableWidget, WarehouseGetView, keys, lines, func)
        )

    def spawn_add_warehouses_table(self):
        headers = WAREHOUSE_HANDLERS
        self.spawn_table(self.table_add_warehouse, "warehouses_table", headers)

        filter_lines = [self.table_add_warehouse.lineEdit_4]

        self.table_add_warehouse.pushButton.clicked.connect(
            lambda: self.addSmthClickEvent(self.table_add_warehouse.tableWidget, WarehouseAddView, filter_lines)
        )

    def spawn_mod_warehouses_table(self):
        headers = WAREHOUSE_HANDLERS
        self.spawn_table(self.table_mod_warehouse, "warehouses_table", headers)

        func = lambda: add_combo_ids(self.table_mod_warehouse.comboBox, self.parent.app.store.warehouses)
        func()
        keys = (self.table_mod_warehouse.comboBox, )
        lines = (self.table_mod_warehouse.lineEdit_4,)
        self.table_mod_warehouse.pushButton.clicked.connect(
            lambda: self.listSmthClickedEvent(self.table_mod_warehouse.tableWidget, WarehouseGetView, keys, lines, func)
        )

        filter_values = [None, None]
        self.dialog_mod_warehouse_form.pushButton.clicked.connect(
            lambda: self.modifySmthClickDialogEvent(
                self.table_mod_warehouse, self.table_mod_warehouse.comboBox, self.dialog_mod_warehouse_form,
                get_warehouses_update_values, get_warehouses_filter_values, modify_warehouses, WarehouseUpdateView
            )
        )
        self.table_mod_warehouse.pushButton_2.clicked.connect(
            lambda: self.modifySmthClickEvent(
                self.table_mod_warehouse, self.table_mod_warehouse.comboBox, self.dialog_mod_warehouse,
                get_warehouses_update_values, filter_values, modify_warehouses, WarehouseUpdateView
            )
        )

    def spawn_del_warehouse_table(self):
        headers = WAREHOUSE_HANDLERS
        self.spawn_table(self.table_del_warehouse, "warehouses_table", headers)

        add_combo_ids(self.table_del_warehouse.comboBox, self.parent.app.store.warehouses)
        keys = (self.table_del_warehouse.comboBox,)
        lines = (self.table_del_warehouse.lineEdit_4,)
        self.listSmthClickedEvent(self.table_del_warehouse.tableWidget, WarehouseGetView, keys, lines)
        self.table_del_warehouse.pushButton.clicked.connect(
            lambda: self.deleteSmthClickEvent(
                self.table_del_warehouse.tableWidget, keys, lines, WarehouseDeleteView, WarehouseGetView,
                lambda: add_combo_ids(self.table_del_warehouse.comboBox, self.parent.app.store.warehouses)
            )
        )

    def spawn_get_product_table(self):
        headers = PRODUCT_HANDLERS
        self.spawn_table(self.table_get_product, "products_table", headers)
        headers = PR_CATEGORY_HANDLERS
        self.setup_extra_table(self.table_get_product.tableWidget_2, headers)

        product_lines = (
            self.table_get_product.lineEdit_3, self.table_get_product.lineEdit_4,
            self.table_get_product.lineEdit_5, self.table_get_product.lineEdit_6,
            self.table_get_product.lineEdit_7, self.table_get_product.lineEdit_8,
            self.table_get_product.lineEdit_9
        )
        self.table_get_product.pushButton.clicked.connect(
            lambda: self.listSmthClickedEvent(self.table_get_product.tableWidget, ProductGetView, product_lines)
        )
        category_lines = (self.table_get_product.lineEdit_10, self.table_get_product.lineEdit_11)
        self.table_get_product.pushButton_2.clicked.connect(
            lambda: self.listSmthClickedEvent(
                self.table_get_product.tableWidget_2, ProductCategoryGetView, category_lines
            )
        )

    def spawn_add_products_table(self):
        headers = PRODUCT_HANDLERS
        self.spawn_table(self.table_add_product, "products_table", headers)

        product_lines = [
            self.table_add_product.lineEdit_23, self.table_add_product.lineEdit_24,
            self.table_add_product.lineEdit_25, self.table_add_product.lineEdit_26,
            self.table_add_product.lineEdit_27, self.table_add_product.lineEdit_28,
        ]
        self.table_add_product.pushButton.clicked.connect(
            lambda: self.addSmthClickEvent(self.table_add_product.tableWidget, ProductAddView, product_lines)
        )

        category_lines = [self.table_add_product.lineEdit_29, ]
        headers = PR_CATEGORY_HANDLERS
        self.table_add_product.pushButton_4.clicked.connect(
            lambda: self.addSmthClickEvent(self.table_add_product.tableWidget_2, ProductCategoryAddView, category_lines)
        )
        self.setup_extra_table(self.table_add_product.tableWidget_2, headers)

    def spawn_mod_products_table(self):
        headers = PRODUCT_HANDLERS
        self.spawn_table(self.table_mod_product, "products_table", headers)

        product_lines = (
            None, self.table_mod_product.lineEdit_4, self.table_mod_product.lineEdit_5,
            self.table_mod_product.lineEdit_6, self.table_mod_product.lineEdit_7,
            self.table_mod_product.lineEdit_9, self.table_mod_product.lineEdit_12,
        )
        self.table_mod_product.comboBox.addItem("---")
        self.table_mod_product.pushButton.clicked.connect(
            lambda: self.listSmthClickedEvent(
                self.table_mod_product.tableWidget, ProductGetView,
                product_lines, lambda: add_combo_items(
                    self.table_mod_product.comboBox, self.table_mod_product.tableWidget
                )
            )
        )
        f_pr_values = [None, None, None, None, None, None, None]
        self.dialog_mod_product_form.pushButton.clicked.connect(
            lambda: self.modifySmthClickDialogEvent(
                self.table_mod_product, self.table_mod_product.comboBox, self.dialog_mod_product_form,
                get_products_update_values, get_products_filter_values, modify_products, ProductUpdateView
            )
        )
        self.table_mod_product.pushButton_2.clicked.connect(
            lambda: self.modifySmthClickEvent(
                self.table_mod_product, self.table_mod_product.comboBox, self.dialog_mod_product,
                get_products_update_values, f_pr_values, modify_products, ProductUpdateView
            )
        )

        #   #   #   #   #   #

        headers = PR_CATEGORY_HANDLERS
        categories_lines = (None, self.table_mod_product.lineEdit_14,)
        self.table_mod_product.comboBox_2.addItem("---")
        self.table_mod_product.pushButton_3.clicked.connect(
            lambda: self.listSmthClickedEvent(
                self.table_mod_product.tableWidget_2, ProductCategoryGetView,
                categories_lines, lambda: add_combo_items(
                    self.table_mod_product.comboBox_2, self.table_mod_product.tableWidget_2
                )
            )
        )
        f_c_values = [None, None]
        self.dialog_mod_category_form.pushButton.clicked.connect(
            lambda: self.modifySmthClickDialogEvent(
                self.table_mod_product, self.table_mod_product.comboBox_2, self.dialog_mod_category_form,
                get_categories_update_values, get_categories_filter_values, modify_categories, ProductCategoryUpdateView
            )
        )
        self.table_mod_product.pushButton_4.clicked.connect(
            lambda: self.modifySmthClickEvent(
                self.table_mod_product, self.table_mod_product.comboBox_2, self.dialog_mod_category,
                get_categories_update_values, f_c_values, modify_categories, ProductCategoryUpdateView
            )
        )
        self.setup_extra_table(self.table_mod_product.tableWidget_2, headers)

    def spawn_del_product_table(self):
        headers = PRODUCT_HANDLERS
        self.spawn_table(self.table_del_product, "products_table", headers)

        product_lines = (
            self.table_del_product.lineEdit_3, self.table_del_product.lineEdit_4,
            self.table_del_product.lineEdit_5, self.table_del_product.lineEdit_6,
            self.table_del_product.lineEdit_7, self.table_del_product.lineEdit_8,
            self.table_del_product.lineEdit_9,
        )
        self.listSmthClickedEvent(self.table_del_product.tableWidget, ProductGetView, product_lines)
        self.table_del_product.pushButton.clicked.connect(
            lambda: self.deleteSmthClickEvent(
                self.table_del_product.tableWidget, product_lines, ProductDeleteView, ProductGetView
            )
        )

        headers = PR_CATEGORY_HANDLERS
        category_lines = (self.table_del_product.lineEdit_10, self.table_del_product.lineEdit_11,)
        self.setup_extra_table(self.table_del_product.tableWidget_2, headers)
        self.listSmthClickedEvent(self.table_del_product.tableWidget_2, ProductCategoryGetView, category_lines)
        self.table_del_product.pushButton_2.clicked.connect(
            lambda: self.deleteSmthClickEvent(
                self.table_del_product.tableWidget_2, category_lines,
                ProductCategoryDeleteView, ProductCategoryGetView
            )
        )

    # EVENTS ------------------------------------------------------------------------------------------------

    def listSmthClickedEvent(self, table_widget: QTableWidget, SmthGetView, keys: tuple, lines: tuple, func=None):
        if table_widget.rowCount() > 0:
            clear_table_widget(table_widget)

        filter_params = [
            key.currentText() if (key is not None and key.currentText() != "---") else None for key in keys
        ]
        filter_params.extend([line.text() if (line is not None and line.text() != "") else None for line in lines])

        smth_get = SmthGetView(self.parent.app)
        response_data = smth_get.get(filter_params)

        fill_table_with_data(response_data, table_widget)

        if func:
            func()

    def addSmthClickEvent(self, table_widget: QTableWidget, SmthAddView, filter_lines):
        if table_widget.rowCount() > 0:
            clear_table_widget(table_widget)

        filter_params = [f_line.text() if (f_line.text() != "") else None for f_line in filter_lines]

        smth_add = SmthAddView(self.parent.app)
        response_data = smth_add.add(filter_params)
        fill_table_with_data([response_data], table_widget)

    def modifySmthClickEvent(
            self, table, combo_widget, dialog_mod, get_smth_func, filter_values, modify_smth, SmthUpdateView
    ):
        smth_id = int(combo_widget.currentText()) if combo_widget.currentText() != "---" else None

        if not smth_id:
            dialog_mod.exec()
            return

        update_values = get_smth_func(table)
        filter_values[0] = str(smth_id)

        modify_smth(SmthUpdateView, filter_values, update_values, self.parent)

    def modifySmthClickDialogEvent(
            self, table, combo_box, dialog_form, get_smth_func, get_smth_filters, modify_smth, SmthUpdateView
    ):
        smth_id = int(combo_box.currentText()) if combo_box.currentText() != "---" else None

        update_values = get_smth_func(table)
        filter_values = get_smth_filters(dialog_form)
        filter_values[0] = str(smth_id) if smth_id is not None else None

        modify_smth(SmthUpdateView, filter_values, update_values, self.parent)

    def deleteSmthClickEvent(
            self, table_widget: QTableWidget, keys: tuple, lines: tuple, SmthDeleteView, SmthGetView, refresh_keys
    ):
        delete_params = [key.currentText() if key.currentText() != "---" else None for key in keys]
        delete_params.extend([line.text() if (line.text() != "") else None for line in lines])

        smth_get = SmthDeleteView(self.parent.app)
        response_data = smth_get.delete(delete_params)

        self.listSmthClickedEvent(
            table_widget, SmthGetView, tuple(None for _ in keys), tuple(QLineEdit() for _ in lines)
        )
        refresh_keys()

        set_up_info_dialog(
            self.parent.info_dialog, self.parent.info_form,
            response_data[0], response_data[1], response_data[2]
        )
